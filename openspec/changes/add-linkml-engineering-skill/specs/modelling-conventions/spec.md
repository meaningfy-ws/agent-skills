# modelling-conventions Specification

## ADDED Requirements

### Requirement: modelling-conventions is the shared modelling-craft layer

The catalogue SHALL provide a `modelling-conventions` skill in the `meaningfy-architecture` bundle that
owns representation-agnostic modelling best-practice: naming discipline, anti-patterns, and the
editor-guiding guardrails a modeller follows while working. It SHALL be authored as a reuse layer —
declared as a `related_skills` dependency by `conceptual-modelling` and `linkml-engineering` — in the
same way `cosmic-python` is reused by the build skills. It SHALL NOT contain representation-specific
mechanics (LinkML syntax, UML profiles, OWL axioms); those belong to the consuming skills.

#### Scenario: A modelling skill needs generic conventions

- **WHEN** `conceptual-modelling` or `linkml-engineering` needs naming, anti-pattern, or guardrail
  guidance
- **THEN** it references `modelling-conventions` and does not restate that guidance inline

#### Scenario: Representation-specific detail is proposed for the shared skill

- **WHEN** LinkML-, UML-, or OWL-specific mechanics are proposed for `modelling-conventions`
- **THEN** the boundary rejects them and routes them to the consuming skill that owns that
  representation

### Requirement: Attributes are decoupled into reusable properties

The skill SHALL state, as a load-bearing generic principle, that attributes are decoupled from classes
and modelled as reusable, first-class properties, rather than redefined per class. It SHALL present this
as representation-agnostic (a property is a citeable concept), leaving the concrete mechanism (e.g.
LinkML top-level `slots:`) to the consuming skill.

#### Scenario: The same attribute recurs on several classes

- **WHEN** an attribute of the same meaning appears on more than one class
- **THEN** the principle models it once as a reusable property that classes reference

### Requirement: Everything is identified, as implicitly as possible

The skill SHALL state that every modelled element carries a stable identifier (a URI), minted at
authoring time and kept implicit by default — made explicit only when a specific value is required — so
that formal/semantic artefacts can be generated naturally. It SHALL keep this a principle and delegate
the representation-specific identifier mechanics to the consuming skills.

#### Scenario: A new class or property is introduced

- **WHEN** a class or property is added to a model
- **THEN** the convention ensures it is identifiable by a stable URI without requiring an explicit URI
  literal unless one is needed

### Requirement: Dual-CLI parity

The skill SHALL ship to both Claude Code and opencode from the Claude source with a regenerated,
never-hand-edited `.opencode/` mirror, and its body SHALL stay CLI-agnostic.

#### Scenario: The catalogue is validated

- **WHEN** `make validate` runs over the change
- **THEN** `modelling-conventions` resolves under `meaningfy-architecture`, its `.opencode/` mirror is
  in sync, and the body-agnosticism gate passes
