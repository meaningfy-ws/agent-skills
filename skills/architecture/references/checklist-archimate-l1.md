# ArchiMate L1 Context Diagram Checklist

Use this checklist when validating or creating an ArchiMate Context/Cooperation view (L1 - system boundary and external interactions).

## Scope & Boundaries
- [ ] System boundary is explicit and clear
- [ ] All major external systems are shown
- [ ] All primary user/actor types are shown
- [ ] One diagram, one clear context view

## Elements (What Should Be Present)
- [ ] Business Layer: Business Actors (people, organizations, roles only)
- [ ] Application Layer: Application Component (system under design)
- [ ] Application Layer: Application Component (each external system)
- [ ] Application Layer: Application Services (named, externally visible capabilities)

## Relationships (What Should Connect)
- [ ] Serving relationships only (Service → Actor/External System)
- [ ] Each relationship means: "this actor/system benefits from this capability"
- [ ] No orchestration or workflow relationships
- [ ] No technical channels or protocols shown

## What Must NOT Be Included
- ❌ Internal structure or components
- ❌ Business processes or workflows
- ❌ Technology details (Kafka, REST, HTTP)
- ❌ Comma-separated labels on relationships ("resolve, validate, store")
- ❌ Application Functions, Processes, or Events
- ❌ Data Objects or schema details
- ❌ Behavioral concerns or sequencing

## Service Definition Quality
- [ ] Each service has a business-meaningful name
- [ ] Service names describe capability, not implementation ("Entity Resolution", not "Query Engine")
- [ ] Services are stable across design iterations
- [ ] No technical jargon in service names

## Red Flags
- ❌ Actors with detailed roles/responsibilities (too much detail)
- ❌ Multiple services on one relationship (use explicit Service elements)
- ❌ Comma-separated labels ("validates, transforms, stores")
- ❌ Internal components visible
- ❌ Workflows or process steps
- ❌ Protocol or technology references
- ❌ Data objects or persistence details

## Questions to Ask
1. Can a non-technical person understand this diagram?
2. Does each service describe a business capability?
3. Are boundaries between "our system" and "external systems" crystal clear?
4. Could I explain this in 2-3 sentences?
