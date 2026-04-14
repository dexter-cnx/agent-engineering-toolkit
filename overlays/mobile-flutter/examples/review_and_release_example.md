# Review and Release Example

## Scenario

A feature is ready for review and release readiness checks.

Example change:

- code review pass
- release audit
- verification against platform-specific risks

## Recommended skills

- `flutter-code-reviewer`
- `flutter-release-reviewer`
- `guide-app-release-checklist`
- `policy-commit-pr-checks`

## Reference files

- `overlays/mobile-flutter/skills/flutter-code-reviewer/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-release-reviewer/SKILL.md`
- `overlays/mobile-flutter/prompts/code_review.md`
- `overlays/mobile-flutter/prompts/release_audit.md`
- `overlays/mobile-flutter/templates/pull_request_checklist.md`
- `overlays/mobile-flutter/CHECKLIST.md`

## Example invocation

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use these skills:
- flutter-code-reviewer
- flutter-release-reviewer
- guide-app-release-checklist

Task:
Review the feature for correctness, architecture fit, and release readiness.

Deliver:
1. review findings
2. release risks
3. verification gaps
4. go/no-go recommendation
```

## Expected output

- blocking issues are separated from non-blocking notes
- architecture fit is checked explicitly
- release risks are stated without softening
- any remaining verification gaps are visible

## Review notes

- do not merge review and implementation concerns into one blur
- call out platform-specific risks clearly
- keep the recommendation tied to evidence, not preference

## Verification notes

- confirm review findings are separated by severity
- confirm release risks are explicit
- confirm the checklist maps to the release path being reviewed
