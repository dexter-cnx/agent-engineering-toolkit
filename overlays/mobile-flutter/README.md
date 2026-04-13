# Mobile Flutter Overlay

Production-oriented Flutter skills overlay for Agent Engineering Toolkit.

This version keeps the current skill/starter assets, but adds a clearer operating layer for long-term team use.

## Start here
- `START_HERE.md`
- `INDEX_CANONICAL.md`
- `INDEX_PROMPTS.md`
- `INDEX_COMPANION.md`
- `INDEX_CHECKLISTS.md`

## Target stack
- Flutter stable
- Dart 3
- Material 3
- Clean Architecture
- `go_router`
- `dio`
- `easy_localization`
- CSV source of truth at `assets/i18n/translations.csv`
- Riverpod as default state management
- GetX as supported opt-in path

## Overlay path
```text
overlays/mobile-flutter/
```

## Included skill groups
- Coordinators
- Design
- Framework reference
- Workflow guides
- Policies
- Utilities

See `SKILLS_INDEX.md` for the skill catalog.

## Toolkit-safe scope
This overlay is architecture-first and capability-driven.

Canonical toolkit scope:
- state management
- localization
- networking
- Firebase
- maps
- offline-first guidance
- Flutter web loading
- policy checks / CI / prompts / templates

The toolkit core should avoid product-specific business assumptions.

## Included support assets
- `prompts/`
- `templates/`
- `ci/github-actions/`
- `repo-customization/`
- `examples/`
- `starter-app-template/`
- `companion-pack/` for repo-facing tooling
- `canonical/` for source-of-truth baseline docs

## Recommended use
1. Start at `START_HERE.md`
2. Use `INDEX_CANONICAL.md` for standards
3. Use `INDEX_PROMPTS.md` for prompt entry points
4. Use `INDEX_COMPANION.md` when integrating into a real Flutter repo
