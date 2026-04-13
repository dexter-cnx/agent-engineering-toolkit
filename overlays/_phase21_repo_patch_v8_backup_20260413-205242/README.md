# Mobile Flutter Overlay

Production-oriented Flutter skills overlay for Agent Engineering Toolkit.

This overlay adapts the small, task-specific skill pattern into a Flutter-first system with an added consolidated operating layer for long-term team use.

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

See `SKILLS_INDEX.md` for the full catalog.

## Recommended use
Use `flutter-dev` as the default starting point. For architecture-heavy requests, use `flutter-architect`. For audits, use `flutter-code-reviewer` or `flutter-release-reviewer`.

For team onboarding and operating guidance, start at `START_HERE.md`.

## Repo integration
Copy this overlay into your toolkit repo:

```bash
cp -R overlays/mobile-flutter <your-agent-engineering-toolkit>/overlays/
```

Then commit and push.

## Design principles
- Keep skills narrow and composable.
- Prefer execution workflows over generic explanation.
- Encode team policy explicitly.
- Keep Flutter code production-friendly by default.
- Avoid business logic in widgets.
- Treat localization and testing as first-class concerns.

## Included support assets
Beyond the skill catalog, this overlay also includes:
- `prompts/` for common agent entry prompts
- `templates/` for project and feature scaffolding
- `ci/github-actions/` for baseline Flutter CI
- `repo-customization/` for adapting the overlay to a specific repository
- `examples/` for copy-paste usage examples
- `canonical/` for source-of-truth baseline docs
- `companion-pack/` for repo-facing integration assets

## Current operating layer
This overlay now has four practical layers:
1. Skills and coordinators in `skills/`
2. Starter and scaffold assets in `starter-app-template/`
3. Prompts, templates, CI, examples, and repo customization
4. Consolidated operating docs in `START_HERE.md`, `INDEX_*`, `canonical/`, and `companion-pack/`
