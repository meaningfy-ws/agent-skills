---
name: project-setup
description: Scaffold or modernise a Meaningfy-standard repo and PROJECT the Meaningfy spine into it — a top-level package (no src/), Poetry + dedicated root tool configs, cosmic-python layering with import-linter guardrails, TDD+BDD tests, a CLAUDE-canonical agentic setup (CLAUDE.md is canonical; AGENTS.md is an optional symlink), the openspec/ spine (config + pinned meaningfy schema + /opsx:* commands + golden thread), three archetypes (product/library/doc-only) with fixed gate profiles, conditional model/ and CD seam, Antora docs, infra, and CI. Use when starting a new repo or bringing an existing one up to standard. Trigger on "set up a new project", "scaffold a repo", "bootstrap a Python project", "new Meaningfy project", "initialise project structure", "add the standard tooling/docs/CI", "project the spine / set up openspec", "modernise/revamp an existing repo", "bring this project up to standard", "gap analysis against Meaningfy standards".
license: Apache 2.0
metadata:
  category: engineering
---

# Project Setup

## Overview

Interview the developer, then scaffold a complete Meaningfy-standard repository **and project the
Meaningfy spine into it**: a **top-level package** (never `/src`), all tool config in the
**repository root**, cosmic-python layering enforced by **import-linter**, a **TDD+BDD** test
layout, a **CLAUDE-canonical** agentic setup (`CLAUDE.md` is the source; `AGENTS.md` is an optional
symlink), the **`openspec/` spine** (config + pinned `meaningfy` schema + `/opsx:*` commands + the
golden thread), an **Antora** documentation site, optional **Docker/infra**, and **GitHub Actions
CI** that calls `make` targets.

This skill provides the *concrete scaffolding artifacts* (templates, checklists, precise file
specs). For the *knowledge* behind them it routes to the installed Meaningfy skills and the spine
rather than restating them:

| For… | Use skill / source |
|------|--------------------|
| Layering, SOLID, the four patterns, CI tools | `cosmic-python` |
| Minimal code — YAGNI, avoid over-engineering | `ponytail` (third-party) |
| System design, C4, ADRs, contracts | `architecture` |
| The domain `model/` (product) | [`../conceptual-modelling/SKILL.md`](../conceptual-modelling/SKILL.md) |
| LinkML gates, `make generate-models` automation, per-module output (if the project uses LinkML) | [`../linkml-engineering/SKILL.md`](../linkml-engineering/SKILL.md) |
| Deploy / versioned image (CD seam) | [`../ci-cd-delivery/SKILL.md`](../ci-cd-delivery/SKILL.md) |
| Release lifecycle — versioning, release notes, PyPI publish, `SECURITY.md` | [`../meaningfy-release/SKILL.md`](../meaningfy-release/SKILL.md) |
| EPIC (work shape) + PLAN, the spine workflow | `epic-planning` + the `/opsx:*` commands |
| Docs writing, AsciiDoc/Antora prose | `technical-writing` |
| Commits, branches, PRs | `meaningfy-git-workflow` |
| TDD discipline while implementing | `superpowers:test-driven-development` |

The spine conventions it lays down are documented in [`../../spine/README.md`](../../spine/README.md);
the target layout in [`../../docs/ai-coding/openspec-setup-guide.md`](../../docs/ai-coding/openspec-setup-guide.md).
**This skill DOES; those docs DESCRIBE.**

## Modes

- **Greenfield** — scaffold a clean repo from nothing (the default procedure below) and project the
  spine into it.
- **Minimal** (`--minimal`) — write *only* the agentic files (`CLAUDE.md` + `AGENTS.md` symlink), the
  `.claude/` index, and print the install commands. Absorbs the old init-script bootstrap as one
  mode of the single scaffolder — no second bootstrap path.
- **Brownfield (modernization)** — bring an *existing* repo up to standard. **Audit → imagine the
  ideal target → propose the upgrade as a shaped EPIC + PLAN (an OpenSpec change) → human approves →
  apply in safe slices.** Not in-place big-bang. `scaffold.sh --dry-run` prints a gap report
  (`+ create` / `= keep`) that writes nothing; full workflow:
  [`references/modernizing-existing-projects.md`](references/modernizing-existing-projects.md).

## Archetypes (the pivotal choice)

Three explicit archetypes, each with a **fixed gate profile**. **Regardless of archetype, the basics
hold: "automate almost everything" + TDD.** The archetype decides the *conditional* layers and gates.

