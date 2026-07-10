---
name: modelling-conventions
description: The shared, representation-agnostic modelling craft reused across the modelling skills — naming discipline, modelling anti-patterns, and the guardrails a modeller follows while working, plus the two load-bearing principles (decouple attributes into reusable first-class properties; identify everything by a stable URI, implicit by default). Use when authoring or reviewing ANY model regardless of representation (conceptual, UML, LinkML, ontology). Trigger on "modelling conventions", "naming conventions for a model", "modelling anti-patterns", "reusable properties/slots", "should this attribute be shared", "URI/identity discipline", "review this model for smells". This is the cosmic-python-style reuse layer for modelling — cited by conceptual-modelling and linkml-engineering, never restated by them.
license: Apache 2.0
metadata:
  category: engineering
---

# Modelling Conventions

## Overview

This is the **shared modelling-craft layer**: the conventions, anti-patterns, and guardrails that are
true of a *good model* whatever representation renders it — a conceptual model, a UML class diagram, a
LinkML schema, or an OWL ontology. It exists for the same reason `cosmic-python` exists: one home for
the craft that many skills reuse, so the rules are stated once and cited everywhere.

It carries **principles, not mechanics**. The concrete syntax that realises a principle in a given
representation (LinkML `slots:`, UML association classes, OWL `owl:ObjectProperty`) belongs to the
skill that owns that representation — this skill states *what good looks like* and *why*, and delegates
*how* to the consuming skill.

Two principles here are load-bearing across every downstream skill; the rest of the craft supports them.

## The two load-bearing principles

### 1. Decouple attributes from classes — model them as reusable, first-class properties

An attribute is not owned by a class. It is a **concept in its own right** — a property with its own
meaning, definition, and identity — that classes *reference*. Define it once; reference it from every
class that needs it. The moment the same attribute (same meaning) appears on a second class, redefining
it inline is duplication that will drift.

Why it matters: reuse keeps meaning single-sourced, makes the model smaller and more consistent, and is
exactly what lets a formal/semantic target (OWL/SHACL) treat properties as the first-class citizens they
already are. See [`references/naming-and-identity.md`](references/naming-and-identity.md).

### 2. Identify everything by a stable URI — implicit by default

Every modelled element — class, property, enumeration value — is identifiable by a **stable URI**,
minted once at authoring time and never changed when the element is renamed or moved. Keep it
**implicit**: derive it from a minted namespace + the element's name rather than writing an explicit URI
literal, and make it explicit only when a specific value is required (reusing a published vocabulary
term, for instance).

Why it matters: a model where everything is identified can be rendered to OWL and SHACL **naturally and
completely** — no retrofitting identity later. Identity is a modelling decision, not a serialization
detail.

## The craft around them

- **Naming** — intention-revealing, consistent, singular-noun classes; the model's names become the
  project's ubiquitous language. Details and the per-representation casing table:
  [`references/naming-and-identity.md`](references/naming-and-identity.md).
- **Anti-patterns** — free strings where a controlled set belongs, god-classes, validation buried in
  code instead of the model, flattening everything onto one class. See
  [`references/anti-patterns.md`](references/anti-patterns.md).
- **Editor guardrails** — the checks a modeller applies *while working*, before generating anything:
  [`references/editor-guardrails.md`](references/editor-guardrails.md).

## Boundary & Related Skills

**This skill OWNS:** representation-agnostic modelling conventions, modelling anti-patterns, the
editor-guiding guardrails, and the two principles above (reusable properties; URI-everywhere) stated as
principles.

**This skill DELEGATES:**
- The living conceptual model, UML conceptual data modelling, terminology, and the model-source
  decision → [`../conceptual-modelling/SKILL.md`](../conceptual-modelling/SKILL.md).
- LinkML mechanics that realise these principles (top-level `slots:`, the URI-as-datatype artifice,
  generation) → [`../linkml-engineering/SKILL.md`](../linkml-engineering/SKILL.md).
- Representation-specific mechanics generally (UML profiles, OWL axioms) → the skill owning that
  representation. Nothing representation-specific belongs here.

**Related:** `conceptual-modelling`, `linkml-engineering`, `architecture`, `cosmic-python` (the same
reuse-layer pattern for code).
