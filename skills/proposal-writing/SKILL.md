---
name: proposal-writing
description: Produce the proposal + Statement of Work (SoW) that frames the paid Decision Phase (P1) offer — with an explicit in/out scope boundary, priced as a fixed frame. This is the ENTRY skill of the consulting front-of-funnel: it qualifies the need, frames the Decision Phase offer, prices it (delegating the numbers to `estimation`), and writes the proposal + SoW. It OWNS proposal/SoW production and the scope-boundary discipline; it DELEGATES pricing/effort to `estimation`, executive framing to `executive-communication`, and the P1 deliverable definition to `decision-package`. Triggers — "write a proposal", "draft the SoW / Statement of Work", "scope boundary for this engagement", "fixed-cost proposal", "frame the Decision Phase offer". Not for producing the Decision Package itself (that is `decision-package`), not for free P0 orientation (that is `semantic-consulting-coach`).
license: Apache 2.0
metadata:
  category: consulting
---

# Proposal Writing

> **Provisional pending the first-engagement gate.** This wiring is the floor, not the finished standard;
> refine it after the first real paid engagement is sold and delivered.

## Overview

The **proposal + SoW** is the commercial artefact that converts a qualified prospect into a signed
**P1 Decision Phase** engagement. It frames the offer, draws an explicit **scope boundary (in/out)**,
and prices the engagement as a **fixed frame** — a bounded commitment the prospect can sign without
open-ended risk on either side.

This is the **entry skill** of the consulting front-of-funnel: the common path runs through here. It
does the qualify → frame → price → write loop, calling `estimation` by reference for the numbers (so
the flow is one path, but `estimation` stays independently triggerable for any estimate that does not
need a full proposal wrapper).

It composes by reference and restates nothing:
- the offer being framed — the P1 Decision Phase — is defined by
  [`decision-package`](../decision-package/SKILL.md) (what P1 *delivers*) and the engagement model in
  [`semantic-consulting-coach`](../semantic-consulting-coach/references/engagement-model.md) (the
  free→paid boundary and the fixed-frame intent);
- the pricing and effort numbers come from [`estimation`](../estimation/SKILL.md);
- the structure and persuasion come from
  [`executive-communication`](../executive-communication/SKILL.md) — a proposal is
  an executive artefact (SCQA + a 3-point pyramid; trade-offs and scope boundaries explicit).

## Flow (R2)

**Inputs:** P0 orientation notes / prospect context (the qualification signals the coach surfaced).
**Output:** a proposal + SoW with an explicit in/out scope boundary, priced as a fixed frame.

1. **Qualify the need.** Confirm the prospect has crossed the free→paid boundary — they are asking
   *"what do we do first, and why?"*, not *"is this relevant?"*. If they have not, this is still P0
   orientation; do **not** write a paid proposal yet (see the boundary discipline in
   [`engagement-model.md`](../semantic-consulting-coach/references/engagement-model.md)). Capture the
   problem, the deciding persona, the measurable outcome, and the constraints.
2. **Frame the Decision Phase offer.** State what P1 delivers — the Decision Package (recommendation,
   in/out scope, pilot→scale roadmap, buy/build/defer, ready-to-contract execution brief; see
   [`decision-package`](../decision-package/SKILL.md)). Frame it answer-first as the offer that makes
   committing safe, not as open-ended discovery.
3. **Price it as a fixed frame** — via [`estimation`](../estimation/SKILL.md). Hand `estimation` the
   work breakdown the offer implies; take back the effort range, the contingency, and the
   assumptions/exclusions. The SoW scope boundary and the estimate's exclusions are the **same list**
   — keep them in lock-step (see the [scope-boundary checklist](references/scope-boundary-checklist.md)).
4. **Write the proposal + SoW.** Use the templates in
   [`references/proposal-template.md`](references/proposal-template.md) and
   [`references/sow-template.md`](references/sow-template.md). Write the proposal in the executive
   voice ([`executive-communication`](../executive-communication/SKILL.md));
   write the SoW as the contractual companion that pins scope, deliverables, price, and exclusions.

## The scope boundary (in/out) — load-bearing

The **explicit in/out scope boundary** is the discipline this skill owns. The "out" list is not
filler: it protects the boundary with the build tier (P2 Execution is *always a separate engagement*)
and pre-empts scope creep on a fixed-frame price. Two rules:

- **The SoW "out of scope" list = the estimate's exclusions.** They are one list in two documents.
  If `estimation` excluded it from the number, the SoW must exclude it from the commitment.
- **Name the clean handover.** State that P2 Execution is separately scoped and priced — the proposal
  earns the right to say *"from here, we can execute, or you can take this and execute with someone
  else."*

The full discipline — what must appear in/out, the boundary checks, the handover clause — is in
[`references/scope-boundary-checklist.md`](references/scope-boundary-checklist.md).

## Pricing as a fixed frame

A **fixed frame** is a bounded commitment, not an open day-rate. The price comes from `estimation`
(PERT-weighted effort + contingency); this skill wraps it with the **stop/extend mechanics** so the
frame stays honest: if agreed outcomes cannot be reached for reasons outside our control, the SoW
already names the option to reduce scope, take a short extension, or stop cleanly with partial
delivery — never silent overwork (the boundary safeguard from `engagement-model.md`).

## Boundary & Related Skills

**This skill OWNS:** producing the **proposal + SoW**, and the **scope-boundary (in/out)
discipline** — including the fixed-frame framing and the stop/extend mechanics that keep the frame
honest.

**This skill DELEGATES:**
- Pricing / effort / contingency numbers → [`estimation`](../estimation/SKILL.md) (the entry flow
  invokes it; it also stands alone).
- Executive framing and voice (SCQA, Minto pyramid, answer-first) →
  [`executive-communication`](../executive-communication/SKILL.md).
- The P1 deliverable definition (what the Decision Phase actually produces) →
  [`decision-package`](../decision-package/SKILL.md).
- Coaching whether/how to run P1 and holding the free→paid boundary →
  [`semantic-consulting-coach`](../semantic-consulting-coach/SKILL.md).

**Related:** `estimation`, `decision-package`, `executive-communication`, `semantic-consulting-coach`, `writing-antipatterns` (Contract/specification genre failure modes for the SoW half of this skill's output).

## Tone & style

British English. The proposal is an executive artefact: answer-first, concise, every claim
load-bearing; scope boundaries and trade-offs explicit, never hedged. The SoW is its contractual
companion: precise, enumerated, no marketing prose. Write the proposal in the engagement's executive
voice (see `executive-communication`), not consultancy-bland.
