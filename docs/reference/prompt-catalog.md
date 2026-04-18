# Prompt Catalog

## Canonical prompts (editable source)
- `prompts/system/operating-contract.md`
- `prompts/tasks/repo-hardening.md`
- `prompts/tasks/release-readiness.md`

## Provider pack manifests
- `prompts/packs/codex/pack-manifest.md`
- `prompts/packs/claude/pack-manifest.md`
- `prompts/packs/gemini/pack-manifest.md`

## Generated compiled outputs (read-only)
- `prompts/compiled/codex-runtime.md`
- `prompts/compiled/claude-runtime.md`
- `prompts/compiled/gemini-runtime.md`

## Build and validation commands
```bash
python3 tools/prompts/compile_prompts.py
python3 tools/prompts/validate_prompt_pack.py
```
