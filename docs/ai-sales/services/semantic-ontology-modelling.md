# Modelling / ontology

## What it is

Every organisation has a set of things it talks about (customers, contracts, shipments, cases,
whatever the business runs on) and a set of words it uses for them. Usually those words drift:
"customer" means one thing to Sales and something narrower to Billing, and nobody wrote either
definition down. Modelling / ontology is the work of writing that shared meaning down once, as a
single living model: the concepts, their attributes, and how they relate to each other. That way
every system, report, and conversation in the organisation can point back to the same definition
instead of re-inventing it.

## The problem it solves

Two teams building two systems will, left alone, invent two different shapes for the same idea. The
symptom shows up later and expensively: a report that doesn't reconcile, an integration that breaks
because "order status" meant something different on each side, a new hire who can't tell which of
three "customer" tables is the real one. This service exists so a client stops paying that cost
repeatedly: the model is built once, kept up to date, and everything else (code, documentation,
data connections) is generated from it rather than hand-copied and left to drift.

## What's included

- Eliciting and defining the domain's entities, attributes, and relationships with the people who
  actually use the terms day to day.
- Choosing how the model is authored and rendered (directly in LinkML, or via a UML-first path)
  and documenting that choice rather than defaulting silently.
- Maintaining a terminology / glossary layer so every term in the model has one definition,
  referenced instead of restated.
- Generating the model's other representations (code contracts, diagrams, formal ontology
  artefacts) from the one source, on a repeatable, checkable basis rather than by hand.
- Applying the shared modelling conventions (naming discipline, reusable properties instead of
  duplicated attributes, stable identifiers for everything) so the model stays consistent as it
  grows.

Scoped per engagement, see the [Decision Package](../../../skills/decision-package/SKILL.md): this
building block can be the whole of a small engagement or one part of a larger build.

## What you get (deliverable)

A living model, versioned like code, that is the organisation's single definition of its own domain,
plus everything generated from it: a glossary of terms, diagrams that stay in sync with the
formal model, and (where the model drives software) the typed code contracts a development team
builds against.

## Owning skill(s)

- [`conceptual-modelling`](../../../skills/conceptual-modelling/SKILL.md) owns the living model
  itself, the model-source decision, and terminology management.
- [`linkml-engineering`](../../../skills/linkml-engineering/SKILL.md) owns turning that model into
  generated artefacts (code contracts, formal ontology files, documentation).
- [`modelling-conventions`](../../../skills/modelling-conventions/SKILL.md) owns the shared naming
  and identity discipline both of the above apply.

Verified by reading each skill's own file: all three are scoped to exactly this work, not adjacent
work being stretched to fit.

## Where it fits

This is the foundation the other five building blocks build on; see
[`engagement-lifecycle.md#the-outcome-semantic-layer-adoption`](../engagement-lifecycle.md#the-outcome-semantic-layer-adoption)
for how it composes into the whole Semantic Layer.
