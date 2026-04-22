# Release Candidate Checklist

Use this checklist before tagging an RC release.

## Required verification checks

- `python3 tools/ci/os_invariant_check.py`
- `python3 tools/ci/doc_lint.py`
- `python3 tools/ci/coherence_lint.py`
- `python3 tools/ci/link_check.py`
- `python3 tools/ci/overlay_lint.py`
- `python3 tools/ci/prompt_lint.py`
- `python3 tools/ci/memory_lint.py`
- `node --experimental-strip-types tools/ci/check-canonical-consistency.ts`
- `node --experimental-strip-types tools/ci/check-merge-gate-consistency.ts`
- `node --experimental-strip-types tools/ci/check-package-metadata.ts`
- `node --experimental-strip-types --test tests/runtime/runtime.test.mjs`
- `npm run os:pack:dryrun`

## Metadata verification

Confirm `package.json` includes correct:

- repository URL
- homepage URL
- bugs URL
- `bin.os` mapping
- engines (`node`, `npm`)
- publish access (`publishConfig.access`)

## Contract-stability expectations

- Machine outputs include `contractVersion`.
- Exit code semantics stay stable (`0`, `1`, `2`).
- Any contract change follows `docs/runtime/cli-contract-governance.md`.

## Scope boundary (intentional)

- Simulation-only prompt execution remains in scope.
- Real provider execution remains out of scope for RC.
