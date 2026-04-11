---
title: Toolkit Overview — Bilingual
tags:
  - toolkit
  - architecture
  - ci
  - design
  - i18n
---

# Toolkit Overview — ไทย + English

> [!summary]
> This guide explains the toolkit system, its principles, and how to use it step by step across different project types.
>
> เอกสารนี้อธิบายระบบ toolkit, หลักการใช้งาน, และวิธีใช้แบบเป็นขั้นตอนสำหรับหลายประเภทโปรเจกต์

## 1. What is the toolkit system? / toolkit system คืออะไร?

**English**

The toolkit system is a repository workflow built around reusable CLIs and docs so coding agents and developers follow the same path every time.

Core tools:
- `toolkit-arch` → validate structure and architecture boundaries
- `toolkit-ci` → inspect CI runs, download logs, summarize failures
- `toolkit-design` → validate design tokens and generate frontend-friendly outputs
- `toolkit-i18n` → validate translation CSV and generate localization files

**ไทย**

toolkit system คือ workflow ใน repo ที่สร้างจาก CLI ที่ใช้ซ้ำได้ + เอกสารกำกับ
เพื่อให้ทั้ง developer และ agent เดิน flow เดียวกันทุกครั้ง

เครื่องมือหลัก:
- `toolkit-arch` → ตรวจโครงสร้างและ boundary ของ architecture
- `toolkit-ci` → ตรวจ pipeline, ดึง log, สรุปจุดพัง
- `toolkit-design` → ตรวจ design tokens และ generate output สำหรับ frontend
- `toolkit-i18n` → ตรวจไฟล์แปลและ generate localization files

## 2. Core principles / หลักการหลัก

### English
1. CLI first
2. Read first, then mutate
3. Compact output
4. Structured workflow
5. Fail safely

### ไทย
1. CLI มาก่อน
2. อ่านก่อน ค่อยเปลี่ยน
3. output ต้องสั้น
4. workflow ต้องเดาได้
5. fail แบบปลอดภัย

## 3. Standard usage pattern / รูปแบบการใช้งานมาตรฐาน

```text
doctor → validate/scan → inspect → export → optional CI enforcement
```

## 4. Step-by-step general workflow / วิธีใช้แบบเป็นขั้นตอน

### Step 1 — Confirm the tool works / เช็กว่า tool ใช้งานได้
```bash
toolkit-arch doctor --json
toolkit-ci doctor --json
toolkit-design doctor --json
toolkit-i18n doctor --json
```

### Step 2 — Validate the domain-specific input / ตรวจ input ของแต่ละงาน
```bash
toolkit-arch scan --target . --json
toolkit-design validate tokens/design-tokens.json --json
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-ci auth status --json
```

### Step 3 — Export useful files / export ไฟล์ที่ใช้ต่อได้
```bash
toolkit-arch export --target . --output artifacts/arch-report.json --json
toolkit-ci logs download 12345 --output artifacts/logs --json
toolkit-design export tokens/design-tokens.json --output artifacts/design --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/i18n
```

### Step 4 — Let Codex or developers act / ให้ Codex หรือ developer ทำต่อ
- refactor structure
- fix CI failures
- sync design tokens
- fix translations
