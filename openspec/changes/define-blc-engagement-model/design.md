<!-- PLAN (design half). PLAN = this file + tasks.md. The clarity gate scores the pair (≥9/10).

     ALTITUDE — the reasoning: HOW + why-this-how. Cite the EPIC's DEC-n; never re-explain a settled bet.
     Acceptance criteria live in the spec deltas as GWT scenarios (WHEN/THEN), NOT here. -->

> Parent: openspec/changes/define-blc-engagement-model/proposal.md

## Context

`docs/engagement/README.md` and `phases.md` state a commercially wrong free→paid boundary
("orientation is free"; a strictly sequential P0→P1→P2→P3 funnel), and the wrong rule has already
propagated into `skills/semantic-consulting-coach/`, `skills/decision-package/`,
`skills/proposal-writing/`, and the root `README.md`. The EPIC (DEC-1..DEC-19) settles every
commercial-fact question — this PLAN only decides how to sequence and structure the documentation
work that makes those facts land: which file is written first, how the new services-skeleton table
is shaped, and how DEC-19's contract-conformance subsection satisfies `define-delivery-release-
lifecycle`'s DEC-12 content contract without waiting on that sibling change to merge first.

No code, runtime, or dependency surface is touched. This is a pure documentation/spec change inside
`docs/engagement/`, `skills/semantic-consulting-coach/references/`, five cited files, and one new
spec capability.

## Goals / Non-Goals

**Goals:**
- Every rewritten or edited file states the corrected model (DEC-1..DEC-19) consistently; no file
  left restating "orientation is free" or the old P0–P3 sequential gate.
- The `engagement-model` spec capability is the enforceable, citeable source of the corrected rules,
  independent of any one doc's wording (`openspec validate --strict` gates it).
- `docs/engagement/services-and-packages.md` exists as a skeleton (DEC-18) — rows and empty `TODO`
  cells only, no prices.
- DEC-19's contract-conformance subsection satisfies all six elements of
  `define-delivery-release-lifecycle`'s DEC-12 content contract, regardless of merge order between
  the two sibling changes.
- `.opencode/` and `docs/skill-inventory.md` regenerate clean after the skill edits.

**Non-Goals:**
- No commercial-mechanics design (pricing, rate cards, qualification scoring, CRM) — Rabbit-holes/
  No-gos.
- No new skill, agent, or role — No-gos.
- No populating the services skeleton beyond the fields this EPIC already decided (P1's frame,
  P0-advisory's duration) — DEC-18, Known gap G-7.
- No edit under `docs/ai-coding/` — that is `define-meaningfy-lifecycle` /
  `define-delivery-release-lifecycle`'s surface (No-gos).
- No redesign of `decision-package` or `proposal-writing` beyond the cited label/pointer passages
  (DEC-11).

## Decisions

All commercial-fact decisions are settled in the EPIC (DEC-1..DEC-19) — cited below by number, never
re-explained. New planning-level choices for this PLAN:

- **PLAN-D1 (spec derived from the EPIC, not from the rewritten docs)**: `specs/engagement-model/
  spec.md` is written directly from the EPIC's DEC-n text, not transcribed from the rewritten
  `README.md`/`phases.md` prose. Rationale: the spec and the docs are two independent citers of the
  same settled decisions (DEC-12); deriving the spec from the docs would make the docs the de-facto
  source of the rule and the spec a lagging copy, inverting DEC-12's own reason for existing (the
  next doc rewrite could drift and the spec would silently follow it instead of catching it).
- **PLAN-D2 (write order: spec → README → phases → services skeleton → coach reference → posture
  file → cited consistency edits → regen)**. Rationale: the spec is the stable target every later
  file can be checked against as it's written; `README.md` sets the funnel-level vocabulary that
  `phases.md` then details; the services skeleton names rows that `README.md` already introduced;
  the coach reference is rewritten only once the commercial facts it now *cites* (rather than
  states) are final; the five one-passage consistency edits go last because they are pointer-shaped
  fixes into text that must already be stable; `.opencode`/inventory regen is mechanically last
  because it mirrors whatever the skill files say at the end.
- **PLAN-D3 (services-and-packages.md table shape)**: one Markdown table, six rows — Presale,
  P0-advisory, P1 Decision, and the three DEC-5 service lines (software development,
  ontology/model development, training & capability building) — five columns: `Scope`, `Duration`,
  `Price`, `Deliverable`, `Owning skill`. Cells are `TODO` **except** where the EPIC already decided
  them: Presale's Price = "Free" (DEC-1), P0-advisory's Duration = "1–2 days" (DEC-14), P1's
  Duration = "6–8 weeks, calendar-boxed" (DEC-15). A one-line header note states the table is a
  skeleton (DEC-18) and links Known gap G-7 for who populates it next. Rationale: this is the
  cheapest structure that is simultaneously citeable, extensible per row without a reshape, and
  impossible to mistake for a priced catalogue (no row is fully populated).
- **PLAN-D4 (DEC-19 subsection wording satisfies the sibling's six-element content contract
  directly)**: the `phases.md` contract-conformance subsection is drafted to contain, in order: (1)
  the named document trail (RfO, offer, contract, meeting minutes/documented exchanges); (2) the
  Shipper accountability statement ("did we deliver what was promised?", role defined only by
  `define-roles-and-raci`); (3) the human-sign-off verdict status (not CI-automatable); (4) a
  one-line pointer to the Builder's DoD in `docs/ai-coding/dod-quality-gates.md` stating the two
  close together on two planes and neither substitutes for the other; (5) a one-line citation (not
  restatement) of the disagreement/re-shape rule that `dod-quality-gates.md` states once; (6) the
  light-touch/agent-assisted framing. Rationale: this is `define-delivery-release-lifecycle`'s
  DEC-12 content contract, cross-checked item-for-item; writing it this way means the subsection is
  correct whether the sibling change lands before or after this one (DEC-13 of that change — the
  pointer targets `docs/engagement/` at directory level if the anchor doesn't exist yet, and
  symmetrically this subsection's pointer to `dod-quality-gates.md` is directory-level-safe too).
- **PLAN-D5 (Known gaps get one shared table, restated nowhere else)**: `README.md`'s corrected TODO
  block gets a single pointer line to the EPIC's Known-gaps table rather than re-listing G-1..G-8 in
  doc prose. Rationale: the EPIC itself is the durable home for gap tracking (`proposal.md` persists
  after archiving); duplicating the table into `README.md` creates a second copy that goes stale the
  moment either is edited — the exact failure mode DEC-11 exists to fix elsewhere in this same
  change.

## Algorithm / approach

Doc/spec change applied as independent, individually-revertible file edits, each checked against the
spec as it lands. Order follows PLAN-D2:

1. Write `specs/engagement-model/spec.md` (ADDED Requirements) directly from DEC-1, DEC-3, DEC-4,
   DEC-5, DEC-6, DEC-8, DEC-14, DEC-15, DEC-16.
2. Rewrite `docs/engagement/README.md`: presale-only-free funnel, three entry points, P2 family,
   repeat-client fact, ownership statement (DEC-8), "canon" removed (DEC-13), link to the services
   skeleton, TODO block reduced per Rabbit-holes with the PLAN-D5 pointer to Known gaps.
3. Rewrite `docs/engagement/phases.md`: `P0` redefined (DEC-2), free/paid rule replaced (DEC-1), the
   sequential P1-then-P2 gate removed and replaced by the input-condition + two-elicitations
   distinction (DEC-4), P1's frame and safeguards (DEC-15, DEC-16), `P3 — Partnership` replaced by
   the repeat-client/relationship-work section (DEC-6, DEC-7), the DEC-19 contract-conformance
   subsection (PLAN-D4).
4. Add `docs/engagement/services-and-packages.md` (PLAN-D3).
5. Rewrite `skills/semantic-consulting-coach/references/engagement-model.md`: keep the coaching
   frame (cognitive states, boundary safeguard, design questions); commercial definitions become
   citations to `docs/engagement/` (DEC-8); cognitive-states table's commercial column re-mapped
   (DEC-9); "working draft" caveat scoped to method only (DEC-10); P0–P3 intentions table replaced;
   pointer to the new posture file.
6. Add `skills/semantic-consulting-coach/references/decision-phase-posture.md` (DEC-17), condensed
   from the round-2 source, cited from the coach's `SKILL.md` reference list.
7. Apply the five cited one-passage consistency edits (DEC-11): coach `SKILL.md`, `decision-
   package/SKILL.md`, `proposal-writing/SKILL.md`, coach's `semantic-consulting-domain.md`, root
   `README.md`.
8. Regenerate `.opencode/` (`make generate-opencode`) and `docs/skill-inventory.md`
   (`make skill-inventory`).

**Idempotency:** every step is a file edit or a deterministic regen command — safe to re-run;
`openspec validate --strict` plus `make lint` are the replayable checks after any subset of steps.

Worked example (the litmus the spec must catch): a hypothetical future PR that reintroduces "a
scoping call is a free courtesy" into any doc — `openspec validate --strict` does not itself catch
prose drift, but the spec's Requirement on presale-is-the-only-free-stage gives reviewers and
`repo_lint`'s `broken_links`/citation checks a stable requirement id to check the PR against, and any
sibling epic can cite it instead of re-deriving the rule.

### Anti-patterns

- Restating the commercial rules inside the coach's `engagement-model.md` instead of citing
  `docs/engagement/` (breaks DEC-8's ownership split — the exact inversion this change fixes).
- Populating any `services-and-packages.md` cell beyond what DEC-18 already decided (turns a
  skeleton into a half-priced catalogue — Rabbit-holes).
- Writing the DEC-19 subsection as if it must wait for `define-delivery-release-lifecycle` to
  merge first (violates PLAN-D4/coordination-by-content; blocks this change on a sibling
  unnecessarily).
- Re-deriving the spec's requirement text from the rewritten `README.md`/`phases.md` prose instead
  of from the EPIC's DEC-n (PLAN-D1 — creates a second, driftable source).
- Duplicating the Known-gaps table into `README.md` prose (PLAN-D5 — creates a second copy that goes
  stale silently, per the EPIC's own closing risk note).
- Renumbering phases or inventing `P2a/P2b/P2c` (DEC-2, DEC-5 — explicitly foreclosed, not reopened
  by this PLAN).
- Expanding `decision-phase-posture.md` into objection-handling / sales-script content (DEC-17
  bound).
- Skipping the `.opencode`/`skill-inventory` regen step — leaves the committed mirror
  inconsistent with the edited skill sources, which `make lint` is expected to catch.

## Error matrix

| Failure mode | Expected handling |
|---|---|
| A consumer (human or agent) still reads the old free-P0 definition from a cached doc or stale mirror | `.opencode/` regen (step 8) plus `repo_lint`'s `broken_links`/staleness checks catch drift in the committed mirror; the spec requirement gives a stable id to cite when correcting the reader |
| A sibling epic (`define-delivery-release-lifecycle`, `define-roles-and-raci`, `define-lifecycle-playbooks`) is authored against the pre-correction model before this change merges | Not this change's failure to prevent — but the spec capability (DEC-12) exists precisely so any sibling can cite `engagement-model`'s requirements once this change lands, rather than re-deriving the (wrong) old model |
| `define-delivery-release-lifecycle` merges before this change and its pointer target (`docs/engagement/`) doesn't yet have the DEC-19 subsection | That sibling's own DEC-13 covers it: the pointer targets `docs/engagement/` at directory level, not a section anchor, until this change lands |
| This change merges before `define-delivery-release-lifecycle` and the DEC-19 subsection cites a disagreement rule not yet written in `dod-quality-gates.md` | The one-line citation is written as a citation-by-topic ("see the Builder/Shipper disagreement rule in `dod-quality-gates.md`"), not a section anchor, so it resolves once the sibling lands; `broken_links` treats the directory-level reference as valid |
| A future contributor adds a price or rate to `services-and-packages.md` | Out of `openspec validate`'s reach (prose, not schema) — caught at review time by the DEC-18 rationale note in the doc header and by this design's anti-pattern list |
| `openspec validate --strict` fails on the new spec (missing scenario, wrong hashtag count) | Fix before commit — the four-hashtag `#### Scenario:` rule is easy to miscount; each requirement is checked to have ≥1 scenario before tasks.md is marked done |
| `make generate-opencode` or `make skill-inventory` produces a diff after the skill edits but it isn't committed | `make lint` gates this (existing repo convention); task 8's verification step runs both makes and re-checks git status is clean |

