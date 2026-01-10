"""Primary screen for the application."""

from textual import events
from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.screen import Screen
from textual.widgets import Static

from discogs_cli.widgets import AsciiHeader, AuthStatusWidget


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield AsciiHeader()
        with Container(id="main-screen"):
            with Vertical(id="main-content"):
                yield Static("Welcome to Discogs", id="main-title")
                yield Static(
                    "Authorize to browse your collection and access account data.",
                    id="main-subtitle",
                )

    def on_screen_resume(self, event: events.ScreenResume) -> None:
        auth_status = self.app.auth_status
        self.query_one("#auth-status", AuthStatusWidget).update_status(auth_status)
