# Architecture

- `src/discogs_cli/app.py` hosts the Textual `App` entrypoint.
- `src/discogs_cli/screens/` contains screen definitions.
- `src/discogs_cli/widgets/` contains reusable UI components.
- `src/discogs_cli/services/` handles Discogs API access.
- `src/discogs_cli/services/oauth.py` runs the OAuth1 flow and returns session tokens.
