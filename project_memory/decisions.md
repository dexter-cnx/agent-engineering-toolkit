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

- Date: 2026-04-08
  Decision: Root-level onboarding tutorials should stay stack-neutral and use generic feature slices instead of Flutter-first examples.
  Why: The foundation repository must not imply one stack as the default identity.
  Consequence: Stack-specific walkthroughs belong in overlay or stack tutorial folders.

- Date: 2026-04-08
  Decision: Internal-only onboarding and team prompt material now lives under `docs/internal/` and `prompts/internal/`.
  Why: Keeps the public root clean while preserving internal workflow references.
  Consequence: Public docs should not point at root internal helper files.

- Date: 2026-04-09
  Decision: Root docs should describe the overlay catalog without exposing a numeric skill count.
  Why: Keeps the foundation identity neutral while leaving capability counts to overlay-local docs.
  Consequence: Overlay catalogs may list and group skills, but the root docs should avoid capability tallies.

- Date: 2026-04-09
  Decision: Overlay workflow and validation docs use explicit names: `SKILL_WORKFLOW.md` and `OVERLAY_VALIDATION_CHECKLIST.md`.
  Why: The old `HOW_TO_APPLY.md` and `VALIDATION.md` names were too generic.
  Consequence: Future overlay docs should prefer descriptive operational names over ambiguous pack-style filenames.

- Date: 2026-04-09
  Decision: Unity capabilities live in a dedicated `overlays/unity/` overlay with a README-first catalog and separate `unity-ugui` and `unity-ui-toolkit` skills.
  Why: Unity needs stack-specific structure, and splitting the UI surface keeps implementation guidance practical.
  Consequence: Future Unity work should extend the Unity overlay instead of adding Unity assumptions to the foundation root.

- Date: 2026-04-09
  Decision: The first Unity game tutorial for this repo lives at `docs/tutorials/unity/how-to-make-tetris-in-unity.md` with a matching EN file and an overlay worked example.
  Why: Gives Unity tutorial content a clear home while keeping the overlay example reusable.
  Consequence: Future Unity tutorial additions should follow the same docs/tutorials/unity pattern and keep examples under `overlays/unity/examples/`.

- Date: 2026-04-11
  Decision: `tools/toolkit-i18n` is implemented as a reusable PATH-friendly wrapper over a stdlib Python CLI with `doctor`, `validate`, `diff`, and `generate` subcommands.
  Why: Keeps localization workflows repeatable, compact, and easy to invoke from outside the source folder.
  Consequence: Future toolkit-i18n changes should preserve the non-interactive surface, compact JSON/text output, and explicit target-directory writes.

- Date: 2026-04-14
  Decision: Feature coverage summaries in `toolkit-arch` and `toolkit-i18n` must use per-feature set intersection, not count-only heuristics.
  Why: Matching by counts alone can overstate coverage when defined and used keys do not actually overlap.
  Consequence: Future coverage changes should derive matched, missing, and unused counts from unique key sets.
