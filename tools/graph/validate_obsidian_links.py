#!/usr/bin/env python3
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs/graph'
pat = re.compile(r'\[\[([^\]]+)\]\]')
all_docs = {str(p.relative_to(ROOT)).replace('.md', '') for p in (ROOT / 'docs').rglob('*.md')}

failed = False
for md in DOCS.rglob('*.md'):
    text = md.read_text(encoding='utf-8', errors='ignore')
    for target in pat.findall(text):
        t = target.replace('.md', '').lstrip('./')
        candidates = {t, f'docs/{t}'}
        if not any(c in all_docs for c in candidates):
            print(f'OBSIDIAN_LINK_FAIL: {md.relative_to(ROOT)} -> [[{target}]]')
            failed = True
if failed:
    sys.exit(1)
print(f'OBSIDIAN_LINK_PASS: validated wiki links in {DOCS.relative_to(ROOT)}.')
