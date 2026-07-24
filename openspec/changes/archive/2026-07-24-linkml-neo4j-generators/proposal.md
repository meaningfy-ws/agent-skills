# EPIC: Vendored, tested Neo4j-targeting LinkML generators

## Appetite

Medium — two generator scripts to fix and enrich, a real (empirically-verified) constraint-support
spike against Neo4j Community, a synthetic fixture schema, a vendored real-schema fixture, a unit
test suite, and a documentation/projection seam. Not small (real bugs to fix correctly, not
patch over); not large (two generators, no new distribution mechanism, no app-layer validation
layer).

## Why

Two custom LinkML generators — `gen_neo4j_constraints.py` (Cypher DDL) and `gen_neomodel.py`
(neomodel OGM classes) — already exist in a sibling project (`hulubul-broker`), built on LinkML's
own `Generator` base class exactly as `linkml-engineering`'s `generation-and-templates.md` already
recommends for custom generators. They have zero tests, and inspecting their actual generated
output against that project's real schema turned up two confirmed bugs (a relationship target that
resolves to nothing when the range is an abstract class) and a real drift risk (a hand-maintained
Cypher file duplicating a subset of the generator's own output). The Cypher generator is also
markedly less expressive than the neomodel generator today — it emits zero relationship-level
constructs and skips every multivalued property outright. Right now, if another project wants this
capability, it copies untested code from `hulubul-broker` by hand and inherits its bugs and its
drift risk. `linkml-engineering` should own a single, tested, correct version instead.

## Solution outline

Fix both generators against their real, confirmed bugs; enrich the Cypher generator to close the
gaps versus neomodel that Neo4j can *actually* enforce natively (no app-layer validation duplicate —
neomodel already is the app-layer companion); empirically verify what Neo4j 5.x Community Edition
can enforce (rather than trust the existing generator's Enterprise-only comments) and generate a
Community-safe profile automatically instead of hand-copying one; make index generation
schema-driven via an opt-in LinkML annotation instead of a permanently hand-maintained file. Vendor
both generators as tested skill assets in `linkml-engineering` (mirroring how `project-setup`
already vendors and projects templates — the `openspec/schemas/meaningfy/` pinned-copy-with-refresh
pattern is the direct precedent), with a fast synthetic unit-test fixture plus a second fixture
vendored from `hulubul-broker`'s real (CC-BY-4.0-licensed) schema as a richness/regression check.
`project-setup` gains the conditional projection step; `generation-and-templates.md`'s existing
"enable-on-demand target matrix" gains the two generators as named, documented targets.

## Key decisions

- **DEC-1** *(revised — see tasks.md §6/§8 for the correction history)*: The generator code is
  vendored as **repo tooling** under `tools/linkml_neo4j/` — **not** a skill asset — tested by a
  real pytest suite in skillery's own `tests/`, and **projected** into a consuming repo by
  `project-setup` (conditional on the project using LinkML + Neo4j) — not published as a separate
  PyPI package, and not left as a copy-by-hand-per-project pattern. `linkml-engineering` documents
  and cites the generators (the behavior is LinkML-generator knowledge); it does not own the code,
  because a Skill's home is reusable *knowledge* per `spec/skill-repo-governance.md`, not a
  maintained, tested codebase — the same "cite, don't own" boundary this catalogue already applies
  to external skills. This reuses the exact pinned-copy/refresh discipline `project-setup` already
  applies to the `meaningfy` OpenSpec schema (see `skills/project-setup/references/
  spine-projection.md`, which is *also* not inside any skill's own folder), so the drift-risk class
  found in `hulubul-broker` (a hand-maintained shadow copy silently diverging from its generated
  source) cannot recur here: the master copy's tests live in skillery, refreshing a project's copy
  is a deliberate, reviewed act (diff shown, never silently overwritten), same as the schema pin.
- **DEC-2**: No app-layer validation output. Where Neo4j cannot natively enforce something
  (enum-membership, patterns, numeric bounds, relationship-cardinality "at least one"), the
  `gen_neomodel.py` generator already is the app-layer companion — this EPIC does not add a third
  validation surface. The Cypher generator's enrichment is scoped strictly to what Neo4j 5.x can
  natively enforce.
- **DEC-3**: Target Neo4j **Community Edition** only. The existing generator's comments assume
  existence/type constraints need Enterprise; this EPIC verifies that empirically against the
  actual pinned version (`neo4j:5.26-community`, per `hulubul-broker`'s own `docker-compose.yaml`)
  rather than trusting the comment, and the generator emits only what Community actually accepts.
  No feature is gated behind an assumed Enterprise requirement without that empirical check.
- **DEC-4**: `gen_neomodel.py` switches from flat, standalone classes to **real Python inheritance
  mirroring each LinkML `is_a` hierarchy** (abstract LinkML class → `__abstract_node__ = True`
  neomodel base; concrete subclasses inherit from it in Python). This is a deliberate reversal of
  the current generator's documented "no inheritance, flat mapping" choice, and is the root fix for
  the abstract-relationship-target bug: neomodel's own polymorphic node resolution then makes
  `RelationshipTo('SpatialObject', ...)` resolve correctly to any concrete subclass carrying that
  label, instead of pointing at a Python name that is never defined.
- **DEC-5**: Index generation becomes schema-driven: an opt-in LinkML slot `annotations` key (e.g.
  `neo4j_index: true`) that the Cypher generator recognises and lowers to `CREATE INDEX`, replacing
  the fully hand-maintained index block found in `hulubul-broker`'s `infra/cypher/schema.cypher`.
- **DEC-6**: Two-tier test data. A small, hand-authored synthetic LinkML fixture (readable,
  deliberately exercises every construct this EPIC touches: `is_a` + abstract base, `any_of`
  range restriction, required multivalued scalar/enum, a value object with no identifier reached by
  relationship, a self-referencing relationship, a `slot_usage` cardinality override) drives fast
  unit tests. A second fixture is a vendored copy of `hulubul-broker`'s actual LinkML schema
  (CC-BY-4.0, attributed) as a real-world richness/regression check — skillery does not take a
  runtime or CI dependency on the sibling repo itself, only a committed copy of its schema files.

## Rabbit-holes

- Don't try to make Cypher constraints emulate what Neo4j fundamentally cannot check (enum
  membership, regex patterns, numeric bounds, "at least one relationship of type X") — per DEC-2,
  name the boundary and move on; neomodel already covers it.
- Don't design a generic "any custom generator" plugin framework — this EPIC ships exactly two
  generators (Neo4j constraints, neomodel), following the pattern `generation-and-templates.md`
  already documents for custom generators. A generic framework is speculative until a third
  generator actually needs one.
- The empirical Community-vs-Enterprise check (DEC-3) is a real spike with a real Neo4j container —
  don't skip it and guess from documentation or the existing (possibly stale) code comments.

## No-gos

- `gen_mermaid_classdiagram.py` and `gen_operational_schemas.py` (the other two scripts read during
  exploration) are untouched — out of scope, unrelated to Neo4j.
- No PyPI package, no new distribution mechanism beyond the existing `project-setup`
  projection/pinning pattern (DEC-1).
- No app-layer validators, triggers, or APOC procedures generated as a Cypher-can't-do-it fallback
  (DEC-2).
- No change to `hulubul-broker` itself in this EPIC — it is a separate, private sibling repo.
  Migrating it to consume the vendored generators (deleting its own copies and the hand-maintained
  `schema.cypher`) is a natural follow-up, explicitly deferred to a later change in that repo, not
  this one.
- No Enterprise-only Neo4j feature emitted unconditionally (DEC-3) — Community Edition is the
  target, full stop.
- No generic "any LinkML construct → Cypher" completeness goal. Scope is the constructs actually
  found in real modelling (this EPIC's two fixtures), not an exhaustive LinkML-spec walk.

---

## What Changes

- Fix: relationship targets that are abstract LinkML classes no longer generate broken references
  in either generator (root-caused via DEC-4 for neomodel; verified/documented for Cypher).
- Enrich `gen_neo4j_constraints.py`: existence (+ type, where Community allows it per the DEC-3
  spike) constraints for required multivalued scalar/enum properties (currently skipped entirely);
  a generated Community-safe profile (replacing the hand-maintained subset file pattern found in
  `hulubul-broker`); schema-driven index generation via an opt-in annotation (DEC-5).
- Enrich `gen_neomodel.py`: real Python inheritance mirroring `is_a` (DEC-4).
- Vendor both generators as skill assets under `skills/linkml-engineering/assets/generators/` with
  a pytest suite in skillery's `tests/`, covering the synthetic fixture and the vendored
  `hulubul-broker` schema fixture (DEC-6).
- `project-setup` gains a conditional projection step for the two generators (parallel to the
  existing conditional LinkML branch), pinned-and-refreshable like the OpenSpec schema copy.
- `generation-and-templates.md`'s "Enable-on-demand target matrix" names both generators as
  documented, opt-in targets.

## Capabilities

### New Capabilities
(none — this is new asset/tooling scope inside the existing `linkml-engineering` capability)

### Modified Capabilities
- `linkml-engineering`: gains a requirement for the two vendored, tested Neo4j-targeting custom
  generators (assets, tests, projection), and the existing "Dual-CLI parity and deferred scope"
  requirement's "no new tooling" no-go (written for the original, docs-only `add-linkml-engineering-
  skill` change) is updated — that deferral is what this EPIC now deliberately picks up.

## Impact

- `skills/linkml-engineering/`: new `assets/generators/` (the two generator scripts), updates to
  `SKILL.md` and `references/generation-and-templates.md`.
- `skills/project-setup/`: conditional projection step for the two generators (references/
  spine-projection.md-style pinning), touching its LinkML branch.
- `tests/`: new pytest suite for the two generators, two fixture schemas (synthetic +
  vendored-from-hulubul-broker).
- `openspec/specs/linkml-engineering/spec.md`: modified requirement (see above).
- No change to any other skill, to `hulubul-broker`, or to the dual-CLI generation/distribution
  mechanism itself (skill assets already sync to `.opencode/` like any other skill file).
