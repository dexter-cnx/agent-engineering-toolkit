# OS 5-Minute Quick Start (Working Example)

This is a real runnable baseline path for validating repo governance.

## Commands

```bash
python3 tools/ci/os_invariant_check.py
python3 tools/ci/doc_lint.py
python3 tools/ci/link_check.py
python3 tools/prompts/compile_prompts.py
python3 tools/prompts/validate_prompt_pack.py
```

## Expected result

- All commands exit with status code `0`.
- Prompt compile writes or refreshes `prompts/compiled/*-runtime.md`.
- Prompt validate confirms source/compiled consistency and checksum markers.

## Why this matters

This path gives contributors a fast, production-relevant smoke test of core OS governance before deeper app/package checks.
