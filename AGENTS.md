# Repository Guidelines

## Project Scope & Current Status
This repository contains a Python Textual TUI scaffold. Keep new features aligned with the existing layout and update this guide when conventions change.

## Project Structure & Module Organization
- `src/discogs_cli/` for application code.
- `src/discogs_cli/screens/` for Textual screens, `src/discogs_cli/widgets/` for reusable UI components.
- `src/discogs_cli/services/` for Discogs API integration and other external services.
- `src/discogs_cli/assets/` for Textual CSS (see `src/discogs_cli/assets/app.tcss`).
- `tests/unit/` and `tests/integration/` for automated tests.
- `docs/` for architecture notes, `scripts/` for helper scripts.

## Build, Test, and Development Commands
- `pip install -e ".[dev]"` to install with developer tooling.
- `discogs` or `python -m discogs_cli` to run the TUI locally.
- `pytest` to run the full test suite.
- `ruff check .` to run linting.

## Coding Style & Naming Conventions
- Use ASCII-only source files unless a feature requires Unicode.
- Default indentation: 2 spaces for JSON/YAML/Markdown, 4 spaces for Python.
- File names: kebab-case for docs/scripts, `test_*.py` for tests.
- Keep modules small and typed; prefer one public class per file in `screens/` and `widgets/`.
- Use absolute imports (`from discogs_cli...`) inside the package.

## Testing Guidelines
- Place unit tests in `tests/unit/` and integration tests in `tests/integration/`.
- Name tests as `test_<feature>.py` (e.g., `test_search.py`).
- Keep unit tests fast and deterministic; mock network calls by default.

## Commit & Pull Request Guidelines
- No commit history exists yet; adopt Conventional Commits (`feat:`, `fix:`, `docs:`).
- PRs should include: a short description, linked issue (if any), and test evidence or rationale for skipping.

## Security & Configuration Tips
- Never commit Discogs API tokens or personal data.
- Store secrets in `.env` or a user config file and add it to `.gitignore`.
- OAuth1 uses `DISCOGS_CONSUMER_KEY` and `DISCOGS_CONSUMER_SECRET`; the app prompts for a verifier at startup and keeps the access token in-memory for the session.
- Discogs API docs: https://www.discogs.com/developers
