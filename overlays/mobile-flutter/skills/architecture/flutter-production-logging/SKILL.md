# flutter-production-logging

## Purpose
Design a production logging boundary for Flutter apps with structured logs, redaction, environment-aware verbosity, and clean handoff to crash reporting or analytics.

## Use when
- The app needs structured logs for debugging or support
- Log calls should stay out of widgets and presentation state
- Logging must coordinate with crash reporting, analytics, or network diagnostics
- The repo needs a reusable app-level logging strategy that fits clean architecture

## Do NOT use when
- You only need one-off `print()` statements during a prototype
- You are changing UI copy or visual design only
- The task is purely backend logging without a Flutter client boundary
- Logging should be embedded directly in widgets or view models

## Inputs required
- Log event types and severity levels
- Redaction rules for secrets and personal data
- Sink destinations such as console, file, remote collector, or crash reporter
- Crash reporting or analytics integration requirements
- Environment and verbosity rules for debug, profile, and release

## Constraints
- Keep the logging boundary in `core/` or another app infrastructure layer
- Keep widget trees free of direct logger or plugin calls
- Keep redaction and formatting deterministic and testable
- Do not log secrets, tokens, or raw personal data
- Keep crash reporting adapter calls behind a boundary instead of inline in UI code

## Step-by-step workflow
1. Identify the sources of logs and the sink destinations that the app needs.
2. Define the logger interface, log context model, formatter, and redaction policy.
3. Implement the app-level logger and wire it at bootstrap in the infrastructure layer.
4. Connect crash reporting or analytics adapters without leaking plugin types upward.
5. Add tests for filtering, redaction, and failure handling.
6. Verify the app builds cleanly and the logging boundary stays out of widgets.

## Output contract
- `lib/core/logging/app_logger.dart` or an equivalent logger interface
- `lib/core/logging/log_context.dart` or an equivalent context model
- `lib/core/logging/log_formatter.dart` or an equivalent formatter helper
- `lib/app/bootstrap/app_bootstrap.dart` or an equivalent wiring entrypoint
- `test/core/logging/app_logger_test.dart` or equivalent boundary tests

## Validation checklist
- The app layer depends on the logger interface, not on vendor SDK types
- Sensitive values are redacted before they leave the boundary
- Release verbosity is lower than debug verbosity
- Crash reporting and analytics integrations are optional adapters, not hard dependencies in widgets
- Targeted tests cover formatting, redaction, and fallback behavior

## Related skills
- `flutter-crash-reporting`
- `flutter-analytics`
- `flutter-network-dio`
- `flutter-clean-architecture-audit`

## References
- [`examples/logging_example.md`](examples/logging_example.md)
- [`templates/logging_plan.template.md`](templates/logging_plan.template.md)
- [`checklists/README.md`](checklists/README.md)
- [`../../../templates/project-bootstrap-template.md`](../../../templates/project-bootstrap-template.md)
- [`../../flutter-crash-reporting/SKILL.md`](../../flutter-crash-reporting/SKILL.md)

## Real example
An app stores logging behavior in `lib/core/logging/app_logger.dart`, builds structured context in `lib/core/logging/log_context.dart`, wires the logger from `lib/app/bootstrap/app_bootstrap.dart`, and verifies redaction with `test/core/logging/app_logger_test.dart`.

## Real file output sample
```text
lib/core/logging/app_logger.dart
lib/core/logging/log_context.dart
lib/core/logging/log_formatter.dart
lib/app/bootstrap/app_bootstrap.dart
test/core/logging/app_logger_test.dart
```
