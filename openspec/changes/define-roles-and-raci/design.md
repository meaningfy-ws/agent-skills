<!-- PLAN (design half). PLAN = this file + tasks.md. The clarity gate scores the pair (≥9/10).

     ALTITUDE — the reasoning: HOW + why-this-how. Cite the EPIC's DEC-n; never re-explain a settled bet.
     Acceptance criteria live in the spec deltas as GWT scenarios (WHEN/THEN), NOT here. -->

> Parent: openspec/changes/define-roles-and-raci/proposal.md (DEC-1 through DEC-17)

## Context

The repo has no named vocabulary for who does the work — "Solution Architect", "Solution Builder",
"Solution Shipper", "Technical Consultant" and "RACI" occur nowhere today (proposal.md, Why). The
EPIC settles the vocabulary and the model in full: six roles (round-2 correction, **DEC-2R**
supersedes round-1's **DEC-2**), a 6×17 RACI matrix, two adaptation notes, and one open question.
This design covers only the **structuring** work left after the EPIC's decisions: how the single
doc lays those settled pieces out, and how the new capability's spec stays structure-only (**DEC-10**).

Nothing here re-litigates a `DEC-n` — every content decision (which six roles, which cell holds
which letter, why Quality Overseer/Customer Success Manager fold in rather than add columns) is
already made in `proposal.md`. This file is the single new axis: **document layout**, not role
content.

## Goals / Non-Goals

**Goals:**
- Lay out `docs/roles-and-raci.md` so the six role blocks, the legend + invariants, the one matrix,
  the two adaptation notes, the open question, and the Known-gaps subsection each have an
  unambiguous, single home in the file (no content duplicated between sections).
- Keep the one-A-per-row invariant mechanically checkable by eye on the matrix as laid out —
  one letter per cell, no merged cells, no footnoted A's (the round-1 defect **DEC-5** fixes).
- Preserve the citation direction for Work Shaper's Architect–Builder positioning: this doc is the
  source (**DEC-13**); `define-lifecycle-playbooks` cites it. Nothing in this design or the spec
  restates that positioning anywhere but the Work Shaper role block and its two boundary paragraphs.

**Non-Goals:**
- No new RACI cell content, no new role, no resolution of the agent-wrapper fork (**DEC-3**) — all
  settled or deliberately open in the EPIC.
- No tooling, no matrix validator (proposal.md rabbit-holes: "Do not write a validator for the
  matrix").
- No edits outside `openspec/changes/define-roles-and-raci/` in this round — `docs/roles-and-raci.md`
  and `README.md` are written by a later implementation phase from `tasks.md`, not by this PLAN.

## Decisions

Settled in the EPIC — cited, not re-argued: **DEC-1** (single file at docs root), **DEC-2R** (six
roles, Work Shaper = Project Owner), **DEC-3** (agent-wrapper fork stays open), **DEC-4** (role =
responsibilities-in-a-process), **DEC-5** (one-A-per-row fixes), **DEC-6/7/8/9** (row splits and
row content), **DEC-10** (capability is structure-only), **DEC-11** (cite skills, never restate),
**DEC-12** (vocabulary alignment with seed §1), **DEC-13** (Work Shaper boundary + Architect–Builder
positioning, authoritative here), **DEC-14/15** (Quality Overseer / Customer Success Manager
adaptation notes), **DEC-16** (rename-and-check pass against siblings), **DEC-17** (Known gaps
subsection).

New structuring choices made while planning this layout:

- **Matrix orientation: roles as columns, activities as rows (6 columns × 17 rows), one table.**
  Rows-as-activities keeps "one A per row" a literal one-cell-per-row scan; putting roles on rows
  would turn the invariant into a column-wise count, which is the harder direction to eyeball on a
  Markdown table. Matches the shape the EPIC already describes (proposal.md, What Changes).
- **Role blocks precede the matrix, in a fixed order**: Sales/Presales, Technical Consultant,
  Solution Architect, Work Shaper, Solution Builder, Solution Shipper. This is the funnel-to-delivery
  order the activities themselves follow (presale → delivery → nurture), so a reader meeting a role
  for the first time in the matrix has already seen its block. Work Shaper sits fourth (after
  Architect, before Builder) — deliberate: its two boundary paragraphs (DEC-13) read against a role
  already introduced (Architect) and one about to be (Builder), rather than forward-referencing both.
- **Each role block is a fixed four-line shape**: mandate (one sentence) → accountable for (bullet
  list) → skills drawn on (cited paths only, DEC-11) → artifacts produced (bullet list). Work
  Shaper's block additionally carries the two DEC-13 boundary paragraphs and the "leaning Builder"
  spectrum line as a labelled sub-block immediately after "accountable for", so the boundary reads
  before the skills/artifacts detail, not buried after it.
- **The legend precedes the matrix and states both invariants inline**: the R/A/C/I/`–` legend,
  immediately followed by two one-line invariant statements — "exactly one A per row" (DEC-5) and
  "a role is a responsibility, not a competence or a headcount" (DEC-4) — so a reader hits the rules
  before the table, not after.
- **Adaptation notes sit immediately after the matrix, before Known gaps.** Quality Overseer then
  Customer Success Manager (handbook order, p. 67 then p. 68), each one paragraph: handbook mandate →
  what replaced it → which role/mechanism now holds it, citing DEC-14/DEC-15.
- **The agent-wrapper open question is its own short subsection between the adaptation notes and
  Known gaps**, stating today's default, the reopening condition, and the DEC-3 priority order
  (Work Shaper first) as three short lines — not folded into Known gaps prose, though it is also
  listed there as an entry (DEC-17 requires the gap be *findable*, not that it live in only one
  place as a promise, since the EPIC's Known-gaps table itself lists the agent-wrapper fork as a row).
- **Known gaps is the five-row table from proposal.md, reproduced verbatim** (gap / nature / owner-
  next-step), per DEC-17 — no new gaps invented, none closed.
- **References table is last**, one row per sibling doc/skill cited anywhere above plus the handbook
  excerpt in `inputs/`, so every relative link the file makes is collected in one auditable place
  (helps the `broken_links` lint check, `tools/repo_lint/lint.py:230`, which applies to docs-root
  files with no illustrative exemption).

## Algorithm / approach

The document is a straight top-to-bottom read, no cross-referencing forward:

1. Title + one-paragraph framing (what this doc is for, who cites it).
2. Six role blocks, fixed order and fixed shape (above).
3. RACI legend + two invariants.
4. One matrix, 6 columns × 17 rows, rows in the funnel-to-delivery order proposal.md's What Changes
   section lists them (presale … partnership/account nurture).
5. Two adaptation notes (Quality Overseer, Customer Success Manager).
6. Agent-wrapper open question (three lines: default, reopening condition, priority order).
7. Known gaps subsection (five-row table, verbatim from the EPIC).
8. References table.

Worked example — the Epic/work-shaping row, the one DEC-5 and DEC-13 both touch, laid out as it
will appear in the matrix:

| Activity | Sales/Presales | Technical Consultant | Solution Architect | Work Shaper | Solution Builder | Solution Shipper |
|---|---|---|---|---|---|---|
| Epic / work shaping | – | – | C | **A/R** | C | C |

Exactly one `A` in the row (Work Shaper's cell), matching DEC-5's resolution and readable by eye —
the mechanism the "no validator" rabbit-hole relies on.

Idempotency: not applicable — this is a hand-authored static document with no retry/replay surface;
the "operation" is a one-time write per task in `tasks.md`.

### Anti-patterns

- Do not let two roles both hold `A` on the same matrix row — the one-A-per-row invariant (DEC-5)
  is violated the moment a row reads e.g. `A` under both Work Shaper and Solution Shipper.
- Do not leave a row with no `A` at all — the round-1 defect DEC-5 fixes (Requirements & UC shallow,
  CBLC both shipped with no accountable role in the draft).
- Do not restate a cited skill's content in a role block — DEC-11 forbids re-explaining what
  `skills/epic-planning/SKILL.md` or `skills/architecture/SKILL.md` already say; cite the path only.
- Do not promote Quality Overseer or Customer Success Manager to a seventh/eighth column — they are
  adaptation notes, not roles (DEC-14, DEC-15, No-gos).
- Do not fold the agent-wrapper open question's resolution into this doc — it ships open (DEC-3,
  No-gos); stating a priority order is not the same as resolving it.
- Do not build a second per-role file or a `docs/roles/` directory — DEC-1 is one file; a directory
  reopens the per-role-file sync burden the EPIC explicitly avoided.
- Do not have `define-lifecycle-playbooks`' Work Shaper playbook restate the Architect–Builder
  positioning prose — that playbook cites this doc's DEC-13; if this design duplicated that prose
  into a second location, the citation direction would break.

## Error matrix

| Failure mode | Expected handling |
|---|---|
| A future activity row is added to the matrix with no accountable role assigned | Reject at authoring time: every new row must carry exactly one `A` before it is added (DEC-5 invariant extends to future rows, not just the 17 named here); if no role fits, the row is not added and the gap is named under Known gaps instead (DEC-17), same treatment as MDLC-standalone (DEC-8). |
| A row is added with two roles both marked `A` | Same rejection: fix the row to one `A` + others as R/C/I/`–` before merging; this is a docs-review catch, not a tooling one (no validator, per rabbit-holes). |
| A relative link in the doc (to a skill, a sibling doc, or the handbook excerpt) goes stale | Caught by `tools/repo_lint`'s `broken_links` check (`tools/repo_lint/lint.py:230`) at `make validate` time — docs-root files get no `_is_illustrative` exemption, so a broken link fails validation, not just review. |
| A sibling EPIC (1–3) publishes an activity/plane/gate name that diverges from a row label already written here | DEC-16's rename-and-check pass: rename the row label to match, do not re-derive or add a new definition (rabbit-hole: "rewriting a definition, not renaming a row, is the trap"). |
| A reader tries to infer per-engagement staffing from the matrix | Explicitly out of scope — DEC-4's "not headcount" line and the No-gos "no per-engagement instantiation" entry both head this off in the doc itself. |

## Risks / Trade-offs

- **[Risk]** The agent-wrapper fork (DEC-3) is stated as genuinely undecided, ranked but open. A
  future reader could mistake the priority line ("Work Shaper is highest-priority-if-ever") for a
  commitment to build a `work-shaper` agent. → **Mitigation:** the doc states explicitly, in the
  same subsection, that this is a priority statement and not a commitment, no stub, no agent (DEC-3
  verbatim); the No-gos list backs this with "no resolution of the agent-wrapper fork" as an explicit
  boundary.
- **[Risk]** DEC-2R reverses a decision two sibling EPICs (round 1) relied on; a reader of an older
  cached view of `define-lifecycle-playbooks` could still see "five roles". → **Mitigation:** out of
  this change's control (playbooks' own artifact), but this doc's re-shape note at the top of
  `proposal.md` is the traceable record; the References table here points at the playbooks EPIC so
  a reader can check its current state rather than trust a stale memory.
- **[Trade-off]** Putting the Work Shaper's Architect–Builder boundary prose only in its own role
  block (not also summarized in the matrix) keeps the matrix compact but means a reader who only
  scans the matrix misses the nuance. Accepted: the matrix is a lookup table (DEC-10, structure
  only); the boundary reasoning belongs in prose, and the References table points every consumer at
  this doc's role-block prose, not at a duplicated summary.

## Open Questions

- The agent-wrapper fork itself (DEC-3) — does any role beyond Builder ever get a dedicated Claude
  Code agent — stays open by design. Not resolved by this design or by implementation; the doc
  states the default, the reopening condition, and the priority order, and stops there.
