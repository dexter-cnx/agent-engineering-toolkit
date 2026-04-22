# Project Bootstrap Template

```text
lib/
  app/
    router/
    theme/
    di/
    bootstrap/
  core/
    config/
    constants/
    errors/
    network/
    storage/
    utils/
    widgets/
  features/
  l10n/
main.dart
```

## Bootstrap checklist
- app entrypoint
- environment/config loading
- router setup
- theme setup
- localization setup
- global error boundary/logging
- app-level structured logging boundary ([`../skills/architecture/flutter-production-logging/SKILL.md`](../skills/architecture/flutter-production-logging/SKILL.md))
- network client
- storage abstraction
- sample feature
- tests wired into CI
