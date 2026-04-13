from pathlib import Path
import sys

DEFAULT_ROWS = [
    ('feature.title', 'Feature', 'ฟีเจอร์'),
    ('feature.action.open', 'Open feature', 'เปิดฟีเจอร์'),
]

def main():
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('assets/i18n/translations.csv')
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    existing = csv_path.read_text(encoding='utf-8') if csv_path.exists() else 'key,en,th\n'
    lines = existing.strip().splitlines()
    existing_keys = {line.split(',')[0] for line in lines[1:] if ',' in line}

    with csv_path.open('a', encoding='utf-8') as f:
        if not csv_path.exists():
            f.write('key,en,th\n')
        for key, en, th in DEFAULT_ROWS:
            if key not in existing_keys:
                f.write(f'{key},{en},{th}\n')

    print(f'Seeded translations into {csv_path}')

if __name__ == '__main__':
    main()
