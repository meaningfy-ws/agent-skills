# EPIC: The build-plane lifecycle — retire v1, name ADLC / MDLC-lite / SDLC

**Golden-thread parents:** [`inputs/2026-07-25-brainstorm-seed.md`](inputs/2026-07-25-brainstorm-seed.md)
§§1, 3, 4, 7, 8; [`inputs/2026-07-26-handbook-findings.md`](inputs/2026-07-26-handbook-findings.md)
§§1–5 (Employee Handbook 2nd ed. excerpt + the round-2 governance quote); and
[`inputs/handover-analysis.md`](inputs/handover-analysis.md) (findings 1–4);
spine conventions [`spine/workflows.md`](../../../spine/workflows.md),
[`spine/golden-thread.md`](../../../spine/golden-thread.md),
[`spine/epic-change-memory-mapping.md`](../../../spine/epic-change-memory-mapping.md).
**Siblings (cited, never restated):** `define-blc-engagement-model` (engagement/commercial),
`define-delivery-release-lifecycle` (DoD + delivery/release), `define-roles-and-raci` (roles + RACI),
`define-lifecycle-playbooks` (big-picture + per-role views).

## Appetite

**Medium.** One doc rewritten and renamed, three deleted, one Mermaid diagram and one responsibility
table adapted, one governance-model paragraph added, six inbound link retargets, two one-line rules
in `tools/repo_lint/lint.py`, one spec delta. No new skills, no new agents, no new bundle, no runtime
code. Round 2 (post-review) adds one short paragraph to the rewrite and two *named-only* gaps in this
EPIC — appetite is unchanged, because naming a gap costs nothing to build.

## Why