| Archetype | `model/`? | Deploy | CI-automatable gates (as `make` targets) |
|-----------|-----------|--------|-------------------------------------------|
| **product** (any built software — service/pipeline/cli) | yes (LinkML) | conditional | `openspec validate --strict` + codegen-in-sync + `check-architecture` + cov ≥80% + code-review |
| **library** | no | no | `openspec validate --strict` + `check-architecture` + cov ≥80% + code-review |
| **doc-only** (non-code) | no | no | `openspec validate --strict` + docs build + lightweight link/structure checks |

- **doc-only** is non-code: the interview MUST run a real **intention-elicitation** step (purpose,
  needed elements, what "good" means) before scaffolding gates — never assume. See
  [`references/interview.md`](references/interview.md) Q2.2.
- **Conditional `model/`** (product): scaffolds `model/` (LinkML default) — the model itself owned by
  [`../conceptual-modelling/SKILL.md`](../conceptual-modelling/SKILL.md). **When the project uses
  LinkML**, also scaffold the LinkML layer owned by
  [`../linkml-engineering/SKILL.md`](../linkml-engineering/SKILL.md): the `make generate-models`
  automation (incl. diagrams), custom generator templates, **per-module dedicated-artefact output** (one
  artefact set per module, not unified), and the **quality gates chosen with the user** (lint-no-mute,
  codegen-freshness, example round-trip). **When the project does not use LinkML**, skip this layer
  entirely — do not scaffold LinkML gates or automation.
- **CD seam** (deployable product): renders the `ci-cd-delivery` CD templates **only after DevOps
  ratifies §6**; until then a clearly-marked `deploy.yaml` TODO stub + boundary docs (`--deployable`).
- **Release seam** (per archetype — content owned by [`../meaningfy-release/SKILL.md`](../meaningfy-release/SKILL.md)):
  **library** projects a `release.yml` stub (release-please + PyPI Trusted Publishing) + `SECURITY.md`;
  **product** points at the `ci-cd-delivery` GHCR image path + gets `SECURITY.md`; **doc-only** gets
  neither. This skill owns *when/into what repo*; the release content/intent lives in `meaningfy-release`.
- **`clarity-gate` is NOT a CI step** — it is a human/agent semantic gate (the automation boundary is
  pinned in [`../../docs/ai-coding/dod-quality-gates.md`](../../docs/ai-coding/dod-quality-gates.md)).

> **Non-negotiables** (hardest to reverse, most-violated by default): no `/src`, all tool config in
> the root, **canonical `CLAUDE.md` with `AGENTS.md` symlinked** (DEC-4), a minimal `pyproject.toml`,
> and the `openspec/` spine projected. See [`references/decisions.md`](references/decisions.md).

## Procedure

Work in phases. Confirm the plan before writing files; commit only on explicit consent.
**For an existing repo, follow [`references/modernizing-existing-projects.md`](references/modernizing-existing-projects.md)**
(audit → shape the change → approve → apply in slices) instead of steps 1–3 below; the pillar
references in step 4 still govern each piece.

1. **Interview** — ask the grouped questions in [`references/interview.md`](references/interview.md)
   (use `AskUserQuestion`). Resolve project name, package name(s), **archetype** (product/library/
   doc-only), product flavour + frameworks, model source, datastores, deployable?, and which optional
   pillars to include (docs, infra, CI). Make no silent assumptions; echo back the resolved profile.
2. **Plan** — present the resolved profile + the file tree you will create (from
   [`references/layout.md`](references/layout.md)). Get a go-ahead.
