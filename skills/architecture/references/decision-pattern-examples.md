# Architectural Decision Pattern Examples

Reference examples showing how to frame and present architectural decisions using the recommended pattern: **Recommended Choice + 1 Rejected Alternative + Rationale**.

---

## Example 1: Synchronous vs Asynchronous Communication (L2 Decision)

### Problem
How should containers communicate at L2? Should inter-container interactions be synchronous (request-reply) or asynchronous (message-driven)?

### Options Presented

**Recommended: Asynchronous (message broker)**
- Containers publish events to topics/queues
- Consumers subscribe and process independently
- Enables container independence and scalability
- Rationale: Reduces coupling, supports independent scaling, enables retry/failure handling

**Rejected: Synchronous (direct HTTP/gRPC calls)**
- One container calls another directly, waits for response
- Simpler to understand and trace
- But: tight coupling, cascading failures, difficult to scale independently

### How to Frame
When asked "async or sync?":
1. **Recommended choice**: Asynchronous via message broker
2. **Why rejected synchronous**: Couples containers, makes independent deployment harder
3. **Trade-off in one sentence**: "We trade operational complexity for container independence and failure isolation"

---

## Example 2: Canonical Entity Repository vs Distributed Data (L2 Decision)

### Problem
Should domain entity data live in one central repository (single source of truth) or be replicated/managed by multiple containers?

### Options Presented

**Recommended: Canonical Entity Repository**
- One authoritative container owns entity state
- All entity versions, metadata, relationships live here
- Other containers query/reference, don't duplicate
- Rationale: Single source of truth, consistent versioning, clear ownership

**Rejected: Distributed ownership**
- Each container manages its own view of entities
- Data replicated/synchronized across containers
- But: conflicts, eventual consistency complexity, unclear ownership, harder to trace relationships

### How to Frame
When asked "canonical vs distributed?":
1. **Recommended choice**: Single canonical repository with clear ownership
2. **Why rejected distributed**: Replication complexity, sync conflicts, unclear authority
3. **Trade-off in one sentence**: "We trade local autonomy for guaranteed consistency and clear version management"

---

## Example 3: Contract Ownership - Who Defines the Interface? (L3 Decision)

### Problem
For a critical interface between components, who should define/own the contract: the provider or the consumer?

### Options Presented

**Recommended: Consumer/Orchestrator owns the contract (Provider realises it)**
- Orchestrator defines what it needs
- Provider implements to that specification
- Contract lives with orchestrator (who knows the requirements)
- Rationale: Reduces coupling, provider can change internal implementation, contract stability

**Rejected: Provider owns the contract**
- Provider defines what it offers
- Consumer must adapt to provider's interface
- But: tightly couples consumer to provider's design, harder to swap providers, provider drives design

### How to Frame
When asked "who owns this interface?":
1. **Recommended choice**: Orchestrator/consumer owns the contract (in OpenAPI or AsyncAPI)
2. **Why rejected provider ownership**: Couples consumer to provider decisions, harder to make provider replaceable
3. **Trade-off in one sentence**: "Consumer defines what it needs; provider is responsible for delivering it—enables pluggability"

---

## Example 4: Monotonic Versioning vs Status Fields (L3 Decision)

### Problem
How should we track entity evolution: via monotonic version numbers or explicit status/lifecycle states?

### Options Presented

**Recommended: Monotonic versioning only**
- Versions increment monotonically (1, 2, 3, ...)
- Clients check version to know if state changed
- Status/meaning evolves with versions, not separate states
- Rationale: Simple, unambiguous, clients control polling/polling frequency

**Rejected: Status field with state machine**
- Entity has status field (DRAFT, RESOLVED, ARCHIVED, etc.)
- State machine defines allowed transitions
- But: status explosion, workflow coupling, unclear versioning, harder to add future states

### How to Frame
When asked "version vs status?":
1. **Recommended choice**: Monotonic versioning; clients observe version changes
2. **Why rejected status fields**: Leads to state explosion, couples clients to business workflow
3. **Trade-off in one sentence**: "We track evolution via versions, not status—simpler and more flexible for future changes"

---

## Example 5: Premature Decision Detection

**When to say "this decision is premature":**

Wrong answer: "We should use async messaging"
Right answer: "This decision is premature until we answer:
1. How many containers will communicate?
2. What's the acceptable latency for responses?
3. Do we need strong consistency or eventual consistency?

Once we decide those, then async vs sync becomes clear."

---

## Template for Your Decisions

```
### Problem
[What architectural question needs answering?]

### Recommended Choice
[Your recommended approach]
[Why this choice makes sense]

### Rejected Alternative
[What you considered but rejected]
[Why it was rejected (constraints, trade-offs)]

### Trade-off Summary
[One sentence capturing the key trade-off]
```

---

## Key Patterns to Notice

1. **Always have exactly 1 rejected alternative** (not 2-3)
   - Simplifies decision
   - Focus on the real tension

2. **Rationale is brief** (1-2 sentences max)
   - Users shouldn't need deep context
   - Should be self-evident once stated

3. **Trade-off is explicit**
   - "We gain X but accept Y"
   - Not hidden in implications

4. **Avoid premature decisions**
   - State what must be decided first
   - Don't decide in a vacuum
