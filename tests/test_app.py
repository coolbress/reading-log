from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from reading_log.app import app


@pytest.fixture
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setenv("DATABASE_URL", str(tmp_path / "reading_log.db"))
    return TestClient(app)


def test_empty_state_invites_the_first_entry(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "No books yet" in response.text


def test_recording_a_book_puts_it_in_the_list(client: TestClient) -> None:
    response = client.post(
        "/books",
        data={
            "title": "Klara and the Sun",
            "author": "Kazuo Ishiguro",
            "finished_on": "2026-03-01",
        },
    )

    assert response.status_code == 200
    assert "Klara and the Sun" in response.text
    assert "Kazuo Ishiguro" in response.text


def test_empty_title_is_rejected_and_nothing_is_recorded(client: TestClient) -> None:
    response = client.post(
        "/books",
        data={"title": "", "author": "Kazuo Ishiguro", "finished_on": "2026-03-01"},
    )

    assert response.status_code == 422
    assert "No books yet" in client.get("/").text


def test_a_book_is_stored_in_the_database_file_not_in_memory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    db_path = tmp_path / "reading_log.db"
    monkeypatch.setenv("DATABASE_URL", str(db_path))
    client = TestClient(app)

    client.post(
        "/books",
        data={"title": "Educated", "author": "Tara Westover", "finished_on": "2026-02-01"},
    )

    assert db_path.exists()
    conn = sqlite3.connect(db_path)
    try:
        rows = conn.execute("SELECT title, author, finished_on FROM books").fetchall()
    finally:
        conn.close()
    assert rows == [("Educated", "Tara Westover", "2026-02-01")]
