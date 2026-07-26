## ADDED Requirements

### Requirement: PROJECT-tier steps each name exactly one owning skill
Every PROJECT-tier step in `docs/ai-coding/build-lifecycle.md` (Requirements & UC, ADLC, MDLC-lite,
project/repo setup) SHALL cite exactly one owning skill by name and path; the doc SHALL NOT restate
that skill's rules.

#### Scenario: ADLC step names its owner
- **WHEN** a reader reads the PROJECT-tier ADLC step
- **THEN** the step names `architecture` as its single owning skill (ADRs, C4, UC White/Blue) and
  does not restate `architecture`'s internal rules

#### Scenario: MDLC-lite step names its owners
- **WHEN** a reader reads the PROJECT-tier MDLC-lite step
- **THEN** the step names `conceptual-modelling` and `linkml-engineering` as owners, cross-checked by
  `modelling-conventions`, and names MDLC-standalone as a one-line known gap with no owning skill

### Requirement: EPIC-tier steps each name exactly one owning skill
Every EPIC-tier step (shape the EPIC, derive the PLAN, BDD, TDD, review, documentation, archive)
SHALL cite exactly one owning skill or OpenSpec mechanism per step.

#### Scenario: Clarity-gate step names its owner
- **WHEN** a reader reads the "derive the PLAN" EPIC-tier step
- **THEN** the step names `clarity-gate` as the sole owner of the ≥9/10 scoring gate

### Requirement: Requirements & UC is documented as one capability at two depths, not a pipeline stage
The doc SHALL present Requirements & UC elicitation as a single capability invoked at two depths
(deep — White + Blue, feeding ADLC; shallow — White only, feeding a P1 Decision) rather than as a
sequential pipeline stage, and SHALL cite the shallow invocation to the engagement docs rather than
restate their commercial framing.

#### Scenario: Deep invocation is documented in this doc
- **WHEN** a reader looks for the deep Requirements & UC invocation
- **THEN** the doc describes White + Blue use-case elicitation feeding ADLC, owned by `architecture`

#### Scenario: Shallow invocation is a citation, not a restatement
- **WHEN** a reader looks for the shallow (White-only) invocation
- **THEN** the doc points to the engagement docs (`docs/engagement/`) for the commercial framing and
  does not restate P0/P1 packaging content

### Requirement: The doc states its governance model in one named, up-front principle
`docs/ai-coding/build-lifecycle.md` SHALL open with a single named principle — "Light steering, heavy
agents, cheap verification" — stating that agents execute and verify while humans steer and decide,
and that every gate offers a low-effort artifact-based check. The principle SHALL cite `guardrails`
and `stream-coding` and SHALL NOT expand into a per-step column, maturity model, or approval workflow.

#### Scenario: Governance principle appears once, up front
- **WHEN** a reader opens `build-lifecycle.md`
- **THEN** the "Light steering, heavy agents, cheap verification" principle appears as one paragraph
  before the tier narrative, citing `guardrails` and `stream-coding`, and no per-step governance
  column or approval matrix appears anywhere else in the doc

### Requirement: The diagram and responsibility table reflect the current artifact vocabulary and agent roster
The adapted Mermaid diagram and the developer-vs-agent responsibility table SHALL represent EPIC as
`proposal.md`, PLAN as `design.md` + `tasks.md`, and the agent roster as exactly the three thin
wrappers `epic-planner`, `implementer`, `code-reviewer`. Neither artifact SHALL reference a
single-file `EPIC.md`, a five-agent roster, `.claude/memory/epics/`, or `MEMORY.md`-as-truth.

#### Scenario: Diagram uses current artifact vocabulary
- **WHEN** a reader inspects the lifecycle diagram
- **THEN** its EPIC node is labelled `proposal.md` and its PLAN node is labelled `design.md` +
  `tasks.md`, with no node referencing a single-file `EPIC.md`

#### Scenario: Responsibility table names only the surviving agents
- **WHEN** a reader inspects the responsibility table's agent column
- **THEN** only `epic-planner`, `implementer`, and `code-reviewer` appear, and neither `gherkin-writer`
  nor `documenter` appears anywhere in the table

### Requirement: The ownership table contains no known-false ownership claims
The single-owner ownership table SHALL NOT name a skill or EPIC id that does not currently exist in
the repo. The CD/release row's exact final content (a corrected owner citation vs. a pointer) is
`define-delivery-release-lifecycle`'s to decide (its DEC-6/DEC-7); this capability only requires that
the false `ci-cd-delivery (EPIC-10, future)` claim is gone once both sibling changes have landed.

#### Scenario: CD/release row no longer claims a false owner
- **WHEN** a reader reads the ownership table's CD/release row after both this change and
  `define-delivery-release-lifecycle` have landed
- **THEN** the row does not say `ci-cd-delivery (EPIC-10, future)`

### Requirement: No deprecated parallel lifecycle doc remains in docs/ai-coding/
After this change, `docs/ai-coding/` SHALL contain exactly one build-plane lifecycle narrative doc
(`build-lifecycle.md`), and no file under `docs/ai-coding/` SHALL reference a retired agent
(`gherkin-writer`, `documenter`) or a single-file `EPIC.md` model.

#### Scenario: v1 files are absent
- **WHEN** the repository is inspected after this change
- **THEN** `docs/ai-coding/ai-coding-methodology.md`, `docs/ai-coding/ai-coding-runbook.md`, and
  `docs/ai-coding/ai-coding-setup-guide.md` do not exist

#### Scenario: No live doc names a retired agent
- **WHEN** `repo_lint`'s `orphan_agent_references` check runs against `docs/ai-coding/`
- **THEN** it reports zero references to `gherkin-writer` or `documenter` in that directory

### Requirement: repo_lint's link and orphan-reference gates pass after the rename
After `two-tier-methodology.md` is renamed to `build-lifecycle.md` and its six inbound links are
retargeted, `repo_lint`'s `broken_links` check SHALL report zero broken links against
`docs/ai-coding/`, and `orphan_agent_references` SHALL report zero findings for this change's
preserved seed files.

#### Scenario: broken_links passes after the rename
- **WHEN** `repo_lint`'s `broken_links` check runs after the rename and all six inbound link
  retargets
- **THEN** it reports no broken link to `two-tier-methodology.md` or `build-lifecycle.md` anywhere in
  `docs/` or `README.md`

#### Scenario: orphan_agent_references passes despite the preserved seed
- **WHEN** `repo_lint`'s `orphan_agent_references` check runs after `openspec/changes/` is exempted
  in `tools/repo_lint/lint.py`
- **THEN** it reports zero findings even though
  `openspec/changes/define-meaningfy-lifecycle/inputs/handover-analysis.md` names both retired agents
