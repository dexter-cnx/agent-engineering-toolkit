#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if len(sys.argv) != 2:
    print('Usage: new_workflow.py <name>')
    sys.exit(1)
out = ROOT / 'agents/workflows' / f'{sys.argv[1]}.md'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(f'# Workflow: {sys.argv[1]}\n\n## Mission\n\n## Inputs\n\n## Outputs\n\n## Boundaries\n\n## Escalation conditions\n', encoding='utf-8')
print(f'SCAFFOLD_PASS: wrote {out.relative_to(ROOT)}')
