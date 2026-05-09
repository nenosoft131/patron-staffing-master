# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies (creates .venv automatically)
uv sync

# Install with dev dependencies
uv sync --dev

# Run the API server
uv run uvicorn main:app --reload --port 8000

# Run all tests
uv run pytest tests/

# Run a single test
uv run pytest tests/test.py::test_create_user_success -v

# Add a new dependency
uv add <package>

# Start Kafka + Zookeeper (required for Kafka features)
docker-compose up -d
```

## Architecture

This is a FastAPI backend following **hexagonal (ports-and-adapters) architecture** with Domain-Driven Design principles.

### Layer responsibilities

| Layer | Path | Role |
|---|---|---|
| HTTP | `app/api/routers/` | Route definitions, Depends() wiring only |
| Use Cases | `app/infrastructure/services/` | Business operations (`CreateUser`, `LoginUser`) |
| Interfaces (Ports) | `app/interfaces/` | Abstract base classes defining contracts |
| Adapters | `app/database/crud/`, `app/infrastructure/security/` | Concrete implementations of interfaces |
| ORM Models | `app/database/models/` | SQLAlchemy table definitions |
| Pydantic Schemas | `app/database/schemas/`, `app/api/schemas/` | Request/response validation and DTOs |
| Config | `app/core/config.py` | `Settings` via pydantic-settings (reads `.env`) |

### Dependency injection flow

FastAPI `Depends()` chains are assembled in `app/utils/dependencies.py`. A request for `CreateUser` follows: `get_async_db` → `UserSQLAlchemyRepository` + `BcryptPasswordHasher` → `CreateUser`. This is the pattern to follow when adding new use cases.

### Database

- Dev/test uses SQLite (`sqlite+aiosqlite:///./test.db`) hardcoded in `app/database/session.py`. Production switches to PostgreSQL via `DATABASE_URL` env var in `app/core/config.py` (the two are not yet wired together).
- SQLAlchemy 2.0 async engine; sessions are request-scoped via `get_async_db()` generator.
- Tables auto-created on startup via `lifespan` in `main.py` calling `init_db()`.

### Authentication

JWT tokens signed with HS256. `create_access_token` / `decode_access_token` live in `app/utils/jwt_handler.py`. The `get_current_user` dependency in `dependencies.py` validates the bearer token and returns the ORM user. `jose` must be installed but is not currently in `requirements.txt`.

### Event system

`app/communication/communication_handler.py` provides a lightweight in-process pub/sub (`subscribe` / `post_event`). This is separate from the Kafka integration in `app/utils/producer.py` + `app/utils/consumer.py`, which is used for external async messaging (requires a running broker via `docker-compose`).

### User roles

`UserRole` enum in `app/database/schemas/user.py`: `admin`, `client`, `candidate`, `staff`. Default role is `candidate`.

## Configuration

Copy `.env` and set:
```
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/patron_dev
SECRET_KEY=<hex string>
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Without `.env`, the app falls back to SQLite in-memory and a hardcoded `SECRET_KEY` from `config.py`.
