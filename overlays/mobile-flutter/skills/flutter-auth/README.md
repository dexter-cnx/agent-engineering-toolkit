# flutter-auth

## Summary

Authentication, session lifecycle, guarded routes, token refresh, logout hygiene.

## Use this skill when

Build or review login, logout, session restoration, guarded navigation, or identity-aware UI flows.

## Category

Core

## Related skills

`flutter-storage`, `flutter-networking`, `flutter-deep-link`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_auth.md`
- `prompts/audit_auth.md`
- `templates/auth_plan.template.md`
- `examples/auth_example.md`

## Expected outputs

- session policy
- guarded route matrix
- auth state model

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
