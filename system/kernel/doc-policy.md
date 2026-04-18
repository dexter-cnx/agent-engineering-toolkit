# Doc Policy

## Non-negotiables
1. Canonical onboarding is a single path (`README -> docs/get-started -> docs/adoption-paths`).
2. Legacy root onboarding docs are compatibility-only redirects.
3. Canonical docs must not duplicate conflicting instructions.
4. Structural workflow/policy changes require matching doc updates in the same change.

## Enforcement
- `tools/ci/doc_lint.py`
- `tools/ci/link_check.py`
