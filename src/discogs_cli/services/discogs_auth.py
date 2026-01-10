"""OAuth1 workflow for Discogs."""

from __future__ import annotations

from dataclasses import dataclass
import os

import discogs_client

from discogs_cli.models import AuthStatus


@dataclass
class OAuthRequest:
    token: str
    secret: str
    authorize_url: str


class DiscogsOAuthService:
    """Discogs OAuth1 helper using discogs_client."""

    def __init__(self, client: discogs_client.Client) -> None:
        self._client = client
        self._request: OAuthRequest | None = None

    @classmethod
    def from_env(cls) -> DiscogsOAuthService:
        user_agent = os.getenv("DISCOGS_USER_AGENT")
        consumer_key = os.getenv("DISCOGS_CONSUMER_KEY")
        consumer_secret = os.getenv("DISCOGS_CONSUMER_SECRET")
        missing = [
            name
            for name, value in [
                ("DISCOGS_USER_AGENT", user_agent),
                ("DISCOGS_CONSUMER_KEY", consumer_key),
                ("DISCOGS_CONSUMER_SECRET", consumer_secret),
            ]
            if not value
        ]
        if missing:
            raise RuntimeError(f"Missing Discogs env vars: {', '.join(missing)}")
        client = discogs_client.Client(
            user_agent,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
        )
        return cls(client)

    def start_authorization(self) -> OAuthRequest:
        token, secret, authorize_url = self._client.get_authorize_url()
        self._request = OAuthRequest(
            token=token,
            secret=secret,
            authorize_url=authorize_url,
        )
        return self._request

    def complete_authorization(self, verifier: str) -> AuthStatus:
        if self._request is None:
            raise RuntimeError("Authorization has not been started.")
        access_token, access_secret = self._client.get_access_token(verifier)
        self._client.set_token(access_token, access_secret)
        identity = self._client.identity()
        account = getattr(identity, "username", None)
        return AuthStatus(
            authorised=True,
            account=account,
            access_token=access_token,
            access_token_secret=access_secret,
        )
