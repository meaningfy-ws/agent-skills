> Derived from EPIC `add-linkml-engineering-skill`

## 1. Shared skill: modelling-conventions

- [x] 1.1 Create `skills/modelling-conventions/SKILL.md` — frontmatter (`name`, `description`,
  `license`, `metadata.category`) and body with Boundary section (satisfies "modelling-conventions
  is the shared modelling-craft layer"). Note: `boundary`/`related_skills` are body sections per house
  style, not frontmatter fields.
- [x] 1.2 `references/naming-and-identity.md` — reusable-property principle (attributes decoupled into
  first-class properties) and URI-everywhere-implicit-by-default principle, representation-agnostic
  (satisfies "attributes are decoupled into reusable properties" + "everything is identified").
- [x] 1.3 `references/anti-patterns.md` — generic modelling anti-patterns (free strings, god-classes,
  validation-in-code, etc.).
- [x] 1.4 `references/editor-guardrails.md` — the guardrails a modeller follows while working.

## 2. Skill: linkml-engineering

- [x] 2.1 Create `skills/linkml-engineering/SKILL.md` — frontmatter (incl. `boundary`,
  `related_skills: [modelling-conventions, conceptual-modelling, architecture]`) and body: three-phase
  workflow (derive → author → generate & guard), follow-up-not-greenfield gate, boundary reusing
  `modelling-conventions` (satisfies "owns the operational LinkML craft").
- [x] 2.2 `references/deriving-linkml.md` — derivation entry points per input kind (text spec, UML,
  model2owl output, existing model) (satisfies "LinkML is a follow-up, never greenfield").
- [x] 2.3 `references/authoring-mechanics.md` — top-level reusable `slots:`, URI-as-datatype artifice,
  minted prefixes + implicit `class_uri`/`slot_uri`, `enums`, schema-level constraints; cite model2owl
  conventions + checkers (satisfies "LinkML-specific authoring mechanics").
- [x] 2.4 `references/owl-shacl-completeness.md` — the MUST-have OWL and SHACL element lists and how
  implicit URIs make complete generation possible even for non-semantic targets (satisfies "complete
  and correct OWL and SHACL generation").
- [x] 2.5 `references/generation-and-templates.md` — custom `--template-dir` templates (strict Pydantic
  base, worked example from mapping-suite-sdk), custom code gen for programming languages, make-target
  automation of transformations incl. diagrams, per-module artefact layout, enable-on-demand target
  matrix (satisfies "custom templates and make-target automation" + "native per-module artefact
  generation").
- [x] 2.6 `references/quality-gates.md` — the guided gate-selection process (ask the user which gates),
  lint-no-mute, codegen-freshness drift, example round-trip, version pinning, edit→lint→regenerate→
  verify→commit loop (satisfies "quality gates are chosen through a guided process").

## 3. Refactor consumers

- [x] 3.1 Relocate generic conventions from `conceptual-modelling/references/` into
  `modelling-conventions`, and LinkML-operational content into `linkml-engineering`; leave one-line
  delegation pointers (satisfies "conceptual-modelling and project-setup are updated as consumers").
- [x] 3.2 Retune `conceptual-modelling` frontmatter `description`/`boundary`/`related_skills` toward
  ontology/UML conceptual modelling and the new reuse layer.
- [x] 3.3 Update `project-setup`: add a conditional LinkML branch that scaffolds the selected gates,
  transformation automations, and per-module layout when the project uses LinkML; skip otherwise
  (satisfies the project-setup scenario).
- [x] 3.4 Grep inbound links to the relocated `conceptual-modelling` sections (`cosmic-python`,
  `architecture`, `project-setup`) and repoint any that referenced moved content.

## 4. Register, version, mirror, validate, release

- [x] 4.1 Add `./skills/modelling-conventions` and `./skills/linkml-engineering` to the
  `meaningfy-architecture` bundle in `.claude-plugin/marketplace.json`.
- [x] 4.2 Run `make generate-opencode`; commit the regenerated `.opencode/` mirror (never hand-edited).
- [x] 4.3 Run `make validate`; fix any gate failures (frontmatter, body-agnosticism, boundary,
  dual-CLI drift, version-sync); confirm the deferred-scope scenario holds (satisfies "dual-CLI parity
  and deferred scope").
- [x] 4.4 MINOR-bump root `VERSION`; confirm sync to `marketplace.json`/`opencode.json`.
- [ ] 4.5 On the proper release branch, cut a new repository release including all
  `meaningfy-architecture` skill changes (final stage, before commit/push).

## Roadmap

- [x] 1.1 · [x] 1.2 · [x] 1.3 · [x] 1.4 · [x] 2.1 · [x] 2.2 · [x] 2.3 · [x] 2.4 · [x] 2.5 · [x] 2.6 · [x] 3.1 · [x] 3.2 · [x] 3.3 · [x] 3.4 · [x] 4.1 · [x] 4.2 · [x] 4.3 · [x] 4.4 · [ ] 4.5

## Verification

`make validate` passes (frontmatter, body-agnosticism, boundary declarations, dual-CLI drift,
version-sync); the reference audit finds generic conventions only in `modelling-conventions` and
LinkML-operational guidance only in `linkml-engineering`; the PLAN clears the clarity gate (≥9/10)
before `apply`; the release is cut on the proper branch.
