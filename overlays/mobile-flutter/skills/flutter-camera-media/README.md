# flutter-camera-media

## Summary

Camera capture, gallery pick, media constraints, compression, upload preparation.

## Use this skill when

Add or review camera and media flows while isolating platform plugins behind adapters.

## Category

Device

## Related skills

`flutter-permissions`, `flutter-file-upload-download`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_camera_media.md`
- `prompts/audit_camera_media.md`
- `templates/camera_media_plan.template.md`
- `examples/camera_media_example.md`

## Expected outputs

- capture policy
- media constraints
- failure matrix

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
