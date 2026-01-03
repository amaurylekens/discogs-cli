"""OAuth1 flow helpers for Discogs authentication."""

from dataclasses import dataclass
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from authlib.integrations.requests_client import OAuth1Session

from discogs_cli.config import AppConfig, OAuthConfig


@dataclass(frozen=True)
class OAuthToken:
    token: str
    secret: str


class DiscogsOAuth:
    def __init__(self, app_config: AppConfig, oauth_config: OAuthConfig) -> None:
        self._app_config = app_config
        self._oauth_config = oauth_config

    def _build_authorize_url(self, request_token: dict[str, str]) -> str:
        parsed = urlparse(self._oauth_config.authorize_url)
        query = dict(parse_qsl(parsed.query))
        query["oauth_token"] = request_token["oauth_token"]
        return urlunparse(parsed._replace(query=urlencode(query)))

    def get_access_token_interactive(self) -> OAuthToken:
        session = OAuth1Session(
            self._oauth_config.consumer_key,
            self._oauth_config.consumer_secret,
            redirect_uri=self._oauth_config.callback_uri,
        )
        session.headers.update({"User-Agent": self._app_config.user_agent})
        request_token = session.fetch_request_token(self._oauth_config.request_token_url)

        authorization_url = self._build_authorize_url(request_token)
        print("Open this URL in your browser and authorize the app:")
        print(authorization_url)
        verifier = input("Paste the verifier code here: ").strip()

        access_session = OAuth1Session(
            self._oauth_config.consumer_key,
            self._oauth_config.consumer_secret,
            token=request_token["oauth_token"],
            token_secret=request_token["oauth_token_secret"],
            verifier=verifier,
        )
        access_session.headers.update({"User-Agent": self._app_config.user_agent})
        access_token = access_session.fetch_access_token(self._oauth_config.access_token_url)

        return OAuthToken(
            token=access_token["oauth_token"],
            secret=access_token["oauth_token_secret"],
        )
