# Spine Projection — what `openspec/` the skill lays down

How `project-setup` projects the **Meaningfy spine** into a target repo: the `openspec/` tree, the
pinned schema, the `/opsx:*` commands, and the golden-thread pre-wiring. The spine's *conventions*
are owned by `spine/`; this doc is the **mechanics** of laying them down (EPIC-09). It DESCRIBES the
projection; `scripts/scaffold.sh` DOES it.

> Background reading (skillery repo root): the spine README, the EPIC↔change mapping, the workflow
> roster, and the golden thread — `../../../spine/README.md`, `../../../spine/epic-change-memory-mapping.md`,
> `../../../spine/workflows.md`, `../../../spine/golden-thread.md`. The target layout is described in
> `../../../docs/environment/openspec-setup-guide.md`.

## What gets scaffolded

```
openspec/
├── config.yaml                 # schema: meaningfy; injected project context:; the 3 thin rules
├── schemas/meaningfy/          # the meaningfy schema, COPIED PINNED from skillery (schema.yaml + templates/)
├── specs/                      # durable capability specs — THE TRUTH (starts empty; README seed)
└── changes/                    # in-flight changes (README seed: the inputs/ convention)
    └── archive/                # completed changes land here after /opsx:archive
```

| Path | Rendered from | Notes |
|------|---------------|-------|
| `openspec/config.yaml` | `assets/templates/openspec/config.yaml.tmpl` | `schema: meaningfy`; a project-specific `context:` (repo, layering, branch, commit + artifact conventions); the **3 thin per-artifact rules** (proposal no-gos, specs SHALL+GWT, tasks cite-your-parent). |
| `openspec/schemas/meaningfy/` | **copied** from skillery's `openspec/schemas/meaningfy/` | **PINNED** — the copy is frozen per repo (see the refresh path below). |
| `openspec/specs/README.md` | `assets/templates/openspec/specs-README.md.tmpl` | states `specs/` is the truth; `.claude/` is a regenerable index. |
| `openspec/changes/README.md` | `assets/templates/openspec/changes-README.md.tmpl` | documents the per-change layout incl. the **`inputs/` seed convention**. |
| `openspec/changes/archive/` | `keepdir` | empty until the first archive. |

## The artifact shift (supersedes the old `.claude/memory/epics/` model)

The legacy local-file model is **retired**. The spine's native artifacts replace it one-for-one:

| Old (retired) | New (spine native) |
|---------------|--------------------|
| `.claude/memory/epics/<name>/EPIC.md` | `openspec/changes/<id>/proposal.md` (EPIC) |
| `.claude/memory/epics/<name>/PLAN.md` | `openspec/changes/<id>/design.md` + `tasks.md` (PLAN) |
| `.claude/memory/epics/<name>/yyyy-mm-dd-<task>.md` | the change's commits + `tasks.md` checkboxes; merged into `openspec/specs/` on archive |

The scaffolder no longer renders `EPIC.md`/`PLAN.md`/`task.md` skeletons (the `.tmpl` files survive
only as redirect notes). `.claude/` keeps a **regenerable index** (R7): `MEMORY.md` (≤200 lines) +
the optional `agents/` and `skills/` dirs. The truth is `openspec/specs/`; if the index disagrees,
specs/ wins.

## Installing the `/opsx:*` commands + the profile

The schema is copied; the **workflow commands** are installed by OpenSpec itself. Default to the
**core profile** (5 verbs — `propose`, `explore`, `apply`, `sync`, `archive` — deterministic,
non-interactive):

```bash
npx -y @fission-ai/openspec@<pin> init --tools claude --profile core
```

The pin is recorded in the scaffolder (`OPENSPEC_PIN`, kept in sync with
`../../../spine/openspec-version.txt`). The expanded verb set (`new`, `continue`, `ff`, `verify`,
`bulk-archive`, `onboard`) is opt-in per repo via `openspec config` — see
`../../../spine/workflows.md#verb-roster`.

## Golden thread pre-wiring (cite your parent)

The cite-your-parent convention is pre-wired in two places at scaffold time:

- **`openspec/config.yaml`** — the `tasks` rule mandates the PLAN cite its parent EPIC id on the
  first line; the `proposal`/`specs` rules keep EPICs shaped and specs testable.
- **the repo `CLAUDE.md`** — a "Golden thread" note in the spine section restates the chain (EPIC →
  PLAN → specs → commit) so an agent honours it without re-reading `spine/`.

The upper rungs (requirement → architecture) stay convention-only for now — see
`../../../spine/golden-thread.md`.

## Schema refresh path (PINNED per repo — YAGNI)

The schema under `openspec/schemas/meaningfy/` is **pinned**: it is a frozen copy taken at scaffold
time, recorded against the OpenSpec pin (`OPENSPEC_PIN` / `../../../spine/openspec-version.txt`).

**To refresh it, re-run `project-setup`** against the repo:

- a `--dry-run` shows the diff (`+ create` / `= keep`) — it **never clobbers authored specs**
  (`openspec/specs/` and any `openspec/changes/` are left untouched);
- with `--skip-existing` the schema dir is kept if present, so a refresh is a deliberate, reviewed
  act, not an accident.

Treat a schema upgrade as a **documented per-repo chore**: re-run the skill, review the schema diff
in a dedicated commit, re-run `openspec validate --strict`, and reconcile any change the new schema
requires. **We deliberately do NOT build a heavy `--upgrade-schema` tool now** (YAGNI, Q9.1) — note
it only as a *possible future mode* once several repos have actually needed a coordinated bump.

## Validation

`openspec validate --strict` (structural) checks the artifact shape + spec-delta format and is
**CI-automated** (a `make` target). The **clarity gate** (semantic, scores the PLAN ≥9/10) is a
human/agent gate and is **NOT** CI — see `ci-and-infra.md` and
`../../../docs/ai-coding/dod-quality-gates.md` for the automation boundary.
