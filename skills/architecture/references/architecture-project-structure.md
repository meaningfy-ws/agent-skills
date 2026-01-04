# Architecture Project Structure - Systematic Organization

Standard folder structure for organizing architecture working sessions as projects. All artifacts from discovery through implementation guide are organized for easy navigation and evolution.

---

## 1. Project Root Structure

```
my-architecture-project/
├── README.md ........................... Project overview & quick start
├── ARCHITECTURE.md ..................... Main architecture document
├── decisions/ .......................... Architectural decisions (ADRs)
├── specifications/ ..................... API & data contracts
├── diagrams/ ........................... All architecture diagrams
├── data-models/ ........................ Domain data structures
├── business/ ........................... Business context & requirements
├── deployment/ ......................... Technology & deployment
├── implementation/ ..................... Code mapping & guidelines
├── glossary.md ......................... Business terms & definitions
├── changelog.md ........................ Evolution log
└── references.md ....................... External links & resources
```

---

## 2. Decisions Folder

```
decisions/
├── README.md ........................... Index & how to read
├── l1-context/
│   ├── ADR-001-system-boundary.md
│   ├── ADR-002-multi-tenant-model.md
│   └── ADR-003-service-exposure.md
├── l2-containers/
│   ├── ADR-010-async-communication.md
│   ├── ADR-011-canonical-repository.md
│   ├── ADR-012-replaceability.md
│   └── ADR-013-deployment-strategy.md
├── l3-components/
│   ├── ADR-020-adapter-pattern.md
│   ├── ADR-021-contract-ownership.md
│   └── ADR-022-orchestration-strategy.md
└── l4-code/
    └── ADR-030-framework-choice.md
```

**Format**: Each file follows ADR_TEMPLATE.md
- Context & Problem
- Considered Options
- Decision Outcome
- Consequences
- Confirmation
- Pros & Cons

**Organization**: By C4 level (makes decision hierarchy visible)

---

## 3. Specifications Folder

```
specifications/
├── openapi/ ........................... REST API contracts
│   ├── entities-api.yaml
│   ├── resolution-api.yaml
│   └── _common/
│       ├── schemas.yaml
│       ├── errors.yaml
│       └── pagination.yaml
├── asyncapi/ .......................... Event/async contracts
│   ├── resolution-events.yaml
│   ├── entity-updates.yaml
│   └── _common/
│       ├── messages.yaml
│       └── channels.yaml
├── linkml/ ............................ (moved to data-models/)
├── json-schema/ ....................... Internal message formats
│   ├── request-format.json
│   └── response-format.json
└── protobuf/ .......................... (if applicable)
    └── domain.proto
```

**Format**:
- OpenAPI 3.0+ YAML
- AsyncAPI 2.6+ YAML
- JSON Schema for validation
- Protobuf if using gRPC

**Note**: These are canonical specifications. Code should be generated from these, not the other way around.

---

## 4. Diagrams Folder

```
diagrams/
├── README.md ........................... Diagram inventory & viewing guide
├── l1-context/
│   ├── system-context.mermaid
│   ├── system-context.txt
│   └── notes-l1.md
├── l2-containers/
│   ├── container-overview.mermaid
│   ├── container-overview.txt
│   ├── communication-patterns.mermaid
│   └── notes-l2.md
├── l3-components/
│   ├── orchestrator-components.mermaid
│   ├── orchestrator-components.txt
│   ├── repository-components.mermaid
│   ├── repository-components.txt
│   └── notes-l3.md
├── l4-code/
│   ├── domain-class-model.mermaid
│   ├── key-interfaces.txt
│   └── critical-flows.mermaid
├── sequences/
│   ├── happy-path-resolution.mermaid
│   ├── failure-path-timeout.mermaid
│   ├── async-processing-flow.mermaid
│   └── polling-for-results.mermaid
├── processes/
│   ├── order-processing-flow.mermaid
│   └── entity-lifecycle.mermaid
├── technology/
│   ├── deployment-topology.txt
│   ├── network-architecture.txt
│   └── infrastructure-nodes.mermaid
└── anti-patterns/
    └── what-we-rejected.md
```

**Organization**:
- By C4 level (L1-L4)
- Behavior diagrams (Sequences, Processes)
- Technology layer (deployment)
- Anti-patterns (for reference)

