# flutter-file-upload-download

## Summary

File picking, upload orchestration, download handling, progress and retry UX.

## Use this skill when

Add or review file transfer flows across mobile and web targets.

## Category

Device

## Related skills

`flutter-networking`, `flutter-storage`, `flutter-permissions`

## Skill contents

- `skill.md`
- `checklists/implementation-checklist.md`
- `checklists/verification-checklist.md`
- `prompts/add_file_upload_download.md`
- `prompts/audit_file_upload_download.md`
- `templates/file_upload_download_plan.template.md`
- `examples/file_upload_download_example.md`

## Expected outputs

- transfer contract
- retry policy
- progress states

## Review focus

- keep capability boundaries explicit
- avoid raw SDK or plugin leakage across layers
- keep human overview separate from AI-operational rules
