# XEI API (`services/api`)

FastAPI backend for **XEI Emotion Intelligence** — the emotion-aware AI service layer developed by MB Stack.

## Requirements

- Python 3.11+
- Virtual environment recommended

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix:    source .venv/bin/activate
pip install -r requirements.txt
```

Copy repo-root `.env.example` to `.env` and set Supabase placeholders as needed.

## Run

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Test & lint

```bash
ruff check .
pytest
```

## Current surface

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/` | Service metadata |
| GET | `/health` | Liveness / readiness probe |
| GET | `/v1/status` | API version status |

Emotion-signal and partner endpoints will land in later iterations.
