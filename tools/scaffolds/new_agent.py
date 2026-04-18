#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if len(sys.argv) != 3:
    print('Usage: new_agent.py <lead|specialists> <name>')
    sys.exit(1)
category, name = sys.argv[1], sys.argv[2]
if category not in {'lead', 'specialists'}:
    print('Category must be lead or specialists')
    sys.exit(1)
out = ROOT / 'agents' / category / f'{name}.md'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(f'# {name}\n\n## Mission\n\n## Inputs\n\n## Outputs\n\n## Boundaries\n\n## Escalation\n', encoding='utf-8')
print(f'SCAFFOLD_PASS: wrote {out.relative_to(ROOT)}')
