---
name: bdd-gherkin
description: Write BDD Gherkin feature files and fabricate test data from a specification. Use to project a use case catalogue (Cockburn White/Blue) or turn acceptance criteria or an EPIC into business-language `.feature` scenarios — Scenario Outline with Examples, explicit edge cases, no implementation detail, traced back to use cases. Trigger on "write Gherkin", "write feature files", "BDD scenarios for this acceptance criterion", "derive scenarios from use cases", "fabricate test data".
license: Apache 2.0
metadata:
  category: ai-coding
---

# BDD / Gherkin Authoring

## Overview

Translate a specification into precise, business-language Gherkin features that define
**what** the system should do in observable, testable terms — not **how**. This is a
**design-phase** activity: the `.feature` files are a **PLAN artifact** authored alongside the
PLAN so `clarity-gate` can score scenario coverage. **Step definitions and production code are NOT
authored here** — they belong to the implement phase (`superpowers:test-driven-development`).
Scenario *thinking* (what to prove, which edge cases) is elicited in `epic-planning`'s interview.

**Where a use case catalogue exists, it is the source, not the EPIC directly.** When the architecture
defines White/Blue use cases (Cockburn — see the `architecture` skill), Gherkin is the **executable
projection** of those use cases, not an independent second spec. Derive scenarios from a UC's Main
Success Scenario, Alternate Scenarios, and Extensions (mapping table in the `architecture` skill's
`use-cases-cockburn.md`); prefer the Blue refinement, which names concrete error codes and boundaries.
Gherkin **adds data, not behaviour**: concrete `Examples:`, boundary values, and edge-case rows that
the UC states abstractly. It **invents no behaviour absent from a use case** — a scenario with nothing
to trace back to is a catalogue gap; fix the UC first, then project. Where no catalogue exists, fall
back to the EPIC acceptance criteria and test-case/error tables.

## Quick Start

1. Read the source spec/EPIC; confirm it is ready (clarity-gate passed) before writing.
2. Write `.feature` files under `tests/features/` (or the project's path), named
   `<capability>.feature`, one file per coherent business capability.
3. Write in **business language** — no SQL, API paths, or class names; only business concepts.
4. Prefer **`Scenario Outline` + `Examples:`** for data-driven coverage:

```gherkin
Scenario Outline: <description>
  Given <precondition>
  When <action with parameter>
  Then <expected outcome>

  Examples:
    | parameter | expected |
    | value1    | result1  |
    | value2    | result2  |
```

5. Cover edge cases **explicitly**, sourced from the spec's test-case table and error matrix.
6. Fabricate sample/test data only where real examples are insufficient; place it in the
   project's fixtures location.

## Quality checks (before finishing)

- [ ] Every task in the breakdown has feature coverage.
- [ ] **Where a UC catalogue exists:** every UC Main Success Scenario, Alternate Scenario, and
      Extension has ≥1 scenario, and every scenario traces back to a UC id (`UC-W1`, `UC-B1.1`) — no
      untraceable, invented behaviour.
- [ ] Every test-case-spec row and every error-matrix row has a scenario.
- [ ] `Scenario Outline` used wherever multiple data variations apply.
- [ ] No implementation details leak in (no SQL / API paths / class names).
- [ ] Files are syntactically valid Gherkin.

## Boundary & Related Skills

**Owns:** feature files + test data. **Does NOT** write step definitions or production code
(that is the implementer's job, following `cosmic-python` + `superpowers:test-driven-development`),
and does NOT plan (`epic-planning`) or score specs (`clarity-gate`).
**Related:** `architecture` (the White/Blue use case catalogue Gherkin projects from), `epic-planning`,
`clarity-gate`, `spec-stewardship`, `cosmic-python`.
