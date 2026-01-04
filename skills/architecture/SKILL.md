# Solution Architecture Skill

Assist users in developing rigorous system architecture models through **contract-first, documentation-first, specification-first** approaches. Use C4 (Context, Container, Component, Code) levels, ArchiMate, and UML notations to express architecture decisions. Support architectural decision-making using ADR (Architecture Decision Record) methodology, and guide users toward the final deliverables: rigorous models in Enterprise Architect, comprehensive architecture documentation, and formally-specified data structures.

## Final Deliverables

The architecture work produces three artifacts that evolve together:

1. **Models in Enterprise Architect (Sparks)**
   - ArchiMate views (L1–L2): Context, Application Cooperation, Technology
   - UML views (L3–L4): Component diagrams, Class diagrams, Sequence diagrams
   - BPMN views where business processes or choreography matter

2. **Architecture Document**
   - Executive summary of system purpose and scope
   - Architectural decisions (ADRs) organized by C4 level
   - Diagrams referenced from documentation, not embedded
   - Trade-off rationale and constraints

3. **Data Structures**
   - Primary: LinkML schemas (canonical definition of domain entities, relationships, attributes)
   - Secondary: UML Class diagrams (for design patterns, inheritance, associations)
   - Message contracts: OpenAPI (REST), AsyncAPI (async), Protobuf/JSON Schema (events)
   - Cross-reference: how LinkML data flows through components and services

## Communication Style

- **Crisp and diagram-oriented**: Describe what to model, emphasize diagrams over prose
- **Minimal explanation**: Assume user understands architecture and modelling
- **No drafting instructions**: Describe end-state results in textual/formal language only
- **Decision-driven**: Every modelling choice is justified by architectural intent
- **Strict semantics**: Correct notation usage is non-negotiable; incorrect semantics are called out explicitly

## Core Principles

### 1. C4 as Zoom Levels, Not Notation

C4 defines **abstraction levels** (Context, Container, Component, Code), not a notation. Each level answers a specific architectural question:

- **L1 (Context)**: Who interacts with the system? What external systems exist?
- **L2 (Container)**: What are the runtime units? What responsibilities do they have? How do they communicate?
- **L3 (Component)**: Inside one container, how are responsibilities divided?
- **L4 (Code)**: Classes, interfaces, message schemas, implementation details.

### 2. Notation Selection by Level

Use the appropriate notation for each level:

- **L1 (Context)**: ArchiMate Context/Cooperation (primary); UML Use Case for structural reference only
- **L2 (Containers)**: ArchiMate Application Cooperation (primary); UML Component as secondary option
- **L3 (Components)**: UML Component (primary); ArchiMate Application Structure as secondary option
- **L4 (Code)**: UML Class / Sequence (primary); no ArchiMate at this level

### 3. ArchiMate as Architectural Truth, UML as Software Design

- **ArchiMate** (L1–L2): States architectural facts, constraints, ownership, governance
  - Use for: system boundaries, contracts, replaceability, enterprise structure
  - Primary elements: Application Component, Application Service, Application Interface
  - Expresses: "what exists and what it offers"

- **UML** (L3–L4): Designs how software fulfills those facts
  - Use for: internal structure, behaviour, implementation details
  - Primary elements: Component, Class, Interface, relationships
  - Expresses: "how software responsibilities are split"

## Architecture Modelling Workflow

### Step 0: Extract Business Requirements & Architectural Drivers

**Purpose**: Understand what the business needs and identify which requirements will drive architecture (vs. implementation detail).

**Before you draw any diagram, answer these questions**:

- **Problem & Goal**: What business problem does this system solve?
- **Users**: Who will use it? How many concurrent users? (scalability driver)
- **Core Functions**: What must the system do? (scope)
- **Performance**: What's the latency/throughput requirement? (performance driver)
- **Availability**: How often can it fail? What's the uptime SLA? (reliability driver)
- **Integration**: Which external systems must it connect to? (integration driver)
- **Security/Compliance**: What data sensitivity? Regulatory requirements? (security driver)
- **Domain Complexity**: What are the key entities and relationships? (complexity driver)

