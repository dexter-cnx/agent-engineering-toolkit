#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

required = [
    'README.md',
    'docs/get-started.md',
    'docs/adoption-paths.md',
    'docs/overlays.md',
    'docs/architecture/os-overview.md',
    'docs/architecture/task-lifecycle.md',
    'docs/reference/canonical-doc-map.md',
    'docs/legacy/README.md',
]

missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('DOC_LINT_FAIL: Missing canonical docs:')
    print('\n'.join(f' - {m}' for m in missing))
    sys.exit(1)

readme = (ROOT / 'README.md').read_text(encoding='utf-8')
for phrase in ['## What this repo is', '## Start here', '## Choose path', '## Choose overlay', '## Secondary References']:
    if phrase not in readme:
        print(f'DOC_LINT_FAIL: README.md missing required section: {phrase}')
        sys.exit(1)
if 'Single onboarding rule:' not in readme:
    print('DOC_LINT_FAIL: README.md must explicitly state single onboarding rule.')
    sys.exit(1)

for legacy_name in [
    'START_HERE.md', 'README_START_HERE.md', 'HOW_TO_USE.md',
    'ONBOARDING_MINIMAL.md', 'ONBOARDING_FULL.md', 'INDEX_CANONICAL.md',
    'INDEX_PROMPTS.md', 'INDEX_COMPANION.md', 'INDEX_CHECKLISTS.md',
    'CHECKLIST.md', 'SKILLS_INDEX.md', 'PHASE_21_FINAL_POLISH.md'
]:
    if legacy_name in readme:
        print(f'DOC_LINT_FAIL: README.md must not reference legacy root file {legacy_name}')
        sys.exit(1)

get_started = (ROOT / 'docs/get-started.md').read_text(encoding='utf-8').lower()
if 'single onboarding path' not in get_started:
    print('DOC_LINT_FAIL: docs/get-started.md must declare itself as single onboarding path.')
    sys.exit(1)

legacy_required = [
    'START_HERE.md', 'README_START_HERE.md', 'HOW_TO_USE.md',
    'ONBOARDING_MINIMAL.md', 'ONBOARDING_FULL.md', 'INDEX_CANONICAL.md',
    'INDEX_PROMPTS.md', 'INDEX_COMPANION.md', 'INDEX_CHECKLISTS.md',
    'CHECKLIST.md', 'SKILLS_INDEX.md', 'PHASE_21_FINAL_POLISH.md'
]

for rel in legacy_required:
    path = ROOT / 'docs/legacy' / rel
    if not path.exists():
        print(f'DOC_LINT_FAIL: Missing archived legacy doc docs/legacy/{rel}')
        sys.exit(1)

print('DOC_LINT_PASS: canonical docs present, onboarding chain preserved, and legacy root drift archived.')
