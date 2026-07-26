> Parent: openspec/changes/define-lifecycle-playbooks/proposal.md

## Context

This EPIC is the fifth and last of a round redefining Meaningfy's business + build lifecycle. It
adds no lifecycle fact of its own (proposal DEC-3, "map, not source"): its whole job is composing
seven small, mostly-link documents over the four sibling EPICs' outputs —
`define-blc-engagement-model` (the corrected commercial funnel), `define-meaningfy-lifecycle` (the
build plane), `define-delivery-release-lifecycle` (the dual DoD), `define-roles-and-raci` (the six
roles and the RACI matrix). Implementation is gated on those four landing on `develop` first
(DEC-10); this PLAN can be written now because it only has to describe *shape*, and every fact the
shape depends on (the six role names, the funnel stages, the plane names) is already settled and
quoted in the four sibling `proposal.md` files read for this design.

The design problem this PLAN actually has to solve is narrow: not "what does the lifecycle look
like" (decided elsewhere) but "what concrete structure keeps seven new files from becoming seven
new places a fact can go stale." That is a documentation-architecture problem, not a lifecycle
problem, and it is the only thing left for this PLAN to design.

## Goals / Non-Goals

**Goals:**
- A concrete, checkable authoring rule that turns DEC-3's principle ("map, not source") into
  something a writer can apply sentence-by-sentence while drafting the map and the six playbooks.
