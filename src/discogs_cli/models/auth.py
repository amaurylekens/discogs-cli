"""Authentication state models."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthStatus:
    authorised: bool = False
    account: str | None = None
    access_token: str | None = None
    access_token_secret: str | None = None
    error: str | None = None
