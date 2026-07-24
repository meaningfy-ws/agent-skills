"""Unit tests for the vendored Neo4j-targeting LinkML generators.

Covers openspec/changes/archive/linkml-neo4j-generators tasks 5.1 (synthetic fixture)
and 5.2 (vendored hulubul-broker fixture). No Docker/Neo4j required — these tests only
exercise the generators' Python string output. See test_linkml_neo4j_integration.py for
the Docker-gated real-database check.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

GENERATORS_DIR = Path(__file__).resolve().parents[1] / "tools/linkml_neo4j"
SYNTHETIC_SCHEMA = Path(__file__).resolve().parent / "fixtures/linkml/synthetic/library.yaml"
HULUBUL_SCHEMA = Path(__file__).resolve().parent / "fixtures/linkml/hulubul/hulubul.yaml"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def neo4j_gen_module():
    return _load_module("gen_neo4j_constraints", GENERATORS_DIR / "gen_neo4j_constraints.py")


@pytest.fixture(scope="module")
def neomodel_gen_module():
    return _load_module("gen_neomodel", GENERATORS_DIR / "gen_neomodel.py")


# ---------------------------------------------------------------------------
# gen_neo4j_constraints — synthetic fixture
# ---------------------------------------------------------------------------


class TestNeo4jConstraintsSynthetic:
    def test_required_multivalued_scalar_gets_existence_constraint(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "book_authorNames_exists" in out
        assert "FOR (n:`Book`) REQUIRE n.`authorNames` IS NOT NULL" in out

    def test_required_multivalued_enum_gets_existence_constraint(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "loan_returnCondition_exists" in out
        assert "FOR (n:`Loan`) REQUIRE n.`returnCondition` IS NOT NULL" in out

    def test_community_profile_is_uniqueness_only(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA), profile="community")
        out = gen.serialize()
        assert "IS UNIQUE" in out
        assert "IS NOT NULL" not in out
        assert "IS ::" not in out

    def test_full_profile_includes_existence_and_type(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA), profile="full")
        out = gen.serialize()
        assert "IS NOT NULL" in out
        assert "IS ::" in out

    def test_default_profile_is_full(self, neo4j_gen_module):
        default_out = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA)).serialize()
        full_out = neo4j_gen_module.Neo4jConstraintGenerator(
            str(SYNTHETIC_SCHEMA), profile="full"
        ).serialize()
        assert default_out == full_out

    def test_annotated_slot_emits_index(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "CREATE INDEX book_isbn_idx IF NOT EXISTS FOR (n:`Book`) ON (n.`isbn`)" in out

    def test_unannotated_slot_gets_no_index(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "CREATE INDEX" not in out.replace(
            "CREATE INDEX book_isbn_idx IF NOT EXISTS FOR (n:`Book`) ON (n.`isbn`);", ""
        )

    def test_community_profile_still_emits_indexes(self, neo4j_gen_module):
        # Indexes are not a constraint kind gated by edition — Community supports them.
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA), profile="community")
        out = gen.serialize()
        assert "CREATE INDEX book_isbn_idx" in out

    def test_relationship_slots_still_skipped(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "borrowedItem" not in out
        assert "partOf" not in out

    def test_value_object_without_identifier_still_gets_property_constraints(self, neo4j_gen_module):
        # Dimensions has no `id` slot but neomodel already promotes it to a real
        # node — the Cypher side should agree it's a label and constrain its
        # required scalar properties, just with no uniqueness constraint (there
        # is no natural key to be unique on).
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA), profile="full")
        out = gen.serialize()
        assert "dimensions_widthCm_exists" in out
        assert "dimensions_heightCm_exists" in out
        assert "dimensions_id_unique" not in out
        assert "FOR (n:`Dimensions`) REQUIRE n.`id`" not in out


# ---------------------------------------------------------------------------
# gen_neomodel — synthetic fixture
# ---------------------------------------------------------------------------


class TestNeomodelSynthetic:
    def test_abstract_class_becomes_abstract_node_base(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "class Media(StructuredNode):" in out
        media_block = out.split("class Media(StructuredNode):")[1].split("\n\n\nclass ")[0]
        assert "__abstract_node__ = True" in media_block

    def test_concrete_subclasses_inherit_from_abstract_base(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "class Book(Media):" in out
        assert "class DVD(Media):" in out

    def test_inherited_slots_not_redeclared_on_subclass(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        book_block = out.split("class Book(Media):")[1].split("\n\n\nclass ")[0]
        # id and name are declared on Media; Book must not redeclare them.
        assert "id = StringProperty" not in book_block
        assert "name = StringProperty" not in book_block
        assert "isbn = StringProperty" in book_block  # Book's own slot still present

    def test_relationship_to_abstract_range_resolves_to_real_class(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "RelationshipTo('Media', 'BORROWED_ITEM'" in out
        # And Media is actually defined as a class (the bug: it wasn't, before).
        assert "class Media(StructuredNode):" in out

    def test_any_of_restriction_is_documented(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        loan_block = out.split("class Loan(StructuredNode):")[1].split("\n\n\nclass ")[0]
        assert "Book" in loan_block and "DVD" in loan_block  # restriction named in a comment

    def test_value_object_without_identifier_is_still_a_node(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        assert "class Dimensions(StructuredNode):" in out

    def test_self_referencing_relationship(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        category_block = out.split("class Category(StructuredNode):")[1].split("\n\n\nclass ")[0]
        assert "RelationshipTo('Category'" in category_block

    def test_slot_usage_cardinality_override(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA))
        out = gen.serialize()
        category_block = out.split("class Category(StructuredNode):")[1].split("\n\n\nclass ")[0]
        shelf_block = out.split("class Shelf(StructuredNode):")[1].split("\n\n\nclass ")[0]
        assert "cardinality=ZeroOrOne" in category_block  # partOf optional on Category
        assert "cardinality=One" in shelf_block  # partOf required on Shelf


# ---------------------------------------------------------------------------
# Both generators — vendored real-world hulubul-broker fixture (task 5.2)
# ---------------------------------------------------------------------------


class TestHulubulFixtureRegression:
    """Confirms the two originally-confirmed bugs no longer reproduce on the real schema."""

    def test_neomodel_generates_without_error(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(HULUBUL_SCHEMA))
        out = gen.serialize()
        assert "class SpatialObject(StructuredNode):" in out
        assert "class AgentInRole(StructuredNode):" in out

    def test_previously_broken_relationship_targets_now_resolve(self, neomodel_gen_module):
        gen = neomodel_gen_module.NeomodelGenerator(str(HULUBUL_SCHEMA))
        out = gen.serialize()
        # SpatialObject and AgentInRole must now actually be defined classes.
        assert "class SpatialObject(StructuredNode):" in out
        assert "class AgentInRole(StructuredNode):" in out
        # And the concrete subclasses must inherit from them, not stand alone.
        assert "class Address(SpatialObject):" in out
        assert "class Area(SpatialObject):" in out
        assert "class Place(SpatialObject):" in out
        assert "class Sender(AgentInRole):" in out
        assert "class Receiver(AgentInRole):" in out
        assert "class Transporter(AgentInRole):" in out

    def test_neo4j_constraints_generates_without_error(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(HULUBUL_SCHEMA))
        out = gen.serialize()
        assert "CREATE CONSTRAINT" in out

    def test_previously_skipped_multivalued_required_now_constrained(self, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(HULUBUL_SCHEMA))
        out = gen.serialize()
        # TransportService.serviceType: multivalued + required enum — was silently skipped.
        assert "transportservice_serviceType_exists" in out


# ---------------------------------------------------------------------------
# The generated neomodel code must actually BE valid neomodel, not just look
# right as a string — this is how the `id`/reserved-attribute-name bug (a
# THIRD real bug, undiscovered by reading code, found only by actually
# importing the generator's own output) was caught. No Docker/live database
# needed: neomodel registers StructuredNode classes at class-definition time,
# with no connection required.
# ---------------------------------------------------------------------------


def _exec_generated_module(source: str, module_name: str):
    import types

    module = types.ModuleType(module_name)
    exec(compile(source, f"<generated:{module_name}>", "exec"), module.__dict__)
    return module


class TestNeomodelGeneratedCodeIsRealNeomodel:
    def test_synthetic_fixture_imports_and_registers(self, neomodel_gen_module):
        source = neomodel_gen_module.NeomodelGenerator(str(SYNTHETIC_SCHEMA)).serialize()
        module = _exec_generated_module(source, "library_ogm_generated")
        assert {c.__name__ for c in module.Media.__subclasses__()} == {"Book", "DVD"}
        # The reserved-name rename: attribute is `id_`, but the real Neo4j
        # property key is preserved as `id` via db_property.
        assert module.Book.id_.db_property == "id"

    def test_hulubul_fixture_imports_and_registers(self, neomodel_gen_module):
        source = neomodel_gen_module.NeomodelGenerator(str(HULUBUL_SCHEMA)).serialize()
        module = _exec_generated_module(source, "hulubul_ogm_generated")
        assert {c.__name__ for c in module.SpatialObject.__subclasses__()} == {
            "Address",
            "Area",
            "Place",
        }
        assert {c.__name__ for c in module.AgentInRole.__subclasses__()} == {
            "Sender",
            "Receiver",
            "Transporter",
        }
        # The relationships that pointed at an undefined class name before the
        # fix now resolve to real, defined, registered classes.
        assert module.DeliveryRequest.hasPickUpLocation is not None
        assert module.Feedback.fromProvider is not None
