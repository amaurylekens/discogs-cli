"""Discogs API client placeholder."""

from dataclasses import dataclass

from authlib.integrations.requests_client import OAuth1Session

from discogs_cli.config import AppConfig, OAuthConfig
from discogs_cli.services.oauth import OAuthToken


@dataclass
class DiscogsClient:
    app_config: AppConfig
    oauth_config: OAuthConfig
    token: OAuthToken | None = None

    def session(self) -> OAuth1Session:
        if not self.token:
            raise RuntimeError("OAuth token missing; authenticate before making API calls.")
        session = OAuth1Session(
            self.oauth_config.consumer_key,
            self.oauth_config.consumer_secret,
            token=self.token.token,
            token_secret=self.token.secret,
        )
        session.headers.update({"User-Agent": self.app_config.user_agent})
        return session

    def healthcheck(self) -> bool:
        # Replace with a real API call.
        # Example: session.get(f"{self.app_config.api_base_url}/database/search")
        return True
