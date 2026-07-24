# Checklists

Two checklists for the scaffold: **(a)** the ordered scaffolding steps, and **(b)** the
Definition of Done. Tick every box before handing off. Pillar-gated steps (docs, infra, CI,
multi-component) apply only if the interview selected them.

> **Existing repo?** This checklist is the greenfield path. To modernise an existing repo, follow
> `modernizing-existing-projects.md` (audit → shape the upgrade as an OpenSpec change → human
> approves → apply in slices); the (b) Definition of Done below still applies once the gaps are
> closed.

## (a) Scaffolding checklist (ordered)

- [ ] **Interview** — run `references/interview.md`; resolve identity, **archetype**
      (product/library/doc-only), product flavour + frameworks, model source, datastores,
      deployable?, pillars, governance. For doc-only run the intention-elicitation step. No silent
      assumptions.
- [ ] **Confirm** — echo back the resolved profile + the file tree; get an explicit "yes".
- [ ] **Git** — ensure a git repo exists (`git init` if empty); set the default branch to
      `<<DEFAULT_BRANCH>>`.
- [ ] **Skeleton** — run `scripts/scaffold.sh -p <package> -n "<Project Name>" -a <product|library|doc-only>`
      (`--deployable` for a deployable product; `--minimal` for agentic-only), or create the tree by
      hand from `layout.md`; add `__init__.py` to every package.
- [ ] **Root config** (code archetypes) — render the root templates (`config-files.md`):
      `pyproject.toml`, `ruff.toml`, `mypy.ini`, `pytest.ini`, `.coveragerc`,
      `.pre-commit-config.yaml`, `sonar-project.properties`, `.gitignore`, `Makefile`, `VERSION`,
      `LICENSE`.
- [ ] **Architecture** (code) — write `.importlinter` (`architecture-guardrails.md`); for
      multi-component, model `code-anatomy.md` first, then translate to contracts.
- [ ] **Model** (product) — `model/` (LinkML seed) + the `make generate-models` bridge
      (`conceptual-modelling`).
- [ ] **Neo4j generators** (product, LinkML model source + Neo4j datastore selected, Q4.5 + Q5.1) —
      project a **pinned copy** of `gen-neo4j-constraints`/`gen-neomodel` (repo tooling at
      `tools/linkml_neo4j/` — documented, not owned, by `linkml-engineering`) into `scripts/`; wire
      `make neo4j-constraints` / `make neomodel` targets alongside the existing `make
      generate-models` ones. Refresh path:
      re-run `project-setup`, review the diff — same discipline as the `meaningfy` OpenSpec schema
      pin (`spine-projection.md`), never silently overwritten.
- [ ] **Tests** (code) — drop the `tests/` tree with the marker-injecting `conftest.py` and one
      smoke unit test + one example feature (`testing-setup.md`).
- [ ] **Agentic** — render the canonical `CLAUDE.md`; create the `AGENTS.md` symlink
      (`ln -s CLAUDE.md AGENTS.md`); seed `.claude/memory/MEMORY.md` (regenerable index)
      (`agentic-setup.md`).
- [ ] **Spine** — project `openspec/` (config + the PINNED `meaningfy` schema + `specs/` +
      `changes/` + `archive/`); install `/opsx:*` core profile; golden thread pre-wired
      (`spine-projection.md`).
- [ ] **Docs** (if selected) — Antora skeleton + playbooks (`antora-docs.md`).
- [ ] **Infra** (if selected) — `infra/` compose, Dockerfile, `Dockerfile.dockerignore`,
      `entrypoint.sh`, `.env.example` (`ci-and-infra.md`).
- [ ] **CI** (if selected) — `.github/workflows/ci.yaml` (+ `docs.yaml`), each calling `make`
      targets; CD `deploy.yaml` TODO stub for a deployable product (`ci-and-infra.md`).
- [ ] **Install & verify** — `make install`; then `make check-all`.
- [ ] **First commit** — only on explicit developer consent; conventional message via the
      `meaningfy-git-workflow` skill.
- [ ] **Spine + skillery + ponytail** — install so `CLAUDE.md` routing + `/opsx:*` resolve:
      `npx -y @fission-ai/openspec@1.4.1 init --tools claude --profile core`;
      `/plugin marketplace add meaningfy-ws/skillery`;
      `/plugin install meaningfy-core meaningfy-building`;
      `/plugin install superpowers@claude-plugins-official`;
      `/plugin marketplace add DietrichGebert/ponytail && /plugin install ponytail@ponytail`.
