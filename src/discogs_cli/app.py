"""Main Textual application entrypoint."""

from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Static

from discogs_cli.services.discogs_client import DiscogsClient


class DiscogsApp(App):
    """Discogs Textual app scaffold."""

    CSS_PATH = "assets/app.tcss"
    BINDINGS = [("q", "quit", "Quit")]

    def _load_ascii_art(self) -> str:
        art_path = Path(__file__).resolve().parent / "assets" / "discogs_ascii.txt"
        try:
            return art_path.read_text(encoding="utf-8").rstrip()
        except FileNotFoundError:
            return "Discogs CLI"

    def __init__(self, client: DiscogsClient | None = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.client = client

    def compose(self) -> ComposeResult:
        status = "authenticated" if self.client and self.client.token else "unauthenticated"
        yield Header(show_clock=True)
        yield Static(self._load_ascii_art(), id="ascii-art")
        yield Static(f"Discogs CLI TUI - {status}", id="welcome")
        yield Footer()
