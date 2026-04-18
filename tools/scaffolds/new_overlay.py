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
    readme.write_text(
        f'# {name}\n\n'
        '## Overlay OS contract\n\n'
        '### Purpose\n'
        f'This overlay provides stack-specific specialization for {name} while preserving the stack-neutral root foundation.\n\n'
        '### When to use\n'
        'Use this overlay when your delivery context clearly matches its specialization scope and constraints.\n\n'
        '### Relation to root guidance\n'
        'Root docs remain canonical for onboarding and governance; this overlay extends implementation guidance only.\n\n'
        '### Boundaries\n'
        'This overlay must not redefine repository identity, canonical lifecycle, or root policy contracts.\n\n'
        '### What this overlay does not replace\n'
        'This overlay does not replace root governance, canonical docs, or core runtime contract checks.\n',
        encoding='utf-8'
    )
print(f'SCAFFOLD_PASS: created {dirp.relative_to(ROOT)}')
