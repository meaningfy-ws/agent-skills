> Parent: `openspec/changes/step-by-step-install-guide/proposal.md` (EPIC: Linear, copy-paste install checklist per CLI)

## Context

Install content already exists and is correct — `README.md` → `docs/environment-setup.md` →
`docs/dual-cli/setup-claude.md` / `setup-opencode.md` (see DEC-1 in the EPIC: the runbooks are the
per-CLI documentation-split target per the `dual-cli-distribution` spec). The problem is
presentation: `setup-claude.md` today is organized as five headed sections ("1. Install bundles",
"2. Root binding", …) that mix a runnable command, a paragraph of rationale, and a forward
cross-reference in the same block. A reader following it has to parse which of those three things
to *act on*. This design rewrites the two runbooks into a stricter literal format and adjusts the
two pointer docs (`README.md`, `environment-setup.md`) to stop restating steps the runbooks now own.

## Goals / Non-Goals

**Goals:**
- Each numbered step in a runbook contains exactly one action: a shell/slash command block, or a
  single external link, plus at most one line of "why" — never a paragraph to interpret.
- External dependencies (`superpowers`, `ponytail`, `stream-coding`, `@fission-ai/openspec`) get
  their upstream link inline at the step that installs them, not only in a separate table.
- Each runbook ends in a verification step: a command the reader runs and a description of the
  expected output, so success/failure is legible without guessing.
- `README.md` and `environment-setup.md` reference the runbook step sequence instead of duplicating
  it — one sequence, read from one of two files depending on CLI choice.

**Non-Goals:**
- No change to *which* bundles, dependencies, or versions are installed (per EPIC no-gos).
- No new install automation (script, Makefile target) — docs only.
- No rewrite of `mapping.md` or `compatibility.md`; they may be linked, not restructured.

## Decisions

- Cites EPIC **DEC-1**: rewrite target is the existing runbooks, not a new quickstart file.
- Cites EPIC **DEC-2**: one runnable artifact per step.
- Cites EPIC **DEC-3**: each runbook ends with a verification step.
- New for design: keep the existing external-dependency table in `environment-setup.md` as the
  canonical version-pin source; runbook steps link to it for pins rather than re-quoting version
  numbers, so a version bump only needs updating in one place (avoids the drift the EPIC's
  rabbit-hole warns about).

## Algorithm / approach

Runbook shape (applies to both `setup-claude.md` and `setup-opencode.md`, CLI-native per step):

```
# Setup — <CLI>

Step 1 — Prerequisites
  - link: CLI install/docs URL
  - command (if any): version check, e.g. `node -v` (Node ≥ 18)

Step 2 — Add the marketplace / plugin source
  - command: exact copy-paste block

Step 3 — Install your bundles
  - command: exact copy-paste block per bundle, with a one-line "install if you… " note

Step 4 — Install mandatory external dependencies
  - one sub-step per dependency (superpowers, ponytail, stream-coding, OpenSpec):
    external link (upstream repo/marketplace) + exact install command

Step 5 — Root binding
  - confirmation only (files ship in the repo) — state what to check, not an action to perform

Step 6 — Wire the spine (per project)
  - command: openspec init / project-setup invocation, linked

Step 7 — Optional: hooks, MCP servers
  - link to hooks/README.md and mcp-setup.md, one line each

Step 8 — Verify
  - command whose output confirms install (e.g. list installed skills/plugins, or
    `openspec --version`)
  - expected output described
```

Worked example (Step 4, superpowers, Claude runbook):

```
**Superpowers** — TDD, debugging, brainstorming, verification disciplines.
Upstream: https://github.com/obra/superpowers (or the pinned marketplace source already in use)
    /plugin install superpowers@claude-plugins-official
```

### Anti-patterns

- ❌ A step that says "see the table below for details" without the reader being able to act from
  the step alone — forces a jump back into reference prose.
- ❌ Re-quoting a version number or dependency list already pinned in `environment-setup.md` —
  creates two sources that can drift; link instead.
- ❌ Mixing two CLIs' commands in one runbook "for completeness" — a reader on opencode should never
  see a `/plugin` command.

## Error matrix

| Failure mode | Expected handling |
|---|---|
| Reader is missing a prerequisite (e.g. Node < 18) | Step 1's version-check command fails visibly before later steps are attempted |
| A mandatory external dependency's upstream link/name has drifted | Runbook step links out; if the linked install command 404s, the existing `compatibility.md` drift-warning process (already documented) is the escalation path — not re-solved here |
| Reader runs opencode steps on Claude or vice versa | Each runbook states its CLI in the title and Step 1; no shared/ambiguous step exists to run by mistake |
| Verification step fails | Step 8 names what "success" looks like, so a mismatch is self-diagnosing rather than silent |

## Risks / Trade-offs

- [Risk] Splitting content across "runbook = steps" vs "environment-setup.md = version pins" could
  still let the two drift apart. → Mitigation: runbook steps link to the pin table rather than
  copy values, so there is exactly one place version numbers live (see Decisions).
- [Risk] More prescriptive step-by-step text is more to maintain when a bundle/dependency changes.
  → Mitigation: no new content is invented — this reshapes existing table/prose content already
  maintained under the `dual-cli-distribution` spec's documentation-split requirement.

## Open Questions

None — scope is bounded to the two runbooks + two pointer docs named in the EPIC's Impact section.
