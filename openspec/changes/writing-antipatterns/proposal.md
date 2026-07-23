# EPIC: Writing antipatterns — a register/genre-conditional catalogue

## Appetite

Small. One new skill, four cross-references added to existing skills, one spec delta. No new
bundle, no tooling, no generation pipeline.

## Why

The writing-skill family (`technical-writing`, `explanatory-writing`, `executive-communication`,
`proposal-writing`, `decision-package`, `architecture`, `semantic-consulting-coach`) each states
*positive* craft rules, but none names the failure modes, and several of those rules **invert**
between genres a single author routinely writes in (a rhetorical question is a craft move in an
explainer and a defect in an ADR). A real 40-page plan review this month diagnosed exactly this
class of failure and converged, across three drafts, on a workable catalogue design. That design is
sound; it has not been placed in the catalogue, cross-linked, or corrected against the actual repo.

## Solution outline

Add a standalone knowledge-only skill, `writing-antipatterns`, in `meaningfy-core`. It owns a single
cross-cutting synthesis no existing skill owns: an 8-genre map (Tutorial, How-to, Reference,
Explanation, Decision, Decision record, Contract/specification, Coaching dialogue) each tagged with
its owning skill, a short list of defects that apply in every genre with no lookup needed, and an
inversion matrix of genre-conditional moves (a move is required in one genre and harmful in
another) with one canonical prose entry per matrix row. Per-genre reference files are **filtered
views with pointers back to the canonical entry**, not restatements — the catalogue must not
itself commit the duplication defect it documents. A human-facing explainer (trimmed from a real
session write-up) carries the teaching layer; the reference stays terse.

Every writing-family skill gets one `Related:` line pointing here. Nothing is restated.

## Key decisions

- **DEC-1**: New standalone skill (`writing-antipatterns`), not folded into `clarity-gate` (its
  stated scope is spec/EPIC actionability, not prose craft) or `executive-communication` (owns
  register, not the Diátaxis genre taxonomy). Matches the existing single-source-of-authority
  pattern (`company-voice.md`).
- **DEC-2**: Classification axis is **genre alone** (8 genres, each carrying its own register
  signature), not a register × genre lattice — collapses what would otherwise be a mostly-empty
  2×8 grid into one axis with a per-genre profile.
- **DEC-3**: Extensibility mechanism is the **inversion matrix**: rows are moves, columns are
  genres, cells are `required / welcome / avoid / harmful / n/a`. Adding an antipattern means
  adding one row. Per-genre files are generated-by-hand-but-pointer-only excerpts of this one
  canonical table, to avoid uncontrolled duplication.
- **DEC-4**: Two-tier split — a short **unguarded** list (fires in every genre, apply without
  judgement) versus the **guarded** (genre-conditional) list, each entry stating where it fails,
  where the same move is required, and the test that tells them apart.
- **DEC-5**: Reuse existing idioms rather than invent a third: `architecture`'s `Smell:`/`Fix:`
  form and the guard/cue shape already worked out across the source drafts. No new notation.
- **DEC-6**: Compress cardinality before shipping: merge "abstraction with no example" with
  "persuasion inside a commitment" (both are about material creating unintended obligation), and
  merge "uncontrolled duplication" with "cardinality drift" (both are about sets that lost their
  single source) — per the source drafts' own self-critique.
- **DEC-7**: Fix a factual overreach in the source material before it ships: one draft claims
  `architecture` sets "five to eight ADRs is typical, fourteen or more signals conflation" as a
  single flat rule. `architecture`'s actual guidance is per-C4-level (L1 2–3, L2 3–5, L3 2–4, L4
  1–2, summing to 8–14), not a flat threshold. Cite it correctly or not at all.
- **DEC-8**: Ship both an audience layer: a terse, agent-facing reference (the matrix + per-genre
  filters) and a trimmed, human-facing explainer (Explanation register, client-specific content
  removed) — mirrors the existing `technical-writing`/`explanatory-writing` split.
- **DEC-9**: Bundle: `meaningfy-core` (cross-cutting, used by every role, like `technical-writing`
  and `guardrails`), not a role-specific bundle.
