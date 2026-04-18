# Patterns

## 1) Canonical-first navigation
Keep one onboarding path (`README` → `docs/get-started` → `docs/adoption-paths`).
This reduces onboarding time and prevents contradictory setup advice.

## 2) Policy must be executable
Every critical governance rule is paired with a lint/workflow check.
If a rule cannot be checked at all, mark it as human-review-only explicitly.

## 3) Redirect instead of remove
When replacing legacy docs, convert them into explicit compatibility redirects.
This preserves inbound links while preventing new divergence.

## 4) Overlay contracts as boundary guards
Overlay READMEs must state when to use and what they do not replace.
This prevents stack-specific logic from leaking into foundation docs.