**Formats**:
- Mermaid (.mermaid) - version controlled, can be rendered
- Text descriptions (.txt) - explains what the diagram shows
- Markdown notes (.md) - rationale, decisions leading to this structure

---

## 5. Data Models Folder

```
data-models/
├── README.md ........................... Data structure overview
├── linkml/
│   ├── domain.yaml ..................... Main schema
│   ├── entity.yaml ..................... Entity definitions
│   ├── relationships.yaml .............. Relationship types
│   ├── enumerations.yaml ............... Value sets
│   ├── imports/
│   │   ├── standard-types.yaml
│   │   └── common-patterns.yaml
│   └── generated/
│       ├── domain.json (generated from LinkML)
│       └── domain.sql (if applicable)
├── uml-conceptual/
│   ├── domain-classes.mermaid
│   ├── domain-classes.txt
│   └── entity-relationships.mermaid
├── validation/
│   ├── entity-constraints.md
│   └── data-quality-rules.md
└── evolution/
    ├── v1.0-changelog.md
    ├── v1.1-changelog.md
    └── compatibility-notes.md
```

**Key Points**:
- LinkML is PRIMARY, canonical source
- UML diagrams are visual reference
- Generated artifacts (JSON, SQL) are NOT hand-edited
- Evolution tracking for schema changes

**Relationship to Specifications**:
- OpenAPI schemas reference LinkML definitions
- AsyncAPI message payloads match LinkML structure
- Code generation tools read LinkML, generate validators

---

## 6. Business Context Folder

```
business/
├── business-context.md ................. Problem, actors, goals, success metrics
├── requirements/
│   ├── functional-requirements.md ...... What system must do
│   ├── non-functional-requirements.md . Scale, latency, availability
│   ├── constraints.md .................. Budget, timeline, technical constraints
│   └── assumptions.md .................. What we assume to be true
├── drivers/
│   ├── architectural-drivers.md ........ Business drivers that shape architecture
│   ├── scalability-drivers.md .......... User count, data volume, throughput
│   ├── reliability-drivers.md .......... Uptime SLA, acceptable downtime
│   └── integration-drivers.md .......... External systems, protocols
├── stakeholders/
│   ├── stakeholder-map.md .............. Who cares about what
│   ├── user-personas.md
│   └── success-criteria.md
└── glossary.md ......................... Business terms & definitions
```

**Purpose**:
- Captures "why" before "how"
- Justifies every architectural decision
- Single source of truth for business context

**Relationship to Decisions**:
- Every ADR traces back to a driver
- Drivers are documented here
- Traceability: requirement → driver → decision → implementation

---

## 7. Deployment & Technology Folder

```
deployment/
├── technology-layer.md ................. Technology choices & rationale
├── deployment-model.md ................. How system is deployed
├── infrastructure/
│   ├── network-architecture.md
│   ├── data-stores.md .................. Databases, caches, queues
│   ├── message-brokers.md .............. Kafka, RabbitMQ, etc.
│   ├── cloud-platform.md ............... AWS, Azure, GCP specifics
│   └── monitoring-observability.md .... Logging, metrics, tracing
├── scaling/
│   ├── horizontal-scaling.md
│   ├── load-balancing.md
│   └── caching-strategy.md
├── disaster-recovery.md ................ Backup, failover, recovery
└── security/
    ├── authentication-strategy.md
    ├── authorization-model.md
    ├── data-protection.md
    └── compliance-requirements.md
```

**Not in Architecture Phase**: Implementation details belong here, not in L1-L3 diagrams
- Specific cloud provider (AWS vs Azure)
- Specific database (PostgreSQL vs MongoDB)
- Specific message broker (Kafka vs RabbitMQ)
- Specific framework versions

---

## 8. Implementation Guidance Folder

```
implementation/
├── code-mapping.md ..................... How diagrams map to code modules
│   ├── L3 components → code packages
│   ├── Services → code classes
│   ├── Interfaces → code interfaces
│   └── Messages → data classes
├── module-structure.md ................. Recommended code layout
├── naming-conventions.md ............... Class, method, package naming
├── implementation-checklist.md ......... Team checklist before coding
├── team-responsibilities.md ............ Who owns what component
└── onboarding-guide.md ................. New developer quick start
```

**Purpose**:
- Bridge between architecture & implementation
- Ensures diagrams guide actual code
- Makes architecture actionable

---

## 9. Meeting Notes & Evolution

