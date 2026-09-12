"""The container's entry point: `python -m <package>`, what the Dockerfile's CMD runs.

Serves `app` over uvicorn. Logs are one JSON object per line on stdout, so a
container's output is collected as is. `log_config=None` keeps uvicorn's own
loggers on this same root handler instead of uvicorn's default (colored,
non-JSON) console formatting.
"""

from __future__ import annotations

import json
import logging
import sys
from typing import Any

import uvicorn

from .app import app

# The fields every LogRecord carries. Anything else came in through
# `logger.info("...", extra={...})` and is kept: context in fields is the
# point of structured logs.
_RESERVED = set(logging.LogRecord("", 0, "", 0, "", None, None).__dict__) | {"message", "asctime"}


class JsonFormatter(logging.Formatter):
    """One JSON object per line."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "time": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        payload.update({k: v for k, v in record.__dict__.items() if k not in _RESERVED})
        return json.dumps(payload, ensure_ascii=False, default=str)


def configure(level: int = logging.INFO) -> None:
    """Point the root logger at stdout in JSON. Safe to call more than once."""
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level)


def main() -> None:
    configure()
    logging.getLogger(__package__).info("started")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)  # noqa: S104


if __name__ == "__main__":
    main()
