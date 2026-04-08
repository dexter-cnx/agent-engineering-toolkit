---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - riverpod
  - clean-architecture
aliases:
  - Flutter Clean Architecture Riverpod
  - Flutter App with Riverpod
---

# วิธีทำ Flutter app แบบ clean architecture + Riverpod

ใช้ tutorial นี้เมื่อคุณอยากสร้าง Flutter app ที่ใช้ clean architecture และ Riverpod เป็น state management

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์ใหม่
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md`
5. เลือก `mobile-flutter` overlay
6. ติดตั้ง `flutter_riverpod`
7. วางโครง clean architecture ให้ชัด
8. ใช้ Riverpod เฉพาะในชั้น presentation/app
9. verify ด้วย Flutter checks
10. บันทึก memory เรื่อง state และ boundary

ตัวอย่าง bootstrap:

```bash
mkdir flutter-clean-riverpod
cd flutter-clean-riverpod
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add flutter_riverpod
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
**Architecture:** Clean Architecture + Riverpod
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- Riverpod
- go_router
- <test command>

## 3. Architecture Rules

- `presentation/` = UI + state
- `domain/` = entities, use cases, repository contracts
- `data/` = models, repository implementations, datasources
- keep providers thin and readable

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
Keep Riverpod providers thin and keep clean architecture boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | boundary และ dependency direction |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Flutter layers และ Riverpod providers |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | provider ต้องไม่แบกรับ business logic เกินไป |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | analysis/test evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable Riverpod rules |

## โครงที่แนะนำ

```text
lib/
  app/
  presentation/
  domain/
  data/
  core/
```

แนวทางใช้งาน Riverpod:

- `presentation` เป็นที่อยู่ของ widgets, providers, และ view state
- `domain` เก็บ entities, value objects, และ use cases
- `data` เก็บ repository implementation และ data source
- `app` เก็บ app bootstrap, router, และ provider scope

## การใช้งาน Riverpod

- เริ่มจาก `Provider`, `StateProvider`, หรือ `NotifierProvider` ตามความเหมาะสม
- อย่าให้ provider กลายเป็นที่รวม business rule ทั้งหมด
- domain use case ควรถูกเรียกจาก presentation layer ผ่าน provider หรือ controller ที่บาง

ตัวอย่าง package:

```bash
flutter pub add flutter_riverpod
```

ถ้าทีมใช้ code generation ค่อยเพิ่มในภายหลัง:

```bash
flutter pub add riverpod_annotation
flutter pub add --dev build_runner riverpod_generator
```

## การ verify

```bash
flutter analyze
flutter test
```

ถ้ามี widget test หรือ provider test ให้เพิ่มเข้าไป

## pitfall

- เอา business logic ไปไว้ใน provider จนแทน domain layer
- ให้ widget รู้เรื่อง data source โดยตรง
- ใช้ provider เป็น repository
- ปล่อยให้ layer boundary หายไป

## memory notes

เก็บ decision ถาวรเกี่ยวกับ:

- รูปแบบ provider ที่ทีมใช้
- boundary ระหว่าง presentation กับ domain
- test strategy สำหรับ provider
- convention เรื่อง state ownership
