# 📘 toolkit-i18n — How to Use

> A practical guide for using `toolkit-i18n` with Codex and manually

---

# 🇺🇸 English

## 🧠 What is toolkit-i18n?

`toolkit-i18n` is a repository CLI designed for:

- validating localization CSV files
- detecting translation issues
- generating JSON files per language
- supporting agent-friendly workflows (Codex / Claude Code)

It follows a **read-first, safe-by-default** pattern:

```text
doctor → validate → diff → generate → (optional write)
```

---

## 📂 Expected Input

CSV file example:

```csv
key,en,th,ja
app.title,Hello,สวัสดี,こんにちは
home.welcome,Welcome,,ようこそ
```

Requirements:
- must have `key` column
- language columns (en, th, etc.)
- supports dotted keys for nested JSON

---

## ⚙️ Basic Commands

### 1. Check environment
```bash
toolkit-i18n doctor
```

### 2. Validate CSV
```bash
toolkit-i18n validate assets/i18n/translations.csv --json
```

Detects:
- duplicate keys
- missing values
- malformed rows

### 3. Show differences (optional)
```bash
toolkit-i18n diff assets/i18n/translations.csv --json
```

### 4. Generate JSON files
```bash
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/i18n/
```

Output:
```text
artifacts/i18n/en.json
artifacts/i18n/th.json
artifacts/i18n/ja.json
```

---

## 🤖 Using with Codex (Recommended)

### Standard prompt

```text
Read tools/toolkit-i18n/prompts/use_toolkit_i18n.md and run it for assets/i18n/translations.csv -> artifacts/i18n.
Only report duplicate keys, missing values, malformed rows, and generated file paths.
```

### Short version

```text
Run toolkit-i18n for assets/i18n/translations.csv -> artifacts/i18n.
Report only key issues and output paths.
```

### Ultra short (after convention is learned)

```text
Run toolkit-i18n default flow.
```

---

## 🔁 Typical Workflow

```text
1. doctor
2. validate
3. diff (optional)
4. generate
5. inspect output files
```

---

## ⚠️ Safety Rules

- No automatic overwrite of CSV
- No hidden mutations
- Output goes to `artifacts/`
- Safe to run multiple times

---

## 📁 Example Output

```json
{
  "issues": {
    "duplicate_keys": ["home.title"],
    "missing_values": [
      {"key": "home.welcome", "lang": "th"}
    ]
  },
  "generated_files": [
    "artifacts/i18n/en.json",
    "artifacts/i18n/th.json"
  ]
}
```

---

## 🧩 Best Practices

- Keep CSV as **single source of truth**
- Always run `validate` before `generate`
- Use `--output` instead of writing directly
- Let Codex handle workflow using CLI, not ad hoc scripts

---

# 🇹🇭 ภาษาไทย

## 🧠 toolkit-i18n คืออะไร?

`toolkit-i18n` คือ CLI สำหรับ:

- ตรวจสอบไฟล์แปล (CSV)
- หา error เช่น key ซ้ำ / ค่า missing
- generate JSON แยกตามภาษา
- ใช้งานร่วมกับ AI agent เช่น Codex

ใช้ pattern:

```text
doctor → validate → diff → generate → (write)
```

---

## 📂 รูปแบบไฟล์ input

ตัวอย่าง CSV:

```csv
key,en,th,ja
app.title,Hello,สวัสดี,こんにちは
home.welcome,Welcome,,ようこそ
```

ข้อกำหนด:
- ต้องมี column `key`
- มี column ภาษา (en, th, ...)
- รองรับ key แบบ dot (nested JSON)

---

## ⚙️ คำสั่งพื้นฐาน

### 1. เช็คระบบ
```bash
toolkit-i18n doctor
```

### 2. ตรวจไฟล์แปล
```bash
toolkit-i18n validate assets/i18n/translations.csv --json
```

ตรวจ:
- key ซ้ำ
- ค่า missing
- row ผิด format

### 3. ดู diff (optional)
```bash
toolkit-i18n diff assets/i18n/translations.csv --json
```

### 4. generate JSON
```bash
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/i18n/
```

ผลลัพธ์:
```text
artifacts/i18n/en.json
artifacts/i18n/th.json
artifacts/i18n/ja.json
```

---

## 🤖 ใช้กับ Codex

### แบบมาตรฐาน
```text
Read tools/toolkit-i18n/prompts/use_toolkit_i18n.md and run it for assets/i18n/translations.csv -> artifacts/i18n.
Only report duplicate keys, missing values, malformed rows, and generated file paths.
```

### แบบสั้น
```text
Run toolkit-i18n for assets/i18n/translations.csv -> artifacts/i18n.
Report only key issues and output paths.
```

### แบบสั้นมาก (ต้องมี context แล้ว)
```text
Run toolkit-i18n default flow.
```

---

## 🔁 workflow ที่แนะนำ

```text
1. doctor
2. validate
3. diff
4. generate
5. ตรวจ output
```

---

## ⚠️ ความปลอดภัย

- ไม่ overwrite CSV อัตโนมัติ
- ไม่มี side-effect แอบแฝง
- เขียน output ไปที่ `artifacts/`
- รันซ้ำได้ปลอดภัย

---

## 📁 ตัวอย่าง output

```json
{
  "duplicate_keys": ["home.title"],
  "missing_values": [
    {"key": "home.welcome", "lang": "th"}
  ],
  "generated_files": [
    "artifacts/i18n/en.json",
    "artifacts/i18n/th.json"
  ]
}
```

---

## 🧩 Best Practice

- ใช้ CSV เป็น source of truth
- validate ก่อน generate เสมอ
- ใช้ output directory แยก
- ให้ Codex ใช้ CLI แทน script

---

# ✅ Summary

**toolkit-i18n** is:
- predictable
- safe
- reusable
- agent-friendly

เหมาะกับ:
- Flutter apps
- localization pipelines
- AI-assisted workflows
