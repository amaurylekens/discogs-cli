"""OAuth1 flow helpers for Discogs authentication."""

from dataclasses import dataclass

import discogs_client

from discogs_cli.config import AppConfig, OAuthConfig


@dataclass(frozen=True)
class OAuthToken:
    token: str
    secret: str


class DiscogsOAuth:
    def __init__(self, app_config: AppConfig, oauth_config: OAuthConfig) -> None:
        self._app_config = app_config
        self._oauth_config = oauth_config

    def _client(self) -> discogs_client.Client:
        client = discogs_client.Client(self._app_config.user_agent)
        client.set_consumer_key(
            self._oauth_config.consumer_key,
            self._oauth_config.consumer_secret,
        )
        return client

    def get_access_token_interactive(self) -> OAuthToken:
        client = self._client()
        authorize_result = client.get_authorize_url()
        if len(authorize_result) != 3:
            raise RuntimeError("Unexpected OAuth authorize response from discogs_client.")
        first, second, third = authorize_result
        if isinstance(first, str) and first.startswith("http"):
            authorization_url, request_token, request_secret = first, second, third
        else:
            request_token, request_secret, authorization_url = first, second, third
        print("Open this URL in your browser and authorize the app:")
        print(authorization_url)
        verifier = input("Paste the verifier code here: ").strip()

        try:
            access_token, access_secret = client.get_access_token(verifier)
        except TypeError:
            access_token, access_secret = client.get_access_token(
                request_token,
                request_secret,
                verifier,
            )

        return OAuthToken(token=access_token, secret=access_secret)