3. **Scaffold the skeleton** — run the scaffolder (flags, not positional args):
   ```
   scripts/scaffold.sh -p <package> -n "<Project Name>" -a <product|library|doc-only> \
       [--deployable] [--minimal] [--python 3.12] [--slug my-project] [--org meaningfy-ws] \
       [--branch develop] [--no-docs] [--no-infra] [--no-ci]
   ```
   It renders every template, creates the package/tests/`.claude`/**`openspec/`** trees, symlinks
   **`AGENTS.md → CLAUDE.md`**, copies the **pinned** `meaningfy` schema, and runs `poetry lock`.
   Idempotent; never clobbers without asking (`--force` / `--skip-existing`). `--minimal` writes only
   the agentic files + `.claude/` layout. Or create files by hand from `assets/templates/` using
   [`references/layout.md`](references/layout.md) + [`references/config-files.md`](references/config-files.md).
4. **Fill the pillars**, each governed by a reference:
   - Code & architecture → [`references/layout.md`](references/layout.md) + [`references/architecture-guardrails.md`](references/architecture-guardrails.md)
   - Tooling & config files → [`references/config-files.md`](references/config-files.md);
     application settings (the mandated `PR-CONFIG-DECOUPLED` pattern) → [`references/settings-pattern.md`](references/settings-pattern.md)
   - Tests (TDD+BDD) → [`references/testing-setup.md`](references/testing-setup.md)
   - Agentic setup (CLAUDE-canonical, memory index) → [`references/agentic-setup.md`](references/agentic-setup.md)
   - The spine (openspec/, pinned schema, /opsx:*, golden thread) → [`references/spine-projection.md`](references/spine-projection.md)
   - Documentation (Antora) → [`references/antora-docs.md`](references/antora-docs.md)
   - CI & infra & the CD seam → [`references/ci-and-infra.md`](references/ci-and-infra.md)
5. **Verify** — run the Definition-of-Done checklist in [`references/checklists.md`](references/checklists.md)
   (`make install && make check-all` must pass on the empty skeleton).
6. **Hand off** — install the spine commands + the Meaningfy skillery so `CLAUDE.md`'s routing and
   the `/opsx:*` workflow resolve, then summarise what was created, what is stubbed, and next steps:
   ```
   npx -y @fission-ai/openspec@1.4.1 init --tools claude --profile core
   /plugin marketplace add meaningfy-ws/skillery
   /plugin install meaningfy-core meaningfy-building
   /plugin install superpowers@claude-plugins-official
   /plugin marketplace add DietrichGebert/ponytail && /plugin install ponytail@ponytail
   ```
   Then shape the first EPIC with `/opsx:propose` (→ `openspec/changes/<id>/proposal.md` = EPIC,
   `design.md` + `tasks.md` = PLAN); gate the PLAN with `clarity-gate` (≥9/10) before `/opsx:apply`.

## Canonical stack (recommended defaults)

These are the defaults the templates implement. Deviate only with a stated reason.

| Concern | Choice | Rejected (why) |
|---------|--------|----------------|
| Packaging / deps | **Poetry** + `[dependency-groups]` | requirements.txt (no lock/groups), setup.py (legacy) |
| Format + lint | **Ruff** (`ruff.toml`) | black+isort+flake8+pylint (4 tools, slow) |
| Types | **mypy** (`mypy.ini`) | — |
| Tests | **pytest** + **pytest-bdd** (`pytest.ini`) | behave (separate runner), nose (dead) |
| Coverage | **coverage.py** (`.coveragerc`, ≥80%) | — |
| Architecture | **import-linter** (`.importlinter`) | manual review (erodes silently) |
| Spine | **OpenSpec** (`openspec/`, pinned `meaningfy` schema, `/opsx:*`) | bespoke `.claude/memory/epics/` (drifts; dies at impl) |
| Domain model (product) | **LinkML** `model/` + `make generate-models` | hand-maintained models (spec-drift) |
| Agent file | **`CLAUDE.md` canonical** + `AGENTS.md` symlink (DEC-4) | two divergent files; AGENTS-canonical |
| Docs | **Antora** (AsciiDoc) | Sphinx (weaker cross-refs), bare MD |
| Task runner | **Makefile** (the dev UX) | tox (env-matrix only; not needed) |

See [`references/decisions.md`](references/decisions.md) for the rationale behind each choice.

## Definition of Done

The scaffold is done when every box in [`references/checklists.md`](references/checklists.md) is
ticked — chiefly: `make install` succeeds; `make check-all` is green on the empty skeleton (lint,
types, architecture, `openspec validate --strict`, a placeholder test); **`CLAUDE.md` exists with
`AGENTS.md` symlinked to it**; `openspec/` is projected (config + pinned schema + `specs/` +
`changes/`); `docs/` builds (`make build-docs`) if docs were selected; CI workflow is present.

## Boundary & Related Skills

**Owns:** the repository scaffold + the spine projection — directory layout, root tool configs, test
harness, the CLAUDE-canonical agentic files, the `openspec/` spine (config + pinned schema + golden
thread), Antora skeleton, CI/infra templates, the conditional `model/` home and the CD TODO stub, and
the setup checklists.
**Delegates:** layering rationale → `cosmic-python`; system design/ADRs → `architecture`; the domain
model + generation → [`../conceptual-modelling/SKILL.md`](../conceptual-modelling/SKILL.md); CD/release
content → [`../ci-cd-delivery/SKILL.md`](../ci-cd-delivery/SKILL.md); EPIC/PLAN content + spec
stewardship → `epic-planning` and the spine; doc prose → `technical-writing`; git mechanics →
`meaningfy-git-workflow`. This skill creates the *containers*; those skills fill them.
**Related:** all of the above, plus the external `superpowers` and `stream-coding` skills.
