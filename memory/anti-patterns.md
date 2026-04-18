# Anti-Patterns

## 1) "Everything is canonical"
When many docs claim to be starting points, users pick random entrypoints and drift.
**Prevention:** enforce one onboarding path and lint redirectors.

## 2) Generic role definitions
Role docs that are interchangeable do not create real accountability.
**Prevention:** each role must own concrete inputs, outputs, and escalation triggers.

## 3) Placeholder governance
Scripts that only check file existence give false confidence.
**Prevention:** lint scripts must validate content contracts, not only path presence.

## 4) Prompt sprawl
Creating prompts without source/pack/compiled discipline causes inconsistent execution.
**Prevention:** maintain prompt catalog + compilation checks in CI.
