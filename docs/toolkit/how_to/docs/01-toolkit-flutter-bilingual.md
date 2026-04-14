---
title: Toolkit for Flutter — Bilingual
tags:
  - toolkit
  - flutter
  - architecture
  - design-tokens
  - i18n
---

# Toolkit for Flutter — ไทย + English

> [!summary]
> Flutter projects benefit from all four tools together: structure, design, localization, and CI.
>
> โปรเจกต์ Flutter จะคุ้มที่สุดเมื่อใช้ทั้ง 4 ตัวร่วมกัน: โครงสร้าง, design, localization, และ CI

## English

### Main principles
- Keep Clean Architecture boundaries clear
- Generate design outputs into explicit folders
- Keep CSV as the localization source of truth
- Use CI checks before merge

### Step-by-step workflow

#### 1) Check architecture
```bash
toolkit-arch doctor --json
toolkit-arch scan --target apps/my_flutter_app --json
toolkit-arch violations --target apps/my_flutter_app --json --limit 20
toolkit-arch export --target apps/my_flutter_app --output artifacts/flutter-arch-report.json --json
```

#### 2) Sync design tokens
```bash
toolkit-design doctor --json
toolkit-design validate tokens/design-tokens.json --json
toolkit-design map tokens/design-tokens.json --json
toolkit-design export tokens/design-tokens.json --output artifacts/flutter-design --json
toolkit-design flutter-sync tokens/design-tokens.json --output lib/design/generated --json
```

#### 3) Validate and generate i18n
```bash
toolkit-i18n doctor --json
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n diff assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/i18n
```

#### 4) If CI fails
```bash
toolkit-ci doctor --json
toolkit-ci auth status --json
toolkit-ci runs list --branch develop --limit 10 --json
toolkit-ci runs read 12345 --json
toolkit-ci logs download 12345 --output artifacts/logs --json
toolkit-ci debug 12345 --output artifacts/debug --json
```

### Example Codex prompt
```text
Use toolkit-arch, toolkit-design, and toolkit-i18n for this Flutter app.
Scan architecture, validate tokens, validate translations, export reports, and summarize only the top issues and generated file paths.
```

## ไทย

### หลักการสำคัญ
- คุม Clean Architecture ให้ชัด
- generate design outputs ไปยังโฟลเดอร์ที่ตั้งใจไว้
- ใช้ CSV เป็น source of truth ของภาษา
- ใช้ CI checks ก่อน merge

### workflow แบบเป็นขั้นตอน

#### 1) ตรวจ architecture
```bash
toolkit-arch doctor --json
toolkit-arch scan --target apps/my_flutter_app --json
toolkit-arch violations --target apps/my_flutter_app --json --limit 20
toolkit-arch export --target apps/my_flutter_app --output artifacts/flutter-arch-report.json --json
```

#### 2) sync design tokens
```bash
toolkit-design doctor --json
toolkit-design validate tokens/design-tokens.json --json
toolkit-design map tokens/design-tokens.json --json
toolkit-design export tokens/design-tokens.json --output artifacts/flutter-design --json
toolkit-design flutter-sync tokens/design-tokens.json --output lib/design/generated --json
```

#### 3) ตรวจและ generate i18n
```bash
toolkit-i18n doctor --json
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n diff assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/i18n
```

#### 4) ถ้า CI พัง
```bash
toolkit-ci doctor --json
toolkit-ci auth status --json
toolkit-ci runs list --branch develop --limit 10 --json
toolkit-ci runs read 12345 --json
toolkit-ci logs download 12345 --output artifacts/logs --json
toolkit-ci debug 12345 --output artifacts/debug --json
```

### ตัวอย่าง prompt สำหรับ Codex
```text
Use toolkit-arch, toolkit-design, and toolkit-i18n for this Flutter app.
Scan architecture, validate tokens, validate translations, export reports, and summarize only the top issues and generated file paths.
```
