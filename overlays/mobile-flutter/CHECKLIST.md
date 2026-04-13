# Unified Checklist

## Setup
- `pubspec.yaml` exists
- `lib/app/router/route_registry.dart` exists
- `assets/i18n/translations.csv` exists
- `docs/overlay/repo_integration.md` exists

## Architecture
- domain/data/presentation exist per feature
- business logic is not buried in widgets

## Capability
- capability was added intentionally
- SDK calls stay behind boundaries where practical

## Quality
- analyze passes
- test passes
- policy check passes

## Scope
- no product-specific assumptions in canonical toolkit docs
