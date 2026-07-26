# EPIC: Roles and RACI — the six delivery roles and who is accountable for what

> **Golden thread.** Parents:
> [`inputs/2026-07-25-brainstorm-seed.md`](inputs/2026-07-25-brainstorm-seed.md) (§5 roles, §6 draft
> RACI, §4 Builder/Shipper split) — the human decisions this EPIC formalises — and
> [`inputs/2026-07-26-handbook-findings.md`](inputs/2026-07-26-handbook-findings.md), the excerpt of
> *Employee Handbook — Second Edition (2026)* (pp. 65–68) that names Meaningfy's six existing project
> roles and supplies the Work Shaper's written mandate. No requirement or architecture artifact sits
> above them; per [`spine/golden-thread.md`](../../../spine/golden-thread.md) the root for a repo not
> starting from a paid engagement is the requirement/seed itself.
> **Re-shape event (round 2, 2026-07-26).** The handbook invalidated part of the round-1 bet, not just
> its plan: **DEC-2 is reversed by DEC-2R** (Work Shaper *is* a role). Logged here as a deliberate,
> visible decision rather than a silent edit, per `epic-planning`'s freeze-vs-re-shape rule.
> **Sibling EPICs shaped in the same round, cited never restated:** `define-blc-engagement-model`
> (the commercial model whose activities this matrix covers), `define-meaningfy-lifecycle` (the build
> loop), `define-delivery-release-lifecycle` (the dual-DoD this matrix's Release row points at),
> `define-lifecycle-playbooks` (per-role filtered views derived from this doc — six now, not five).

## Appetite

**Small.** One new hand-written doc, two edits to `README.md`, one spec delta. The round-2 correction
adds one role block and one matrix column to the same single document — it does not change the
shape of the bet. No new skills, no new agents, no tooling, no generated artifacts. If it grows a
second doc or a validator, the bet was mis-shaped.

## Why

Meaningfy's lifecycle docs describe activities but never name who performs them. The strings
"Solution Architect", "Solution Builder", "Solution Shipper", "Technical Consultant" and "RACI" occur
nowhere in the repo today (the only match is the title of
[`skills/architecture/SKILL.md`](../../../skills/architecture/SKILL.md), "Solution Architecture
Skill" — a skill name, not a role). Every activity therefore has an implicit owner, and the two
accountabilities that genuinely collide at delivery — Epic/architecture-spec conformance versus
contract/client-requirement conformance (seed §4) — have no named holders at all.

Worse, the vocabulary is not merely missing but **split**: Meaningfy already has a written six-role
model in a 103-page Employee Handbook that no repo document references, so the roles that do the work
and the roles the repo can name have drifted apart. Round-1 shaping drifted with them and concluded
there were five roles.

Why now: four sibling EPICs are re-cutting the lifecycle narrative in this same round. Without a
single named role vocabulary they will each invent one, and the divergence will have to be
reconciled afterwards across four documents instead of fixed once here.

## Solution outline

One document, `docs/roles-and-raci.md`, with two halves that together let any other doc name an owner
by citation instead of by restating ownership:

1. **Six role definitions** — Sales/Presales, Technical Consultant, Solution Architect, **Work
   Shaper**, Solution Builder, Solution Shipper. Each is one short block: mandate (one sentence),
   what it is *accountable* for, the skills it draws on (cited by path, never restated), and the
   artifacts it produces. Definitions come from seed §5 and the handbook excerpt, and are treated as
   decided.
2. **One RACI matrix** over the full activity list, presale through partnership nurture, with an
   explicit legend and one structural invariant: **exactly one A per activity row**.

Two handbook roles that Meaningfy no longer staffs are recorded as **adaptation notes** rather than
role blocks, so the reader sees what happened to them instead of finding a silent gap: the **Quality
Overseer**'s four-eyes review is now agent-assisted (DEC-14), and the **Customer Success Manager**'s
mandate is Sales/Presales' account-nurture activity (DEC-15). Both cite the handbook as the
pre-LLM-agent precedent they replace.

One ambiguity still ships as a documented feature rather than a defect to close: the
**agent-wrapper fork** (does any role beyond Builder get a dedicated Claude Code agent?) is recorded
as an open question with today's default, the condition that would reopen it, and a stated priority
order (DEC-3). Everything a reader might otherwise mistake for an oversight lands in a labelled
**Known gaps** section (DEC-17).

The outcome: a reader can answer "who is accountable for this?" from one table row, and the four
sibling docs can cite a role name instead of describing an owner.

## Key decisions

- **DEC-1**: **One file at `docs/roles-and-raci.md`** — not a `docs/roles/` directory with a file per
  role. Rationale: `define-lifecycle-playbooks` already owns one short playbook per role, so a
  per-role file here would create a second per-role home and a permanent sync burden between the two.
  Docs *root* rather than `docs/engagement/` (commercial-only) or `docs/ai-coding/` (build-tier home,
  and listed in `FROZEN_GLOBS` at `tools/repo_lint/lint.py:39`) because roles span both planes;
  `docs/skill-inventory.md` and `docs/environment-setup.md` set the precedent that cross-cutting docs
  sit at docs root.
- **DEC-2**: ~~Exactly five roles; "Work Shaper" is not a sixth role.~~ **SUPERSEDED by DEC-2R.**
  Retained as a stub for citation integrity only — the round-1 reasoning inferred a conflation from
  the brainstorm seed alone, which was not evidence that no role existed. Do not cite DEC-2 as live.
- **DEC-2R**: **Six roles. "Work Shaper" is a real role, and its real-world equivalent is Project
  Owner.** *Evidence:* the Employee Handbook's own project-role list (p. 65) names six roles —
  Mastermind Wizard (Business Developer), **Shaper (Project Owner)**, Builder (Engineering or
  Implementation Lead), Shipper (Delivery Manager), Quality Overseer (QA Lead), Customer Success
  Manager (Client Relationship Manager) — and p. 66 gives the Shaper a written mandate: develop the
  Work Breakdown Structure from the request-for-offer, the offer and the client meeting notes;
  establish the project roadmap; **write the Epic Pitches based on the Shape Up methodology**;
  identify risks and mitigations; oversee the project from inception to delivery; and **discover work
  with the Builders, mapping the Epic scope into User Stories (or Tasks)**. *Consequence:* the role
  is added to the doc with that mandate, and its accountability moves onto the matrix (DEC-5).
  *The observation that makes it non-negotiable:* this mandate is near-verbatim what
  [`skills/epic-planning/SKILL.md`](../../../skills/epic-planning/SKILL.md) already does — "Writing
  down the Epic Pitches" is authoring `proposal.md`, "map the Epic scope with User Stories" is
  deriving `tasks.md`. Work Shaper is the **human role that owns and steers `epic-planning`**, and of
  all six roles it is the closest to already having a mature agent counterpart (`epic-planner`). The
  doc states this explicitly wherever the role appears.
- **DEC-3**: **The agent-wrapper fork stays open, with a stated priority order.** The doc states the
  current default (documentation-only; the roster remains `epic-planner`, `implementer`,
  `code-reviewer`) and names the reopening condition — the role has actually been exercised on a real
  engagement. It adds one ranking line: **Work Shaper is the highest-priority candidate if the fork
  is ever resolved**, precisely because `epic-planner` already performs most of its mandate (DEC-2R),
  so a wrapper there is a thin steering layer over an existing agent rather than new capability. This
  is a *priority statement, not a commitment*: no agent, no stub, no recommendation dressed as a
  decision. Listed under Known gaps (DEC-17) so it is findable.
- **DEC-4**: **A role is a set of responsibilities in a process — not a competence, and not a
  headcount.** Three claims, stated in the doc in this order:
  1. *Not a competence.* The handbook makes this distinction itself (p. 65): "Profiles are defined in
     terms of skills, competencies and academic background"; "Roles are defined in terms of
     responsibilities in the company or a project". Competences (Semantic Engineer, Software
     Engineer, DevOps Engineer, QA Engineer) are **profiles**; this doc assigns **roles**.
  2. *Therefore roles are plane-agnostic.* Stated in the human's own shape: **a Builder is a Builder
     for a modelling/ontology project, or for a software-development process, or for a
     teaching-and-preparing-materials process; and a Shaper shapes the ontology, the software, or the
     course.** Same role label, same responsibilities, different plane and different profile
     executing it. The handbook's single Builder role spanning both Software-Engineer and
     Semantic-Engineer profiles (p. 67) is its own worked example. **Work Shaper is plane-agnostic in
     exactly the same way Builder is** — this is consistent with, not a contradiction of, DEC-13's
     Architect/Shaper split, which divides *kind of work* (technical design vs. scoping), never
     *plane*.
  3. *Not headcount.* One person may hold several roles on a small engagement, and two people may
     share one role. The matrix constrains *accountability*, not staffing. Without this line a
     six-column matrix reads as a six-person org chart Meaningfy does not have.
- **DEC-5**: **One A per row is an invariant**, and the draft rows that violate or misplace it are
  fixed. Seed §6's "Requirements & UC (via P1, shallow)" and "CBLC" rows have no A at all; its
  "Epic / work shaping" row has a footnoted, deliberately role-fluid A that DEC-2R now resolves.
  - Shallow Req&UC → **Technical Consultant A/R** (they own assessment and Decision-Package content
    per seed §5), Sales/Presales C.
  - **Epic / work shaping → Work Shaper A/R**, with **Solution Architect C** and **Solution Builder
    C**: both inform the shape — the Architect with technical constraint, the Builder with
    discovered work — but neither owns authoring it (DEC-13). Solution Shipper stays C on appetite
    and client-commitment fit.
  - CBLC is resolved by DEC-7.
- **DEC-6**: **Split the draft's combined "Presale / P0-advisory / P1" row into three rows.** The
  corrected commercial model makes these three distinct products with different performers — presale
  is free relationship work (Sales R), while P0-advisory and P1 are paid and the Technical Consultant
  does the work (Sales A). One row hid that difference.
- **DEC-7**: **Split CBLC into CBLC-lite and CBLC-standalone**, mirroring the MDLC-lite/standalone
  split the seed already makes (§3). CBLC-lite (documentation for what was built, inside any plane) →
  **A/R Solution Builder**. CBLC-standalone (training/docs sold as the whole engagement) → **A
  Solution Shipper, R Solution Builder**, Work Shaper **C** (it is the Shaper who shapes the course,
  per DEC-4), Sales/Presales C on the sale. Collapsing both into one row is what left the original
  row without an A.
- **DEC-8**: **Keep the MDLC-standalone row in the matrix**, A = Solution Architect, no R, explicitly
  annotated "no owning skill — parked capability gap". Keeping the row makes the gap visible at the
  point where a reader looks for an owner; deleting the row would hide it. Also listed under Known
  gaps (DEC-17).
- **DEC-9**: **Keep the draft's Review row as the human set it** (R Solution Builder, A Solution
  Shipper) and scope the word in the legend: "Review" is the build-tier review gate *closing* — the
  Builder does the review work and responds to it; the Shipper is accountable that the gate actually
  closed before anything reaches a client. Recorded rather than silently normalised, because the row
  reads surprising and the surprise is the human's call. DEC-14 explains *who or what* now performs
  the reviewing itself.
