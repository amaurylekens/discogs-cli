"""Textual application entrypoint."""

from __future__ import annotations

from textual import on
from textual.app import App
from textual.widgets import Button
from dotenv import load_dotenv

from discogs_cli.models import AuthStatus
from discogs_cli.screens.main import MainScreen
from discogs_cli.screens.oauth import OAuthScreen
from discogs_cli.services.discogs_auth import DiscogsOAuthService, OAuthRequest
from discogs_cli.widgets import AuthStatusWidget


class DiscogsApp(App):
    """Discogs TUI application."""

    CSS_PATH = "assets/app.tcss"
    ENABLE_MOUSE = True
    auth_status: AuthStatus
    oauth_service: DiscogsOAuthService | None

    def __init__(self) -> None:
        super().__init__()
        load_dotenv()
        self.auth_status = AuthStatus()
        self.oauth_service = None

    def on_mount(self) -> None:
        self.push_screen(MainScreen())

    def update_auth_status(self, status: AuthStatus) -> None:
        self.auth_status.authorised = status.authorised
        self.auth_status.account = status.account
        self.auth_status.access_token = status.access_token
        self.auth_status.access_token_secret = status.access_token_secret
        self.auth_status.error = status.error
        try:
            widget = self.query_one("#auth-status", AuthStatusWidget)
        except Exception:
            return
        widget.update_status(status)

    @on(Button.Pressed, "#auth-status-button")
    def _open_oauth(self, event: Button.Pressed) -> None:
        self.push_screen(OAuthScreen())

    def start_oauth(self) -> OAuthRequest:
        try:
            if self.oauth_service is None:
                self.oauth_service = DiscogsOAuthService.from_env()
            return self.oauth_service.start_authorization()
        except Exception as exc:
            self.update_auth_status(AuthStatus(authorised=False, error=str(exc)))
            raise

    def complete_oauth(self, verifier: str) -> AuthStatus:
        if self.oauth_service is None:
            error = "OAuth service not initialized."
            self.update_auth_status(AuthStatus(authorised=False, error=error))
            raise RuntimeError(error)
        try:
            status = self.oauth_service.complete_authorization(verifier)
        except Exception as exc:
            self.update_auth_status(AuthStatus(authorised=False, error=str(exc)))
            raise
        self.update_auth_status(status)
        return status
