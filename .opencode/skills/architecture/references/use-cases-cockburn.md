# Use Case Specifications — Cockburn White & Blue

How to write the use case catalogue for a system architecture, following Alistair Cockburn's
*Writing Effective Use Cases*. Conventions generalized from a real, reviewed catalogue (the
Entity Resolution System, ERSys — an engine-authoritative, async, idempotent resolution service).
Use with the two copy-paste templates: `use-case-template-white.adoc`, `use-case-template-blue.adoc`.

## What the catalogue is (and is not)

The use case catalogue is the **authoritative specification of externally observable behaviour**:
what the system guarantees to its actors, under which conditions, with which explicit limitations.

It is a **behavioural contract** — **not** an API specification, data schema, or implementation
guide. Those live in the contract and model artefacts this skill already owns (OpenAPI/AsyncAPI/
LinkML, ADRs, C4 diagrams). The catalogue cross-references them; it never inlines schemas or code.

Place it as an annexe of the architecture document (ERSys: *Annexe B*), cross-linked with the
glossary and the ADRs.

## Two altitude levels only: White and Blue

Cockburn colours use cases by *altitude* — how far the goal sits from the sea. The full ladder has
five levels (very-high summary / summary / user-goal / subfunction / too-low). **Deliberately use
only two**, because a two-level catalogue stays reviewable and each level has one clear audience:

| | Cockburn label | States | Audience | Specified at |
|---|---|---|---|---|
| **White** | Summary (cloud, above the sea) | The **contract**: value + guarantees that always hold, incl. degraded conditions; system boundary | Reviewers, stakeholders | the C4 **L1** boundary (externally observable value/services) |
| **Blue** | User-goal (sea level, the waterline) | The **realisation**: how the value is fulfilled through interactions between internal responsibilities | Implementers, integrators, reviewers | the C4 **L2–L3** responsibility boundaries |

> **Honesty note — this is a black-box/white-box split, not pure Cockburn altitude.** Cockburn has two
> *independent* axes: *altitude* (summary / user-goal / subfunction) and *transparency* (black-box vs
> white-box). In canonical Cockburn a summary use case *aggregates several* user-goal use cases. This
> convention does **not** do that: White and Blue describe the **same goal at the same altitude** —
> White as the black-box contract, Blue as its white-box realisation. We reuse Cockburn's colours to
> label a transparency split because it reads cleanly, but a reader coming from the book should expect
> "blue = realisation of a White", not "blue = a standalone user-goal that a summary rolls up". If a
> catalogue genuinely needs *altitude* aggregation (one summary over many user-goals), that is a
> different, additional structure — add it explicitly rather than overloading White/Blue.

Both levels stay **technology-agnostic**. Blue exposes responsibility boundaries, idempotency
rules, and failure paths; it does not name frameworks, protocols, or wire formats. The C4 columns say
*specified at* a boundary, not *is* that boundary: use cases are behavioural, C4 levels are structural;
a White use case is a contract stated **over** the L1 boundary, not an L1 element.

Skip Cockburn's subfunction (fish) and very-high-summary (kite) levels unless a catalogue genuinely
needs them — reach for them only when a shared sub-goal is referenced by three or more use cases.

## White states the contract; Blue realises it (the DRY discipline)

This is the single most important convention and the reason the split earns its keep:

- A **White** use case is self-contained: it states the full contract.
- A **Blue** use case **refines exactly one White** parent. It opens with a cross-reference to that
  parent, names the shared elements (guarantees, scenarios, business rules), and then states **only
  the realisation deltas**. It does **not** restate the shared contract.
- One White use case may fan out to several Blue use cases (one per realisation surface — e.g. a
  synchronous API path, an asynchronous integration path, a bulk-sync path).

If a Blue page repeats the White guarantees verbatim, the split has failed — collapse or re-cut it.

## Numbering and anchors

- White: `UC-W<n>` — anchor `[#uc-w<n>]` (e.g. `UC-W1`, `[#uc-w1]`).
- Blue: `UC-B<n>.<m>` where `<n>` is the parent White — anchor `[#uc-b<n>-<m>]`
  (e.g. `UC-B1.1` refines `UC-W1`, anchor `[#uc-b1-1]`).
- The doctitle (`=` line) is the use case name and must match the catalogue index link **exactly**.
- The `[#…]` anchor lets the glossary, ADRs, and architecture pages deep-link individual use cases.

## The canonical skeleton (one skeleton for every page)

Every page uses the **same section names, order, and heading levels**: one `=` doctitle, then `==`
sections. A section appears **only when it has content**, but when present it always uses this name
and this position. This uniformity is what makes the catalogue reviewable at a glance.

Metadata block (bold inline lines, right after the doctitle):

- **Use Case Level:** White (Summary) *or* Blue (User-goal).
- **Primary Actor:** the actor pursuing the goal (a glossary preferred term). The system itself may
  legitimately be the primary actor where one large use case is split into parts.
- **Supporting Actors:** *Blue only* — the internal components participating in the realisation, each
  with a one-line role. **White use cases have no supporting actors.** This is how Blue makes
  responsibility boundaries explicit while White stays a black-box contract.