- **DEC-10**: **One new capability, `role-accountability-model`, carrying only structural invariants**
  — the six-role closed set, one-A-per-row, roles-are-responsibilities-not-competences-or-headcount,
  and every named activity present in the matrix. It does **not** normativise individual RACI cell
  values: cells are editorial content that will be refined as service lines mature, and freezing them
  as RFC-2119 SHALL would turn every future refinement into a spec delta.
- **DEC-11**: **Role definitions cite owning skills by repo-relative path and never restate their
  content** — the repo's single-source-of-authority rule. A role block lists the skills it draws on;
  what those skills say stays in the skills.
- **DEC-12**: **Vocabulary alignment** with seed §1: the doc uses neither "canon" nor "two-tier", and
  scopes "SDLC" to the EPIC-tier build loop only.
- **DEC-13**: **Work Shaper is bounded against the two roles it is most easily confused with —
  Solution Architect and Solution Shipper.** The doc carries one short paragraph on each boundary:
  - **vs. Solution Architect — by kind of work.** The Architect owns the **technical design**: ADRs,
    C4 views, UC White/Blue, MDLC-lite domain and technical models. It answers *how the system is
    built and why that structure*. The Work Shaper owns **turning a decided scope into a shaped,
    appetite-bound bet**: the WBS, the roadmap, the Epic pitch, the risk list, and the mapping of
    Epic scope into stories with the Builder. It answers *what we are betting on, how much appetite
    it gets, and what the increments are* — **planning and scoping, not technical design**. They meet
    at the shaping table and neither substitutes for the other: an Architect's design with no
    appetite bound is an unshaped wish; a Shaper's bet with no technical constraint is a guess. On
    the matrix this is exactly A/R Work Shaper with Architect C (DEC-5).
  - **vs. Solution Shipper — by what "through to delivery" means.** The handbook's mandate has the
    Shaper "overseeing ... from project inception to delivery", which reads as a delivery
    accountability it does not hold. The Shaper's oversight is over **the shape**: is this still the
    bet we made, is the appetite intact, has discovered work changed the scope. The **Shipper** holds
    the delivery-close accountability against the contract and the client's documented requirements
    (seed §4). The Shaper is present through delivery; it is not accountable for it.
  - **Positioned on the Architect–Builder spectrum, leaning Builder.** The human's own words, given
    directly against this role: *"skillwise it is something between architect and builder (more
    leaning towards the builder, but thinking the actual work to be done ahead, kind of planning and
    making important decisions)."* This is consistent with, not a restatement of, the two boundary
    paragraphs above — those distinguish Shaper's work *by kind* (planning/scoping vs. technical
    design, vs. delivery-close); this is the same distinction read as a single spectrum, stated
    because `define-lifecycle-playbooks`' Work Shaper playbook cites this line and this doc is the
    authoritative source for it, not the playbook.
