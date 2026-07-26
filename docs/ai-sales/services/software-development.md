# Software development

## What it is

This is the building block most people picture when they hear "consulting project": a working
system gets designed and built. Think of it as constructing a building: someone draws the blueprint
before anyone pours a foundation, and nobody trusts a wall that isn't load-bearing. Someone decides
how the pieces fit together (what runs where, what talks to what) and then a team writes, tests,
and ships the code that makes it real. It covers both halves of that: the design decisions (the
blueprint: what to build, why, and how the pieces connect) and the engineering discipline (laying
tested, load-bearing code) that turns those decisions into working software.

## The problem it solves

A client rarely wants "some code." They want a system that keeps working after the people who built
it have moved on: one that a new developer can understand in an afternoon, that doesn't break every
time a requirement changes, and whose design decisions are recorded somewhere instead of living only
in one person's head. This service exists so the client isn't left with a working demo that quietly
becomes unmaintainable, or a pile of undocumented decisions nobody can safely revisit.

## What's included

- System design: the blueprint for what the software's major pieces are, how they talk to each
  other, and the trade-offs behind those choices, recorded as they're made rather than left implicit.
- Contracts defined before code is written: the load-bearing walls of the design (what a service
  accepts and returns), so nothing rests on an aspirational diagram.
- A new repository (or an existing one brought up to standard) set up with the project's standard
  layout, tooling, and automated checks from day one.
- Code organised into clear, independently testable layers, with dependencies enforced in one
  direction so the system doesn't quietly tangle over time.
- Automated tests written alongside the code, not after it, covering the business rules that matter
  most.

Scoped per engagement, see the [Decision Package](../../../skills/decision-package/SKILL.md): a small
build might be one service; a larger one is several, sequenced together.

## What you get (deliverable)

A working, tested system built to that blueprint, plus the design record behind it (the decisions
made, the contracts agreed, and the reasoning for both), so a future team can maintain and extend it
without having to reverse-engineer the original thinking.

## Owning skill(s)

- [`architecture`](../../../skills/architecture/SKILL.md) owns the system-level design: how the
  pieces fit together, the contracts between them, and the record of why each decision was made.
- [`project-setup`](../../../skills/project-setup/SKILL.md) owns scaffolding a new repository (or
  modernising an existing one) to the project's standard.
- [`cosmic-python`](../../../skills/cosmic-python/SKILL.md) owns the code-level discipline: how the
  code inside a service is organised into layers, tested, and kept clean as it grows.

Verified by reading each skill's own file: `architecture` is explicit that it does system design, not
code structure; `cosmic-python` is explicit about the reverse; `project-setup` is explicit that it
scaffolds the container and routes to the other two for the content.

## Where it fits

Software development is usually the block that turns the model and the architecture into something
a client can actually run; see
[`engagement-lifecycle.md#the-outcome-semantic-layer-adoption`](../engagement-lifecycle.md#the-outcome-semantic-layer-adoption)
for how it composes into the whole Semantic Layer.