**End Result**: Business Context document with extracted **Architectural Drivers**
- Drivers are requirements that directly shape architecture
- Distinguish drivers from implementation details
- Each driver will justify an ADR

**Reference**: See `business-requirements-to-architecture.md` for detailed guidance on extracting drivers from requirements.

**Critical**: Do not proceed to modeling (L1-L4) without clarity on drivers. Architecture decisions should trace back to business needs.

---

### Step 1: L1 – System Context

**Purpose**: Establish system boundary, identify external actors and systems, and define externally visible services.

**End Result (ArchiMate Context/Cooperation View)**:

- Business Layer: Business Actor (people/organisations only)
- Application Layer: Application Component (system under design + external systems)
- Application Services: Named, stable capabilities exposed by the system
- Relationships: Serving (service → actor/external system)

**What L1 Must NOT Include**:
- Business processes or workflows
- Internal structure or components
- Technology details
- Behaviour or sequencing
- Comma-separated labels on relationships (lift meaning into explicit Service elements instead)

### Step 2: L2 – Container View

**Purpose**: Define the major runtime deployable units and their collaboration patterns.

**End Result (ArchiMate Application Cooperation View)**:

- Application Components: Each container has one clear runtime responsibility
- Application Services: (Optional but clean) Named capabilities realised by each container
- Application Interfaces: (Optional) Contract surfaces where interaction modality matters
- Relationships: Realization, Serving, Flow (for sync/async only, no protocol detail)
- Exclude: All orchestration logic, step sequencing, protocol specifics, pre/post tasks

**Critical L2 Discipline**:
- One container = one runtime responsibility
- No mixing of behaviour or workflow semantics
- No internal orchestration details
- No data objects or schema concerns
- Containers are structure, not process

### Step 3: L3 – Component View

**Purpose**: Show internal responsibility division within ONE container only.

**End Result (UML Component Diagram or ArchiMate Application Structure)**:

- Internal components (logical building blocks of responsibility)
- Explicit interfaces and contracts
- Relationships: Dependency (labelled with interaction style: REST, Async event, In-process)
- One diagram per container
- No cross-container scope
- No Flow relationships between internal components (use dependency or association instead)

**Discipline**:
- Only internal design of a single container
- No behaviour (no Triggering or sequencing)
- No database specifics
- Responsibility-centric naming (Orchestrator, Validator, Adapter)

### Step 4: L4 – Code View

**Purpose**: Model implementation abstractions and contracts only.

**End Result (UML Class/Sequence Diagram)**:
- Only stable, public abstractions
- Interfaces, key classes, message schemas
- Do not model every class
- Minimal use; code is the source of truth

## Architectural Decision Records (ADRs)

Capture significant architectural decisions using a structured format. Organize ADRs by C4 level (Context, Containers, Components, Code) to make the decision hierarchy explicit. Each ADR documents an **irreversible architectural commitment** that shapes multiple lower-level concerns—not micro-decisions.

### Granularity: One ADR Per Significant Decision

- **L1 (Context)**: Decisions about system purpose, boundaries, major service exposure, actor definitions
  - Examples: "Separate public vs internal APIs", "Support multi-tenant or single-tenant model", "Define primary business actors and roles"
  - Typical count: 2–3 per system

- **L2 (Containers)**: Decisions about runtime units, deployment strategy, inter-container communication patterns
  - Examples: "Async message broker vs synchronous HTTP", "Canonical entity repository as single source of truth", "Container replaceability constraints"
  - Typical count: 3–5 per system

- **L3 (Components)**: Decisions about responsibility division within containers, interface ownership, internal patterns
  - Examples: "Adapter pattern for external integrations", "Orchestrator vs choreography within a container", "Contract ownership (who defines the interface)"
  - Typical count: 2–4 per container, not per component

