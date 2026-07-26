# Roles and RACI: who is accountable for what

This page names Meaningfy's six project roles and assigns exactly one accountable role to every
lifecycle activity, presale through partnership/account-nurture. It exists so any other document
(an engagement-model doc, a lifecycle doc, a per-role playbook) can **name an owner by citation**
instead of restating who does the work. Roles here are **responsibilities in a process**, not
competences and not a headcount or org-chart model; see the invariants before the matrix. Each
role block cites the skills it draws on by path rather than restating their content.

## Role definitions

### Sales/Presales

**Mandate:** own the presale relationship and the commercial thread from first contact through
partnership.

- **Accountable for:** presale qualification and relationship-building (free); commercial leadership
  of Discovery & Onboarding (both tiers); partnership and account-nurture once a client becomes a
  repeat client.
- **Skills drawn on:** [`skills/semantic-consulting-coach/SKILL.md`](../skills/semantic-consulting-coach/SKILL.md),
  [`skills/proposal-writing/SKILL.md`](../skills/proposal-writing/SKILL.md),
  [`skills/executive-communication/SKILL.md`](../skills/executive-communication/SKILL.md).
- **Artifacts produced:** qualified opportunity, commercial proposal/SoW co-ownership, account-nurture
  cadence.

### Technical Consultant

**Mandate:** provide technical assessment and Decision-Package development, and strategic advisory
on data governance and management.

- **Accountable for:** assessment work and Decision-Package content during Discovery & Onboarding
  (both tiers); shallow Requirements & Use-Case work carried via the Deep tier.
- **Skills drawn on:** [`skills/decision-package/SKILL.md`](../skills/decision-package/SKILL.md),
  [`skills/estimation/SKILL.md`](../skills/estimation/SKILL.md).
- **Artifacts produced:** the Decision Package (recommendation, scope, roadmap, buy/build/defer).

### Solution Architect

**Mandate:** own technical design: the system's structure and the reasoning behind it.

- **Accountable for:** ADLC (ADRs, C4 views, Use-Case White/Blue); MDLC-lite domain and technical
  modelling within a software contract.
- **Skills drawn on:** [`skills/architecture/SKILL.md`](../skills/architecture/SKILL.md),
  [`skills/conceptual-modelling/SKILL.md`](../skills/conceptual-modelling/SKILL.md).
- **Artifacts produced:** ADRs, C4 diagrams, Use-Case White/Blue documents, domain/technical models.

### Work Shaper

**Mandate:** develop the Work Breakdown Structure from the request-for-offer, the offer, and the
client meeting notes; establish the project roadmap; write the Epic Pitches per the Shape-Up
methodology; identify risks and mitigations; and discover work with the Builder, mapping Epic scope
into stories.

- **Accountable for:** the shaped, appetite-bound bet: the WBS, the roadmap, the Epic pitch, the
  risk list, and the ongoing mapping of discovered work into stories/tasks with the Builder.
- **Boundary vs. Solution Architect (by kind of work).** The Architect owns the **technical
  design**: ADRs, C4 views, UC White/Blue, MDLC-lite domain and technical models. It answers *how
  the system is built and why that structure*. The Work Shaper owns **turning a decided scope into
  a shaped, appetite-bound bet**: the WBS, the roadmap, the Epic pitch, the risk list, and the
  mapping of Epic scope into stories with the Builder. It answers *what we are betting on, how much
  appetite it gets, and what the increments are*: planning and scoping, not technical design. They
  meet at the shaping table and neither substitutes for the other: an Architect's design with no
  appetite bound has not been committed to a scope; a Shaper's bet with no technical constraint has
  not been checked against what can actually be built. On the matrix this is A/R Work Shaper with
  Architect C.
- **Boundary vs. Solution Shipper (by what "through to delivery" means).** The Shaper's mandate reads
  as overseeing "from project inception to delivery", which could be misread as a delivery
  accountability. It is not: the Shaper's oversight is over **the shape**: is this still the bet we
  made, is the appetite intact, has discovered work changed the scope. The **Shipper** holds the
  delivery-close accountability against the contract and the client's documented requirements. The
  Shaper is present through delivery; it is not accountable for it.
- **Positioned on the Architect–Builder spectrum, leaning Builder.** Skillwise the Work Shaper sits
  between Architect and Builder, closer to the Builder, while thinking the actual work to be done
  ahead of time: planning and making the important decisions before the Builder executes them.
  This is the authoritative statement of that positioning; other documents cite this page rather
  than restating it.
- **Skills drawn on:** [`skills/epic-planning/SKILL.md`](../skills/epic-planning/SKILL.md): the
  Work Shaper is the human role that owns and steers this skill.
