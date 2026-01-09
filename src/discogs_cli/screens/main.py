"""Primary screen for the application."""

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static

from discogs_cli.widgets import AsciiHeader


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield AsciiHeader()
        yield Static("Welcome to Discogs", id="main-screen")
