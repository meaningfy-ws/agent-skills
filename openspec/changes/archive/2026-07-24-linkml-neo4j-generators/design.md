> Parent: `openspec/changes/linkml-neo4j-generators/proposal.md` (EPIC: Vendored, tested
> Neo4j-targeting LinkML generators)

## Context

Two generator scripts exist today in `hulubul-broker/scripts/`, both subclassing
`linkml.utils.generator.Generator` exactly as `linkml-engineering`'s
`references/generation-and-templates.md` already recommends for custom generators:

- `gen_neo4j_constraints.py` → Cypher DDL. Emits, per entity class (concrete + has an identifier
  slot): a `CREATE CONSTRAINT ... IS UNIQUE` on the identifier, and per non-identifier scalar/enum
  slot, `IS NOT NULL` (if required) + `IS :: <TYPE>`. Explicitly skips: multivalued slots (any),
  object-valued slots (treated as relationships and dropped entirely — no relationship-level
  constraint of any kind is ever emitted).
- `gen_neomodel.py` → neomodel `StructuredNode` classes via a Jinja2 template. Every concrete class
  becomes a **flat, standalone** class (the docstring calls this out as deliberate: "no Python
  inheritance, mirroring the flat per-label mapping"). Object-valued slots become
  `RelationshipTo(<range-name>, ...)` with a cardinality derived from `required`/`multivalued`.

Both were read against `hulubul-broker`'s real schema (7 LinkML files, 798 lines) and its
already-committed generated output (`model/generated/neo4j/constraints.cypher`,
`model/generated/neomodel/hulubul_ogm.py`). Two real bugs and one real drift risk were confirmed
empirically (not hypothesised) — see EPIC "Why". Zero tests exist for either generator today.

`hulubul-broker` also hand-maintains `infra/cypher/schema.cypher`: a Community-safe subset of the
generator's uniqueness constraints, copied by hand, plus 15 hand-picked `CREATE INDEX` statements
the generator has no way to produce. Deployed Neo4j is `neo4j:5.26-community` (from that project's
`docker-compose.yaml`) — Community Edition, not Enterprise, which is the edition the current
generator's own comments assume existence/type constraints need.

## Goals / Non-Goals

**Goals:**
- Fix the abstract-relationship-target bug in both generators, at the root cause (DEC-4 for
  neomodel: real inheritance; equivalent correctness fix for Cypher).
- Close the Cypher generator's gap versus neomodel for constructs Neo4j 5.x **Community** can
  actually enforce: required-multivalued existence(+type), and a generated (not hand-copied)
  Community-safe profile.
- Make index generation schema-driven (an opt-in annotation) instead of permanently hand-maintained.
- Vendor both generators as tested skill assets, with a projection path via `project-setup`.
- Empirically verify the Community/Enterprise boundary against the actual pinned image
  (`neo4j:5.26-community`) rather than trust existing comments.

**Non-Goals:**
- Achieving constraint parity for anything Neo4j cannot natively check (DEC-2) — enum membership,
  patterns, numeric bounds, relationship-cardinality "at least one" stay neomodel's job.
- A generic pluggable custom-generator framework (Rabbit-holes).
- Touching `hulubul-broker` itself, or its hand-maintained `schema.cypher`/seed/demo files, in this
  change (No-gos) — this EPIC only produces the capability skillery ships; adopting it in that repo
  is a separate, later change there.

## Decisions

Cites EPIC DEC-1 through DEC-6 (asset+projection distribution, no app-layer duplication,
Community-only target, neomodel inheritance, annotation-driven indexes, two-tier fixtures — see
proposal.md). New for design:

- **Community/Enterprise spike is a real test, not a one-off.** Rather than a manual spike whose
  result then gets hand-encoded as a comment (the exact pattern that produced the current stale
  assumption), the empirical check becomes a permanent integration test (testcontainers, `neo4j:
  5.26-community`) that applies each candidate constraint type and asserts accept/reject. If Neo4j
  changes this boundary in a future image, the test catches it instead of the code silently lying
  again.
- **Index annotation key**: `annotations: {neo4j_index: true}` on a slot (LinkML's generic
  `annotations` dict, not a schema extension) — read via `SchemaView.get_slot(...).annotations`.
  Chosen over a new LinkML schema extension/mixin because `annotations` already exists in LinkML
  for exactly this "generator-specific hint" purpose and needs no schema-language change.
- **Community-safe profile as a CLI flag**, e.g. `--profile community` (default) vs
  `--profile full` (the reference/Enterprise-annotated file), on the *same* generator — not two
  separate scripts — so there is exactly one code path and the two outputs cannot diverge from each
  other structurally, only in which constraint lines they include.

## Algorithm / approach

### Fixing the abstract-relationship-target bug (worked example)

Today (`hasPickUpLocation`, range `SpatialObject`, abstract, `any_of: [Address, Place]`):
```python
# gen_neomodel.py today — broken: SpatialObject is never defined as a class anywhere
hasPickUpLocation = RelationshipTo('SpatialObject', 'HAS_PICK_UP_LOCATION', cardinality=One)
```

After DEC-4 (real inheritance), `SpatialObject` **is** generated, as an abstract neomodel base:
```python
class SpatialObject(StructuredNode):
    __abstract_node__ = True
    comment = StringProperty()
    hasCoordinates = RelationshipTo('GeoCoordinates', 'HAS_COORDINATES', cardinality=ZeroOrOne)

class Address(SpatialObject):
    number = StringProperty(required=True)
    ...

class Place(SpatialObject):
    ...
```
`RelationshipTo('SpatialObject', ...)` now resolves correctly — neomodel's own polymorphic
node-loading resolves a string target against its class registry, and `Address`/`Place`/`Area` are
all real, registered subclasses of the real, registered `SpatialObject` base. The `any_of`
restriction (pickup location is `Address ∪ Place`, not `Area`) is **not** mechanically enforceable
this way (neomodel has no union-of-subclasses relationship constraint) — documented as a comment on
the generated relationship line, consistent with DEC-2 (no new app-layer validation surface; this is
a documentation gap, not a missing feature to build).

### Cypher: required-multivalued existence (worked example)

Today `serviceType` (multivalued, required, enum `ServiceType`) on `TransportService` gets **no**
constraint at all (multivalued slots are unconditionally skipped). After this change:
```cypher
CREATE CONSTRAINT transportservice_serviceType_exists IF NOT EXISTS
FOR (n:`TransportService`) REQUIRE n.`serviceType` IS NOT NULL;
```
Neo4j's existence constraint checks property-key presence regardless of whether the stored value is
a scalar or a list — this needs no new Neo4j feature, just removing the blanket
`if slot.multivalued: continue` for the existence case. Type constraints on lists
(`IS :: LIST<STRING>`) are added **only if** the Community spike confirms Neo4j 5.26-community
actually accepts them — this is exactly the kind of claim the spike test verifies rather than
assumes.

### Index annotation (worked example)

```yaml
# hulubul_request.yaml, hasStatus slot (hypothetical annotation addition — schema-side, not code)
hasStatus:
  range: RequestStatus
  required: true
  annotations:
    neo4j_index: true
```
Cypher generator emits, alongside the existing property constraints:
```cypher
CREATE INDEX deliveryrequest_hasStatus_idx IF NOT EXISTS FOR (n:`DeliveryRequest`) ON (n.`hasStatus`);
```
This directly replaces the class of statement `hulubul-broker`'s `infra/cypher/schema.cypher`
currently hand-maintains — once a project's schema is annotated and it adopts the vendored
generator, the index block becomes generated, not hand-written. (Annotating `hulubul-broker`'s own
schema is that project's follow-up, per the EPIC's no-gos — this design only needs the generator to
support the annotation, verified against the synthetic fixture.)

### Anti-patterns

- ❌ Encoding the Community/Enterprise boundary as a source-code comment again, without the
  accompanying test that would catch it going stale (the exact anti-pattern found in the current
  `gen_neo4j_constraints.py`).
- ❌ Two separate scripts/files for "full" vs "community" profiles — one code path, one flag
  (Decisions, above); two files is exactly the drift shape found in `hulubul-broker`.
- ❌ Adding a Cypher-side workaround (trigger, APOC procedure) for anything Neo4j cannot natively
  constrain — that violates DEC-2 outright, no matter how tempting mid-implementation.
- ❌ Silently keeping the flat/no-inheritance neomodel mapping "for now" and patching the
  abstract-target bug with a string special-case — that fixes the symptom, not the cause, and the
  next abstract-ranged slot added to any schema breaks again.

## Error matrix

| Failure mode | Expected handling |
|---|---|
| A slot's range is abstract with **no** `any_of` restriction (e.g. `fromProvider: AgentInRole`) | Resolved by DEC-4's real inheritance — the abstract class is generated as a `__abstract_node__` base; no special-case needed |
| A slot's range is abstract **with** `any_of` (e.g. `hasPickUpLocation`) | Same DEC-4 fix resolves the *reference*; the union restriction itself is documented as a comment, not mechanically enforced (Non-Goal) |
| Community spike finds a constraint type is genuinely Enterprise-only on 5.26 | Excluded from the `--profile community` output; kept (with a clear comment) in `--profile full` only |
| A schema has no `neo4j_index` annotations at all | Generator emits zero `CREATE INDEX` statements — no behavior change from today's baseline for a schema that hasn't opted in |
| The vendored `hulubul-broker` fixture schema changes upstream after being copied in | Treated exactly like the OpenSpec schema pin: a stale copy is not auto-detected, refreshing it is a deliberate follow-up task, not a CI failure — this fixture is a richness/regression check, not a live contract with the sibling repo |
| A project runs the generator against a schema with a relationship slot whose range has **no** identifier and is **not** abstract (a plain value object, e.g. `GeoCoordinates`) | Already handled by the existing "value object → neomodel node reached by relationship, no Cypher uniqueness" split; unchanged by this EPIC except that its required scalar properties now also get existence/type constraints in the Cypher output where previously it got none at all (it has no identifier so `_is_entity` excludes it — worth confirming during implementation whether that exclusion should relax to "concrete class, id or not" so `GeoCoordinates.latitude required` gets a constraint; parked as an Open Question below) |

## Risks / Trade-offs

- [Risk] Real inheritance in `gen_neomodel.py` (DEC-4) changes the shape of every previously-flat
  generated class for any adopting project — a bigger diff than a point patch. → Mitigation: this is
  exactly why the fix belongs in a properly tested, vendored generator rather than a quick patch
  copied by hand into `hulubul-broker`; the generated-code diff for that project is its own
  follow-up change to review, not silently absorbed here.
- [Risk] A testcontainers-based integration test is a heavier CI dependency (Docker required) than
  anything in skillery's test suite today (currently pure-Python, no external services). →
  Mitigation: mark it as an opt-in/slow test (e.g. a pytest marker), not part of the default fast
  `make test` path, so the existing test suite's speed/dependency profile is unaffected for
  contributors who don't touch this generator.
- [Risk] Vendoring `hulubul-broker`'s schema as a fixture could drift from that project's actual
  current schema over time. → Mitigation: it's a snapshot fixture (like any test fixture), not a
  live sync; explicitly named as such in the Error matrix above.

## Open Questions

- Should the Cypher generator's definition of "entity" (currently: concrete + has an identifier)
  relax to "concrete, identifier or not" so that non-identified-but-concrete classes like
  `GeoCoordinates` also get existence/type constraints on their required scalar properties (they
  already become real neomodel nodes today, so the two generators currently disagree on whether
  such a class is "real")? Leaning yes for consistency between the two generators, but this changes
  what counts as a Neo4j label at all for the Cypher side and deserves a decision during
  implementation rather than being folded silently into DEC-4.
