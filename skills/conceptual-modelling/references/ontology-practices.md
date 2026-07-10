# Ontology-engineering practices (concept level)

The conceptual model is an ontology in the engineering sense: identified concepts with stable meaning.
This file owns the **concept-level policy** — the decisions made once, at the model level. The
representation-agnostic *conventions* (reusable properties, URI-everywhere, naming, vocabulary reuse as
a principle) live in [`../../modelling-conventions/SKILL.md`](../../modelling-conventions/SKILL.md); the
LinkML *mechanics* that realise them (minted `prefixes`, implicit `class_uri`/`slot_uri`, the
URI-as-datatype artifice) live in `linkml-engineering`. This file states policy and delegates both.

## Stable-IRI policy

The *principle* that everything is identified by a stable URI, implicit by default, is a shared
convention — see
[`../../modelling-conventions/references/naming-and-identity.md`](../../modelling-conventions/references/naming-and-identity.md).
The **policy decisions** are owned here:

- **Mint a base namespace per model** you own (e.g. `https://data.meaningfy.ws/<domain>/`) and declare
  it once. Choosing the namespace is a model-level decision, not a per-element one.
- **Identifiers are opaque and permanent**; do not encode mutable facts (version, owner, location) into
  the local name. Minted at authoring time, human-readable, like the other golden-thread IDs
  (`EPIC-`, `ADR-`, `R<n>` — see [`../../../spine/golden-thread.md`](../../../spine/golden-thread.md)).
- **Cross-repo citation.** When the model lives in its own repo, downstream code and specs cite these
  IRIs — the cross-repo rung of the golden thread.

## Modularity

- **One concern per schema/module**; separate the core domain from project-specific extensions so a
  shared model stays clean and consumers extend it without forking. Mirror the bounded contexts the
  architecture defines. (The LinkML `imports:` mechanism and per-module output are owned by
  `linkml-engineering`.)

## Vocabulary reuse

Preferring published vocabularies over invented terms is a shared *principle* (see
`modelling-conventions`). The model-level decision owned here is **which** vocabularies a given model
aligns to — `schema.org`, Dublin Core, SKOS, FOAF, an EU reference ontology, a domain standard — and
recording that alignment so it survives into the generated OWL. Only mint a new term when no suitable
published one exists.

## The source decision — LinkML vs model2owl

This is an **explicit decision point, never silently defaulted**, and it is owned here:

| Use… | When |
|------|------|
| **LinkML directly** (default) | The team authors the schema in LinkML; fastest path to the wired targets. |
| **model2owl first** | The team models the domain in **UML**. model2owl generates LinkML artefacts (and has strong OWL/SHACL/HTML generators of its own), which then drive the LinkML generators. model2owl becomes a **prerequisite stage** of generation. |
| **Other OWL-first tooling** (Protégé, SHACL-first) | An existing ontology asset already lives in OWL; document the chosen tool as a named pattern and bridge to LinkML if Pydantic/JSON Schema targets are also needed. |

We do **not** abstract these behind a source-adapter interface (YAGNI). Pick one consciously per project.
Once chosen, the LinkML execution (deriving, authoring, generating) is owned by
[`../../linkml-engineering/SKILL.md`](../../linkml-engineering/SKILL.md); configuring model2owl itself is
a future dedicated skill.
