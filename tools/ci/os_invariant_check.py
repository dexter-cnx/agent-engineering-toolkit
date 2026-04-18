#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INV = ROOT / 'system/kernel/os-invariants.md'


def fail(msg: str) -> None:
    print(f'OS_INVARIANT_FAIL: {msg}')
    sys.exit(1)


def load_invariants() -> dict:
    txt = INV.read_text(encoding='utf-8')
    m = re.search(r'```json\n([\s\S]*?)\n```', txt)
    if not m:
        fail('system/kernel/os-invariants.md missing machine-readable json block')
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError as exc:
        fail(f'invalid json in os-invariants.md: {exc}')


def check_onboarding(inv: dict) -> None:
    front = ROOT / inv['front_door']
    if not front.exists():
        fail(f'missing front door: {inv["front_door"]}')
    readme = front.read_text(encoding='utf-8')
    if 'Single onboarding rule:' not in readme:
        fail('README.md must explicitly contain "Single onboarding rule:"')

    for rel in inv['canonical_onboarding']:
        if not (ROOT / rel).exists():
            fail(f'missing canonical onboarding file: {rel}')

    # Prevent secondary onboarding claims outside approved files.
    approved = set(inv['canonical_onboarding']) | set(inv['compatibility_root_docs'])
    markers = ['single onboarding path', 'canonical onboarding', 'start in 30 seconds']
    candidate_entrypoints = [
        'START_HERE.md', 'README_START_HERE.md', 'HOW_TO_USE.md',
        'ONBOARDING_MINIMAL.md', 'ONBOARDING_FULL.md', 'INDEX_CANONICAL.md',
        'INDEX_PROMPTS.md', 'INDEX_COMPANION.md', 'INDEX_CHECKLISTS.md'
    ]
    for rel in candidate_entrypoints:
        md = ROOT / rel
        if not md.exists():
            continue
        text = md.read_text(encoding='utf-8', errors='ignore').lower()
        if any(m in text for m in markers) and rel not in approved and 'legacy' not in text and 'compatibility' not in text:
            fail(f'unapproved onboarding claim in root doc: {rel}')


def check_root_doc_classification(inv: dict) -> None:
    allowed = set(inv['canonical_onboarding']) | set(inv['compatibility_root_docs'])
    # Additional classified root docs expected to be legacy/reference status notes.
    allowed |= {
        'README_TH.md', 'CHANGELOG.md', 'CHECKLIST.md', 'CODE_OF_CONDUCT.md', 'CONTRIBUTING.md',
        'LICENSE', 'SECURITY.md', 'AGENTS.md', 'AGENTS.overlay.md', 'INDEX_PROMPTS.md',
        'INDEX_COMPANION.md', 'INDEX_CHECKLISTS.md', 'SKILLS_INDEX.md', 'PHASE_21_FINAL_POLISH.md',
        'TREE.txt'
    }
    for md in ROOT.glob('*.md'):
        if md.name not in allowed:
            fail(f'unclassified root markdown file detected: {md.name}')


def check_top_level_dirs(inv: dict) -> None:
    classified = {}
    for status, dirs in inv['managed_top_level_dirs'].items():
        for d in dirs:
            if d in classified:
                fail(f'directory appears in multiple classifications: {d}')
            classified[d] = status

    ignored = set(inv['ignored_top_level_dirs'])
    actual_dirs = sorted([p.name for p in ROOT.iterdir() if p.is_dir() and p.name not in ignored])

    for d in actual_dirs:
        if d not in classified:
            fail(f'top-level directory missing classification: {d}')

    for d, status in classified.items():
        p = ROOT / d
        if not p.exists():
            fail(f'classified top-level directory not found: {d}')
        readme = p / 'README.md'
        if not readme.exists():
            fail(f'top-level directory missing README.md: {d}/README.md')
        text = readme.read_text(encoding='utf-8', errors='ignore').lower()
        needed = status if status != 'legacy' else 'legacy'
        if needed not in text:
            fail(f'{d}/README.md must declare status containing "{needed}"')
        if not any(k in text for k in inv['status_keywords']):
            fail(f'{d}/README.md missing classification keyword set: {inv["status_keywords"]}')


def check_duplication_guards(inv: dict) -> None:
    canonical_dirs = set(inv['managed_top_level_dirs']['canonical'])
    if 'agents' not in canonical_dirs or 'memory' not in canonical_dirs:
        fail('agents and memory must remain canonical surfaces')
    if 'agent_team' in canonical_dirs or 'project_memory' in canonical_dirs:
        fail('legacy parallel namespaces must not be canonical')


def check_compiled_prompts(inv: dict) -> None:
    for rel in inv['compiled_prompts']:
        p = ROOT / rel
        if not p.exists():
            fail(f'missing compiled prompt: {rel}')
        txt = p.read_text(encoding='utf-8', errors='ignore')
        if 'generated: tools/prompts/compile_prompts.py' not in txt:
            fail(f'compiled prompt missing generator marker: {rel}')


def main() -> None:
    if not INV.exists():
        fail('missing invariant source file system/kernel/os-invariants.md')
    inv = load_invariants()
    check_onboarding(inv)
    check_root_doc_classification(inv)
    check_top_level_dirs(inv)
    check_duplication_guards(inv)
    check_compiled_prompts(inv)
    print('OS_INVARIANT_PASS: repository invariants are satisfied.')


if __name__ == '__main__':
    main()
