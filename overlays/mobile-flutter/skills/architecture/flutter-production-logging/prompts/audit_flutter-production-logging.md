Audit the consuming Flutter repository for `flutter-production-logging` readiness.

Check:
- architecture boundaries
- widget or presentation leakage
- structured context and typed contracts
- redaction and fallback behavior
- crash reporting or analytics handoff
- consistency between implementation and documentation

Fail when:
- widgets directly own logging orchestration
- raw vendor logging types leak into domain or app-facing contracts
- referenced docs or files are missing
- logging ownership overlaps unclearly with companion skills
