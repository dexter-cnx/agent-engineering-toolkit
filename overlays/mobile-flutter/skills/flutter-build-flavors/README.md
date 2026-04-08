# flutter-build-flavors

## Summary

Environment-specific builds, app IDs, endpoints, feature toggles, secrets boundaries.

## Use this skill when

Add or review development, staging, and production build segregation for Flutter apps.

## Category

Release

## Related skills

`flutter-web-deployment`, `flutter-app-signing-release`, `flutter-ci-cd-mobile`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_build_flavors.md`
- `prompts/audit_build_flavors.md`
- `templates/build_flavors_plan.template.md`
- `examples/build_flavors_example.md`

## Expected outputs

- environment matrix
- naming scheme
- secret boundary notes

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
