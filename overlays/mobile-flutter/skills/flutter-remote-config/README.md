# flutter-remote-config

## Summary

Remote configuration fetch, activation, defaults, validation, rollback safety.

## Use this skill when

Add or review remotely controlled app behavior while keeping defaults explicit and safe.

## Category

Product

## Related skills

`flutter-feature-flags`, `flutter-storage`, `flutter-networking`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_remote_config.md`
- `prompts/audit_remote_config.md`
- `templates/remote_config_plan.template.md`
- `examples/remote_config_example.md`

## Expected outputs

- config registry
- default values
- activation rules

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
