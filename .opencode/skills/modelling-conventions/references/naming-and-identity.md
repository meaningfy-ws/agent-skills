# Naming and identity

Representation-agnostic rules for how modelled things are named and identified. The concrete syntax
lives in the consuming skill (see the LinkML mechanics in `linkml-engineering`); this file states the
discipline.

## Reusable, first-class properties

- **A property has one definition, referenced from many classes.** When an attribute of the same
  meaning recurs, model it once and reference it — never redefine it inline per class.
- **A property carries its own meaning**: a name, a prose definition, a range/type, and an identity.
  It is a citeable concept, not a field of a class.
- **Distinguish same-name-different-meaning.** Two attributes that happen to share a label but mean
  different things are two properties, not one. Reuse is by *meaning*, not by *spelling*.
- **Group cohesive optionals into a small value-object class** rather than flattening a dozen loose
  properties onto one class — a container class is itself a reusable, identifiable concept.

## Naming discipline

- **Intention-revealing and consistent.** The same Clean Code naming standard as code — a reader
  should infer meaning from the name without cross-referencing.
- **Classes are singular nouns** (`InvoiceLine`, not `invoice_lines` or `InvoiceLines`).
- **Properties are verbs/nouns that read as roles** (`issued_at`, `total_amount`, `has_part`).
- **Enumerations name a closed set**; each value is a stable key, never a free string.
- **The model's names are the ubiquitous language.** Terminology management (definitions, synonyms,
  disambiguation) is owned by `conceptual-modelling` — names chosen here feed it.

Casing is representation-specific (LinkML uses `UpperCamelCase` classes / `snake_case` slots; UML and
OWL differ). Each consuming skill states its casing table; the rule *here* is only "consistent and
intention-revealing".

## Definitions are conceptual, not technical

Every class, property, and enumeration value gets a real prose **definition** — and the definition
states what the concept *means*, not how it is stored or serialised. Define the concept even when the
concept is itself technical: "the moment the artefact came into force" rather than "an ISO-8601 string
field". A conceptual definition survives a change of representation and is what makes the model usable
as ubiquitous language; a technical one rots the moment the encoding changes. Add synonyms and a
human-readable label where they aid understanding. Missing or technical-only definitions are a smell
(see [`anti-patterns.md`](anti-patterns.md)).

## Identity: stable URIs, implicit by default

- **Mint a base namespace per model, once.** Every element's identity derives from it.
- **Identifiers are opaque and permanent.** Do not encode mutable facts (version, owner, location,
  file path) into the local name. The label can change; the identity must not.
- **Implicit by default.** Let the identity derive from `namespace + element-name`; write an explicit
  URI only when a specific value is required — most importantly when **reusing a published vocabulary
  term** (schema.org, Dublin Core, SKOS, a domain standard) instead of minting a new one.
- **Prefer reuse over invention.** Mapping onto an existing, published vocabulary signals
  interoperability and reduces semantic drift; mint a new term only when no suitable published one
  exists. Record the reuse so it survives into the generated semantic artefacts.
- **Mint at authoring time**, human-readable, like the other golden-thread IDs — not auto-generated
  from content hashes (those break on moves and across repos).

Why "implicit by default" matters downstream: a model where identity is systematic — not hand-written
per element — is one a generator can render to OWL/SHACL **completely**, because every class and
property already resolves to a URI. The LinkML realisation of this (minted `prefixes` +
`default_prefix`, implicit `class_uri`/`slot_uri`, the URI-as-datatype artifice) is owned by
`linkml-engineering`.
