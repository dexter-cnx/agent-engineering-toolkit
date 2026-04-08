# Prompt Pipeline

This is the canonical source of truth for the toolkit lifecycle.

## Canonical lifecycle

1. `PLAN`
2. `DESIGN`
3. `IMPLEMENT`
4. `REVIEW`
5. `VERIFY`
6. `FINALIZE`
7. `MEMORY`

## Prompt mapping

1. `prompts/plan_change.md`
2. `prompts/architecture_review.md`
3. `prompts/implement_change.md`
4. `prompts/review_change.md`
5. `prompts/verification_pass.md`
6. `prompts/finalize_change.md`
7. `prompts/update_project_memory.md`

## Usage notes
- Not every task needs every prompt.
- Non-trivial work usually benefits from the full sequence.
- Structural work should almost always include PLAN, DESIGN, REVIEW, VERIFY, and MEMORY.
- Avoid redefining the lifecycle order elsewhere. Link back to this file instead.