- **L4 (Code)**: Decisions about stable APIs, public abstractions, library choices affecting architecture
  - Examples: "HTTP framework choice", "ORM vs query builder", "Async library choice"
  - Typical count: 1–2 per system (code-level decisions rarely affect architecture)

### ADR Template

```
## [Title]

### Context and Problem Statement
[Describes the issue, constraints, and context that motivated this decision]

### Considered Options
1. [Option A] – Description and trade-offs
2. [Option B] – Description and trade-offs
3. [Option C] – Description and trade-offs

### Decision Outcome
[The chosen option and why it was selected]

### Consequences
- [Positive consequence]
- [Positive consequence]
- [Negative consequence or limitation]
- [Negative consequence or limitation]

### Confirmation
[How this decision is validated in the model or implemented]

### Pros and Cons of the Options

#### Option A: [Title]
Good, because [argument a]
Good, because [argument b]
Bad, because [argument c]

#### Option B: [Title]
Good, because [argument a]
Neutral, because [argument b]
Bad, because [argument c]
```

### ADR Best Practices

1. **Compress by architectural significance** – One ADR per irreversible architectural commitment
   - Do compress: Multiple implementation consequences that follow from one design decision (e.g., "monotonic versioning" covers versioning strategy, update semantics, client expectations)
   - Do not compress: Decisions with independent trade-offs (e.g., async patterns and contract ownership are separate decisions)
   - Guideline: 5–8 ADRs is typical; 14+ suggests decisions are conflated or redundant

2. **Organize by C4 level** – Place ADRs in your Architecture Document grouped by L1, L2, L3
   - Helps readers understand scope: "Context decisions affect all containers"
   - Makes trade-offs visible: "We chose async at L2, which enables component independence at L3"

3. **Critique and polish** – Iteratively refine through:
   - Identify weak points or imprecision
   - Add missing options or constraints
   - Correct over-absolute statements
   - Ensure consequences match decision scope

4. **Avoid hand-waving** – Every consequence and trade-off must be explicit
   - If vague terms appear ("best effort", "appropriate"), introduce structure instead
   - Example: replace "role-based access" with explicit service boundaries or configuration rules

5. **Link to deliverables** – For each ADR, show how it appears in:
   - Models (which diagram elements, relationships, or patterns express this decision)
   - Specifications (OpenAPI, AsyncAPI, LinkML impacts)
   - Code (where the decision is enforced or visible)

## Common Interaction Patterns

### Pattern 0: Business Requirements to Architectural Drivers

**When to use**: At the start of any architecture project, before designing anything.

1. **Gather requirements** – Ask stakeholders what problem this system solves
2. **Identify scale drivers** – How many users? How much data? What throughput?
3. **Identify performance drivers** – What latency/freshness/consistency is needed?
4. **Identify reliability drivers** – What uptime SLA? Acceptable downtime?
5. **Identify integration drivers** – What external systems must it connect to?
6. **Identify security/compliance drivers** – Data sensitivity? Regulations?
7. **Identify domain complexity** – Key entities? Relationships? Master data needs?
8. **Distinguish drivers from detail** – What shapes architecture vs. implementation?
9. **Document business context** – Create Business Context document with drivers extracted

**Deliverable**: Business Context document; each architectural decision will justify itself against these drivers

**Reference**: See `business-requirements-to-architecture.md` for detailed guidance

---

### Pattern 1: Greenfield Architecture Discovery

**Assumes**: Business Context document with Architectural Drivers already extracted (Pattern 0)

1. **Confirm drivers** – Align with stakeholders on business drivers and constraints
2. **Propose L1 context** – ArchiMate showing actors, system boundary, services
3. **Propose L2 containers** – ArchiMate showing runtime units, responsibilities
4. **Map to drivers** – Show how each container addresses a business driver
5. **Record high-level design decisions** – ADRs for async vs sync, contracts, replaceability
6. **Specify contracts** – OpenAPI/AsyncAPI for inter-system communication
7. **Define domain structures** – LinkML for key entities and relationships
8. **Iterate** – Refine models and decisions based on feedback; ensure traceability to drivers

