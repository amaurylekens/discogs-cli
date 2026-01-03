"""Module entrypoint for `python -m discogs_cli`."""

from discogs_cli.app import DiscogsApp
from discogs_cli.config import load_app_config, load_oauth_config
from discogs_cli.services.discogs_client import DiscogsClient
from discogs_cli.services.oauth import DiscogsOAuth


def main() -> None:
    app_config = load_app_config()
    oauth_config = load_oauth_config()
    access_token = DiscogsOAuth(app_config, oauth_config).get_access_token_interactive()
    client = DiscogsClient(app_config=app_config, oauth_config=oauth_config, token=access_token)
    DiscogsApp(client=client).run()


if __name__ == "__main__":
    main()