`docs/ai-coding/` carries **two live, contradictory definitions of how we build**. v1
(`ai-coding-runbook.md`) still describes a single-file `EPIC.md` holding spec+plan+roadmap and routes
work through `gherkin-writer` and `documenter` agents that **do not exist in `agents/`** — and it is
the more obviously-named file (no `v1` in the filename), so a developer who opens it first gets the
stale model and tries to invoke agents that were retired. Its sunset condition ("kept live until the
first real engagement closes") has no owner, no date, and no way to verify.

The successor, `two-tier-methodology.md`, is right about artifacts but wrong about narrative in five
specific ways: (a) it has **no diagram at all** — a regression against the deprecated doc it
superseded, whose lifecycle Mermaid diagram and Developer-vs-Agent table are still the best
onboarding artifacts in the repo; (b) its entire PROJECT tier is **four one-line bullets** that never
name architecture (ADLC) or modelling (MDLC-lite), so the two most expensive human-led steps of a
build contract are invisible even though `architecture`, `conceptual-modelling`, `linkml-engineering`,
`modelling-conventions` and `project-setup` are all mature and shipping today; (c) it calls itself
"two-tier", a frame that undercounts the real structure now that commercial, architecture, modelling,
building and delivery are distinct concerns; (d) it treats Requirements & UC as a pipeline *stage*
when it is one capability invoked at two depths, and its ownership table still asserts that CD/release
is `ci-cd-delivery (EPIC-10, future)` — false since the day that table was written; (e) it never
states **who is supposed to be doing the work** — it describes gates without saying that agents
execute and humans steer, so a reader cannot tell how much attention each gate is meant to cost them.

**Why now:** this is one of five parallel epics redefining the lifecycle documentation; the four
siblings all point *into* the build-plane doc, so it must stop being ambiguous about which of the two
live definitions is real before they can cite it.

## Solution outline

**One doc owns the build plane, end to end, with every step naming its single owning skill — and
saying who steers it and who executes it.**

`docs/ai-coding/two-tier-methodology.md` becomes `docs/ai-coding/build-lifecycle.md`: the same three
correct v2 foundations (EPIC/PLAN split, single-owner ownership table, no-double-spec normative
layering) carried forward, with the PROJECT tier expanded from four bullets into **named steps that
cite their owners** — Requirements & UC (a capability at two depths, `architecture`'s UC White/Blue),
**ADLC** (`architecture`: ADRs, C4, UC White/Blue), **MDLC-lite** (`conceptual-modelling` +
`linkml-engineering`, cross-checked by `modelling-conventions`), project/repo setup
(`project-setup`) — and with **SDLC scoped precisely to the EPIC-tier build loop** (shape EPIC →
derive PLAN → clarity-gate → BDD → TDD → review → archive), not used as a synonym for the whole build
contract. The two salvageable v1 artifacts are **adapted, not ported**: the lifecycle diagram is
redrawn for the current reality (EPIC ≡ `proposal.md`, PLAN ≡ `design.md` + `tasks.md`, the
three-wrapper agent roster, OpenSpec-native paths, seeds under `changes/<id>/inputs/`, no
`MEMORY.md`-as-truth), and the responsibility table is rebuilt against the new steps. Then all three
v1 files are deleted in the same change.

Two framing additions carry the round-2 review: the doc **names its method spine** — documentation-first
`stream-coding`, OpenSpec-native artifacts, and Meaningfy build practice adjusted for advanced LLM
agents (DEC-17) — and it opens the lifecycle with a short, **named governance-model principle**:
light human steering, heavy agent execution, and a cheap way to verify each gate (DEC-18).

Outcomes that tell us it worked:

- A reader can name every step of a software build contract and the **one** skill that owns it
  without leaving the doc.
- A reader can say, for any gate, **who executes it, who steers it, and the cheapest way to check the
  result** — without reading a second document (DEC-18).
- Zero live docs describe retired agents or a single-file `EPIC.md`; zero v1 files remain.
- Zero known-false ownership claims in the doc (the `EPIC-10, future` row goes).
- `repo_lint` is green again, including the check the preserved seeds currently trip (DEC-16), and the
  build-plane doc is no longer exempt from the repo's own consistency tripwires.

## Key decisions

- **DEC-1**: **"Two-tier" is retired as the doc's identity, not as its internal structure.** The
  PROJECT-tier/EPIC-tier nesting is real and stays — it just stops being the title and the frame.
  Rationale: the human retired the *name* because it undercounts the concern count (seed §1); the
  nesting itself is still the accurate description of "runs once, up front" vs "runs per Epic", and it
  matches the Employee Handbook's own project anatomy — Conception (charter) → shaping & building →
  progressive shipping (handbook seed §1).
- **DEC-2**: **Successor path is `docs/ai-coding/build-lifecycle.md`** (rewrite + rename, not a new
  file alongside). "Build" names the plane (a P2 software contract), keeping it clearly distinct from
  epic 1's engagement docs, epic 3's delivery gates, and epic 5's umbrella doc — whose name space
  (`How We Work` / `Meaningfy Delivery Model` / `Meaningfy Lifecycle Guide`) this epic must not
  occupy. Cost is six inbound link retargets; `repo_lint.broken_links` (a blocking check that already
  covers `docs/ai-coding/`) is the safety net.
- **DEC-3**: **"SDLC" is scoped to the EPIC-tier build loop only.** ADLC and MDLC-lite are PROJECT-tier
  *siblings* of the SDLC loop, not sub-steps of it. Rationale: seed §1's explicit terminology rule.
- **DEC-4**: **ADLC is named explicitly as a PROJECT-tier step, owner `architecture`** (ADRs, C4,
  UC White/Blue). Narrated and cited only — no architecture rules restated in this doc.
- **DEC-5**: **MDLC-lite is named explicitly as a PROJECT-tier step inside a software contract**,
  owners `conceptual-modelling` + `linkml-engineering`, cross-checked by `modelling-conventions`.
  **MDLC-standalone** (ontology/application-profile development as its own contract) is named in one
  line as a **known gap with no owning skill today**, parked for a separately-shaped future EPIC —
  named so it is visible, not closed (seed §3).
- **DEC-6**: **Requirements & UC is documented as one capability invoked at two depths, not a stage**
  (seed §4). This doc covers the **deep** invocation (White + Blue, feeding ADLC — whether handed off
  from a completed P1 or as the first real elicitation when a client came straight to build); the
  **shallow** invocation (White only, feeding a P1 Decision) is cited to epic 1's engagement docs. The
  *commercial* framing of the direct-to-build path stays epic 1's.
- **DEC-7**: **All three v1 files are deleted in this change**, not re-dated or re-bannered.
  Rationale: the successor content lands in the same change; the sunset condition is unowned, undated
  and unverifiable; the only live inbound links to v1 come from v1's own siblings (verified). Keeping
  a "deprecated" doc that routes readers to non-existent agents has a real cost and no benefit.
- **DEC-8**: **The diagram and responsibility table are ADAPTED, not ported** (seed §7, explicit human
  instruction). Concretely, the adaptation must replace: single-file `EPIC.md` → EPIC ≡ `proposal.md`
  + derived PLAN ≡ `design.md` + `tasks.md`; clarity gate applied to the PLAN pair (not to a spec
  blob); five agents → the three wrappers `epic-planner`/`implementer`/`code-reviewer`;
  `.claude/memory/epics/` + `MEMORY.md`-as-truth → `openspec/changes/<id>/` with archive into
  `openspec/specs/`; "Confluence Work Shape" input → seeds archived under `changes/<id>/inputs/`.
- **DEC-9**: **One diagram covering the whole build plane** (PROJECT tier + EPIC tier in a single
  graph), with Delivery & Release as a **single terminal node pointing to `dod-quality-gates.md`**.
  Rationale: v2's failure was having no diagram; two or three diagrams would re-fragment the picture,
  and the delivery lane's internals belong to epic 3. The Employee Handbook made the same call for the
  same reason — one BPMN diagram of *"the complete end-to-end process"*, kept for *"Simplify
  Complexity / Quick Reference / Alignment"* (handbook seed §2).
- **DEC-10**: **The responsibility table stays human-vs-agent and names no roles.** The roles and
  the RACI are epic 4's (`define-roles-and-raci`) — cited once, never restated. Rationale: two
  parallel role tables in two docs is exactly the duplication the no-double-spec rule forbids. Note
  the split of concerns: *what a human vs an agent does* is this doc's business (DEC-18); *which named
  role the human holds* is epic 4's.
- **DEC-11 (superseded during cross-epic consistency pass):** ~~The stale `CD / release |
  ci-cd-delivery (EPIC-10, future)` row becomes a pointer row to `dod-quality-gates.md`, not a
  corrected owner list.~~ This conflicted with `define-delivery-release-lifecycle`'s own DEC-6, which
  claims the same row and replaces it with **two concern-split rows** citing `ci-cd-delivery` and
  `meaningfy-release` directly (plus a cross-reference to the table's existing `meaningfy-git-workflow`
  row) — a format that matches every other row in this table (skill name, not a pointer to another
  doc) and that epic 3 had already reasoned through in more depth (its own DEC-6: "the merged CD/release
  row is what let the staleness hide; the split boundary is already asserted in those skills' own
  Boundary sections"). **Resolution:** this epic makes no ownership-table row edit of its own. The row
  is `define-delivery-release-lifecycle`'s to correct (its DEC-6/DEC-7), consistent with that epic's
  own "follow the content, not the path" rule — this epic only supplies the renamed file the table
  lives in. This epic's sole remaining obligation toward that row is removing the false `EPIC-10,
  future` claim if epic 3 has not yet landed when this epic implements; if epic 3 lands first, there is
  nothing left for this epic to touch. The **diagram's** Delivery & Release terminal node still points
  to `dod-quality-gates.md` per DEC-9, unaffected by this correction — DEC-9 and DEC-11 were two
  different artifacts (diagram vs. ownership table) that had been conflated.
- **DEC-12**: **`docs/ai-coding/` is dropped from `FROZEN_GLOBS` in `tools/repo_lint/lint.py`.** Two
  reasons, both verified in the code: (i) the constant's premise — "content must never be edited" —
  becomes false the moment this epic rewrites the doc, so leaving it is a lie in the guardrail; (ii)
  its only *blocking* effect today is exempting the directory from `orphan_agent_references`, an
  exemption that exists solely because v1 names `gherkin-writer`/`documenter`. With v1 deleted the
  successor must not name them either (the old→new mapping already lives, lint-exempt by filename, in
  `docs/environment-setup.md` §6). `broken_links` already covers `docs/ai-coding/` regardless of the
  freeze; the advisory prose checks (`duplicate_fact_candidates`) start applying, which is desirable
  for a doc whose whole job is to point rather than restate.
- **DEC-13**: **`docs/environment-setup.md` §6's claim that "the `docs/ai-coding/` runbook … still
  names the older agents" is corrected** — one sentence, a necessary consequence of DEC-7. The
  old→new mapping table itself stays (it is useful history and lint exempts that file by name).
- **DEC-14**: **New capability `build-lifecycle`** carries the spec delta. No existing spec in
  `openspec/specs/` references these docs (verified), so **Modified Capabilities is empty**. The
  capability covers the build-plane lifecycle *narrative contract* (every step names one owner; the
  doc reflects the current artifact vocabulary and agent roster; the doc states its governance model);
  delivery/release requirements stay epic 3's, roles stay epic 4's.
- **DEC-15**: **v2's correct parts are carried forward, not re-litigated:** the EPIC/PLAN split, the
  single-owner ownership table, the no-double-spec normative layering (including the dropped-EARS
  decision), the labelled Shape-Up divergence on front-loaded architecture, the guardrails pointer,
  model tiering, and the optional SEED / AgOCQs++ elicitation aids. Rationale: this is a narrative
  fix, not a methodology change; re-opening settled decisions would blow the appetite. What DEC-15
  carried *implicitly* — that agents do the heavy lifting — is made explicit by DEC-18.
- **DEC-16**: **`openspec/changes/` (active changes) is exempted from `orphan_agent_references`,**
  alongside the existing `_ARCHIVE_PREFIX` and `environment-setup.md` exemptions. Evidence this is
  needed *now*: the preserved seed `inputs/handover-analysis.md` names both retired agents when
  quoting v1's routing, so the blocking check (`ALL_CHECKS` → exit 1; asserted by
  `tests/test_repo_lint.py::test_no_orphan_agent_references`) is red on this branch, and seeds are
  **never groomed** — the tripwire, not the seed, is what must change. Rationale for exempting the
  whole change tree rather than only `inputs/`: an active `proposal.md` legitimately names the agents
  it is retiring or adding (this very file does), exactly as archived changes do. Alternative
  considered and rejected: exempt only `*/inputs/` and forbid literal agent names in proposals — that
  makes retirement decisions unwriteable in the artifact that decides them.
- **DEC-17**: **The doc names its method spine in one short passage, as pointers only.** The build
  plane is documentation-first (`stream-coding`, external — docs are the work, code is the printout,
  and a failing implementation sends you back to the spec), OpenSpec-native in its artifacts (EPIC ≡
  `proposal.md`, PLAN ≡ `design.md` + `tasks.md`, `openspec/changes/<id>/` → archive into
  `openspec/specs/`), and executed with Meaningfy build practice tuned for advanced LLM agents
  (`bdd-gherkin` for design-phase feature coverage, `cosmic-python` + TDD for implementation,
  `meaningfy-code-review` for multi-lens review, `clarity-gate` at ≥9/10 before code). Rationale: the
  round-2 review asked for these three to be visible in the rewrite; they are already true of how we
  work, so the doc's job is to *cite* them at the step that uses each one, not to restate their rules
  — the no-double-spec rule (DEC-15) forbids a second copy.
- **DEC-18**: **The rewrite opens with a named principle, "Light steering, heavy agents, cheap
  verification".** One short paragraph, not a restructuring: the build loop assumes LLM agents do the
  bulk of execution *and* quality verification, while humans supervise, decide, and steer — so every
  gate must offer a **low-effort way for the steering human to confirm they got what they asked for**
  (the gate's artifact is the check: a scored PLAN, a `.feature` file that reads in business language,
  a review report — not a code read-through). `guardrails` is cited as the behaviour gate that keeps
  agents inside those bounds; `stream-coding` (external) as the content method that makes the artifact
  legible enough to be checked cheaply. Rationale, human quote (handbook seed §3): *"people must
  mainly supervise and guide while LLM agents do the work and quality assessment verification …
  minimal engagement in steering and having an easy way to check if they got what they wanted."*
  Scope guard: the principle is stated once, up front, and then referenced — it does not become a
  per-step column, a maturity model, or an approval workflow.

## Rabbit-holes

- **Don't let the rename become a `docs/ai-coding/` reorganisation.** `opsx-runbook.md`,
  `openspec-setup-guide.md` and `dod-quality-gates.md` keep their names, scopes and owners; they get a
  link retarget and nothing else.
- **Un-freezing (DEC-12) may surface advisory prose findings in the sibling docs.** Fix **broken
  links only**. Any content-level finding in `dod-quality-gates.md` is epic 3's; do not expand this
  epic into a directory-wide lint cleanup.
- **Don't widen the lint work.** DEC-12 and DEC-16 are two one-line rules. `orphan_path_mentions` is
  not wired into `ALL_CHECKS` — leave it alone; do not "while we're here" refactor the exemption
  mechanism into a config file.
- **Don't draw the three-plane (SDLC/MDLC/CBLC) picture here.** One plane, one graph (DEC-9); the
  cross-plane synthesis is epic 5's whole reason to exist.
- **Don't sketch an MDLC-standalone methodology.** One naming line, then stop (DEC-5) — that gap is a
  parked EPIC with real skill-authorship in it.
- **Don't invent role names** to make the responsibility table read better (DEC-10). "Developer" and
  "agent" are the only actors this doc knows.
- **Don't turn DEC-18 into a governance framework.** One named paragraph and citations to `guardrails`
  and `stream-coding`. No approval matrix, no per-gate sign-off form, no escalation ladder — the
  moment it grows a table of its own it has become epic 4's roles work or epic 3's DoD work.
- **Don't re-argue the settled divergences** (front-loaded architecture vs canonical Shape Up; EARS
  dropped). Carried forward in substance (DEC-15).
- **Don't add navigation infrastructure** (mkdocs nav, a `docs/ai-coding/README.md`, an index page).
  One line in the root `README.md` docs table is the whole navigation change.

### Known gaps — named here, deliberately not closed

Real, valuable operational practice that exists in the Employee Handbook (2nd ed., 2026) and has **no
skillery-side equivalent today**. They are recorded so a future EPIC can pick them up; **this EPIC
designs neither**, and neither is written into `build-lifecycle.md` — unlike DEC-5's MDLC-standalone
line, which names a missing *plane* the lifecycle narrative must at least gesture at, these two are
*operational patterns around Epics* with no step in the build-plane narrative to hang off yet.
Deciding where they attach is itself the future EPIC's shaping work. Full quotes:
[`inputs/2026-07-26-handbook-findings.md`](inputs/2026-07-26-handbook-findings.md) §§4–5.

- **GAP-1 — "Improvements Outside Contract".** A dedicated-EPIC pattern for improvement/maintenance
  work that the client never asked for and the contract does not cover. Its shape, per the handbook:
  case-by-case, never a blanket rule; the EPIC is created *inside the project*, not in a central
  backlog, to keep accountability with the team; it must be a proper shaped pitch with an explicit
  **appetite** like any other EPIC; it needs **conceptual-level sign-off** before work starts; and it
  is only justified once the work has been shown *not* to fit inside an active Work Package — small
  improvements are absorbed into the active EPIC/Story, and the inability to absorb is itself the
  signal that the scope is too large. Natural future owner: `epic-planning` (it is an EPIC-shaping
  variant with an extra admissibility gate).
- **GAP-2 — Redelivery Policy.** A repeatable process for rework after a delivered Epic is not
  accepted, designed to protect the traceability of the original. Its shape, per the handbook: the
  initial Epic is marked **Done and closed regardless of final acceptance**; if the feedback exceeds
  the closed Epic's scope or appetite (new elements, extended scope, materially higher effort, a new
  iteration of work) a **dedicated redelivery Epic** is opened with its **own appetite and its own
  pitch**, referencing the original and stating the reason; minor feedback that fits the original
  appetite and adds no requirements stays in place instead; **the closed Epic is never reopened** and
  no further work is logged against it; and every redelivery closes with a **lessons-learned** pass,
  escalating to a **post-mortem / root-cause analysis when the redelivery itself overruns its new
  appetite** or uncovers critical issues. Natural future owner: `epic-planning` for the re-shape half,
  `spec-stewardship` for the close/archive/traceability half — which of the two owns it is exactly the
  question the future EPIC has to answer, not this one.

Both need adapting, not copying, before they can land: the handbook assumes human reviewers and a
ticketing system at each step, whereas the modern shape assumes agent execution with light human
sign-off (DEC-18) and OpenSpec change folders rather than tickets.

## No-gos

- **No content edits to `docs/engagement/`** — epic 1 owns that text. The *only* permitted touch is
  retargeting the three `two-tier-methodology.md` links to the new filename: a mechanical path swap,
  no prose change.
- **No changes to the DoD ladder, the Builder/Shipper dual-DoD, or the engagement-gate split in
  `dod-quality-gates.md`** — epic 3 owns all of it; this epic only retargets its inbound link (and
  points at that file from the diagram and the ownership table).
- **No roles doc, no RACI matrix, no per-role playbooks, no umbrella "how we work" doc** — epics 4
  and 5. This includes the Employee Handbook's six project roles (Business Developer, Project Owner /
  Work Shaper, Builder, Reviewer, Delivery Manager, Customer Success Manager): read as background,
  named nowhere in this epic's output.
- **No commercial content** — presale/free-vs-paid, P0-advisory, P1 Decision packaging, the
  direct-to-build *contract* path, partnership-as-status — all epic 1.
- **No new skills and no new agents or agent stubs.** The roster stays `epic-planner`, `implementer`,
  `code-reviewer`; whether any other role ever gets a wrapper is an explicitly deferred decision
  (seed §5) that this epic must not pre-empt.
- **No MDLC-standalone methodology content** beyond naming the gap (DEC-5).
- **No design work on GAP-1 or GAP-2** — naming them is the entire deliverable. No process text, no
  templates, no new sections in `build-lifecycle.md`, no skill edits to `epic-planning` or
  `spec-stewardship`.
- **No sprint/ritual mechanics ported from the handbook** — stand-ups, sprint cadence, hill charts,
  heartbeat reports, timesheets and ticketing rules are pre-LLM team mechanics and stay out of the
  build-plane doc.
- **No changes to `tests/ownership.yaml`.** The doc narrates the tripwire; the tripwire's capability
  tags are unchanged. The only permitted `tools/` changes are the two lint rules in DEC-12 and DEC-16.
- **No grooming, editing or deleting of anything under `inputs/`.** All three seeds are preserved
  records (this is what forces DEC-16 rather than a seed edit).
- **No duplication of the handbook or advisory source documents into this change's `inputs/`** — the
  canonical copies live in `openspec/changes/define-lifecycle-playbooks/inputs/`; this change carries
  only the summarised excerpt.
- **No pulling `ci-cd-delivery` forward, and no CI/CD implementation** — the release gap is pointed
  at, not filled.
- **No "canon" in any heading, sentence or filename** (seed §1).
- **No verbatim carry-over of v1's diagram or table** — adaptation is mandatory (DEC-8); a
  copy-paste is a failed implementation of this EPIC.

---

## What Changes

- **BREAKING** (documentation): delete `docs/ai-coding/ai-coding-methodology.md`,
  `docs/ai-coding/ai-coding-runbook.md`, `docs/ai-coding/ai-coding-setup-guide.md` (DEC-7).
- **BREAKING** (path): `docs/ai-coding/two-tier-methodology.md` → `docs/ai-coding/build-lifecycle.md`
  (DEC-2), with all six live inbound links retargeted: `docs/engagement/README.md` (×2),
  `docs/engagement/phases.md` (×1), `docs/ai-coding/opsx-runbook.md`,
  `docs/ai-coding/openspec-setup-guide.md`, `docs/ai-coding/dod-quality-gates.md` (×1 each).
- Rewrite the successor doc: retitled and de-"two-tier"-framed (DEC-1); PROJECT tier expanded into
  named, owner-citing steps — Requirements & UC at two depths (DEC-6), ADLC (DEC-4), MDLC-lite +
  the MDLC-standalone gap line (DEC-5), project/repo setup; SDLC scoped to the EPIC-tier loop
  (DEC-3); v2's correct sections carried forward (DEC-15).
- Add a short **method-spine passage** citing `stream-coding`, the OpenSpec artifact vocabulary, and
  the Meaningfy build skills each step uses (DEC-17).
- Add the named **"Light steering, heavy agents, cheap verification"** principle as one opening
  paragraph, citing `guardrails` and `stream-coding` (DEC-18).
- Add an **adapted** lifecycle Mermaid diagram and an **adapted** developer-vs-agent responsibility
  table (DEC-8, DEC-9, DEC-10).
- Ownership table: no row edit by this epic (DEC-11, superseded) — `define-delivery-release-lifecycle`
  corrects the `CD / release` row in place (its DEC-6/DEC-7); if that epic has not landed yet, this
  epic removes only the false `EPIC-10, future` claim, leaving the row otherwise as-is for epic 3 to
  replace.
- `tools/repo_lint/lint.py`: drop `docs/ai-coding/` from `FROZEN_GLOBS`, comment updated to say why
  the freeze is gone (DEC-12); exempt `openspec/changes/` from `orphan_agent_references` (DEC-16).
- `docs/environment-setup.md` §6: correct the one sentence claiming a live v1 runbook (DEC-13).
- Root `README.md` docs table: update the `docs/ai-coding/` row's description and the referenced
  filename.
- Add `openspec/changes/define-meaningfy-lifecycle/specs/build-lifecycle/spec.md` (DEC-14).
- Add `inputs/2026-07-26-handbook-findings.md` (already written; the round-2 seed excerpt).
- **No file changes** for GAP-1/GAP-2 — named in this EPIC only.

## Capabilities

### New Capabilities

- `build-lifecycle`: the documented build-plane lifecycle contract — every PROJECT-tier and EPIC-tier
  step names exactly one owning skill; Requirements & UC is documented as a capability at two depths
  rather than a stage; the doc states the governance model it assumes (humans steer, agents execute
  and verify, every gate has a cheap human check) and names its method spine by citation; the doc's
  diagram and responsibility table reflect the current artifact vocabulary (EPIC ≡ `proposal.md`,
  PLAN ≡ `design.md` + `tasks.md`) and the three-wrapper agent roster; no deprecated parallel
  lifecycle doc exists in `docs/ai-coding/`.

### Modified Capabilities

None. No spec in `openspec/specs/` currently references `docs/ai-coding/` or the two-tier methodology
(verified) — the delivery/release requirements this doc points at are
`define-delivery-release-lifecycle`'s to add or modify.

## Impact

**Files:** `docs/ai-coding/build-lifecycle.md` (renamed + rewritten); three `docs/ai-coding/ai-coding-*.md`
deleted; link-only edits in `docs/engagement/README.md`, `docs/engagement/phases.md`,
`docs/ai-coding/opsx-runbook.md`, `docs/ai-coding/openspec-setup-guide.md`,
`docs/ai-coding/dod-quality-gates.md`; one-line edits in `README.md` and `docs/environment-setup.md`;
two one-line rules in `tools/repo_lint/lint.py`.

**Gates:**

| Gate | State today | After this change |
|---|---|---|
| `repo_lint.broken_links` (blocking; already covers `docs/ai-coding/`) | green | green — catches any missed link retarget from the rename |
| `repo_lint.orphan_agent_references` (blocking; `tests/test_repo_lint.py`) | **red** — `inputs/handover-analysis.md` names both retired agents | green via DEC-16 (exempt `openspec/changes/`), plus the successor doc no longer names them |
| `repo_lint.duplicate_fact_candidates` (advisory, non-blocking) | skips `docs/ai-coding/` | applies to the successor — expect pointer-vs-restatement notes to review |
| `tests/test_repo_lint_negative.py` | no test pins `docs/ai-coding/` as frozen (verified) | unchanged — DEC-12 needs no test edit |

**Not affected:** no runtime code, no `.claude-plugin/marketplace.json` (no skill/bundle change), no
`.opencode/` regeneration (the generated tree carries skills and agents, not `docs/`), no
`tests/ownership.yaml` capability tags, no skill files.

**Cross-epic coordination:** epic 1 (`define-blc-engagement-model`) rewrites the two
`docs/engagement/` files this rename touches — whichever lands second reconciles the pointer; epic 3
(`define-delivery-release-lifecycle`) inherits the delivery/release lane this doc points at and any
advisory prose findings the un-freeze surfaces in `dod-quality-gates.md`; epics 4 and 5 consume this
doc's step names as the vocabulary their RACI rows and playbook views index against, so the step
names in the rewrite are a de-facto interface. Epic 4 also owns the Employee Handbook's role material
(including the Work Shaper) that this epic deliberately leaves untouched (DEC-10).

**Deliberately left open** (flagged, not decided here): whether the build-plane doc should later be
absorbed into epic 5's umbrella doc as a chapter, or stay a standalone pointed-to doc — epic 5's call
once its own shape is known. Separately, GAP-1 and GAP-2 above are open by design: named, unowned,
and awaiting their own shaping cycle.
