# EPIC: linkml-engineering + modelling-conventions — the shared modelling layer and the LinkML craft

## Appetite

**Medium–large.** Two new skills (a shared `modelling-conventions` and `linkml-engineering`), a
boundary refactor of `conceptual-modelling`, a conditional-consumer update to `project-setup`, and the
dual-CLI regeneration. No new runtime code — the cost is authoring discipline, a clean three-way
boundary, and getting the generic/LinkML-specific split right.

## Why

Meaningfy's single-source-of-specifications approach pivots on LinkML (UML/spec → LinkML →
Pydantic/OWL/SHACL/JSON-LD/TS/SQL), but the catalogue covers LinkML only at *overview* altitude inside
`conceptual-modelling`, and the **generic modelling best-practice** that should be shared across
modelling skills (like `cosmic-python` is shared across build skills) does not exist as its own home.
The operational craft — reusable-slot decoupling, URI-everywhere so OWL/SHACL generate *completely*
and correctly, custom generator templates, per-module artefact generation, and a real quality-gate
process — lives only in throwaway scratchpads and one project's Makefile. That is exactly what a skill
exists to make reusable.

## Solution outline

Introduce a **shared modelling-conventions layer** and a **LinkML craft skill**, both in the
`meaningfy-architecture` ("modelling") bundle, with a clean three-way boundary:

- **`modelling-conventions` (new, shared).** Representation-agnostic modelling best-practice,
  anti-patterns, naming discipline, and the **editor-guiding guardrails** a modeller follows while
  working — including the two load-bearing principles: *decouple attributes from classes and model them
  as reusable properties/slots*, and *everything is identified (URI-bearing), as implicitly as
  possible*. Reused by `conceptual-modelling` and `linkml-engineering` today, and by the future
  ontology/model2owl skills — exactly the `cosmic-python` reuse pattern.
- **`linkml-engineering` (new).** The LinkML craft, **downstream of an existing model or spec — never
  greenfield**: derive LinkML from an input, author/refine it under the shared conventions *plus*
  LinkML-specific mechanics (reusable `slots:`, the URI-as-datatype artifice, implicit `class_uri`/
  `slot_uri`), generate the full target set with custom templates and **make-target automation**
  (including diagrams), and guard it. A first-class concern: **complete, correct OWL & SHACL
  generation** — the skill names the elements that MUST be present so the semantic artefacts are usable
  even when the delivered target is JSON/JSON-LD/Python/DB.
- **`conceptual-modelling` (refactored).** Sheds its LinkML-operational overhang (to
  `linkml-engineering`) and its generic conventions (to `modelling-conventions`); keeps the living
  conceptual-model concept, UML conceptual data modelling, the source decision, and terminology.
- **`project-setup` (conditional consumer).** When a project uses LinkML, it scaffolds the LinkML
  quality gates and transformation automations and the **per-module dedicated-artefact** layout;
  otherwise it skips them.

Quality gates are **not imposed as a fixed set** — the skill drives a short process that *asks the user
which gates to establish* for their project.

## Key decisions

- **DEC-1**: **Name = `linkml-engineering`** — the LinkML-specific engineering discipline, sibling to
  `conceptual-modelling` (the concept) and `modelling-conventions` (the shared craft). Not `-best-practices`.
- **DEC-2 (revised)**: **Create a shared `modelling-conventions` skill now**, the cosmic-python reuse
  pattern, reused by `conceptual-modelling` and `linkml-engineering`. The "editor-guiding" guardrails
  the user floated are **the same thing** as this shared conventions layer — one home, not a third
  skill. This change therefore creates **two** new skills.
- **DEC-3**: **LinkML is follow-up, never greenfield.** It activates only after a model or text spec
  exists and derives LinkML from it. Load-bearing boundary with `conceptual-modelling`, where a model
  is *born*.
- **DEC-4**: **Three-way boundary, single source of authority.** `modelling-conventions` OWNS generic
  conventions/anti-patterns/guardrails; `conceptual-modelling` OWNS the concept + UML conceptual
  modelling + terminology + source decision; `linkml-engineering` OWNS the LinkML craft. The two
  modelling skills *reuse* `modelling-conventions`. LinkML-operational content relocates from
  `conceptual-modelling` to `linkml-engineering`; generic conventions relocate to `modelling-conventions`.
- **DEC-5 (refined)**: **Split SEMIC/model2owl conventions carefully.** The generic naming/anti-pattern
  slice lands in `modelling-conventions`; only the LinkML-specific URI/datatype mechanics land in
  `linkml-engineering`. model2owl conventions + checkers are cited as the external authority, not restated.
- **DEC-6**: **Custom generator templates are the highest-leverage customization** (strict Pydantic
  base via `--template-dir`); wired first-class, extended to **custom code generation for programming
  languages** and **make-target automation of transformations, including diagrams**.
- **DEC-7 (new)**: **Decouple attributes from classes → reusable properties/slots.** Generic principle
  (properties as first-class) lives in `modelling-conventions`; the LinkML top-level `slots:` mechanism
  lives in `linkml-engineering`.
- **DEC-8 (new)**: **URI-everywhere, implicit by default → complete OWL/SHACL.** Everything carries a
  URI, as implicit as possible (explicit only when needed), via the LinkML URI-as-datatype artifice and
  minted prefixes. `linkml-engineering` documents the MUST-have OWL and SHACL elements so both are
  generated completely and correctly regardless of the final delivered target.
