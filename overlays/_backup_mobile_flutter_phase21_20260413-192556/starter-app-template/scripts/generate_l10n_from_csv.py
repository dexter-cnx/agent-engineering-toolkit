from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / 'assets' / 'i18n' / 'translations.csv'
OUT_DIR = ROOT / 'assets' / 'i18n' / 'generated'


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open('r', encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))

    locales = [name for name in rows[0].keys() if name != 'key'] if rows else []
    payloads: dict[str, dict[str, str]] = {locale: {} for locale in locales}

    for row in rows:
        key = (row.get('key') or '').strip()
        if not key:
            continue
        for locale in locales:
            payloads[locale][key] = row.get(locale, '')

    for locale, payload in payloads.items():
        out_path = OUT_DIR / f'{locale}.json'
        out_path.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + '
',
            encoding='utf-8',
        )
        print(f'Wrote {out_path}')


if __name__ == '__main__':
    main()
