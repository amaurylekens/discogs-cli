"""Release table widget."""

from __future__ import annotations

import asyncio
from typing import AsyncIterator, Protocol

from textual.widgets import DataTable


class ReleaseRowProvider(Protocol):
    """Protocol for streaming release rows into the table."""

    async def iter_release_rows(self) -> AsyncIterator[tuple[str, str, str, str]]:
        """Yield release rows as (cover, artist/title/label, format, year)."""


class ReleasesTable(DataTable):
    """Table for listing Discogs releases."""

    def __init__(self, data_retriever: ReleaseRowProvider | None = None) -> None:
        super().__init__()
        self.data_retriever = data_retriever

    def on_mount(self) -> None:
        self.add_columns("Cover", "Artist - Title - Label", "Format", "Year")
        if self.data_retriever is not None:
            asyncio.create_task(self.load_releases())

    async def load_releases(self) -> None:
        """Populate the table from the configured data retriever."""
        if self.data_retriever is None:
            return
        async for row in self.data_retriever.iter_release_rows():
            self.add_row(*row)
