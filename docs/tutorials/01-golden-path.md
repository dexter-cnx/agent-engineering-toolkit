---
tags:
  - tutorial
  - onboarding
  - golden-path
aliases:
  - First 10 Minutes
---

# เส้นทางหลัก 10 นาทีแรก

ใช้โน้ตนี้เมื่อคุณอยากพิสูจน์เร็วที่สุดว่า toolkit นี้ใช้งานได้จริงใน repo ใหม่ โดยยังไม่ผูกกับ stack ใด stack หนึ่ง

## เป้าหมาย

เมื่อจบ tutorial นี้ คุณควรได้:

- repo ใหม่จากโฟลเดอร์เปล่า
- toolkit ถูกเพิ่มเข้ามาแล้ว
- `AGENTS.md` แบบสั้นที่ใช้งานได้จริง
- project memory ขั้นต่ำ
- งานเล็ก 1 ชิ้นที่ผ่าน canonical lifecycle ครบ

## ผลลัพธ์ที่แนะนำ

ถ้ายังไม่รู้จะเริ่มจากอะไร ให้เลือก outcome แบบนี้:

- feature slice เล็ก ๆ 1 ชิ้น
- boundary ชัด
- verify ได้จริง
- ไม่ผูกกับ stack ใด stack หนึ่งตั้งแต่เริ่ม

## ขั้นตอนเร็วที่สุด

1. สร้างโฟลเดอร์เปล่าและ `git init`
2. เพิ่ม toolkit แบบ submodule หรือ copy เข้ามา
3. สร้าง `AGENTS.md` แบบสั้น
4. คัดลอก `project_memory/`
5. เลือก overlay ถ้า stack ของ repo ชัดแล้ว
6. ใช้ prompt pipeline ให้ครบ 1 รอบ
7. ขอให้ AI สร้างงานเล็ก ๆ ที่ verify ได้จริง

## AGENTS.md แบบสั้นที่พอใช้ได้

```md
# AGENTS.md

**Project:** Demo starter
**Type:** <project-type>
**Architecture:** <chosen-architecture>
**Target:** <target users>

This file defines the repo-wide operating rules for all agents working in this repository.

## 1. Repository Purpose
<what this repo is for>

## 2. Default Tech Stack
- <stack item 1>
- <stack item 2>
- <stack item 3>

## 3. Architecture Rules
- Keep the major boundaries explicit
- Do not bypass domain rules from entry-layer code
- Keep third-party integrations behind adapters

## 4. Workflow Rules
1. Read AGENTS.md first
2. Use canonical prompts in order
3. Verify before finalize
4. Update project memory after durable decisions
```

## Prompt ชุดสั้นสำหรับ first success

```text
We are starting from a blank folder.

Read AGENTS.md first.
Adopt the toolkit into this repository.
Choose the correct overlay only if the stack is known.
Create only the minimum files needed for a first successful pass.
Use the canonical lifecycle in order:
adopt -> plan -> architecture -> implement -> review -> verify -> finalize -> memory.

Goal:
- one small feature slice
- clear folder structure
- one successful verification pass

Do not over-engineer.
Keep the result small but production-shaped.
```

## สิ่งที่ถือว่า “สำเร็จแล้ว”

งานชิ้นแรกไม่จำเป็นต้องใหญ่ แต่ควรมีครบ 4 อย่าง:

- โครงสร้างไม่มั่ว
- boundary ชัด
- คำอธิบาย final response ชัด
- verification บอกตรง ๆ ว่าตรวจอะไรแล้ว

## pitfall ที่พบบ่อย

- เริ่มจาก feature ใหญ่เกินไป
- ยังไม่ได้ตั้ง `AGENTS.md`
- ยังไม่ได้เลือก overlay แต่เริ่ม implement
- ขอให้ AI ทำทุกอย่างรวดเดียวจนไม่มีจุด review
- ไม่มี verification pass

## หลังจากจบหน้าแรกนี้

ให้ไปต่อที่:

- [Tutorial Hub](./index.md)
- [AGENTS.md และ prompt guide](./agents-and-prompts.md)
- tutorial เฉพาะ stack ที่คุณจะใช้จริง
