# Generation, custom templates, and automation

Generation is **deterministic and outside the LLM path**: the LLM authors the *source* (YAML), a fixed
`make`-driven toolchain renders the *targets*. Treat it exactly like other schema-based codegen —
regenerate in CI, fail the build on drift (see [`quality-gates.md`](quality-gates.md)). Never hand-edit a
generated file; a needed change goes to the schema or the template.

## The `make generate-models` bridge

One target regenerates everything from the source; nothing downstream edits generated files by hand. Fail
loudly — write to a temp file and `mv` into place only on success, so a failed run leaves no partial
output.

```makefile
generate-models:                ## Regenerate all model targets from the LinkML source
	gen-pydantic --meta None --template-dir $(TEMPLATES)/ $(SCHEMA) > $(GEN_PY).tmp && mv $(GEN_PY).tmp $(GEN_PY)
	gen-json-schema $(SCHEMA) > $(GEN_JSON)
	gen-owl   $(SCHEMA) > $(GEN_OWL)
	gen-shacl $(SCHEMA) > $(GEN_SHACL)
	ruff check --select F401 --select I --fix $(GEN_PY) && ruff format $(GEN_PY)   # match house style
```

Pin the LinkML version deliberately (it is a codegen dependency, not a runtime one) and note *why* —
generators can change output between minor versions; an unrelated dependency bump must not silently
regenerate different code. Bump, regenerate, diff, then accept.

## Custom generator templates (the highest-leverage customization)

LinkML's Pydantic generator supports `--template-dir` with Jinja overrides. Use it to make every generated
model inherit the project's **own strict base class** instead of LinkML's generic `ConfiguredBaseModel` —
so the whole generated set obeys house conventions, defined once in hand-written code. This turns
"generated code" into "generated code that already obeys our conventions."

Worked example (from `mapping-suite-sdk`) — the class template swaps the base:

```jinja
{# templates/class.py.jinja #}
{% if bases == "ConfiguredBaseModel" %}
class {{ name }}(PydanticModel):        {# the project's strict base #}
{% else %}
class {{ name }}({{ bases }}):
{% endif %}
```

The strict base (hand-written, one place) sets the cross-cutting Pydantic config:

```python
class PydanticModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid", validate_assignment=True, validate_default=True,
        use_enum_values=True, populate_by_name=True,
    )
```

Keep override templates minimal — they only swap the base class and strip LinkML meta noise. The same
technique authors a **custom generator for any language**: subclass LinkML's `Generator` (or walk the
schema with `SchemaView`) so the generator is a pure function of the schema — deterministic, no side
inputs — and add it to `make generate-models` and the freshness check.

## Automation of transformations, including diagrams

Everything is a `make` target, not an ad-hoc command — models, secondary artefacts, and **diagrams**:

```makefile
generate-model-view:            ## Diagrams + inspectable schemas from the LinkML source
	gen-plantuml    $(SCHEMA) > diagrams/$(NAME).puml
	gen-json-schema $(SCHEMA) > schemas/$(NAME).schema.json
```

Generate only what is actually consumed somewhere — do not gold-plate artefacts nobody reads.

## Per-module artefact generation (not unified)

A multi-module project generates **dedicated artefacts per module**, mirroring each schema's path into the
output package — not one merged mega-artefact. The pattern (from `mapping-suite-sdk`): walk the schema
tree and mirror the relative path.

```makefile
generate-models-recursive:
	find $(SCHEMA_PATH) -name '*.yaml' | while read -r f; do \
	  rel=$${f#$(SCHEMA_PATH)/}; out=$(PKG)/$${rel%.yaml}.py; \
	  mkdir -p "$$(dirname "$$out")"; \
	  gen-pydantic --meta None --template-dir $(TEMPLATES)/ "$$f" > "$$out.tmp" && mv "$$out.tmp" "$$out"; \
	done
```

`schema/<domain>/<name>.yaml` → `<pkg>/<domain>/<name>.py`, same relative path and basename — trivial to
automate, trivial for a human to locate. Split schemas by bounded concept, one schema file per aggregate;
don't put unrelated domains in one giant file. **Scaffolding this layout into a repo is `project-setup`'s
job** (conditional on the project using LinkML).

## Enable-on-demand target matrix

First-class (wired and tested): **Pydantic, JSON Schema, OWL, SHACL** — the semantic core. Add the rest
only when a project consumes the target: **TypeScript** (`gen-typescript`), **SQL DDL / SQLAlchemy**
(`gen-sqlddl`/`gen-sqla` — keep the repository around the ORM hand-written, in `adapters/`),
**Markdown/HTML docs** (`gen-doc`), **JSON-LD context** (`gen-jsonld-context`), and **custom generators**.

## Architectural boundary for generated modules

Generated models still live inside the layered architecture (see `cosmic-python`): `models` (generated or
not) must not import `services`/`adapters`/`entrypoints`. If parallel versioned/variant model packages
exist (v1/v2/v3, per tenant), enforce their independence with `import-linter` the same as hand-written
code — codegen is not an exemption from the architecture.
