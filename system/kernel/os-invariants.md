# OS Invariants (Single Source of Truth)

These invariants define non-negotiable repository behavior.

## Invariants

1. `README.md` is the public front door.
2. Canonical onboarding path is only: `README.md -> docs/get-started.md -> docs/adoption-paths.md`.
3. Root must not introduce additional onboarding entrypoints.
4. Every managed top-level directory must be classified and have a status README.
5. Compatibility files are non-canonical and explicitly labeled.
6. Legacy/frozen surfaces must be labeled and must not claim canonical status.
7. `agents/`, `memory/`, `system/`, `prompts/`, `tools/`, `docs/`, `overlays/` are the primary OS surfaces.
8. Memory must contain ADRs with required sections.
9. Prompt compiled outputs must be generated and committed.

## Machine-readable invariants

```json
{
  "front_door": "README.md",
  "canonical_onboarding": [
    "README.md",
    "docs/get-started.md",
    "docs/adoption-paths.md"
  ],
  "compatibility_root_docs": [
    "START_HERE.md",
    "README_START_HERE.md",
    "HOW_TO_USE.md",
    "ONBOARDING_MINIMAL.md",
    "ONBOARDING_FULL.md",
    "INDEX_CANONICAL.md"
  ],
  "managed_top_level_dirs": {
    "canonical": [".github", "agents", "memory", "system", "prompts", "tools", "docs", "overlays"],
    "legacy": ["agent_team", "project_memory", "core", "canonical", "checklists", "skills", "companion-pack", "orchestrator"],
    "reference": ["apps", "packages", "samples", "examples", "evals", "tests", "reports", "artifacts", "assets", "audits", "templates", "runners", "scripts"]
  },
  "ignored_top_level_dirs": [".git", "node_modules"],
  "status_keywords": ["canonical", "compatibility", "legacy", "frozen", "reference", "transitional"],
  "compiled_prompts": [
    "prompts/compiled/codex-runtime.md",
    "prompts/compiled/claude-runtime.md",
    "prompts/compiled/gemini-runtime.md"
  ]
}
```
