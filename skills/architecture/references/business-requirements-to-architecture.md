# Business Requirements to Architecture: Extraction and Translation

This guide helps translate business requirements into architectural constraints, decisions, and specifications.

---

## Phase 1: Gather Business Requirements

### Key Questions to Ask

**Purpose & Scope**
- What problem does the system solve?
- Who are the primary users/actors?
- What is the business goal (revenue, cost reduction, efficiency, compliance)?
- What's in scope? What's out of scope?

**Users & Actors**
- Who will use this system? (internal, external, partners?)
- What are their roles and responsibilities?
- What's the expected usage pattern? (volume, frequency, concurrency)

**Core Capabilities (What Must It Do?)**
- What are the primary business functions?
- What data must the system handle?
- What decisions must the system support or automate?

**Quality & Non-Functional Needs**
- How fast must it respond? (latency requirements)
- How many users/transactions? (scalability, throughput)
- How often can it fail? (availability, uptime SLA)
- How long can data be "stale"? (consistency requirements)
- Security & compliance needs? (authentication, data protection, regulations)
- How long must data be retained? (data lifecycle)

**Constraints & Assumptions**
- Technology constraints? (existing systems, standards, skill set)
- Budget/timeline constraints?
- Organizational structure that affects design?
- Regulatory or compliance requirements?

**Future Vision**
- How might this system evolve?
- What are future use cases or integrations?
- Extensibility/modularity requirements?

---

## Phase 2: Extract Architectural Drivers

**Architectural drivers** are requirements that directly shape the system architecture (not implementation detail).

### Mapping Requirements → Architectural Drivers

| Requirement Category | Question | Architectural Driver | Example |
|---|---|---|---|
| **Users & Scale** | How many concurrent users? | Scalability constraints | "Support 10,000 concurrent users" |
| | How much data? | Data volume & storage | "Handle 100GB datasets" |
| **Performance** | Response time SLA? | Latency requirements | "95th percentile latency < 200ms" |
| | Data freshness? | Consistency model | "Near-real-time updates (< 5 sec)" |
| **Availability** | Uptime requirement? | Deployment & redundancy | "99.9% uptime SLA" |
| **Integration** | External systems? | Communication patterns | "Integrate with 3 external APIs" |
| **Security** | Data sensitivity? | Access control & boundaries | "PII must be isolated from public access" |
| | Compliance? | Audit & governance | "GDPR compliance required" |
| **Complexity** | Domain complexity? | Abstraction levels | "Complex entity relationship management" |

### Red Flags: What's NOT an Architectural Driver

❌ "Use Spring Boot" (technology choice, not driver)
❌ "Database in the cloud" (infrastructure, not driver)
❌ "Fast response times" (too vague; needs specific SLA)
❌ "User-friendly UI" (implementation concern)
✓ "Support 1000 concurrent requests per second" (architectural)
✓ "Process international payment in < 5 seconds" (latency driver)
✓ "Support multiple currencies and tax regimes" (domain complexity)

---

## Phase 3: Link Requirements to Architecture Decisions

### Example: E-Commerce Order Processing

**Business Requirement:**
"Process orders from multiple channels (web, mobile, API) with high reliability. Orders must be processed in < 2 seconds. Handle 10,000 concurrent users during peak times."

**Extracted Architectural Drivers:**
1. Multi-channel integration (drives L1 context and inter-system contracts)
2. Sub-2-second latency (drives synchronous vs async decision at L2)
3. 10,000 concurrent users (drives scalability and deployment strategy)
4. High reliability (drives fallback and retry patterns at L3)

**Architecture Decisions These Enable:**
- L2 Decision: "Async message queue for order events" (handles concurrency, decouples channels)
- L2 Decision: "Order status cache for fast reads" (sub-2-second latency)
- L3 Decision: "Circuit breaker pattern for payment service" (high reliability)

**Specifications Derived:**
- OpenAPI: Order submission endpoint (multi-channel entry points)
- AsyncAPI: Order events topic (decoupled processing)
- LinkML: Order entity schema (what data flows through system)

---

## Phase 4: Document Requirements as Architecture Context

### Template for Architecture Document

