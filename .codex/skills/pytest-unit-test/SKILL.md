---
name: pytest-unit-test
description: "Write a pytest unit test for a specified function, instance method, or class method, following our repo conventions in references/pytest_guidelines.md."
---

# Pytest unit test (convention-first)

## Rule 0: conventions win
Before writing or editing tests, **open and follow** `references/pytest_guidelines.md`.
If the repo already has patterns (fixtures, factories, layout), match the repo first; use the guidelines to break ties.

> Note: files under `references/` are not automatically loaded—read them when you need them.

## What to do when invoked

### 1. Identify the unit under test
From the user prompt (and the codebase), determine:
- fully-qualified import path (`package.module:Name` or `package.module.Name`)
- whether it’s a **function**, **instance method**, or **class method**
- sync vs async
- expected outputs or expected exception(s)

If the prompt is vague, infer intent from docstrings, callers, type hints, and existing tests.

### 2. Pick the right test location
- Prefer extending an existing test module that already covers the same area.
- Otherwise create a new test module consistent with the repo layout.

### 3. Design scenarios (minimum useful coverage)
Write tests for:
- the main “happy path”
- at least one meaningful edge/error path (where applicable)

Use parametrization/fixtures/mocking exactly as described in `references/pytest_guidelines.md`.

### 4. Mock boundaries, not internals
Mock external boundaries (network, filesystem, DB, time, randomness, external SDKs).
Patch where the dependency is *used*, not where it’s defined, unless conventions say otherwise.

### 5. Implement + verify
- Keep tests readable and deterministic.
- Run the narrowest pytest command that validates the change (single file/test).
- Ensure the new tests pass.

## Output
- Provide the exact file changes (new/updated test files and any minimal test doubles).
- No production refactors unless strictly needed to enable testing; keep any such change minimal.
