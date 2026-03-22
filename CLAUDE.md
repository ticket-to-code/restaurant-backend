# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

Backend REST API for a SaaS Restaurant Management System (MVP).
Built with FastAPI + PostgreSQL. Requirements are documented as User Stories in Spanish.

## Tech Stack

- **Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: PostgreSQL (Docker container, local dev)
- **ORM**: SQLAlchemy 2.x (async) — no migrations, tables created via `create_all` on startup
- **Validation**: Pydantic v2 (built into FastAPI)
- **Auth**: JWT (python-jose + passlib)
- **Env vars**: python-dotenv

## Project Structure

```
app/
  main.py               # FastAPI app entry point + create_all on startup
  core/
    config.py           # Settings loaded from .env
    security.py         # JWT encode/decode logic
    database.py         # Async SQLAlchemy engine + session dependency
  models/               # SQLAlchemy ORM models (one file per domain)
  schemas/              # Pydantic schemas for request/response (one file per domain)
  routers/              # FastAPI routers (one file per domain)
  services/             # Business logic (one file per domain)
  dependencies.py       # Shared FastAPI dependencies (get_db, get_current_user)
docs/
  epicas/               # Original epic files — DO NOT READ OR MODIFY
  user-stories/         # Full HUs — DO NOT READ (too large, frontend included)
  user-stories-backend/ # Backend-only HUs — USE THESE (one file per HU)
    00-index.md         # Index of all HUs with status
.env                    # Local env vars (never commit)
.env.example            # Template for env vars (always commit)
requirements.txt
PROGRESS.md             # Tracks which HUs are done — READ THIS before every session
```

## Database (Local Docker)

- **Host**: localhost
- **Port**: 5432
- **DB name**: YOUR_DB_NAME   ← replace with your actual DB name
- **User**: YOUR_DB_USER      ← replace with your actual user
- Connection string in `.env`:
  `DATABASE_URL=postgresql+asyncpg://YOUR_USER:YOUR_PASSWORD@localhost:5432/YOUR_DB_NAME`

## Common Commands

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## PROGRESS TRACKING — Read this first, every session

**Before doing anything**, read `PROGRESS.md` in the project root.
It tells you exactly which HUs are done and which are pending.
Never implement a HU marked as `done` — it already exists in the codebase.

`PROGRESS.md` format:
```
## HU Status
- [x] HU-001 — POST /auth/login
- [x] HU-002 — POST /auth/register
- [ ] HU-003 — POST /auth/recover-password   ← next
- [ ] HU-004 — ...
```

**After finishing a HU**, update `PROGRESS.md` immediately:
- Mark the HU as `[x]`
- Add the endpoint(s) implemented
- Do this before the session ends

## Working with User Stories

HUs live in `docs/user-stories-backend/` — backend-only extracts, ~30 lines each.

### Every session follows this exact sequence
1. Read `PROGRESS.md` — identify the next pending HU
2. Read **only** that HU's file from `docs/user-stories-backend/`
3. List every file to create or modify — **wait for approval before writing any code**
4. Implement in order: `model → schema → service → router`
5. Register router in `app/main.py` if it's a new domain
6. Update `PROGRESS.md` marking the HU as done

### Rules
- One HU per session — use `/clear` before starting the next one
- Never read `docs/user-stories/` or `docs/epicas/` — they are too large
- Never read more than one HU file unless there is an explicit dependency stated in the HU
- If a HU depends on another, read only that one additional file

## Architecture & Domain Modules

### Auth & Users (HU-001 to HU-005)
- JWT — Bearer token in Authorization header
- Roles: `owner` (full access), `cashier` (operational access)

### Dashboard (HU-006 to HU-009)
- KPI calculations per role, read-only

### Menu (HU-010 to HU-013+)
- Categories and Products
- Soft delete via `deleted_at` (set timestamp, never hard delete)

### Orders
- State machine: `pending` → `in_preparation` → `ready` → `closed`
- POS orders go directly to `closed` on payment

### POS
- Cart logic handled server-side

### Sales History
- Read-only reporting — never mutate historical records

## Coding Standards

- **Code**: English — variables, functions, comments, filenames
- **HUs**: Spanish — never translate them
- **Naming**: `snake_case` variables/functions/DB fields · `PascalCase` classes/schemas/models · `SCREAMING_SNAKE_CASE` constants
- **Money**: `Decimal` only — never `float`
- **Historical data**: Snapshot tax rate and currency on the order row — not FK references
- **Validation**: At Pydantic schema layer — services receive clean data
- **Errors**: `HTTPException` with `{"detail": "message"}`

## What NOT to do

- Do NOT use `float` for money
- Do NOT commit `.env`
- Do NOT put business logic in routers
- Do NOT use sync SQLAlchemy
- Do NOT create Alembic migrations
- Do NOT write tests
- Do NOT read `docs/user-stories/` or `docs/epicas/`
- Do NOT implement a HU already marked `[x]` in `PROGRESS.md`
- Do NOT start coding without showing the plan first