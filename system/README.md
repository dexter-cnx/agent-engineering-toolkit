# System Layer (Canonical)

Operational kernel for repository behavior and governance enforcement.

## kernel/
Defines static invariants: canonical paths, naming, documentation and release policy.

## runtime/
Defines execution contracts for task delivery, handoff quality, review, and acceptance.

## policies/
Defines enforcement intent (evidence, deprecation, edit-scope) that CI/tooling must support.

## Rule of use
When repository behavior and docs disagree, update either policy or implementation so they match; never leave silent drift.

## Boundary note

`core/` is a legacy/frozen quick-reference namespace.
Canonical operating contracts live in `system/`.
