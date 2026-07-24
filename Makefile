.PHONY: install validate lint test validate-spine fix-spec-links generate-opencode skill-inventory

install:
	python3 -m venv .venv && . .venv/bin/activate && pip install -q -r requirements-dev.txt

# validate = the guardrail (CLI report) + the test suite (incl. negative tests)
validate: lint test

lint:
	. .venv/bin/activate && python -m tools.repo_lint

# fix-spec-links = auto-correct relative-link depth in openspec/specs after an
# `openspec archive` (the archive copies a delta's links verbatim). Run it right
# after archiving; `lint` (broken_links) is the safety net if you forget.
fix-spec-links:
	. .venv/bin/activate && python -m tools.repo_lint --fix

# generate-opencode = regenerate the committed .opencode/ tree from source
# (skills, agents, commands, manifests, parity/gap reports) and sync versions.
# The drift/parity/version-sync/coverage gates run inside `lint` (repo_lint).
generate-opencode:
	. .venv/bin/activate && python -m tools.opencode_gen generate

test:
	. .venv/bin/activate && python -m pytest tests/ -q

# skill-inventory = regenerate docs/skill-inventory.md (purpose + related skills,
# derived from each SKILL.md + marketplace.json). Freshness enforced by
# tests/test_skill_inventory.py, part of `make test`.
skill-inventory:
	. .venv/bin/activate && python -m tools.skill_inventory

# validate-spine = the structural gate on the OpenSpec spine (needs node + npx).
# Kept separate from `validate` so the Python guardrail runs without a node
# toolchain. The clarity gate (semantic, on the PLAN) is run by a human/agent,
# not here. Pinned version lives in spine/openspec-version.txt.
validate-spine:
	@v=$$(cat spine/openspec-version.txt); \
	npx --yes @fission-ai/openspec@$$v schema validate meaningfy && \
	npx --yes @fission-ai/openspec@$$v validate --all --strict
