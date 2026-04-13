# flutter-deep-link Example

## Example scenario

A Flutter application needs `flutter-deep-link` support while preserving clean boundaries between presentation, application, data, and integration layers.

## Example review questions

- Which layer owns orchestration?
- Which layer talks to the provider or plugin?
- Which typed models cross boundaries?
- What happens on failure, denial, timeout, or unsupported devices?
- Which companion skills are required?

## Example outcome

A good implementation keeps `flutter-deep-link` isolated as a capability, composes with companion skills only where needed, and documents verification instead of assuming success.
