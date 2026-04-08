# flutter-feature-flags

## Summary

Feature flag evaluation, defaults, overrides, rollout safety, kill switches.

## Use this skill when

Add or review gradual rollout controls and local developer overrides.

## Category

Product

## Related skills

`flutter-remote-config`, `flutter-storage`, `flutter-analytics`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_feature_flags.md`
- `prompts/audit_feature_flags.md`
- `templates/feature_flags_plan.template.md`
- `examples/feature_flags_example.md`

## Expected outputs

- flag registry
- default matrix
- override policy

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
