# Seed — Employee Handbook + Decision-Phase advisory (excerpt for `define-blc-engagement-model`)

**Status: SEED — secondary, preserved, never groomed.** Round-2 input, dated 2026-07-26. Like
[`2026-07-25-brainstorm-seed.md`](2026-07-25-brainstorm-seed.md), `proposal.md` supersedes this file
as the *primary, shaped* truth but does not replace it; where the two disagree, the proposal wins and
the disagreement is traceable to a `DEC-`. Do not edit, condense, or "update" this file.

## Provenance and where the full text lives

Two source documents were supplied by Eugeniu Costetchi and physically archived, in full, at
[`openspec/changes/define-lifecycle-playbooks/inputs/`](../../define-lifecycle-playbooks/inputs/):

| Source | Canonical path | What it is |
|---|---|---|
| `Employee Handbook - Second Edition (2026) (1).pdf` (103 pp.) | `define-lifecycle-playbooks/inputs/` | Meaningfy's pre-LLM-agent operating manual, incl. the six project roles (§ *Role structure*, pp. 65–70) |
| `decission-phase-advisory.md` | `define-lifecycle-playbooks/inputs/` | Three registers of the P1 Decision Phase: operational definition, internal posture/discipline, client-facing narrative |
| `presales-material.md` | `define-lifecycle-playbooks/inputs/` | The pre-existing presale/discovery sheet and the original P0–P3 framing this epic corrects |

**They are deliberately not duplicated here.** This file quotes only the load-bearing excerpts that
bear on `define-blc-engagement-model`, per the round-2 archiving instruction. For anything else, read
the canonical files.

A third source is the human's own **inline `EC:` review comments**, written directly into round 1's
`proposal.md` and removed from it once resolved. They are preserved verbatim in §6 below so the
directives remain traceable after the proposal text was cleaned.

## Ground rule carried into round 2 (verbatim, from the human)

> "work autonomously towards the completion of this task just up to the moment you are ready to
> implement, ask nothing, assume the provided materials are outdated, but of good quality and need
> to be carried forward to a modern way of working where people govern, and steer and check lightly
> the heavy work of LLM agents"

---

## 1. P1 Decision Phase — duration (corrects the round-1 seed)

`decission-phase-advisory.md`, § *Structure of the Decision Phase → Duration*:

> Typically 6–8 weeks
>
> Calendar-based, not effort-based

And in the client-facing register:

> The Decision Phase typically runs for six to eight weeks and is carried out by a small senior team
> from Meaningfy.

The round-1 brainstorm seed carried "**4-6wk**". That figure is superseded. No file in the repo
states a P1 duration today, so this is a new fact being introduced, not a correction of live text.

Commercial model, same section:

> Fixed price · Fixed duration · Variable depth handled explicitly (see safeguards below)

> we do not anchor the Decision Phase to a predefined number of man-days or a rate card

## 2. The safeguards mechanism (existing practice, previously undocumented)

`decission-phase-advisory.md`, § *Safeguards & boundaries*:

> If, due to factors outside Meaningfy's control (availability of stakeholders, access to
> information), the agreed outcomes cannot reasonably be reached within the agreed duration,
> Meaningfy will:
>
> Explicitly signal the issue
>
> Propose one of:
>
> A scope reduction
>
> A short extension
>
> A formal stop with partial delivery
>
> This avoids silent overwork and preserves trust.

The client-facing register names the triggering risk factors:

> limited availability of key stakeholders, late involvement of decision-makers, fragmented or
> contradictory information across teams, ongoing internal reorganisations, or parallel initiatives
> that change priorities mid-stream. These are not exceptional situations; they are common in
> complex organisations.

## 3. Internal posture and discipline (for the coach skill)

`decission-phase-advisory.md`, second register — *"the internal posture, behaviour, and decision
discipline Meaningfy adopts during the Decision Phase … written for senior consultants and
leadership, not as a sales script and not as a junior playbook."* Its stated purpose: that under
pressure Meaningfy consistently acts as

