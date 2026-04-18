#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
required = [
    'memory/README.md',
    'memory/glossary.md',
    'memory/patterns.md',
    'memory/anti-patterns.md',
    'memory/state/current-focus.md',
    'memory/state/known-debts.md',
    'memory/state/next-pass.md',
]

missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('MEMORY_LINT_FAIL: Missing memory files:')
    print('\n'.join(f' - {m}' for m in missing))
    sys.exit(1)

adrs = sorted((ROOT / 'memory/decisions').glob('*.md'))
if len(adrs) < 3:
    print('MEMORY_LINT_FAIL: Require at least 3 ADRs in memory/decisions for production baseline.')
    sys.exit(1)

for adr in adrs:
    txt = adr.read_text(encoding='utf-8').lower()
    for marker in ['## status', '## decision']:
        if marker not in txt:
            print(f'MEMORY_LINT_FAIL: {adr.relative_to(ROOT)} missing required section {marker}.')
            sys.exit(1)
    if 'todo' in txt:
        print(f'MEMORY_LINT_FAIL: {adr.relative_to(ROOT)} contains TODO placeholders.')
        sys.exit(1)

for rel in ['memory/patterns.md', 'memory/anti-patterns.md']:
    txt = (ROOT / rel).read_text(encoding='utf-8')
    entries = [line for line in txt.splitlines() if line.startswith('## ')]
    if len(entries) < 3:
        print(f'MEMORY_LINT_FAIL: {rel} must contain at least 3 concrete entries.')
        sys.exit(1)
    if any('TODO' in line.upper() for line in txt.splitlines()):
        print(f'MEMORY_LINT_FAIL: {rel} contains TODO placeholders.')
        sys.exit(1)

state = (ROOT / 'memory/state/current-focus.md').read_text(encoding='utf-8')
if 'Exit criteria for this pass' not in state:
    print('MEMORY_LINT_FAIL: memory/state/current-focus.md must define explicit exit criteria.')
    sys.exit(1)
if len(state.split()) < 40:
    print('MEMORY_LINT_FAIL: memory/state/current-focus.md is too short to be operationally useful.')
    sys.exit(1)

print('MEMORY_LINT_PASS: memory files contain actionable decisions, patterns, and state.')
