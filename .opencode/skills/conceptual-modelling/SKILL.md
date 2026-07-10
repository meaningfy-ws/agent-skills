---
name: conceptual-modelling
description: Build and evolve a living, representation-agnostic conceptual model for a product (programming) project — the domain's entities, attributes, relationships, and meaning — and choose how it is rendered. Use to model the domain, do conceptual data modelling in UML, run ontology-engineering at the concept level (stable-IRI policy, vocabulary reuse), decide the model *source* (LinkML directly vs model2owl-first), set up a conceptual model, or run terminology/definitions/glossary management. Trigger on "model the domain", "conceptual/UML data model", "set up conceptual model", "which model source", "ontology/terminology management", "ubiquitous language glossary". For the LinkML craft itself (authoring, generation, gates) see linkml-engineering; for generic modelling conventions see modelling-conventions. Conditional: applies to product-development repos that build software; a doc-only/non-product repo does not need it.
license: Apache 2.0
metadata:
  category: engineering
---

# Conceptual Modelling

> **Provisional pending the first-engagement gate.** This skill's consulting-facing depth will be refined
> after the first real engagement that builds a domain model; treat the wiring here as the floor.

## Overview

The **conceptual model** is the single, living, representation-agnostic definition of the domain:
entities, attributes, relationships, and their meaning. It is *generative* — code, contracts, and
documentation are derived **deterministically** from it, never hand-maintained in parallel. The
generation layer is a `make generate-models`-style bridge that stays **outside the LLM path** (the
principled answer to spec-drift and failed model-driven development): the LLM authors the *source*,
a deterministic toolchain renders the *targets*.

**Conditional.** This skill applies only to **product-development (programming) projects** — repos
that build software with a domain to model. A documentation-only or non-product repo does not need a
conceptual model and should not scaffold one.

This skill **owns the model**; it does not own system topology, code layering, or normative
requirements — see [Boundary & Related Skills](#boundary--related-skills).

## Where the model lives (two modes)

The model is a first-class asset with a home of its own. Pick the mode explicitly:

- **In-project `model/` directory (default).** This is what `project-setup` scaffolds by default
  (EPIC-09): the model lives beside the code it generates, versioned with the repo. Generated
  artefacts land under the relevant package (e.g. `models/`, see `cosmic-python`) via
  `make generate-models`. Use this for a model owned by one product.
- **Own repo / imported library.** For a model shared across repos, give it its **own repository**
  and import it as a dependency (LinkML schema published as a package, or generated artefacts
  released as a versioned library). Each consuming repo regenerates from the pinned version.

**Golden-thread implication.** Model entities carry stable IDs (see ontology practices). When the
model lives in its own repo, downstream code and specs **cite those entity IDs across repos** — the
cross-repo rung of the golden thread (see [`../../spine/golden-thread.md`](../../spine/golden-thread.md),
which notes cross-repo IDs are convention-only for now).

## The source: LinkML by default, not by default-only

**LinkML is the wired default source** for the model. It is declarative, generates many targets, and
is the canonical domain-definition format the `architecture` skill already references for contracts.

Choosing the source is an **explicit decision point — never silently defaulted**:

- **LinkML (default)** — author the schema directly; drives all generators below.
- **model2owl** — a UML-driven ontology-engineering path with strong **OWL, SHACL, and HTML**
  generators. In some projects model2owl is used to *generate LinkML artefacts*, which then drive
  the other generators — so **model2owl can be a prerequisite step *before* the LinkML generators**,
  not an alternative to them. Surface this ordering when a project models in UML.
- **Other ontology-engineering tooling** exists (Protégé/OWL-first, SHACL-first, etc.); document the
  chosen one as a named pattern.

We deliberately do **not** build a source-adapter abstraction (YAGNI) — alternatives are documented
as named patterns, not wired behind an interface. The **source decision** and the concept-level
ontology policy are owned here (see [`references/ontology-practices.md`](references/ontology-practices.md));
the LinkML craft that executes on the chosen source is owned by `linkml-engineering`.

## Deterministic multi-target generation (the concept)

From the chosen source, code, contracts, and documentation are generated **deterministically and
outside the LLM path** — reproducible, diffable, CI-checkable. This skill owns *that this is how the
model becomes artefacts*; it does **not** own the LinkML authoring, the generator wiring, the custom
templates, or the quality gates — those belong to
[`../linkml-engineering/SKILL.md`](../linkml-engineering/SKILL.md). The semantic core (Pydantic, JSON
Schema, OWL, SHACL) and the enable-on-demand targets are catalogued there; see
[`references/generators.md`](references/generators.md) for the pointer.

**The seam to `cosmic-python`.** The model **owns the contract**; the generated Pydantic/JSON Schema
*is* the contract. A service's `entrypoints/api` **consumes** the generated contract — it does not
redefine the domain. This skill owns the source side of that seam; `linkml-engineering` owns the
generation that crosses it.

## The craft around the model

A model is more than a schema. Two adjacent practices are part of the discipline:

- **Diagrams alongside the formal model.** Generate/maintain **Mermaid** (and other) diagrams from
  or beside the model so the human view and the formal view stay in step. Architecture's C4/UML
  class diagrams are a *consumer* of the same domain concepts — keep them coherent, but the formal
  source of truth is the model.
- **Terminology, disambiguation, and definitions management.** The glossary / ubiquitous-language
  layer: every model class is a term with a definition, and OpenSpec specs reference those classes
  as **ubiquitous language**. See [`references/terminology-management.md`](references/terminology-management.md).

## Boundary & Related Skills

**This skill OWNS:** the living conceptual model (representation-agnostic source of domain truth);
conceptual data modelling in UML; the concept-level ontology policy (stable-IRI *policy*, modularity,
vocabulary-reuse *principle*); the **model-source decision** (LinkML-direct vs model2owl-first); and
terminology / definitions / glossary management (ubiquitous language).

**This skill REUSES:**
- Representation-agnostic modelling craft (reusable-property and URI-everywhere *principles*, naming,
  anti-patterns, guardrails) → [`../modelling-conventions/SKILL.md`](../modelling-conventions/SKILL.md).
  This skill applies those conventions; it does not restate them.

**This skill DELEGATES:**
- The LinkML craft — authoring, generation, custom templates, quality gates, per-module output →
  [`../linkml-engineering/SKILL.md`](../linkml-engineering/SKILL.md). This skill picks the source and
  owns the model; `linkml-engineering` executes the LinkML.
- System/solution architecture — C4 levels, ADRs, the contract-first *order of artifacts* →
  [`../architecture/SKILL.md`](../architecture/SKILL.md). Architecture authors *which* contracts
  exist; this skill owns the domain model that backs them.
- Code layering and what consumes the generated contract →
  [`../cosmic-python/SKILL.md`](../cosmic-python/SKILL.md). `entrypoints/api` *consumes* the
  generated contract; this skill owns the model that produces it.
- Normative requirements and the spec spine → the spine specs (see
  [`../../spine/README.md`](../../spine/README.md)). Model classes are *ubiquitous language*
  that specs reference; specs state the *rules*.

**Conditional:** product-development (programming) projects only — see the Overview.

**Related:** `modelling-conventions`, `linkml-engineering`, `architecture`, `cosmic-python`.
