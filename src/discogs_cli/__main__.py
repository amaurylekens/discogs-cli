"""Module entrypoint for `python -m discogs_cli`."""

from discogs_cli.app import DiscogsApp


def main() -> None:
    DiscogsApp().run()


if __name__ == "__main__":
    main()
