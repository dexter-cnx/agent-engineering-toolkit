---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - mobile
aliases:
  - Basic Flutter App Tutorial
  - Flutter App from Blank Folder
---

# วิธีทำ Flutter app แบบพื้นฐาน

ใช้ tutorial นี้เมื่อคุณอยากสร้าง Flutter app ทั่วไปโดยยังคง foundation boundary ให้ชัด

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์เปล่าสำหรับแอป
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md` ที่ root ของ repo
5. เลือก `mobile-flutter` overlay
6. สร้าง Flutter app shell
7. ใช้ lifecycle prompts ตามลำดับ
8. verify ด้วยคำสั่งของ Flutter
9. finalize และบันทึก memory

ตัวอย่าง bootstrap:

```bash
mkdir flutter-basic-app
cd flutter-basic-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
```

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Mobile Flutter overlay README](../../../overlays/mobile-flutter/README.md)
- [Mobile Flutter overlay rules](../../../overlays/mobile-flutter/AGENTS.overlay.md)
- [Mobile Flutter worked example](../../../overlays/mobile-flutter/examples/worked_example.md)
- [docs/tutorial.md](../../tutorial.md)

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Flutter App
**Architecture:** <chosen-architecture>
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- <state management>
- <routing>
- <test command>

## 3. Architecture Rules

- widgets stay focused on UI
- keep business logic out of widgets
- keep routing and state boundaries explicit

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
Keep widget, state, and routing boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path, overlay, bootstrap files |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | task restatement, facts, assumptions, risks |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | boundaries, structure, guardrails |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` ถ้าต้องจัดโครงเพิ่ม | Flutter files และ app structure |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | strengths, blocking issues, non-blocking issues |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | checks, evidence, uncertainty |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary, follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable notes |

## โครง Flutter ที่แนะนำ

ใช้โครงของ mobile overlay เป็นจุดเริ่ม:

```text
lib/
  presentation/
  domain/
  data/
  app/
  core/
```

ให้ boundary เหล่านี้ชัด:

- widgets ต้องโฟกัสที่ UI
- domain เก็บ business rules
- data เป็นเจ้าของ persistence หรือ API access
- navigation ต้องไม่ไปปะปนใน leaf widgets

## การ verify

รันคำสั่งที่ตรงกับ Flutter app นี้:

```bash
flutter analyze
flutter test
```

ถ้ามี startup หรือ device smoke test ก็ใส่เพิ่มตรงนี้

## pitfall

- ใส่ business logic ลงใน widgets
- เรียก API ตรงจาก presentation code
- ปล่อยให้ navigation กระจายไปอยู่ใน widgets ที่ไม่เกี่ยวกัน
- ใส่ assumption ของ Flutter กลับเข้าไปใน foundation docs

## memory notes

เก็บเฉพาะ note ที่มีอายุยืน เช่น:

- รูปแบบ boundary ของ widgets ที่ทีมใช้
- กติกาเรื่อง navigation
- convention ของ state management
- กติกาการทดสอบสำหรับ Flutter repo นี้