## Risks / Trade-offs

- **Risk:** `P0`'s meaning change (DEC-2) confuses a reader who only saw the old model. →
  **Mitigation:** every live restatement is corrected in the same change (DEC-11); no prospect-facing
  template uses the bare label "P0" (verified in the EPIC's Impact section), so the blast radius is
  internal docs only.
- **Risk:** Known gaps (G-1..G-8) are named with no owner and could be silently closed elsewhere
  without the table being updated. → **Mitigation:** PLAN-D5 keeps one single copy of the table (in
  the EPIC) rather than forking it into `README.md`, so there is exactly one place to keep current.
- **Risk:** DEC-19's coordination-by-content with a sibling still-in-flight change could drift if
  either side's wording changes after this PLAN is derived. → **Mitigation:** PLAN-D4 lists the six
  required elements explicitly so a reviewer can diff the shipped subsection against the contract
  directly, independent of merge order.
- **Trade-off:** Deriving the spec directly from the EPIC (PLAN-D1) rather than from the rewritten
  docs means the spec and the docs are authored somewhat in parallel rather than one mechanically
  generating the other — slightly more authoring effort, traded for the spec staying an independent
  check rather than a lagging mirror.

## Open Questions

Parked, not guessed at — carried forward from the EPIC's own Known-gaps section (G-1..G-8), unowned
by design:

- **G-1 / G-5**: What is the presale-to-contract process, and what external sales/closing
  methodology feeds it? Not designed here; possibly a future doc or skill.
- **G-2**: How is a demo scoped, built, rehearsed, and bounded in what it may promise? Not designed
  here; likely a future skill.
- **G-3**: How is CRM/lead communication handled (meeting-minutes grooming, lead cadence)? Not
  designed here; likely a future skill.
- **G-4**: Does a strategic-negotiation/relationship-thinking skill or agent belong in the catalogue,
  and what does it contain? Named only, per the human's precise ask; not designed here.
- **G-6**: What are the contractual mechanics behind the safeguards mechanism (extension pricing,
  partial-delivery entitlements, notice periods)? Out of this change's appetite; likely a
  contractual/legal artifact, not a skill.
- **G-7**: Who populates `services-and-packages.md`'s TODO cells, and on what cadence? This change
  adds the skeleton only; populating it is explicitly deferred, owner TBD.
- **G-8**: Does MDLC-standalone ontology/application-profile methodology need its own shaping round?
  Parked by the round-1 seed for its own cycle; out of scope here.
