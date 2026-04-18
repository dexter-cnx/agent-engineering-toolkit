#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
state_dir = ROOT / 'memory/state'
out = ROOT / 'artifacts/memory-state-rollup.md'
out.parent.mkdir(parents=True, exist_ok=True)
sections = []
for p in sorted(state_dir.glob('*.md')):
    sections.append(f'## {p.name}\n\n{p.read_text(encoding="utf-8").strip()}')
out.write_text('# Memory State Rollup\n\n' + '\n\n'.join(sections) + '\n', encoding='utf-8')
print(f'WROTE: {out.relative_to(ROOT)}')