```
sessions/
├── 2024-01-15-kickoff.md
├── 2024-01-22-l1-review.md
├── 2024-02-05-async-decision.md
└── 2024-02-15-component-refinement.md
```

**Content**:
- What was discussed
- Decisions made (with links to ADRs)
- Open questions
- Next steps

**Use**: Understand decision context and evolution

---

## 10. Root-Level Documents

### README.md
```markdown
# [System Name] Architecture

Brief description of what this system does.

## Quick Start
- For diagrams: see `diagrams/README.md`
- For business context: see `business/business-context.md`
- For decisions: see `decisions/README.md`
- For API contracts: see `specifications/openapi/`
- For data models: see `data-models/linkml/`

## Key Facts
- Business drivers: see `business/drivers/`
- Deployment: see `deployment/`
- Team: see `implementation/team-responsibilities.md`
```

### ARCHITECTURE.md (Main Document)
```markdown
# [System Name] Architecture Document

1. Executive Summary
2. Problem Statement & Business Drivers
3. System Context (L1 - with diagram)
4. Container Architecture (L2 - with diagram)
5. Component Architecture (L3 - with diagrams per container)
6. Data Model (LinkML schema + UML class diagram)
7. Key Sequence Flows (interaction diagrams)
8. Architectural Decisions (ADRs organized by level)
9. Deployment & Technology
10. Implementation Roadmap
11. Glossary & References
```

**Links**: Each section links to detailed documents in subfolders

### changelog.md
```markdown
# Evolution Log

## Version 1.1 (2024-02-15)
- ADR-021: Changed contract ownership from provider to orchestrator
- Added async polling pattern to L3 components
- Updated LinkML schema v1.1 with new entity types

## Version 1.0 (2024-01-15)
- Initial architecture complete
- L1-L3 diagrams finalized
- Core ADRs documented
```

---

## 11. File Naming Conventions

### Diagrams
```
{level}-{component}-{type}.{format}
l1-system-context.mermaid
l2-containers-communication.mermaid
l3-orchestrator-components.mermaid
sequence-async-resolution.mermaid
```

### Decisions
```
ADR-{number}-{title}.md
ADR-001-system-boundary.md
ADR-010-async-communication.md
ADR-020-adapter-pattern.md
```

### Specifications
```
{domain}-{type}.{format}
entities-api.yaml
resolution-events.yaml
domain-schema.yaml
```

### Data Models
```
{entity-type}.{format}
domain.yaml
entity.mermaid
entity-relationships.mermaid
```

---

## 12. Complete Folder Tree Example

