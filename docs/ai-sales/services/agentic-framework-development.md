# Agentic framework development

## What it is

An "agent," in this context, is software built on a large language model that can look things up,
take actions, and carry out multi-step work on a client's behalf: answering a question by actually
querying the client's systems, or completing a task rather than just describing how to do it.
Agentic framework development is the work of building those agents for a client, grounded in their
own semantic model (see [modelling / ontology](semantic-ontology-modelling.md)) so the agent reasons
using the client's real, shared definitions instead of guessing at them.

## The problem it solves

A generic AI assistant that hasn't been connected to an organisation's actual data and definitions
either refuses to answer specific questions or, worse, answers confidently and wrongly. This service
exists so a client can hand real, bounded work to an AI agent, equipped with the guardrails and
grounding that make its answers and actions trustworthy, instead of getting either an over-cautious
chatbot or an ungrounded one.

## What's included

**No skill in this catalogue owns agentic-product development.** Searching every skill for
agentic-framework, multi-agent, or agent-development content surfaced only
[`guardrails`](../../../skills/guardrails/SKILL.md), and that skill is scoped to a different job: it
governs the safety of Meaningfy's *own* internal build-loop agents (decision bounds, output
validation, prompt-injection defence), not the design of an agentic product for a client. Until a
skill exists for that, this block is delivered as bespoke engineering, borrowing `guardrails`'
safety practices and the general software-development skills (see
[software-development.md](software-development.md)) rather than any purpose-built method for agent
products.

## What you get (deliverable)

Not yet standardised. Once an agentic-framework skill exists, this section states the concrete
artefact (e.g. a running agent with its scoped tool access, decision bounds, and evaluation results).
Today, the deliverable is whatever is agreed case by case in the engagement's Decision Package.

## Owning skill(s)

**No owning skill exists.** [`guardrails`](../../../skills/guardrails/SKILL.md) was read in full to
check the fit and confirm the gap: it applies guardrails to *any* agentic step in Meaningfy's own
build loop, a real and reusable safety practice, but it is not a skill for scoping or building a
client-facing agent product. Naming it as this block's owner would overstate what it actually does.

## Where it fits

Agentic framework development is one of the six building blocks the Semantic Layer decomposes into;
see
[`engagement-lifecycle.md#the-outcome-semantic-layer-adoption`](../engagement-lifecycle.md#the-outcome-semantic-layer-adoption).
Meaningfy can still scope and deliver this today; only the dedicated build method is missing.