- **DEC-9 (new)**: **Quality gates are chosen, not imposed.** The skill drives a process that asks the
  user which gates to establish (lint policy, codegen-freshness, example round-trip, coverage) for their
  project, rather than hard-coding one set.
- **DEC-10 (new)**: **Native per-module artefact generation.** Dedicated artefacts are generated *per
  module*, not as one unified output; supported natively and scaffolded by `project-setup`.
- **DEC-11 (new)**: **`project-setup` is a conditional consumer.** When a project uses LinkML it
  scaffolds the gates + automations + per-module layout from `linkml-engineering`; otherwise it skips.
- **DEC-12**: **`linkml-engineering` is not an ontology skill**, but keeps ontologies in mind (implicit
  URIs, complete OWL/SHACL). A dedicated ontology/semantic-modelling skill (methodologies, competency
  questions) is a separate future EPIC.

## Rabbit-holes

- **Restating LinkML's own docs** or the full SEMIC/model2owl UML styleguide — capture *practice*, cite
  upstream (external references are OK).
- **Mis-splitting generic vs LinkML-specific conventions** — the DEC-4/DEC-5 line must be decisive, or
  `modelling-conventions` and `linkml-engineering` will both claim naming/URIs.
- **Gold-plating the generator matrix** — Pydantic/JSON Schema/OWL/SHACL first-class;
  TS/SQL/XSD/custom-code enable-on-demand.
- **Over-engineering the quality-gate process** — it is a short guided choice, not a gate framework.

## No-gos

- **No model2owl configuration/transformation skill** in this change — a separate future EPIC, tightly
  linked to `project-setup`.
- **No ontology/semantic-modelling skill** (methodologies, competency questions) — separate future EPIC.
- **No greenfield-from-nothing LinkML workflow** — the skill assumes an upstream model/spec (DEC-3).
- **No new tooling, CLI, or runtime code** — knowledge artefacts + boundary refactor; the skills
  *document* generators/Makefiles, they do not vendor runnable code.
- **No rewrite of `conceptual-modelling`'s concept-level content** — only overhang relocates.
- **No hand-editing of the generated `.opencode/` tree** — regenerate via the dual-CLI generator.

---

## What Changes

- Add skill `skills/modelling-conventions/` (`SKILL.md` + references): generic modelling best-practice,
  anti-patterns, naming, editor-guiding guardrails, reusable-property and URI-everywhere principles.
- Add skill `skills/linkml-engineering/` (`SKILL.md` + references): derivation, LinkML-specific
  authoring (reusable slots, URI-as-datatype, implicit URIs), complete OWL/SHACL generation, custom
  templates + make-target automation (incl. diagrams), per-module generation, and the guided
  quality-gate process.
- Register both skills in the `meaningfy-architecture` bundle in `.claude-plugin/marketplace.json`.
- **Refactor `conceptual-modelling`** (**BREAKING** frontmatter/`references/`): relocate LinkML-operational
  detail to `linkml-engineering` and generic conventions to `modelling-conventions`; add delegation
  pointers; retune `description`/`boundary`/`related_skills` toward ontology/UML conceptual modelling and
  the new reuse.
- **Update `project-setup`** (conditional consumer, DEC-11): scaffold LinkML gates, transformation
  automations, and per-module artefact layout when the project uses LinkML.
- Repoint any other consumer that linked to relocated content.
- Regenerate the `.opencode/` mirror via `make generate-opencode`.
- Bump the root `VERSION` (MINOR — additive skills) and **cut a new repository release** on the proper
  branch, including all `meaningfy-architecture` skill changes (final stage, before commit/push).

## Capabilities

### New Capabilities
- `modelling-conventions`: representation-agnostic modelling best-practice, anti-patterns, naming, and
  editor-guiding guardrails (incl. reusable-property and URI-everywhere principles); the shared layer
  reused by the modelling skills.
- `linkml-engineering`: the LinkML craft — derivation from an existing model/spec, LinkML-specific
  authoring (reusable slots, URI-as-datatype, implicit URIs), complete-and-correct OWL/SHACL
  generation, custom templates + make-target automation, per-module generation, the guided quality-gate
  process, and the three-way boundary.

### Modified Capabilities
<!-- None as durable specs. conceptual-modelling and project-setup are skills without capability specs;
     their changes are skill-body refactors captured under Impact. -->

## Impact

- **New skills:** `skills/modelling-conventions/` and `skills/linkml-engineering/` (each `SKILL.md` +
  `references/`).
- **Modified skills:** `skills/conceptual-modelling/` (boundary/description/frontmatter + relocated
  `references/`), `skills/project-setup/` (conditional LinkML scaffolding).
- **Bundle manifest:** `.claude-plugin/marketplace.json` (`meaningfy-architecture` gains two skills).
- **Generated mirror:** `.opencode/skills/{modelling-conventions,linkml-engineering}/` + updated
  `conceptual-modelling`/`project-setup` mirrors (regenerated, never hand-edited).
- **Version & release:** root `VERSION` MINOR bump propagating to `marketplace.json`/`opencode.json`;
  new repository release on the proper branch.
- **Validation gates:** `make validate` (frontmatter, body-agnosticism, boundary declarations, dual-CLI
  drift, version-sync) must pass.
- **External references (cited, not vendored):** model2owl docs (conventions + checkers), LinkML
  generator docs; the mapping-suite-sdk template set as the custom-template worked example.
