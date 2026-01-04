# UML Component Diagram Checklist

Use this checklist when validating or creating a UML Component diagram (typically L3 - internal structure within a container).

## Scope & Clarity
- [ ] Diagram addresses one container only (clear L3 scope)
- [ ] Each component has one clear responsibility
- [ ] Component names describe responsibility, not implementation (e.g., "Validator", "Adapter", "Orchestrator")

## Interactions & Interfaces
- [ ] All component-to-component interactions go through explicit interfaces
- [ ] Each dependency/interface is labelled with interaction style (REST, Async Event, In-Process)
- [ ] Async communication is NOT disguised as synchronous calls
- [ ] No direct component-to-component calls without interface mediation

## Structure Discipline
- [ ] No internal orchestration logic visible (that's L2+)
- [ ] No database specifics or persistence details
- [ ] No technology choices leaking in (e.g., "REST Adapter" is OK; "Spring Bean" is not)
- [ ] No behavioral details (sequencing, state machines)

## Red Flags
- ❌ Direct component calls without interfaces
- ❌ Orchestration mixed with execution components
- ❌ Components named after technology ("HTTP Handler", "Database Layer")
- ❌ Relationships without clear interaction style
- ❌ Too many components (> 6-8 suggests L4 detail)
- ❌ External system concerns inside container boundary

## Reachability & Contracts
- [ ] If claiming replaceability, interface ownership is explicit
- [ ] Incoming interfaces are owned by consumer or orchestrator
- [ ] Outgoing interfaces are owned by provider/dependency

## Questions to Ask
1. Can I describe what each component does in one sentence?
2. Does every relationship have a clear interaction style?
3. Would this change if I replaced one component?
4. Is any orchestration logic visible (if yes, move to L2 or sequence diagram)?
