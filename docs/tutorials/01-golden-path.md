---
tags:
  - tutorial
  - onboarding
  - golden-path
aliases:
  - First 10 Minutes
---

# เส้นทางหลัก 10 นาทีแรก

ใช้โน้ตนี้เมื่อคุณอยากพิสูจน์เร็วที่สุดว่า toolkit นี้ “ใช้งานได้จริง” ไม่ใช่แค่อ่านเอกสาร

## เป้าหมาย

เมื่อจบ tutorial นี้ คุณควรได้:

- repo ใหม่จากโฟลเดอร์เปล่า
- toolkit ถูกเพิ่มเข้ามาแล้ว
- `AGENTS.md` แบบสั้นที่ใช้งานได้จริง
- project memory ขั้นต่ำ
- งานจริง 1 ชิ้นที่ผ่าน lifecycle ครบ

## ผลลัพธ์ที่แนะนำ

ถ้ายังไม่รู้จะเริ่มจากอะไร ให้เลือก outcome แบบนี้:

- Flutter app skeleton 1 ตัว
- หน้าจอเดียว
- มี state management และ routing ชัด
- verify ได้

## ขั้นตอนเร็วที่สุด

1. สร้างโฟลเดอร์เปล่าและ `git init`
2. เพิ่ม toolkit แบบ submodule หรือ copy เข้ามา
3. สร้าง `AGENTS.md` แบบสั้น
4. คัดลอก `project_memory/`
5. เลือก overlay ให้ชัด
6. ใช้ prompt pipeline ให้ครบ 1 รอบ
7. ขอให้ AI สร้างงานเล็ก ๆ ที่ verify ได้จริง

## AGENTS.md แบบสั้นที่พอใช้ได้

```md
# AGENTS.md

**Project:** Demo starter
**Type:** Flutter app
**Architecture:** Clean architecture with explicit presentation/domain/data boundaries
**Target:** Android, iOS, Web

This file defines the repo-wide operating rules for all agents working in this repository.

## 1. Repository Purpose
Build a maintainable Flutter application using the toolkit lifecycle and overlay conventions.

## 2. Default Tech Stack
- Flutter
- Dart
- Material 3

## 3. Architecture Rules
- Keep presentation, domain, and data separate
- Do not bypass domain rules from UI
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
Choose the correct overlay for a small Flutter starter app.
Create only the minimum files needed for a first successful pass.
Use the canonical lifecycle in order:
adopt -> plan -> architecture -> implement -> review -> verify -> finalize -> memory.

Goal:
- one Flutter app
- one home screen
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

- [Mental model ของระบบ Agent](./02-agent-mental-model.md)
- [Workflow ของจริงแบบ Lead → Architecture → Feature](./03-real-workflow.md)
- tutorial เฉพาะ stack ที่คุณจะใช้จริง
