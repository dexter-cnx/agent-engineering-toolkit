---
tags:
  - agent-engineering-toolkit
  - tutorial
  - node
  - backend
aliases:
  - Backend Node Tutorial
  - Node Service from Blank Folder
---

# วิธีทำ backend-node

ใช้ tutorial นี้สำหรับ Node backend, API service หรือ job processor

## เริ่มจากโฟลเดอร์เปล่า

1. สร้างโฟลเดอร์และ initialize git
2. เพิ่ม toolkit และ project memory
3. เพิ่ม `AGENTS.md`
4. เลือก `backend-node` overlay
5. initialize โปรเจกต์ Node
6. สร้าง service structure
7. แยก transport, orchestration, persistence และ adapter ออกจากกัน
8. verify ด้วย lint, test และ startup checks
9. บันทึก memory สำหรับกติกาเรื่อง boundary และ provider

ตัวอย่าง bootstrap:

```bash
mkdir backend-node-app
cd backend-node-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
npm init -y
```

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Backend Node overlay README](../../../overlays/backend-node/README.md)
- [Backend Node overlay rules](../../../overlays/backend-node/AGENTS.overlay.md)
- [Backend Node worked example](../../../overlays/backend-node/examples/worked_example.md)

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

- Node.js
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
Choose the backend-node overlay.
Use the prompt pipeline in order.
Keep transport, orchestration, persistence, and adapter boundaries explicit.
```

## ลำดับ prompt ที่แนะนำ

| Step | Prompt | Skill ที่ควรอ่าน | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path และ overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` และ `skills/dependency-review/README.md` | route/service/repository/adapter boundaries |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Node files และ boundary |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | route ต้องบางและ transport leakage ต้องไม่มี |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | lint/test/startup evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary และ follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | ไม่มี skill เพิ่ม | durable Node rules |

## โครง backend ที่แนะนำ

ใช้ overlay structure นี้เป็นจุดตั้งต้น:

```text
src/
  routes/
  services/
  repositories/
  adapters/
  domain/
  schemas/
```

กติกาที่ควรยึด:

- route handler ต้องบาง
- service ต้องไม่ import request/response types
- repository ต้องไม่ผสม persistence กับ transport
- adapter ต้อง isolate external providers

## การ verify

ใช้คำสั่งตรวจที่มีอยู่จริงใน consuming repo:

```bash
npm run lint
npm test
```

ถ้า service มี startup หรือ smoke command ให้ใส่เพิ่ม

## pitfall

- route handler หนาเกินไป
- service code รู้เรื่อง transport มากเกินไป
- เรียก provider ตรงจากนอก adapter
- กระจาย config ไปทั่ว handler

## memory notes

เก็บ decision ที่ควรจำถาวร เช่น:

- routing style
- service boundary rules
- repository behavior
- adapter และ provider rules