- **Scope:** the system or boundary under design (Blue narrows it to the realising surface).

Section order (fixed):

1. Stakeholders and Interests — parties affected and what each requires
2. Brief Description — goal, value, narrative; system-of-interest scoping
3. Preconditions — what must hold before it begins
4. Trigger — the initiating event
5. Success Guarantee (Postconditions) — what is guaranteed on success
6. Minimal Guarantees (On Failure) — what holds even when it does not complete
7. Main Success Scenario — the primary numbered flow
8. Alternate Scenarios — named alternative flows
9. Extensions — step-keyed exception/variation handling (`1a.`, `2b.`, …)
10. Out of Scope — explicitly excluded behaviour
11. Special Requirements — cross-cutting constraints (idempotency, authority, lineage)
12. Notes and Business Rules — standing rules qualifying interpretation
13. Technology and Data Variations — deployment/format variation points
14. Frequency of Occurrence — expected invocation rate (feeds NFRs)

## Conventions that travel to any system

- **Actor names bind to the glossary.** The glossary is the single source of truth for terminology;
  use its preferred terms consistently. Any apparent conflict resolves in favour of the glossary.
- **Guarantees, not steps, carry the contract.** Success/Minimal guarantees are observable outcomes
  ("returns a canonical identifier within the budget"), independent of the flow that produced them.
- **Name the degraded-mode guarantee explicitly.** The strongest use cases state what still holds
  when the happy path cannot complete (ERSys: a deterministic provisional identifier on engine
  timeout). Minimal Guarantees is where a system earns trust.
- **Extensions are step-keyed deltas**, not prose — `<step><letter>. <condition> — <handling>`.
- **Idempotency, authority, and lineage** are recurring Special Requirements for any integration or
  data system; state them once in White and only realise them in Blue.
- **Reading guide up front.** Tell stakeholders to read White; tell implementers/reviewers to read
  the Blue refinements together with the relevant ADRs.

## The use case catalogue is the source for BDD (no double-specification)

A use case's numbered flows and a Gherkin `.feature` file describe the **same behaviour** — the UC at
architecture time, Gherkin at implementation time. To stop them drifting, treat the catalogue as the
**single source of behavioural truth** and Gherkin as its **executable projection**, not a second,
independent specification. The `bdd-gherkin` skill authors the `.feature` files *from* the catalogue.

Derivation mapping (UC section → Gherkin construct):

| Use case element | Projects to Gherkin |
|---|---|
| Main Success Scenario | The happy-path `Scenario` (one per UC) |
| Alternate Scenarios | One `Scenario` each (still-successful variants) |
| Extensions (`1a.`, `2b.`, …) | One `Scenario` each (exception/variation paths), keyed back to the step |
| Preconditions | `Given` steps / `Background` |
| Trigger | `When` step |
| Success Guarantee (postconditions) | `Then` steps |
| Minimal Guarantees (on failure) | `Then` steps of the failure/degraded scenarios |
| Technology and Data Variations | `Scenario Outline` + `Examples:` axes |

Rules that keep the two in sync:

- **Every UC Main Success Scenario, Alternate Scenario, and Extension has at least one Gherkin
  scenario.** That is the coverage floor.
- **Gherkin invents no behaviour absent from a use case.** If a scenario has no UC (or, where no
  catalogue exists, no EPIC acceptance criterion) to trace back to, that is a gap in the catalogue —
  fix the UC first, then project. New behaviour enters through the UC, never through a `.feature` file.
- **Gherkin *adds* data, not behaviour.** The extra exercise Gherkin performs over a UC is
  *enumeration*: concrete `Examples:` rows, boundary values, and edge-case data that the UC states
  abstractly ("supported formats", "within the budget"). This is expected and encouraged — it is
  fabricating test data, not specifying new guarantees.
- **Prefer Blue over White as the projection source** where a Blue refinement exists: Blue names the
  concrete error codes and responsibility boundaries that make good `Then` assertions. Fall back to
  White where no Blue refinement has been written.
- **Trace explicitly.** Tag or name each feature/scenario with its UC id (`UC-W1`, `UC-B1.1`) so
  coverage and drift are auditable. `bdd-gherkin`'s quality checklist enforces the coverage floor.

## Reusable workflow to build a catalogue

1. Extract goals from the business drivers (Step 0 of the architecture workflow). Each user-visible
   goal is a candidate **White** use case (typically 3–7 for a service).
2. Write each **White** use case: contract, guarantees (success + minimal/degraded), boundary.
3. For each White, identify the distinct realisation surfaces (sync API, async integration, bulk
   sync, UI-driven action…). Each becomes one **Blue** refinement.
4. Write each **Blue** use case as deltas over its White parent, naming supporting actors (internal
   components) and cross-referencing the contract artefacts (OpenAPI/AsyncAPI/LinkML) and ADRs.
5. Keep the index table (`index.adoc`) in lockstep: every page has a row; link text matches the
   doctitle; the one-line purpose distinguishes White (value) from Blue (realisation).
