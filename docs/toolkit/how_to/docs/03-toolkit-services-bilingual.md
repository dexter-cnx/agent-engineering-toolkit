---
title: Toolkit for Services — Bilingual
tags:
  - toolkit
  - backend
  - services
  - ci
  - architecture
  - localization
---

# Toolkit for Services — ไทย + English

> [!summary]
> Services projects usually use `toolkit-arch` and `toolkit-ci` most heavily. `toolkit-i18n` applies when services manage localized content, templates, or message catalogs.
>
> โปรเจกต์ services มักใช้ `toolkit-arch` กับ `toolkit-ci` หนักที่สุด ส่วน `toolkit-i18n` จะมีประโยชน์เมื่อ service ดูแล localized content, templates หรือ message catalogs

## English

### Main principles
- Keep module boundaries clear
- Enforce CI debugging with exported artifacts
- Use i18n validation if the service owns user-facing messages
- Keep structure and provider integrations testable

### Step-by-step workflow

#### 1) Validate service structure
```bash
toolkit-arch doctor --json
toolkit-arch scan --target services/my_service --json
toolkit-arch violations --target services/my_service --json --limit 20
toolkit-arch export --target services/my_service --output artifacts/service-arch-report.json --json
```

#### 2) Debug service CI
```bash
toolkit-ci doctor --json
toolkit-ci auth status --json
toolkit-ci runs list --branch main --limit 10 --json
toolkit-ci runs read 12345 --json
toolkit-ci logs download 12345 --output artifacts/service-logs --json
toolkit-ci debug 12345 --output artifacts/service-debug --json
```

#### 3) Validate localized catalogs if needed
```bash
toolkit-i18n doctor --json
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/service-i18n
```

### Example Codex prompt
```text
Use toolkit-arch and toolkit-ci for this service first.
If the service owns localized templates or message catalogs, also use toolkit-i18n.
Export useful reports and summarize only the highest-signal findings.
```

## ไทย

### หลักการสำคัญ
- คุม boundary ของ module ให้ชัด
- debug CI ผ่านไฟล์ artifact
- ใช้ i18n validation ถ้า service ถือข้อความที่ผู้ใช้เห็น
- ทำให้โครงสร้างและการเชื่อม provider ตรวจสอบได้

### workflow แบบเป็นขั้นตอน

#### 1) ตรวจโครงสร้าง service
```bash
toolkit-arch doctor --json
toolkit-arch scan --target services/my_service --json
toolkit-arch violations --target services/my_service --json --limit 20
toolkit-arch export --target services/my_service --output artifacts/service-arch-report.json --json
```

#### 2) debug CI ของ service
```bash
toolkit-ci doctor --json
toolkit-ci auth status --json
toolkit-ci runs list --branch main --limit 10 --json
toolkit-ci runs read 12345 --json
toolkit-ci logs download 12345 --output artifacts/service-logs --json
toolkit-ci debug 12345 --output artifacts/service-debug --json
```

#### 3) ตรวจ localized catalogs ถ้ามี
```bash
toolkit-i18n doctor --json
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/service-i18n
```

### ตัวอย่าง prompt สำหรับ Codex
```text
Use toolkit-arch and toolkit-ci for this service first.
If the service owns localized templates or message catalogs, also use toolkit-i18n.
Export useful reports and summarize only the highest-signal findings.
```
