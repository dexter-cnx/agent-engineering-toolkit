# flutter-offline-first

## Summary

Cache-first reads, sync queues, optimistic updates, conflict handling.

## Use this skill when

Add or review offline-capable user flows and synchronization behavior.

## Category

Product

## Related skills

`flutter-storage`, `flutter-networking`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_offline_first.md`
- `prompts/audit_offline_first.md`
- `templates/offline_first_plan.template.md`
- `examples/offline_first_example.md`

## Expected outputs

- sync strategy
- conflict policy
- queue ownership plan

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
