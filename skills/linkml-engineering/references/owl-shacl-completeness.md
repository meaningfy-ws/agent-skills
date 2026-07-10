# Complete and correct OWL & SHACL generation

Complete OWL and SHACL are a **first-class outcome** of a well-authored schema, not a side effect. They
are achievable precisely because every class and property is URI-identified (implicit by default — see
[`authoring-mechanics.md`](authoring-mechanics.md)). Author for this completeness **even when the project
only ships JSON/Python/DB**, so the semantic option stays open at no extra cost.

Verify the generated artefacts against the model2owl checkers
(<https://docs.ted.europa.eu/M2O/latest/checkers/model2owl-checkers.html>) and LinkML's own
`gen-owl`/`gen-shacl` output — this file lists what MUST be present for each to be *usable*.

## OWL — MUST be present

- **An ontology declaration** — `owl:Ontology` with a stable ontology IRI (from the minted namespace)
  and, ideally, version/metadata (label, description, `owl:versionIRI`).
- **A class axiom per class** — each LinkML class → an `owl:Class` with its resolved IRI.
- **Property axioms per slot** — each slot → an `owl:ObjectProperty` (range is a class) or
  `owl:DatatypeProperty` (range is a literal type). URI-valued slots (`uriorcurie`) are object
  properties, not datatype properties — this is why the URI-as-datatype artifice matters.
- **Domain and range** — `rdfs:domain` / `rdfs:range` on properties, so reasoners and consumers can
  align data. A property with no range is incomplete.
- **Subclass axioms** — `rdfs:subClassOf` from every `is_a`; `owl:equivalentClass`/`owl:disjointWith`
  only where the model states them.
- **Labels and definitions** — `rdfs:label` and `rdfs:comment`/`skos:definition` from each `description:`.
  Empty descriptions produce empty semantics — hence "definition on every element".
- **Enumerations** — closed value sets as the chosen pattern (individuals with `owl:oneOf`, or a SKOS
  concept scheme), each value carrying its `meaning:` IRI where one exists.
- **Vocabulary mappings** — `owl:equivalentClass`/`owl:equivalentProperty` (or `skos:exactMatch`) from
  every `mappings:`/`exact_mappings:`, so reuse of published terms survives into the ontology.

## SHACL — MUST be present

- **A node shape per class** — `sh:NodeShape` with `sh:targetClass` pointing at the class IRI.
- **A property shape per slot** — `sh:property` with an explicit `sh:path` (the slot's IRI). A property
  shape with no path validates nothing.
- **Cardinality** — `sh:minCount` from `required: true`; `sh:maxCount 1` for single-valued slots
  (omitted for `multivalued`). Missing cardinality is the most common silent gap.
- **Datatype / class constraints** — `sh:datatype` for literal ranges, `sh:class` for object ranges,
  `sh:nodeKind sh:IRI` for URI-valued slots.
- **Value constraints** — `sh:pattern` from `pattern`, `sh:minInclusive`/`sh:maxInclusive` from numeric
  bounds, `sh:in` from enum ranges.
- **Uniqueness / keys** — the shapes realising `unique_keys` / `identifier` where the target store must
  enforce them.
- **Severity** — an explicit `sh:severity` policy (default `sh:Violation`) so consumers know a failure
  is blocking.

## The rule of thumb

If a class or property has **no URI**, **no range**, or **no description**, its OWL/SHACL will be
incomplete — and that is a schema defect to fix in the YAML, not a generator limitation. The
completeness of the semantic artefacts is a direct, checkable function of authoring discipline.