**Validation**: For each architecture decision, can you trace it back to a business driver?

### Pattern 2: Design Decision Exploration

1. **Identify the problem** – What architectural question are we answering?
2. **List options** – At least 2–3 genuinely different approaches
3. **Compare trade-offs** – Consequences and constraints for each
4. **Recommend and justify** – Present:
   - **Recommended choice** (with rationale)
   - **One rejected alternative** (briefly, why it was rejected)
   - Keep response concise: 1 paragraph max for rationale
5. **Record the decision** – As an ADR if it is irreversible and significant

**Note on decision framing**: If decision is premature, say so explicitly and state what must be decided first.

### Pattern 3: Diagram Review and Critique

1. **Validate scope** – What C4 level is this attempting to answer?
2. **Check notation** – Is this the right notation for this level? (See notation table)
3. **Identify semantic issues** – Are elements/relationships used correctly?
4. **Suggest improvements** – Remove what doesn't belong, add missing structure
5. **Propose end-state** – Describe the corrected result in formal language

**Reference**: See `diagram-examples-mermaid.md` for L1, L2, L3 examples + anti-patterns in Mermaid syntax. Shows correct structure, what to avoid, and why each pattern matters.

## Diagram Checklists (Apply Silently)

### ArchiMate L1 (Context/Cooperation)
- ✓ Business Actors represent people/organisations
- ✓ Application Components represent software systems
- ✓ Application Services represent externally visible capabilities
- ✓ Serving relationships only (no behaviour)
- ✗ No Business Processes, Functions, or Events
- ✗ No internal structure
- ✗ No comma-separated labels on relationships

### ArchiMate L2 (Application Cooperation)
- ✓ Application Components represent runtime containers
- ✓ Application Services represent capabilities (optional but clean)
- ✓ Application Interfaces represent contract surfaces
- ✓ Realization, Serving, Flow (sync/async only) relationships
- ✗ No Application Functions, Processes, or Events
- ✗ No Data Objects (schema concerns belong later)
- ✗ No protocol specifics (Kafka vs REST detail)
- ✗ No orchestration or step sequencing

### UML L3 (Component)
- ✓ Components represent logical responsibilities
- ✓ Dependency relationships labelled with interaction style
- ✓ Scope to single container only
- ✓ Explicit interfaces
- ✗ No Flow between internal components (use Dependency)
- ✗ No Classes or implementation detail
- ✗ No behaviour (Triggering, sequencing)

### UML L4 (Class/Sequence)
- ✓ Stable public abstractions only
- ✓ Interfaces, key classes, enumerations, key associations
- ✓ For behaviour: Sequence diagrams with lifelines and messages
- ✗ Do not model every class
- ✗ ArchiMate is not used at this level

**Class Diagrams (Domain Models)**: See `checklist-uml-class-domain.md`
- Domain concepts, not technical implementation
- Business semantics (not database schema)
- Expressible in LinkML (our canonical definition)
- Primary artifact for data structure specification

**Sequence Diagrams (Interaction)**: See `checklist-uml-sequence.md`
- Happy path + failure path (both shown)
- Async explicit (broker/queue shown)
- Who blocks vs. who's independent (visible)
- Matches L3 component structure

### UML Activity Diagram (Technical Workflows)
- ✓ Single owner (one component, one activity)
- ✓ Meaningful decisions (not step-by-step procedures)
- ✓ Swimlanes represent responsibility boundaries
- ✓ Use for: internal technical workflows, state machines, algorithms
- ✗ Not for: every small step or procedure
- ✗ Not for: messages (those belong in Sequence diagrams)

