---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - offline-first
aliases:
  - Offline First Flutter Tutorial
  - Flutter Offline App
---

# วิธีทำ Flutter app แบบ offline-first

ใช้ tutorial นี้เมื่อแอปต้องทำงานได้แม้ไม่มี network และค่อย sync ทีหลัง

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์และ initialize git
2. เพิ่ม toolkit และ project memory
3. เพิ่ม `AGENTS.md`
4. เลือก `mobile-flutter` overlay
5. ตัดสินใจเรื่อง offline data strategy ก่อนเขียนโค้ด
6. สร้าง app shell และ local storage boundary
7. ติดตั้ง `isar` เป็นตัวอย่าง local database
8. ค่อยเพิ่มกติกาเรื่อง sync หรือ queue หลังจาก boundary ชัดแล้ว
9. verify ทั้งกรณีปกติและกรณี offline
10. บันทึก memory สำหรับเรื่อง sync และ conflict

ตัวอย่าง bootstrap:

```bash
mkdir flutter-offline-first-app
cd flutter-offline-first-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add isar isar_flutter_libs
```

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Mobile Flutter overlay README](../../../overlays/mobile-flutter/README.md)
- [Mobile Flutter overlay rules](../../../overlays/mobile-flutter/AGENTS.overlay.md)
- [Mobile Flutter worked example](../../../overlays/mobile-flutter/examples/worked_example.md)

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Flutter App
**Architecture:** Offline-First / Clean Architecture
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- isar
- <state management>
- <routing>
- <offline storage>

## 3. Architecture Rules

- UI stays thin
- offline data flow is explicit
- keep repository boundary clean

## 4. Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify before finalizing
5. Update project memory after durable decisions
```

## ตัวอย่าง prompt เริ่มงาน

```text
Follow AGENTS.md strictly.
Start from a blank folder.
Create a short, practical repo-root AGENTS.md.
Choose the mobile-flutter overlay.
Use Isar as the local database and keep it behind a repository or storage adapter.
Use the prompt pipeline in order.
Keep offline-first data flow and widget boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay ที่เลือก |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | offline assumptions, risks, constraints |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | local storage, sync boundary, conflict policy |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | app shell, cache, sync adapter, queue boundary |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | leakage checks และ boundary review |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | offline evidence, remaining uncertainty |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable offline rules |

## โครง offline-first ที่ควรมี

ให้แยกความรับผิดชอบให้ชัด:

- presentation
- domain/use cases
- local persistence หรือ cache
- sync adapter หรือ queue processor

ตัวอย่าง `isar` ที่ใช้ในชั้น data/storage:

```dart
final isar = await Isar.open(
  [MyEntitySchema],
  directory: '/path/to/app/data',
);
```

ให้ใช้ `isar` เป็น local source of truth หรือ cache layer แล้วค่อยให้ sync logic วิ่งแยกออกจาก widget

คำถามที่ควรถามไว้ก่อน:

- อะไรคือ source of truth ตอน offline
- ถ้า sync ชนกันจะทำอย่างไร
- อนุญาตให้ retry แบบไหน
- action ไหนควรถูก queue ไว้ทีหลัง

## การ verify

ใช้ Flutter checks ร่วมกับ offline smoke test ถ้าเป็นไปได้:

```bash
flutter analyze
flutter test
```

ถ้าแอปมี sync behavior ให้เพิ่มการทดสอบตอนตัด network หรือเข้า airplane mode ด้วย

## pitfall

- สมมติว่ามี network ตลอดเวลา
- ซ่อน sync logic ไว้ใน widgets
- ปล่อยให้ conflict policy ไม่ชัด
- เรียก API ตรงจาก presentation code

## memory notes

เก็บ decision ที่ควรจำถาวร เช่น:

- offline source of truth
- sync rules
- conflict handling
- queue และ retry behavior
