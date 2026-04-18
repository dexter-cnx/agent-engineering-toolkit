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
]

missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('DOC_LINT_FAIL: Missing canonical docs:')
    print('\n'.join(f' - {m}' for m in missing))
    sys.exit(1)

readme = (ROOT / 'README.md').read_text(encoding='utf-8')
for phrase in ['## Start in 30 seconds', '## Choose your path (concise)', '## Overlay catalog (concise)', '## Runnable/reference paths (concise)']:
    if phrase not in readme:
        print(f'DOC_LINT_FAIL: README.md missing required section: {phrase}')
        sys.exit(1)
if 'Single onboarding rule:' not in readme:
    print('DOC_LINT_FAIL: README.md must explicitly state single onboarding rule.')
    sys.exit(1)

get_started = (ROOT / 'docs/get-started.md').read_text(encoding='utf-8').lower()
if 'single onboarding path' not in get_started:
    print('DOC_LINT_FAIL: docs/get-started.md must declare itself as single onboarding path.')
    sys.exit(1)

# Detect duplicate onboarding claims in known competing entrypoint docs.
entrypoint_candidates = [
    'START_HERE.md', 'README_START_HERE.md', 'HOW_TO_USE.md',
    'ONBOARDING_MINIMAL.md', 'ONBOARDING_FULL.md', 'INDEX_CANONICAL.md'
]
for rel in entrypoint_candidates:
    txt = (ROOT / rel).read_text(encoding='utf-8').lower()
    if 'compatibility redirect' not in txt or 'not canonical' not in txt:
        print(f'DOC_LINT_FAIL: {rel} must remain compatibility-only and non-canonical.')
        sys.exit(1)
redirect_expectations = {
    'START_HERE.md': 'generic root onboarding index',
    'README_START_HERE.md': 'old "start here" reading order',
    'HOW_TO_USE.md': 'overlay-centric usage flow',
    'ONBOARDING_MINIMAL.md': 'minimal onboarding checklist',
    'ONBOARDING_FULL.md': 'phased full onboarding program',
    'INDEX_CANONICAL.md': 'canonical baseline docs at root',
}
for rel, legacy_desc in redirect_expectations.items():
    path = ROOT / rel
    if not path.exists():
        print(f'DOC_LINT_FAIL: Missing redirector doc {rel}')
        sys.exit(1)
    txt = path.read_text(encoding='utf-8').lower()
    if 'compatibility redirect' not in txt or 'not canonical' not in txt or legacy_desc.lower() not in txt:
        print(f'DOC_LINT_FAIL: {rel} must state legacy purpose and compatibility-only status.')
        sys.exit(1)

print('DOC_LINT_PASS: canonical docs present, duplicate onboarding prevented, redirectors are explicit.')
