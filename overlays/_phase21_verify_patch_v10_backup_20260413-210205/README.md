# Mobile Flutter Overlay

Production-oriented Flutter skills overlay for Agent Engineering Toolkit.

This overlay adapts the small, task-specific skill pattern into a Flutter-first system with four layers of value:

1. Coordinators route work to the right skills.
2. Reference skills explain packages, APIs, and platform details.
3. Workflow guides tell the agent how to execute real delivery work.
4. Policies enforce team standards so output stays consistent.

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

For onboarding and current operating guidance, start at `START_HERE.md`.

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