> a safe pair of hands – highly skilled, calm, respectful, and firm in its professional boundaries.

Load-bearing principles:

- **Ambiguity is a signal, not a failure.** *"When a client is vague, contradictory, or unsure, this
  is not a weakness to compensate for. It is a signal that a decision has not yet been made … Our
  task is not to resolve ambiguity immediately, but to hold it safely until it can be resolved
  deliberately."*
- **Helpfulness vs usefulness.** *"Helpfulness – answering questions, explaining concepts, reacting
  quickly. Usefulness – enabling the client to make a decision that will hold over time. In the
  Decision Phase, usefulness always takes priority over helpfulness."*
- **We do not guess.** No architectural sketches, sequencing recommendations, pilot definitions, or
  governance designs *"based on partial or informal understanding. When information is insufficient,
  we say so — calmly and explicitly."*
- **Calm under pressure.** *"Client urgency does not transfer to us … our response is to slow the
  interaction down, not accelerate it. Calm is not passivity. Calm is control."*
- **No need to prove expertise.** *"If we feel the need to impress, we are already outside our
  professional posture."*
- **Protective, not defensive, formulations.** *"We can, but that would be guesswork at this
  stage."* · *"We could sketch something, but it would not be responsible without context."* ·
  *"Giving you something quick now may cost you more later."*
- **Redirect, don't block.** *"The right way to create value here is to clarify a few decisions
  first."* · *"This is exactly what our Decision Phase is designed to address."*
- **Yes / not yet.** *"We say yes to orientation, explanation, and clarification. We say not yet to
  recommendations, sequencing, and commitments. 'Not yet' is not refusal. It is sequencing."*
- **End cleanly.** Summarise what is known, what is undecided, what step would be required — then
  pause. *"Silence is an acceptable outcome."*
- **Internal red flags** (pause and reassess): answering the same contextual questions repeatedly;
  sketching solutions with no ownership on the client side; feeling pressure to justify our value;
  the client avoiding decision authority or budget.
- **Final principle.** *"We are not here to move fast. We are here to move right."*

Also relevant to the free/paid line, § *Internal note (for Meaningfy)*:

> If a client asks for recommendations, sequencing, or scoping before committing to this phase, that
> is a signal to pause and propose the Decision Phase explicitly. This is the boundary between free
> orientation and paid value.

## 4. The six project roles (context only — `define-roles-and-raci` owns this)

Employee Handbook, § *Role structure — On Roles, Profiles and Levels* (p. 65), verbatim:

> Roles are defined in terms of responsibilities in the company or a project. Most often we refer to
> project roles (real-world equivalents in parentheses):
> • Mastermind Wizard (Business Developer) • Shaper (Project Owner) • Builder (Engineering or
> Implementation Lead) • Shipper (Delivery Manager) • Quality Overseer (QA Lead) • Customer Success
> Manager (Client Relationship Manager)

Profiles (distinct from roles) are *Semantic Engineer, Software Engineer, DevOps Engineer, QA
Engineer*.

**Consequence for the wider round:** Meaningfy already names a **Work Shaper** (Project Owner) role,
which the round-1 five-role model omitted. `define-roles-and-raci` and `define-lifecycle-playbooks`
are adding it as a real sixth role. This epic defines no roles (see its No-gos) — the finding is
recorded here only so that any role name this epic *cites* stays consistent with the six-role model.

## 5. The Shipper's document trail (feeds the contract-conformance DoD)

Employee Handbook, § *Brief: what are the project roles?* (pp. 66–68):

- **Project Owner / Work Shaper:** *"Developing the Work Breakdown Structure based on the request for
  offer, the offer and adjacent meeting notes with the client."*
- **Business Developer:** *"Develop a clear, and comprehensive project offer for the client that
  delimits clearly the scope, deadlines, and the approach."*