### BPMN Process/Collaboration (Business Workflows)
- ✓ Pools represent independent actors or systems
- ✓ Message flows only between pools
- ✓ Tasks are business-meaningful (not technical steps)
- ✓ Use for: end-to-end workflows, stakeholder choreography, business processes
- ✓ Show separate happy path and failure/timeout paths
- ✗ Not for: internal algorithms (use Activity diagram)
- ✗ Not for: message flows inside a single pool

## Behaviour and Interaction Patterns

### Sequence Diagrams (Technical Interactions)
- **Use for**: clarifying interaction timing and order (happy path + failure paths)
- **Participants**: components or services
- **Async requirement**: make async behaviour explicit (queues, topics, polling, callbacks)
- **Always show**:
  - Happy path (normal case)
  - At least one failure or timeout path
- **Do not use to replace**: L3 component responsibility division – use component diagrams for structure

**Reference**: See `sequence-diagram-examples.md` for 5 real examples in Mermaid syntax:
- Synchronous REST request-reply
- Asynchronous message-driven with polling
- Orchestrator coordinating multiple services
- Synchronous with timeout & retry
- Event-driven updates with parallel processing

### BPMN Workflows (Business-Facing Processes)
- **Use for**: stakeholder-facing workflows, end-to-end processes
- **Participants**: pools (independent actors or systems)
- **Message flows**: only between pools, not within
- **Always show**:
  - Happy path explicitly
  - Failure/timeout paths separately
- **Do not use for**: internal technical algorithms (use Activity diagram)

### Activity Diagrams (Internal Logic)
- **Use for**: internal workflows, state machines, complex technical algorithms
- **Participants**: swimlanes represent responsibility boundaries
- **Decisions**: only meaningful branch points, not step-by-step procedures
- **Single owner**: one component or service per activity diagram

## Contract-First, Specification-First Approach

Before drawing diagrams, define contracts and specifications. This ensures models are grounded in implementable reality rather than aspirational structure.

### Order of Artifacts

1. **Specifications first**: Define what the system must accept and produce
   - OpenAPI for REST endpoints (request/response schemas, error codes)
   - AsyncAPI for events and messages (topic/queue payloads, semantics)
   - LinkML for domain data structures (entities, attributes, relationships)
   - Protobuf or JSON Schema for internal message formats

2. **Documentation second**: Write architecture decisions and rationale
   - ADRs explain why choices were made
   - Constraint and trade-off documentation
   - Implementation notes linking decisions to code

3. **Models third**: Express architecture as diagrams anchored in specifications
   - ArchiMate/UML models visualize the structure
   - Reference specification artifacts (OpenAPI doc, LinkML schema)
   - Diagrams are views into a coherent specification, not independent

### Benefits of This Order

- **Specifications reveal ambiguities** before diagramming (e.g., "what exactly does this service produce?")
- **Models stay accurate** because they're derived from specs, not hand-drawn
- **Contracts are enforceable** (code generators, API validators) rather than aspirational
- **Evolution is traceable** (spec changes flow to models and code)

## Anti-Patterns to Avoid

1. **Mixing L2 with L3**: Embedding internal orchestration, tasks, or steps in a container view
   - **Smell**: Internal request processing details, pipeline steps, inter-component flows in the same diagram as runtime containers
   - **Fix**: Move to L3 component diagram; L2 shows only container boundaries and inter-container contracts

2. **Over-labelled relationships**: Using commas or prose to encode capabilities
   - **Smell**: "validates requests, transforms data, stores state" on one relationship
   - **Fix**: Create explicit Application Service elements; one relationship per interaction modality

3. **Conflating structure and behaviour**: Using Application Functions, Processes, or Events to describe structure
   - **Smell**: L2 diagram with "Request Validation", "Processing Pipeline" as components
   - **Fix**: Model as structure (components/containers) at L2; behaviour emerges from component interactions

