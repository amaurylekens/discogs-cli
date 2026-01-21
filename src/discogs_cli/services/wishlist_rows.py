"""Wishlist-based release row provider."""

from __future__ import annotations

import asyncio
from typing import AsyncIterator

import discogs_client

from discogs_cli.widgets.releases_table import ReleaseRowProvider


class DiscogsWishlistRowProvider(ReleaseRowProvider):
    """Fetch wishlist releases via python3-discogs-client."""

    def __init__(self, client: discogs_client.Client) -> None:
        self._client = client

    async def iter_release_rows(self) -> AsyncIterator[tuple[str, str, str, str]]:
        identity = await asyncio.to_thread(self._client.identity)
        wantlist = identity.wantlist
        total_pages = await asyncio.to_thread(lambda: wantlist.pages)
        for page_number in range(1, total_pages + 1):
            page = await asyncio.to_thread(wantlist.page, page_number)
            for item in page:
                release = getattr(item, "release", item)
                yield (
                    self._cover(release),
                    self._artist_title_label(release),
                    self._format(release),
                    self._year(release),
                )

    @staticmethod
    def _cover(release: object) -> str:
        return getattr(release, "thumb", None) or ""

    @staticmethod
    def _artist_title_label(release: object) -> str:
        artists = getattr(release, "artists", None) or []
        labels = getattr(release, "labels", None) or []
        artist_name = ", ".join(
            getattr(artist, "name", "") for artist in artists if getattr(artist, "name", "")
        )
        label_name = ", ".join(
            getattr(label, "name", "") for label in labels if getattr(label, "name", "")
        )
        title = getattr(release, "title", "") or ""
        parts = [part for part in (artist_name, title, label_name) if part]
        return " - ".join(parts)

    @staticmethod
    def _format(release: object) -> str:
        formats = getattr(release, "formats", None) or []
        if not formats:
            return ""
        names = []
        for info in formats:
            if isinstance(info, dict):
                name = info.get("name") or ""
                descriptions = info.get("descriptions") or []
                if descriptions:
                    name = f"{name} ({', '.join(descriptions)})" if name else ", ".join(descriptions)
                if name:
                    names.append(name)
        return ", ".join(names)

    @staticmethod
    def _year(release: object) -> str:
        year = getattr(release, "year", None)
        return str(year) if year else ""
