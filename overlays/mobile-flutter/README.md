# Mobile Flutter Overlay v3

Production Flutter operating overlay for the Agent Engineering Toolkit.

This overlay keeps the foundation general and pushes Flutter-specific execution into smaller atomic skills, workflows, policies, templates, and examples.

## Start here

- `AGENTS.overlay.md`
- `SKILLS_INDEX.md`
- `SKILL_SCHEMA.md`
- `HOW_TO_USE.md`

## What changed in v2

- The catalog is now routed through a decision index instead of a flat list.
- Skills are atomic execution capsules with explicit single responsibilities.
- Policies live outside skills.
- Workflows orchestrate multiple skills in a fixed order.
- CI validates that every active skill follows `SKILL_SCHEMA.md`.

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

Use `SKILLS_INDEX.md` to select the smallest skill that can finish the task, then compose workflows when the work spans multiple execution units.

## Legacy assets

The overlay retains older catalog material in place for reference, but only the v2 skill set is considered active and CI-validated.

## Related docs

- `docs/tutorials/README.md`
- `workflows/new-project/README.md`
- `workflows/new-feature/README.md`
- `workflows/release-app/README.md`
- `workflows/migrate-project/README.md`
