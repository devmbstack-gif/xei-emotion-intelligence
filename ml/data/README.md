# `ml/data` — datasets (local only)

This folder holds **local** training / evaluation data for XEI’s emotion-aware AI work.

## Rules

- **Do not commit raw datasets.** Contents under `ml/data/` are gitignored except this README.
- Prefer licensed, synthetic, or explicitly consented corpora.
- Document source, license, retention period, and PII status in a private tracker or a local `MANIFEST.md` that you do **not** push if it contains sensitive paths.
- Strip or hash identifiers before any shared analysis artifact.

## Expected local layout (example)

```
ml/data/
├── README.md          # this file (tracked)
├── raw/               # gitignored
├── processed/         # gitignored
└── MANIFEST.local.md  # optional, gitignored via *.local.md if added later
```

When you add a new dataset locally, record: name, source URL or owner, license, approximate size, and whether it may leave the developer machine.
