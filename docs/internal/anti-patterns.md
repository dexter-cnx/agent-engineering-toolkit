# Internal Anti-Patterns

## 1. Foundation becoming product-specific
Bad: shared docs start naming one product, one stack detail, or one team's workflow as the default truth.

## 2. Prompt-first, architecture-later
Bad: implementation prompts define structure accidentally because architecture was skipped.

## 3. Tutorial drift
Bad: tutorials explain rules differently from architecture docs.

## 4. Example becomes policy
Bad: people copy an example folder layout and assume it is the canonical architecture.

## 5. Overlay leakage
Bad: overlay assumptions leak into core templates, docs, or AGENTS files.

## 6. Unverifiable output
Bad: prompts generate code or docs with no acceptance checks.

## 7. Duplicate navigation
Bad: README, tutorial hub, and doc map all say different entry points.

## 8. One giant super-prompt
Bad: lead, architecture, implementation, and review collapse into one opaque instruction blob.
