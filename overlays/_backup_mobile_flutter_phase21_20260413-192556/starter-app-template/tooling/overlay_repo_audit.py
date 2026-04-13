#!/usr/bin/env python3
"""Basic repo audit for the starter app and overlay expectations."""

from __future__ import annotations

from pathlib import Path

REQUIRED = [
    'lib/main.dart',
    'lib/app/app.dart',
    'lib/app/router/app_router.dart',
    'assets/i18n/translations.csv',
    'scripts/generate_l10n_from_csv.py',
    'tooling/policy_check.sh',
]


def main() -> int:
    root = Path('.').resolve()
    missing = [path for path in REQUIRED if not (root / path).exists()]
    if missing:
        print('Missing required files:')
        for item in missing:
            print(f'- {item}')
        return 1

    features_dir = root / 'lib' / 'features'
    if not features_dir.exists():
        print('Missing lib/features directory')
        return 1

    print('Overlay repo audit passed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
