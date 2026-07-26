# Discovery & Onboarding

The narrate-and-point detail behind the `ai-sales` domain. The canonical *coaching* intentions
of each stage live in the coach's
[`engagement-model.md`](../../skills/semantic-consulting-coach/references/engagement-model.md);
this file states the commercial facts, maps each stage to its owning skill(s), and the boundary
that protects it. It restates no skill's rules.

## The free→paid boundary

**Presale is the only free stage**: everything that produces a deliverable is sold. Presale
answers *"are we even relevant to each other?"*; the moment talk shifts to *"what should we do?"*
or *"build this for us"*, a paid stage has been reached.

---

## Presale (free, no deliverable)

**Question:** "Is this even relevant to us?" · **Commercial:** free (precisely because it
produces no deliverable).

Mutual recognition. Teach generously but never deeply customise; the moment talk shifts from *"is
this relevant?"* to *"what should we do?"* or *"build this for us"*, presale has reached its
boundary and the next step is Discovery & Onboarding or direct-to-build below, not more free
discussion.

- **Owner:** [`semantic-consulting-coach`](../../skills/semantic-consulting-coach/SKILL.md):
  it holds the free→paid line and coaches which paid path fits.

---

## Discovery & Onboarding (paid, two depths)

A client's first paid purchase is a **single package sold at two depths**, not two different
products: a **Light** tier and a **Deep** tier. Both answer the same underlying question
("what should we do, and why?") at a depth the client chooses.

| Tier | Duration | Best for |
|---|---|---|
| **Light** | A 1–2 day workshop | a fast, expert read on the client's situation |
| **Deep** | 4–6 weeks, calendar-boxed | a safe, informed decision about what to build next |

Both tiers work from the same method: a gap analysis of where the client is today against where
it needs to be. The Light tier turns that gap analysis into a fast, expert read and a strategic
roadmap. The Deep tier turns it into the **Decision Package** (see `decision-package` under
Skills, below): a recommendation, in/out scope, a pilot-to-scale roadmap, and a buy/build/defer
call, produced by running gap analysis against the client's strategic ambition (distinct from a
formal semantic and data maturity assessment, a separate, separately-sellable service). Depth
changes how thoroughly we get there, and, at the Deep tier, what we hand back.

**Duration note (Deep tier):** the 4–6 weeks is **calendar-based, not effort-based**, stated
alongside the number because the number alone could be misread as an effort estimate; this model is
not priced by a man-day count or a rate card.

**Safeguards (existing practice, captured here as a rule):** if, for reasons outside Meaningfy's
control (stakeholder availability, information access, late decision-makers, reorganisations), the
agreed outcomes cannot reasonably be reached within the agreed duration, Meaningfy signals this
explicitly and proposes one of exactly three options: **a scope reduction, a short extension, or
a formal stop with partial delivery**, never a silent overrun.

The skills behind Discovery & Onboarding, and what each owns:

- [`semantic-consulting-coach`](../../skills/semantic-consulting-coach/SKILL.md) coaches which
  depth fits and holds the free→paid line into the Light tier.
- [`proposal-writing`](../../skills/proposal-writing/SKILL.md) is the **entry skill** for the Deep
  tier: qualifies the need, frames the offer, prices it as a fixed frame, and writes the
  **proposal + SoW** with an explicit in/out scope boundary.
- [`estimation`](../../skills/estimation/SKILL.md) is the **pricing/scoping** discipline
  (PERT + work breakdown + ranges + contingency) that `proposal-writing` invokes for the numbers;
  independently triggerable.
- [`decision-package`](../../skills/decision-package/SKILL.md) **produces** the Deep tier's
  deliverable: recommendation, in/out scope, pilot→scale roadmap, buy/build/defer, and the
  ready-to-contract execution brief that hands off to a build contract.

**Boundary:** execution is *always* a separate engagement. Discovery & Onboarding earns the right
to say *"from here, we can execute, or you can take this and execute with someone else."*

### Direct-to-build

**Question:** "We know what we want: build it." · **Commercial:** paid, separately scoped.

A client who already knows what they want can buy a build contract directly, skipping Discovery &
Onboarding. Its precondition is an **input condition**, not a gate to pass: the requirements/use-case
elicitation Discovery & Onboarding would have supplied must instead be done, at depth, at the start
of the build contract.

