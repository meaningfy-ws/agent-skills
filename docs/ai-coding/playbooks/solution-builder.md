# Solution Builder: playbook

> Role definition, mandate, and RACI cells:
> [`roles-and-raci.md`](../../roles-and-raci.md#solution-builder).

## Your stages

- **Project/repo setup**: you are accountable (`A/R`). See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).
- **Epic build (BDD/TDD)**: you are accountable (`A/R`) for the build loop: BDD features, TDD
  implementation, review. See
  [`build-lifecycle.md`](../build-lifecycle.md#epic-tier-one-epic-at-a-time--the-sdlc-loop).
- **Review**: you do the work (`R`); the Solution Shipper signs off (`A`). See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).
- **Release & deploy**: you do the work (`R`); the Solution Shipper is accountable (`A`). See
  [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).

You consult (`C`) during Epic shaping (documented collaboration with the Work Shaper, not a
role conflation). See [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).

## Skills you invoke

- [`cosmic-python`](../../../skills/cosmic-python/SKILL.md): layered architecture + TDD.
- [`bdd-gherkin`](../../../skills/bdd-gherkin/SKILL.md): `.feature` scenarios and test data.
- [`linkml-engineering`](../../../skills/linkml-engineering/SKILL.md): LinkML schema authoring
  and generation, where the plane is a model build.

Full list: [`roles-and-raci.md`](../../roles-and-raci.md#solution-builder).

## Handed to you by

- The **Work Shaper** hands you the shaped, clarity-gated Epic (PLAN) to build. See
  [`build-lifecycle.md`](../build-lifecycle.md#epic-tier-one-epic-at-a-time--the-sdlc-loop).
- The **Solution Architect** hands you MDLC-lite modelling work under their accountability (`A`).
  See [`roles-and-raci.md`](../../roles-and-raci.md#raci-matrix).

## You hand off to

- Discovered work during execution is reported back to the **Work Shaper**, who maps it into
  stories/tasks. See
  [`roles-and-raci.md`](../../roles-and-raci.md#solution-builder).
- The built increment hands off to the **Solution Shipper** at the Delivery & Release gate: your
  DoD closes on the SDLC plane, the Shipper's closes on the commercial plane, in parallel. See
  [`dod-quality-gates.md`](../dod-quality-gates.md#delivery--release).

## Your done

The Epic's DoD: built right (tests green, coverage met, architecture check clean, review passed)
and right thing built (acceptance criteria and `.feature` scenarios demonstrably pass). See
[`dod-quality-gates.md`](../dod-quality-gates.md#delivery--release).
