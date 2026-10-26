# Contributing to XEI Emotion Intelligence

Thanks for helping build XEI — an emotion-aware / empathic AI partner by **MB Stack**.

## Branching

- Create work from `main` (or the current integration branch).
- Use the prefix **`feature/*`** for new work:
  - `feature/api-health-checks`
  - `feature/emotion-signal-schema`
- Use `fix/*` for bug fixes and `docs/*` for documentation-only changes when helpful.
- Keep branches focused: one concern per PR.

## Pull requests

1. Open a PR against `main` with a clear title and short summary of **why**.
2. Link related issues or design notes when they exist.
3. Ensure CI passes (API lint + tests).
4. Prefer small, reviewable diffs over large catch-all PRs.
5. Call out privacy or security impact explicitly (see `docs/privacy-rules.md`).

### Review expectations

- At least one approving review before merge (team size permitting).
- Reviewers check: correctness, wording (use **emotion-aware AI** / **empathic AI** — never “real feelings”), privacy rules, and test coverage for behavior changes.
- Authors respond to feedback or explain trade-offs; do not merge with unresolved blocking comments.

## Local checks (API)

```bash
cd services/api
ruff check .
pytest
```

## Commit style

- Prefer concise, imperative messages focused on why (e.g. `add health route for API readiness`).
- Do not commit secrets, `.env`, raw datasets, or model weight files.

## Product wording

In UI copy, docs, and comments:

- Use **emotion-aware AI** or **empathic AI**.
- Do **not** use phrases like “real feelings” or claim the system experiences emotion.
