from discogs_cli.__main__ import main


def test_cli_entrypoint_runs():
    # This just checks that the entrypoint imports successfully.
    assert callable(main)
