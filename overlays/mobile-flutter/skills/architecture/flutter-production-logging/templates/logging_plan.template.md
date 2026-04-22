# flutter-production-logging Plan Template

## Goal

Describe the production logging boundary that the Flutter app needs.

## Scope

- Logger interface
- Structured context model
- Formatter and redaction rules
- Bootstrap wiring
- Crash reporting or analytics adapters

## Proposed files

- `lib/core/logging/app_logger.dart`
- `lib/core/logging/log_context.dart`
- `lib/core/logging/log_formatter.dart`
- `lib/app/bootstrap/app_bootstrap.dart`
- `test/core/logging/app_logger_test.dart`

## Implementation notes

- Keep widgets free of logging plugin calls.
- Keep secrets redacted before logs leave the boundary.
- Keep release verbosity lower than debug verbosity.
- Keep crash reporting integration behind an adapter.

## Verification

- Targeted logging tests pass
- `flutter analyze` stays clean
- No direct vendor logging SDK imports appear in widgets
