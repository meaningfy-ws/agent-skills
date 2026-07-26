---
name: decision-package
description: Produce the Decision Package — the paid keystone deliverable of a semantic/data consulting engagement's P1 Decision Phase. Use to write the recommendation, the in/out scope, the sequenced (pilot → scale) roadmap, the buy/build/defer decisions, and the ready-to-contract execution brief that hands off to the build/architecture tier. The unit of value is decision-readiness; the artefact sits ABOVE architecture (it justifies and scopes the build before a repo exists). Triggers — "produce a decision package", "write the recommendation / scope / roadmap / buy-build-defer", "decision-readiness deliverable", "execution brief for the build", "scope this engagement", "Semantic Readiness & Direction / Decision Foundation deliverable". This skill PRODUCES the artefact; it does NOT coach the engagement design or hold the free→paid line (that is semantic-consulting-coach — "produce" vs "coach"). Not for free P0 orientation, not for delivery artefacts (an ontology, a mapping), not for code architecture.
license: Apache 2.0
metadata:
  category: consulting
---

# Decision Package

> **Provisional pending the first-engagement gate.** The consulting depth here refines after the first real
> paid P1 engagement; treat this wiring as the floor, not the finished standard.

## Overview

The **Decision Package** is the paid keystone deliverable of Discovery & Onboarding's **Deep-tier
Decision Phase**. Its unit of value is **decision-readiness**: the state in which the client knows
*what to do next, why, what success looks like, and what comes later* — the moment uncertainty
becomes safe to commit. This skill **PRODUCES** that artefact.

It sits deliberately **above architecture**: it justifies and scopes the build *before a repo
exists*. Architecture, the conceptual model, and the EPICs all descend from it — the Decision
Package is the consulting-tier **root of the golden thread**.

**Provenance.** The coach (`semantic-consulting-coach`) shapes *whether and how* to run the Deep
tier and holds the **free → paid boundary**; the design intent of the Decision Phase lives in its
[`engagement-model.md`](../semantic-consulting-coach/references/engagement-model.md). This skill picks
up *after* that line is crossed and the client has bought the Deep tier: it **builds the
deliverable**. Keep the boundary crisp — **produce** here, **coach** there.

## The deliverable: five parts (R1)

The Decision Package is an **executive artefact** framed around decision-readiness. Frame and write
it with the [`executive-communication`](../executive-communication/SKILL.md) skill
(Governing Thought → SCQA → Minto pyramid, answer-first); this skill supplies the *what*, that skill
supplies the *how it reads*. Its five required parts:

1. **Recommendation** — the first initiative to commit to, stated answer-first as a Governing
   Thought, with the reasoning that makes it safe to commit.
2. **Scope** — explicitly **in** and explicitly **out**. The "out" list is load-bearing: it protects
   the boundary with the build tier (P2) and prevents scope creep.
3. **Sequenced roadmap** — **pilot → scale**: what to do first, then next, in deliberate order.
4. **Buy / build / defer decisions** — for each capability, a named decision with rationale.
5. **Ready-to-contract execution brief** — the hand-off to the build tier / architecture: enough for
   P2 (or another implementer) to scope and contract cleanly.

It earns the right to say, calmly: *"From here, we can execute, or you can take this and execute with
someone else."* The full fillable template is in
[`references/decision-package-template.md`](references/decision-package-template.md).

## The Deep-tier discovery flow (R3, R5)

The package is the output of a structured flow, not a maturity assessment or open-ended discovery.
This is **one coherent discovery framework** — the still-relevant items of the internal
product-blueprint checklist are **absorbed into it** where they serve decision-readiness, and the
pure product-delivery mechanics are dropped (the reconciliation is in
[`references/blueprint-absorbed.md`](references/blueprint-absorbed.md)).

1. **Structured discovery** — the problem, the deciding persona, the measurable outcome, the
   competitive/strategic "why now". *(Absorbs blueprint Q1 problem/persona/outcome, Q2 success
   metrics, Q3 why-we-win — reframed as decision inputs, not an MVP brief.)*
2. **Landscape / data reading** — the data estate, governance maturity, legacy constraints, existing
   assets and obligations.
3. **Gap analysis** — current state vs. the strategic ambition: where the gaps are, which ones
   block the first safe step, which can wait.
