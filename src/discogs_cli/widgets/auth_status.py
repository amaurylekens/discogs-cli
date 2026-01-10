"""Authentication status widget."""

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Static

from discogs_cli.models import AuthStatus


class AuthStatusWidget(Horizontal):
    """Shows the current auth status with a lightweight authorize action."""

    def compose(self) -> ComposeResult:
        yield Static(self._status_text(self.app.auth_status), id="auth-status-text")
        yield Button("Authorize", id="auth-status-button", variant="default")

    def on_mount(self) -> None:
        self.update_status(self.app.auth_status)

    def update_status(self, status: AuthStatus) -> None:
        self.query_one("#auth-status-text", Static).update(self._status_text(status))

    @staticmethod
    def _status_text(status: AuthStatus) -> str:
        if status.authorised:
            account = status.account or "unknown"
            return f"([green]●[/green] authorised {account})"
        return "([red]●[/red] not authorised)"
