# Memory State Rollup

## current-focus.md

# Current Focus

## Objective
Move from structural bootstrap to production readiness of governance behavior.

## In progress
- Tighten lint checks from file-existence to content-quality checks.
- Make prompts executable and auditable across providers.
- Reduce onboarding ambiguity to one obvious path.

## Exit criteria for this pass
- New user can start in under 30 seconds from README.
- Redirect docs are compatibility-only and non-competing.
- Roles/workflows contain non-generic operational boundaries.
- CI fails on real contract violations.

## known-debts.md

# Known Debts

1. Legacy long-form docs outside canonical map still exist and may overlap conceptually.
2. Prompt packs currently share one runtime shape; provider-specific variants are limited.
3. Link checks are scoped to canonical docs and graph docs, not every historical markdown file.

## next-pass.md

# Next Pass

1. Add provider-specific prompt variations with safety and token-budget envelopes.
2. Gradually classify legacy docs as canonical, reference, or archive.
3. Add automated stale-memory detection for `memory/state/*` update age.
