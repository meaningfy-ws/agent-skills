# Attribution

The `hulubul_*.yaml` / `hulubul.yaml` LinkML schema files in this directory are a **vendored
copy**, unmodified, of the real conceptual model from the `hulubul-broker` project (a sibling,
private Meaningfy repository — not a dependency of skillery, and not kept in sync automatically).

- **Source:** `hulubul-broker/model/linkml/*.yaml`
- **License:** each file declares `license: https://creativecommons.org/licenses/by/4.0/`
  (CC BY 4.0) — copying with attribution is permitted.
- **Copied:** 2026-07-23, as part of `openspec/changes/linkml-neo4j-generators` (skillery), to
  serve as a real-world richness/regression fixture for the vendored Neo4j-targeting LinkML
  generators (`skills/linkml-engineering/assets/generators/`).

This is a **snapshot fixture**, not a live sync — see
`skills/linkml-engineering/assets/generators/` tests for how it's used, and this change's
`design.md` Error matrix for why it isn't treated as a contract with the source project. Refreshing
it (if `hulubul-broker`'s model changes materially) is a deliberate, manual follow-up, not an
automated or CI-enforced step.
