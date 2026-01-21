from __future__ import annotations

from types import SimpleNamespace

import pytest

from discogs_cli.services.wishlist_rows import DiscogsWishlistRowProvider


@pytest.fixture
def discogs_client():
    return SimpleNamespace()


@pytest.fixture
def discogs_wishlist_row_provider(discogs_client):
    return DiscogsWishlistRowProvider(client=discogs_client)
