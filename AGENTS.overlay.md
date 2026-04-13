# AGENTS.overlay.md

## Purpose
This overlay guides AI coding agents working on Flutter repositories.

## Default routing
- Start at `START_HERE.md`
- Use `INDEX_CANONICAL.md` for standards
- Use `INDEX_PROMPTS.md` for task prompts
- Use `INDEX_COMPANION.md` for repo-facing tooling

## Core rules
- Prefer capability-driven changes over product-specific assumptions
- Keep business logic out of widgets
- Use feature-based folder structure
- Keep SDK usage behind adapters/services when possible
- Treat route registry, translation source, and policy checks as first-class repo assets

## State management
- Riverpod is supported
- GetX is supported
- Pick one per feature flow intentionally
- Do not mix styles casually in the same delivery slice

## Required repo-facing files
At minimum, the repo should converge toward:
- `pubspec.yaml`
- `lib/app/router/route_registry.dart`
- `assets/i18n/translations.csv`
- `docs/overlay/repo_integration.md`

## Review expectations
Before merge, validate:
- architecture boundaries
- changed files scope
- route registration
- translation source updates
- policy check success
- Flutter analyze/test/build paths