- [ ] **First EPIC** (optional) — `/opsx:propose` → `openspec/changes/<id>/proposal.md` (EPIC) +
      `design.md` + `tasks.md` (PLAN); gate the PLAN with `clarity-gate` before `/opsx:apply`.
- [ ] **Hand off** — summarise what was created, what is stubbed, and the next steps.

## (b) Definition of Done (the scaffold is complete when…)

- [ ] `make install` succeeds (all dependency groups; does **not** run `poetry lock`).
- [ ] `make check-all` is **green** on the empty skeleton (lint + types + architecture +
      `openspec validate --strict` + placeholder test).
- [ ] `make lint` (ruff) and `make typecheck` (mypy) pass with no errors.
- [ ] `make check-architecture` passes — `.importlinter` contracts hold (optional layer names
      keep the empty skeleton green).
- [ ] `make test` runs and the placeholder unit test + example feature pass; coverage gate
      configured (≥80%).
- [ ] `CLAUDE.md` is canonical and `AGENTS.md` is a **symlink** to it (`ls -l AGENTS.md` shows the
      arrow); the symlink is documented in the README; the repo `CLAUDE.md` routes to (not restates)
      the global `~/.claude/CLAUDE.md` standard.
- [ ] `.claude/memory/MEMORY.md` seeded as a ≤200-line **regenerable index** (truth = `openspec/specs/`).
- [ ] **Spine projected** — `openspec/` has `config.yaml`, the PINNED `schemas/meaningfy/`, `specs/`,
      and `changes/` (+ `archive/`); `openspec validate --strict` passes; `/opsx:*` core profile installed.
- [ ] **Skillery + ponytail installed** — the Meaningfy plugins and `ponytail` are present so the
      skill routing in `CLAUDE.md` resolves (no unresolved skill references).
- [ ] **No `/src`** — the package is top-level; `pytest.ini` has `pythonpath = .`;
      `pyproject.toml` `packages` include has no `from`.
- [ ] `pyproject.toml` is **minimal** — only `[project]`, `[tool.poetry]`,
      `[dependency-groups]`, `[build-system]`; every other tool config is in its own root file.
- [ ] **Version has a single source of truth** (`cosmic-python:PR-SSOT-DRY`) — one source (a root
      `VERSION` file or `__init__.__version__`); `pyproject.toml` derives from it. No second hard-coded literal.
- [ ] **Docs** (if selected): `make build-docs` produces a site under `docs/build/`.
- [ ] **Infra** (if selected): `infra/compose.yaml` validates (`docker compose … config`);
      `Dockerfile.dockerignore` co-located; `.env.example` present, real `.env` git-ignored.
- [ ] **CI** present: `ci.yaml` exists and calls `make` targets (mirrors the local gates).
- [ ] `README.md` is accurate — how to install, run, test, build docs; documents the symlink.
- [ ] `.gitignore` covers `.venv/`, caches, build artefacts, `infra/.env`, secrets.
- [ ] First commit is clean and conventional (only on developer consent).

## Smoke verification commands

Run from the repo root after scaffolding. These mirror the CI gates — green here means green in
CI.

```bash
make install                       # all dependency groups, no lock
make check-all                     # lint + typecheck + check-architecture + test (the umbrella gate)

# individual gates (if check-all is not yet defined or you want to isolate a failure)
make lint                          # ruff format --check + ruff check
make typecheck                     # mypy
make check-architecture            # poetry run lint-imports --config .importlinter
make test                          # pytest (markers stamped by tests/conftest.py)

# agentic + spine + layout sanity
ls -l AGENTS.md                    # → AGENTS.md -> CLAUDE.md (CLAUDE-canonical)
test -f .claude/memory/MEMORY.md && echo "MEMORY.md present"
test -f openspec/config.yaml && test -d openspec/schemas/meaningfy && echo "spine projected"
ls -d <<PACKAGE>>/                 # top-level package exists (no src/)

# pillars (only if selected)
make build-docs                    # Antora site → docs/build/
docker compose -f infra/compose.yaml --env-file infra/.env config >/dev/null   # compose valid
```
