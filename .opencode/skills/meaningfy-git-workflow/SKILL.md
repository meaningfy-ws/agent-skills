---
name: meaningfy-git-workflow
description: Meaningfy git and GitHub conventions — Conventional Commits (imperative, no trailing punctuation), branch naming, rebase/merge etiquette, the pull-request workflow, free-tier GitHub constraints, and dev-environment hygiene. Use when committing, branching, opening or maintaining a PR, or setting up a development environment for a Meaningfy project.
license: Apache 2.0
metadata:
  category: engineering
---

# Meaningfy Git Workflow

## Overview

How we use Git and GitHub at Meaningfy so history stays readable and reviews stay cheap.
This skill owns the **conventions and policy**; it delegates the mechanical *act* of
committing/pushing/opening PRs to the external `commit-commands` skill.

## Commits

- Follow **Conventional Commits** (`type(scope): summary`).
- **Summary line:** imperative mood, **no trailing period or punctuation**; keep it short and
  meaningful (e.g. `feat: add credit-note support`, not `Added credit notes.`).
- **Body:** separated from the summary by one blank line; explain *why*, not *what*.
- Commit often, in **granular, conceptually atomic** chunks so peers can follow the change.
- Avoid successive commits with the same message (`trying to fix X`, `fix X again`). Make them
  locally and **squash** into one before sharing; if already pushed, squash + rebase + force-push
  at the end.
- Use the developer's **company email** for company projects (set globally or per-repo).

## Branch naming

**GitFlow** is the standard branching model. Branch names are **lowercase + hyphens only** — no
underscores, no spaces, and **never** a commit-type prefix (`feat/`, `fix/`, `chore/`, `rel/`, …):
those belong to *commit messages*, not branches.

**Permanent branches** (never delete, never commit directly):

- `main` — production history. We use `main`; `master` is an accepted alias. Every merge is tagged
  `vX.Y.Z`.
- `develop` — integration branch for the next release. A repo always has both.

**Temporary branches** (delete after merge; merge with `--no-ff` to preserve grouping):

| Prefix | Branch off | Merge back into | Name |
|--------|-----------|-----------------|------|
| `feature/` | `develop` | `develop` | `feature/<descriptor>` or `feature/<author>/<ticket-id>` (e.g. `feature/login-ui`, `feature/ec/PROJ-123`) |
| `release/` | `develop` | `main` **and** `develop` | `release/<version>` (e.g. `release/1.2.0`) |
| `hotfix/`  | `main`    | `main` **and** `develop` | `hotfix/<version>` or `hotfix/<issue>` (e.g. `hotfix/1.2.1`) |

Prefer the ticketing system's branch-name feature (e.g. Jira) to generate a `feature/` name. The
`release/` + `hotfix/` *lifecycle* (cut-from, back-merge, tagging) is owned by
[`meaningfy-release`](../meaningfy-release/SKILL.md) — this skill owns only the branch *shape*.

## Workflow

- **GitFlow is the model for every project** — always a `develop` and a `main`/`master`, with
  `feature/` / `release/` / `hotfix/` supporting branches (above). A client may dictate extra
  process, but the branch model and names are the Meaningfy default.
- On a shared feature branch, use `git pull --rebase` (not plain `pull`).
- Use **rebase** to incorporate base-branch changes and keep history clean — **unless** the
  changes are numerous, in which case **merge**. Once you merge into a branch, do not rebase it
  again for its lifetime (unless redoing the whole history before final merge).
- After a **force-push** of a rebased branch, notify other developers to `reset --hard` (or
  delete + refetch); they must stash/save work first — it is destructive.

## Pull Requests

- The feature's **main developer** opens the PR (another dev may open it in their stead).
- Give the PR a **short, meaningful title** — not the verbatim branch name.
- Assign **at least one reviewer** (four-eyes), except for small/non-critical/non-functional
  changes or when sole-developer; assign at least one assignee (may be yourself) as the merger.
- Mark work-in-progress with a **`[WIP]`** title prefix or the draft feature; remove it and
  notify reviewers when ready.
- Keep the PR branch up to date against its base (rebase for small changes; merge for large).

## Free-tier GitHub constraints

We do not use paid GitHub plans, so on private repos: **reviewers are limited to 1**, and
**draft PRs are not available** — use the **`[WIP]` title prefix** instead of a draft. Any PR
automation must assume this, not the paid-tier feature set.

## Dev-environment hygiene

See `references/dev-environment.md` (WSL filesystem trap, RDF auto-format warning, editor
plugins, notification routing).

## Boundary & Related Skills

**Owns:** VCS/PR conventions + dev-environment hygiene. **Does NOT own:** code structure
(`cosmic-python`), the mechanical commit/push/PR *commands* (external `commit-commands`), or the
**release/hotfix branch lifecycle + versioning** (`meaningfy-release` — this skill owns only the
branch *mechanics* it builds on).
**Related:** `cosmic-python`, `meaningfy-release`, `commit-commands` (external), `code-review`
(external) + `meaningfy-code-review` (the checklist).
