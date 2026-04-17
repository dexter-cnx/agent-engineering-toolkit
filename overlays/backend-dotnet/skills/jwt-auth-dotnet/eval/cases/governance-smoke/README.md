# Governance Smoke Case

This static case keeps the JWT auth contract aligned with the Karpathy governance plane.

## Scenario

An ASP.NET Core backend needs JWT issuance and verification with explicit claims, expiry,
and signing rules.

## Checkpoints

- the contract file exists
- the expected result fixture exists
- the skill can be evaluated with the canonical Karpathy scripts
- promotion stays regression-safe and token-governed
