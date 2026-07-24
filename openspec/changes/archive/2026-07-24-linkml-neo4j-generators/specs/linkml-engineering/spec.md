## ADDED Requirements

### Requirement: Tested Neo4j-targeting custom generators, referenced not vendored
The catalogue SHALL provide two custom LinkML generators — a Neo4j Cypher-constraint generator and
a neomodel OGM generator — as tested repo tooling under `tools/linkml_neo4j/`, each built on
LinkML's `Generator` base class per the existing custom-generator mechanism. Per the skill-repo
governance rule that a Skill is reusable knowledge, not a maintained/tested codebase, the
generators SHALL NOT live inside `skills/linkml-engineering/`; the `linkml-engineering` skill SHALL
document and cite them (in `references/generation-and-templates.md`) without owning them — the same
"referenced, not vendored" pattern already used for the OpenSpec schema pin at
`openspec/schemas/meaningfy/`. Both generators SHALL resolve relationship targets correctly when
the LinkML range is an abstract class, by mirroring the schema's `is_a` hierarchy as real
inheritance in generated code rather than producing a reference to an undefined class. The Cypher
generator SHALL emit only constraint and index forms verified to work on Neo4j Community Edition,
SHALL emit existence constraints for required multivalued scalar/enum properties, and SHALL support
an opt-in LinkML slot annotation that lowers to a generated index statement. Neither generator
SHALL emit application-layer validation (triggers, procedures, or any construct standing in for
something Neo4j cannot natively enforce) as a substitute for what the neomodel generator's own
Python-layer validation already covers. `project-setup` SHALL project both generators into a
consuming repository as a pinned, refreshable copy (sourced from `tools/linkml_neo4j/`),
conditional on the project using LinkML with a Neo4j target, following the same projection
discipline already used for the `meaningfy` OpenSpec schema.

#### Scenario: A relationship's range is an abstract LinkML class
- **WHEN** a slot's range is an abstract class in the LinkML schema
- **THEN** the generated neomodel code defines that class as an abstract base with real Python
  inheritance to its concrete subclasses, and the relationship referencing it resolves to a real,
  registered class rather than an undefined name

#### Scenario: A required slot is multivalued
- **WHEN** a scalar or enum slot is both `required: true` and `multivalued: true`
- **THEN** the Cypher generator emits an existence constraint for that property, rather than
  skipping it because it is multivalued

#### Scenario: A slot is annotated for indexing
- **WHEN** a slot in the schema carries an opt-in index annotation
- **THEN** the Cypher generator emits a corresponding `CREATE INDEX` statement, without requiring
  a hand-maintained index file

#### Scenario: Projecting the generators into a consuming project
- **WHEN** `project-setup` scaffolds or modernises a project that uses LinkML with a Neo4j target
- **THEN** it projects a pinned copy of both generators from `tools/linkml_neo4j/`, refreshable
  later by re-running the skill and reviewing the diff, the same discipline already used for the
  `meaningfy` OpenSpec schema

#### Scenario: Something Neo4j cannot natively enforce
- **WHEN** a LinkML construct (an enum's permissible values, a pattern, numeric bounds, or a
  relationship cardinality lower bound) has no native Neo4j constraint equivalent
- **THEN** neither generator emits a substitute enforcement mechanism for it; the neomodel
  generator's existing Python-layer validation remains the only enforcement for that construct

#### Scenario: A generator's code is proposed for placement inside the skill

- **WHEN** a change proposes adding or modifying generator code under `skills/linkml-engineering/`
- **THEN** it is rejected on skill-repo-governance grounds and redirected to `tools/linkml_neo4j/`,
  with `linkml-engineering` updated to cite it, not host it

## MODIFIED Requirements

### Requirement: Dual-CLI parity and deferred scope
The skill SHALL ship to both Claude Code and opencode from the Claude source with a regenerated,
never-hand-edited `.opencode/` mirror, and its body SHALL stay CLI-agnostic. This skill SHALL NOT
introduce a model2owl configuration/transformation skill, an ontology/semantic-modelling skill, or a
greenfield LinkML workflow. Custom generator tooling IS in scope for the skill to *document and
cite* — as tested, projectable repo tooling at `tools/linkml_neo4j/` (see the generators
requirement above) — but SHALL NOT be vendored as a skill asset; the prior blanket deferral of "new
tooling or CLI" applied to the skill's original, documentation-only scope and does not extend to
referencing this narrower, tested-and-projected class of repo tooling.

#### Scenario: The catalogue is validated
- **WHEN** `make validate` runs over the change
- **THEN** `linkml-engineering` resolves under `meaningfy-architecture`, the `.opencode/` mirror is
  in sync, the version-sync gate passes, and no deferred artefact (model2owl skill, ontology skill,
  greenfield LinkML workflow) is present

#### Scenario: A new custom generator is proposed
- **WHEN** a change proposes adding a custom generator as tested repo tooling with a
  `project-setup` projection path
- **THEN** it is in scope for `linkml-engineering` to document and cite, distinguishing it from the
  general "new tooling or CLI" deferral, provided the generator's code itself lives outside the
  skill directory
