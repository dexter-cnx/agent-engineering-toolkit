# toolkit-arch

Python-based repository CLI for validating Clean Architecture guardrails and failing CI when layer boundaries are violated.

## Install

```bash
cd tools/toolkit-arch
python -m pip install -e .
```

## Commands

```bash
toolkit-arch doctor
toolkit-arch scan --target apps/my_app --json
toolkit-arch violations --target apps/my_app --json --limit 20
toolkit-arch export --target apps/my_app --output artifacts/arch-report.json
toolkit-arch ci-check --target apps/my_app
toolkit-arch i18n-usage --target apps/my_flutter_app --output artifacts/i18n-used-keys.json --json
toolkit-arch i18n-layer-check --target apps/my_flutter_app --json
toolkit-arch i18n-coverage --target apps/my_flutter_app --translations assets/i18n/translations.csv --json
```

## Current status

This is a production-ready skeleton:
- command surface exists
- JSON output exists
- export flow exists
- CI-friendly exit codes exist

Project-specific architecture rules still need to be implemented for your repo conventions.

## Localization link

- `i18n-usage` scans Dart/Flutter code for localization key usage.
- `i18n-layer-check` flags localization usage in `domain` and `data` layers.
- `i18n-coverage` combines source usage with `translations.csv` for coverage reporting.
- `i18n-usage --output <file>` writes a JSON report that `toolkit-i18n keys diff` can read.
