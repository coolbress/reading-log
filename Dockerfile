# reading-log: the container image of a service archetype.
#
# Base images are pinned by digest, not tag: a tag can move, a digest cannot,
# the same reason Actions are pinned to commit SHAs. Dependabot's `docker`
# ecosystem raises the digests.

# ── build stage ───────────────────────────────────────────────────────────
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim@sha256:e5b65587bce7de595f299855d7385fe7fca39b8a74baa261ba1b7147afa78e58 AS build

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

# Dependencies before source: a source-only change reuses this layer.
COPY pyproject.toml uv.lock ./
# --locked: fails when the lockfile disagrees with pyproject, so the image
# never silently carries other versions. --no-dev: no tests or linters inside.
RUN uv sync --locked --no-install-project --no-dev

COPY src/ ./src/
COPY README.md ./
RUN uv sync --locked --no-dev

# ── run stage ─────────────────────────────────────────────────────────────
FROM python:3.12-slim@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea

# Not root: a container escape reaches less.
RUN useradd --create-home --uid 10001 app
WORKDIR /app
# WORKDIR runs as root and would otherwise leave /app root-owned; the app
# writes its SQLite file here (DATABASE_URL, default reading_log.db).
RUN chown app:app /app

COPY --from=build --chown=app:app /app/.venv /app/.venv
COPY --from=build --chown=app:app /app/src /app/src
ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1

USER app

# The entry point is this package's __main__.py: reading_log.app under uvicorn.
CMD ["python", "-m", "reading_log"]
