# flutter-push-notifications

## Summary

FCM/APNs orchestration, token registration, tap-to-route behavior.

## Use this skill when

Add or review remote notifications without leaking provider SDK logic across widgets and features.

## Category

Core

## Related skills

`flutter-auth`, `flutter-deep-link`, `flutter-storage`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_push_notifications.md`
- `prompts/audit_push_notifications.md`
- `templates/push_notifications_plan.template.md`
- `examples/push_notifications_example.md`

## Expected outputs

- event model
- routing map
- token lifecycle notes

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
