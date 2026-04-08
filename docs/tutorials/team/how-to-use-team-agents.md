---
tags:
  - agent-engineering-toolkit
  - tutorial
  - agents
  - team
  - obsidian
aliases:
  - How to Use Team Agents
  - Team Agents Workflow
---

# วิธีใช้ Team Agents

ใช้ tutorial นี้เมื่อคุณอยากให้ Codex หรือ Claude ทำงานแบบมีบทบาทชัดเจน ไม่ใช่เป็น assistant เดียวที่ตอบทุกอย่างในครั้งเดียว

## แนวคิดหลัก

1. LEAD วางกรอบและลำดับงาน
2. ARCHITECT วาง boundary และโครงสร้าง
3. BUILDER ลงมือทำ
4. REVIEWER ตรวจคุณภาพและความเสี่ยง
5. VERIFIER ตรวจหลักฐานที่รันจริง
6. FINALIZER จัดผลลัพธ์ให้พร้อมส่งต่อ
7. MEMORY เก็บสิ่งที่ต้องจำถาวร

## เริ่มจากสิ่งที่ควรมี

1. มี repo ที่มี `AGENTS.md`
2. มี `docs/prompt-pipeline.md`
3. มี `docs/agent-team-system.md`
4. รู้ว่า task นี้เป็นงานเล็กหรือใหญ่
5. เลือกว่าจะใช้ Codex, Claude, หรือทั้งคู่

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** <platform/project-type>
**Architecture:** <chosen-architecture>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Canonical References

- docs/prompt-pipeline.md
- docs/agent-team-system.md

## 3. Role Rules

- LEAD handles framing and sequencing
- ARCHITECT handles boundaries and interfaces
- BUILDER handles implementation
- REVIEWER handles critique
- VERIFIER handles evidence
- FINALIZER handles packaging
- MEMORY handles durable notes

## 4. Workflow

1. Read this file.
2. Use the lifecycle prompts in order.
3. Keep review and verification separate.
4. Update project memory after durable decisions.
```

## ตัวอย่าง prompt เริ่มงาน

```text
Follow AGENTS.md strictly.
Use the team-agent workflow from docs/agent-team-system.md.
Start as LEAD and restate the task.
Then switch to ARCHITECT for boundaries.
Use BUILDER, REVIEWER, VERIFIER, FINALIZER, and MEMORY in order.
Keep each role's output separate.
```

## ตัวอย่าง prompt สำหรับแต่ละ role

### LEAD

```text
Act as LEAD.
Restate the task, list assumptions, identify constraints, and sequence the next steps.
Do not implement yet.
```

### ARCHITECT

```text
Act as ARCHITECT.
Define boundaries, interfaces, layering, and the main structural risks.
Return the safest structure before implementation starts.
```

### BUILDER

```text
Act as BUILDER.
Implement only what the plan and architecture approved.
List files changed and call out deviations.
```

### REVIEWER

```text
Act as REVIEWER.
Critique correctness, readability, maintainability, and hidden risk.
Separate blocking issues from non-blocking issues.
```

### VERIFIER

```text
Act as VERIFIER.
State what was actually checked, what evidence exists, and what remains uncertain.
Do not claim checks that were not run.
```

### FINALIZER

```text
Act as FINALIZER.
Package the result clearly and keep the handoff concise.
```

### MEMORY

```text
Act as MEMORY.
Capture only durable decisions, constraints, patterns, and reminders.
```

## ใช้กับ Codex

- เหมาะกับงานที่ต้องอ่าน repo, แก้ไฟล์, และรันคำสั่งตรวจสอบ
- แนะนำให้แยก prompt ตาม role แทนการยัดทุกอย่างใน prompt เดียว
- ถ้างานใหญ่ ให้ส่งต่อเป็น sequence: LEAD -> ARCHITECT -> BUILDER -> REVIEWER -> VERIFIER -> FINALIZER -> MEMORY

## ใช้กับ Claude

- ใช้ role sequence เดียวกันกับ Codex
- ถ้าทำงานใน thread เดียว ให้เปลี่ยนบทบาทชัด ๆ ในแต่ละช่วง
- อย่าให้ review กับ verification ปนกัน
- ให้ Claude ยึด `AGENTS.md` และ prompt pipeline เหมือนกัน

## วิธีทำงานที่แนะนำ

1. ใช้ LEAD สรุป task
2. ใช้ ARCHITECT สรุป boundary
3. ใช้ BUILDER ลงมือทำ
4. ใช้ REVIEWER หาจุดเสี่ยง
5. ใช้ VERIFIER เช็กหลักฐาน
6. ใช้ FINALIZER สรุปผล
7. ใช้ MEMORY บันทึกสิ่งที่ต้องจำ

## pitfall

- ข้าม LEAD แล้วรีบ implement
- ให้ role เดียวทำทุกอย่างในครั้งเดียว
- ปล่อยให้ review กับ verification ปะปนกัน
- ไม่เก็บ memory หลังมี decision สำคัญ

