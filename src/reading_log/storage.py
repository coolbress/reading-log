"""SQLite persistence for recorded books. No ORM: one table, three queries."""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Book:
    id: int
    title: str
    author: str
    finished_on: str


def init_db(conn: sqlite3.Connection) -> None:
    """Create the `books` table if it is not there yet. Safe to call every request."""
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            finished_on TEXT NOT NULL
        )
        """
    )
    conn.commit()


def add_book(conn: sqlite3.Connection, *, title: str, author: str, finished_on: date) -> None:
    conn.execute(
        "INSERT INTO books (title, author, finished_on) VALUES (?, ?, ?)",
        (title, author, finished_on.isoformat()),
    )
    conn.commit()


def list_books(conn: sqlite3.Connection) -> list[Book]:
    """Recorded books, most recently finished first."""
    # A book can be recorded after one that finished more recently (a
    # backfilled entry), so the row id alone does not track finish order;
    # finished_on is the real key, id only breaks ties within the same day.
    rows = conn.execute(
        "SELECT id, title, author, finished_on FROM books ORDER BY finished_on DESC, id DESC"
    ).fetchall()
    return [Book(id=row[0], title=row[1], author=row[2], finished_on=row[3]) for row in rows]
