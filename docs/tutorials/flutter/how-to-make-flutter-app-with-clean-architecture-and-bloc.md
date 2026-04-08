---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - bloc
  - clean-architecture
aliases:
  - Flutter Clean Architecture Bloc
  - Flutter App with BLoC
---

# วิธีทำ Flutter app แบบ clean architecture + BLoC

ใช้ tutorial นี้เมื่อคุณอยากสร้าง Flutter app ที่ใช้ clean architecture และ BLoC เป็น state management

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์ใหม่
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md`
5. เลือก `mobile-flutter` overlay
6. ติดตั้ง `flutter_bloc` และ `bloc`
7. วางโครง clean architecture ให้ชัด
8. ใช้ BLoC เฉพาะในชั้น presentation/feature
9. verify ด้วย Flutter checks
10. บันทึก memory เรื่อง event/state flow

ตัวอย่าง bootstrap:

```bash
mkdir flutter-clean-bloc
cd flutter-clean-bloc
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add flutter_bloc bloc
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
**Architecture:** Clean Architecture + BLoC
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- flutter_bloc
- go_router
- <test command>

## 3. Architecture Rules

- `presentation/` = UI + bloc/cubit
- `domain/` = entities, use cases, repository contracts
- `data/` = models, repository implementations, datasources
- keep events and states thin and readable

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
Keep BLoC events and states thin and keep clean architecture boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | boundary และ dependency direction |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Flutter layers และ BLoC classes |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | bloc ต้องไม่รับภาระเกินไป |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | analysis/test evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable BLoC rules |

## โครงที่แนะนำ

```text
lib/
  app/
  presentation/
  domain/
  data/
  core/
```

แนวทางใช้งาน BLoC:

- `presentation` เป็นที่อยู่ของ widgets และ blocs/cubits
- `domain` เก็บ entities, use cases และ business rules
- `data` เก็บ repository implementation และ data source
- `app` เก็บ app bootstrap, route, และ DI wiring

## การใช้งาน BLoC

- ใช้ `Event` และ `State` เพื่อทำให้ flow ชัด
- อย่าให้ bloc กลายเป็น repository
- ให้ widget ส่ง event และ render state อย่างเดียว

ตัวอย่าง package:

```bash
flutter pub add flutter_bloc bloc
```

ถ้าทีมใช้ value equality ค่อยพิจารณา `equatable`

## การ verify

```bash
flutter analyze
flutter test
```

ถ้ามี bloc test หรือ widget test ให้เพิ่มเข้าไป

## pitfall

- bloc หนาเกินไป
- event/state กลายเป็นที่รวม business logic ทั้งหมด
- widget รู้เรื่อง data source โดยตรง
- ใช้ bloc แทน domain layer

## memory notes

เก็บ decision ถาวรเกี่ยวกับ:

- รูปแบบ event/state ของทีม
- boundary ระหว่าง presentation กับ domain
- test strategy สำหรับ bloc
- convention เรื่อง state ownership
