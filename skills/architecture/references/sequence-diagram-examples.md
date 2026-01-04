# Sequence Diagram Examples

Real-world sequence diagrams showing interaction patterns, happy paths, and failure paths.

---

## Example 1: Synchronous REST Request-Reply

**Scenario**: Simple synchronous interaction between API Client and REST service.

### Happy Path

```mermaid
sequenceDiagram
    participant Client
    participant APIGateway as API Gateway
    participant Service
    participant Database

    Client->>APIGateway: POST /resolve (entity data)
    APIGateway->>Service: REST Call: resolve(entity)
    Service->>Database: Query: find_entity(id)
    Database-->>Service: entity record
    Service->>Service: Process entity
    Service-->>APIGateway: 200 OK + resolved entity
    APIGateway-->>Client: 200 OK + result
```

**Key points:**
- Synchronous request-reply (arrow `>>` for calls, `-->>` for returns)
- Each step waits for response
- Clear sequence from request to response
- Participant names match components/services

### Failure Path: Timeout

```mermaid
sequenceDiagram
    participant Client
    participant APIGateway as API Gateway
    participant Service
    participant Database

    Client->>APIGateway: POST /resolve (entity data)
    APIGateway->>Service: REST Call: resolve(entity)
    Service->>Database: Query: find_entity(id)
    Database--xService: Timeout (no response)
    Service--xAPIGateway: 504 Gateway Timeout
    APIGateway--xClient: 504 Gateway Timeout
```

**Key points:**
- Use `--x` to show failed/error returns
- Timeout shown as no response from database
- Error propagates up the chain
- Client sees timeout error

---

## Example 2: Asynchronous Message-Driven Interaction

**Scenario**: Order resolution via async message queue. Publisher doesn't wait for response.

### Happy Path: Async Processing

```mermaid
sequenceDiagram
    participant Client
    participant Orchestrator as Resolution<br/>Orchestrator
    participant Broker as Message Broker<br/>(Kafka/RabbitMQ)
    participant Engine as Entity Resolution<br/>Engine
    participant Repository as Entity<br/>Repository

    Client->>Orchestrator: resolve(entity) - sync request
    Orchestrator->>Repository: save_draft_entity()
    Repository-->>Orchestrator: draft entity + URI
    Orchestrator-->>Client: 202 Accepted + URI (async job)

    Note over Orchestrator,Broker: Async Processing (decoupled)

    Orchestrator->>Broker: publish(resolution_request)
    Broker-->>Orchestrator: acknowledged

    Broker->>Engine: deliver(resolution_request)
    Engine->>Engine: process entity
    Engine->>Broker: publish(resolution_result)

    Broker->>Orchestrator: deliver(resolution_result)
    Orchestrator->>Repository: update_canonical_entity(result)
    Repository-->>Orchestrator: entity updated
```

**Key points:**
- Client gets immediate `202 Accepted` response (not 200)
- Actual processing happens asynchronously after response
- Message broker is **explicit** (shown as participant)
- Each service publishes/consumes independently
- No synchronous waiting

### Failure Path: Processing Error

```mermaid
sequenceDiagram
    participant Client
    participant Orchestrator as Resolution<br/>Orchestrator
    participant Broker as Message Broker
    participant Engine as Entity Resolution<br/>Engine
    participant Repository as Entity<br/>Repository

    Client->>Orchestrator: resolve(entity)
    Orchestrator->>Repository: save_draft_entity()
    Repository-->>Orchestrator: draft entity + URI
    Orchestrator-->>Client: 202 Accepted + URI

    Orchestrator->>Broker: publish(resolution_request)
    Broker->>Engine: deliver(resolution_request)

    Engine-xEngine: Error: Invalid entity format
    Engine->>Broker: publish(resolution_error)

    Broker->>Orchestrator: deliver(resolution_error)
    Orchestrator->>Repository: mark_entity_as(UNRESOLVABLE)
    Repository-->>Orchestrator: acknowledged

    Note over Client: Client can poll /status/{URI}<br/>to see entity moved to UNRESOLVABLE
```

**Key points:**
- Engine publishes error event
- Orchestrator marks entity as unresolvable
- Client discovers failure via polling (see Step 3 below)
- No exception thrown to client (async = fire-and-forget)

### Client Polling for Results

```mermaid
sequenceDiagram
    participant Client
    participant Orchestrator
    participant Repository

    Client->>Orchestrator: GET /entities/{uri}?ifVersion=1
    Orchestrator->>Repository: get_entity(uri)
    Repository-->>Orchestrator: entity (version=1, status=DRAFT)
    Orchestrator-->>Client: 200 OK + entity v1

    Note over Client: Polling loop: client checks periodically

    Client->>Orchestrator: GET /entities/{uri}?ifVersion=1
    Orchestrator->>Repository: get_entity(uri)
    Repository-->>Orchestrator: entity (version=2, status=RESOLVED)
    Orchestrator-->>Client: 200 OK + entity v2 (RESOLVED)
```

**Key points:**
- `ifVersion` parameter lets client detect changes
- No need for client to wait or receive push notifications
- Client controls polling frequency
- Stateless queries (can hit any instance)

---

## Example 3: Orchestrator Coordinating Multiple Services

**Scenario**: Complex flow with multiple synchronous dependencies.

### Happy Path: Sequential Calls

