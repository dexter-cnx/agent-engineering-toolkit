# Agent Flow Demo (Working Example)

This demo shows a real input → agent checks → output artifact flow.

## Input

- `input.md` (a small requested change)

## Commands

```bash
cat examples/working/agent-flow-demo/input.md
python3 tools/ci/os_invariant_check.py
python3 tools/ci/doc_lint.py
python3 tools/prompts/compile_prompts.py
python3 tools/prompts/validate_prompt_pack.py
python3 tools/memory/state_rollup.py
```

## Expected artifacts/output

- `prompts/compiled/codex-runtime.md` (and other provider compiled prompts)
- `artifacts/memory-state-rollup.md`
- PASS markers from invariant/doc/prompt checks

## Before / After

- **Before:** request exists only as text input (`input.md`).
- **After:** request is validated through OS guardrails and produces deterministic artifacts + pass/fail evidence.

## Notes

This is a governance runtime example, not a feature implementation example.
