# The Advisory Runbook

**Audience:** the Technical Consultant, and anyone stepping into that role during a Deep-tier
engagement.

**Purpose:** the day-to-day operational script for a Deep-tier engagement, from intake to hand-off.
The techniques a step might call on live in [`methods/`](methods/); the commercial facts (tiers,
durations, safeguards) live in
[`docs/ai-sales/engagement-lifecycle.md`](../ai-sales/engagement-lifecycle.md); the deliverable
itself is owned by the [`decision-package`](../../skills/decision-package/SKILL.md) skill. This
runbook sequences those pieces; it does not restate any of them.

A runbook is the one operational script for this domain, in order, regardless of who's doing which
step; a playbook (see the `playbooks/` folder alongside this file) is the same flow filtered to one
role's view of it.

---

## 1. Intake

Establish the deciding persona, the problem in the client's own situation, and the measurable
outcome they want. See
[`skills/decision-package/references/discovery-flow.md` §1](../../skills/decision-package/references/discovery-flow.md#1-structured-discovery).

## 2. Landscape reading

Read the data estate, governance maturity, and legacy constraints the recommendation must fit
inside. See
[`skills/decision-package/references/discovery-flow.md` §2](../../skills/decision-package/references/discovery-flow.md#2-landscape--data-reading).

## 3. Method selection

Decide which technique in [`methods/`](methods/) the engagement actually needs. **Gap analysis is
always in scope**, because it is how step 4 below is done, and it has a real owner (see
[`methods/gap-analysis.md`](methods/gap-analysis.md)). Wardley mapping, enterprise/process
modelling, data-maturity assessment, and semantic-maturity assessment are named techniques with no
owning skill today; if intake surfaces a need for one of them, say so plainly to the client rather
than delivering an ad-hoc version of it under the Decision Package's name. See each stub in
[`methods/`](methods/) for what specifically is missing.

## 4. Gap analysis, option framing, sequencing, and buy/build/defer

This is the substantive core of the engagement, and the one step this runbook states in full
rather than pointing past. Compare the current state (steps 1-2) against the client's strategic
ambition and classify every gap as blocking, sequenced, or out of scope. Frame the candidate first
initiatives as genuine options, each with its trade-off. Order the chosen option into a pilot to
scale roadmap, naming what is explicitly not in the first step. For each capability the roadmap
needs, decide buy, build, or defer, with a one-line rationale. See
[`skills/decision-package/references/discovery-flow.md` §3-6](../../skills/decision-package/references/discovery-flow.md#3-gap-analysis)
for the detail behind each of these four moves; this runbook sequences them, it does not repeat
their content.

## 5. Decision Package production

Assemble the five required parts (recommendation, scope, sequenced roadmap, buy/build/defer
decisions, ready-to-contract execution brief) into the Decision Package itself. See the
[`decision-package`](../../skills/decision-package/SKILL.md) skill's own deliverable definition;
this runbook names the step, the skill owns the artefact.

## 6. Hand-off

Assemble the ready-to-contract execution brief and hand it to the build tier, or to the client to
execute elsewhere. Execution is always a separate engagement. See
[`skills/decision-package/references/discovery-flow.md` §7](../../skills/decision-package/references/discovery-flow.md#7-execution-brief).

---

Steps 1, 2, 5, and 6 are thin pointers on purpose: the source material behind them is already
settled elsewhere, and restating it here would create a second copy to keep in sync. Step 4 is
written in full because the sequencing of a Deep-tier engagement is fully known today; only the
individual techniques in [`methods/`](methods/) are the open gap, not the script that calls on
them.
