#!/usr/bin/env python3
"""neomodel OGM generator, built on the LinkML ``Generator`` infrastructure.

Subclasses ``linkml.utils.generator.Generator`` (like ``gen_neo4j_constraints``)
so it reuses schema loading, import resolution, ``SchemaView`` and the shared
``gen-*`` CLI. Renders neomodel ``StructuredNode`` classes with a Jinja2 template.

Mapping to neomodel:
  * a class with no ``is_a``      -> direct ``StructuredNode`` subclass
  * a class with ``is_a: Parent`` -> subclasses the generated ``Parent`` class in
    real Python (mirrors the LinkML hierarchy) — each class renders only its own
    *directly declared* slots; inherited slots come down through Python
    inheritance, not by being redeclared
  * abstract class                -> still generated, as ``__abstract_node__ = True``
    (neomodel's own polymorphic-node marker) — this is what makes a relationship
    whose range is an abstract class resolve correctly: neomodel looks the target
    up by name in its class registry, and the abstract base is now a real,
    registered class with real, registered concrete subclasses, instead of a
    name that was never defined at all
  * identifier slot               -> ``StringProperty(unique_index=True, required=True)`` —
    renamed to ``id_`` when the schema's identifier slot is literally called
    ``id`` (LinkML's own convention, used by every fixture this generator is
    tested against), since neomodel reserves ``id``/``deleted``/``element_id``
    as Python attribute names and raises at class-definition time otherwise;
    the actual Neo4j property key is preserved via ``db_property=...``
  * scalar slot                   -> typed ``*Property`` (``required=True`` if required)
  * enum slot                     -> ``StringProperty(choices=...)``
  * multivalued scalar/enum       -> ``ArrayProperty(<inner>)``
  * object-valued slot            -> ``RelationshipTo(target, 'REL_NAME', cardinality=...)``
  * ``any_of``-restricted range   -> the relationship still points at the (now real)
    abstract/base target; the restriction to specific subclasses is noted in a
    trailing comment, not mechanically enforced (neomodel has no union-of-
    subclasses relationship constraint, and this generator does not add
    application-layer validation to fill that gap — see the parent EPIC's DEC-2)

Divergence from the linkml-store mapping: neomodel has no inlining, so value objects
(e.g. GeoCoordinates, no id) also become StructuredNodes and are reached by a
relationship rather than embedded. Noted in the generated header.

Usage:  python gen_neomodel.py schema.yaml
   or:  gen-neomodel schema.yaml   (once installed)
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import click
from jinja2 import Template
from linkml.utils.generator import Generator, shared_arguments

# LinkML scalar range -> neomodel property class.
NEOMODEL_PROP = {
    "string": "StringProperty",
    "uri": "StringProperty",
    "uriorcurie": "StringProperty",
    "curie": "StringProperty",
    "ncname": "StringProperty",
    "time": "StringProperty",  # neomodel has no time-only property
    "integer": "IntegerProperty",
    "float": "FloatProperty",
    "double": "FloatProperty",
    "decimal": "FloatProperty",
    "boolean": "BooleanProperty",
    "date": "DateProperty",
    "datetime": "DateTimeProperty",
}

_TEMPLATE = Template(
    '''"""neomodel OGM classes generated from {{ schema_name }}.

