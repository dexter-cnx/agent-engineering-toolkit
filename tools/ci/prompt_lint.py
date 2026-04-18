#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
required = [
    'prompts/README.md',
    'prompts/system/operating-contract.md',
    'prompts/tasks/repo-hardening.md',
    'prompts/tasks/release-readiness.md',
    'prompts/packs/codex/pack-manifest.md',
    'prompts/packs/claude/pack-manifest.md',
    'prompts/packs/gemini/pack-manifest.md',
    'prompts/compiled/codex-runtime.md',
    'prompts/compiled/claude-runtime.md',
    'prompts/compiled/gemini-runtime.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('PROMPT_LINT_FAIL: Missing prompt runtime files:')
    for m in missing:
        print(f' - {m}')
    sys.exit(1)

readme = (ROOT / 'prompts/README.md').read_text(encoding='utf-8')
for phrase in ['Canonical source prompts', 'Provider packs', 'Compiled prompts']:
    if phrase not in readme:
        print(f'PROMPT_LINT_FAIL: prompts/README.md missing section: {phrase}')
        sys.exit(1)

for provider in ['codex', 'claude', 'gemini']:
    compiled = (ROOT / f'prompts/compiled/{provider}-runtime.md').read_text(encoding='utf-8')
    if 'generated: tools/prompts/compile_prompts.py' not in compiled:
        print(f'PROMPT_LINT_FAIL: compiled prompt missing generation marker for {provider}')
        sys.exit(1)

print('PROMPT_LINT_PASS: prompt runtime structure and compiled metadata are valid.')
