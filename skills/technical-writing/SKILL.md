---
name: technical-writing
description: Produce clear documentation, explanations, summaries, and docstrings — AsciiDoc/Antora or Markdown — with a lightweight clarity check. Use to write or improve project docs, explain how a module works, summarise an area, or add docstrings. Trigger on "document this", "write docs/README", "explain how X works", "add docstrings", "summarise this module".
license: Apache 2.0
metadata:
  category: ai-coding
---

# Technical Writing

## Overview

Clear, concise documentation, explanations, and summaries. Aligns with the project's
established terminology (read `MEMORY.md` and existing docs first).

## What you produce

- **Code explanations** for onboarding/knowledge transfer (suggest a stronger model for deep
  architectural analysis).
- **Summaries** of modules, epics, or areas.
- **Docstrings** — Google style unless the project uses another convention (check existing code).
- **Documentation pages** — AsciiDoc (Antora) or Markdown for `docs/`.
- **README updates.**

## Clarity check (apply to everything you write)

Apply the **lightweight clarity check owned by [`clarity-gate`](../clarity-gate/SKILL.md)**
(actionable · current · specific references · single-source). It is defined there; this skill
*applies* it to prose and does not restate the criteria. The full 13-item gate (for specs) also
lives in `clarity-gate`.

## Writing style

- Direct language, no fluff. Prefer tables and lists over long prose.
- Code examples where they clarify; file:line references when explaining code.
- AsciiDoc: follow Antora conventions (`docs/antora.yml`, `docs/antora-playbook.yml`).
- Markdown: standard GitHub-flavored.

### Explanation sub-mode

The defaults above suit Reference and How-to docs. When the page is a Diátaxis **Explanation** (an
explainer, a "how X works" narrative, broad-audience teaching prose), borrow the texture craft from
[`explanatory-writing`](../explanatory-writing/SKILL.md) — one controlling metaphor, a concrete
example beside every abstract claim, self-answered question pivots. The terse/tables default still
governs Reference and How-to output.

## Boundary & Related Skills

**Owns:** documentation, explanations, summaries, docstrings. **Does NOT** plan (`epic-planning`),
run the full clarity gate (`clarity-gate`), or write/modify production code or tests.
**Related:** `clarity-gate` (full gate), `epic-planning`, `explanatory-writing` (Explanation-quadrant texture), `writing-antipatterns` (genre-conditional failure modes for Tutorial/How-to/Reference).
