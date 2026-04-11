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
```

## Current status

This is a production-ready skeleton:
- command surface exists
- JSON output exists
- export flow exists
- CI-friendly exit codes exist

Project-specific architecture rules still need to be implemented for your repo conventions.
