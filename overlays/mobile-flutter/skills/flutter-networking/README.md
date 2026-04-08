# flutter-networking

## Summary

API clients, DTO mapping, retry and timeout policy, normalized errors.

## Use this skill when

Add or review remote data access while keeping transport details out of domain and UI layers.

## Category

Core

## Related skills

`flutter-auth`, `flutter-offline-first`, `flutter-remote-config`, `flutter-analytics`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_networking.md`
- `prompts/audit_networking.md`
- `templates/networking_plan.template.md`
- `examples/networking_example.md`

## Expected outputs

- service contract
- error mapping
- DTO-domain mapping

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
