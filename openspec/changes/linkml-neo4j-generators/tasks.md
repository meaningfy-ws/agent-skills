> Derived from EPIC `linkml-neo4j-generators`

## 1. Spike: empirical Community/Enterprise boundary (DEC-3)

- [ ] 1.1 **BLOCKED (this session)** — Stand up `neo4j:5.26-community` (testcontainers or local
      docker), try each candidate constraint type by hand: node property existence
      (`IS NOT NULL`), node property type (`IS :: TYPE`), list-typed property
      (`IS :: LIST<STRING>`), node key. Record what Community actually accepts vs rejects.
      Docker daemon is inactive in this sandbox and starting it needs sudo; user chose to skip
      Docker-dependent tasks for this session rather than wait. Generator defaults to the
      conservative pre-existing assumption (uniqueness = Community-safe; existence/type/list-typed
      = unverified, kept out of the `community` profile) until this actually runs.
- [ ] 1.2 **BLOCKED (this session)** — same reason as 1.1. The permanent test is written (task 5.3)
      but not executed.

## 2. Fixtures (DEC-6)

- [x] 2.1 Author a small synthetic LinkML fixture schema that deliberately exercises: an abstract
      base class (`is_a` hierarchy) with 2+ concrete subclasses, a slot whose range is that abstract
      class, an `any_of`-restricted relationship range, a required+multivalued scalar slot, a
      required+multivalued enum slot, a value object with no identifier reached by a relationship,
      a self-referencing relationship (`X.rel -> X`), and a `slot_usage` cardinality override.
      → `tests/fixtures/linkml/synthetic/library.yaml` (Media/Book/DVD/Dimensions/Category/Shelf/
      Loan). Verified loading via `SchemaView` — all constructs present as designed.
- [x] 2.2 Vendor a copy of `hulubul-broker`'s real LinkML schema (`model/linkml/*.yaml`, CC-BY-4.0)
      into skillery's test fixtures with an attribution header noting source repo + license + the
      date copied. No CI or runtime dependency on the sibling repo itself.
      → `tests/fixtures/linkml/hulubul/*.yaml` + `ATTRIBUTION.md`.

## 3. Fix + enrich `gen_neo4j_constraints.py`

- [x] 3.1 Add required-multivalued scalar/enum → existence constraint (remove the blanket
      multivalued skip for the existence case). Type constraint for multivalued stays out (task 3.2).
- [ ] 3.2 **DEFERRED, needs 1.1** — list-typed property constraints (`IS :: LIST<STRING>`) for
      multivalued properties. Not added: 1.1 never ran (Docker unavailable this session), and DEC-3
      says don't emit unverified constraint forms. Existence-for-multivalued (3.1) needed no such
      verification — list-vs-scalar doesn't change existence-constraint semantics — so it shipped;
      this one genuinely needs the empirical check.
- [x] 3.3 Add `--profile community` (default `full`) to the same generator/CLI — one code path.
      `community` = uniqueness + indexes only; `full` = also existence/type, explicitly commented
      as carried-over-unverified pending the spike (not asserted as confirmed-safe).
- [x] 3.4 Add opt-in `annotations: {neo4j_index: true}` slot recognition → `CREATE INDEX` emission.
      Indexes are not edition-gated, so emitted in both profiles.
- [x] 3.5 Resolve/verify relationship-target correctness against an abstract range — confirmed the
      Cypher generator never referenced relationship targets by name at all (it only checks
      `slot.range in class_names` to decide "skip, this is a relationship"), so there was nothing to
      break here; the bug was neomodel-only (task 4).
