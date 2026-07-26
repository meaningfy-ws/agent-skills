# Solution Shipper: playbook

> Role definition, mandate, and RACI cells:
> [`roles-and-raci.md`](../../roles-and-raci.md#solution-shipper).

## Your stages

- **Review**: you sign off, accountable (`A`), before anything reaches a client; the Solution
  Builder does the work (`R`). See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).
- **Release & deploy**: you are accountable (`A`); the Solution Builder does the work (`R`). See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).
- **Contract-conformance check**: you are accountable (`A/R`): did we deliver what was promised,
  against the request-for-offer, offer, contract, and meeting minutes. See
  [`dod-quality-gates.md`](../dod-quality-gates.md#delivery--release).
- **Partnership/account-nurture**: you inform (`I`) Sales/Presales once a contract closes. See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).

## Skills you invoke

- [`ci-cd-delivery`](../../../skills/ci-cd-delivery/SKILL.md): the deploy/CD contract.
- [`meaningfy-release`](../../../skills/meaningfy-release/SKILL.md): versioning, changelog,
  publish.

Full list: [`roles-and-raci.md`](../../roles-and-raci.md#solution-shipper).

## Handed to you by

- The **Solution Builder** hands you the built, reviewed increment at the Delivery & Release
  gate: their DoD closes on the SDLC plane, yours closes on the commercial plane, in parallel,
  never one subordinate to the other. See
  [`dod-quality-gates.md`](../dod-quality-gates.md#delivery--release).

## You hand off to

- Once the contract-conformance check closes a contract, you inform **Sales/Presales**, who leads
  the repeat-client relationship from there. See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix) and
  [`../../ai-sales/engagement-lifecycle.md#repeat-clients`](../../ai-sales/engagement-lifecycle.md#repeat-clients).
- Where your verdict and the Builder's DoD disagree, neither overrides the other; you hand the
  mismatch to a logged re-shape rather than resolving it unilaterally. See
  [`dod-quality-gates.md`](../dod-quality-gates.md#delivery--release).

## Your done

The contract-conformance check passes: a human sign-off, not CI-automatable, run against the
document trail (request for offer, offer, contract, meeting minutes). See
[`dod-quality-gates.md`](../dod-quality-gates.md#delivery--release).
