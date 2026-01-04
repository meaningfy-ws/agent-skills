# UML Sequence Diagram Checklist

Use this checklist when validating or creating a Sequence diagram (L3/L4 - interaction behaviour over time).

## Purpose & Scope
- [ ] Diagram shows interaction between specific participants (components, services, or actors)
- [ ] Clear start and end points (request → response or event → processing)
- [ ] One clear interaction scenario (not trying to show everything at once)
- [ ] Realistic timing: sync vs async is visible

## Participants (Who's Involved?)
- [ ] Each participant is a real component, service, or external system
- [ ] NOT: generic roles ("service", "API") - be specific
- [ ] Participants match L3 component structure or L2 containers (depending on scope)
- [ ] External systems clearly identified

## Happy Path (Normal Case)
- [ ] Clear sequence of calls/messages from first participant to last
- [ ] Each message has clear sender and receiver
- [ ] Response/acknowledgement shown (or explicitly asynchronous)
- [ ] Conditions for success are clear
- [ ] End state is explicit (what's completed, what's not)

## Failure Path (At Least One)
- [ ] At least one failure or timeout scenario shown
- [ ] Failure shown explicitly (timeout after X seconds, error response, etc.)
- [ ] How system recovers (retry, fallback, abort)
- [ ] Failure doesn't leave system in ambiguous state

## Synchronous vs Asynchronous - EXPLICIT
- [ ] If sync: solid arrow `→`, sender waits for response
- [ ] If async: message broker/queue shown as participant (if applicable)
- [ ] Async: sender gets ack, actual work happens later (202 Accepted pattern)
- [ ] Polling shown if client waits for async result (GET with version/timestamp)
- [ ] No hidden assumptions about timing

## Message Quality
- [ ] Each message has clear name/label (business meaningful or technical operation)
- [ ] Parameters/data shown (or at least what matters for understanding)
- [ ] Response/return values explicit (or noted as asynchronous/fire-and-forget)
- [ ] Errors shown explicitly (`--x` for error/exception)

## Blocking & Independence
- [ ] Clear which participants block (wait for response)
- [ ] Clear which can proceed independently
- [ ] If parallel: shown with `par ... and ... end` blocks
- [ ] Timing assumptions visible (can reader understand who waits for whom?)

## Anti-Patterns & Red Flags
- ❌ Participants that don't exist in L3/L2 (too abstract or too detailed)
- ❌ Happy path without failure path (unrealistic)
- ❌ Sync shown as async or vice versa (timing ambiguity)
- ❌ Missing broker/queue in async scenario (implied magic)
- ❌ Too many messages (> 10-15 suggests too complex; split into multiple diagrams)
- ❌ Vague message names ("call", "message", "process")
- ❌ Unclear response or timeout behaviour
- ❌ Infinite loops or unclear termination

## Validation Against Components
- [ ] Does sequence match L3 component interfaces?
- [ ] Are all dependencies shown in the component diagram reflected here?
- [ ] Could someone implement each component based on what they see?
- [ ] Are async contracts (topics, queues) visible?

## Questions to Ask
1. **Can I understand the flow?** Read top to bottom - is it clear?
2. **What happens on timeout/failure?** Is it shown?
3. **Who waits, who proceeds?** Is blocking visible?
4. **Is async explicit?** Broker shown? Acknowledgement pattern clear?
5. **Do these participants exist in L3?** Or am I mixing levels?
6. **What are success/failure criteria?** Are both paths shown?
7. **Could someone code this?** Is detail sufficient to guide implementation?
8. **Is there a better notation?** (e.g., L3 component diagram if showing structure, not interaction)
