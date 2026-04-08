---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - getx
  - clean-architecture
aliases:
  - Flutter Clean Architecture GetX
  - Flutter App with GetX
---

# วิธีทำ Flutter app แบบ clean architecture + GetX

ใช้ tutorial นี้เมื่อคุณอยากสร้าง Flutter app ที่ใช้ clean architecture และ GetX เป็น state management / DI / routing helper

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์ใหม่
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md`
5. เลือก `mobile-flutter` overlay
6. ติดตั้ง `get`
7. วางโครง clean architecture ให้ชัด
8. ใช้ GetX เฉพาะในชั้น app/presentation
9. verify ด้วย Flutter checks
10. บันทึก memory เรื่อง controller และ route boundary

ตัวอย่าง bootstrap:

```bash
mkdir flutter-clean-getx
cd flutter-clean-getx
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add get
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
**Architecture:** Clean Architecture + GetX
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- get
- go_router or GetX routing
- <test command>

## 3. Architecture Rules

- `presentation/` = UI + controller
- `domain/` = entities, use cases, repository contracts
- `data/` = models, repository implementations, datasources
- keep controllers thin and readable

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
Use the prompt pipeline in order.
Keep GetX controllers thin and keep clean architecture boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | boundary และ dependency direction |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Flutter layers และ GetX controllers |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | controller ต้องไม่กลายเป็น god object |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | analysis/test evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable GetX rules |

## โครงที่แนะนำ

```text
lib/
  app/
  presentation/
  domain/
  data/
  core/
```

แนวทางใช้งาน GetX:

- `presentation` เก็บ widgets และ controllers
- `app` เก็บ routing, bindings, และ app bootstrap
- `domain` เก็บ entities, use cases และ business rules
- `data` เก็บ repository implementation และ data source

## การใช้งาน GetX

- ใช้ `GetMaterialApp` และ bindings เพื่อจัดการ dependency เฉพาะที่จำเป็น
- อย่าใช้ controller เป็นที่รวม business logic ทุกอย่าง
- ให้ routing และ DI อยู่ในชั้น app/presentation เท่านั้น

ตัวอย่าง package:

```bash
flutter pub add get
```

## การ verify

```bash
flutter analyze
flutter test
```

ถ้ามี widget test หรือ integration test ให้เพิ่มเข้าไป

## pitfall

- controller หนาเกินไป
- ให้ GetX กลายเป็น architecture เอง
- ใช้ global state เพื่อข้าม boundary
- ปล่อยให้ routing ผสมกับ domain logic

## memory notes

เก็บ decision ถาวรเกี่ยวกับ:

- รูปแบบ controller และ binding
- boundary ระหว่าง presentation กับ domain
- test strategy สำหรับ GetX
- convention เรื่อง route ownership
