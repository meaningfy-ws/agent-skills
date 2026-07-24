"""Integration test: the empirical Neo4j-Community constraint spike, made permanent.

This is task 1.2's permanent form of the task 1.1 spike (openspec/changes/archive/
linkml-neo4j-generators): rather than a one-off manual check whose result gets
hand-encoded as a comment (the exact anti-pattern that produced the original
generator's stale Enterprise-only assumption), the check is a real, repeatable
test against a real `neo4j:5.26-community` container.

Requires Docker. Skipped automatically if the Docker daemon isn't reachable —
this must NOT run as part of the default `make test` path (task 5.4); it's
opt-in via `pytest -m docker` or by running this file directly once Docker is
available.

NOTE: this test was written but never executed in the session that authored it
— the sandbox's Docker daemon was inactive and starting it needed a sudo
password unavailable there. Its assertions encode the *intended* verification;
run it for real before trusting its "passed" status, and update
gen_neo4j_constraints.py's module docstring + this file's TODO once it has.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

GENERATORS_DIR = Path(__file__).resolve().parents[1] / "tools/linkml_neo4j"
SYNTHETIC_SCHEMA = Path(__file__).resolve().parent / "fixtures/linkml/synthetic/library.yaml"

pytestmark = pytest.mark.docker


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _docker_available() -> bool:
    try:
        import docker

        docker.from_env().ping()
        return True
    except Exception:
        return False


requires_docker = pytest.mark.skipif(not _docker_available(), reason="Docker daemon not reachable")


@pytest.fixture(scope="module")
def neo4j_gen_module():
    return _load_module("gen_neo4j_constraints", GENERATORS_DIR / "gen_neo4j_constraints.py")


@pytest.fixture(scope="module")
def neo4j_driver():
    from testcontainers.neo4j import Neo4jContainer

    with Neo4jContainer(image="neo4j:5.26-community") as container:
        yield container.get_driver()


@requires_docker
class TestCommunityEditionConstraintSupport:
    """TODO(1.1/1.2): run this for real once Docker is available, then update
    gen_neo4j_constraints.py's module docstring with the actual result instead
    of "unverified"."""

    def test_uniqueness_constraint_accepted(self, neo4j_driver):
        with neo4j_driver.session() as session:
            session.run(
                "CREATE CONSTRAINT test_unique IF NOT EXISTS "
                "FOR (n:TestNode) REQUIRE n.key IS UNIQUE"
            )
            result = session.run("SHOW CONSTRAINTS YIELD name WHERE name = 'test_unique' RETURN name")
            assert result.single() is not None

    def test_property_existence_constraint(self, neo4j_driver):
        """The open question: does Community 5.26 accept this, or does it still need Enterprise?"""
        with neo4j_driver.session() as session:
            try:
                session.run(
                    "CREATE CONSTRAINT test_exists IF NOT EXISTS "
                    "FOR (n:TestNode2) REQUIRE n.prop IS NOT NULL"
                )
            except Exception as exc:  # noqa: BLE001 — recording the boundary, not hiding it
                pytest.skip(f"Community rejected property existence constraint: {exc}")
            result = session.run("SHOW CONSTRAINTS YIELD name WHERE name = 'test_exists' RETURN name")
            assert result.single() is not None

    def test_property_type_constraint(self, neo4j_driver):
        with neo4j_driver.session() as session:
            try:
                session.run(
                    "CREATE CONSTRAINT test_type IF NOT EXISTS "
                    "FOR (n:TestNode3) REQUIRE n.prop IS :: STRING"
                )
            except Exception as exc:  # noqa: BLE001
                pytest.skip(f"Community rejected property type constraint: {exc}")
            result = session.run("SHOW CONSTRAINTS YIELD name WHERE name = 'test_type' RETURN name")
            assert result.single() is not None

    def test_list_typed_property_constraint(self, neo4j_driver):
        with neo4j_driver.session() as session:
            try:
                session.run(
                    "CREATE CONSTRAINT test_list_type IF NOT EXISTS "
                    "FOR (n:TestNode4) REQUIRE n.prop IS :: LIST<STRING>"
                )
            except Exception as exc:  # noqa: BLE001
                pytest.skip(f"Community rejected list-typed property constraint: {exc}")
            result = session.run(
                "SHOW CONSTRAINTS YIELD name WHERE name = 'test_list_type' RETURN name"
            )
            assert result.single() is not None

    def test_node_key_constraint(self, neo4j_driver):
        with neo4j_driver.session() as session:
            try:
                session.run(
                    "CREATE CONSTRAINT test_node_key IF NOT EXISTS "
                    "FOR (n:TestNode5) REQUIRE (n.a, n.b) IS NODE KEY"
                )
            except Exception as exc:  # noqa: BLE001
                pytest.skip(f"Community rejected NODE KEY constraint: {exc}")
            result = session.run(
                "SHOW CONSTRAINTS YIELD name WHERE name = 'test_node_key' RETURN name"
            )
            assert result.single() is not None


@requires_docker
class TestGeneratedCommunityProfileAppliesCleanly:
    """The generated `--profile community` Cypher must apply without error, and
    actually enforce what it claims (a violating write is rejected)."""

    def test_community_profile_applies_without_error(self, neo4j_driver, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA), profile="community")
        statements = [s.strip() for s in gen.serialize().split(";") if s.strip() and "//" not in s.split("\n")[0]]
        with neo4j_driver.session() as session:
            for statement in statements:
                session.run(statement)

    def test_uniqueness_is_actually_enforced(self, neo4j_driver, neo4j_gen_module):
        gen = neo4j_gen_module.Neo4jConstraintGenerator(str(SYNTHETIC_SCHEMA), profile="community")
        statements = [s.strip() for s in gen.serialize().split(";") if s.strip() and "//" not in s.split("\n")[0]]
        with neo4j_driver.session() as session:
            for statement in statements:
                session.run(statement)
            session.run("CREATE (:Book {id: 'b-1'})")
            with pytest.raises(Exception):  # noqa: PT011 — driver-specific constraint-violation type
                session.run("CREATE (:Book {id: 'b-1'})")
