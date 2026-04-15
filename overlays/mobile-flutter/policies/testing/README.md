# Testing Policy

## Minimum expectations

- Add tests when behavior changes.
- Cover repository and state behavior with unit tests where practical.
- Cover user-facing flows with widget or integration tests when the change touches UI.
- Verify release changes with platform-specific checks.

## Rules

- Do not count screenshots alone as verification.
- Do not skip tests for auth, routing, or repository wiring.
- Do not add brittle tests that depend on implementation trivia.
- Prefer behavior assertions over private-member assertions.

## Verification checklist

- The expected file tree exists.
- The main branch of the new behavior is covered.
- Failure and edge-case paths are considered.
