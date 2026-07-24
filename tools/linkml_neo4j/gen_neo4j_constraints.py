#!/usr/bin/env python3
"""Neo4j constraint generator, built on the LinkML ``Generator`` infrastructure.

Subclasses ``linkml.utils.generator.Generator`` so it reuses the standard schema
loading, import resolution, ``SchemaView`` access, and the shared ``gen-*`` CLI
(``--format``, ``--stacktrace``, version handling) — identical in shape to
``gen-owl`` / ``gen-shacl``.

Emits only the constraints Neo4j can actually enforce, derived unambiguously
from LinkML (SHACL is a poor source — it has no uniqueness):

  identifier slot           -> uniqueness constraint      (Community)
  required scalar/enum      -> existence constraint       (assumed Enterprise;
                                unverified — see below)
  typed scalar/enum         -> property-type constraint   (assumed Enterprise;
                                unverified — see below)
  required multivalued      -> existence constraint too — Neo4j's existence
  scalar/enum                  check is on property-key presence, regardless
                                of whether the stored value is a scalar or a
                                list, so there is no reason to skip it
  annotated slot                -> index (`neo4j_index: true` in the slot's
  (`neo4j_index: true`)         `annotations`) — indexes are not edition-gated

Mapping rules (mirror the linkml-store Neo4j mapping documented in the Makefile):
  * concrete class = a :Label node, identifier or not — a value object with no
    natural key (e.g. a composed value like Dimensions/GeoCoordinates) still
    gets a label and existence/type constraints on its own properties; it just
    gets no uniqueness constraint, since there is no natural key to be unique on
    (this makes the Cypher and neomodel generators agree on what is a node —
    neomodel already promotes every concrete class, keyed or not)
  * abstract class = never instantiated -> skipped (concrete subclasses carry
    their own inherited ``id`` and get constraints individually)
  * object-valued slot (range is a class) -> a relationship, not a node property
    -> skipped (this generator emits no relationship-level constraints; Neo4j has
    no native "at least one relationship of type X" constraint at all, and none
    of this schema's relationships carry their own properties, so relationship
    property existence/type constraints have nothing to attach to yet)

Community vs Enterprise: the ``profile`` option controls what's emitted.
``community`` emits only uniqueness constraints and indexes — the subset this
generator can currently *prove* runs on Neo4j Community Edition. ``full`` (the
default) additionally emits existence and property-type constraints, carried
over from this generator's original assumption that they need Enterprise. That
assumption has NOT been empirically re-verified against a real Neo4j Community
instance (openspec/changes/archive/linkml-neo4j-generators, tasks 1.1/1.2/5.3 —
blocked on Docker access when this generator was last touched). Treat ``full``
as the reference/aspirational output and ``community`` as the only profile
currently safe to apply blind to a Community deployment, until that spike runs
for real and this comment is updated with its result.

Usage:  python gen_neo4j_constraints.py schema.yaml [--profile community|full]
   or:  gen-neo4j-constraints schema.yaml --profile community   (once installed)
"""
from __future__ import annotations

from dataclasses import dataclass, field

import click
from linkml.utils.generator import Generator, shared_arguments

# LinkML scalar range -> Neo4j property type (for `IS :: <TYPE>` constraints).
NEO4J_TYPES = {
    "string": "STRING",
    "uriorcurie": "STRING",
    "uri": "STRING",
    "curie": "STRING",
    "ncname": "STRING",
    "integer": "INTEGER",
    "float": "FLOAT",
    "double": "FLOAT",
    "decimal": "FLOAT",
    "boolean": "BOOLEAN",
    "date": "DATE",
    "datetime": "DATETIME",
    "time": "LOCAL_TIME",
}

PROFILES = ("community", "full")


def _index_annotation(slot) -> bool:
    """True iff the slot carries a truthy ``neo4j_index`` annotation."""
    ann = getattr(slot.annotations, "neo4j_index", None)
    return bool(ann.value) if ann is not None else False


