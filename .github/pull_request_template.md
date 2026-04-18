## Summary
Describe the change clearly.

## Why this change belongs here
Explain why this belongs in the foundation toolkit instead of a consuming repository or overlay.

## Type of change
- [ ] Foundation content
- [ ] Overlay content
- [ ] Docs update
- [ ] Prompt pipeline
- [ ] Skill
- [ ] Template
- [ ] CI / repo management
- [ ] Bugfix

## Checklist
- [ ] Root stays stack-agnostic
- [ ] Docs updated if workflow changed
- [ ] Templates and examples aligned
- [ ] Overlay used instead of polluting root
- [ ] CI passes
- [ ] Canonical onboarding path remains unchanged (`README.md -> docs/get-started.md -> docs/adoption-paths.md`)
- [ ] OS invariants still pass (`python3 tools/ci/os_invariant_check.py`)
- [ ] Prompt compiled artifacts were validated (`compile_prompts.py` + `validate_prompt_pack.py`)
