# Sales DoD: Definition of Done for the commercial plane

**Audience:** Sales/Presales and the Solution Shipper.

**Purpose:** the Shipper's Definition of Done, the commercial-plane check that runs alongside the
Builder's DoD. For the build-plane DoD and the gate ladder it closes against, see
[`docs/ai-coding/dod-quality-gates.md`](../ai-coding/dod-quality-gates.md). This file does not
restate that doc's build-tier content.

**The Shipper's DoD (contract conformance)** is whether the shipped increment matches what was
promised to the client. It closes together with the Builder's DoD, on a different, commercial plane.
It asks one question: **did we deliver what was promised?** The check runs against a written
trail (**request for offer, offer, contract, and meeting minutes / documented exchanges**),
adapted from Meaningfy's pre-agent operating practice, and it is led by the **Shipper** role
(defined in
[`docs/roles-and-raci.md`](../roles-and-raci.md#solution-shipper)).

This verdict is a **human sign-off**, not CI-automatable: no pipeline check can confirm a
client's promise was kept; a person reads the trail and decides. In practice this is
**light-touch and agent-assisted**: an agent can assemble and cross-check the document trail, but
the sign-off itself stays human.

When this DoD and the Builder's DoD disagree, neither one wins by default: see the Disagreement
rule in [`docs/ai-coding/dod-quality-gates.md#delivery--release`](../ai-coding/dod-quality-gates.md#delivery--release),
which governs both DoDs and is defined there once, not restated here.
