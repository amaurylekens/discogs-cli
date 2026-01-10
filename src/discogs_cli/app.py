"""Textual application entrypoint."""

from textual.app import App

from discogs_cli.models import AuthStatus
from discogs_cli.screens.main import MainScreen
from discogs_cli.services.discogs_auth import DiscogsOAuthService, OAuthRequest


class DiscogsApp(App):
    """Discogs TUI application."""

    CSS_PATH = "assets/app.tcss"
    auth_status: AuthStatus
    oauth_service: DiscogsOAuthService | None

    def __init__(self) -> None:
        super().__init__()
        self.auth_status = AuthStatus()
        self.oauth_service = None

    def on_mount(self) -> None:
        self.push_screen(MainScreen())

    def start_oauth(self) -> OAuthRequest:
        try:
            if self.oauth_service is None:
                self.oauth_service = DiscogsOAuthService.from_env()
            return self.oauth_service.start_authorization()
        except Exception as exc:
            self.auth_status = AuthStatus(authorised=False, error=str(exc))
            raise

    def complete_oauth(self, verifier: str) -> AuthStatus:
        if self.oauth_service is None:
            error = "OAuth service not initialized."
            self.auth_status = AuthStatus(authorised=False, error=error)
            raise RuntimeError(error)
        try:
            status = self.oauth_service.complete_authorization(verifier)
        except Exception as exc:
            self.auth_status = AuthStatus(authorised=False, error=str(exc))
            raise
        self.auth_status = status
        return status
