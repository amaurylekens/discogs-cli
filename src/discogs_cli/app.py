"""Textual application entrypoint."""

from textual.app import App

from discogs_cli.screens.main import MainScreen


class DiscogsApp(App):
    """Discogs TUI application."""

    CSS_PATH = "assets/app.tcss"

    def on_mount(self) -> None:
        self.push_screen(MainScreen())