This is a different elicitation from the sales-strategy elicitation presale and the Light tier run
(pain points, fears, aspirations, the values a client decides by: psychological, goal-oriented,
input to a proposal). Use-case elicitation produces `architecture`'s UC White (contract-level) and
UC Blue (realisation-level) behaviour specifications; at the business level expect at most a sketchy
UC White, and often not even that: real use-case work happens once the build contract starts.

- **Pointer:** [`../ai-coding/build-lifecycle.md`](../ai-coding/build-lifecycle.md) (the
  PROJECT and Epic tiers).

---

## The outcome: Semantic Layer adoption

Whichever path a client takes (Discovery & Onboarding or straight to build), Meaningfy engagements
lead to the same place: **Semantic Layer adoption**. A Semantic Layer isn't a single off-the-shelf
deliverable; it's shaped to the client's own organisational configuration: modelled, connected,
and operated the way that specific organisation needs, not a generic template dropped in place.

The Semantic Layer decomposes into **building blocks**:

- Modelling / ontology
- Software development
- Data mappings & integration
- Analytics / BI connections
- Agentic framework development
- Training & capability building

A commercial project scopes against **one** of these blocks, **several** of them, or the **whole**
Semantic Layer, always in a controlled, scoped way. This is composable, not a menu of fixed
contract types: a client buys exactly the blocks it needs today, and nothing stops it adding more
later. See [`semantic-layer-services.md`](semantic-layer-services.md) for where each block is
catalogued as a sellable line.

The hand-off into a build contract is Discovery & Onboarding's ready-to-contract execution brief
(see [`decision-package`](../../skills/decision-package/SKILL.md)), which becomes the parent of
the first architecture/requirement artefacts; direct-to-build hands off via its own
start-of-contract elicitation instead. See
[`../ai-coding/build-lifecycle.md`](../ai-coding/build-lifecycle.md) for what happens next.

---

## Repeat clients

A client who has closed **two or more contracts** is a repeat client, stated as a plain fact, not
a capitalised status label ("Partner") and not a numbered phase. No status is awarded, recorded, or
expires; it is simply true or not true at any given moment, alongside whatever engagement is
currently live.

The relationship work that follows (governance support, semantic operations, capability
building, sustaining and evolving what was built) is real and continues; it is described here as
**relationship work**, not phase work, and it has an owner: **Sales/Presales leads the
repeat-client relationship**, drawing on
[`executive-communication`](../../skills/executive-communication/SKILL.md) for the client-facing
messaging and board-level framing Sales/Presales uses in that role.

### Hand-off into the relationship

Once the contract-conformance check (see
[`docs/ai-coding/dod-quality-gates.md`](../ai-coding/dod-quality-gates.md#delivery--release))
closes a contract, the **Solution Shipper** informs Sales/Presales, who takes the relationship from
there. See
[`roles-and-raci.md`](../roles-and-raci.md#raci-matrix) for the accountability cells.

### Your done

Partnership/account-nurture has no closing condition; it continues for as long as the
relationship does.

---

## Known gaps

The wider commercial mechanics of the front-of-funnel are **still to be brainstormed and
crystallised**, and must not be invented here. Open items:

- **Qualification:** the criteria and signals that move a prospect to a paid stage.
- **Pre-sale:** nurture, discovery cadence, when to propose.
- **Sale:** closing mechanics, the proposal/SoW motion (skill exists:
  [`proposal-writing`](../../skills/proposal-writing/SKILL.md); the *commercial process*
  around it does not).
- **Marketing:** positioning, content, demand generation.
- **CRM & lead communication:** pipeline, follow-up, lead nurture.
- **Fit-for-market:** segment fit, B2B vs B2G motion differences.

These are placeholders, not commitments. For the full, numbered list of named gaps (the presale
process itself, demo preparation, CRM/lead skill, strategic-negotiation thinking, the safeguards'
contractual mechanics, services-inventory population, and MDLC-standalone ontology
methodology), see the **Known gaps** table in
[`define-blc-engagement-model`'s proposal](../../openspec/changes/define-blc-engagement-model/proposal.md#known-gaps),
which is the single place to check; it is not duplicated here.
