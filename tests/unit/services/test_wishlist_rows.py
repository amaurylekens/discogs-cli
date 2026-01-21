from __future__ import annotations

from types import SimpleNamespace

import pytest


@pytest.mark.parametrize(
    ("release", "expected"),
    [
        pytest.param(
            SimpleNamespace(thumb="https://example.test/cover.jpg"),
            "https://example.test/cover.jpg",
            id="thumb-present",
        ),
        pytest.param(
            SimpleNamespace(thumb=None),
            "",
            id="thumb-none",
        ),
        pytest.param(
            SimpleNamespace(),
            "",
            id="thumb-missing",
        ),
    ],
)
def test_discogs_wishlist_row_provider_cover(discogs_wishlist_row_provider, release, expected):
    actual = discogs_wishlist_row_provider._cover(release)

    assert actual == expected


@pytest.mark.parametrize(
    ("formats", "expected"),
    [
        pytest.param(
            [
                {"name": "Vinyl", "descriptions": ["LP", "Album"]},
                {"name": "CD"},
            ],
            "Vinyl (LP, Album), CD",
            id="name-and-descriptions",
        ),
        pytest.param(
            [
                {"name": "", "descriptions": ["Limited Edition"]},
                {"descriptions": ["Unofficial Release"]},
            ],
            "Limited Edition, Unofficial Release",
            id="descriptions-only",
        ),
        pytest.param(
            [],
            "",
            id="empty-formats",
        ),
        pytest.param(
            None,
            "",
            id="formats-none",
        ),
    ],
)
def test_discogs_wishlist_row_provider_format(discogs_wishlist_row_provider, formats, expected):
    release = SimpleNamespace(formats=formats)

    actual = discogs_wishlist_row_provider._format(release)

    assert actual == expected
