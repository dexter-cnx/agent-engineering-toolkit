#!/usr/bin/env python3
from pathlib import Path
import hashlib
import re

ROOT = Path(__file__).resolve().parents[2]
providers = ['codex', 'claude', 'gemini']
bullet = re.compile(r'^- `([^`]+)`$')

for provider in providers:
    manifest = ROOT / f'prompts/packs/{provider}/pack-manifest.md'
    srcs = []
    for raw in manifest.read_text(encoding='utf-8').splitlines():
        m = bullet.match(raw.strip())
        if not m:
            continue
        val = m.group(1)
        if val.startswith('prompts/compiled/'):
            continue
        srcs.append(val)

    if not srcs:
        raise SystemExit(f'COMPILE_FAIL: no sources found in {manifest.relative_to(ROOT)}')

    parts = []
    for src in srcs:
        src_path = ROOT / src
        if not src_path.exists():
            raise SystemExit(f'COMPILE_FAIL: missing source {src}')
        parts.append(src_path.read_text(encoding='utf-8').strip())

    joined = '\n\n---\n\n'.join(parts)
    checksum = hashlib.sha256(joined.encode('utf-8')).hexdigest()
    source_list = ', '.join(srcs)

    out = ROOT / f'prompts/compiled/{provider}-runtime.md'
    compiled_text = (
        f'# Compiled {provider.title()} Runtime Prompt\n\n'
        '<!-- generated: tools/prompts/compile_prompts.py -->\n'
        f'<!-- provider: {provider} -->\n'
        f'<!-- sources: {source_list} -->\n'
        f'<!-- content_sha256: {checksum} -->\n\n'
        + joined
        + '\n'
    )
    out.write_text(compiled_text, encoding='utf-8')
    print(f'WROTE: {out.relative_to(ROOT)} (sources={len(srcs)}, sha256={checksum[:12]})')
