# Project Quality & CI/CD Configuration (Real Examples)

**From:** mapping-suite-sdk

This document shows how to set up Makefile, tox, pylint, importlinter, and CI/CD to enforce Clean Architecture automatically.

## 1. Makefile: Standard Developer Workflow

**mapping-suite-sdk/Makefile** (key sections):

```makefile
SHELL=/bin/bash -o pipefail

# Color codes for output
BUILD_PRINT = \e[1;34m
END_BUILD_PRINT = \e[0m
ICON_DONE = [✔]
ICON_ERROR = [x]
ICON_PROGRESS = [-]

#---------------------------------------------
# Installation & Setup
#---------------------------------------------

install: install-poetry
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Installing requirements$(END_BUILD_PRINT)"
	@ poetry lock
	@ poetry install --all-groups
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Installation complete$(END_BUILD_PRINT)"

install-poetry:
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Installing Poetry$(END_BUILD_PRINT)"
	@ pip install "poetry==2.0.1"
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Poetry installed$(END_BUILD_PRINT)"

#---------------------------------------------
# Testing & Code Quality
#---------------------------------------------

test-unit: generate-models
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Running unit tests$(END_BUILD_PRINT)"
	@ poetry run tox
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Tests passed$(END_BUILD_PRINT)"

lint:
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Running Pylint$(END_BUILD_PRINT)"
	@ poetry run pylint --rcfile=.pylintrc ./mapping_suite_sdk ./tests
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Lint check passed$(END_BUILD_PRINT)"

lint-report:
	@ poetry run pylint --rcfile=.pylintrc --recursive=y ./mapping_suite_sdk ./tests | tail -n 3 > pylint_report.txt || true
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Report: pylint_report.txt$(END_BUILD_PRINT)"

# Clean Code checks: complexity + maintainability
check-clean-code: _check-complexity _check-maintainability
	@ poetry run xenon mapping_suite_sdk --max-absolute C --max-modules C --max-average A
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Clean Code checks passed$(END_BUILD_PRINT)"

_check-complexity:
	@ echo -e "$(BUILD_PRINT)=== Cyclomatic Complexity ===$(END_BUILD_PRINT)"
	@ poetry run radon cc mapping_suite_sdk -a --total-average

_check-maintainability:
	@ echo -e "$(BUILD_PRINT)=== Maintainability Index ===$(END_BUILD_PRINT)"
	@ poetry run radon mi mapping_suite_sdk --show --sort

# Architecture boundaries
check-architecture:
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Checking architectural boundaries$(END_BUILD_PRINT)"
	@ poetry run lint-imports
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Architecture check passed$(END_BUILD_PRINT)"

# Full quality pipeline
all-quality-checks: lint check-architecture check-clean-code test-unit
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) All quality checks passed!$(END_BUILD_PRINT)"

#---------------------------------------------
# Code Generation (Schema-based)
#---------------------------------------------

generate-models:
	@ echo -e "$(BUILD_PRINT)$(ICON_PROGRESS) Generating Python models from LinkML$(END_BUILD_PRINT)"
	@ $(MAKE) generate-models-recursive
	@ $(MAKE) optimize-models-imports
	@ echo -e "$(BUILD_PRINT)$(ICON_DONE) Models generated$(END_BUILD_PRINT)"

#---------------------------------------------
# Documentation
#---------------------------------------------

build-docs: run-antora
clean-docs:
	@ rm -rfv docs/build
```

**Key Patterns:**
- ✅ Colored output for readability
- ✅ `@` suppresses echo, `echo` shows output
- ✅ Separate targets for each concern
- ✅ `make all-quality-checks` runs everything (CI/CD runs this)
- ✅ Documentation generation included

## 2. Tox: Isolated Test Environments

**mapping-suite-sdk/tox.ini**:

```ini
[tox]
isolated_build = True
envlist = py312, architecture, clean-code
skip_missing_interpreters = True


[testenv]
skip_install = True
allowlist_externals =
    poetry
    python
commands_pre =
    poetry install --sync
passenv =
    PYTHONPATH
    PYTHON*
    HOME


# Main test environment: Python 3.12 unit tests + coverage
[testenv:py312]
description = Run unit tests and coverage analysis
commands =
    pytest tests/unit \
        --cov={env:PACKAGE_NAME:mapping_suite_sdk} \
        --cov-report=term \
        --cov-report=term-missing:skip-covered \
        --cov-report=xml:coverage.xml \
        -v \
        {posargs}


# Coverage configuration
[coverage:run]
branch = True
source = mapping_suite_sdk

[coverage:report]
precision = 2
show_missing = True
skip_empty = True
sort = Cover
exclude_lines =
    pragma: no cover
    def __repr__
    if self\.debug
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:

# ENFORCE: Fail if coverage < 80%
fail_under = 80

[coverage:xml]
output = coverage.xml


# Pytest configuration
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --strict-markers
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    integration: marks tests as integration tests


# Architecture validation: Import linter
[testenv:architecture]
description = Validate architectural boundaries (Cosmic Python)
commands =
    lint-imports


# Clean Code validation
[testenv:clean-code]
description = Check code complexity and maintainability
commands =
    # Cyclomatic Complexity - A (1-5) = simple, B (6-10) = manageable, C (11-20) = complex
    radon cc mapping_suite_sdk -a --total-average --show-complexity

    # Maintainability Index - A = best, C = worst
    radon mi mapping_suite_sdk --show --sort

    # Fail if exceeds thresholds
    xenon mapping_suite_sdk \
        --max-absolute C \
        --max-modules C \
        --max-average B \
        --exclude "*test*,*__pycache__*"

[testenv:clean-code-report]
description = Generate detailed complexity report (no failures)
commands =
    radon cc mapping_suite_sdk -a --total-average --show-complexity --json > reports/complexity.json
    radon mi mapping_suite_sdk --show --json > reports/maintainability.json
    radon hal mapping_suite_sdk
```

**Key Patterns:**
- ✅ `py312` = unit tests with 80% coverage requirement
- ✅ `architecture` = lint-imports (boundary validation)
- ✅ `clean-code` = complexity and maintainability checks
- ✅ `isolated_build = True` = dependencies fully isolated
- ✅ `--cov-report=xml` = SonarCloud integration
- ✅ Markers for selective testing (`@pytest.mark.slow`)

## 3. Pylint: Code Quality & Style

**mapping-suite-sdk/.pylintrc**:

```ini
[MASTER]
ignore=CVS, tests
persistent=yes
load-plugins=

[MESSAGES CONTROL]
# Disable specific warnings (pragmatic choices)
disable=C0111,  # missing-docstring (docstrings are good, but enforcing everywhere is overkill)
        C0103,  # invalid-name (sometimes 'x', 'y' are appropriate)
        C0301,  # line-too-long (handled by formatter)
        C0303,  # trailing-whitespace
        C0305,  # trailing-newlines
        C0321,  # multiple-statements
        C0415,  # import-outside-toplevel (sometimes necessary)
        W0107,  # unnecessary-pass
        W0221,  # arguments-differ (acceptable in overrides)
        W0311,  # bad-indentation
        W0511,  # fixme (TODO comments are OK)
        W0603,  # global-statement
        W0613,  # unused-argument (sometimes intentional)
        W0707,  # raise-missing-from
        R0903,  # too-few-public-methods (dataclasses often have few methods)
        R0913,  # too-many-arguments (accept longer signatures for clarity)
        R0914,  # too-many-locals
        R1705,  # no-else-return
        R1711,  # useless-return
        R0801,  # duplicate-code
        E1134   # not-a-mapping (false positive with config objects)

[REPORTS]
output-format=text
reports=no
score=yes

[BASIC]
# Good names: single-letter, common abbreviations
good-names=i,j,k,v,e,ex,f,fp,fd,x,y,z,id,pk,db,df,dt,ts,tz,io,ok,_,__,Run,log,url,uri,api,sql,xml,json,csv,ttl,rdf,ns,ctx,cfg,tmp

# Bad names: generic, unhelpful
bad-names=foo,bar,baz,toto,tutu,tata,temp,tmp2,tmp3,data,info,obj,item,thing,stuff,do_stuff,handle,process,manager,helper,util,utils,utility,common,misc,base,abstract,generic,value,result,output,input,flag,flag1,flag2,aux,auxiliary

function-rgx=[a-z_][a-z0-9_]{2,30}$

[DESIGN]
max-attributes=7
max-locals=15
max-branches=12
max-statements=50
```

**Key Patterns:**
- ✅ Disable checks that are too strict (e.g., C0111 docstring everywhere)
- ✅ Allow pragmatic code patterns (unused arguments, multi-statement lines)
- ✅ Define "good names" vs "bad names"
- ✅ Set reasonable complexity thresholds

## 4. Import Linter: Enforce Architectural Boundaries

**mapping-suite-sdk/.importlinter**:

