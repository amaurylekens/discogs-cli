"""Discogs API client placeholder."""

from dataclasses import dataclass

import discogs_client

from discogs_cli.config import AppConfig, OAuthConfig
from discogs_cli.services.oauth import OAuthToken


@dataclass
class DiscogsClient:
    app_config: AppConfig
    oauth_config: OAuthConfig
    token: OAuthToken | None = None

    def client(self) -> discogs_client.Client:
        if not self.token:
            raise RuntimeError("OAuth token missing; authenticate before making API calls.")
        return discogs_client.Client(
            self.app_config.user_agent,
            consumer_key=self.oauth_config.consumer_key,
            consumer_secret=self.oauth_config.consumer_secret,
            token=self.token.token,
            secret=self.token.secret,
        )

    def healthcheck(self) -> bool:
        # Replace with a real API call.
        # Example: self.client().identity()
        return True
