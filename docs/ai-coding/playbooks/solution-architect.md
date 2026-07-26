# Solution Architect: playbook

> Role definition, mandate, and RACI cells:
> [`roles-and-raci.md`](../../roles-and-raci.md#solution-architect).

## Your stages

- **ADLC (architecture & system design)**: you are accountable (`A/R`) for ADRs, C4 views, Use-Case
  White/Blue. Front-loaded and kept stable before Epics are carved. See
  [`build-lifecycle.md`](../build-lifecycle.md#project-tier-upfront-human-led).
- **Requirements & UC, deep depth (White + Blue)**: you are accountable (`A/R`), whether handed
  off from a completed Deep-tier engagement or elicited fresh on direct-to-build. See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).
- **MDLC-lite**: you are accountable (`A`) for the domain/technical modelling within a software
  contract; the Solution Builder does the work (`R`). See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).

You consult (`C`) during Epic shaping (documented collaboration with the Work Shaper, not a
role conflation). See [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).

## Skills you invoke

- [`architecture`](../../../skills/architecture/SKILL.md): ADRs, C4, contracts, UC White/Blue.
- [`conceptual-modelling`](../../../skills/conceptual-modelling/SKILL.md): the living domain
  model and its source decision.

Full list: [`roles-and-raci.md`](../../roles-and-raci.md#solution-architect).

## Handed to you by

- The **Technical Consultant**, via the Decision Package's execution brief, or direct-to-build's
  own elicitation, hands you the decided scope for deep requirements/architecture work. See
  [`../../ai-sales/engagement-lifecycle.md`](../../ai-sales/engagement-lifecycle.md#the-outcome-semantic-layer-adoption).

## You hand off to

- The stabilised architecture is sliced into a backlog of shaped Epics, handed to the **Work
  Shaper** for Epic shaping (where you then consult, `C`). See
  [`build-lifecycle.md`](../build-lifecycle.md#project-tier-upfront-human-led).
- MDLC-lite modelling work is handed to the **Solution Builder** for execution (`R`), under your
  accountability (`A`). See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).

## Your done

Architecture is done when it has stabilised (kept stable *before* Epics are carved), per this
build plane's deliberate divergence from canonical Shape Up. See
[`build-lifecycle.md`](../build-lifecycle.md#3-labelled-divergence-from-canonical-shape-up).
