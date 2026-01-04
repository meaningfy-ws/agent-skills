# BPMN Process/Collaboration Diagram Checklist

Use this checklist when validating or creating a BPMN diagram for business workflows or choreography.

## Purpose & Scope
- [ ] Diagram shows a complete end-to-end business process or choreography
- [ ] Primary audience is stakeholders/business users (not technical)
- [ ] One clear workflow from start to end

## Elements (What Should Be Present)
- [ ] Pools (one per independent actor or system)
- [ ] Swim lanes (optional within pools, for different roles)
- [ ] Tasks (business-meaningful steps, not technical sub-steps)
- [ ] Gateways (decision points based on business logic)
- [ ] Events (start, end, intermediate states/triggers)

## Relationships (What Should Connect)
- [ ] Message flows ONLY between pools (never within a pool)
- [ ] Sequence flows only within a pool
- [ ] Messages represent business events or data exchange
- [ ] Each message is named for business meaning ("Order Placed", "Payment Approved")

## Business Realism
- [ ] All tasks are business-meaningful (something someone would understand)
- [ ] Task names describe business action ("Validate Address", "Calculate Discount")
- [ ] No internal IT procedures disguised as tasks
- [ ] No single-step detail ("Call API", "Write to Database")

## Path Completeness
- [ ] Happy path (normal case) is shown explicitly
- [ ] At least one failure or timeout path shown separately
- [ ] Both paths lead to clear end state
- [ ] No ambiguous or "someday maybe" paths

## What Must NOT Be Included
- ❌ Message flows inside a single pool
- ❌ Internal IT procedures or algorithms
- ❌ Technical implementation details
- ❌ Low-level steps (database operations, API calls as primary tasks)
- ❌ Technology choices
- ❌ Swim lanes used to show technical layers
- ❌ More than 2-3 decision points (if complex, split to multiple diagrams)

## Red Flags
- ❌ Tasks with IT jargon ("REST call", "Database insert", "Cache lookup")
- ❌ Message flows inside a pool (use sequence diagram for internal interaction)
- ❌ Pools representing technical layers (API, Database, Cache)
- ❌ Too many tasks (> 10-12 suggests multiple processes)
- ❌ No failure paths shown
- ❌ Unclear which pool is responsible for each step
- ❌ Messages without business meaning

## Path Definition Quality
- [ ] Happy path is complete and unambiguous
- [ ] Failure/timeout path is explicit (not assumed)
- [ ] Each path has a clear end event
- [ ] Paths don't merge mysteriously
- [ ] Timing assumptions are clear (sync vs async wait)

## Questions to Ask
1. Could a business person read and approve this diagram?
2. Does it show what needs to happen, not how to implement it?
3. Are all message exchanges between independent actors clear?
4. What happens when something goes wrong? (visible in diagram?)
5. Could I trace a complete order/request through happy and failure paths?
