# Discogs CLI (TUI)

Textual-based terminal UI for browsing and managing Discogs data.

## Quick Start

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
export DISCOGS_CONSUMER_KEY=your_key
export DISCOGS_CONSUMER_SECRET=your_secret
export DISCOGS_USER_AGENT="discogs-cli/0.1 (you@example.com)"
discogs
```

On launch, the app starts the Discogs OAuth1 flow and prompts you to open a URL,
authorize the app, and paste the verifier code back into the terminal.
