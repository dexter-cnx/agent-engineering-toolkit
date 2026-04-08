# Decisions

- Date: 2026-04-08
  Decision: Foundation stays stack-agnostic at the root.
  Why: Prevents misleading identity drift as overlays expand.
  Consequence: Stack-specific assumptions must live in overlays or consuming repos.

- Date: 2026-04-08
  Decision: Canonical lifecycle source is `docs/prompt-pipeline.md`.
  Why: Reduces drift across README, docs, templates, and examples.
  Consequence: Other files should link back to that doc instead of redefining the order.

- Date: 2026-04-08
  Decision: Canonical guide paths use hyphen naming (`how-to-use`).
  Why: Avoids dual-path documentation drift.
  Consequence: Underscore duplicates should not be reintroduced.
