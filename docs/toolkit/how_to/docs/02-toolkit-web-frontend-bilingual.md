---
title: Toolkit for Web Frontend — Bilingual
tags:
  - toolkit
  - web
  - frontend
  - design-tokens
  - i18n
  - ci
---

# Toolkit for Web Frontend — ไทย + English

> [!summary]
> Web frontend projects usually benefit most from `toolkit-design`, `toolkit-i18n`, and `toolkit-ci`, with `toolkit-arch` enforcing project structure.
>
> โปรเจกต์ web-frontend มักได้ประโยชน์มากจาก `toolkit-design`, `toolkit-i18n`, และ `toolkit-ci` โดยใช้ `toolkit-arch` คุมโครงสร้าง

## English

### Main principles
- Keep design token sync deterministic
- Keep localization files validated before build
- Keep component and feature structure predictable
- Use CI artifacts instead of pasting long logs

### Step-by-step workflow

#### 1) Validate structure
```bash
toolkit-arch doctor --json
toolkit-arch scan --target apps/web_frontend --json
toolkit-arch violations --target apps/web_frontend --json --limit 20
toolkit-arch export --target apps/web_frontend --output artifacts/web-arch-report.json --json
```

#### 2) Validate and export design tokens
```bash
toolkit-design doctor --json
toolkit-design validate tokens/design-tokens.json --json
toolkit-design map tokens/design-tokens.json --json
toolkit-design export tokens/design-tokens.json --output artifacts/web-design --json
```

#### 3) Validate and generate translations
```bash
toolkit-i18n doctor --json
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/web-i18n
```

#### 4) Debug frontend CI
```bash
toolkit-ci doctor --json
toolkit-ci auth status --json
toolkit-ci runs list --branch main --limit 10 --json
toolkit-ci logs download 12345 --output artifacts/web-logs --json
toolkit-ci debug 12345 --output artifacts/web-debug --json
```

### Example Codex prompt
```text
Use toolkit-arch, toolkit-design, toolkit-i18n, and toolkit-ci for this web frontend.
Validate structure, tokens, and translations, then report only top issues and exported paths.
```

## ไทย

### หลักการสำคัญ
- ทำให้ design token sync เดาได้
- validate localization ก่อน build
- คุมโครงสร้าง component/feature ให้คงที่
- ใช้ไฟล์ artifact แทนการแปะ log ยาว ๆ

### workflow แบบเป็นขั้นตอน

#### 1) ตรวจโครงสร้าง
```bash
toolkit-arch doctor --json
toolkit-arch scan --target apps/web_frontend --json
toolkit-arch violations --target apps/web_frontend --json --limit 20
toolkit-arch export --target apps/web_frontend --output artifacts/web-arch-report.json --json
```

#### 2) ตรวจและ export design tokens
```bash
toolkit-design doctor --json
toolkit-design validate tokens/design-tokens.json --json
toolkit-design map tokens/design-tokens.json --json
toolkit-design export tokens/design-tokens.json --output artifacts/web-design --json
```

#### 3) ตรวจและ generate translations
```bash
toolkit-i18n doctor --json
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/web-i18n
```

#### 4) debug CI ของ frontend
```bash
toolkit-ci doctor --json
toolkit-ci auth status --json
toolkit-ci runs list --branch main --limit 10 --json
toolkit-ci logs download 12345 --output artifacts/web-logs --json
toolkit-ci debug 12345 --output artifacts/web-debug --json
```

### ตัวอย่าง prompt สำหรับ Codex
```text
Use toolkit-arch, toolkit-design, toolkit-i18n, and toolkit-ci for this web frontend.
Validate structure, tokens, and translations, then report only top issues and exported paths.
```
