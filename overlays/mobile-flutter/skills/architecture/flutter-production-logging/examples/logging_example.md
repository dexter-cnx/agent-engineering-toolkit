# flutter-production-logging Example

## Example scenario

A Flutter app needs production-safe logging that can capture support signals without leaking tokens or UI-layer details.

## Example outcome

- `lib/core/logging/app_logger.dart` owns the app logger interface.
- `lib/core/logging/log_context.dart` stores structured fields such as screen, feature, request id, and session id.
- `lib/core/logging/log_formatter.dart` renders a stable text or JSON output for the selected sink.
- `lib/app/bootstrap/app_bootstrap.dart` wires the logger once at startup.
- `test/core/logging/app_logger_test.dart` verifies redaction and fallback behavior.

## Example review questions

- Which layer owns the logger contract?
- Which adapter talks to a crash reporter or analytics sink?
- Which fields are safe to log in release builds?
- What happens if the logging sink throws?
- How does the app redact secrets before emission?
