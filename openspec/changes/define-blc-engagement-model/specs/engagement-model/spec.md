## ADDED Requirements

### Requirement: Presale is the only free stage
The engagement model SHALL treat presale as the sole free stage. No activity that produces a
deliverable — an advisory session, a scoping conversation, a roadmap, an orientation workshop, or
any paid-tier work — SHALL be described anywhere in the catalogue as free or unpaid.

#### Scenario: A doc restates the old free-orientation rule
- **WHEN** a reviewer finds a file stating that orientation, a scoping call, or a roadmap
  conversation is free
- **THEN** the file is out of conformance with this requirement and MUST be corrected to state that
  only presale (no deliverable) is free

#### Scenario: Presale itself is checked
- **WHEN** a reader asks whether presale produces a deliverable
- **THEN** the answer is no — presale is the free stage precisely because it has no deliverable, and
  every stage that does have one is paid

### Requirement: Three alternative paid entry points after presale
The engagement model SHALL define exactly three paid entry points reachable directly from presale —
P0-advisory, P1 Decision, and direct-to-build — modelled as mutually exclusive first purchases. A
client SHALL be able to buy any one of the three as their first paid engagement, without a
precondition that any other entry point must be completed first. After entry, the three SHALL remain
freely composable in any order (e.g., P0-advisory may lead to P1; a build contract may lead back to
P1 for a subsequent initiative).

#### Scenario: A client wants to buy a build contract directly
- **WHEN** a client already knows what they want and requests a direct-to-build engagement without
  having purchased P0-advisory or P1 first
- **THEN** the model permits selling the build contract directly, subject only to direct-to-build's
  own precondition (a requirements/use-case elicitation done at the start of the build contract, not
  a completed P1)

#### Scenario: A gate is found requiring P1 before P2
- **WHEN** a document states that a build engagement ("P2") is valid only once P1 is complete
- **THEN** the document is out of conformance with this requirement and the gate MUST be removed, not
  softened

### Requirement: P0-advisory is defined commercially, not procedurally
P0-advisory SHALL be documented as a paid, named, sellable product distinct from presale, typically
1–2 days in duration, whose output is explicitly not the Decision Package produced by P1. The
engagement model SHALL NOT prescribe P0-advisory's deliverable template, format, or internal
procedure.

#### Scenario: A reader asks whether P0-advisory substitutes for the Decision Package
- **WHEN** a reader checks what P0-advisory produces
- **THEN** the model states it is not, and does not substitute for, the Decision Package — the two
  are distinct paid products

#### Scenario: A document tries to define P0-advisory's deliverable template
- **WHEN** a proposed edit adds a deliverable template, artefact structure, or step-by-step
  procedure for P0-advisory
- **THEN** the edit exceeds this requirement's scope — P0-advisory is defined by its commercial
  facts (paid, 1–2 days, distinct from the Decision Package) only

### Requirement: P1 is a calendar-boxed fixed frame with a safeguards mechanism
P1 (Decision Phase) SHALL be documented as running 6–8 weeks, calendar-based rather than
effort-based, at a fixed price and fixed duration. The engagement model SHALL state a safeguards
mechanism: when agreed outcomes cannot reasonably be reached within the agreed duration for reasons
outside Meaningfy's control, Meaningfy SHALL signal this explicitly and propose one of exactly three
options — a scope reduction, a short extension, or a formal stop with partial delivery. A silent
overrun SHALL NOT be an available outcome.

#### Scenario: P1 risks running past its agreed duration
- **WHEN** stakeholder unavailability, information access problems, late decision-makers, or a
  reorganisation puts P1's agreed outcomes at risk within the agreed 6–8 week window
- **THEN** Meaningfy signals this explicitly to the client and proposes one of scope reduction, a
  short extension, or a formal stop with partial delivery

#### Scenario: A document anchors P1 to a man-day or rate-card estimate
- **WHEN** a document describes P1's price as derived from a predefined number of man-days or a rate
  card
- **THEN** the document is out of conformance — P1 is calendar-based, not effort-based, and the
  distinction MUST be stated alongside the 6–8 week figure

#### Scenario: A silent overrun is proposed as a resolution
- **WHEN** P1 is at risk of running long and no scope reduction, extension, or formal stop is
  proposed
- **THEN** this is out of conformance with the safeguards mechanism — silent overrun is not a valid
  outcome

### Requirement: P2 is a family of three independently sellable service lines
The engagement model SHALL define P2 as a family of three named service lines — software
development, ontology/model development, and training & capability building — named by service
line rather than sub-numbered. Each service line SHALL be independently sellable and freely
combinable with the others; none SHALL require another to be purchased first.

#### Scenario: A client wants to buy only the training service line
- **WHEN** a client requests only training & capability building, without a software-development or
  ontology-development contract
- **THEN** the model permits selling that service line on its own

#### Scenario: A document sub-numbers the service lines
- **WHEN** a document labels the service lines `P2a`, `P2b`, `P2c` or otherwise implies an order or
  hierarchy between them
- **THEN** the document is out of conformance — the service lines are named, not sub-numbered, and
  carry no implied order

### Requirement: Repeat business is a plain fact, not a labelled phase
A client who has closed two or more contracts SHALL be described as a repeat client, stated as a
plain fact rather than as a capitalised status label (e.g., "Partner") or as a numbered phase (e.g.,
"P3"). `executive-communication` SHALL be the owner that leads the repeat-client relationship. No
document SHALL reintroduce a capitalised partnership label or a phase-numbered slot for repeat
business.

#### Scenario: A client closes their second contract
- **WHEN** a client closes a second contract with Meaningfy
- **THEN** the client is described as a repeat client, and `executive-communication` leads that
  relationship going forward — no status is awarded, recorded, or expires

#### Scenario: A document reintroduces the "Partner" label or a P3 phase
- **WHEN** a document uses a capitalised "Partner" label or numbers repeat business as a fourth
  sequential phase ("P3")
- **THEN** the document is out of conformance with this requirement and MUST state the plain fact
  instead

### Requirement: Commercial-fact ownership is split from coaching-knowledge ownership
`docs/engagement/` SHALL be the single source of authority for the engagement model as company fact
(the stages, the free/paid line, the entry points, the service lines, the repeat-client rule).
`skills/semantic-consulting-coach/references/engagement-model.md` SHALL carry only reusable coaching
knowledge (the client cognitive states, state-2 signals, boundary-holding technique, and
engagement-design questions) and SHALL cite `docs/engagement/` for Meaningfy's instantiated
commercial facts rather than restating them.

#### Scenario: The coach reference states a commercial fact directly
- **WHEN** `skills/semantic-consulting-coach/references/engagement-model.md` states a commercial fact
  (e.g., a price, a duration, a free/paid boundary) without citing `docs/engagement/`
- **THEN** the file is out of conformance with this requirement and MUST be changed to cite the
  owning doc instead of restating the fact

#### Scenario: docs/engagement/ is missing a fact the coach reference states
- **WHEN** a commercial fact about the engagement model exists only in the coach's reference file and
  not in `docs/engagement/`
- **THEN** the fact MUST be added to `docs/engagement/` as the owning source, and the coach reference
  updated to cite it
