# Mobile Flutter Overlay Phase 6

Production Flutter operating overlay for the Agent Engineering Toolkit.

This overlay keeps the foundation general and pushes Flutter-specific execution into smaller atomic skills, workflows, policies, templates, examples, and generator tooling.

## Start here

- `AGENTS.overlay.md`
- `SKILLS_INDEX.md`
- `SKILL_SCHEMA.md`
- `HOW_TO_USE.md`

## What changed in v2

- The catalog is routed through a generated decision index instead of a flat list.
- Skills are atomic execution capsules with explicit single responsibilities.
- Generator tooling creates new skills from a standard template.
- Policies live outside skills.
- Workflows orchestrate multiple skills in a fixed order.
- CI validates schema, overlap, docs sync, and index synchronization.

## Active architecture

```text
overlays/mobile-flutter/
  AGENTS.overlay.md
  README.md
  SKILLS_INDEX.md
  SKILL_SCHEMA.md
  skills/
  workflows/
  policies/
  canonical/
  templates/
  examples/
  checklists/
  ci/
  starter-app-template/
```

## Default stack

- Flutter stable
- Dart 3
- Clean Architecture
- Riverpod by default
- GetX when explicitly selected
- `go_router` for navigation
- Firebase adapters behind repository boundaries
- CSV-driven localization when localization is needed

## Operating rule

Use `SKILLS_INDEX.md` to select the smallest skill that can finish the task, then compose workflows when the work spans multiple execution units. Use `tools/skillgen/` to add or sync skills safely.

## Legacy assets

The overlay retains older catalog material in place for reference, but only the v2 skill set is considered active and CI-validated.

## Related docs

- `docs/tutorials/README.md`
- `AGENT_CONTRIBUTION_RULES.md`
- `workflows/new-project/README.md`
- `workflows/new-feature/README.md`
- `workflows/release-app/README.md`
- `workflows/migrate-project/README.md`
