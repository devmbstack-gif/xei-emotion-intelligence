# Privacy rules — XEI Emotion Intelligence

These twelve rules govern how XEI’s emotion-aware / empathic AI handles data for small tech businesses and software houses. They apply to product, API, and ML workstreams.

1. **Minimize by default** — Collect only what is required for the active feature; prefer ephemeral processing over long-term storage of emotional signals.
2. **Purpose limitation** — Use emotion-signal and workspace data solely to improve collaboration support and stated product features — never for unrelated profiling or sale.
3. **Informed consent** — Users and org admins must understand what signals are inferred and how they are used before enabling empathic AI features.
4. **Org-scoped isolation** — Tenant data stays isolated; no cross-customer training or comparison without a separate, explicit agreement.
5. **No covert sensing** — Do not enable ambient capture (mic/camera) or silent emotion inference without clear, revocable consent and visible indicators.
6. **Sensitive inference caution** — Treat affect estimates as probabilistic assistive context, not medical, legal, or HR determinations.
7. **Access control** — Restrict emotion-derived insights to roles the org configures; default to the individual and their chosen managers/partners only.
8. **Retention & deletion** — Define retention windows; honor user/org deletion requests for messages, signals, and derived profiles within a documented SLA.
9. **Encryption & secrets** — Encrypt data in transit and at rest; never commit secrets; rotate credentials promptly (see `.env.example`).
10. **Vendor discipline** — Third-party LLM or analytics providers must meet equivalent privacy commitments; avoid sending unnecessary identifiers.
11. **Auditability** — Log access to sensitive emotion-derived records for security review without storing raw content longer than needed.
12. **Human override** — Users can disable emotion-aware features and fall back to non-affective assistance without losing core product access.

Questions or exceptions: document them in the PR and flag for MB Stack privacy review before merge.
