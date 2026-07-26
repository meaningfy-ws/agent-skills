# EPIC: Delivery & Release — build-tier DoD for the Builder, contract-conformance DoD on the commercial plane

> **Golden-thread parents:**
> [`inputs/2026-07-25-brainstorm-seed.md`](inputs/2026-07-25-brainstorm-seed.md) §4 (the Delivery &
> Release resolution) and §7 (the stale ownership line + the `dod-quality-gates.md` split);
> [`inputs/2026-07-26-handbook-and-advisory-findings.md`](inputs/2026-07-26-handbook-and-advisory-findings.md)
> (round-2 human directives + the Employee Handbook's "Project shipping / Contractual Validation"
> content — full source at
> [`define-lifecycle-playbooks/inputs/`](../define-lifecycle-playbooks/inputs/));
> [`.claude/HARD-QUESTIONS.md`](../../../.claude/HARD-QUESTIONS.md) HQ-08.1 (the commercial layer is
> unshaped — this change removes its second copy);
> [`spine/golden-thread.md`](../../../spine/golden-thread.md) (citation discipline).
> **Sibling changes, cited not restated:** `define-blc-engagement-model` (owns `docs/engagement/` —
> the destination for both the removed engagement gates **and** the Shipper's DoD, per DEC-11),
> `define-meaningfy-lifecycle` (owns the PROJECT-tier / ADLC / MDLC narrative and may relocate the
> ownership table's host file), `define-roles-and-raci` (owns the definition of the Builder and
> Shipper roles), `define-lifecycle-playbooks` (consumes all of the above).

## Appetite

**Small.** One doc restructured, one table row corrected, one content contract handed to a sibling
change, one new capability spec. If this grows into authoring engagement content, defining roles,
building a shipping/PM process, or automating a contract-conformance gate, the bet is being overrun —
stop and re-scope.

## Why

[`docs/ai-coding/dod-quality-gates.md`](../../../docs/ai-coding/dod-quality-gates.md) calls itself
"the single authority" for the gate ladder but serves two audiences from one file by an explicit past
decision (`Q8.2=A`, quoted in its own preamble): human/commercial engagement gates *and* the
automated build-tier DoD. That decision produced the opposite of a single authority — its
"Commercial layer — TODO" block is duplicated near-verbatim in
`docs/engagement/README.md` §35 (that path was later retired by a follow-up restructure into
`docs/how-we-work/business/`; unlinked here for historical accuracy), so the unshaped commercial
layer now has two homes and no owner.

Two related defects sit on top of it. First, the DoD ladder ends at "code review passed" and
"archived into `openspec/specs/`" — nothing anywhere says who is accountable that what shipped matches
what the *client bought*, so the closing moment of a contract has no documented owner. That check is
not a missing paragraph in a build doc; it is a whole step of how Meaningfy already works that was
never carried into the repo. The Employee Handbook's shipping chapter opens the Shipping Process with
**"Contractual Validation: review the deliverables against the contractual agreement"** — real,
practised, and entirely absent from `docs/`. Second, the ownership table in
[`docs/ai-coding/build-lifecycle.md`](../../../docs/ai-coding/build-lifecycle.md) §5
still points CD/release at `ci-cd-delivery (EPIC-10, future)` when `ci-cd-delivery`,
`meaningfy-release`, and `meaningfy-git-workflow` all shipped months ago — a reader following that
row concludes we have no release capability at all.

**Why now:** four sibling changes rewrite the surrounding narrative in this same round. Leaving this
file mixed would strand the new engagement docs against a second, contradicting copy of their own
content, and leave the delivery accountability that epic 4's RACI matrix depends on undefined.

## Solution outline

`dod-quality-gates.md` becomes **single-audience**: build-tier only. The engagement-gates table and
the commercial TODO are deleted (not copied, not rephrased) and replaced by one pointer to
`docs/engagement/`, whose wording `define-blc-engagement-model` owns. The measurable outcome: zero
duplicated commercial paragraphs across `docs/`, and one home per audience.

The **dual accountability at delivery** survives that split intact, but it stops being one section in
one file. Two Definitions of Done close at the same event on two different planes and do not
substitute for each other — and each now lives on its own plane's shelf:

- The **Builder's DoD** (SDLC-plane) asks whether the shipped increment matches the EPIC and the
  architecture. That is the existing ladder, now explicitly labelled Builder-side, and it **stays in
  `dod-quality-gates.md` in full**.
- The **Shipper's DoD** (commercial plane) asks whether the shipped increment matches what was
  promised in the documents exchanged with the client — the request for an offer, the offer, the
  contract, the meeting minutes and documented exchanges, and any other document recording a need and
  our agreement to fulfil it. That question is answered against documents the repository does not
  hold, by a human reading commercial correspondence, at a cadence a build doc does not govern. It is,
  in the human's words, *"clearly a document part of the commercial bulk of the documentation not
  SDLC"* — so it **moves to `docs/engagement/`** (DEC-11), specified here, authored by
  `define-blc-engagement-model`.

What remains in `dod-quality-gates.md`'s Delivery & Release section is therefore the Builder's DoD in
full, a one-line pointer to where the Shipper's DoD now lives, the disagreement rule, and citations of
the skills that own release mechanics — and no commercial or contract content whatsoever. The
disagreement rule is the load-bearing one: if the two verdicts conflict, neither role overrides the
other; the EPIC and the contract have drifted and the change is re-shaped. It is stated once, in this
file, and stated as applying to **both** DoDs regardless of which file each lives in.

Finally the stale ownership row is corrected in place to cite the skills that actually exist, split
by concern so the same staleness cannot hide again, and the delivery section points at those skills
for the *how* rather than restating any of it.

## Key decisions

- **DEC-1**: **`dod-quality-gates.md` becomes single-audience build-tier DoD**, reversing `Q8.2=A`.
  The reversal is recorded as *superseded* in the change record, not silently dropped — the original
  rationale ("one legible sequence from selling to building") is real but was better served by a
  pointer: two audiences with different cadences and different enforcement (human sign-off vs CI)
  were sharing one "single authority", and the shared file demonstrably produced a duplicate rather
  than a sequence.
- **DEC-2**: **Delete here, do not migrate.** This change removes the engagement-gates table and the
  commercial TODO from `dod-quality-gates.md` and leaves a one-line pointer; it authors **no**
  replacement text under `docs/engagement/`. Rationale: the content already exists there in TODO form,
  so nothing is lost even if `define-blc-engagement-model` lands later, and two agents must not write
  the same paragraph. DEC-11 applies the same rule to the Shipper's DoD.
- **DEC-3**: **Delivery & Release is two co-closing DoDs on two planes, not a stage and not a
  sequence** — Builder ↔ EPIC/architecture spec (SDLC-plane), Shipper ↔ the agreement documents
  exchanged with the client (commercial plane). Taken directly from the seed §4; documented as paired
  accountability, never as "builder finishes, then shipper checks". **Revised in round 2:** the two
  DoDs are also two *documents*, in two directories, one per plane (DEC-11). The pairing is asserted
  by reciprocal one-line pointers, not by co-location — co-location was never what made them paired.
- **DEC-4**: **The Shipper's DoD is a third question, not a re-run of the existing two.**
  `dod-quality-gates.md`'s "built right (verification) / right thing built (validation)" pair both
  measure against the EPIC and stay Builder-side. The third question — "did we deliver what was
  promised?" — measures against the contract, so the file **names** it and points to it rather than
  answering it. Rationale (own call, seed §4 states the dual accountability but not this framing): an
  EPIC can be perfectly satisfied while the contract is under-delivered, and vice versa, so folding
  contract conformance into "validation" would erase exactly the distinction this change exists to
  make. Naming-and-pointing preserves the distinction without pulling commercial content back into a
  build doc.
- **DEC-5**: **The Shipper's DoD is a human sign-off and is not CI-automatable — and that declaration
  travels with the DoD to `docs/engagement/`.** `dod-quality-gates.md`'s "automation boundary"
  section gains **no** new entry, and the Shipper's DoD is **not** a row in the build-tier gate-set
  table. **Revised in round 2** (previously: declare it in the automation boundary). Rationale: that
  boundary section is a single source other skills already cite
  ([`skills/project-setup/references/ci-and-infra.md`](../../../skills/project-setup/references/ci-and-infra.md)),
  and it enumerates *build-tier gates* — listing a gate that is not in the file and not in the build
  tier would re-import the two-audience defect DEC-1 removes. The non-automatable status is not
  dropped; it is a required element of the content contract in DEC-12.
- **DEC-6**: **The stale row is replaced by two rows split by concern, not one merged row** — `CD /
  deploy` → [`ci-cd-delivery`](../../../skills/ci-cd-delivery/SKILL.md), `Release lifecycle
  (versioning, changelog, publish)` → [`meaningfy-release`](../../../skills/meaningfy-release/SKILL.md)
  — and the delivery section cross-references the table's **already-present**
  `meaningfy-git-workflow` row for branch/commit/PR mechanics instead of adding a third, duplicate
  row. Rationale: the merged "CD / release" row is what let the staleness hide; the split boundary is
  already asserted in those skills' own Boundary sections, so the doc cites it rather than inventing a
  variant.
- **DEC-7**: **The fix follows the content, not the path.** The ownership table lives in
  `two-tier-methodology.md` §5 today; if `define-meaningfy-lifecycle` renames or relocates that file
  first, this change edits the row wherever the table then lives. No second copy of the table is
  created under any circumstances.
- **DEC-8**: **Roles are referenced, not defined — in either file.** "Builder" and "Shipper" appear
  only as accountabilities attached to a DoD, each linking to `define-roles-and-raci`'s output for the
  role definition. **Extended in round 2:** this now binds two files rather than one — the content
  contract in DEC-12 carries the same prohibition, so relocating the Shipper's DoD does not create a
  second de-facto role definition on the commercial side. Rationale: two docs defining the same role
  is the exact failure mode this whole round is fixing, and a relocation is precisely when such a
  definition tends to get re-written from scratch.
- **DEC-9**: **One new capability, `delivery-release-dod`**, carries the durable invariants as
  RFC-2119 requirements: one audience per file; the Builder's DoD present in the build doc; the
  Shipper's DoD present in the engagement docs with the document trail of DEC-12; a live pointer in
  each direction; the disagreement rule stated once; no stale owner citation. Scoping it to the
  *contract between the two documents* rather than to one file's contents is what keeps the invariant
  enforceable after DEC-11's split. `release-lifecycle` and `catalogue-governance` were checked and
  are **not** modified — the former governs the `meaningfy-release` skill's ownership, not the
  `docs/ai-coding/` narrative.
- **DEC-10**: **When the two DoDs disagree, it is a divergence to re-shape — not an override.** If the
  Builder's DoD passes and the Shipper's fails (or the reverse), neither role's verdict wins by
  seniority; the mismatch means the EPIC and the contract have drifted apart, which is
  [`epic-planning`](../../../skills/epic-planning/SKILL.md)'s "EPIC-level wrongness" case, resolved by
  a logged re-shape. Rationale (own call — the seed says the two DoDs "close together" and neither
  substitutes for the other, but does not say what happens when they conflict; leaving that gap would
  make the dual DoD unusable the first time it fired). **Unchanged by DEC-11's split:** the rule is
  written once, in `dod-quality-gates.md`, explicitly scoped to both DoDs *regardless of which file
  each lives in*; the engagement side cites that sentence rather than restating it. The doc **cites**
  the re-shape path; it does not invent an escalation ladder.
- **DEC-11**: **The Shipper's DoD moves out of `docs/ai-coding/` and into `docs/engagement/`; the
  build doc keeps a one-line pointer.** *(New in round 2 — the human explicitly reopened this
  change's own No-go: "unless you decide to put the second dod there". Decision: move it.)*
  Rationale, in the human's words: *"this shipping/business delivery is clearly a document part of the
  commercial bulk of the documentation not SDLC."* Three things confirm it independently: the DoD is
  checked against artifacts the repository does not hold (offers, contracts, minutes); its enforcement
  is human sign-off on a commercial cadence, not CI on a per-Epic cadence; and its handbook ancestor
  sits in the shipping chapter, next to handover and client demonstration, not in any engineering
  standard. Keeping it in a build-tier file would have re-created, one round later, exactly the
  two-audiences-one-file defect DEC-1 exists to remove. The **Builder's DoD stays in
  `dod-quality-gates.md`** unchanged in placement — that one is genuinely SDLC-plane.
- **DEC-12**: **This change specifies the Shipper's DoD; `define-blc-engagement-model` writes it.**
  *(New in round 2.)* Per DEC-2's rule that two agents must not author the same paragraph, and because
  epic 1 is editing `docs/engagement/` in this same round, this proposal hands over a **content
  contract**, not prose. The relocated Shipper's DoD MUST contain, in whatever wording epic 1 chooses:
  1. **The document trail it checks against**, named concretely — the request for an offer, the offer,
     the contract, the meeting minutes and documented exchanges, and any other document recording a
     client need and our agreement to fulfil it, and how. (Human's own enumeration; matches the
     handbook's Contractual Validation step — *"review the deliverables against the contractual
     agreement"* — and the Work Shaper's mandate, which builds the work breakdown from that same
     trail. Checked back against its own source, one lifecycle later.)
  2. **The accountability**: the Shipper answers "did we deliver what was promised?", with the role
     itself defined only by `define-roles-and-raci` (DEC-8).
  3. **The verdict's status**: human sign-off, explicitly not CI-automatable (DEC-5).
  4. **The pairing**: a one-line pointer back to the Builder's DoD, stating that the two close
     together, on two planes, and that neither substitutes for the other (DEC-3).
  5. **The disagreement rule**: a one-line citation of DEC-10's re-shape path in
     `dod-quality-gates.md` — cited, never restated.
  6. **The light-touch framing**: the check is a human judgement that MAY be agent-assisted — an agent
     can read the document trail and draft the conformance summary; the human signs. This is the
     round's standing adaptation of pre-LLM-agent practice ("people govern, steer and check lightly").
     What it is not: a mandated tool, a required artifact, or an automated gate.

  Deliberately **not** in the contract: exact section title, file (`README.md`, `phases.md`, or a new
  engagement doc — epic 1's call), tone, and any ordering relative to epic 1's other content.
- **DEC-13**: **The pointer is written even if epic 1 has not landed; the contract lives in the spec,
  not in a hand-off note.** *(New in round 2.)* Implementation of this change is not blocked on
  `define-blc-engagement-model` (consistent with DEC-7's follow-the-content rule). If the destination
  section does not yet exist when this change is implemented, the pointer targets
  `docs/engagement/` at directory level rather than a section anchor, and DEC-12's six required
  elements stand as RFC-2119 requirements in the `delivery-release-dod` capability. Rationale: the
  failure mode of a relocation is that the content evaporates in the gap between two changes — putting
  the contract in the spec delta rather than in prose means the obligation is validated, not
  remembered. A dangling pointer is a visible, fixable defect; an unwritten DoD is not.

## Rabbit-holes

- **Do not build a PM process.** The Shipper's DoD is a checklist in a document — not an
  acceptance-certificate artifact, a sign-off form, a new `openspec/` artifact type, or a workflow.
  This holds after DEC-11's relocation: moving the DoD to the commercial plane is not licence to
  author the surrounding shipping process there. **This rabbit-hole is a bounded scope limit, not a
  settled question — see [Known gaps](#known-gaps) G1.**
- **Do not read "close together" as simultaneity.** It is dual accountability at one closing event,
  not a same-commit or same-day timing rule. Writing a timing constraint would create an unenforceable
  requirement.
- **Do not make contract conformance CI-enforceable** (see DEC-5). It is semantic judgement against a
  contract the repo does not hold.
- **Do not grow DEC-10 into a dispute-resolution procedure.** One sentence naming the re-shape path is
  the whole of it; roles, approvers, and timelines belong to `define-roles-and-raci` if anywhere.
- **Do not write the engagement-side prose** (DEC-12). The content contract is the deliverable; the
  temptation to draft "just a placeholder paragraph" for epic 1 to overwrite is the same
  two-agents-one-paragraph failure DEC-2 exists to prevent.
- **Dependency, not a blocker:** epics 1 and 2 own the destination doc and the ownership table's host
  file respectively. Shape and implement against today's paths; if either lands first, follow the
  content (DEC-7, DEC-13) and adjust the pointer target. Do not wait for them, and do not pre-empt
  their wording.
- **Do not re-tune any threshold.** ≥9/10 clarity gate, ≥80% coverage, "no open Critical findings" are
  restructured in place, never re-argued here.
- **Resist expanding the ownership-table edit.** Exactly one stale row is in scope. The missing
  ADLC/MDLC rows and the MDLC-standalone gap belong to `define-meaningfy-lifecycle`.
- **Do not resolve HQ-08.1.** After this change the commercial TODO has one home; whether the
  commercial layer gets shaped at all is a separate future workstream.

## Known gaps

Named here, deliberately not closed by this change. Each is a real absence, not a deferred nicety.

- **G1 — There is no shipping/delivery process, only a conformance check.** The Employee Handbook's
  shipping chapter runs six steps: Contractual Validation, Documentation and Preparation, Delivery
  Scheduling, Delivery Execution, Client Demonstration, Final Approval and Handover — plus formalities
  (deliverable demo, meeting minutes, official email to the client). This change carries **only step
  1** across, as the Shipper's DoD. Steps 2–6 have no home in `docs/` and no owner in the skill
  catalogue. That is a genuine gap in how a Meaningfy delivery closes, and it is what the "do not
  build a PM process" rabbit-hole is protecting this Small bet from — it bounds *this* change; it does
  not declare the question answered. A future change must decide whether these steps belong to
  `docs/engagement/`, to a Shipper playbook under `define-lifecycle-playbooks`, or to a new skill;
  none of the three is obviously right today, which is precisely why it is not decided here.
- **G2 — Agent-assisted contract review has no mechanism.** DEC-12 permits the conformance summary to
  be agent-drafted, but the documents live outside the repository (email, drive, CRM) and no skill
  covers ingesting them. Until something does, "agent-assisted" is a permission, not a capability.
- **G3 — The rework path after a failed Shipper's DoD is undefined here.** DEC-10 routes a
  Builder/Shipper *disagreement* to a re-shape, but says nothing about a client rejecting an accepted
  delivery. The handbook's **Redelivery Policy** (close the initial Epic regardless, open a dedicated
  redelivery Epic with its own appetite and pitch, never reopen the closed one) and its
  **"Improvements Outside Contract"** dedicated-EPIC pattern are the practised answers, and both are
  named as gaps by `define-meaningfy-lifecycle`. Cross-referenced here because a failed contract
  conformance is their most likely trigger; **not duplicated, and not owned here.**
- **G4 — The relocation's second half is owed by a sibling change.** DEC-11 moves the Shipper's DoD to
  a file this change does not edit. DEC-13 keeps the obligation visible in the capability spec rather
  than in a hand-off note, but until `define-blc-engagement-model` lands its side, the split DoD is
  half-written by design. Tracked, not hidden.

## No-gos

- **No edits to any file under `docs/engagement/`** — that is `define-blc-engagement-model`'s output.
  This survives DEC-11 unchanged: the Shipper's DoD *content* moves there, but this change contributes
  it as a specification (DEC-12), not as an edit. Every word under `docs/engagement/` is still written
  by epic 1.
- **No PROJECT-tier / ADLC / MDLC / v1-retirement work** — that is `define-meaningfy-lifecycle`. In
  particular, v1 (`ai-coding-methodology.md`, `ai-coding-runbook.md`, `ai-coding-setup-guide.md`) is
  not touched, even though it links to `dod-quality-gates.md`.
- **No role definitions and no RACI matrix** — that is `define-roles-and-raci` (DEC-8).
- **No new skills and no new agents or agent stubs**, and no changes to any existing `SKILL.md`.
- **No new documentation file authored by this change.** It restructures existing files only; whether
  the Shipper's DoD lands in an existing `docs/engagement/` file or a new one is epic 1's call
  (DEC-12), and a new synthesis doc is `define-lifecycle-playbooks`' territory.
- **No shipping-process, handover, or redelivery content** — Known gaps G1 and G3 name these; naming
  is the whole of the treatment they get here.
- **No CI/workflow changes** — no GitHub Actions, no `Makefile` targets, no new validator rules beyond
  at most additive tags in `tests/ownership.yaml` (see Impact).
- **No work on the MDLC-standalone capability gap** — parked for its own shaping cycle.
- **No renaming of "two-tier" or removal of "canon"** anywhere in this change, despite the seed §1
  terminology rules — renaming is epic 2's, and doing it here would collide mid-round.

---

## What Changes

- **BREAKING (doc contract)** — Remove the **"Engagement gates (human / commercial)"** section from
  `docs/ai-coding/dod-quality-gates.md` in full: the four-row table (including its `Build DoD` row,
  which is redundant with the build-tier table below it), the **"Commercial layer — TODO"** blockquote,
  and the `Q8.2=A` "one ladder with two clearly-separated halves" paragraph. Replace with a single
  pointer to `docs/engagement/`. Any consumer relying on that file for engagement gates must follow
  the pointer.
- Rewrite the file's **Purpose/Audience** header so its stated scope is build-tier DoD only.
- Add a **Delivery & Release** section carrying the following four elements and **no commercial or
  contract content** (DEC-11):
  1. the **Builder's DoD** in full — SDLC-plane, conformance to the EPIC + architecture, with its
     accountability named and the role definition cited (DEC-3, DEC-8);
  2. a **one-line pointer** to the Shipper's DoD in `docs/engagement/`, stating that the two close
     together on two planes and neither substitutes for the other (DEC-13 governs the pointer target
     if epic 1 has not landed);
  3. the **disagreement rule** (DEC-10), stated once and explicitly scoped to both DoDs regardless of
     which file each lives in;
  4. **release-mechanics citations** — [`ci-cd-delivery`](../../../skills/ci-cd-delivery/SKILL.md)
     (CD/deploy), [`meaningfy-release`](../../../skills/meaningfy-release/SKILL.md)
     (versioning/changelog/publish), and
     [`meaningfy-git-workflow`](../../../skills/meaningfy-git-workflow/SKILL.md) (branch/commit/PR) —
     links only, no restatement of what those skills own.
- Re-anchor **"The two questions"** as Builder-side, and name the third, contract-conformance question
  as belonging to the Shipper's DoD — naming and pointing, not answering (DEC-4).
- **No change to "The automation boundary"** section (DEC-5, revised) — the Shipper's DoD is not a
  build-tier gate and is not listed there; its non-automatable status is a required element of the
  content contract instead.
- Replace the stale `CD / release | ci-cd-delivery (EPIC-10, future)` row in the ownership table
  (today `docs/ai-coding/two-tier-methodology.md` §5) with two concern-split rows citing the existing
  skills, preserving the "CI vs CD do not overlap" note (DEC-6, DEC-7).
- Add the `delivery-release-dod` spec delta (DEC-9), carrying DEC-12's six required elements of the
  Shipper's DoD as RFC-2119 requirements on the engagement-side document.
- **Hand-off, not an edit:** DEC-12's content contract is delivered to `define-blc-engagement-model`,
  which authors the Shipper's DoD under `docs/engagement/`. This change writes no prose there.

## Capabilities

### New Capabilities

- `delivery-release-dod`: the documentation contract for delivery across both planes — that
  `dod-quality-gates.md` carries build-tier DoD only (no engagement/commercial gates); that the
  **Builder's DoD** lives there in full; that the **Shipper's DoD** lives in the engagement
  documentation and names the concrete document trail it checks against (RfO, offer, contract, meeting
  minutes and documented exchanges, other agreement documents), its accountability, and its status as
  non-CI-automatable human sign-off that may be agent-assisted; that each document carries a live
  pointer to the other and neither is presented as substituting for or sequentially following the
  other; that a disagreement between them routes to a logged re-shape rather than an override, stated
  once and scoped to both; and that delivery/release/CD ownership cites only skills that exist in the
  catalogue.

### Modified Capabilities

None. `release-lifecycle` and `catalogue-governance` were both checked: neither's requirements change
(the former scopes the `meaningfy-release` skill's ownership, not the `docs/ai-coding/` narrative).

## Impact

**Files edited (2):**

| File | Change |
|---|---|
| [`docs/ai-coding/dod-quality-gates.md`](../../../docs/ai-coding/dod-quality-gates.md) | Sections removed (engagement gates, commercial TODO, `Q8.2=A` paragraph); Delivery & Release section added (Builder's DoD + pointer + disagreement rule + mechanics citations); purpose header and "two questions" revised. Automation boundary **untouched** (DEC-5) |
| [`docs/ai-coding/build-lifecycle.md`](../../../docs/ai-coding/build-lifecycle.md) §5 | One stale ownership row → two correct rows. Path already moved by `define-meaningfy-lifecycle` (DEC-7); follow the content |

**Files specified but not edited (1):** a file under `docs/engagement/` gains the Shipper's DoD per
DEC-12's content contract, authored by `define-blc-engagement-model`. Exact file and wording are epic
1's call; the obligation is carried as RFC-2119 requirements in the `delivery-release-dod` capability
so it cannot be lost between the two changes (DEC-13).

**Inbound links — verified safe.** Every live inbound reference to `dod-quality-gates.md` targets the
**build-tier** half, so the deletion breaks no link:
`docs/engineering-standards/testing-standard.md:56` (coverage), `docs/ai-coding/opsx-runbook.md:8`,
`docs/ai-coding/two-tier-methodology.md:8` ("the build-tier gate set"),
`skills/project-setup/SKILL.md:85` and `skills/project-setup/references/{ci-and-infra.md:62,68,81,
spine-projection.md:96, interview.md:50}` (all the automation boundary — which DEC-5's revision now
leaves entirely unmodified, removing the only risk to those five citations). The only inbound
reference from v1 (`docs/ai-coding/ai-coding-methodology.md:11,239`) is being retired by
`define-meaningfy-lifecycle` and is not touched here.

**Dual-CLI mirror:** none needed. `.opencode/skills/**` is generated from `skills/**`; this change
touches no skill file and no doc path that skills link to, so no regeneration is required.

**`tests/ownership.yaml` — candidate additive tags, deliberately unresolved.** The file carries no
delivery/release tag today, so the newly-explicit split has no tripwire. Two additive candidates
(exact tag names and `claim_patterns` to be settled in the PLAN, not here): one for CD/deploy owned by
`ci-cd-delivery`, one for the release lifecycle owned by `meaningfy-release`. Any addition is purely
additive — no existing tag is renamed or re-owned — and the validator's flags are non-blocking, so the
worst case of getting a pattern slightly wrong is a spurious warning, not a broken build. If the PLAN
finds no pattern specific enough to avoid false positives on legitimate citations, adding no tag is an
acceptable outcome.

**Known dangling reference, not owned here:** `.claude/HARD-QUESTIONS.md` HQ-08.1 states the
commercial TODO is stubbed "in `docs/engagement/` and the DoD ladder". After this change only the
first is true. HQ-08.1 is a commercial-layer question — updating its text belongs with
`define-blc-engagement-model` or a follow-up; this change does not edit `.claude/`.

**No runtime impact.** No Python, no CI configuration, no `spine/` conventions, no schema changes, no
dependency changes. Documentation and one spec delta only.