@dataclass
class Neo4jConstraintGenerator(Generator):
    """Generate Neo4j constraint DDL (Cypher) for the enforceable LinkML subset."""

    generatorname = "gen-neo4j-constraints"
    generatorversion = "2.0.0"
    valid_formats = ["cypher"]
    file_extension = "cypher"
    uses_schemaloader = False  # we drive everything through self.schemaview

    profile: str = field(default="full")

    def __post_init__(self, *args, **kwargs):
        if self.profile not in PROFILES:
            raise ValueError(f"profile must be one of {PROFILES}, got {self.profile!r}")
        super().__post_init__(*args, **kwargs)

    def _is_node_label(self, class_name: str) -> bool:
        """A class becomes a Neo4j `:Label` iff it is concrete.

        No longer requires an identifier slot: a value object with no natural key
        (e.g. a composed value like ``Dimensions``/``GeoCoordinates``) is still
        promoted to a real node by the neomodel generator's mapping, so the two
        generators should agree it's a label. Existence/type constraints don't
        depend on uniqueness — only the uniqueness constraint itself is
        conditional on there actually being an identifier slot to be unique on
        (see ``_class_constraints``).
        """
        cls = self.schemaview.get_class(class_name)
        return not cls.abstract

    @staticmethod
    def _neo4j_type(range_: str | None) -> str:
        """Neo4j property type for a scalar/enum range (enums store as STRING)."""
        return NEO4J_TYPES.get(range_ or "string", "STRING")

    def _class_constraints(self, class_name: str) -> list[str]:
        sv = self.schemaview
        label = class_name
        id_slot = sv.get_identifier_slot(class_name)  # may be None — value object, no natural key
        class_names = set(sv.all_classes())
        full = self.profile == "full"

        out = [f"// ---- {label} " + "-" * max(0, 68 - len(label))]

        # Identifier -> uniqueness (Community). NODE KEY (unique+exists) is the
        # Enterprise upgrade; noted rather than emitted so this runs on Community.
        # Only emitted when the class actually has a natural key.
        if id_slot is not None:
            p = id_slot.name
            out.append(
                f"CREATE CONSTRAINT {label.lower()}_{p}_unique IF NOT EXISTS\n"
                f"FOR (n:`{label}`) REQUIRE n.`{p}` IS UNIQUE;"
                "  // NODE KEY on Enterprise"
            )

        for slot in sv.class_induced_slots(class_name):
            if id_slot is not None and slot.name == id_slot.name:
                continue
            if slot.range in class_names:  # object-valued -> relationship
                continue
            p = slot.name

            # Existence: checks property-key presence regardless of scalar vs
            # list storage, so multivalued is no reason to skip this one.
            if full and slot.required:
                out.append(
                    f"CREATE CONSTRAINT {label.lower()}_{p}_exists IF NOT EXISTS\n"
                    f"FOR (n:`{label}`) REQUIRE n.`{p}` IS NOT NULL;"
                    "  // Enterprise (unverified on Community — see module docstring)"
                )

            # Property-type: skipped for multivalued for now — a list-typed
            # constraint (`IS :: LIST<STRING>`) needs its own Community check,
            # not assumed correct just because scalar existence is safe to add.
            if full and not slot.multivalued:
                out.append(
                    f"CREATE CONSTRAINT {label.lower()}_{p}_type IF NOT EXISTS\n"
                    f"FOR (n:`{label}`) REQUIRE n.`{p}` IS :: {self._neo4j_type(slot.range)};"
                    "  // Enterprise (unverified on Community — see module docstring)"
                )

            if _index_annotation(slot):
                out.append(
                    f"CREATE INDEX {label.lower()}_{p}_idx IF NOT EXISTS "
                    f"FOR (n:`{label}`) ON (n.`{p}`);"
                )
        return out

    def serialize(self, **kwargs) -> str:
        sv = self.schemaview
        header = [
            f"// Neo4j constraints generated from {self.schema.name}",
            "// DO NOT EDIT — regenerate with `make neo4j-constraints`.",
            f"// Profile: {self.profile}.",
            (
                "// Uniqueness and indexes are Community-safe. Existence/type constraints are"
                if self.profile == "full"
                else "// Uniqueness and indexes only — the Community-safe subset."
            ),
        ]
        if self.profile == "full":
            header.append(
                "// carried over unverified (see module docstring); omitted from --profile community."
            )
        header.append("")
        body = [
            "\n".join(self._class_constraints(cn))
            for cn in sorted(sv.all_classes())
            if self._is_node_label(cn)
        ]
        return "\n".join(header) + "\n\n".join(body) + "\n"


@shared_arguments(Neo4jConstraintGenerator)
@click.command(name="gen-neo4j-constraints")
@click.option(
    "--profile",
    type=click.Choice(PROFILES),
    default="full",
    help="community = uniqueness + indexes only (Community-safe); full = also existence/type.",
)
@click.version_option(Neo4jConstraintGenerator.generatorversion, "-V", "--version")
def cli(yamlfile, profile, **kwargs):
    """Generate Neo4j constraint DDL from a LinkML schema."""
    gen = Neo4jConstraintGenerator(yamlfile, profile=profile, **kwargs)
    print(gen.serialize())


if __name__ == "__main__":
    cli()