- A fixed internal structure for the map (one diagram, one pointer-table pattern, one Known-gaps
  format) and for each playbook (DEC-5's four headings, given a concrete on-page format) so the six
  playbooks are mechanically comparable.
- Exact wording for the "start here" link lines added to the four sibling outputs, so DEC-14's
  "additive lines only" constraint is unambiguous at implementation time.

**Non-Goals:**
- No per-plane diagrams (proposal *Known gaps* — this EPIC's successor).
- No new lifecycle facts, role definitions, gate thresholds, or RACI cells — all cited, per DEC-3.
- No tooling or generation pipeline for the playbook set (proposal Rabbit-holes: "Generating the
  playbooks from a single source table" is explicitly rejected at six files).

## Decisions

Settled in the EPIC — cited, not re-argued: DEC-1 (name), DEC-2 (paths), DEC-3 (map not source),
DEC-4 (one diagram), DEC-5 (fixed template), DEC-6 (repeat-client annotation), DEC-7 (delivery
lanes), DEC-8 (Req&UC at two depths), DEC-9 (Work Shaper playbook, citing
`define-roles-and-raci`'s DEC-13 for the Architect–Builder-spectrum positioning claim — this PLAN
keeps that citation direction and restates nothing of the claim itself), DEC-10 (implement last),
DEC-11 (named gaps stay named), DEC-12 (register per genre), DEC-13 (six playbooks), DEC-14
(link-only discoverability edits), DEC-15 (bidirectional coverage spec), DEC-16 (Known gaps
section).

New structuring choices made while deriving this PLAN:

- **The pointer-discipline mechanism.** DEC-3 states the principle; this PLAN gives it a mechanical
  test a writer runs on every declarative sentence while drafting the map or a playbook: *if this
  sentence would still read as true after deleting the document it cites, it is a copy — cut it or
  attach the link.* Concretely: every sentence in `README.md` or a playbook that states a rule, a
  gate, a threshold, a duration, a price boundary, a role definition, or a RACI cell must end in or
  sit beside a markdown link to the sibling doc that owns that fact. Sentences that carry only
  sequence, transition, or "what comes next" (orientation prose) are exempt — that is what DEC-3
  says this folder *should* carry. This is the same test the proposal's own Rabbit-holes section
  states in prose; the PLAN's contribution is making it the literal self-check run at task 5.3, not
  a restatement of the rule.
- **Per-section format inside the fixed DEC-5 template.** Each of the four playbook sections (*Your
  stages*, *Skills you invoke*, *Handed to you by*, *You hand off to*) is a short bullet list, not a
  table — a table implies rows with more than one column of information, and each section here
  carries exactly one column (a stage name, a skill link, a role link). Bullets keep the one-screen
  cap (DEC-5, ~120 lines) honest; a table would pad each entry to a row and make six one-page files
  look longer than the content justifies. *Your done* is one short paragraph, not a list, because a
  role's definition-of-done is usually one condition, not an enumerable set.
- **The map's pointer-table pattern.** `README.md` carries one pointer table per plane/stage cluster
  (funnel, planes, delivery close), each row `Fact | Owning doc`, immediately under the prose
  paragraph that narrates the shape — mirroring `writing-antipatterns`' own "per-genre pointer
  table, not prose" precedent (that skill's design.md, same repo). This gives the pointer-discipline
  self-check a fixed place to land: a normative fact that isn't already a table row is the thing the
  self-check is looking for.
- **"Start here" link wording, fixed once.** Each of the four sibling outputs gets exactly one line,
  placed directly under that document's own title/H1, reading:
  `> **Start here:** for the end-to-end flow and every role's view of it, see How We Work at`
  `docs/how-we-work/README.md` (as a real markdown link, with the relative path adjusted per file
  location — written here as plain text so this illustrative example isn't itself mistaken for a
  navigable link by `broken_links`). One fixed sentence, reused verbatim across all four
  insertion points, keeps the edit mechanically additive (DEC-14) and trivially diffable — a
  reviewer can confirm "additive only" by checking the line is byte-identical in all four places
  modulo the relative path.
- **Known-gaps table format in `README.md`.** Same three columns as the proposal's own Known gaps
  table (`Gap | Status | Owner`), because DEC-16 says the map's section "mirrors" the proposal's
  list — reusing the exact column shape is what makes that mirroring literal rather than a
  paraphrase.

## Algorithm / approach

Two documents, one shared authoring discipline:

1. Draft `README.md` bottom-up from the four sibling `proposal.md` "What Changes" / "Capabilities"
   sections: for every fact the map needs to narrate (funnel stages, plane names, the Work-Shaper-
   authored Epic step, the paired delivery close, the repeat-client annotation), find the sibling
   doc section that will state it once implemented, write one pointer-table row, then write the
   connecting prose as orientation-only.
2. Draft each playbook by filling DEC-5's four sections from the same source material, run through
   the same "does this sentence survive deletion of its target" test.
3. Run the pointer-discipline self-check (task 5.3) as a final pass over both: grep every
   declarative sentence in `README.md` and the six playbooks that is not exempted as orientation
   prose, and confirm each carries an adjacent link.

Idempotency: every task in this change is a file creation or a single additive line insertion at a
fixed anchor (the top of an existing doc, a named table). Re-running an already-applied task is
safe — the file exists with the expected content, or the line is already present — so no task needs
a retry/dedupe mechanism beyond "check before writing," standard for a docs-only change.

### Anti-patterns

- ❌ **Asserting a lifecycle fact here that isn't cited from a sibling epic.** This is the EPIC's
  core anti-pattern (DEC-3) and the one this PLAN's pointer-discipline mechanism exists to catch.
  Any sentence in `README.md` or a playbook that states a number, a gate, a role boundary, or a
  RACI cell without an adjacent link is this defect, full stop — regardless of how minor or
  "obviously true" it reads while drafting.
- ❌ Restating a sibling's content because its own wording is momentarily inconvenient to link to
  (e.g., paraphrasing `define-roles-and-raci`'s DEC-13 positioning line instead of citing it in the
  Work Shaper playbook). If a sibling's wording is genuinely too weak to link to, the fix is filing
  that as a finding against the sibling — never rewriting it in this folder (Rabbit-holes).
- ❌ Letting a playbook grow past DEC-5's one-screen cap by re-explaining a stage instead of linking
  to where it's defined — a playbook that needs a second screen is duplicating its target.
- ❌ A per-genre or per-role table that copies row content across the map and a playbook instead of
  each linking to the one place that states it (the `writing-antipatterns` A1 duplication smell,
  applied to this EPIC's own output).

## Error matrix

| Failure mode | Expected handling |
|---|---|
| A sibling epic's content that this map/playbook cites changes wording or moves after this EPIC ships | Because every fact is a link (never a copy), the map's own prose does not go stale — only the link target might move, and `repo_lint`'s `broken_links` gate (blocking) catches a moved/renamed target immediately. A copy-based design would instead go silently stale in prose that no lint gate reads for correctness — this is the concrete case DEC-3's "map not source" choice is protecting against. |
| A sibling epic's content this EPIC cites is *substantively revised* (not moved, reworded) after this EPIC ships | The map's link still resolves and the prose still reads as true (it only ever asserted the shape/sequence, never the substance), so no edit is needed here. This is the difference between a link surviving a definition change and a copy not surviving one. |
| A seventh role is added to `define-roles-and-raci` later | `lifecycle-playbooks`' spec requirement is a bidirectional coverage invariant, not a fixed count (DEC-15) — the next shaping round adds a seventh playbook file and the spec's Given/When/Then check would fail (highlighting the gap) until it does, without the spec itself needing an edit. |
| Implementation is attempted before all four sibling changes land on `develop` | DEC-10's readiness condition is violated; links written against unmerged siblings resolve to nothing and `broken_links` fails at `make validate`. Task 1.1 makes this an explicit go/no-go gate before any file is written. |
| A playbook's four sections can't be filled without inventing a rule | Per the proposal's Appetite: "If a playbook cannot be written without inventing a rule, that is a defect in epic 1-4's output, not a reason to spend more here." The task is paused and the missing fact is filed as a finding against the owning sibling epic, not authored here. |
| A reviewer can't tell whether an edit to one of the four sibling outputs is "additive only" per DEC-14 | The fixed, byte-identical "start here" wording (Decisions, above) makes this a one-line diff check rather than a judgment call. |

## Risks / Trade-offs

- **[Risk]** The per-plane diagram set (BLC/SDLC/MDLC/ADLC/CBLC individually) is real, requested
  ("eventually"), and out of scope. → **Accepted, not mitigated**: proposal *Known gaps* names it as
  this EPIC's successor's work, sized comparably to this whole EPIC. Nothing in this PLAN attempts a
  partial version — a partial per-plane diagram would be a half-finished commitment that reads as an
  oversight rather than a deliberate deferral, which is exactly what DEC-16's Known-gaps discipline
  exists to prevent.
- **[Risk]** Six hand-maintained playbooks plus a map create a standing maintenance obligation
  every time the role set, the funnel, the build loop, or the delivery DoD changes (proposal
  Impact). → **Mitigation**: the `lifecycle-playbooks` spec's bidirectional coverage requirement
  makes the role↔playbook half of that obligation mechanically checkable rather than something a
  reviewer has to remember to notice; the pointer-discipline requirement means a sibling's content
  change never requires an edit here unless the sibling's *file path* moves.
- **[Trade-off]** Bullet lists inside the DEC-5 template (this PLAN's Decisions) read slightly
  thinner than a table would for readers used to this repo's other reference tables. → Accepted:
  the one-screen cap and the single-column nature of each section make a table pure overhead here,
  and `writing-antipatterns`' own A8 guard ("dense tables in place of prose... required in
  Reference/How-to" only when a *second dimension* exists) supports bullets when there isn't one.

## Open Questions

Parked, not designed, per the proposal's own Known gaps / No-gos:

- **Per-plane diagrams** (BLC/SDLC/MDLC/ADLC/CBLC individually) — this EPIC's successor.
- **Presales-process description** — owned by `define-blc-engagement-model` (epic 1), named there
  as a gap, not authored here.
- **P0-advisory package description** — owned by `define-blc-engagement-model` (epic 1), same
  status.
- **MDLC-standalone methodology** — parked as its own future EPIC (seed §3); this EPIC only carries
  the one-line "known gap" marker on the map, per DEC-11.
- **Agent wrappers for non-Builder roles** — open fork owned by `define-roles-and-raci` (epic 4);
  Work Shaper is named there as the highest-priority candidate if the fork is ever resolved. This
  EPIC neither answers nor prepares for it (No-gos).
- **Single-source generation trigger for the playbook set** — not needed at six hand-maintained
  files (proposal Known gaps); revisit only if the set outgrows this size.