- **Artifacts produced:** the WBS, the project roadmap, Epic Pitches (`proposal.md`), the risk list,
  the discovered-work backlog mapped into stories/tasks (`tasks.md`).

### Solution Builder

**Mandate:** execute the practical work of the Epic, translating a shaped scope into tangible,
demonstrable, deliverable increments.

- **Accountable for:** project/repo setup; the Epic build loop (BDD/TDD); Epic/architecture-spec
  conformance at delivery; discovering work as it is executed and reporting it back to the Work
  Shaper.
- **Skills drawn on:** [`skills/cosmic-python/SKILL.md`](../skills/cosmic-python/SKILL.md),
  [`skills/bdd-gherkin/SKILL.md`](../skills/bdd-gherkin/SKILL.md),
  [`skills/linkml-engineering/SKILL.md`](../skills/linkml-engineering/SKILL.md).
- **Artifacts produced:** working, reviewed increments (code or models) conforming to the Epic and
  the architecture.

### Solution Shipper

**Mandate:** oversee delivery to the client, like a PM adapted to Shape-Up, responsible for
delivering what the client requested (ideally a bit more, to keep the client happy).

- **Accountable for:** release & deploy; contract-conformance check; sign-off on the review gate
  closing before anything reaches a client: the commercial-plane delivery accountability, paired
  with but distinct from the Builder's Epic/architecture-spec accountability.
- **Skills drawn on:** [`skills/ci-cd-delivery/SKILL.md`](../skills/ci-cd-delivery/SKILL.md),
  [`skills/meaningfy-release/SKILL.md`](../skills/meaningfy-release/SKILL.md).
- **Artifacts produced:** the shipped release, the contract-conformance check, the client handover.

## RACI legend and invariants

| Mark | Meaning |
|---|---|
| **A** | Accountable: answers for the outcome; exactly one per row |
| **R** | Responsible: does the work |
| **C** | Consulted: informs before/during the work |
| **I** | Informed: kept up to date after the fact |
| **–** | Not involved |

> **Invariant 1: exactly one `A` per row.** Every activity has exactly one accountable role (alone
> or combined as `A/R`). A row with zero `A` marks or with more than one is not published; if no role
> genuinely fits, the activity is named under Known gaps instead of forced onto a column.
>
> **Invariant 2: roles are responsibilities in a process, not competences or headcount.** A role is
> not a skills/competency/seniority profile (Semantic Engineer, Software Engineer, DevOps Engineer,
> QA Engineer are profiles, not roles) and not a staffing commitment: one person may hold several
> roles on a small engagement, and two people may share one role. The matrix constrains
> accountability, not who is hired or how many people are on the project.

## RACI matrix

| Activity | Sales/Presales | Technical Consultant | Solution Architect | Work Shaper | Solution Builder | Solution Shipper |
|---|---|---|---|---|---|---|
| Presale | A/R | C | – | – | – | – |
| Discovery & Onboarding, Light tier | A | R | C | – | – | – |
| Discovery & Onboarding, Deep tier | A | R | C | C | – | – |
| Requirements & UC, shallow (White, via the Deep tier) | C | A/R | I | – | – | – |
| Requirements & UC, deep (White+Blue, via the build contract) | I | C | A/R | – | C | – |
| ADLC | I | C | A/R | C | C | – |
| MDLC-lite | – | – | A | – | R | – |
| MDLC-standalone | C | C | A *(no owning skill; parked capability gap)* | – | – | – |
| Project/repo setup | – | – | C | – | A/R | – |
| Epic/work shaping | – | – | C | **A/R** | C | C |
| Epic build (BDD/TDD) | – | – | C | I | A/R | I |
| Review | – | – | C | – | R | A |
| Release & deploy | – | – | – | I | R | A |
| Contract-conformance check | I | C | – | I | C | A/R |
| CBLC-lite | – | – | – | – | A/R | I |
| CBLC-standalone | C | – | – | C | R | A |
| Partnership/account nurture | A/R | C | – | – | – | I |

**CBLC** (Capacity-Building Life Cycle, named in this doc set alongside ADLC and MDLC) covers
training and capability-building work: **-lite** runs inside an existing software contract;
**-standalone** is its own dedicated training engagement.

Every row above has exactly one `A` (alone or as `A/R`), verified by inspection, row by row, per
Invariant 1; no row carries zero or two.

## Adaptation notes

Two handbook roles are not carried forward as named roles. Each note below cites the handbook page
it replaces (see [`openspec/changes/define-roles-and-raci/inputs/2026-07-26-handbook-findings.md`](../openspec/changes/define-roles-and-raci/inputs/2026-07-26-handbook-findings.md)).

