"""OAuth authorization screen."""

from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Input, Static


class OAuthScreen(ModalScreen[None]):
    """Modal flow for Discogs OAuth1 authorization."""

    def __init__(self) -> None:
        super().__init__()
        self._authorize_url: str | None = None

    def compose(self) -> ComposeResult:
        with Container(id="oauth-dialog"):
            with Vertical(id="oauth-body"):
                yield Static("Authorize Discogs", id="oauth-title")
                yield Static(
                    "Open the URL in your browser, authorize the app, then paste the verifier.",
                    id="oauth-instructions",
                )
                yield Static("", id="oauth-url")
                yield Static("", id="oauth-error")
                yield Input(placeholder="Verifier code", id="oauth-verifier")
                with Horizontal(id="oauth-actions"):
                    yield Button("Cancel", id="oauth-cancel", variant="default")
                    yield Button("Submit", id="oauth-submit", variant="primary")

    def on_mount(self) -> None:
        try:
            request = self.app.start_oauth()
        except Exception as exc:
            self.query_one("#oauth-error", Static).update(str(exc))
            return
        self._authorize_url = request.authorize_url
        self.query_one("#oauth-url", Static).update(self._authorize_url)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "oauth-cancel":
            self.dismiss(None)
            return
        if event.button.id != "oauth-submit":
            return
        verifier = self.query_one("#oauth-verifier", Input).value.strip()
        if not verifier:
            self.query_one("#oauth-error", Static).update("Verifier code is required.")
            return
        try:
            self.app.complete_oauth(verifier)
        except Exception as exc:
            self.query_one("#oauth-error", Static).update(str(exc))
            return
        self.dismiss(None)
