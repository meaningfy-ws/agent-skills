# Quality gates — chosen, not imposed

Quality gates are what keep the schema and its generated code from drifting. But the *right* set depends
on the project — so this skill **asks the user which gates to establish** rather than hard-coding one
profile. Run the selection as a short conversation, wire the chosen gates into `make` + CI, and record the
choice.

## The selection process

Walk the candidate gates below with the user; for each, confirm enable/skip and any threshold. Default to
enabling the first three (they are cheap and catch the most common drift); make the rest a deliberate
choice.

| Gate | What it catches | Ask |
|------|-----------------|-----|
| **Schema lint (no muted warnings)** | naming/metadata/convention violations | Enable with a committed ruleset? |
| **Codegen freshness** | a YAML edit committed without regenerating | Enable? (strongly recommended) |
| **Example round-trip** | documentation examples that rot | Enable if the schema uses `examples:`? |
| **Coverage on hand-written code** | untested adapters/validators around the models | What threshold (project default ≥80%)? |
| **Import-linter on generated modules** | generated `models` importing upward, variant cross-imports | Enable if layered/versioned? |
| **model2owl / SHACL checker** | incomplete or incorrect OWL/SHACL | Enable if OWL/SHACL is a delivered target? |

Record the outcome (e.g. in the repo's CONTRIBUTING or a `make` help block) so the choice is visible and
revisitable, not folklore.

## Gate mechanics

### Schema lint — without muting

Run **`linkml-lint`** (`linkml-lint schema.yaml`, or a directory recursively) **without** muting
warnings, against a committed ruleset. Muting silently discards every naming/metadata convention the
linter enforces — treat a muted linter as a violated gate. Configure it with a committed
`.linkmllint.yaml` that `extends: recommended`; wire it into the default build and CI. Exit codes: `0`
clean, `1` warnings, `2` errors.

Key rules to enable (see <https://linkml.io/linkml/schemas/linter.html>):

- **`recommended`** — requires recommended metaslots (chiefly `description`) — this is what enforces the
  "define every element" rule.
- **`standard_naming`** — CamelCase classes/enums, snake_case slots.
- **`tree_root_class`** — requires a single `tree_root: true` class (important for JSON/REST models).
- **`canonical_prefixes`** — prefixes align with the standard prefixmaps.
- **`no_invalid_slot_usage`** — a `slot_usage` must reference a real slot.
- **`permissible_values_format`** — consistent enum value casing.
- **`no_empty_title`**, **`no_xsd_int_type`** — annotation hygiene.

See also the LinkML [validation](https://linkml.io/linkml-model/1.11.x/docs/specification/05validation/)
spec for instance-data validation beyond schema linting.

### Codegen freshness — regenerate and diff

Generated code is committed but nothing guarantees it matches the YAML. In CI, regenerate and fail on a
non-empty diff:

```makefile
check-models: generate-models
	git diff --exit-code -- $(GEN_PY) $(GEN_JSON) $(GEN_OWL) $(GEN_SHACL)
```

A YAML edit without regeneration then fails the build — the single most valuable LinkML gate.

### Example round-trip

Validate the schema's inline `examples:` against the schema (`linkml-validate`) so documentation examples
can't drift from the model they illustrate.

### Coverage and architecture

Apply the project's normal coverage bar to the hand-written code *around* the generated models (adapters,
validators). Enforce the layering on generated modules with `import-linter` (see the boundary note in
[`generation-and-templates.md`](generation-and-templates.md)).

## The non-negotiable working loop

Whatever gates are chosen, the authoring loop is fixed: **edit YAML → lint → regenerate → verify the diff
→ validate examples → commit YAML and regenerated artefacts together**. Anti-patterns that mean STOP:
editing a generated file; adding a validation in Python that belongs in the schema; a bare string where an
enum fits; muting the linter; committing model changes without regenerating.

## Scaffolding

Wiring these gates + the generation automation + the per-module layout into a repo is `project-setup`'s
job, conditional on the project using LinkML. This skill owns *what* the gates are and *how* to choose
them; `project-setup` owns *installing* the chosen set.