DO NOT EDIT — regenerate with `make neomodel`.
Value objects (no identifier) are modelled as StructuredNodes reached by a
relationship: neomodel has no inlining. Abstract LinkML classes are generated as
`__abstract_node__ = True` bases with real Python inheritance to their concrete
subclasses, so relationships targeting an abstract class resolve correctly.
"""
from neomodel import (
    StructuredNode,
    StringProperty, IntegerProperty, FloatProperty, BooleanProperty,
    DateProperty, DateTimeProperty, ArrayProperty,
    RelationshipTo, ZeroOrMore, ZeroOrOne, OneOrMore, One,
)


{% for c in classes %}
class {{ c.name }}({{ c.base }}):
    """{{ c.doc }}"""
{% if c.abstract %}
    __abstract_node__ = True
{% endif %}
{% for line in c.lines %}
    {{ line }}
{% endfor %}
{% if not c.lines and not c.abstract %}
    pass
{% endif %}


{% endfor %}''',
    trim_blocks=True,
    lstrip_blocks=True,
)


def _rel_name(slot_name: str) -> str:
    """camelCase slot -> UPPER_SNAKE relationship type (providesService -> PROVIDES_SERVICE)."""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", slot_name).upper()


def _cardinality(required: bool, multivalued: bool) -> str:
    if multivalued:
        return "OneOrMore" if required else "ZeroOrMore"
    return "One" if required else "ZeroOrOne"


def _any_of_targets(slot) -> list[str]:
    """The concrete ranges an ``any_of``-restricted slot is actually limited to."""
    return [expr.range for expr in (slot.any_of or []) if expr.range]


# neomodel raises ValueError at class-definition time if a StructuredNode declares
# a Python attribute with any of these names — they collide with neomodel/Neo4j
# internals. `id` is also LinkML's own conventional identifier-slot name (used by
# both fixtures this generator is tested against), so this is not a hypothetical
# edge case — every schema following that convention hits it.
RESERVED_NEOMODEL_ATTRS = {"id", "deleted", "element_id"}


def _safe_attr_name(slot_name: str) -> str:
    """A Python attribute name that avoids neomodel's reserved names.

    The underlying Neo4j property key is preserved via ``db_property=...`` (see
    ``_property_line``) whenever the attribute name had to change — this is a
    Python-attribute-only rename, so the graph property (and the Cypher
    constraint generator's own property references) are unaffected.
    """
    return f"{slot_name}_" if slot_name in RESERVED_NEOMODEL_ATTRS else slot_name


@dataclass
class NeomodelGenerator(Generator):
    """Generate neomodel OGM classes for the LinkML entity/value-object classes."""

    generatorname = "gen-neomodel"
    generatorversion = "2.0.0"
    valid_formats = ["python"]
    file_extension = "py"
    uses_schemaloader = False

    def _choices_arg(self, enum_name: str) -> str:
        pv = self.schemaview.get_enum(enum_name).permissible_values
        pairs = ", ".join(f"({v!r}, {v!r})" for v in pv)
        return f"choices=({pairs},)"

    def _property_line(self, slot, id_name: str | None) -> str:
        name = slot.name
        attr = _safe_attr_name(name)
        db_property_kw = f"db_property={name!r}" if attr != name else None

        if name == id_name:
            args = ["unique_index=True", "required=True"]
            if db_property_kw:
                args.append(db_property_kw)
            return f"{attr} = StringProperty({', '.join(args)})"

        is_enum = slot.range in self.schemaview.all_enums()
        base = "StringProperty" if is_enum else NEOMODEL_PROP.get(slot.range, "StringProperty")
        inner_args = [self._choices_arg(slot.range)] if is_enum else []

        if slot.multivalued:
            inner = f"{base}({', '.join(inner_args)})"
            outer_args = []
            if slot.required:
                outer_args.append("required=True")
            if db_property_kw:
                outer_args.append(db_property_kw)
            outer = f", {', '.join(outer_args)}" if outer_args else ""
            return f"{attr} = ArrayProperty({inner}{outer})"

        args = list(inner_args)
        if slot.required:
            args.append("required=True")
        if db_property_kw:
            args.append(db_property_kw)
        return f"{attr} = {base}({', '.join(args)})"

    def _relationship_line(self, slot) -> str:
        card = _cardinality(bool(slot.required), bool(slot.multivalued))
        line = (
            f"{slot.name} = RelationshipTo('{slot.range}', "
            f"'{_rel_name(slot.name)}', cardinality={card})"
        )
        targets = _any_of_targets(slot)
        if targets:
            line += f"  # restricted to: {', '.join(targets)} (not mechanically enforced)"
        return line

    def _direct_slots(self, class_name: str):
        """Slots declared *directly* on this class — not inherited ones.

        Inherited slots come down through the generated Python inheritance
        instead (see ``serialize``'s topological ordering), so re-emitting them
        here would just redeclare what the parent class already provides.
        """
        sv = self.schemaview
        return [sv.induced_slot(name, class_name) for name in sv.class_slots(class_name, direct=True)]

    def _class_dict(self, class_name: str) -> dict:
        sv = self.schemaview
        class_names = set(sv.all_classes())
        cls = sv.get_class(class_name)
        id_slot = sv.get_identifier_slot(class_name)
        # Only treat the identifier specially if THIS class declares it directly
        # (i.e. it isn't inherited from a base that already renders it).
        own_slot_names = {s.name for s in self._direct_slots(class_name)}
        id_name = id_slot.name if id_slot and id_slot.name in own_slot_names else None

        lines = []
        for slot in self._direct_slots(class_name):
            if slot.range in class_names:
                lines.append(self._relationship_line(slot))
            else:
                lines.append(self._property_line(slot, id_name))

        doc = " ".join((cls.description or class_name).split())
        return {
            "name": class_name,
            "doc": doc,
            "lines": lines,
            "abstract": bool(cls.abstract),
            "base": cls.is_a if cls.is_a else "StructuredNode",
        }

    def _parents_first_order(self, class_names: set[str]) -> list[str]:
        """Topological order (parent before child) so Python class bodies compile."""
        sv = self.schemaview
        ordered: list[str] = []
        visited: set[str] = set()

        def visit(name: str) -> None:
            if name in visited or name not in class_names:
                return
            visited.add(name)
            parent = sv.get_class(name).is_a
            if parent:
                visit(parent)
            ordered.append(name)

        for name in sorted(class_names):
            visit(name)
        return ordered

    def serialize(self, **kwargs) -> str:
        sv = self.schemaview
        class_names = set(sv.all_classes())
        classes = [self._class_dict(cn) for cn in self._parents_first_order(class_names)]
        return _TEMPLATE.render(schema_name=self.schema.name, classes=classes)


@shared_arguments(NeomodelGenerator)
@click.command(name="gen-neomodel")
@click.version_option(NeomodelGenerator.generatorversion, "-V", "--version")
def cli(yamlfile, **kwargs):
    """Generate neomodel OGM classes from a LinkML schema."""
    gen = NeomodelGenerator(yamlfile, **kwargs)
    print(gen.serialize())


if __name__ == "__main__":
    cli()
