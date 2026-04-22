# App Log and Production Logging

## Purpose

Show the shortest safe path for adding app-level production logging to a Flutter repository.

## Prerequisites

- You know whether the app already has a logger or needs one
- You know if crash reporting or analytics should receive log handoff
- You have the target logger files or bootstrap entrypoint in mind

## Exact repository paths

- `overlays/mobile-flutter/skills/architecture/flutter-production-logging/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-crash-reporting/SKILL.md`
- `overlays/mobile-flutter/skills/flutter-analytics/SKILL.md`
- `overlays/mobile-flutter/templates/project-bootstrap-template.md`
- `overlays/mobile-flutter/prompts/new_feature.md`

## Step-by-step instructions

1. Open `skills/architecture/flutter-production-logging/SKILL.md` and confirm the logging boundary.
2. Decide which files own the logger interface, context model, and formatter.
3. Wire the logger in the app bootstrap layer, not in widgets.
4. Add crash reporting or analytics adapters only if the app needs them.
5. Redact secrets and personal data before logs leave the boundary.
6. Add tests for formatting, redaction, and fallback behavior.
7. Update `HOW_TO_USE.md` or the relevant feature prompt if the logging path changes.

## What skills to use

- `flutter-production-logging`
- `flutter-crash-reporting` if logs hand off to crash tooling
- `flutter-analytics` if events or breadcrumbs are part of the requirement
- `flutter-clean-architecture-audit` if the logging ownership is unclear

## Expected inputs

- Log event types
- Redaction rules
- Sink destinations
- Crash reporting or analytics integration requirements
- Release verbosity rules

## Expected outputs

- Logger interface and supporting context models
- Formatter and redaction helpers
- Bootstrap wiring for the logging boundary
- Tests for sensitive-data handling

## Common mistakes

- Putting logger calls directly in widgets
- Logging tokens, emails, or other sensitive fields
- Mixing crash reporting adapter code into the UI layer
- Leaving release verbosity too noisy

## Troubleshooting

- If the app only needs temporary debug output, use `print()` locally and do not add the full boundary.
- If the logger becomes noisy, lower release verbosity and keep debug detail only in non-release builds.
- If crash reporting is already wired, keep the logging boundary focused on formatting and redaction.

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/docs/tutorials/app-log-and-production-logging.md.
Use overlays/mobile-flutter/skills/architecture/flutter-production-logging/SKILL.md.

Task:
Add production logging to the Flutter app.

Deliver:
1. logger boundary plan
2. exact files to update
3. integration points
4. verification checklist
```

## Thai

ดู `app-log-and-production-logging_TH.md` สำหรับเวอร์ชันภาษาไทย
