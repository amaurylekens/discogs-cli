"""Primary screen for the application."""

from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.screen import Screen
from textual.widgets import Static

from discogs_cli.widgets import AsciiHeader


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
