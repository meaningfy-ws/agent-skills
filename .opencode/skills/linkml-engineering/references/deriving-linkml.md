# Deriving LinkML from an existing source

LinkML is never authored from nothing here — it is derived from a model or spec that already exists,
then refined (see [`authoring-mechanics.md`](authoring-mechanics.md)). If there is no upstream source,
stop and establish the model first via `conceptual-modelling`.

Each input kind has a distinct entry point. In all cases the output is a *draft* LinkML schema that you
then bring up to the conventions — derivation gets you the structure, refinement gets you the quality.

## From a UML model

The strongest path when the domain is modelled in UML. Run **model2owl**, which has mature OWL/SHACL/HTML
generators and can emit LinkML artefacts from the UML. In that setup:

```
UML model ──model2owl──▶ LinkML schema ──LinkML generators──▶ Pydantic / JSON Schema / OWL / SHACL / …
```

model2owl runs **first**, as a prerequisite stage of generation — it is not a competing path. Configuring
model2owl and wiring it into a repo is a separate concern (a future dedicated skill, tightly linked to
`project-setup`); here, treat its LinkML output as the derivation input. Map UML classes → LinkML
classes, UML attributes/associations → **reusable top-level slots**, and UML enumerations → LinkML
`enums`. Carry the UML element identities into minted URIs so nothing loses identity in the crossing.

## From a text specification

When the source is prose (a spec, a standard, an API description):

1. Extract the entities → candidate classes, the attributes → candidate **shared slots**, and the closed
   value sets → `enums`.
2. Where the spec mirrors a published standard (e.g. an error shape, a bibliographic record), map onto
   that vocabulary rather than inventing terms, and record the mapping.
3. Draft the schema, then refine to the conventions. The spec's own wording seeds the `description:` of
   each class and slot — definitions are not optional.

## From a model2owl output

If a project already runs model2owl, its LinkML output *is* the derivation input — do not re-derive from
the UML by hand. Refine the generated schema (reusable slots, implicit URIs, constraints) rather than
editing it as if hand-authored; if the generated shape is wrong, fix it upstream in the UML/model2owl
config, not in the LinkML.

## From another existing model

An existing schema (JSON Schema, an ORM, a protobuf/XSD, an older LinkML) is a derivation source:
translate its structure into LinkML classes + reusable slots + enums, then refine. Prefer regenerating
from the new LinkML over maintaining both — the point of the pivot is to collapse parallel definitions
into one source of truth.

## After derivation

Whatever the source, the draft is not done until it clears the conventions
([`../../modelling-conventions/references/editor-guardrails.md`](../../modelling-conventions/references/editor-guardrails.md))
and the LinkML mechanics in [`authoring-mechanics.md`](authoring-mechanics.md): reusable slots, implicit
URIs everywhere, enums for closed sets, constraints in the schema, a description on every class and slot.
