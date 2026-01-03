"""Primary screen for the application."""

from textual.screen import Screen
from textual.widgets import Static


class MainScreen(Screen):
    def compose(self):
        yield Static("Welcome to Discogs", id="main-screen")