```
entity-resolution-architecture/
├── README.md
├── ARCHITECTURE.md
├── changelog.md
├── glossary.md
├── references.md
│
├── decisions/
│   ├── README.md
│   ├── l1-context/
│   │   ├── ADR-001-system-boundary.md
│   │   ├── ADR-002-public-vs-internal-apis.md
│   │   └── ADR-003-multi-tenant.md
│   ├── l2-containers/
│   │   ├── ADR-010-async-communication.md
│   │   ├── ADR-011-canonical-repository.md
│   │   └── ADR-012-replaceability.md
│   ├── l3-components/
│   │   ├── ADR-020-adapter-pattern.md
│   │   └── ADR-021-contract-ownership.md
│   └── l4-code/
│       └── ADR-030-framework-choice.md
│
├── specifications/
│   ├── openapi/
│   │   ├── entities-api.yaml
│   │   ├── resolution-api.yaml
│   │   └── _common/
│   │       ├── schemas.yaml
│   │       └── errors.yaml
│   ├── asyncapi/
│   │   ├── resolution-events.yaml
│   │   └── _common/
│   │       └── channels.yaml
│   └── json-schema/
│       ├── request-format.json
│       └── response-format.json
│
├── diagrams/
│   ├── README.md
│   ├── l1-context/
│   │   ├── system-context.mermaid
│   │   ├── system-context.txt
│   │   └── notes-l1.md
│   ├── l2-containers/
│   │   ├── container-overview.mermaid
│   │   ├── container-overview.txt
│   │   └── notes-l2.md
│   ├── l3-components/
│   │   ├── orchestrator-components.mermaid
│   │   ├── orchestrator-components.txt
│   │   ├── repository-components.mermaid
│   │   └── repository-components.txt
│   ├── l4-code/
│   │   └── domain-class-model.mermaid
│   ├── sequences/
│   │   ├── happy-path-resolution.mermaid
│   │   ├── failure-path-timeout.mermaid
│   │   └── async-processing-flow.mermaid
│   └── processes/
│       └── entity-lifecycle.mermaid
│
├── data-models/
│   ├── README.md
│   ├── linkml/
│   │   ├── domain.yaml
│   │   ├── entity.yaml
│   │   ├── relationships.yaml
│   │   ├── enumerations.yaml
│   │   └── generated/
│   │       ├── domain.json
│   │       └── domain.sql
│   ├── uml-conceptual/
│   │   ├── domain-classes.mermaid
│   │   └── domain-classes.txt
│   └── evolution/
│       ├── v1.0-changelog.md
│       └── v1.1-changelog.md
│
├── business/
│   ├── business-context.md
│   ├── requirements/
│   │   ├── functional-requirements.md
│   │   ├── non-functional-requirements.md
│   │   ├── constraints.md
│   │   └── assumptions.md
│   ├── drivers/
│   │   ├── architectural-drivers.md
│   │   ├── scalability-drivers.md
│   │   └── reliability-drivers.md
│   └── stakeholders/
│       ├── stakeholder-map.md
│       └── user-personas.md
│
├── deployment/
│   ├── technology-layer.md
│   ├── deployment-model.md
│   ├── infrastructure/
│   │   ├── data-stores.md
│   │   ├── message-brokers.md
│   │   └── monitoring-observability.md
│   └── security/
│       ├── authentication-strategy.md
│       └── authorization-model.md
│
├── implementation/
│   ├── code-mapping.md
│   ├── module-structure.md
│   ├── naming-conventions.md
│   ├── implementation-checklist.md
│   └── team-responsibilities.md
│
└── sessions/
    ├── 2024-01-15-kickoff.md
    ├── 2024-01-22-l1-review.md
    ├── 2024-02-05-async-decision.md
    └── 2024-02-15-component-refinement.md
```

---

## 13. Workflow: How Folders Work Together

### Starting a New Architecture Project

1. **Create project folder** with README
2. **Gather business context** → `business/`
3. **Extract architectural drivers** → `business/drivers/`
4. **Design L1 context** → `diagrams/l1-context/` + `decisions/l1-context/`
5. **Design L2 containers** → `diagrams/l2-containers/` + `decisions/l2-containers/`
6. **Design L3 components** → `diagrams/l3-components/` + `decisions/l3-components/`
7. **Define data model** → `data-models/linkml/` + `diagrams/l4-code/`
8. **Create specifications** → `specifications/openapi/` + `specifications/asyncapi/`
9. **Plan deployment** → `deployment/`
10. **Create implementation guide** → `implementation/`
11. **Consolidate into ARCHITECTURE.md** → root level

### Reviewing Architecture

1. Read `README.md` and `ARCHITECTURE.md` for overview
2. Check `business/business-context.md` for "why"
3. Follow diagrams: `diagrams/l1/` → `diagrams/l2/` → `diagrams/l3/`
4. Read relevant ADRs for decisions
5. Check specifications for contracts
6. Review data model in `data-models/`

### Implementing from Architecture

1. Check `implementation/code-mapping.md` for structure
2. Follow `business/` for business rules
3. Use `diagrams/l3-components/` for component structure
4. Reference `specifications/` for API contracts
5. Use `data-models/linkml/` for data structures
6. Check `deployment/` for runtime requirements

---

## 14. Benefits of This Structure

✅ **Organization**
- Everything has a clear home
- Easy to find what you need
- Scalable to large projects

✅ **Traceability**
- Business drivers → Decisions → Diagrams → Specs → Code
- Clear links between artifacts

✅ **Collaboration**
- Team members know where to look
- Clear ownership (who owns what folder)
- Session notes for context

✅ **Evolution**
- Changelog tracks changes
- Data models versioned
- Decisions never deleted (only superseded)

✅ **Documentation**
- Self-documenting structure
- README in each folder
- Clear naming conventions

✅ **Tool Integration**
- Diagrams in Mermaid (version control friendly)
- Specs in YAML (code generation ready)
- Data models in LinkML (canonical source)
- Markdown for documentation (readable anywhere)

✅ **Maintainability**
- Architecture decisions are immutable (with ADR supersede pattern)
- Diagrams stay in sync with code
- Specs drive implementation (not other way around)
