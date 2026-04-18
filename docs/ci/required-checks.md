# Required CI Checks by Change Type

This document defines mandatory CI governance for production-grade changes.

| Change Type | Required Checks |
|---|---|
| Docs | `doc-governance` |
| Overlay | `overlay-ci` |
| Prompt | `prompt-ci` |
| Fullstack | `fullstack-ci` |
| Release | `release-check` |

## Check definitions

### `doc-governance`
Validates canonical documentation quality, link integrity, and onboarding consistency.

### `overlay-ci`
Validates overlay contract conformance, overlay structure, and specialization boundary safety.

### `prompt-ci`
Validates prompt source quality, prompt compilation integrity, and runtime prompt pack consistency.

### `fullstack-ci`
Validates reference implementation contract compatibility and end-to-end integration expectations.

### `release-check`
Validates release readiness requirements (versioning, changelog discipline, and publish-time integrity signals).
