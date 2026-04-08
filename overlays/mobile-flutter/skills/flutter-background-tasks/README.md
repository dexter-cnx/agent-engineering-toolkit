# flutter-background-tasks

## Summary

Scheduled work, background fetch, retry windows, battery-sensitive execution.

## Use this skill when

Add or review background processing such as sync, cleanup, and deferred uploads.

## Category

Device

## Related skills

`flutter-offline-first`, `flutter-push-notifications`, `flutter-storage`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_background_tasks.md`
- `prompts/audit_background_tasks.md`
- `templates/background_tasks_plan.template.md`
- `examples/background_tasks_example.md`

## Expected outputs

- task registry
- execution policy
- battery constraints

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
