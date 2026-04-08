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

- Date: 2026-04-08
  Decision: The root README family and how-to-use guides should point to `docs/strict-audit-prompt.md` as canonical and mention `scripts/bootstrap-project-memory.sh` as the optional helper.
  Why: Keeps entry-point docs aligned with current canonical paths and avoids stale helper references.
  Consequence: Future docs edits should preserve those two references consistently.

- Date: 2026-04-08
  Decision: New audit artifacts should be added to `docs/tree-manifest.txt` immediately when saved.
  Why: Keeps the manifest truthful as the authoritative tree snapshot.
  Consequence: Saving an audit file now includes a manifest refresh in the same change set.
