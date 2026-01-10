"""Authentication status widget."""

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Static

from discogs_cli.models import AuthStatus
from discogs_cli.screens.oauth import OAuthScreen


class AuthStatusWidget(Horizontal):
    """Shows the current auth status with a lightweight authorize action."""

    def compose(self) -> ComposeResult:
        yield Static(f"{self._status_text(self.app.auth_status)} ", id="auth-status-text")
        yield Button("authorize", id="auth-status-button", variant="default", flat=True)

    @staticmethod
    def _status_text(status: AuthStatus) -> str:
        if status.authorised:
            account = status.account or "unknown"
            return f"([green]●[/green] authorised {account})"
        return "([red]●[/red] not authorised)"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "auth-status-button":
            self.app.push_screen(OAuthScreen())
