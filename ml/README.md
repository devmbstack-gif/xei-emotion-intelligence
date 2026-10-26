# ML workspace — XEI Emotion Intelligence

Baseline notes for the emotion-aware / empathic AI modeling track.

## Goals (v0)

1. Establish reproducible notebook workflows for exploratory analysis.
2. Define signal schemas (text-derived affect cues, intensity, confidence) without storing unnecessary PII.
3. Keep raw datasets and trained weights **out of git**; document provenance in `data/README.md`.
4. Prefer privacy-preserving defaults aligned with `docs/privacy-rules.md`.

## Layout

| Path | Purpose |
| --- | --- |
| `notebooks/` | Jupyter experiments and baseline reports |
| `data/` | Local-only datasets (gitignored except README) |

## Suggested baseline experiments

- Lexicon / lightweight classifier baseline for valence–arousal style labels on synthetic or licensed text.
- Confidence calibration notes before any product-facing threshold.
- Offline evaluation harness (to be expanded under `docs/test-cases.md`).

## Conventions

- Notebook names: `NNN_short_slug.ipynb` (e.g. `001_signal_schema_spike.ipynb`).
- Export key findings into `docs/` when they become product decisions.
- Wording: **emotion-aware AI** / **empathic AI** only — never claim the system has “real feelings”.