- **DEC-14**: **Quality Overseer is not added as a role; its review work is recorded as
  agent-assisted.** The handbook (p. 67) defines a Reviewer — the Quality Overseer (QA Lead) — whose
  mandate is the **four-eyes principle**: every piece of work reviewed by another qualified team
  member against the Epic Pitch specification, methodologies and best practices. *Adaptation, stated
  in the doc as the "people govern, agents do the heavy work" move:* that review is now largely
  carried out by LLM agents —
  [`skills/meaningfy-code-review/SKILL.md`](../../../skills/meaningfy-code-review/SKILL.md)'s
  multi-lens automated review — with the **Builder** doing the work and light **human sign-off** on
  top: the **Solution Shipper** signs off (it is A on the Review row, DEC-9), and where a review
  closes on a non-software plane with no client-facing shipment in that increment, the **Work Shaper**
  performs the sign-off as R while the Shipper remains A. The invariant holds: one A per row.
  Consequence: **no dedicated review headcount** in the corrected model. The handbook role is cited
  in the doc as the pre-LLM-agent precedent this replaces — named, not silently dropped.
- **DEC-15**: **Customer Success Manager is not added as a role; its mandate folds into
  Sales/Presales.** The handbook (p. 68) defines a Customer Success Manager — the Wizard of Client
  Satisfaction (Client Relationship Manager) — owning client-relationship management, expectation
  management, status and demo meetings, **client aftercare post-delivery**, satisfaction reviews, and
  the ceremonial handover. In the corrected model that is precisely the **partnership /
  account-nurture** activity already assigned to **Sales/Presales** (seed §2: the repeat-client
  relationship, led with `executive-communication`). Folding it in rather than adding a seventh
  column avoids two roles sharing one activity's accountability, which would break DEC-5. The
  handbook role is cited on the partnership row as the precedent; the row's A stays Sales/Presales.
