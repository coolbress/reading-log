# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

A single user: the repo owner, recording a book right after finishing it and later browsing the list. No accounts, no sharing, no other audience.

## Product Purpose

A personal, durable record of every book finished, in the order finished. Success is the log being complete and always there — surviving a process restart — not engagement, growth, or discovery.

## Positioning

Deliberately not a reading-tracking platform. No ratings, reviews, social feed, recommendations, or multi-user accounts — the value is being the smallest possible durable record: log a book, see the list, nothing else competes for attention.

## Operating Context

A FastAPI app behind uvicorn, containerized (`python -m reading_log` is the Dockerfile's `CMD`), with structured JSON logs to stdout. Data persists in a SQLite file (path from the `DATABASE_URL` env var, default `reading_log.db`), so history survives a restart or redeploy.

## Capabilities and Constraints

- Record a book (title, author, date finished) and view every recorded book, newest-finished first.
- No editing or deleting entries, no ratings/notes/tags, no multi-user auth, no pagination — by design, not a gap slated to close.
- One self-contained Jinja2 template (`src/reading_log/templates/index.html`): no CSS/JS framework, no external assets, no build step. This is a standing constraint for all future design work, not a one-off choice from the last redesign.
- The form field names/ids (`title`, `author`, `finished_on`) and the template variables (`books` loop, `book.title`, `book.author`, `book.finished_on`, the empty state) are the fixed contract between backend and template. Visual work changes markup and styling around them, never the names themselves.

## Evidence on Hand

No user content beyond what the owner logs. No testimonials, case studies, press, or usage data exist, and none should be invented.

## Product Principles

1. Stay the smallest possible durable record — resist features that compete with "log it, see it," even when they're common in the category.
2. The framework-free, build-step-free single template is a durable technical constraint, carried into every future visual pass.
3. The backend/template contract (field names, template variables) is fixed; visual work never touches it.
4. Design for one user, one sitting at a time — no concurrency or multi-user concerns beyond what SQLite already handles.

## Accessibility & Inclusion

WCAG AA contrast on text, inputs, and interactive controls, confirmed in both light and dark color scheme (`prefers-color-scheme`). Established as a requirement in the last redesign; applies to all future visual work.