```mermaid
sequenceDiagram
    participant Client
    participant Orchestrator
    participant Validator
    participant Resolver
    participant Cache
    participant DB

    Client->>Orchestrator: process_order(order_data)

    Orchestrator->>Validator: validate(order)
    Validator-->>Orchestrator: valid=true

    Orchestrator->>Cache: get_customer_preferences(id)
    Cache-->>Orchestrator: preferences (cache hit)

    Orchestrator->>Resolver: resolve_address(address)
    Resolver-->>Orchestrator: resolved_address

    Orchestrator->>DB: save_order(order, resolved_address)
    DB-->>Orchestrator: order_id

    Orchestrator-->>Client: 200 OK + order_id
```

**Key points:**
- Orchestrator coordinates sequence
- Cache used for frequently accessed data
- Database write last (after validations)
- Clear linear sequence of operations

### Failure Path: Validation Fails

```mermaid
sequenceDiagram
    participant Client
    participant Orchestrator
    participant Validator
    participant Cache

    Client->>Orchestrator: process_order(order_data)

    Orchestrator->>Validator: validate(order)
    Validator--xOrchestrator: ValidationError: invalid_amount

    Orchestrator--xClient: 400 Bad Request + error details

    Note over Orchestrator,Cache: Stops here - no further calls
```

**Key points:**
- Validation happens FIRST (fail-fast)
- No caching or database operations if validation fails
- Clear error returned to client
- Prevents cascading failures

---

## Example 4: Synchronous with Timeout & Retry

**Scenario**: Resilient pattern with timeout and automatic retry.

```mermaid
sequenceDiagram
    participant Client
    participant Service
    participant ExternalAPI as External API<br/>(unreliable)

    Client->>Service: get_data()
    Service->>ExternalAPI: request (timeout=5s)

    ExternalAPI--xService: Timeout (5 seconds elapsed)

    Note over Service: Retry attempt 1
    Service->>ExternalAPI: request (timeout=5s)
    ExternalAPI-->>Service: 200 OK + data

    Service-->>Client: 200 OK + data
```

**Key points:**
- Timeout set explicitly
- First attempt times out
- Automatic retry (circuit breaker pattern)
- Second attempt succeeds
- Client unaware of internal retries

---

## Example 5: Event-Driven Update Notification

**Scenario**: Service publishes event; multiple subscribers process independently.

```mermaid
sequenceDiagram
    participant Producer as Entity<br/>Repository
    participant Broker as Event Broker<br/>(Topic)
    participant Consumer1 as Search Index<br/>Updater
    participant Consumer2 as Cache<br/>Invalidator
    participant Consumer3 as Analytics<br/>Pipeline

    Producer->>Broker: publish(EntityUpdated)
    Broker-->>Producer: ack

    par Parallel Processing
        Broker->>Consumer1: EntityUpdated event
        Consumer1->>Consumer1: Update search index
        Consumer1-->>Broker: ack
    and
        Broker->>Consumer2: EntityUpdated event
        Consumer2->>Consumer2: Invalidate cache entry
        Consumer2-->>Broker: ack
    and
        Broker->>Consumer3: EntityUpdated event
        Consumer3->>Consumer3: Log for analytics
        Consumer3-->>Broker: ack
    end

    Note over Consumer1,Consumer3: All process in parallel<br/>independently
```

**Key points:**
- Event published once
- Multiple independent subscribers
- Parallel processing (not sequential)
- Each consumer processes at its own pace
- Broker coordinates (topics or subscriptions)

---

## Key Patterns to Recognize

### Pattern: Synchronous (Request-Reply)
- Caller blocks waiting for response
- Good for: Immediate feedback needed, strong consistency
- Bad for: High load, cascading failures
- Show with: Solid arrows `>>` and returns `-->>`

### Pattern: Asynchronous (Fire-and-Forget)
- Caller gets immediate ack; actual processing happens later
- Good for: Decoupled systems, high throughput, resilience
- Bad for: Immediate confirmation needed
- Show with: Message broker as explicit participant, separate async flow

### Pattern: Polling for Results
- Client checks for completion periodically
- Good for: Async processing, client controls timing
- Bad for: Frequent updates, low-latency needs
- Show with: Client making repeated GET requests, version/timestamp checks

### Pattern: Callback
- Service calls back when done (not shown here, but similar to event)
- Good for: Async without polling, server-driven updates
- Bad for: Firewall issues, client availability assumptions

---

## Template for Your Sequence Diagrams

```mermaid
sequenceDiagram
    participant A as Component A
    participant B as Component B
    participant C as Component C

    A->>B: Synchronous call
    B-->>A: Response

    A->>C: Async publish (no wait)
    C-->>B: Message delivery

    Note over B,C: Commentary or timing notes

    par Parallel block
        B->>C: Task 1
    and
        B->>A: Task 2
    end
```

**Syntax notes:**
- `A->>B` = call from A to B
- `A-->>B` = return from B to A
- `A-xB` = error/exception
- `Note over X,Y` = comment/annotation
- `par ... and ... end` = parallel blocks

---

## Questions to Ask About Your Sequence Diagram

1. **Is the flow clear?** Can someone read from top to bottom and understand?
2. **Is async explicit?** Is the message broker shown if async?
3. **Are both paths shown?** Happy path AND failure path?
4. **Are timeouts shown?** If synchronous, what happens on timeout?
5. **Who blocks?** Which participants wait for responses?
6. **Who's independent?** Which can happen in parallel?
7. **Is error handling visible?** What happens when something fails?
8. **Do participant names match your L3 components?** (for internal) or L2 containers (for integration)?