- **DEC-16**: **The "do not re-derive" rule is a rule against re-deriving *content*, not against
  aligning *vocabulary* — and a consistency pass is required, not optional.** Once siblings 1–3 land,
  this doc's activity names are checked against the vocabulary those documents actually publish
  (activity names, plane names, gate names), and mismatches are fixed here as renames. Rationale, in
  the human's words: "do not rederive but a proper adjustment and alignment is desirable to avoid
  vocabulary drift or conflations or ambiguity." The pass is a rename-and-check exercise with no new
  definitions; the rabbit-hole below states the same boundary from the other side.
- **DEC-17**: **The doc carries an explicit, labelled "Known gaps" subsection** rather than leaving
  gaps distributed through prose and footnotes. Rationale, in the human's words: "if any are needed
  flag them and mark that need somewhere easy to identify." Each entry names the gap and its owner-
  if-any; none is closed here. The section's contents are enumerated under **Known gaps** below.

## Rabbit-holes

- **Do not re-derive the lifecycle, but do align its vocabulary.** Activity names are *used* here and
  *defined* by the sibling EPICs. If a definition feels thin while writing a row, cite the sibling and
  move on — do not write a paragraph explaining ADLC or P1 in this doc. The pass DEC-16 requires is
  narrower than it sounds: compare row labels against the siblings' published names, rename where
  they diverge, flag conflations. Rewriting a definition, not renaming a row, is the trap.
- **Do not wait for siblings 1-3 to land.** The conceptual dependency is real but shallow: if a
  sibling renames an activity, this doc changes a row label. That is a rename, not a re-shape.
