Audit the consuming Flutter repository for `flutter-biometric-auth` readiness.

Check:
- architecture boundaries
- provider or plugin leakage
- typed contracts
- fallback and failure states
- platform-specific notes
- consistency between implementation and documentation

Fail when:
- widgets directly own capability orchestration
- raw SDK types leak into domain or app-facing contracts
- referenced docs or files are missing
- capability ownership overlaps unclearly with companion skills