```yaml
[importlinter]
root_package = mapping_suite_sdk
max_workers = 4

[importlinter:contract:1]
name = Architecture: No circular imports
type = forbidden
source_modules =
    mapping_suite_sdk.core
destination_modules =
    mapping_suite_sdk.mapping_package_v1
    mapping_suite_sdk.mapping_package_v2
    mapping_suite_sdk.mapping_package_v3
    mapping_suite_sdk.tools

[importlinter:contract:2]
name = Architecture: Core can't import from tools or versioned packages
type = forbidden
source_modules =
    mapping_suite_sdk.core
destination_modules =
    mapping_suite_sdk.tools
    mapping_suite_sdk.mapping_package_v1
    mapping_suite_sdk.mapping_package_v2
    mapping_suite_sdk.mapping_package_v3

[importlinter:contract:3]
name = Architecture: Models don't import from services or adapters
type = forbidden
source_modules =
    mapping_suite_sdk.*.models
destination_modules =
    mapping_suite_sdk.*.services
    mapping_suite_sdk.*.adapters

[importlinter:contract:4]
name = Architecture: Adapters don't import from services or entrypoints
type = forbidden
source_modules =
    mapping_suite_sdk.*.adapters
destination_modules =
    mapping_suite_sdk.*.services
    mapping_suite_sdk.*.entrypoints
    mapping_suite_sdk.tools.entrypoints

[importlinter:contract:5]
name = Architecture: Services don't import from entrypoints
type = forbidden
source_modules =
    mapping_suite_sdk.*.services
destination_modules =
    mapping_suite_sdk.*.entrypoints
    mapping_suite_sdk.tools.entrypoints
```

**Key Patterns:**
- ✅ Explicit contracts (forbidden imports)
- ✅ Names describe intent ("Architecture: ...")
- ✅ One contract per boundary rule
- ✅ Ran as `make check-architecture` or `tox -e architecture`

## 5. CI/CD Configuration (GitHub Actions)

**Example workflow for mapping-suite-sdk**:

```yaml
name: Quality Checks & Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

jobs:
  quality:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.12"]

    steps:
      - uses: actions/checkout@v4

      # Setup Python & Poetry
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
          cache: 'poetry'

      - name: Install dependencies
        run: |
          pip install poetry
          poetry install --all-groups

      # Code Quality Checks
      - name: Lint with Pylint
        run: make lint
        continue-on-error: false

      - name: Check Architecture (Import Linter)
        run: make check-architecture
        continue-on-error: false

      - name: Check Clean Code
        run: make check-clean-code
        continue-on-error: false

      # Testing
      - name: Run unit tests with coverage
        run: make test-unit

      # Upload coverage to SonarCloud
      - name: Upload coverage to SonarCloud
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}

      # Build & publish (optional)
      - name: Build package
        if: success()
        run: poetry build

      - name: Publish to PyPI (on release)
        if: startsWith(github.ref, 'refs/tags/')
        run: poetry publish --username __token__ --password ${{ secrets.PYPI_TOKEN }}
```

**Key Patterns:**
- ✅ Matrix testing (different Python versions)
- ✅ Poetry caching (`cache: 'poetry'`)
- ✅ All checks before tests (fail fast)
- ✅ SonarCloud integration (coverage reports)
- ✅ Conditional publishing (only on tags)

## 6. Quality Gates in Makefile

**Recommended CI/CD invocation**:

```bash
# Developer runs before committing
make all-quality-checks

# CI/CD runs (more comprehensive)
make install
make generate-models
make lint-report
make all-quality-checks
# Then upload to SonarCloud if all pass
```

**Exit codes matter:**
- `0` = all checks passed
- `1` = tests or quality checks failed
- `2` = architecture boundaries violated
- `3` = coverage below threshold

## 7. Summary: The Quality Pyramid

```
        SonarCloud (cloud analysis)
              ↑
      Complexity & Maintainability
              ↑
       Architecture Boundaries
              ↑
        Code Style (Pylint)
              ↑
    Unit Tests + Coverage (80%+)
              ↑
        Code Compilation
```

**Each level must pass for CI/CD to succeed:**

```bash
# Level 1: Can code compile?
python -m py_compile mapping_suite_sdk/**/*.py

# Level 2: Do unit tests pass + 80% coverage?
make test-unit

# Level 3: Does code follow style rules?
make lint

# Level 4: Are boundaries respected?
make check-architecture

# Level 5: Is complexity acceptable?
make check-clean-code

# Level 6: Cloud analysis (SonarCloud)
# Automatic after merge
```

## 8. Local Development Workflow

```bash
# Setup once
make install

# Before each commit
make all-quality-checks

# Quick check during development
make test-unit      # Fast (unit tests only)
make lint           # Quick style check
make check-architecture  # Boundary check

# Full check before pushing
make all-quality-checks

# After making big changes
make lint-report    # Generate report
make check-clean-code  # Detailed complexity analysis
```

## Summary

**Project-level quality automation:**
- ✅ Makefile: Standard targets (`install`, `test-unit`, `lint`, `check-architecture`)
- ✅ Tox: Isolated test environments, 80% coverage enforced
- ✅ Pylint: Code style with pragmatic disables
- ✅ Import Linter: Architectural boundary enforcement
- ✅ GitHub Actions: Automated CI/CD with SonarCloud
- ✅ Quality pyramid: Compile → Tests → Style → Architecture → Complexity → Cloud
- ✅ Exit codes: Meaningful failures for automated tooling

**Result:** Code quality is enforced, not just suggested. Developers can't merge broken code.
