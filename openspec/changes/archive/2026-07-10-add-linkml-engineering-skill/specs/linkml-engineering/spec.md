# linkml-engineering Specification

## ADDED Requirements

### Requirement: linkml-engineering owns the operational LinkML craft

The catalogue SHALL provide a `linkml-engineering` skill in the `meaningfy-architecture` bundle that
owns the operational LinkML discipline as one workflow with three phases — **derive** (LinkML from an
existing model or spec), **author/refine** (LinkML-specific authoring atop the shared conventions), and
**generate & guard** (custom templates, make-target automation, multi-target generation, and the guided
quality-gate process). It SHALL declare a `boundary` and `related_skills` in its frontmatter, reusing
`modelling-conventions` for generic craft and delegating the model concept to `conceptual-modelling`. It
SHALL NOT own the representation-agnostic conceptual model, the LinkML-vs-model2owl source decision,
terminology, or generic modelling conventions.

#### Scenario: A developer with an existing model needs LinkML

- **WHEN** a task asks to derive, author, or refine a LinkML schema, or to wire its generation
- **THEN** `linkml-engineering` applies, reusing `modelling-conventions` for generic guardrails and
  adding the LinkML-specific craft

#### Scenario: A task is about the concept or generic conventions

- **WHEN** a task is about the representation-agnostic model, ontology/UML modelling, terminology, or
  generic naming/anti-patterns
- **THEN** the boundary defers to `conceptual-modelling` or `modelling-conventions`, and
  `linkml-engineering` does not restate that content

### Requirement: LinkML is a follow-up representation, never greenfield

The skill SHALL activate only after an upstream artefact exists — a text specification, a UML model, a
model2owl output, or another existing model — and SHALL treat LinkML as a *derived* representation of
that source. It SHALL document a derivation entry point for each supported input kind.

#### Scenario: A request assumes an upstream source

- **WHEN** a request provides or names an existing model or spec to turn into LinkML
- **THEN** the skill derives an initial LinkML schema from that source and refines it

#### Scenario: A request has no upstream model

- **WHEN** a request asks to author LinkML from nothing
- **THEN** the skill points back to `conceptual-modelling` to establish the model first, rather than
  greenfielding a schema

### Requirement: LinkML-specific authoring mechanics

The skill SHALL carry the LinkML mechanics that realise the shared conventions: attributes modelled as
top-level reusable `slots:` (realising the decoupled-property principle), the LinkML URI-as-datatype
artifice for URI-typed values, minted `prefixes`/`default_prefix` with implicit `class_uri`/`slot_uri`
so identifiers stay implicit by default, `enums` in place of free strings, and constraints (`required`,
`multivalued`, bounds, `pattern`, `unique_keys`) expressed in the schema rather than in code. It SHALL
cite the SEMIC and model2owl conventions and checkers as the external authority for the LinkML-specific
URI/datatype/naming slice, without restating the UML-side styleguide.

#### Scenario: An attribute recurs across classes

- **WHEN** the same attribute appears on multiple classes
- **THEN** it is authored once as a top-level reusable slot and referenced, not redefined per class

#### Scenario: A slot holds a URI value

- **WHEN** a slot's values are URIs
- **THEN** the URI-as-datatype artifice is used so the value is typed as a URI, not an opaque string

### Requirement: Complete and correct OWL and SHACL generation

The skill SHALL treat complete, correct OWL and SHACL generation as a first-class outcome — achievable
because every class and property carries a stable URI (implicit by default). It SHALL enumerate the
elements that MUST be present for the generated OWL (e.g. ontology declaration, class and property
axioms, domains/ranges) and SHACL (e.g. node shapes per class, property shapes with paths, cardinality
and datatype constraints) to be usable, and SHALL state that these hold even when the delivered target
is JSON, JSON-LD, Python, or a database.

#### Scenario: Generating semantic artefacts from the schema

- **WHEN** OWL and SHACL are generated from a schema authored under these conventions
- **THEN** every class and property resolves to a stable URI and the output contains the enumerated
  MUST-have elements

