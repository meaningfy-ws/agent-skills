# Interview Script

The grouped questions to ask before scaffolding. Use `AskUserQuestion` — one tool call per
group, batching the questions inside it. Make **no silent assumptions**; every answer below
drives which templates and pillars get applied. End by echoing back the resolved profile for
explicit confirmation (Plan phase, SKILL.md step 2).

Order matters: identity → archetype → runtime → frameworks → datastores → pillars → governance.
Later groups are **pre-filtered by the archetype** (R5/R8/R10): a `library` skips the datastore,
web-framework, and `model/` questions; a `doc-only` runs a mandatory **intention-elicitation** step
(Q2.2) and short-circuits Groups 3–5 (skip to Group 6 docs + Group 7).

---

## Group 1 — Identity

**Q1.1 Project name (human-readable).**
- Free text. Drives `<<PROJECT_NAME>>` in `AGENTS.md`, `MEMORY.md`, docs, `pyproject.toml`
  description.

**Q1.2 Distribution slug / repo name.**
- Free text; default = kebab-case of the name (e.g. `My Project` → `my-project`).
- Drives `<<PROJECT_SLUG>>` (Poetry `name`, sonar key, repo URL).

**Q1.3 Import package name.**
- Free text; default = snake_case of the slug (`my-project` → `my_project`).
- Drives `<<PACKAGE>>` — the **top-level package** (no `/src`; decision D1). Multiple
  deployable units → confirm extra package names (e.g. `<<PACKAGE>>_dags`).

---

## Group 2 — Archetype (the pivotal question)

Three explicit archetypes, each with a **fixed gate profile** (R5/R8/R10). **Regardless of
archetype the basics hold: "automate almost everything" + TDD.** The archetype decides which
*conditional* layers and gates apply on top of the basics.

**Q2.1 What kind of project is this?**

| Option | Description | `model/`? | Gate profile (CI-automatable gates as `make` targets) | Deploy |
|--------|-------------|-----------|--------------------------------------------------------|--------|
| **product** (recommended for any built software) | Software with a domain — REST service, pipeline, CLI, worker. Full 4 layers. | **yes** (LinkML) | `openspec validate --strict` + **codegen-in-sync** (`make generate-models`) + `check-architecture` + coverage ≥80% + code-review | conditional (Q2.4) |
| **library** | Importable/publishable package, no process, no domain to model. | no | `openspec validate --strict` + `check-architecture` + coverage ≥80% + code-review | **no** |
| **doc-only** | Non-code / documentation repository. | no | `openspec validate --strict` + docs build + (lightweight) link/structure checks | **no** |

- **Default/recommendation:** none — must be answered explicitly; it gates every later group.
- The old `service`/`pipeline`/`cli` answers all **map to `product`** (they differ only in the
  entrypoint/framework, asked in Group 4) — pick `product` and resolve the flavour there.
- `clarity-gate` is in **no** profile as a CI step — it is a human/agent semantic gate (the
  automation boundary, `../../../docs/ai-coding/dod-quality-gates.md`); CI may emit a reminder only.

**Q2.2 (doc-only ONLY) — intention elicitation (MANDATORY; do not assume).**
A non-code repo has no default shape. Before scaffolding any gates, run a real elicitation step —
do not guess the purpose:

- **What is the purpose of this repo?** (e.g. a knowledge base, an Antora doc site, an ADR log, a
  spec/decision corpus, a glossary). Free text.
- **What elements does it need?** (which Antora components/IA buckets; whether it carries the spine
  `openspec/` for decision/spec artifacts; whether it builds + publishes a site).
- **What does "done"/"good" mean here?** → which lightweight checks become the gate profile (link
  check, build, structure) — there is no Python test suite to gate.

Capture the answers; they decide the doc-only pillars (Groups 6–7) and its gate profile. A `library`
or `product` answer short-circuits Q2.2.

---

## Group 3 — Runtime (skip for `doc-only`)

**Q3.1 Minimum Python version.**
- Options: `3.12` (recommended), `3.11`, `3.13`.
- Drives `<<PYTHON_VERSION>>` in `pyproject.toml`, `ruff.toml` `target-version`, `mypy.ini`,
  CI matrix. Skip for `doc-only`.

---

## Group 4 — Product flavour + frameworks (ask only for `product`)

A `product` covers service / pipeline / CLI flavours; these questions resolve which entrypoint(s)
and frameworks apply. A `library` skips them (no process); a `doc-only` skips Groups 3–5 entirely.

**Q4.1 Primary process / entrypoint flavour?**
- Options: **service** (REST/HTTP), **pipeline** (batch/Airflow/worker), **cli**, *plain library
  inside a product*. Drives which `entrypoints/` skeleton and console script are scaffolded.

**Q4.2 Web framework?** (when flavour = service)
- Options: **FastAPI** (recommended), Starlette, Flask, *none*.
- Drives runtime deps, the `entrypoints/` API skeleton, OTel FastAPI wiring, CI smoke test.

**Q4.3 Orchestrator?** (when flavour = pipeline)
- Options: **Airflow** (recommended for batch), Prefect, *plain workers / none*.
- Drives a `<<PACKAGE>>_dags` top-level package, infra worker services.

**Q4.4 CLI library?** (when flavour = cli)
- Options: **Typer** (recommended), Click, argparse.
- Drives the `entrypoints/` CLI skeleton and console-script entry point.

