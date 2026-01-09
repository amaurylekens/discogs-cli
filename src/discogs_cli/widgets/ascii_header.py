"""ASCII logo header widget."""

from importlib import resources

from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static

from discogs_cli.models import AuthStatus


class AsciiHeader(Widget):
    """Header widget that renders the Discogs ASCII logo."""

    def compose(self) -> ComposeResult:
        logo = (
            resources.files("discogs_cli.assets")
            .joinpath("discogs_ascii.txt")
            .read_text(encoding="utf-8")
        )
        yield Static(logo, id="ascii-header-logo")
        yield Static(self._status_text(self.app.auth_status), id="ascii-header-status")

    @staticmethod
    def _status_text(status: AuthStatus) -> str:
        if status.authorised:
            account = status.account or "unknown"
            return f"([green]●[/green] authorised {account})"
        return "([red]●[/red] not authorised)"
