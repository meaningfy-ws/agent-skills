# ArchiMate L2 Container/Application Cooperation Checklist

Use this checklist when validating or creating an ArchiMate Application Cooperation view (L2 - runtime deployable units).

## Scope & Clarity
- [ ] Each element represents one runtime deployable unit (container)
- [ ] Each container has one clear runtime responsibility
- [ ] Container names describe responsibility ("Entity Repository", "Resolution Engine", "API Gateway")
- [ ] Diagram shows all major inter-container communication paths

## Elements (What Should Be Present)
- [ ] Application Components (one per container/runtime unit)
- [ ] Application Services (optional but clean - each represents a capability realised by containers)
- [ ] Application Interfaces (where contract/interaction modality matters)
- [ ] All containers that communicate with each other

## Relationships (What Should Connect)
- [ ] Realization: Container realises Service (what does this container provide)
- [ ] Serving: Service serves other containers or external systems
- [ ] Flow: shows sync or async interaction only (no detail on protocol)
- [ ] No orchestration logic or workflow steps

## Critical L2 Discipline
- [ ] No internal orchestration details visible
- [ ] No step sequencing or pre/post conditions
- [ ] No pipeline stages or workflow steps
- [ ] No database specifics or persistence concerns
- [ ] No protocol details (Kafka vs RabbitMQ, REST vs gRPC)
- [ ] No data objects or schema concerns
- [ ] Structure only, no behavior

## Interaction Quality
- [ ] Each Flow relationship is clearly sync OR async (not ambiguous)
- [ ] If critical, async is explicit (topic, queue, event stream name)
- [ ] No multi-step interactions in single relationship
- [ ] Contract ownership is clear (which side owns the interface definition)

## What Must NOT Be Included
- ❌ Internal components within a container
- ❌ Application Functions, Processes, or Events
- ❌ Data Objects
- ❌ Pre/post conditions or task sequences
- ❌ Protocol specifics
- ❌ Orchestration logic
- ❌ Technology choices (Kafka, Redis, REST as primary elements)

## Red Flags
- ❌ Containers named after technology ("Kafka", "Redis Cache", "REST API")
- ❌ Workflow/pipeline steps as containers
- ❌ Multiple responsibilities per container
- ❌ Request processing details embedded
- ❌ Data schema or business logic visible
- ❌ Unclear sync vs async communication
- ❌ Relationships with comma-separated labels

## Replaceability Check
- [ ] If a container is claimed "pluggable" or "replaceable":
  - Is the interface boundary explicit?
  - Is interface ownership clear (who defines it)?
  - Is the contract specified (OpenAPI/AsyncAPI)?

## Questions to Ask
1. Could I deploy/undeploy each container independently?
2. Does each container have one reason to change?
3. Are all inter-container contracts clear?
4. Could someone implement each container in a different language?
5. Is any business logic or orchestration visible (if yes, move to L3)?
