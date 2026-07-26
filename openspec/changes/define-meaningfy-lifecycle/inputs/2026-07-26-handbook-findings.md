# Seed — Employee Handbook (2nd ed., 2026): excerpts relevant to the build plane

**Status:** secondary input, preserved record. Never groomed, never deleted (see the EPIC's No-gos).
**Date captured:** 2026-07-26. **Round:** 2 (post-review).

**Canonical source, not duplicated here:** `Employee Handbook - Second Edition (2026) (1).pdf`
(104 pp.) lives at
[`openspec/changes/define-lifecycle-playbooks/inputs/`](../../define-lifecycle-playbooks/inputs/),
alongside `decission-phase-advisory.md` and `presales-material.md`. This file summarises **only the
excerpt bearing on `define-meaningfy-lifecycle`** (the build plane); page numbers below are the
handbook's own (footer numbering).

**How to read it** (human instruction, round 2, verbatim): *"assume the provided materials are
outdated, but of good quality and need to be carried forward to a modern way of working where people
govern, and steer and check lightly the heavy work of LLM agents"*. Port the **substance** (project
shape, gates, patterns), never the pre-LLM mechanics (Jira minutiae, Slack channels, timesheets,
career levels).

---

## 1. Project anatomy (§15, p. 46) — the pre-LLM precedent for the PROJECT/EPIC tier split

Verbatim: *"Our work is organised into projects. Each project begins with a charter, is shaped before
execution into deliverables, and is shipped to stakeholders (internal or external). … Before
execution begins, work is shaped so that builders can proceed effectively. … Shipping starts once
deliverables are ready. After deliverables are shipped and accepted by stakeholders, the project is
closed. Customer success management and communication are continuous activities, beginning at project
inception and extending beyond project closure."*

The accompanying timeline shows three overlapping bands — **Conception** (project initiated → Project
Charter complete → kick-off), **Shaping & Building** ("Shaping up work & Planning execution"
overlapping "Executing planned work (Building)"), **Shipping** ("Progressive shipping") — with
**Customer Success Management & Communication** running as one continuous lane underneath all three.

Relevance: this is the same nesting the build-plane doc calls PROJECT tier (runs once, up front) vs
EPIC tier (runs per Epic), stated a year earlier in human-team vocabulary. It supports keeping the
nesting while retiring the "two-tier" *name* (DEC-1), and it validates one end-to-end picture rather
than several fragments.

## 2. BPMN workflow diagram (§22, pp. 62–63) — precedent for one whole-plane diagram

Verbatim: *"we've created a Business Process Model and Notation (BPMN) diagram to illustrate the
complete end-to-end process of how projects are initiated, executed, and delivered at Meaningfy. This
diagram serves as a concise visual guide."* Stated purposes: *"Simplify Complexity"*, *"Quick
Reference"*, *"Alignment"*. Its five labelled phases: Project Conception, Work Shaping, Project
Execution, Shipping Phase, Customer Success and Feedback.

Relevance: direct precedent for DEC-9 (one diagram covering the whole build plane). The handbook's
phase set also confirms Shipping and Customer Success sit **outside** the build loop proper — matching
this EPIC's decision to render Delivery & Release as a single terminal node pointing at epic 3.

## 3. Governance model — the round-2 steering quote (human, not handbook)

Verbatim: *"people must mainly supervise and guide while LLM agents do the work and quality
assessment verification, and documentation people are mainly supposed to have minimal engagement in
steering and having an easy way to check if they got what they wanted."*

Relevance: becomes a named principle in the rewritten `build-lifecycle.md` (DEC-18) rather than
staying implicit in DEC-15's model-tiering carry-forward. It is also the lens through which the two
patterns below must eventually be adapted: the handbook assumes human reviewers at every gate; the
modern shape assumes agent execution + verification with cheap human confirmation.

## 4. "Managing Out-of-Contract Improvements" (§18, p. 52) — named as a gap, not designed

Load-bearing lines, verbatim:

- *"The 'Improvements Outside Contract' EPIC is **not a general rule** but a **case-by-case
  approach**."*
- *"The EPIC should be created within the project, and not in Meaningfy PM, to maintain clarity and
  accountability at the team level."*
- *"Every EPIC must be well-defined and have a clear appetite (time budget allocated). A proper EPIC
  PITCH should be prepared according to our internal guidelines to avoid accumulating unplanned
  activities that might impact project deliveries."*
- *"Activities included in the EPIC must be validated at the conceptual level by [management] to
  ensure efficient and appropriate resource allocation."*
- *"We must ensure that these activities cannot initially be integrated into one of the existing WPs
  under the current contract."*
- Key consideration: *"If an improvement task cannot be absorbed into an active EPIC/WP, it means the
  scope is too large, or the idea is too ambitious, and should be handled through a dedicated new EPIC
  — 'Improvements Outside Contract'."*

## 5. "Redelivery Policy" (§20, pp. 55–56) — named as a gap, not designed

Load-bearing lines, verbatim:

- Purpose: *"Establish a clear, repeatable process for re-delivery work driven by client or
  operational feedback, without compromising the traceability or stability of the original Epics."*
- A new EPIC is required if: *"new elements are added / the scope is extended / the effort is
  significantly higher / the original appetite is exceeded / it becomes a new iteration of work. In
  this case, we also need a new Shape Up process and an Epic Pitch."*
- Stay in the same EPIC only if: *"the feedback is minor / it does not extend the scope / it fits
  within the original appetite / no new requirements are introduced."*
- Closing the initial Epic: *"At the end of the first delivery, mark the Epic **Done** and close it —
  regardless of final acceptance."*
- Creating the new one: *"Open a dedicated Epic for redelivery only, with a new appetite and pitch."*
  Minimum fields: title *"[Component] Redelivery"*, summary *"Rework as per client/operational
  feedback"*.
- Logging: *"Create all sub-tasks and stories exclusively in the new Epic. Do not open new tickets or
  log additional hours against the closed (Done) Epics."*
- Traceability: *"In the new Epic's comments, reference the original Epic and state the reason for
  redelivery."*
- Post-redelivery review: **Lessons Learned** by default (*"Within 5 working days of finishing a
  redelivery"* — what worked, what didn't, immediate improvement actions), and a **Post-Mortem**
  *"when required"* — *"If the redelivery exceeds the new appetite or uncovers critical issues, run a
  formal root-cause analysis."*

**Both patterns are named, not designed, in this EPIC** — see the proposal's *Known gaps* subsection
under Rabbit-holes. They have no skillery-side equivalent today and are candidates for `epic-planning`
or `spec-stewardship` to own in a separately-shaped future EPIC.

## 6. Read but out of scope for this EPIC

- §19 *Project shipping* / Delivery Manager ("The Shipper"), incl. the *Contractual Validation* step
  (*"Review the deliverables against the contractual agreement"*) — **epic 3**
  (`define-delivery-release-lifecycle`) and **epic 1** (`define-blc-engagement-model`) own it.
- §§24–27 *Role structure* / *Brief* / *Allegory: what are the project roles?* (six named project
  roles, incl. **Project Owner — the Work Shaper**) — **epic 4** (`define-roles-and-raci`) owns it;
  this EPIC's No-gos already forbid naming roles in the build-plane doc.
- §17 *Agile project execution* (sprints, deep work/cooldown, appetite-not-estimates) and §21 *Project
  Rituals* — team-cadence mechanics, deliberately not ported into the build-plane doc.
