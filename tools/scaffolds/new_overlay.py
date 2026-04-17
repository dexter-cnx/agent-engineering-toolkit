#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if len(sys.argv) != 2:
    print('Usage: new_overlay.py <overlay-name>')
    sys.exit(1)
name = sys.argv[1]
dirp = ROOT / 'overlays' / name
dirp.mkdir(parents=True, exist_ok=True)
readme = dirp / 'README.md'
if not readme.exists():
    readme.write_text(f'# {name}\n\n## Purpose\n\n## When to use\n\n## Relation to root guidance\n\n## Boundaries\n\n## What this overlay does not replace\n', encoding='utf-8')
print(f'SCAFFOLD_PASS: created {dirp.relative_to(ROOT)}')