4. **Technology-first modelling**: Allowing infrastructure choices to drive the architecture
   - **Smell**: "Kafka container", "Redis cache", "REST gateway" as primary elements
   - **Fix**: Model architecture first (ArchiMate with abstract services); place technology choices in Technology layer or suppress at L2

5. **Diagram-first without specifications**: Drawing before contracts are defined
   - **Smell**: Diagrams with vague labels ("API gateway", "data processor") that don't map to OpenAPI/AsyncAPI
   - **Fix**: Define OpenAPI, AsyncAPI, LinkML first; then diagram the runtime structure

6. **Unclear contracts**: Mixing API details, message schemas, and protocol concerns at the wrong level
   - **Smell**: Endpoint paths, JSON payloads, or header rules embedded in L1–L2 diagrams
   - **Fix**: Define contracts separately (OpenAPI, AsyncAPI); reference from diagrams only

7. **Replaceability claims without proof**: Saying something is "replaceable" without explicit interface ownership
   - **Smell**: "Service is pluggable" but no interface boundary drawn or contract specified
   - **Fix**: Model as Application Interface owned by orchestrator; service realises it; specify contract in OpenAPI/AsyncAPI

## Key Definitions

- **Container** (C4 L2): A runtime deployable unit (service, database, web app, etc.)
- **Component** (C4 L3): A logical responsibility within a container
- **Application Service** (ArchiMate): An externally visible capability offered by the system
- **Application Interface** (ArchiMate): A contract surface (API, topic, channel) through which a service is accessed
- **Realization**: "Component X realises Service Y" (the component provides that capability)
- **Serving**: "Service X serves Actor Y" (the actor benefits from / consumes the service)
- **Flow**: Interaction between components (synchronous or asynchronous; no protocol detail at L1–L2)

## When to Create Diagrams vs. Skip Them

- **Create** if the diagram answers one clear C4 question and supports decision-making
- **Skip** if the diagram mixes multiple levels or relies on prose labels to carry meaning
- **Defer** if you're uncertain about scope; document as ADR instead
- **Use Sequence diagrams** only to clarify critical behaviour; don't use to replace L3 structure

## Architecture Work Cycle: Toward Three Deliverables

### Phase 0: Understand Business Drivers

**Inputs**: Business stakeholders, requirements documents, constraints, vision

1. **Set up project structure** – Create folder organization for architecture artifacts
2. **Gather business requirements** – What problem does this solve? Who uses it? At what scale?
3. **Extract architectural drivers** – Which requirements directly shape architecture?
4. **Document business context** – Problem statement, users, goals, success metrics
5. **Identify constraints** – Scale, performance, availability, integration, security, domain complexity

**Deliverable**: Business Context document with Architectural Drivers clearly identified (in `business/` folder)

**References**:
- See `architecture-project-structure.md` for folder organization and workflow
- See `business-requirements-to-architecture.md` for detailed extraction process

**Critical**:
- Each architectural decision (ADR) must trace back to a driver
- Organize work in project folders from the start
- No drivers = no justified architecture

---

### Phase 1: Specify & Decide (Contracts and ADRs)

1. **Define domain structures** in LinkML (entities, attributes, relationships)
2. **Specify external contracts** as OpenAPI (REST) and AsyncAPI (async/events)
3. **Record architectural decisions** as ADRs organized by C4 level
4. **Document constraints** and non-functional requirements

**Deliverable**: Architecture Document with ADRs, LinkML schemas, and contract references

### Phase 2: Model the Architecture (Enterprise Architect)

1. **Create L1 (Context)** – ArchiMate showing system boundary, actors, external systems, services
2. **Create L2 (Containers)** – ArchiMate showing runtime deployable units and inter-container contracts
3. **Create L3 (Components)** – UML for critical containers showing internal responsibility division
4. **Create L4 (Code)** – UML Class/Sequence diagrams for critical abstractions (if needed)
5. **Map data flow** – trace LinkML domain objects through components and services

**Deliverable**: Enterprise Architect models (Sparks) with diagrams referenced from Architecture Document

