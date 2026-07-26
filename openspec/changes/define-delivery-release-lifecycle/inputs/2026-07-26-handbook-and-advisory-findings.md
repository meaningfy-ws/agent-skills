# Seed — Employee Handbook + round-2 human directives (excerpt for `define-delivery-release-lifecycle`)

**Status: SECONDARY input. Never groomed, never deleted.** The shaped EPIC
([`../proposal.md`](../proposal.md)) supersedes this as the primary truth but does not replace it.
Companion to [`2026-07-25-brainstorm-seed.md`](2026-07-25-brainstorm-seed.md) (round 1).

**Canonical source location — not duplicated here.** The full source documents live at
[`openspec/changes/define-lifecycle-playbooks/inputs/`](../../define-lifecycle-playbooks/inputs/):

| Document | Path |
|---|---|
| `Employee Handbook - Second Edition (2026) (1).pdf` (103 pp.) | `../../define-lifecycle-playbooks/inputs/Employee Handbook - Second Edition (2026) (1).pdf` |
| `decission-phase-advisory.md` | `../../define-lifecycle-playbooks/inputs/decission-phase-advisory.md` |
| `presales-material.md` | `../../define-lifecycle-playbooks/inputs/presales-material.md` |

This file archives **only the excerpt that feeds this change** — the handbook's shipping content and
the human's round-2 directives on the Shipper's DoD. The advisory and presales documents are P0/P1
commercial material owned by `define-blc-engagement-model`; they are cited here for completeness and
deliberately not excerpted.

---

## 1. Human directives, round 2 (verbatim)

On the Shipper's DoD substance:

> "it is pretty clear that by this point we want to have a dod for the shipper as well? no? and have
> the shipper ensure that what is built is what is promised in some written documents exchanged with
> the client (a request for an offer, the offer, the contract, the meeting minutes and documented
> exchanges, any other relevant documents describing needs/desired and our agreement to fulfill those,
> and how)"

On where it belongs — this reopened the proposal's own No-go against touching `docs/engagement/`:

> "So this shipping/business delivery is clearly a document part of the commercial bulk of the
> documentation not SDLC"

> "unless you decide to put the second dod there"

On marking gaps rather than presenting the bet as settled:

> "we want however to mark places that need further clarification and strengthening"

Standing ground rule for the whole round:

> "assume the provided materials are outdated, but of good quality and need to be carried forward to a
> modern way of working where people govern, and steer and check lightly the heavy work of LLM agents"

## 2. Employee Handbook — "Project shipping" (p. 53–54 / 103)

The operational content behind the abstract Shipper's DoD. Load-bearing lines, verbatim:

> **Introduction.** "The Shipping Phase marks the culmination of our team's efforts, where the project
> transitions from creation to delivery. This phase is critical for ensuring that all deliverables meet
> client expectations, contractual agreements, and the highest quality standards."

> **The Shipping Process — 1. Contractual Validation:**
> "Review the deliverables against the contractual agreement."
> "Address and rectify any misalignments before proceeding to the client."

Subsequent steps of the same process, for context (2) Documentation and Preparation, (3) Delivery
Scheduling, (4) Delivery Execution, (5) Client Demonstration, (6) Final Approval and Handover — these
are **delivery logistics and client-facing ceremony**, not a conformance check, and are the material
behind this change's "no PM process" rabbit-hole and its Known-gaps note.

> **Key Values of the Shipping Phase — Accountability:** "Deliverables are thoroughly checked against
> contract specifications, leaving no room for errors."

## 3. Employee Handbook — "Delivery Manager - the Shipper" (p. 68 / 103)

> "The Delivery Manager is responsible for overseeing the final phase of the project, ensuring the
> timely and accurate delivery of project outputs to the client. This role involves ensuring that all
> deliverables meet the highest quality standards and are in complete accordance with the contractual
> agreements."

Key responsibilities include: "Conducting comprehensive inspections of the deliverables to guarantee
quality and adherence to contract specifications" and "Facilitating a seamless handover process,
achieving full client satisfaction and contractual compliance."

Also on the same page, **Project Owner — the Work Shaper**: "Developing the Work Breakdown Structure
based on the request for offer, the offer and adjacent meeting notes with the client." This is the
same document trail the human names for the Shipper's DoD, entering the lifecycle at the other end —
the shape is drawn from those documents, and the delivery is checked back against them. The Work
Shaper role itself is owned by `define-roles-and-raci` and `define-lifecycle-playbooks`, not here.

## 4. How this seed is used (and what it is not used for)

- **Used:** to sharpen the Shipper's DoD from an abstract "matches the contract" to the concrete
  document trail (RfO, offer, contract, meeting minutes, documented exchanges, any other agreement
  documents), and to justify relocating that DoD into `docs/engagement/` (proposal DEC-11, DEC-12).
- **Adapted, not copied:** the handbook's shipping process is written for a human-only team with a
  dedicated Delivery Manager. Carried forward as **light human sign-off with agent-assisted document
  review**, per the ground rule above.
- **Not used here:** the handbook's Redelivery Policy (p. 55–56) and "Managing Out-of-Contract
  Improvements" (p. 52) are named as Known gaps by `define-meaningfy-lifecycle`; the role roster
  (p. 65–70) belongs to `define-roles-and-raci`; the rituals and formalities (p. 57–61) are
  PM-process material this change explicitly does not build.
