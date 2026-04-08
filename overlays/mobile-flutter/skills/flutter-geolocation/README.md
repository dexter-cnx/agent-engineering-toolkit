# flutter-geolocation

## Summary

Current position, watch position, accuracy policy, service-disabled handling.

## Use this skill when

Add or review location-aware features without coupling UI directly to geolocation plugins.

## Category

Core

## Related skills

`flutter-permissions`, `flutter-maps`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_geolocation.md`
- `prompts/audit_geolocation.md`
- `templates/geolocation_plan.template.md`
- `examples/geolocation_example.md`

## Expected outputs

- location policy
- service contract
- failure matrix

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
