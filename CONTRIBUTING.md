# Contributing

Thank you for contributing to `agent-engineering-toolkit`.

## Scope
This repository is the **foundation layer** of the toolkit. Keep root-level content:
- stack-agnostic
- reusable
- clearly documented
- easy to adopt across multiple project types

Do **not** add technology-specific assumptions to the foundation unless they are truly generic. Put stack-specific material in `overlays/`.

## Before opening a pull request
Please check:
1. The change fits the foundation identity of the repository.
2. Canonical docs are updated if workflow or structure changed (`README -> docs/get-started -> docs/adoption-paths`).
3. Examples/templates still match current guidance.
4. The relevant overlay was updated instead of polluting the root.
5. CI still passes.

## Preferred contribution flow
1. Open an issue first for large changes.
2. Keep pull requests focused.
3. Explain why the change belongs in foundation vs overlay.
4. Include before/after rationale when changing workflow or docs.

## Pull request checklist
- [ ] I kept the root stack-agnostic.
- [ ] I updated docs where needed.
- [ ] I checked prompts/templates/examples for alignment.
- [ ] I added or updated overlay content if specialization was needed.
- [ ] I ran relevant checks locally.

## Recommended local enforcement checks

```bash
python3 tools/ci/os_invariant_check.py
python3 tools/ci/doc_lint.py
python3 tools/ci/link_check.py
python3 tools/ci/overlay_lint.py
python3 tools/ci/prompt_lint.py
python3 tools/ci/memory_lint.py
python3 tools/prompts/compile_prompts.py
python3 tools/prompts/validate_prompt_pack.py
```

## File placement guidance
GitHub surfaces contributing guidelines from the root, `docs/`, or `.github/` directory. This file is kept at the root so contributors can discover it easily. 
