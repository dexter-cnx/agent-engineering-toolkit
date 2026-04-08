# flutter-biometric-auth

## Summary

Biometric prompts, fallback auth, secure-session unlock, device capability checks.

## Use this skill when

Add or review biometric login or step-up verification flows.

## Category

Device

## Related skills

`flutter-auth`, `flutter-storage`, `flutter-permissions`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_biometric_auth.md`
- `prompts/audit_biometric_auth.md`
- `templates/biometric_auth_plan.template.md`
- `examples/biometric_auth_example.md`

## Expected outputs

- capability matrix
- fallback path
- unlock policy

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
