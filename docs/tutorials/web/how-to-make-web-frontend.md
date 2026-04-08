---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - frontend
aliases:
  - Web Frontend Tutorial
  - Frontend from Blank Folder
---

# วิธีทำ web-frontend

ใช้ tutorial นี้สำหรับเว็บ UI, admin dashboard หรือ product frontend

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์และ initialize git
2. เพิ่ม toolkit และ project memory
3. เพิ่ม `AGENTS.md`
4. เลือก `web-frontend` overlay
5. initialize เว็บแอปด้วย starter ที่ทีมใช้อยู่
6. แยก page orchestration ออกจาก reusable components
7. อย่าให้ data access และ state flow ไปปนใน presentation primitives
8. verify ด้วย lint และ build checks
9. บันทึก memory สำหรับกติกาเรื่อง design-system และ state

ตัวอย่าง bootstrap:

```bash
mkdir web-frontend-app
cd web-frontend-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
```

จากนั้นค่อยใช้ web starter ที่ทีมคุณถนัด เช่น starter ทางการของ framework นั้น ๆ

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)
- [Web Frontend worked example](../../../overlays/web-frontend/examples/worked_example.md)

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Web Frontend
**Architecture:** Page / Component / State / Service
**Localization:** <csv-first / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- <framework>
- <state solution>
- <routing solution>
- <test/build commands>

## 3. Architecture Rules

- pages own screen orchestration
- components stay reusable
- services own API and external integration
- data fetching stays out of leaf UI

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
Choose the web-frontend overlay.
Use the prompt pipeline in order.
Keep page, component, state, and service boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` และ `skills/dependency-review/README.md` | page/component/state/service boundaries |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | frontend files และ structure |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | page ต้องบางและ boundary ต้องชัด |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | lint/build evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable frontend rules |

## โครง frontend ที่แนะนำ

ใช้ overlay structure นี้เป็นจุดตั้งต้น:

```text
src/
  pages/ or app/
  components/
  features/
  services/
  state/
  design-system/
```

กติกาที่ควรยึด:

- page components ใช้ประกอบหน้าจอ
- reusable components ต้อง reusable จริง
- data fetching ต้องไม่อยู่ใน presentational components
- design-system primitives ต้องไม่มี feature logic

## การ verify

ใช้ checks ที่ repo frontend รองรับ:

```bash
npm run lint
npm run build
```

ถ้ามี test command ให้เพิ่มเข้าไปด้วย

## pitfall

- ย้าย page logic ไปอยู่ใน reusable components
- ซ่อน data fetching ไว้ใน leaf UI primitives
- ปล่อยให้ design-system drift เงียบ ๆ
- ใส่ assumption ของ framework กลับเข้า foundation root

## memory notes

เก็บ decision ที่ควรจำถาวร เช่น:

- component boundaries
- state ownership
- design-system rules
- API access boundaries
