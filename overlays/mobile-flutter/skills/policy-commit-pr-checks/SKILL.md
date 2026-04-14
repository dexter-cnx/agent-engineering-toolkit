# policy-commit-pr-checks

## Category

policy

## Purpose

Required lint, format, tests, docs, and review gates before merge.

## When to use

Use this skill when the task directly involves **required lint, format, tests, docs, and review gates before merge.**.

## Default behavior

- Stay consistent with `policy-folder-structure` and `policy-clean-architecture`.
- Prefer production-safe, testable output.
- Keep user-facing strings localizable.
- Keep business logic out of widgets unless this skill explicitly states otherwise.

## What this skill should help produce

- Clear implementation plan
- Flutter-specific code patterns
- Platform setup notes where needed
- Follow-up checks or review points

## Recommended companion skills

- `flutter-dev`
- `flutter-code-reviewer`
- `flutter-ci-checks`

## Execution notes

1. Clarify the scope of the request in implementation terms.
2. Apply the most relevant architecture and policy skills.
3. Generate or review code with maintainability in mind.
4. Add tests and docs where the change justifies them.