- **Do not build one matrix per plane** (an SDLC RACI, an MDLC RACI, a CBLC RACI). Three matrices
  triple the drift surface for rows that are mostly identical. One matrix whose rows are plane-scoped.
- **Do not drift into an HR artifact** — no competency framework, seniority ladder, job description,
  hiring rubric, or capacity model. The handbook has all of these; none of them is ported. Roles here
  exist only to hold accountability for named activities, and the handbook's own Roles-vs-Profiles
  split (DEC-4) is the line that keeps them out.
- **Do not port the handbook's mechanics.** JIRA keys, Confluence spaces, Google-Drive template
  folders, document header/footer rules, Hill Charts, and career levels are pre-LLM-agent tooling
  detail. Substance (who is responsible for what) travels; mechanics do not.
- **Do not resolve the MDLC-standalone gap** (DEC-8 names it, nothing more). It has its own future
  shaping cycle.
- **Do not map the 3-agent roster onto the 6 roles beyond a one-way pointer.** Agents are execution
  wrappers, not roles; 3 ≠ 6 and forcing the correspondence is exactly what DEC-3 defers — including
  for Work Shaper, whose close fit with `epic-planner` (DEC-2R) is stated as a *priority*, not as a
  mapping to build.
- **Do not write a validator for the matrix.** One A per row is verifiable by eye on a table this
  size; `tools/repo_lint` gains nothing and would need to parse Markdown tables to get it.

## No-gos

- **No new skills and no new agents or agent stubs** — including no `work-shaper` agent and no
  `solution-shipper` agent. This EPIC is documentation only, even though it is *about* roles. Where a
  skill or agent genuinely appears to be needed, it is **named under Known gaps** (DEC-17) and left
  unbuilt.
- **No role beyond the six**, and specifically no promotion of Quality Overseer or Customer Success
  Manager to a seventh or eighth one. They are recorded as adaptation notes (DEC-14, DEC-15), not as
  columns.
- **No company-role coverage.** The handbook's company roles (CEO, Operations Officer, Finance
  Officer, Communications and Marketing Officer, Business Development and Sales Officer) are org-chart
  positions. This doc covers **project roles** only.
- **No resolution of the agent-wrapper fork** (DEC-3). It ships open, on purpose, priority order and
  all.
- **No edits to `docs/ai-coding/**` or `docs/engagement/**`.** Those files are owned by siblings 1-3
  in this same round; editing them here would create write collisions in a parallel shaping round.
  Inbound links are the siblings' to add when they rewrite; discoverability here rests on `README.md`
  plus the umbrella doc from `define-lifecycle-playbooks`.
- **No per-engagement instantiation.** The doc states the *default* accountability for Meaningfy work.
  Tailoring for a specific client contract is a proposal/contract concern, not this doc's.
- **No RACI rows outside the named activity list** — no internal operations, recruiting, finance, or
  administration. The list is closed at the 17 rows enumerated under **What Changes**.
- **No `design.md` / `tasks.md` in this change round.** Shaping only.

## Known gaps

Named here and reproduced in the doc's own **Known gaps** subsection (DEC-17). None is closed by this
EPIC; each is stated so a reader stops looking for it elsewhere.

| Gap | Nature | Owner / next step |
|---|---|---|
| **A `work-shaper` agent wrapper** | Highest-priority candidate of all deferred agent questions: `epic-planner` already performs most of the Work Shaper mandate (DEC-2R), so this would be a thin steering layer, not new capability. | Deferred by DEC-3. Reopens once the role has been exercised on a real engagement. Not built here. |
| **Agent wrappers for the other four non-Builder roles** | Lower priority; no existing agent covers their mandates. | Deferred by DEC-3, same condition. |
| **MDLC-standalone has no owning skill** | Genuine capability gap: the ontology/application-profile development methodology (METHONTOLOGY/NeOn/LOT-style) has no skill; `conceptual-modelling` explicitly scopes itself to product-development projects. | Parked for its own shaping cycle (seed §3). Visible on the matrix via DEC-8. |
| **Agent-assisted review has no non-software equivalent** | `meaningfy-code-review` is code-scoped. DEC-14 retires the Quality Overseer headcount across *all* planes, but the automated multi-lens review that replaces it exists only for the software plane; ontology and training-material review currently fall back to unaided human sign-off. | Named only. Candidate future skill; not designed here. |
| **Vocabulary consistency pass pending** | This doc's activity names are provisional until siblings 1–3 publish theirs. | Required follow-up under DEC-16 — a rename-and-check pass, not a re-derivation. |
| **Handbook material beyond the role sections** | Operational patterns in the same handbook (out-of-contract improvement Epics, the redelivery policy, contractual-validation steps) have no skillery equivalent. | Out of scope here; named by `define-meaningfy-lifecycle` and `define-delivery-release-lifecycle` — cited, not restated. |

