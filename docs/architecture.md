# Architecture notes — XEI Emotion Intelligence

High-level design for the emotion-aware AI partner developed by **MB Stack**.

## Context

XEI helps small tech business owners and software houses communicate with better emotional context. The system provides **empathic AI** assistance: inferred affect cues inform tone and recommendations. It does not experience emotion.

## Current scaffold

```
Clients (future: apps/web, desktop, integrations)
        │
        ▼
┌───────────────────┐
│  services/api     │  FastAPI (Python 3.11)
│  health / status  │  CORS, settings via env
└─────────┬─────────┘
          │
          ▼
┌───────────────────┐
│  Supabase (planned)│  Auth, Postgres, storage
└───────────────────┘

ml/  → offline notebooks & evaluation (not on request path yet)
```

## Planned components (not in this base)

| Component | Role |
| --- | --- |
| Emotion-signal service | Infer valence/intensity/confidence from text (and later optional modalities) |
| Partner / conversation API | Session context, org settings, feature flags for emotion-aware mode |
| `apps/web` | Landing and product UI (deferred) |
| Workers | Async jobs for retention, exports, model refresh |

## Cross-cutting concerns

- **Privacy**: Enforce `docs/privacy-rules.md` at API boundaries and ML pipelines.
- **Config**: Secrets and Supabase keys via environment (see `.env.example`).
- **Observability**: Structured logs; avoid logging raw emotional content at debug in production.
- **CI**: Lint and unit tests for `services/api` on every PR (`.github/workflows/ci.yml`).

## Versioning

- Public HTTP surface under `/v1/...` once feature routes exist.
- Internal package version in `services/api/app/__init__.py`.
