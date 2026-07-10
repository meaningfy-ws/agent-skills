# LinkML authoring mechanics

How LinkML's own constructs realise the shared modelling conventions
([`../../modelling-conventions/SKILL.md`](../../modelling-conventions/SKILL.md)). This file owns the
*mechanism*; the *principle* (reusable properties, URI-everywhere, conceptual definitions) lives in
`modelling-conventions` and is not restated here. The SEMIC styleguide and the **model2owl conventions
and checkers** are the cited authority for the URI/naming/datatype slice; the LinkML metamodel is the
authority for the metaslots below.

**Reference links (LinkML spec, 1.11.x):**
[schemas](https://linkml.io/linkml-model/1.11.x/docs/specification/03schemas/) ·
[derived schemas](https://linkml.io/linkml-model/1.11.x/docs/specification/04derived-schemas/) ·
[validation](https://linkml.io/linkml-model/1.11.x/docs/specification/05validation/) ·
[mapping](https://linkml.io/linkml-model/1.11.x/docs/specification/06mapping/) ·
[OWL profile](https://linkml.io/linkml-model/1.11.x/docs/OwlProfile/) ·
[basic subset](https://linkml.io/linkml-model/1.11.x/docs/BasicSubset/) ·
[annotations](https://linkml.io/linkml/schemas/annotations.html) · model2owl:
[conventions](https://docs.ted.europa.eu/M2O/latest/uml/conceptual-model-conventions.html),
[checkers](https://docs.ted.europa.eu/M2O/latest/checkers/model2owl-checkers.html).

## Schema header — always set these

Every schema starts with a complete header; without it, implicit URIs and OWL/SHACL generation are not
possible.

```yaml
id: https://data.meaningfy.ws/<domain>/schema        # the official schema URI — an IRI close to the
                                                     # default-prefix namespace, with a distinguishing suffix
name: <domain>_model                                  # unique schema name
description: |                                         # conceptual description of what this model covers
  ...
version: 0.1.0
prefixes:
  linkml: https://w3id.org/linkml/                    # always declare at least linkml:
  dom: https://data.meaningfy.ws/<domain>/            # the model's own minted namespace
default_prefix: dom                                    # ALWAYS set — ask the user what it should be
default_range: string                                 # ALWAYS set explicitly (usually string) — then treat
                                                       # every remaining bare string as a smell to audit (below)
imports:
  - linkml:types                                       # always import the built-in types
```

- **`default_prefix` is mandatory and is a decision — ask the user** what the prefix (and its namespace)
  should be; it drives every implicit `class_uri`/`slot_uri`.
- The schema **`id`** should sit close to the `default_prefix` namespace but be distinguishable (a
  `/schema` suffix, say), so the schema IRI and the instance namespace don't collide.
- Set **`description`**, **`name`**, **`version`** on every schema — they flow into the generated
  ontology metadata and docs.

## Reusable slots (the decoupled-property mechanism)

Define attributes **once** in the top-level `slots:` block and reference them by name from every class.
This is the LinkML realisation of the reusable-property principle.

```yaml
slots:
  issued_at:
    description: The moment at which the artefact came into force.
    range: datetime
    required: true
classes:
  Invoice:    { slots: [issued_at] }
  CreditNote: { slots: [issued_at] }        # referenced, not redefined
```

Never redefine a same-meaning attribute inline under `attributes:` per class. When one class needs a
*refinement* of a shared slot (a tighter range, required here but optional elsewhere), express it with
**`slot_usage:`** in that class — do not fork the slot:

```yaml
classes:
  FinalInvoice:
    slot_usage:
      issued_at: { required: true }         # refine the shared slot in this class's context
```

## Identity: implicit URIs by default

Mint the namespace once (header) and let identity derive from it — do **not** hand-write a
`class_uri`/`slot_uri` on every element. With `default_prefix: dom`, class `Invoice` and slot
`issued_at` resolve to `dom:Invoice` / `dom:issued_at` implicitly. Provide `class_uri`/`slot_uri`
**explicitly as much as possible where they are NOT default-generatable** — chiefly when the element
**reuses a published vocabulary term**:

```yaml
slots:
  title:
    slot_uri: dcterms:title                 # explicit: reuses Dublin Core
```

For OWL sub-property semantics, use **`subproperty_of`** (maps to `rdfs:subPropertyOf`) — sparingly, for
elegant hierarchies:

```yaml
slots:
  has_author:
    subproperty_of: contributor
```

Treat `default_range: string` as a **smell magnet**: audit every string slot. Identifiers/URIs →
`uriorcurie`; timestamps → `datetime`; a closed set → an `enum`. Leave a slot as bare `string` only when
it is genuinely opaque free text.

## The URI-as-datatype artifice

When a slot's *values* are URIs (a reference/link/external identifier — not the element's identity), type
them as URIs, not opaque strings, with the built-in `uriorcurie` / `uri` types:

```yaml
slots:
  see_also: { description: A related resource., range: uriorcurie, multivalued: true }
```

For a project-specific URI notion, declare a `type` deriving from `uriorcurie` so the intent is named
once. This makes generated OWL/SHACL treat the value as a resource reference and keeps JSON-LD contexts
correct.

## Every element is defined — conceptually, and well annotated

- **`description` on every class, slot, and enum** — it *is* the definition. Definitions are
  **conceptual, not technical**: describe what the concept *means*, even when the concept is technical
  (see [`../../modelling-conventions/references/naming-and-identity.md`](../../modelling-conventions/references/naming-and-identity.md)).
- Add **`title`** (a human-readable label) and **`aliases`** (synonyms) where they aid understanding —
  they feed docs and disambiguation.
- Add **`examples:`** to slots with non-obvious values, as much as possible — they feed docs and are
  round-trip validated by the gates.

## The slot contract — make it unambiguous

For every slot (or its use on a class) state:

- **`range`** — always clear (a class, a built-in type, or an enum). An unranged slot is incomplete.
- **Cardinality** — at minimum **`required: true/false`**; use **`recommended: true`** for
  should-be-present-but-not-mandatory. `multivalued: true` for collections.
- **Inlining** — a nested object: `inlined: true`; a list of nested objects: `multivalued: true` +
  `inlined_as_list: true`.
- **Keys** — **`identifier: true`** on the aggregate's identifying slot (or `key: true`); at most one
  per class.
- **Validation** (very important, wherever expressible) — `pattern` / `structured_pattern` (regex),
  `minimum_value` / `maximum_value`, `equals_string` / `equals_number`, `unique_keys` (class-level).
  A constraint that lives only in code will drift.
- **`designates_type: true`** on a base slot for self-identifying polymorphic JSON.

## Enums are SKOS concept schemes

A LinkML `enum` transposes to a `skos:ConceptScheme` whose permissible values are `skos:Concept`s. Every
enum **and every value carries a `description`**; give each value a **`meaning:`** IRI wherever a
published vocabulary has the concept (that IRI is the `skos:exactMatch`/concept binding in the generated
semantics):

```yaml
enums:
  DocumentStatus:
    description: The lifecycle state of a document.
    permissible_values:
      DRAFT:  { description: Not yet issued. }
      ISSUED: { description: Issued and immutable., meaning: dom:Issued }
```

## Class design — inheritance, abstractness, tree root

- **`abstract: true`** — mark any class that must not be instantiated directly (a base). Confirm intent,
  then mark it.
- **`is_a`** — genuine taxonomy (single primary parent; propagates inheritable metaslots).
- **`mixins`** — cross-cutting bundles of slots shared across unrelated hierarchies; especially useful
  for **technical concepts** (timestamped, identifiable, versioned). Compose with `is_a`; don't overload
  `abstract` to fake a mixin.
- **`tree_root: true`** — mark **exactly one** class per model as the tree root. This is important for
  **JSON and REST API** design (it is the document/root of the generated JSON Schema), and the linter's
  `tree_root_class` rule expects a single one.

## Modularity vs profiling — two different tools

- **`imports:`** — split a large model into modules and import them; this is how modularity works
  (mirror the bounded contexts, one concern per file).
- **`subsets:` + `in_subset`** — define named **subsets** (`subsets:` block of `SubsetDefinition`s) and
  tag elements into them with `in_subset`. Subsets are for **profiles / views** (a "minimal" or "basic"
  slice, like LinkML's own [BasicSubset](https://linkml.io/linkml-model/1.11.x/docs/BasicSubset/)) — not
  for splitting a model into modules. Use them to carve a view out of one model, `imports` to compose
  many.
