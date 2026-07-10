> Parent: EPIC `add-linkml-engineering-skill` (proposal.md)

## Context

The catalogue ships skills as `skills/<name>/SKILL.md` (+ optional `references/`), registered in a
bundle in `.claude-plugin/marketplace.json`, mirrored to a **generated** `.opencode/` tree, and gated
by `make validate`. The `meaningfy-architecture` ("modelling") bundle holds `architecture` and
`conceptual-modelling`; the latter carries LinkML-operational detail (`references/generators.md`,
`references/ontology-practices.md`) and generic conventions mixed together. `cosmic-python` is the
precedent for a shared knowledge skill that many others reuse.

Source material: two field-tested scratchpads (LinkML best practices; LinkML schema engineering), the
`mapping-suite-sdk` reference implementation (custom Pydantic templates under `resources/templates/` +
a `generate-models` Makefile target), and the model2owl conventions + checkers docs as the external
URI/naming authority.

## Goals / Non-Goals

**Goals:**
- Add `skills/modelling-conventions/` (shared) and `skills/linkml-engineering/`.
- Draw a decisive three-way boundary (DEC-4) and relocate `conceptual-modelling`'s overhang so no
  guidance lives twice (generic → `modelling-conventions`; LinkML-operational → `linkml-engineering`).
- Fold in the new decisions: reusable slots (DEC-7), URI-everywhere → complete OWL/SHACL (DEC-8),
  guided quality-gate process (DEC-9), per-module generation (DEC-10), `project-setup` as conditional
  consumer (DEC-11).
- Ship on both CLIs via regeneration; pass all `make validate` gates; cut a MINOR release.

**Non-Goals:**
- Any new tooling/CLI/runtime code; any generator or Makefile shipped as executable catalogue code (the
  skills *document* the pipeline, not vendor it).
- A model2owl skill or an ontology/semantic-modelling skill (No-gos — future EPICs).
- Restating LinkML docs or the full SEMIC/model2owl UML styleguide (DEC-5, rabbit-holes).

## Decisions

- **D-1 — The generic/LinkML-specific split line (realises DEC-4/DEC-5/DEC-7/DEC-8).** Content is placed
  by *whether it survives changing the representation*:
  - **Generic → `modelling-conventions`:** naming discipline; anti-patterns (free strings, god-classes,
    validation-in-code); the *principle* that attributes are decoupled into reusable first-class
    properties (DEC-7); the *principle* that everything is identified by a stable URI, implicit by
    default (DEC-8); editor-guiding guardrails.
  - **LinkML-specific → `linkml-engineering`:** top-level `slots:` as the reuse mechanism; the LinkML
    URI-as-datatype artifice; `prefixes`/`default_prefix` + implicit `class_uri`/`slot_uri`; `enums`,
    schema-level constraints; the OWL/SHACL MUST-have element lists; generation, templates, gates.
  When in doubt, ask "would an ontology or UML modeller also need this?" — yes ⇒ generic.
- **D-2 — File decomposition (prefer-small-focused-skills).**
  - `modelling-conventions`: lean `SKILL.md` + `references/anti-patterns.md`,
    `references/naming-and-identity.md` (reusable-property + URI-everywhere principles),
    `references/editor-guardrails.md`.
  - `linkml-engineering`: lean `SKILL.md` + `references/deriving-linkml.md` (DEC-3 input kinds),
    `references/authoring-mechanics.md` (slots, URI-as-datatype, implicit URIs, enums, constraints —
    citing model2owl), `references/generation-and-templates.md` (custom templates, custom-code-gen,
    make-target automation incl. diagrams, per-module layout, enable-on-demand matrix),
    `references/owl-shacl-completeness.md` (the MUST-have element lists), `references/quality-gates.md`
    (the guided gate-selection process + the edit→lint→regenerate→verify→commit loop).
- **D-3 — Boundary refactor is relocation, not addition (DEC-4).** Move each slice out of
  `conceptual-modelling/references/` into its new home; leave one-line delegation pointers + links.
  `conceptual-modelling` keeps the concept, UML conceptual modelling, source decision, terminology, and
  vocabulary-reuse *principle*. Retune its `description`/`boundary`/`related_skills` to add
  `modelling-conventions` and `linkml-engineering`. This is the BREAKING part.
- **D-4 — `project-setup` gains a conditional LinkML branch (DEC-10/DEC-11).** Add a "when the project
  uses LinkML" section that references `linkml-engineering` for the gates, transformation automations,
  and per-module artefact layout; explicitly skip otherwise. Reference, do not restate.