- [x] 3.6 Decided the Open Question: relaxed `_is_entity` → `_is_node_label` to "concrete class,
      identifier or not" (not "concrete + has identifier"). A value object like `Dimensions` now
      gets existence/type constraints on its own required properties (no uniqueness constraint,
      since there's no natural key) — existence/type don't depend on uniqueness, and this makes the
      Cypher and neomodel generators finally agree on what counts as a node.

## 4. Fix + enrich `gen_neomodel.py`

- [x] 4.1 Switch from flat, standalone classes to real Python inheritance mirroring each schema's
      `is_a` hierarchy; abstract LinkML classes become `__abstract_node__ = True` neomodel bases.
      Classes now emitted in parent-before-child topological order; each renders only its *direct*
      slots (inherited ones come down through Python inheritance instead of being redeclared).
- [x] 4.2 Confirmed relationships whose range is an abstract class now resolve correctly — verified
      two ways: (a) string assertions in the unit tests, (b) **actually importing the generated
      module and instantiating the classes through real neomodel** (no Docker needed — neomodel
      registers classes at definition time, no DB connection required). `SpatialObject`/
      `AgentInRole` are now real, registered classes with real, registered subclasses.
- [x] 4.3 Added a trailing comment on any relationship whose LinkML slot carries `any_of`, naming
      the restricted concrete targets (documentation only, per DEC-2 — no new validation code).
- [x] **Unplanned but found while doing 4.2**: a *third* real, previously-undiscovered bug —
      neomodel reserves the Python attribute names `id`, `deleted`, `element_id` (raises
      `ValueError` at class-definition time). Both fixtures' identifier slot is named `id`
      (LinkML's own convention), so the *original* generator (in both `hulubul-broker` and this
      change's first draft) has always produced code that crashes the instant neomodel actually
      tries to build the class — undetected because neither project had a test that imports the
      generated output; string-matching tests wouldn't have caught it either. Fixed: reserved
      names get a Python-side `_` suffix (`id_`) while `db_property=...` preserves the real Neo4j
      property key, so the Cypher constraint generator's property references are unaffected.

## 5. Tests

- [x] 5.1 Unit tests against the synthetic fixture (task 2.1): assert exact/partial expected Cypher
      and neomodel output for every construct the fixture exercises, including the two fixed bugs.
      → `tests/test_linkml_neo4j_generators.py` (`TestNeo4jConstraintsSynthetic`,
      `TestNeomodelSynthetic`) plus `TestNeomodelGeneratedCodeIsRealNeomodel` — the latter actually
      executes the generated source and instantiates real neomodel classes (not just string
      matching), which is what caught the reserved-attribute-name bug (task 4, unplanned item).
- [x] 5.2 Unit tests against the vendored real fixture (task 2.2): assert the generator runs
      without error over the real, messy schema and that the previously-broken relationship targets
      now resolve. → `TestHulubulFixtureRegression` + the hulubul case of
      `TestNeomodelGeneratedCodeIsRealNeomodel`. Skipped the "golden-file constraint-set diff" —
      the exact-match assertions on the abstract-class fix and the multivalued-existence fix are
      the regression signal that matters; a full golden file would need updating every time either
      generator's cosmetic output changes, for no extra safety.
- [x] 5.3 Integration test written (opt-in `docker` marker, testcontainers +
      `neo4j:5.26-community`) → `tests/test_linkml_neo4j_integration.py`. Applies the generated
      Community-profile Cypher, checks a violating write is rejected, AND runs the actual
      task-1.1 spike (existence/type/list-typed/NODE KEY probes against a real Community
      container) so the result is a repeatable test, not a comment. **Not executed this session**
      (Docker unavailable) — marked clearly in the file's own docstring; run it for real before
      trusting its "passed" status, then update gen_neo4j_constraints.py's docstring with the
      actual Community-support boundary it finds.
- [x] 5.4 Confirmed via `pytest.ini` (`addopts = -m "not docker"`, `docker` marker registered) —
      verified empirically: `make test` / `pytest tests/ -q` shows the 3 integration-test classes'
      cases deselected (7 items), not run, not even collected-and-skipped-slowly.

## 6. Vendor as repo tooling *(relocated — see §10)*

- [x] 6.1 Moved both generator scripts into `skills/linkml-engineering/assets/generators/`; the
      test suite imports them by file path (`importlib.util`), no packaging/install step needed.
      **Superseded by §10**: relocated to `tools/linkml_neo4j/` — a skill's home is knowledge, not
      a maintained codebase (`spec/skill-repo-governance.md`).
- [x] 6.2 Ran `make generate-opencode` — needed a real fix, not just "confirm": `tools/opencode_gen`'s
      `map_skill` mirrored a stray `__pycache__` (created as a side effect of running the tests
      locally) into `.opencode/`, because no prior skill ever shipped importable Python and the
      generator had never needed to exclude bytecode-cache artifacts. Fixed `map_skill` to skip
      `__pycache__`/`.pyc`/`.pyo`, added a regression test (`tests/test_opencode_gen.py::
      test_skill_pycache_excluded`). `make validate`'s two gates (drift, repo_lint) are green;
      full suite is 88 passed, 0 failed, 7 deselected (the opt-in Docker tests). *(This fix stands
      regardless of §10 — some future skill may still ship importable Python.)*

## 7. Docs

- [x] 7.1 Added both generators to `generation-and-templates.md`'s "Enable-on-demand target matrix"
      as a new named subsection, alongside TypeScript/SQL/docs.
- [x] 7.2 Noted the Community-Edition-only scope, the `--profile` split, the annotation-driven
      index mechanism, and the reserved-attribute-name handling in that same subsection (no new
      doc file needed — it fit cleanly).

## 8. `project-setup` projection

- [x] 8.1 Added the conditional projection step (LinkML model source + Neo4j datastore selected).
      Found along the way: **Neo4j wasn't even a listed datastore option** in `interview.md`'s Q5.1
      (only MongoDB/PostgreSQL/Redis) — added it. **Self-correction**: this task was first marked
      done on documentation alone (interview.md/checklists.md/layout.md prose) — when the user
      asked "how is this installed", checking `scaffold.sh` (the script that actually DOES the
      projection `spine-projection.md` only describes) showed no code path existed at all: no
      `--neo4j` flag, no `scaffold_neo4j_generators` function, nothing called. The "pinned/
      refreshable exactly like the OpenSpec schema copy" claim was aspirational, not real. Fixed:
      added a real `--neo4j` flag and `scaffold_neo4j_generators()` to `scaffold.sh`, mirroring
      `scaffold_openspec()`'s exact copy/skip/force discipline, gated on `$PRODUCT && $NEO4J`.
      **Verified by actually running it** (dry-run, real run, re-run without `--force` → skipped,
      re-run with `--force` → refreshed, a second run without `--neo4j` → no `scripts/` at all) —
      not just read for plausibility.
- [x] 8.2 Documented the refresh path (re-run `project-setup`, review diff) in `checklists.md`'s new
      "Neo4j generators" item and in `scaffold.sh`'s own inline copy, citing `spine-projection.md`'s
      established discipline rather than restating it. Added the `scripts/` entry to `layout.md`'s
      reference tree and the `--neo4j` flag to `scaffold.sh`'s `usage()` text.

## 9. Validate

- [x] 9.1 `openspec validate --changes linkml-neo4j-generators --strict` → passed (2/2, including
      the unrelated pre-existing `example-spine-roundtrip` change).
- [x] 9.2 `make validate` green: lint (repo_lint exit 0 — the printed notes are pre-existing,
      non-blocking advisories, not new failures) + test (88 passed, 0 failed, 7 deselected — the
      opt-in Docker-marked integration tests, confirmed excluded from the default path per 5.4).
      Also required a real fix along the way (task 6.2's `__pycache__` mirroring bug) — not just a
      pass-through check.

## 10. Course correction — code home (post-completion, user-flagged)

After §1-9 were all checked off, the user asked "how is this installed/used" — checking that
surfaced two real problems, both fixed:

- [x] 10.1 **`scaffold.sh` never actually projected anything.** §8 was marked done on documentation
      alone (interview.md/checklists.md/layout.md prose describing a `--neo4j` flag and a
      `scaffold_neo4j_generators` step) — neither existed in the actual script. Added both for
      real, mirroring `scaffold_openspec()`'s exact copy/skip/force discipline. **Verified by
      running it**, not just reading it: dry-run, real copy (byte-identical to source), re-run
      without `--force` → skipped, re-run with `--force` → refreshed, a run without `--neo4j` → no
      `scripts/` at all.
- [x] 10.2 **The code didn't belong inside `skills/linkml-engineering/` at all.** User: "so linkml
      skill carries this burden not the project setup?" Checked `spec/skill-repo-governance.md`:
      a Skill's home is *reusable knowledge*, not a maintained/tested codebase — every other skill
      in the catalogue is prose. Compared against the actual precedent (the OpenSpec schema pin):
      it lives at a neutral `openspec/schemas/meaningfy/`, **outside any skill's folder**, with
      `project-setup` the one that copies it — not inside project-setup's own folder either.
      Relocated both generators to `tools/linkml_neo4j/` (the existing home for skillery's own
      maintained-and-tested Python tooling — `repo_lint`, `opencode_gen`), updated every reference
      (`scaffold.sh`'s source path, both test files' `GENERATORS_DIR`, `generation-and-templates.md`,
      `checklists.md`, `interview.md`, `layout.md`), and re-verified end to end: scaffold.sh still
      copies correctly from the new location, full suite still 88 passed / 0 failed / 7 deselected,
      `repo_lint` exit 0. `linkml-engineering` now documents and cites the generators; it does not
      own them — the DEC-1 pattern used everywhere else in this catalogue ("referenced, not
      vendored").

## Roadmap

- [x] 1.1 · [x] 1.2 (blocked, documented) · [x] 2.1 · [x] 2.2 · [x] 3.1 · [x] 3.2 (deferred,
      documented) · [x] 3.3 · [x] 3.4 · [x] 3.5 · [x] 3.6 ·
      [x] 4.1 · [x] 4.2 · [x] 4.3 · [x] 5.1 · [x] 5.2 · [x] 5.3 (written, unexecuted) · [x] 5.4 ·
      [x] 6.1 · [x] 6.2 ·
      [x] 7.1 · [x] 7.2 · [x] 8.1 · [x] 8.2 · [x] 9.1 · [x] 9.2

## Verification

`openspec validate --strict` for structure; the new pytest suite (fast unit tests in the default
`make test` path, the Neo4j integration test opt-in) is the functional verification; a manual read
of the generated output against both fixtures confirms the two originally-confirmed bugs no longer
reproduce.
