# Git & Collaboration (Engineering Standard)

Human-readable canon for how we use Git/GitHub and set up dev environments. The **operational**
version — the one agents follow — is the `meaningfy-git-workflow` skill; this document narrates
the policy and the *why*. It does not restate command mechanics.

## Why

Decentralised work (DVCS) plus a central platform (GitHub) only stays sane if history is
readable and reviews are cheap. The conventions below buy that.

## At a glance

- **Commits:** Conventional Commits; imperative-mood summary with **no trailing punctuation**;
  blank line before the body; granular, conceptually atomic commits; squash repeated "fix X"
  commits before sharing. Commit with your **company email**.
- **Branches:** GitFlow — permanent `develop` + `main` (we use `main`; `master` is an accepted
  alias); temporary `feature/`, `release/`, `hotfix/` (lowercase + hyphens). **Never** a commit-type
  prefix (`feat/`, `fix/`, `chore/`, `rel/`). Full table in `meaningfy-git-workflow`.
- **Workflow:** GitFlow for every project; `pull --rebase` on shared branches; rebase to incorporate
  base changes (merge if numerous); merge supporting branches with `--no-ff`; notify peers before a
  force-push of a rebased branch (it is destructive — they must stash first).
- **Pull requests:** main developer opens it; short meaningful title; ≥1 reviewer (four-eyes)
  except small/non-critical/sole-dev; `[WIP]` prefix while in progress; keep the branch current.
- **Free-tier GitHub reality:** private repos get **1 reviewer max** and **no draft PRs** — use
  the `[WIP]` title prefix. Automation must assume this.

## Dev environment

- Editor plugins must exist for your stack (highlighting at minimum).
- **Turn off auto-format for less-common stacks (RDF!)** — it mangles them.
- **Never store a project on the Windows filesystem and reach it through WSL** — keep files in
  WSL; it avoids non-obvious slowdowns (slow `git status`/`diff` from slow indexing).
- Route notifications, or check GitHub every working day.

For the actionable rules an agent follows, see the **`meaningfy-git-workflow`** skill (and its
`references/dev-environment.md`). Commit/PR *mechanics* are delegated to the external
`commit-commands` skill.
