from discogs_cli.app import DiscogsApp


def test_app_constructs():
    app = DiscogsApp()
    assert app is not None
