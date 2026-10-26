# Test cases — placeholder

Scenarios for XEI Emotion Intelligence (emotion-aware / empathic AI). Expand as features ship.

## API (scaffold)

| ID | Scenario | Expected |
| --- | --- | --- |
| API-01 | `GET /health` | `200`, `status: ok` |
| API-02 | `GET /v1/status` | `200`, capability `emotion-aware AI` |
| API-03 | `GET /` | `200`, product name present |

## Product / ML (TBD)

| ID | Scenario | Expected |
| --- | --- | --- |
| EI-01 | Neutral workplace message | Low-intensity, high-confidence neutral / calm band |
| EI-02 | Frustrated delivery update | Elevated stress/frustration cue with confidence score |
| EI-03 | User disables emotion-aware mode | No affect inference; standard assistant behavior |
| EI-04 | Cross-tenant request | Denied / isolated (privacy rules 4, 7) |
| EI-05 | Deletion request | Signals and derived profile cleared per retention SLA |

> Fill acceptance criteria, fixtures, and owners as endpoints and models land.
