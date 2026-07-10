# Multi-target generation — see linkml-engineering

Generation is **deterministic and outside the LLM path**: the model is the source, a fixed toolchain
renders the targets. This is a concept `conceptual-modelling` owns *that it happens*; the operational
detail is owned by the LinkML craft skill.

**The `make generate-models` wiring, the first-class target set (Pydantic / JSON Schema / OWL / SHACL),
the enable-on-demand targets, custom generator templates, per-module output, and the
model2owl-as-prerequisite flow all live in
[`../../linkml-engineering/SKILL.md`](../../linkml-engineering/SKILL.md)** and its references:

- Deriving LinkML from an existing model/spec → `linkml-engineering/references/deriving-linkml.md`
- Generation, custom templates, automation, per-module output →
  `linkml-engineering/references/generation-and-templates.md`
- Complete OWL/SHACL element lists → `linkml-engineering/references/owl-shacl-completeness.md`
- Quality gates → `linkml-engineering/references/quality-gates.md`

What stays here: the **source decision** (LinkML-direct vs model2owl-first) and the concept-level
ontology policy — see [`ontology-practices.md`](ontology-practices.md).
