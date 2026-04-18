# ADR 0003: Governance Check Philosophy

## Status
Accepted

## Context
Initial governance checks focused on structural presence (files/folders). That baseline was useful but insufficient for release confidence.

## Decision
Governance checks must validate **behavioral contracts** where possible:
- docs: canonical onboarding and compatibility-only redirect semantics
- overlays: explicit boundary statements
- prompts: canonical source/pack/compiled mapping and freshness
- memory: minimum decision/state quality expectations

## Consequences
- CI failures become more actionable and trustworthy.
- Decorative/placeholder content is less likely to pass.
- Maintenance cost increases slightly but is justified by higher signal.
