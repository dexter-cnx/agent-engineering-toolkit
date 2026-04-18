#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
overlays = sorted((ROOT / 'overlays').glob('*/README.md'))
required_sections = [
    '## Overlay OS contract',
    '### Purpose',
    '### When to use',
    '### Relation to root guidance',
    '### Boundaries',
    '### What this overlay does not replace',
]

section_re = re.compile(r'### (Purpose|When to use|Relation to root guidance|Boundaries|What this overlay does not replace)\n([\s\S]*?)(?=\n### |\Z)')
failed = False

for readme in overlays:
    txt = readme.read_text(encoding='utf-8')
    lower = txt.lower()

    for marker in required_sections:
        if marker not in txt:
            print(f'OVERLAY_LINT_FAIL: {readme.relative_to(ROOT)} missing section: {marker}')
            failed = True

    if 'stack-neutral' not in lower:
        print(f'OVERLAY_LINT_FAIL: {readme.relative_to(ROOT)} must mention stack-neutral root foundation.')
        failed = True

    extracted = {name: body.strip() for name, body in section_re.findall(txt)}
    for name in ['Purpose', 'When to use', 'Boundaries', 'What this overlay does not replace']:
        body = extracted.get(name, '')
        if len(body.split()) < 8:
            print(f'OVERLAY_LINT_FAIL: {readme.relative_to(ROOT)} section "{name}" is too thin to be actionable.')
            failed = True

    if 'does not replace' not in extracted.get('What this overlay does not replace', '').lower():
        print(f'OVERLAY_LINT_FAIL: {readme.relative_to(ROOT)} non-replacement section must explicitly use replacement wording.')
        failed = True

if failed:
    sys.exit(1)
print(f'OVERLAY_LINT_PASS: validated structure and actionable overlay boundaries across {len(overlays)} overlays.')
