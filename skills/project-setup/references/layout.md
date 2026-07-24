# Repository Layout

The canonical file tree for a no-`/src` Meaningfy project (decision **D1**). All tool config
sits at the **root** (D2); the deployable unit is a **top-level package** named `<<PACKAGE>>`.
Two shapes are given: **single-component** (start here) and **multi-component / tiered** (when
several business components exist). For the layering *rationale* see the **cosmic-python**
skill; for contract authoring see `architecture-guardrails.md`.

`<<PACKAGE>>` = import package (e.g. `myproject`). Layers inside a component package, innermost
first: `domain` (the book's `models/`) → `adapters` → `services` → `entrypoints`. Direction:
`entrypoints → services → domain`, `adapters → domain`; `domain` imports nothing upward.

## Single-component tree

```
<repo-root>/
├── CLAUDE.md                     # CANONICAL agent instructions (D8 — CLAUDE-canonical, DEC-4)
├── AGENTS.md → CLAUDE.md         # SYMLINK — never a second copy
├── README.md                     # documents the symlink + how to run
├── LICENSE
├── VERSION                       # single source of the version string
│
├── pyproject.toml                # MINIMAL: [project] [tool.poetry] [dependency-groups] [build-system]
├── poetry.lock
├── ruff.toml                     # format + lint (replaces black/isort/flake8/pylint)
├── mypy.ini                      # type checking
├── pytest.ini                    # pythonpath=. ; markers ; NO coverage flags here (D5)
├── .coveragerc                   # coverage config (≥80%)
├── .importlinter                 # architecture contracts (D7) — checked by make check-architecture
├── .pre-commit-config.yaml       # ruff hook (+ optional AGENTS.md sync on Windows)
├── sonar-project.properties      # SonarQube key/sources
├── Makefile                      # the dev UX — install / check-all / test / build-docs / up…
├── .gitignore
│
├── <<PACKAGE>>/                   # ── the deployable top-level package (NO src/) ──
│   ├── __init__.py
│   ├── commons/                  # shared, imports no business component (tier 0)
│   │   ├── domain/               #   value objects, shared errors
│   │   ├── adapters/             #   config_resolver, hasher, tracing, base repos
│   │   └── __init__.py
│   ├── domain/                   # entities, value objects, domain services — no I/O, no frameworks
│   ├── adapters/                 # DB clients, HTTP clients, queues, file system — imports domain only
│   ├── services/                 # use-case orchestration — imports domain + adapters
│   └── entrypoints/              # API / CLI / listeners — imports services
│
├── tests/                        # SIBLING of the package; mirrors the code tree (D5)
│   ├── conftest.py               # pytest_collection_modifyitems stamps markers by path
│   ├── unit/                     # marker: unit       — fast, no I/O; mirrors the code tree
│   ├── feature/                  # marker: feature    — pytest-bdd (.feature + steps); mirrors capabilities
│   ├── e2e/                      # marker: e2e        — near-real stack
│   ├── integration/              # marker: integration— needs a running datastore
│   └── test_data/                # fixtures, used sparingly
│
├── model/                        # conceptual model (LinkML) — PRODUCT archetype only (R5)
│   └── schema.yaml               #   the domain source; make generate-models renders the targets
│
├── scripts/                      # PINNED, projected generators — only if LinkML + Neo4j (Q4.5+Q5.1)
│   ├── gen_neo4j_constraints.py  #   copied from skillery's tools/linkml_neo4j/; refresh
│   └── gen_neomodel.py           #   = re-run project-setup, review the diff (never silent)
│
├── openspec/                     # the SPINE (see spine-projection.md) — projected into every repo
│   ├── config.yaml               # schema: meaningfy ; context: ; the 3 thin per-artifact rules
│   ├── schemas/meaningfy/         # the PINNED meaningfy schema (copied from skillery)
│   ├── specs/                    # durable capability specs — THE TRUTH (deltas merge here on archive)
│   └── changes/                  # in-flight changes (proposal.md=EPIC, design.md+tasks.md=PLAN, inputs/)
│       └── archive/              #   completed changes
│
├── .claude/                      # regenerable INDEX layer (see agentic-setup.md) — NOT the truth
│   ├── agents/                   # optional thin wrappers
│   ├── skills/                   # project-specific skills only
│   └── memory/
│       └── MEMORY.md             # regenerable orientation index, ≤200 lines (truth = openspec/specs/)
│
├── docs/                         # Antora component (D10) — if docs pillar selected
│   ├── antora-playbook.yml
│   ├── antora-playbook.local.yml
│   ├── antora.yml                # component descriptor
│   └── modules/ROOT/
│       ├── nav.adoc
│       └── pages/                # tutorials/ how-to/ reference/ architecture/ adr/ …
│
├── infra/                        # Docker & deploy (D11) — if infra pillar selected
│   ├── compose.yaml
│   ├── .env.example              # committed; real .env is git-ignored, lives at infra/.env
│   ├── .secrets.example          # committed template; real .secrets is git-ignored
│   ├── docker/
│   │   ├── Dockerfile            # multistage builder→slim runtime, non-root
│   │   └── Dockerfile.dockerignore   # NOT a root .dockerignore (Docker auto-discovers this)
│   └── scripts/entrypoint.sh
│
└── .github/workflows/            # CI (D12) — workflows call make targets, never inline commands
    ├── ci.yaml                   # openspec-validate → lint → typecheck → check-architecture → test → cov → Sonar
    ├── docs.yaml                 # build + deploy to Pages (if docs selected)
    └── deploy.yaml               # CD TODO stub — DEPLOYABLE PRODUCT only, pending DevOps (ci-cd-delivery, R10)
```

### Annotations that matter

- **No `/src`.** `pyproject.toml` uses `packages = [{include = "<<PACKAGE>>"}]` with no `from`;
  `pytest.ini` sets `pythonpath = .`.
- **`tests/` is a sibling**, not nested — `tests/unit/` mirrors the code tree, `tests/feature/`
  the business capabilities. For the full test-tree layout, marker-by-path mechanics, and the
  `pytestmark`-in-conftest gotcha, see **`testing-setup.md`** (this file stays focused on the
  directory tree).
- **`commons` is tier 0** — shared code that imports no business component; everyone may import it.
- A component need not have all four layers (a coordinator may be `services`-only). Declare only
  the layers that exist; optional layer names in `.importlinter` keep the empty skeleton green.

## Multi-component / tiered tree

When there are several business components, each becomes its own sub-package with its own four
layers, and a **tier hierarchy** orders them (D7). Only the package body differs from above:

```
<<PACKAGE>>/
├── __init__.py
├── commons/                      # TIER 0 — shared; imports no business component
│   ├── domain/  adapters/  services/
│
├── <foundation_a>/              # TIER 1 (foundation) — may import commons
│   ├── domain/  adapters/  services/  entrypoints/
├── <foundation_b>/              # TIER 1 (foundation)
│   ├── domain/  adapters/  services/
│
├── <coordinator>/               # TIER 2 (orchestration) — may import tiers 0–1, not peers
│   ├── domain/  services/        #   (services-only component — no adapters/entrypoints)
├── <integrator>/                # TIER 2 (orchestration)
│   ├── domain/  adapters/  services/  entrypoints/
│
└── <public_api>/                # TIER 3 (entrypoint APIs) — may import tiers 0–2
    ├── domain/  adapters/  services/  entrypoints/
```

Tier rules (encoded in `.importlinter`): a component may import any **lower** tier, never a
**same-tier peer** (needs `forbidden`/`independence` contracts) nor a higher tier. `tests/`
mirrors the same component breakdown. This is the multi-component shape; capture it in a
code-anatomy.md dependency map.

### Pipeline archetype: a separate `<<PACKAGE>>_dags/` package

The **pipeline** archetype adds a second top-level deployable package alongside `<<PACKAGE>>/`:

```
<repo-root>/
├── <<PACKAGE>>/                  # the library/services package (no entrypoints needed by the dags)
└── <<PACKAGE>>_dags/             # SEPARATE deployable unit — Airflow DAG modules; imports <<PACKAGE>>
    └── __init__.py
```

`<<PACKAGE>>_dags/` is its own top-level package (D1: one package per deployable unit), so the
DAG bundle deploys independently of the core code it imports.

## Contrast: the `/src` layout (a common migration target)

> The full brownfield sequence (where this lift is the highest-blast-radius step) lives in
> `modernizing-existing-projects.md`.


An older repo may predate this standard and bury its package under `src/`.
Normalising it to this layout **shifts the package up one level**, the key insight being:

```
src/<pkg>/<component>/   →   <pkg>/<component>/   # package becomes top-level (D1)
```

(deploy units like `src/dags/` → `<pkg>_dags/` and `src/infra/` → `infra/` follow the same
lift). This skill's scope is **greenfield / young repos**; a full `/src` migration is an EPIC,
not an in-place edit — see SKILL.md "When to use / not use".
