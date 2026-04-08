---
tags:
  - agent-engineering-toolkit
  - tutorial
  - agents
  - prompts
  - obsidian
aliases:
  - AGENTS and Prompts Guide
  - Tutorial Setup Guide
---

# AGENTS.md และ prompt สำหรับเริ่ม tutorial

ใช้โน้ตนี้ก่อนเริ่ม tutorial ใด ๆ ในโฟลเดอร์นี้ เพื่อเลือก `AGENTS.md` ที่ควรสร้างก่อน และเลือก prompt ให้ตรงกับ platform

## หลักคิดสั้น ๆ

1. เริ่มจาก `AGENTS.md` แบบสั้นและใช้งานได้จริง
2. ใส่ข้อมูลให้พอรู้ว่า repo นี้คืออะไร, ใช้ stack อะไร, และห้ามอะไร
3. ถ้ารู้ stack แล้ว ค่อยเพิ่ม overlay-specific rules ใน repo นั้น
4. ใช้ prompt ตามลำดับจาก `docs/prompt-pipeline.md`
5. อย่าเริ่ม implement ก่อนกำหนด boundary

## AGENTS.md แบบสั้นที่แนะนำ

ถ้าคุณอยากได้ไฟล์ประมาณโปรเจกต์เก่าที่ใช้งานได้จริง ให้เริ่มจากโครงแบบนี้:

```md
# AGENTS.md

**Project:** <project-name>
**Type:** <platform/project-type>
**Architecture:** <chosen-architecture>
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- <stack item 1>
- <stack item 2>
- <stack item 3>

## 3. Architecture Rules

- <boundary rule 1>
- <boundary rule 2>
- <boundary rule 3>

## 4. Localization Rules

- <localization rule 1>
- <localization rule 2>

## 5. State Management & Routing

- <state rule 1>
- <routing rule 1>

## 6. Development Workflow

1. Read this file.
2. Read the canonical docs.
3. Use the lifecycle prompts in order.
4. Verify before finalizing.
5. Update project memory after durable decisions.

## 7. Output Format

1. Task Summary
2. Files Created / Modified
3. Verification Result
4. Next Recommended Step
5. Artifacts
```

ถ้าโปรเจกต์เล็กมาก ให้ตัดหัวข้อที่ไม่จำเป็นออกได้ แต่ควรเก็บ 3 อย่างไว้เสมอ:

- repo purpose
- architecture / boundary rules
- workflow + verification rules

ถ้ารู้ stack แล้ว ให้เติม overlay-specific notes แบบสั้น ๆ ต่อท้ายเท่าที่จำเป็น แล้วพา reader ไปอ่าน tutorial เฉพาะ stack แทนการคัด template ยาว ๆ ซ้ำในหน้านี้

Stack-specific examples ที่มีอยู่แล้ว:

- Flutter: `docs/tutorials/flutter/how-to-make-basic-flutter-app.md`
- Web frontend: `docs/tutorials/web/how-to-make-web-frontend.md`
- Services: `docs/tutorials/services/how-to-make-backend-node.md`
- Python service: `docs/tutorials/services/how-to-make-python-service.md`

The stack tutorials and overlays carry the concrete platform-specific AGENTS.md examples and prompt starters.

## Prompt flow ที่ควรใช้

| Stage | Prompt | ใช้ทำอะไร |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | เลือกว่าจะ bootstrap repo นี้อย่างไร และควรใช้ overlay ไหน |
| Plan | `prompts/planning/plan_change.md` | แปลง request ให้เป็นแผนที่ชัดเจน |
| Architecture | `prompts/design/architecture_review.md` | กำหนด boundary และ guardrail |
| Implement | `prompts/implementation/implement_change.md` | ลงมือสร้างไฟล์จริง |
| Review | `prompts/review/review_change.md` | ตรวจว่ามี leakage หรือ design debt ไหม |
| Verify | `prompts/verification/verification_pass.md` | ยืนยันสิ่งที่ตรวจแล้วและสิ่งที่ยังไม่แน่ใจ |
| Finalize | `prompts/finalization/finalize_change.md` | สรุปผลให้พร้อมส่งต่อ |
| Memory | `prompts/memory/update_project_memory.md` | เก็บ decision และ constraint ที่ควรจำ |

## Prompt starter ตาม platform

### Flutter

```text
We are starting from a blank folder for a Flutter app.
Create a short, practical repo-root AGENTS.md first in the style of the example in docs/tutorials/agents-and-prompts.md.
Then choose the mobile-flutter overlay.
Use the prompt pipeline in order and keep state management, routing, and localization rules explicit.
```

### Web frontend

```text
We are starting from a blank folder for a web frontend repo.
Create a short, practical repo-root AGENTS.md first in the style of the example in docs/tutorials/agents-and-prompts.md.
Then choose the web-frontend overlay.
Use the prompt pipeline in order and keep page, component, state, and service rules explicit.
```

### Services

```text
We are starting from a blank folder for a service repo.
Create a short, practical repo-root AGENTS.md first in the style of the example in docs/tutorials/agents-and-prompts.md.
Then choose the backend-node or python-service overlay.
Use the prompt pipeline in order and keep transport, orchestration, persistence, and adapter rules explicit.
```

## อ่านต่อ

- [เริ่มจากโฟลเดอร์เปล่า](./00-common-start.md)
- [Tutorial Hub](./index.md)
- [docs/prompt-pipeline.md](../prompt-pipeline.md)
- [docs/agent-team-system.md](../agent-team-system.md)
