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

- Date: 2026-04-08
  Decision: `prompts/review/audit_repo.md` is the role-based audit prompt and `docs/strict-audit-prompt.md` is the invocation template companion.
  Why: Separates agent-facing workflow guidance from paste-ready prompt text.
  Consequence: Root docs should reference both explicitly.

- Date: 2026-04-08
  Decision: Public release version `1.0.4` captures the audit-prompt split fix, overlay lifecycle notes, and the honest same-day release note.
  Why: Keeps the changelog and release docs aligned with the latest public surface.
  Consequence: Release references such as `scripts/push-guide.md` should point at `v1.0.4` until the next release.

- Date: 2026-04-08
  Decision: Prompt workflows now have canonical stage hubs in `prompts/index.md` and `prompts/index_EN.md`, with stage-specific EN mirrors under each prompt subfolder.
  Why: Gives a single browseable entry point while keeping the canonical prompt files grouped by lifecycle stage.
  Consequence: New prompt documentation should link to the stage hub first and then to the exact stage file.

- Date: 2026-04-08
  Decision: `docs/public-repo-checklist.md` is the human-readable summary and `scripts/check-public-repo.paths` is the machine-readable public-release source of truth.
  Why: The checklist and gate need a clear ownership split so they do not drift or overclaim exact coverage.
  Consequence: Public-release edits should update the summary and the path manifest together.

- Date: 2026-04-08
  Decision: Foundation tutorial hubs and Obsidian-friendly pages should link to stack-specific examples instead of reprinting long platform templates.
  Why: Stack-specific examples belong in overlays and stack tutorials, not in foundation navigation pages.
  Consequence: Future updates should prefer links and short pointers over duplicated template blocks.
