#!/usr/bin/env python3
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
link_pattern = re.compile(r'\[[^\]]+\]\(([^)]+)\)')

files = [
    ROOT / 'README.md',
    ROOT / 'START_HERE.md',
    ROOT / 'README_START_HERE.md',
    ROOT / 'HOW_TO_USE.md',
    ROOT / 'ONBOARDING_MINIMAL.md',
    ROOT / 'ONBOARDING_FULL.md',
    ROOT / 'INDEX_CANONICAL.md',
    ROOT / 'docs/get-started.md',
    ROOT / 'docs/adoption-paths.md',
    ROOT / 'docs/overlays.md',
]

for dir_path in [ROOT / 'docs/architecture', ROOT / 'docs/reference', ROOT / 'docs/graph', ROOT / 'agents', ROOT / 'memory', ROOT / 'prompts', ROOT / 'system']:
    files.extend(dir_path.rglob('*.md'))

files.extend((ROOT / 'overlays').glob('*/README.md'))

failed = False
for md in sorted(set(files)):
    if not md.exists():
        print(f'LINK_CHECK_FAIL: missing required file {md.relative_to(ROOT)}')
        failed = True
        continue
    text = md.read_text(encoding='utf-8', errors='ignore')
    for target in link_pattern.findall(text):
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1]
        target = target.split('#')[0]
        if not target:
            continue
        resolved = (md.parent / target).resolve()
        if not resolved.exists():
            print(f'LINK_CHECK_FAIL: {md.relative_to(ROOT)} -> {target}')
            failed = True

if failed:
    sys.exit(1)
print(f'LINK_CHECK_PASS: validated internal markdown links across {len(set(files))} governed docs.')
