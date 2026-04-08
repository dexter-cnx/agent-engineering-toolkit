# flutter-permissions

## Summary

Permission education, request orchestration, denied and permanently denied flows.

## Use this skill when

Add or review feature access that depends on runtime permissions across Android and iOS.

## Category

Core

## Related skills

`flutter-geolocation`, `flutter-maps`, `flutter-camera-media`, `flutter-push-notifications`, `flutter-contacts-sharing`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_permissions.md`
- `prompts/audit_permissions.md`
- `templates/permissions_plan.template.md`
- `examples/permissions_example.md`

## Expected outputs

- permission rationale
- request orchestration
- fallback UX

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
