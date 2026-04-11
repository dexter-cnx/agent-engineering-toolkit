# toolkit-arch — How to Use

## English
toolkit-arch validates layer boundaries, scans Flutter i18n usage, and supports CI failure on violations.

## ภาษาไทย
ใช้ `toolkit-arch` สำหรับ workflow นี้แบบทำซ้ำได้ใน repo.

### Localization workflow

1. `toolkit-arch i18n-usage --target <flutter-app> --output <used-keys.json>`
2. `toolkit-i18n keys diff --used-file <used-keys.json> --translations assets/i18n/translations.csv`
3. `toolkit-i18n coverage --used-file <used-keys.json> --translations assets/i18n/translations.csv`
4. `toolkit-arch i18n-layer-check --target <flutter-app>`
