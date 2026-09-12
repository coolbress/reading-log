"""The reading log: one page to record a finished book and see the list."""

from __future__ import annotations

import os
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import date
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, Response
from fastapi.templating import Jinja2Templates

from . import storage

app = FastAPI()
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


def _db_path() -> str:
    return os.getenv("DATABASE_URL", "reading_log.db")


@contextmanager
def _connection() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(_db_path())
    try:
        storage.init_db(conn)
        yield conn
    finally:
        conn.close()


@app.get("/")
def index(request: Request) -> Response:
    with _connection() as conn:
        books = storage.list_books(conn)
    return templates.TemplateResponse(request, "index.html", {"books": books})


@app.post("/books")
def create_book(
    title: str = Form(..., min_length=1),
    author: str = Form(..., min_length=1),
    finished_on: date = Form(...),
) -> RedirectResponse:
    with _connection() as conn:
        storage.add_book(conn, title=title, author=author, finished_on=finished_on)
    return RedirectResponse("/", status_code=303)
