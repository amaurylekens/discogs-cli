"""ASCII logo header widget."""

from importlib import resources

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static


class AsciiHeader(Widget):
    """Header widget that renders the Discogs ASCII logo."""

    def compose(self) -> ComposeResult:
        logo = (
            resources.files("discogs_cli.assets")
            .joinpath("discogs_ascii.txt")
            .read_text(encoding="utf-8")
        )
        yield Static(logo, id="ascii-header-logo")
        yield Static("(not authorised)", id="ascii-header-status")