- **DEC-10**: Fill a real gap the source drafts left dangling: the inversion matrix in the most
  advanced draft has four rows (direct address, controlling metaphor, options-shown-not-just-the-
  choice, structure-before-alignment) with no corresponding prose entry anywhere. Write full
  entries for all matrix rows; a matrix row that cites nothing is not shippable.
- **DEC-11**: Add two independently-verified, well-known antipatterns absent from every source
  draft: **curse of knowledge** (Pinker) as a new guarded entry (fails in Tutorial/Explanation,
  correct in Reference/Contract, where assuming domain fluency is the explicit reader contract),
  and **weasel words / unattributed authority** ("studies show", vague quantifiers) plus
  **terminology drift** as two new unguarded entries — both distinct from the existing Hedging
  entry, which is about the author's own epistemic qualifiers, not vague attribution to nobody.
- **DEC-12**: The "internal working plan" genre gap the source material also surfaces (no skill
  owns a team's own working plan, recommending a future `plan-writing` skill) is explicitly
  **out of scope** here — a one-line pointer only, no artifact.
- **DEC-13**: **Domain is not genre.** A sales pitch, a PM status update, a BI insight memo, and an
  architecture narrative are not missing genres — they are domain flavours of the 8 genres already
  named (sales pitch → Decision; PM status update → the deferred internal-working-plan gap, DEC-12;
  BI memo → Explanation or Decision depending on its job). Model/diagram-correctness antipatterns
  (`modelling-conventions/references/anti-patterns.md`, `architecture`'s `Smell:`/`Fix:` set) are a
  **separate axis** — this skill covers prose/rhetoric, not model structure — and are cited, never
  duplicated. State this explicitly in the genre map so a future contributor does not invent a new
  genre column for a domain that already maps onto an existing one.

## Rabbit-holes

- Do not attempt to make the per-genre files auto-generated from the matrix (no tooling exists for
  this and the matrix is small enough to keep in sync by hand, same discipline as this repo's many
  hand-maintained `Owns:`/`Related:` tables).
- Do not chase every antipattern found on the web — two additions (curse of knowledge, weasel
  words/terminology drift) are enough to prove the catalogue extends cleanly; more can be added
  later, one row at a time, by design.

## No-gos

- No `plan-writing` skill in this change (DEC-12).
- No new bundle.
- No generation/freshness-gate tooling for this skill (unlike `docs/skill-inventory.md`, the
  entry count here is small and hand-maintained, matching how every other skill's reference tables
  are kept).
- No rewriting of the Hulubul-specific plan review itself; only the generalizable frame and
  catalogue are vendored in.

---

## What Changes

- Add `skills/writing-antipatterns/` (`SKILL.md` + `references/`: `inversion-matrix.md`, one file
  per genre, `explainer.md`).
- Add `writing-antipatterns` to the `meaningfy-core` bundle in
  `.claude-plugin/marketplace.json`.
- Add one `Related:` line in each of: `technical-writing`, `explanatory-writing`,
  `executive-communication`, `proposal-writing`, `decision-package`, `architecture`,
  `semantic-consulting-coach`.
- **MODIFIED**: `explanatory-writing`'s spec requirement "Writing knowledge has a single home;
  consumers reference it" currently enumerates the writing-skill family as exactly
  `technical-writing`, `executive-communication`, `explanatory-writing` — this list must expand to
  include `writing-antipatterns` or the new skill contradicts a standing, enforced requirement.

## Capabilities

### New Capabilities

- `writing-antipatterns`: the register/genre-conditional antipattern catalogue — genre map,
  unguarded defects, inversion matrix, per-genre filtered views, human explainer.

### Modified Capabilities

- `explanatory-writing`: the "single home for writing knowledge" requirement's family list expands
  to include `writing-antipatterns`.

## Impact

- New skill directory, no code/runtime impact.
- `.claude-plugin/marketplace.json` (bundle membership) and the generated `.opencode/` tree
  (regenerated via `make generate-opencode`).
- Cross-reference edits in 7 existing skills (additive `Related:` lines only).
- `docs/skill-inventory.md` regenerates to include the new skill (`make skill-inventory`), and its
  `PURPOSE_OF` mapping in `tools/skill_inventory.py` needs one new entry or generation fails its
  coverage gate.
