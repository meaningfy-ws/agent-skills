---
name: linkml-engineering
description: The operational LinkML craft, downstream of an existing model or spec — never greenfield. Use to derive a LinkML schema from a UML model, a text spec, a model2owl output, or another existing model; to author/refine it (reusable slots, the URI-as-datatype artifice, implicit class_uri/slot_uri, enums, schema-level constraints); to generate the full target set (Pydantic/JSON Schema/OWL/SHACL/TS/SQL) with custom templates and make-target automation including diagrams; and to establish LinkML quality gates. Trigger on "write/derive a LinkML schema", "generate models/OWL/SHACL from LinkML", "custom Pydantic template", "LinkML quality gates", "per-module generation", "make generate-models". Reuses modelling-conventions for generic craft; defers the model concept to conceptual-modelling. Not an ontology-authoring skill.
license: Apache 2.0
metadata:
  category: engineering
---

# LinkML Engineering

## Overview

LinkML is the **pivot artefact** in Meaningfy's single-source-of-specifications approach: from one
hand-authored schema, a deterministic toolchain renders Pydantic, JSON Schema, OWL, SHACL, JSON-LD,
TypeScript, SQL, docs, and diagrams. This skill owns the *engineering* of that pivot — how to run
LinkML in a layered project without it becoming a foot-gun.

It is deliberately **not a greenfield schema-authoring skill**. LinkML is always a *follow-up*
representation of a model that already exists (a UML model, a text specification, a model2owl output,
another existing model). If no model exists yet, that is `conceptual-modelling`'s job first.

This skill **reuses** [`../modelling-conventions/SKILL.md`](../modelling-conventions/SKILL.md) for the
representation-agnostic craft (reusable properties, URI-everywhere, anti-patterns, naming) and adds the
**LinkML-specific mechanics** that realise those principles. It is not an ontology-authoring skill —
but it keeps ontologies in mind, because a well-authored schema must generate complete, correct OWL and
SHACL even when the delivered target is JSON or Python.

## The workflow: derive → author → generate & guard

### 1. Derive — LinkML from an existing source

Turn the upstream artefact into an initial schema. There is a distinct entry point per input kind (UML,
text spec, model2owl output, existing model). See
[`references/deriving-linkml.md`](references/deriving-linkml.md).

### 2. Author / refine — LinkML mechanics atop the shared conventions

Apply the shared conventions through LinkML's own constructs: top-level reusable `slots:`, the
URI-as-datatype artifice, minted `prefixes`/`default_prefix` with **implicit** `class_uri`/`slot_uri`,
`enums` over free strings, and constraints declared in the schema. SEMIC and model2owl conventions and
checkers are the cited authority for the URI/naming/datatype slice. See
[`references/authoring-mechanics.md`](references/authoring-mechanics.md).

**Complete OWL/SHACL is a first-class outcome, not a side effect.** Because every class and property is
URI-identified, the schema can render *complete* OWL and SHACL — the elements that MUST be present for
each are listed in [`references/owl-shacl-completeness.md`](references/owl-shacl-completeness.md). Author
for that completeness even when the project only ships JSON/Python/DB, so the semantic option stays open.

### 3. Generate & guard

Render the targets deterministically, **outside the LLM path**, via `make`-driven generation with custom
templates (a strict project Pydantic base, custom code generation for other languages) and per-module
artefact layout. Then establish quality gates — **chosen with the user, not imposed**. See
[`references/generation-and-templates.md`](references/generation-and-templates.md) and
[`references/quality-gates.md`](references/quality-gates.md).

## The working loop

1. Locate the schemas dir and the `make` target that generates from it — never invoke generators ad hoc.
2. Make the change in **YAML only** (never hand-edit a generated file), respecting the conventions.
3. Lint the schema (warnings not muted); fix what it reports.
4. Regenerate the targets.
5. Review the generated diff — it should touch only what you expect.
6. Validate the inline examples; run the project's tests.
7. Commit the YAML **and** the regenerated artefacts together, never separately.

## Boundary & Related Skills

**This skill OWNS:** the operational LinkML discipline — deriving LinkML from an existing source;
LinkML-specific authoring mechanics (reusable `slots:`, URI-as-datatype, implicit `class_uri`/`slot_uri`,
enums, schema-level constraints); complete-and-correct OWL/SHACL generation; custom generator templates
and `make`-target transformation automation (including diagrams); per-module artefact generation; and
the guided quality-gate process.

**This skill REUSES:**
- Generic modelling craft (reusable-property and URI-everywhere *principles*, anti-patterns, naming,
  guardrails) → [`../modelling-conventions/SKILL.md`](../modelling-conventions/SKILL.md). This skill
  states the LinkML *mechanism*; it does not restate the principle.

**This skill DELEGATES:**
- The representation-agnostic model, UML conceptual modelling, terminology, and the LinkML-vs-model2owl
  **source decision** → [`../conceptual-modelling/SKILL.md`](../conceptual-modelling/SKILL.md).
- Where the generated Pydantic/JSON Schema contract is *consumed* (a service's `entrypoints/api`) →
  [`../cosmic-python/SKILL.md`](../cosmic-python/SKILL.md).
- Scaffolding the gates/automation/per-module layout into a repo → `project-setup` (conditional on the
  project using LinkML).

**Conditional:** product-development projects that use LinkML. A project modelling only in OWL/UML
without a LinkML pivot does not need this skill.

**Related:** `modelling-conventions`, `conceptual-modelling`, `architecture`, `cosmic-python`,
`project-setup`.
