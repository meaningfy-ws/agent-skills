# Editor guardrails

The checks a modeller applies **while working** — before generating anything downstream. They are the
live, per-edit version of the conventions: cheap questions that catch a smell at authoring time instead
of at generation time. A consuming skill (e.g. `linkml-engineering`) may add representation-specific
guardrails on top of these, or turn them into an automated lint rule.

## Per-edit checklist

When you add or change a modelled element, confirm:

- **Reuse first.** Does this attribute already exist as a property elsewhere? If yes, reference it. If
  it recurs, promote it to a reusable property now, not later.
- **Identity present.** Does this element resolve to a stable URI (implicitly, via the minted
  namespace)? If it needs an explicit one, is it because it reuses a published term?
- **Closed set → enumeration.** Are any values drawn from a fixed set? Model the set, don't inline the
  strings.
- **Definition written.** Does every new class and property have a real prose definition?
- **Constraint in the model.** Any required-ness, cardinality, bound, pattern, or uniqueness — is it
  declared in the model rather than left to code?
- **Cohesion held.** Did this class just grow a fifth unrelated responsibility? If so, split it.
- **Vocabulary reuse considered.** Is there a published term this maps onto? Prefer mapping over
  minting.

## Turning guardrails into guardrails-as-code

These checks graduate from human discipline to enforcement in the consuming skill:

- A **schema linter** (owned by the representation skill) enforces naming, missing-definition, and
  metadata rules — run it without muting warnings.
- A **review pass** (see the code-review family) treats a surviving anti-pattern as a finding.
- A **CI gate** fails the build when the model regresses (e.g. a bare string reintroduced where an
  enum was).

Where and how to wire these is representation-specific; the *intent* — catch the smell as early as the
edit — is the guardrail this file owns.