**Q4.5 Conceptual-model source?** (product only — the conditional `model/`, R5)
- Options: **LinkML** (recommended default), **model2owl** (UML-driven, generates LinkML first),
  *other ontology tooling*. Never silently defaulted.
- Drives the `model/` directory + the `make generate-models` bridge (Pydantic / JSON Schema / OWL /
  SHACL). The model *source* and the generators are owned by the
  [`conceptual-modelling`](../../conceptual-modelling/SKILL.md) skill; `project-setup` only lays
  down `model/` and a seed schema. `library`/`doc-only` skip `model/`.

---

## Group 5 — Datastores (ask only for `product`)

**Q5.1 Primary datastore(s)?** (multi-select)
- Options: **MongoDB** (motor), **PostgreSQL** (SQLAlchemy/asyncpg), **Redis** (cache/streams),
  **Neo4j** (`neomodel`), *none / in-memory*.
- **Neo4j + LinkML model source (Q4.5) together** additionally project the vendored
  `gen-neo4j-constraints`/`gen-neomodel` custom generators (repo tooling at `tools/linkml_neo4j/`,
  documented by `linkml-engineering`) into `scripts/` — see `checklists.md` and `layout.md`.
- Drives runtime deps, the `adapters/` repository skeleton, `infra/compose.yaml` services,
  `infra/.env.example`, integration-test markers (`tests/integration/`), and the
  `Datastores / external systems` bullet in `CLAUDE.md`.

**Q5.2 External systems / APIs to integrate?**
- Free text (e.g. "an OpenAPI client to engine X", "an S3 bucket").
- Drives `adapters/` gateway stubs and the "external systems" note in `CLAUDE.md`.

---

## Group 6 — Pillars (which optional halves to include)

Each is a yes/no with a recommended default keyed off the archetype.

**Q6.1 Antora documentation?**
- Default: **yes** (no for `library` → reference-only). Drives the `docs/` Antora skeleton,
  `make build-docs`, and `docs.yaml` CI.

**Q6.2 Docker / infra?**
- Default: **yes** for service/pipeline flavours, **no** for `library`/`cli`. Drives `infra/`
  (compose, Dockerfile, entrypoint, `.env.example`, co-located dockerignore — D11).

**Q6.3 CI workflows?**
- Default: **yes** (always recommended). Drives `.github/workflows/ci.yaml` (calls `make`
  targets — D12) and, if docs selected, `docs.yaml`. `doc-only` gets `docs.yaml` only (no code CI).

**Q6.4 Deployable? — the CD seam (R10).**
- Default: **no**. Ask only for `product`. **Yes** → render the CD/release templates owned by the
  [`ci-cd-delivery`](../../ci-cd-delivery/SKILL.md) skill — BUT per its §6, only **after DevOps
  ratification**; until then scaffold a clearly-marked `deploy.yaml` **TODO stub** + the boundary
  docs (`--deployable`). `library`/`doc-only` get **no** deploy workflow.

**Q6.5 Multi-component tiers?**
- Default: **no** (single component). Yes when several business components exist → adds the
  tier hierarchy in `.importlinter` and the multi-component layout (see `layout.md`,
  `architecture-guardrails.md`). Start single; promote to tiers only when warranted.

---

## Group 7 — Governance

**Q7.1 License.**
- Options: **Apache-2.0** (recommended), MIT, proprietary/none.
- Drives `LICENSE`, `pyproject.toml` `license`, file headers.

**Q7.2 GitHub org / owner.**
- Free text. Drives `<<GITHUB_ORG>>` in repo URLs, CI, Sonar, docs site base.

**Q7.3 Default branch.**
- Options: **develop** (recommended at Meaningfy), `main`.
- Drives `<<DEFAULT_BRANCH>>` in `CLAUDE.md`, CI triggers, branch-protection guidance.

---

## Resolved-profile echo-back

Before writing any files, render this filled-in block and ask the developer to confirm:

```
Resolved profile
─────────────────
Project name      : <<PROJECT_NAME>>
Slug / repo       : <<PROJECT_SLUG>>
Package(s)        : <<PACKAGE>>[, <<PACKAGE>>_dags]
Archetype         : product | library | doc-only
  (doc-only purpose / elements : <from Q2.2 intention elicitation>)
Product flavour   : service | pipeline | cli | n/a
Python            : <<PYTHON_VERSION>>      (n/a for doc-only)
Web framework     : FastAPI | … | none
Orchestrator      : Airflow | … | none
CLI library       : Typer | … | n/a
Model source      : LinkML | model2owl | other | n/a   (product only → model/)
Datastores        : MongoDB, Redis | … | none
External systems  : <free text>
Gate profile      : openspec-validate + [codegen-sync (product)] + check-architecture + cov≥80 + review
                    (clarity-gate is human/agent, NOT CI)
Deployable        : yes (CD TODO stub, pending DevOps) | no
Pillars           : docs[y/n]  infra[y/n]  CI[y/n]  multi-component-tiers[y/n]
License           : Apache-2.0 | …
GitHub org        : <<GITHUB_ORG>>
Default branch    : <<DEFAULT_BRANCH>>
Spine             : openspec/ projected (schema meaningfy, PINNED); /opsx:* core profile

→ Will create: <file tree from layout.md, scoped to the pillars above>
Proceed? (yes / adjust)
```

Only on an explicit "yes" move to the scaffold phase (SKILL.md step 3). If the developer
adjusts, update the profile and re-echo — never start writing from an unconfirmed profile.