---

## What Changes

- Add **`docs/roles-and-raci.md`**, containing:
  - **six** role definition blocks (mandate / accountable for / skills drawn on / artifacts
    produced) — Sales/Presales, Technical Consultant, Solution Architect, **Work Shaper**, Solution
    Builder, Solution Shipper — with the Work Shaper block naming `epic-planning` as the skill it
    owns and steers (DEC-2R) and two short paragraphs separating it from Solution Architect and
    Solution Shipper (DEC-13);
  - a RACI legend (R, A, C, I, `–` = not involved) and the stated invariants from DEC-4, DEC-5;
  - one RACI matrix, **6 role columns × 17 activity rows**: presale; P0-advisory; P1 Decision;
    Requirements & UC shallow (White, via P1); Requirements & UC deep (White+Blue, via P2); ADLC;
    MDLC-lite; MDLC-standalone *(gap, DEC-8)*; project/repo setup; **Epic/work shaping (A/R Work
    Shaper, C Architect, C Builder — DEC-5, DEC-13)**; Epic build (BDD/TDD); review *(DEC-9,
    DEC-14)*; release & deploy; contract-conformance check; CBLC-lite; CBLC-standalone;
    partnership/account nurture. Row count is unchanged; the Work Shaper column's remaining cells are
    editorial content per DEC-10;
  - two **adaptation notes** — Quality Overseer (DEC-14) and Customer Success Manager (DEC-15) —
    each citing the handbook role it replaces or folds in;
  - the open agent-wrapper question with its priority order (DEC-3), marked deliberate rather than
    pending;
  - a **Known gaps** subsection (DEC-17) reproducing the table above;
  - a references table with deep links to the sibling docs that define each activity, and to the
    handbook excerpt in `inputs/`.
- Add one row to `README.md`'s **Documentation** table (after the `docs/engagement/` row) and extend
  the `docs/` line in the **Repository structure** block.
- Add a spec delta for the new capability `role-accountability-model`.

No breaking changes.

## Capabilities

### New Capabilities

- `role-accountability-model`: the closed **six-role** set and the structural invariants of the
  accountability matrix — one accountable role per activity, roles as responsibilities-in-a-process
  rather than competences or headcount, every named lifecycle activity present. Structure only, not
  cell values (DEC-10).

### Modified Capabilities

None. No existing spec in `openspec/specs/` mentions roles or accountability (checked:
`catalogue-governance`, `release-lifecycle`, `pr-review-modes`, `code-principles-governance`,
`modelling-conventions`, `explanatory-writing`, `writing-antipatterns`, `linkml-engineering`,
`dual-cli-generation`, `dual-cli-distribution`).

## Impact

- **Docs:** one new file at `docs/roles-and-raci.md`; `README.md` (one table row + one structure
  line).
- **Validation:** unlike `docs/ai-coding/` (frozen, `tools/repo_lint/lint.py:39`), a doc at docs root
  is subject to the link check (`broken_links`, `tools/repo_lint/lint.py:230`) — every relative link
  to a skill or sibling doc must resolve or `make validate` fails. Docs-root files are *not*
  `_is_illustrative`, so there is no exemption.
- **No regeneration:** no skill, agent, or marketplace change → no `make generate-opencode`, and
  `docs/skill-inventory.md` is unaffected (it indexes skills, not docs).
- **Consumers:** `define-lifecycle-playbooks`' per-role playbooks are filtered views over this
  matrix — **six playbooks, including a Work Shaper playbook**, following DEC-2R;
  `define-delivery-release-lifecycle`'s dual-DoD lane and `define-blc-engagement-model`'s funnel
  supply the activity definitions this matrix assigns owners to.
- **Round-2 ripple:** DEC-2R reverses a decision two epics relied on. `define-lifecycle-playbooks`
  takes the larger share (a sixth playbook and a redrawn map diagram); no other sibling's scope
  changes, since none of them names role columns.
- **Only possible merge conflict in this round:** `README.md`, if a sibling EPIC also adds a
  Documentation-table row. Mechanical, single-hunk.