- **D-5 — External docs cited, never vendored (DEC-5).** model2owl + LinkML docs by URL; the
  mapping-suite-sdk template set is the worked example for custom templates.
- **D-6 — opencode mirror generated last, release cut last.** Author Claude sources fully, then
  `make generate-opencode`, then `make validate`, then MINOR-bump `VERSION` and cut the release on the
  proper branch.

## Algorithm / approach

Build order (each step verifiable before the next):

1. **`modelling-conventions`** — `SKILL.md` (frontmatter incl. `boundary`, `related_skills`) + its three
   references. Establishes the reuse target the others cite.
2. **`linkml-engineering`** — `SKILL.md` (three-phase workflow, follow-up-not-greenfield gate, boundary
   reusing `modelling-conventions`) + its five references, porting practice from the scratchpads and the
   mapping-suite-sdk templates. Worked examples: the `gen-pydantic --template-dir` invocation + strict
   base-class stub; the OWL/SHACL MUST-have checklists.
3. **Refactor `conceptual-modelling`** (D-3): relocate content, insert pointers, retune frontmatter.
4. **Update `project-setup`** (D-4): conditional LinkML branch.
5. **Register** both skills in the `meaningfy-architecture` bundle; grep inbound links to relocated
   sections and repoint.
6. **Regenerate** opencode mirror; **validate**; **MINOR-bump `VERSION`**; **cut the release** on the
   proper branch.

The change is a documentation edit set — **idempotent by construction**: re-authoring, re-registering,
and regenerating converge to the same tree; `make validate` is the replay-safe check.

### Anti-patterns
- ❌ Generic conventions duplicated in both `modelling-conventions` and `linkml-engineering` (or left in
  `conceptual-modelling`) — single-source-of-authority violation.
- ❌ LinkML mechanics (slots, URI-as-datatype, OWL axioms) leaking into `modelling-conventions`.
- ❌ Imposing a fixed quality-gate set instead of the guided choice (DEC-9).
- ❌ A unified all-modules artefact where per-module is required (DEC-10).
- ❌ Restating LinkML tutorials / the full UML styleguide.
- ❌ Hand-editing `.opencode/`; shipping runnable generators as catalogue code; CLI-isms in bodies.
- ❌ A greenfield "author LinkML from nothing" path (DEC-3).

## Error matrix

| Failure mode | Expected handling |
|---|---|
| `make validate` fails on dual-CLI drift | Re-run `make generate-opencode`; commit regenerated mirror. Never hand-edit `.opencode/`. |
| Version-sync gate fails | Bump root `VERSION`; let sync flow to manifests. |
| Body-agnosticism check flags a CLI-ism | Rephrase neutral, or record a cosmetic gap in the audit. |
| Boundary/frontmatter gate fails | Add `boundary`/`related_skills` to all three touched skills. |
| Reference audit finds duplicated guidance | Relocation (D-3) incomplete; remove the duplicate, leave a pointer. |
| Generic content lands in the LinkML skill (or vice-versa) | Apply the D-1 test; move to the correct home. |
| Clarity gate scores PLAN < 9/10 | Resolve the flagged ambiguity before `apply`. |

## Risks / Trade-offs

- **[Three-way boundary bleed]** Three skills could re-claim naming/URIs/conventions. *Mitigation:* the
  D-1 placement test + the spec's delegation requirements + the reference audit.
- **[Scratchpad rot]** Source scratchpads live in `/tmp` and will vanish. *Mitigation:* port their
  substance now; never link to `/tmp`.
- **[External-doc drift]** model2owl/LinkML docs move. *Mitigation:* cite stable roots; capture the
  principle, not page text.
- **[Scope creep toward the future skills]** model2owl / ontology skills tempt inclusion. *Mitigation:*
  explicit No-gos; the validate scenario checks no deferred artefact is present.
- **[project-setup coupling]** Over-wiring `project-setup` to LinkML. *Mitigation:* reference-only,
  strictly conditional, skip-when-absent.

## Open Questions

- Final name of the shared skill (`modelling-conventions` is the working name; confirm at authoring).
- Exact ordering of the two new skills in the `meaningfy-architecture` array (cosmetic).
- Which existing consumers (`cosmic-python`, `architecture`, `project-setup`) link to the relocated
  `conceptual-modelling` sections — resolve by grepping inbound links during D-3.
- The precise OWL/SHACL MUST-have element lists (DEC-8) — confirm against model2owl checkers + LinkML
  gen-owl/gen-shacl output during authoring.