- **Delivery Manager / Shipper:** *"Conducting comprehensive inspections of the deliverables to
  guarantee quality and adherence to contract specifications"* … *"Facilitating a seamless handover
  process, achieving full client satisfaction and contractual compliance."*

Together these name the concrete written trail a contract-conformance check runs against: **request
for offer → offer → contract → meeting minutes and documented exchanges**.

Two handbook roles that this round deliberately does **not** carry forward as roles, recorded here
as precedent: the **Quality Overseer** (its four-eyes review is now largely automated agent review
with light human sign-off) and the **Customer Success Manager** (*"maintaining and enhancing customer
relationships … client aftercare … long-term customer relationship management"* — in the corrected
model this is Sales/Presales' repeat-client relationship work, not a separate role).

## 6. The human's inline `EC:` directives on round-1 `proposal.md` (verbatim)

Written into round 1's `proposal.md` and removed from it once resolved in round 2. Preserved here so
the directives stay traceable. Typos are the human's; quoted as written.

On **DEC-2** (new inputs and missing presale skills):

> there shall be place for new inputs, for example on how we do presale and sale, what is the process
> before up to singing a contract.
> In the presale there is a variety of skills needed, for example executive communication in
> preparing the presentations and naotehr skill in rpeparing the demos.
> And we need a skill for clearly keeping communcation with the leads and feed on each mset of
> meeting minutes and groom the CRM, and send emails, and plan strategiclaly according to Chriss
> Voss, Robert Greene and SunZhi. Yes we need also a strategic thinking agent/skill that can think o
> fthe relationships like a chess game, cold calculated, deeply psychological.

On **DEC-3** (services inventory):

> we must have the possibility to add an inventry of services and standard packages, and that inventr
> must be ease to edt and maintain and it cna serve as reference for any further skills and processes
> and vice versa.

On **DEC-4** (sales-strategy vs use-case elicitation):

> we must distinguish between sales strategy steps (e.g. elicit pain points, fears and fantasies, and
> values they play by) from concrete use cases elicitation that already can be framed and moved
> towards an offer based on the discusisons. I assume that at the business level, we could only
> sketch white UCs at best, if at all and rather stay ins peculative psychological driven objectives
> towards a single goal, having them close. So here we need to bring in external materals teaching
> how to sell and close.

On **DEC-5** (packages as a shop shelf):

> yes I already addressed this above, we must have a services we sell inventory and a set of packages
> we sell. so that the client can easely buy from us, like from a shop, pick from a shelf and know
> what is in the box and how much it costs. this is a TODO now, and must be extended in the future,
> prepare the placeholders, and knows sales services and products so far ...

On **DEC-6** (the Partner label):

> yes partner is only a recurring client, better to even drop this label, not really helpful here.

On the **"do not design the commercial mechanics" rabbit-hole**:

> despite this being a risk you could give it a short, limited attempt only, but mark it as a point
> to work on further and extend.

On the **"do not renumber the phases" rabbit-hole**:

> feel free to do so, if there is a more appropriate way of marking it

On the **No-gos**:

> only mark places on what is missing and where new things are needed (n ew documents or skills)

## 7. What the round-2 addendum instructed for this epic (paraphrased, not verbatim)

The addendum (a working note, not archived as a source) directed, for this epic specifically: fix the
P1 duration; add the safeguards mechanism as a short bounded addition and mark fuller commercial
mechanics as future work; fold the internal-posture material into the coach's rewrite, with a new
short reference file justified if it does not fit; name the four missing sales/presale skills as
known gaps (confirming `executive-communication` already covers pitch material and is *not* a gap);
sharpen DEC-4 with the sales-strategy-vs-use-case distinction; add a services-and-packages skeleton
as a deliberate small appetite increase; drop or shorten the "Partner" label; and leave room for the
Shipper's contract-conformance DoD, which `define-delivery-release-lifecycle` relocates into
`docs/engagement/`.