4. **Option framing** — the candidate first initiatives, each with its trade-off (the "big
   decision" framing of blueprint Q4, kept as *options to decide between*, not a pre-made choice).
5. **Sequencing** — order the options into a pilot → scale roadmap; name what is explicitly **not**
   in the first step (the discipline of blueprint Q6/Q7, recast as roadmap + out-of-scope).
6. **Buy / build / defer** — for each needed capability, decide and justify.
7. **Execution brief** — assemble the ready-to-contract hand-off to the build tier.

Detail, including gap-analysis and buy/build/defer guidance, is in
[`references/discovery-flow.md`](references/discovery-flow.md).

### First-cut conceptual model (R4)

A **first-cut conceptual model** of the domain often surfaces during discovery (a sketch of the key
entities and relationships, to ground scope and options). When it does, produce that fragment with
the [`conceptual-modelling`](../conceptual-modelling/SKILL.md) skill — but keep it a
*sketch in service of the decision*. Do **not** pull modelling depth (LinkML authoring, generation,
ontology engineering) into the Decision Package; the real model is built later, in the build tier.

## The free → paid boundary (R6)

Only **presale** is free — everything else, including the Deep tier, is paid. See
[`docs/ai-sales/engagement-lifecycle.md`](../../docs/ai-sales/engagement-lifecycle.md) for the
full commercial model; this skill operates **only inside the paid Deep tier**. Do not blur Decision Package production into free coaching: if the
work being asked for is still presale, it has not crossed the boundary, and this skill should not be
producing a paid artefact yet — that is the coach's territory (`semantic-consulting-coach`), and the
coach protects the line.

## Golden-thread root: where the package lives (R7)

The durable Decision Package lands as its **own spine artefact type**, at:

```
openspec/decisions/<id>.md
```

It is **not** forced into `openspec/specs/` — those are RFC-2119 behaviour contracts, and a Decision
Package is an **executive narrative**, a different genre. It gets its own home so the genres do not
collide.

It is the **consulting-tier root of the golden thread** (see
[`../../spine/golden-thread.md`](../../spine/golden-thread.md)). The first `specs/` /
architecture entries **cite it as their parent**:

```
decision-package (openspec/decisions/<id>.md)
  → requirement / architecture
    → conceptual model
      → EPIC / change
        → task → test → commit
```

Make this convention explicit when producing the package: mint a human-readable ID, and ensure the
downstream architecture/requirement artefacts cite it as parent.

## Naming (R8)

The default name is **"Decision Package"** — for both this skill and the client-facing deliverable.
An engagement **MAY relabel the *client-facing* artefact** without renaming the skill, e.g.
*Semantic Readiness & Direction*, *Decision Foundation*, *Scope Definition*. This is an allowed
per-engagement override: the skill name and the five-part structure stay fixed; the cover label
flexes to the engagement.

## Boundary & Related Skills

**This skill OWNS:** producing the Decision Package (the five R1 parts) and running the
**Deep-tier discovery flow** that yields it (structured discovery → landscape reading → gap analysis → option
framing → sequencing → buy/build/defer → execution brief), including the absorbed product-blueprint
items recast for decision-readiness.

**This skill DELEGATES:**
- Coaching the engagement design and **holding the free → paid boundary** →
  [`../semantic-consulting-coach/SKILL.md`](../semantic-consulting-coach/SKILL.md). The coach decides
  *whether/how* to run the Deep tier; this skill builds its deliverable.
- Executive framing and voice (Governing Thought, SCQA, Minto) →
  [`../executive-communication/SKILL.md`](../executive-communication/SKILL.md).
- The **first-cut conceptual model** fragment →
  [`../conceptual-modelling/SKILL.md`](../conceptual-modelling/SKILL.md)
  (sketch only; no modelling depth here).
- Proposal / Statement of Work for the engagement → `proposal-writing` (EPIC-08, future).
- System/solution architecture that descends from the package →
  [`../architecture/SKILL.md`](../architecture/SKILL.md).

**Related:** `semantic-consulting-coach`, `executive-communication`, `conceptual-modelling`,
`architecture`, `writing-antipatterns` (Decision genre failure modes).

## Tone & style

British English. The Decision Package is an executive artefact: answer-first, concise, every claim
load-bearing. Recommendation before proof; scope boundaries and trade-offs explicit; buy/build/defer
decisions named, not hedged. Write it in the engagement's executive voice (see
`executive-communication`), not consultancy-bland.
