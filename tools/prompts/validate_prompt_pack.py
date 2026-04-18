#!/usr/bin/env python3
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
providers = ['codex', 'claude', 'gemini']
bullet = re.compile(r'^- `([^`]+)`$')
sha_marker = re.compile(r'content_sha256: ([0-9a-f]{64})')
failed = False

for provider in providers:
    manifest = ROOT / f'prompts/packs/{provider}/pack-manifest.md'
    compiled = ROOT / f'prompts/compiled/{provider}-runtime.md'

    if not manifest.exists() or not compiled.exists():
        print(f'PROMPT_PACK_FAIL: missing files for provider={provider}')
        failed = True
        continue

    srcs = []
    for raw in manifest.read_text(encoding='utf-8').splitlines():
        m = bullet.match(raw.strip())
        if not m:
            continue
        p = m.group(1)
        if p.startswith('prompts/compiled/'):
            continue
        srcs.append(p)

    if not srcs:
        print(f'PROMPT_PACK_FAIL: {manifest.relative_to(ROOT)} has no source mappings')
        failed = True
        continue

    source_texts = []
    provider_failed = False
    for src in srcs:
        src_path = ROOT / src
        if not src_path.exists():
            print(f'PROMPT_PACK_FAIL: source missing for {provider}: {src}')
            failed = True
            provider_failed = True
            break
        source_texts.append(src_path.read_text(encoding='utf-8').strip())
    if provider_failed:
        continue

    joined = '\n\n---\n\n'.join(source_texts)
    expected_sha = hashlib.sha256(joined.encode('utf-8')).hexdigest()
    actual = compiled.read_text(encoding='utf-8')
    source_list = ', '.join(srcs)
    expected_compiled = (
        f'# Compiled {provider.title()} Runtime Prompt\n\n'
        '<!-- generated: tools/prompts/compile_prompts.py -->\n'
        f'<!-- provider: {provider} -->\n'
        f'<!-- sources: {source_list} -->\n'
        f'<!-- content_sha256: {expected_sha} -->\n\n'
        + joined
        + '\n'
    )

    if actual != expected_compiled:
        print(
            f'PROMPT_PACK_FAIL: {compiled.relative_to(ROOT)} does not exactly match generated body; '
            'run compile_prompts.py'
        )
        failed = True

    m = sha_marker.search(actual)
    if not m:
        print(f'PROMPT_PACK_FAIL: {compiled.relative_to(ROOT)} missing checksum marker')
        failed = True
    elif m.group(1) != expected_sha:
        print(f'PROMPT_PACK_FAIL: {compiled.relative_to(ROOT)} checksum mismatch (expected {expected_sha[:12]})')
        failed = True

    print(f'PROMPT_PACK_OK: {provider} sources={len(srcs)} content_sha={expected_sha[:12]}')

if failed:
    sys.exit(1)
print('PROMPT_PACK_PASS: compiled prompts are consistent with source mappings.')
