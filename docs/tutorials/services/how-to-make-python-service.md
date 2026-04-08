---
tags:
  - agent-engineering-toolkit
  - tutorial
  - python
  - service
aliases:
  - Python Service Tutorial
  - Python Service from Blank Folder
---

# วิธีทำ python service

ใช้ tutorial นี้สำหรับ Python service, worker, adapter layer หรือ automation system

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์และ initialize git
2. เพิ่ม toolkit และ project memory
3. เพิ่ม `AGENTS.md`
4. เลือก `python-service` overlay
5. ตั้งค่า Python environment
6. สร้าง app structure
7. แยก routers, services, repositories, adapters และ schemas ออกจากกัน
8. verify ด้วย import, startup และ test checks
9. บันทึก memory สำหรับกติกาเรื่อง provider และ API contract

ตัวอย่าง bootstrap:

```bash
mkdir python-service-app
cd python-service-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
python3 -m venv .venv
```

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Python Service overlay README](../../../overlays/python-service/README.md)
- [Python Service overlay rules](../../../overlays/python-service/AGENTS.overlay.md)
- [Python Service worked example](../../../overlays/python-service/examples/python_service_feature.md)

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Service
**Architecture:** Transport / Orchestration / Persistence / Adapter
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Python
- <framework>
- <database / queue / provider>
- <test/startup commands>

## 3. Architecture Rules

- transport layer must stay thin
- orchestration layer owns the flow
- persistence layer owns storage
- adapter layer wraps external providers

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
Choose the python-service overlay.
Use the prompt pipeline in order.
Keep transport, orchestration, persistence, and adapter boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | task restatement, facts, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` และ `skills/dependency-review/README.md` | router/service/repository/adapters/schemas |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Python files และ structure |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | handlers ต้องบางและ boundary ต้องชัด |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | import/startup/test evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable Python rules |

## โครง Python service ที่แนะนำ

ใช้ overlay guidance นี้:

```text
app/
  routers/
  services/
  repositories/
  domain/
  adapters/
  schemas/
tests/
scripts/
```

กติกาที่ควรยึด:

- routers ต้องบาง
- services ต้องเป็นเจ้าของ orchestration
- repositories ต้องเป็นเจ้าของ persistence access
- adapters ต้อง isolate providers และ side effects
- schemas ต้อง define request และ response shapes

## การ verify

รัน checks ที่ repo รองรับ:

```bash
python -m pytest
python -c "from app.main import app; print(app.title)"
```

ถ้ามี lint หรือ static checks ให้เพิ่มเข้าไปด้วย

## pitfall

- ผสม transport กับ business logic
- เรียก provider ตรงจาก module ที่ไม่เกี่ยวข้อง
- เขียน contract rule ไว้แต่ไม่ได้บันทึกให้ชัด
- อ้างว่า verify แล้วทั้งที่ไม่มี evidence

## memory notes

เก็บ decision ที่ควรจำถาวร เช่น:

- provider constraints
- retry และ timeout behavior
- contract rules
- background-job behavior assumptions