```markdown
## Business Context

### Problem & Opportunity
[What business problem does this solve?]

### Primary Users
[Who uses this system?]

### Key Business Goals
1. [Goal 1]
2. [Goal 2]
3. [Goal 3]

## Architectural Drivers (Requirements That Shape Architecture)

### Scalability
- Expected concurrent users: [number]
- Expected transactions/sec: [number]
- Data volume: [size]
- **Architecture Impact**: [How this drives decisions]

### Performance
- Latency SLA: [response time]
- Data freshness requirement: [staleness tolerance]
- **Architecture Impact**: [How this drives decisions]

### Availability & Reliability
- Uptime SLA: [percentage]
- Acceptable downtime window: [duration]
- **Architecture Impact**: [How this drives decisions]

### Integration & Interoperability
- External systems to integrate: [list]
- Communication protocols: [REST, async, gRPC, etc.]
- **Architecture Impact**: [How this drives decisions]

### Security & Compliance
- Data sensitivity: [public/internal/confidential]
- Regulatory requirements: [GDPR, HIPAA, etc.]
- Authentication model: [OAuth, SAML, etc.]
- **Architecture Impact**: [How this drives decisions]

### Domain Complexity
- Key domain concepts: [entity types, relationships]
- Master data requirements: [canonical entities]
- **Architecture Impact**: [How this drives decisions]

## Non-Drivers (Explicitly Out of Scope)

- [Constraint that will not drive architectural decisions]
- [Technology choice to be made later]
- [Implementation detail]
```

---

## Phase 5: Validate Requirements → Architecture Traceability

**Traceability Matrix**: Can you trace each architectural decision back to a business requirement?

```
Business Requirement          → Architectural Driver → Architecture Decision → Specification
─────────────────────────────────────────────────────────────────────────────────────────
"Handle 10K concurrent users" → Scalability          → Async message queue → AsyncAPI: order-events
"Sub-2-sec latency"           → Performance          → Cache layer for reads → Implementation detail
"Multi-channel integration"   → Integration          → L1 context shows 3 entry points → OpenAPI for each
"PII isolation"               → Security             → Separate access control per data type → Spec: data classification
```

If you can't trace it, either:
- The requirement isn't architectural (it's implementation detail)
- The decision isn't justified by requirements (add the requirement or remove the decision)

---

## Key Principles

1. **Requirements → Drivers → Decisions → Specs**
   - Not: Specs without requirements
   - Not: Decisions without driver
   - Not: Drivers without business context

2. **Explicit about what matters**
   - State SLAs, not "fast" or "reliable"
   - State integration needs, not "will integrate eventually"
   - State compliance rules, not "secure"

3. **Distinguish business value from technical implementation**
   - Business: "Process 1M transactions/day with < 1% error"
   - Technical: "Use Kafka for async, Redis for cache"
   - Architecture bridges these (why Kafka helps with business need)

4. **Some requirements are NOT architectural**
   - "Use Kubernetes" → technical choice, not driver
   - "Pretty dashboard" → UI/UX, not architecture
   - "RESTful API" → implementation choice, not driver
   - But: "API accessed by 100K clients" → scalability driver

---

## Questions to Challenge Requirements

**Is this really a requirement?**
- "Is this something the business pays for or cares about?"
- "If we removed this, would customers notice or care?"
- "Is this driven by regulation/compliance or business choice?"

**Is this architectural?**
- "Does this change how we structure components?"
- "Does this affect inter-system contracts?"
- "Does this limit our implementation choices significantly?"

**Is this measurable?**
- "Can we test whether we met this requirement?"
- "Can we define SLA/metric for this?"
- "Is this vague ('fast') or specific ('< 200ms')"?

---

## Common Requirements Patterns

### High-Throughput System
```
Requirements:
- 1M+ requests/day
- 100-1000 requests/second

Architecture Impact:
- Async patterns (queues, topics)
- Horizontal scaling needed
- Load balancing & cache layers
- May need eventual consistency
```

### Real-Time System
```
Requirements:
- Sub-100ms latency
- < 1 second data freshness
- Strong consistency needed

Architecture Impact:
- Synchronous communication
- In-memory caches
- No heavy async processing
- Replication for high availability
```

### Master Data System (Single Source of Truth)
```
Requirements:
- Canonical entity authority
- Cross-system entity references
- Version history tracking

Architecture Impact:
- Central repository
- Other systems query/reference
- Versioning strategy (monotonic recommended)
- Audit trail for compliance
```

### Multi-Tenant System
```
Requirements:
- Data isolation per tenant
- Independent scaling per tenant
- Custom configurations per tenant

Architecture Impact:
- Data partitioning strategy
- Access control granularity
- Deployment: shared vs. separate
- Configuration management
```

---

## Checklist: Before You Design Architecture

- [ ] Documented business problem & goals
- [ ] Identified primary users & actors
- [ ] Listed core business functions
- [ ] Extracted scalability drivers (users, data volume, throughput)
- [ ] Extracted performance drivers (latency, freshness, consistency)
- [ ] Extracted reliability drivers (uptime SLA, acceptable downtime)
- [ ] Identified integration needs (external systems, protocols)
- [ ] Documented security & compliance requirements
- [ ] Identified domain complexity (key entities, relationships)
- [ ] Distinguished architectural drivers from implementation details
- [ ] Assigned owner for each driver (who cares about this requirement?)
- [ ] Prioritized drivers (which matter most?)
