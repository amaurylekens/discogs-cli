"""Configuration helpers and defaults."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    api_base_url: str = "https://api.discogs.com"
    user_agent: str = "discogs-cli"


@dataclass(frozen=True)
class OAuthConfig:
    consumer_key: str
    consumer_secret: str
    callback_uri: str = "oob"
    request_token_url: str = "https://api.discogs.com/oauth/request_token"
    authorize_url: str = "https://www.discogs.com/oauth/authorize"
    access_token_url: str = "https://api.discogs.com/oauth/access_token"


def load_app_config() -> AppConfig:
    user_agent = os.getenv("DISCOGS_USER_AGENT", "discogs-cli")
    return AppConfig(user_agent=user_agent)


def load_oauth_config() -> OAuthConfig:
    key = os.getenv("DISCOGS_CONSUMER_KEY")
    secret = os.getenv("DISCOGS_CONSUMER_SECRET")
    if not key or not secret:
        raise RuntimeError(
            "Missing Discogs OAuth credentials. Set DISCOGS_CONSUMER_KEY and "
            "DISCOGS_CONSUMER_SECRET in your environment."
        )
    return OAuthConfig(consumer_key=key, consumer_secret=secret)