#### Scenario: The delivered target is non-semantic

- **WHEN** a project delivers only JSON/Python/DB artefacts from the schema
- **THEN** the schema is still authored so complete OWL/SHACL could be generated, keeping the semantic
  option open

### Requirement: Custom templates and make-target automation

The skill SHALL document custom generator templates (`--template-dir`) as the first-class mechanism for
representation-specific type-setting — most importantly a strict project Pydantic base class in place of
LinkML's generic `ConfiguredBaseModel` — and SHALL extend this to custom code generation for
programming languages. It SHALL document make-target automation of the transformations, including
diagram generation, so the pipeline is reproducible and outside the LLM path. Generated artefacts SHALL
never be hand-edited; changes go to the schema or the template.

#### Scenario: Generated models must obey a house base class

- **WHEN** Pydantic (or other language) models are generated
- **THEN** each inherits the project's strict base via the custom template, defined once

#### Scenario: A transformation is run

- **WHEN** models, diagrams, or other artefacts are (re)generated
- **THEN** a make target performs it deterministically, not an ad-hoc command

### Requirement: Native per-module artefact generation

The skill SHALL support generating dedicated artefacts per module, not as a single unified output, so a
multi-module project produces module-scoped artefacts. It SHALL identify `project-setup` as the place
this layout is scaffolded.

#### Scenario: A multi-module project generates artefacts

- **WHEN** a project has multiple modules and runs generation
- **THEN** dedicated artefacts are produced per module rather than one merged artefact

### Requirement: Quality gates are chosen through a guided process

The skill SHALL drive a short process that asks the user which quality gates to establish for their
project — rather than imposing a fixed set — covering at least schema lint policy (warnings not muted),
a codegen-freshness drift check, example round-trip validation, and coverage expectations. It SHALL
state that generation is pinned and outside the LLM path.

#### Scenario: Setting up gates for a project

- **WHEN** quality gates are being established for a LinkML project
- **THEN** the skill asks the user which gates to enable and wires the selected ones, rather than
  assuming a fixed set

#### Scenario: A schema edit lands without regeneration

- **WHEN** the codegen-freshness gate is enabled and a schema is edited without regeneration
- **THEN** the gate produces a non-empty diff and fails the build

### Requirement: conceptual-modelling and project-setup are updated as consumers

`conceptual-modelling` SHALL relocate its LinkML-operational content to `linkml-engineering` (and its
generic conventions to `modelling-conventions`), replacing them with delegation pointers, so no
LinkML-operational guidance exists in two places. `project-setup` SHALL, conditionally on a project
using LinkML, scaffold the LinkML quality gates, transformation automations, and per-module artefact
layout, and skip them otherwise.

#### Scenario: The reference audit checks for duplication

- **WHEN** the boundary is audited
- **THEN** LinkML-operational guidance appears only in `linkml-engineering`, generic conventions only in
  `modelling-conventions`, and `conceptual-modelling` links rather than restates

#### Scenario: Scaffolding a LinkML project

- **WHEN** `project-setup` scaffolds a project that uses LinkML
- **THEN** it wires the selected gates, the transformation automations, and the per-module layout
- **WHEN** the project does not use LinkML
- **THEN** it skips the LinkML scaffolding entirely

### Requirement: Dual-CLI parity and deferred scope

The skill SHALL ship to both Claude Code and opencode from the Claude source with a regenerated,
never-hand-edited `.opencode/` mirror, and its body SHALL stay CLI-agnostic. This change SHALL NOT
introduce a model2owl configuration/transformation skill, an ontology/semantic-modelling skill, new
tooling or CLI, or a greenfield LinkML workflow.

#### Scenario: The catalogue is validated

- **WHEN** `make validate` runs over the change
- **THEN** `linkml-engineering` resolves under `meaningfy-architecture`, the `.opencode/` mirror is in
  sync, the version-sync gate passes, and no deferred artefact (model2owl skill, ontology skill, new
  tooling) is present
