# XEI Emotion Intelligence

**XEI** is an **emotion-aware AI** partner for small tech business owners and software houses. It helps teams communicate with clearer context, reduce friction, and stay aligned under delivery pressure — developed by **MB Stack**.

XEI is empathic AI: it models emotional signals from text and interaction patterns to support healthier collaboration. It does **not** claim to experience emotion.

## Tech stack

| Layer | Choice |
| --- | --- |
| API | FastAPI (Python 3.11) |
| Data / Auth (planned) | Supabase |
| ML workspace | Jupyter notebooks under `ml/` |
| CI | GitHub Actions |

> The marketing / landing app (`apps/web`) is intentionally out of scope for this base scaffold.

## Repository layout

```
xei-emotion-intelligence/
├── services/api/     # FastAPI backend
├── ml/               # Notebooks + data guidelines (no raw datasets)
├── docs/             # Architecture, privacy rules, test cases
├── .github/workflows # CI for API lint & tests
├── .env.example      # Env template (Supabase placeholders)
├── CONTRIBUTING.md
└── README.md
```

## Quick start — API

```bash
cd services/api
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
cp ../../.env.example ../../.env   # then edit values
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Health: `GET http://localhost:8000/health`
- Docs: `http://localhost:8000/docs`

## ML workspace

See [`ml/README.md`](ml/README.md) for baseline notes. Keep raw datasets and model weights out of git (see `.gitignore` and `ml/data/README.md`).

## Documentation

- [Architecture](docs/architecture.md)
- [Privacy rules](docs/privacy-rules.md)
- [Test cases](docs/test-cases.md)
- [Contributing](CONTRIBUTING.md)

## License

Proprietary — MB Stack. All rights reserved unless otherwise stated.
