"""Textual application entrypoint."""

from textual.app import App

from discogs_cli.models import AuthStatus
from discogs_cli.screens.main import MainScreen


class DiscogsApp(App):
    """Discogs TUI application."""

    CSS_PATH = "assets/app.tcss"
    auth_status: AuthStatus

    def __init__(self) -> None:
        super().__init__()
        self.auth_status = AuthStatus()

    def on_mount(self) -> None:
        self.push_screen(MainScreen())
