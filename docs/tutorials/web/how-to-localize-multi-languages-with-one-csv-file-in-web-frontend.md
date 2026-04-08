---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - localization
aliases:
  - Web CSV Localization
  - Multi Language CSV in Web Frontend
---

# วิธีทำ localization หลายภาษาใน web-frontend ด้วย CSV ไฟล์เดียว

ใช้ tutorial นี้เมื่อ web frontend ต้องใช้ CSV ไฟล์เดียวเป็น source of truth สำหรับหลายภาษา

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Web Frontend
**Architecture:** CSV-first Localization
**Localization:** CSV-first
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- <framework>
- <state solution>
- <routing solution>
- CSV localization builder or loader

## 3. Architecture Rules

- CSV is the source of truth
- keep localization setup in the app/bootstrap layer
- do not hardcode translated strings in components

## 4. Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify key coverage and fallback behavior
5. Update project memory after durable decisions
```

## ตัวอย่าง prompt เริ่มงาน

```text
Follow AGENTS.md strictly.
Start from a blank folder.
Create a short, practical repo-root AGENTS.md.
Choose the web-frontend overlay.
Use a CSV localization workflow.
Use the prompt pipeline in order and verify translation coverage.
```

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์โปรเจกต์
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md`
5. เลือก `web-frontend` overlay
6. ตัดสินใจว่าจะ generate locale assets จาก CSV อย่างไร
7. สร้างโครงเว็บและโฟลเดอร์ localization
8. สร้าง script สำหรับ generate หรือ validate translation files
9. verify key coverage และ fallback behavior
10. บันทึก memory เรื่อง naming และ fallback

ตัวอย่าง bootstrap:

```bash
mkdir web-csv-localization
cd web-csv-localization
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory src/i18n tool
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
```

## โครง CSV ที่แนะนำ

เก็บไฟล์เดียวไว้เป็น source of truth เช่น:

```text
key,en,th,ja
nav.home,Home,หน้าหลัก,ホーム
cta.save,Save,บันทึก,保存
```

กติกาที่ควรยึด:

- `key` ต้อง stable และสื่อความหมาย
- แต่ละคอลัมน์คือ locale หนึ่งตัว
- generated files เป็นผลลัพธ์ ไม่ใช่ source of truth
- CSV ต้องเป็น shared contract ของทีม

## prompts ที่ควรใช้

| Stage | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| Plan | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| Architecture | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` + `skills/dependency-review/README.md` | localization boundary, file placement, package choice |
| Implement | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | CSV, generator, generated assets |
| Review | `prompts/review/review_change.md` | `skills/docs-update/README.md` | string coverage และ boundary clarity |
| Verify | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | key coverage, fallback checks, evidence |
| Finalize | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| Memory | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable localization rules |

## skills ที่ควรอ่าน

- `skills/skill-router/README.md`
- `skills/risk-scoring/README.md`
- `skills/architecture-review/README.md`
- `skills/dependency-review/README.md`
- `skills/safe-refactor/README.md`
- `skills/docs-update/README.md`
- `skills/verification-pass/README.md`

## scripts ที่ควรมีใน consuming repo

ไม่มี script กลางของ toolkit สำหรับงานนี้ ให้สร้าง command ใน repo ปลายทางเอง เช่น:

```bash
npm run i18n:build
npm run lint
npm run build
```

ถ้าใช้ตัวช่วยตรวจ CSV ให้เพิ่ม command เช่น:

```bash
npm run i18n:validate
```

## โครง web-frontend ที่แนะนำ

แยก responsibility ให้ชัด:

- CSV source
- generator script
- generated locale assets
- runtime localization loader
- fallback language handling

## pitfall

- ให้ generated file กลายเป็น source of truth
- ปล่อยให้ key drift ระหว่างภาษา
- hardcode string ลงใน component โดยไม่ผ่าน localization layer
- ไม่ทดสอบ fallback language

## การ verify

- ตรวจว่า CSV มี key ครบทุกภาษา
- ตรวจว่า generate แล้วไม่มี key หาย
- รัน `npm run lint`
- รัน `npm run build`
- รัน command validate CSV ถ้ามี

## memory notes

เก็บ decision ถาวรเกี่ยวกับ:

- โครง CSV
- naming convention ของ key
- fallback language
- script ที่ใช้ generate หรือ validate