**Quality Overseer (handbook p. 67).** The handbook's Reviewer mandate (the four-eyes principle,
every piece of work reviewed by another qualified team member against the Epic Pitch specification,
methodologies, and best practices) is not carried forward as a dedicated role. That review is now
largely agent-assisted (see [`skills/meaningfy-code-review/SKILL.md`](../skills/meaningfy-code-review/SKILL.md)'s
multi-lens automated review): the **Solution Builder** does the work, the **Solution Shipper** signs
off as the row's `A`, and on non-software-plane reviews with no client-facing shipment in that
increment, the **Work Shaper** signs off as `R` while the Shipper remains `A`. No dedicated review
headcount exists in this model.

**Customer Success Manager (handbook p. 68).** The handbook's Customer Success Manager
(client-relationship management, expectation management, status/demo meetings, post-delivery
aftercare, satisfaction reviews, ceremonial handover) folds into **Sales/Presales**' partnership/account-nurture
row rather than becoming a seventh column; both roles owning one activity's accountability would
break Invariant 1.

## Open question: agent wrappers

Whether any role beyond the Builder ever gets a dedicated Claude Code agent is an open fork, stated
here as a priority, not a commitment:

- **Today's default:** documentation-only. The agent roster stays `epic-planner`, `implementer`,
  `code-reviewer`; no new agent or agent stub is added for any of the other five roles.
- **Reopening condition:** this stays closed until a role has actually been exercised on a real
  engagement; the fork is not resolved speculatively.
- **Priority order if it ever reopens:** **Work Shaper is the highest-priority candidate**, because
  `epic-planner` already performs most of the Work Shaper mandate: a dedicated wrapper there would
  be a thin steering layer over an existing agent, not new capability. The other four roles have no
  existing agent covering their mandates and rank lower. This is a priority statement only: no agent,
  no stub, and no recommendation to build one is made here.

## Known gaps

| Gap | Nature | Owner / next step |
|---|---|---|
| **A `work-shaper` agent wrapper** | Highest-priority candidate of all deferred agent questions: `epic-planner` already performs most of the Work Shaper mandate, so this would be a thin steering layer, not new capability. | Deferred (see Open question above). Reopens once the role has been exercised on a real engagement. Not built here. |
| **Agent wrappers for the other four non-Builder roles** | Lower priority; no existing agent covers their mandates. | Deferred, same condition. |
| **MDLC-standalone has no owning skill** | Genuine capability gap: the ontology/application-profile development methodology (METHONTOLOGY/NeOn/LOT-style) has no skill; `conceptual-modelling` explicitly scopes itself to product-development projects. | Parked for its own shaping cycle. Visible on the matrix as the MDLC-standalone row. |
| **Agent-assisted review has no non-software equivalent** | `meaningfy-code-review` is code-scoped. The Quality Overseer headcount is retired across *all* planes, but the automated multi-lens review that replaces it exists only for the software plane; ontology and training-material review currently fall back to unaided human sign-off. | Named only. Candidate future skill; not designed here. |
| **Vocabulary consistency pass pending** | This doc's activity names are provisional until the sibling changes below publish theirs. | Required follow-up: a rename-and-check pass, not a re-derivation, once those changes land. |

## References

| Doc | What it defines |
|---|---|
| [`../openspec/changes/define-blc-engagement-model/proposal.md`](../openspec/changes/define-blc-engagement-model/proposal.md) | the corrected commercial model whose activities (presale, Discovery & Onboarding, partnership/account nurture) this matrix assigns owners to |
| [`../openspec/changes/define-meaningfy-lifecycle/proposal.md`](../openspec/changes/define-meaningfy-lifecycle/proposal.md) | the ADLC/MDLC-lite build loop and Requirements & UC rows |
| [`../openspec/changes/define-delivery-release-lifecycle/proposal.md`](../openspec/changes/define-delivery-release-lifecycle/proposal.md) | the dual-DoD lane the Review and Release & deploy rows point at |
| [`../openspec/changes/define-lifecycle-playbooks/proposal.md`](../openspec/changes/define-lifecycle-playbooks/proposal.md) | the six per-role playbooks derived as filtered views over this matrix |
| [`../openspec/changes/define-roles-and-raci/inputs/2026-07-26-handbook-findings.md`](../openspec/changes/define-roles-and-raci/inputs/2026-07-26-handbook-findings.md) | the Employee Handbook excerpt (pp. 65–68) this doc's six roles and adaptation notes are drawn from |
