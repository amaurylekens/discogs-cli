"""Status bar widget placeholder."""

from textual.widgets import Static


class StatusBar(Static):
    def __init__(self, message: str = "Ready") -> None:
        super().__init__(message, id="status-bar")
