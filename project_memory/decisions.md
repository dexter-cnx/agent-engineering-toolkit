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

- Date: 2026-04-08
  Decision: `prompts/audit_repo.md` is a compatibility alias, not a second canonical audit prompt.
  Why: Prevents duplicated audit guidance from drifting over time.
  Consequence: `docs/strict-audit-prompt.md` remains the single canonical audit source.

- Date: 2026-04-08
  Decision: `scripts/bootstrap-project-memory.sh` is the small helper for submodule addition plus memory-template copying only.
  Why: Keeps the script name honest about its limited scope.
  Consequence: AGENTS setup, overlay choice, and verification commands remain manual steps in the consuming repo.