### Phase 3: Verify & Trace

1. **Ensure specifications match models** – OpenAPI endpoints realised by L2 containers/L3 components
2. **Trace ADRs to implementation** – show how each decision appears in models, specs, and code
3. **Document deployment** – technology layer showing where containers run, databases, queues, etc.
4. **Plan evolution** – identify which decisions are stable vs. which might change

**Deliverable**: Complete architecture package: document + models + verified specifications

## Practical Example Structure

For a given system (any domain, any scale):

```
1. Architecture Document (Markdown or AsciiDoc)
   ├── Executive Summary
   ├── System Purpose & Scope
   ├── Non-Functional Requirements
   ├── ADRs Grouped by Level
   │   ├── L1 Context Decisions (2–3)
   │   ├── L2 Container Decisions (3–5)
   │   └── L3 Component Decisions (2–4)
   └── References to Diagrams & Specs

2. Enterprise Architect Repository (Sparks)
   ├── L1 Context Diagram (ArchiMate)
   ├── L2 Container Diagram (ArchiMate)
   ├── L3 Component Diagrams (UML, one per critical container)
   ├── Sequence Diagrams (critical paths)
   └── Technology Layer (where applicable)

3. Specifications (Git-versioned alongside code)
   ├── LinkML schemas/ (domain.yaml, entity.yaml, etc.)
   ├── OpenAPI specs/ (api.yaml, endpoints)
   ├── AsyncAPI specs/ (events.yaml, topics)
   └── Message schemas/ (Protobuf, JSON Schema)
```

All three artifacts reference each other and evolve together.

---

## Supporting Materials in /references/

This skill includes comprehensive reference guides in the `/references/` folder:

### Templates & Guides
- **ADR_TEMPLATE.md** – Standard format for creating Architectural Decision Records
- **business-requirements-to-architecture.md** – How to extract architectural drivers from business requirements
- **architecture-project-structure.md** – Project-oriented folder organization for architecture working sessions (decisions, diagrams by level, specifications, data models, deployment, implementation)

### Diagram Examples
- **diagram-examples-mermaid.md** – L1 Context, L2 Containers, L3 Components with Mermaid syntax + anti-pattern
- **diagram-examples.md** – Same examples in text format for detailed explanation
- **sequence-diagram-examples.md** – 5 real Sequence diagram examples in Mermaid (sync, async, polling, retry, events)

### Validation Checklists (1-page each)
- **checklist-archimate-l1.md** – Validate ArchiMate L1 Context diagrams
- **checklist-archimate-l2.md** – Validate ArchiMate L2 Container diagrams
- **checklist-uml-component.md** – Validate UML L3 Component diagrams
- **checklist-uml-sequence.md** – Validate UML Sequence diagrams (interaction paths, sync/async)
- **checklist-uml-class-domain.md** – Validate UML Class diagrams (domain concepts, expressible in LinkML)
- **checklist-bpmn.md** – Validate BPMN Process/Collaboration diagrams

### Pattern & Decision Examples
- **decision-pattern-examples.md** – 5 real decision examples + template (async vs sync, canonical data, contract ownership, versioning, detecting premature decisions)

**Total**: 13 supporting materials covering requirements, diagrams (text + Mermaid), checklists, decisions, sequences, and project organization.

---

## References for Deeper Understanding

- **C4 Model**: Context → Container → Component → Code, one zoom level per diagram
- **ArchiMate**: Standard notation for enterprise architecture (structure, services, governance)
- **UML**: Standard notation for software design (components, classes, sequences)
- **LinkML**: Declarative schema language for data structures and ontologies
- **ADR Format**: Captured in template above; compress by architectural significance, not implementation detail
- **Contract-First Design**: Treat OpenAPI / AsyncAPI / LinkML as canonical; diagrams and code reference, not replace
- **Enterprise Architect (Sparks)**: Repository for ArchiMate and UML models, source of truth for architecture diagrams
