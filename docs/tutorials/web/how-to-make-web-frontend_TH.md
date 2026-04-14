---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - frontend
aliases:
  - วิธีสร้าง Web Frontend จากโฟลเดอร์เปล่า
  - คู่มือเริ่มต้น Web Frontend ภาษาไทย
---

# วิธีทำ Web Frontend จากโฟลเดอร์เปล่า

หน้านี้เป็น hub ภาษาไทยสำหรับการเริ่ม web frontend ใหม่
เลือก tutorial ตาม stack ที่ทีมใช้:

- [React + Vite](./how-to-make-web-frontend-react-vite_TH.md)
- [Next.js](./how-to-make-web-frontend-nextjs_TH.md)

ทั้งสองเส้นทางจะคุมเรื่องเดียวกัน:

- routing
- state
- networking
- auth
- forms
- i18n
- design-style / design system

## สิ่งที่ควรอ่านก่อน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)
- [Web Frontend worked example](../../../overlays/web-frontend/examples/worked_example.md)

## กติกาที่เหมือนกันทุก stack

- page หรือ route layer เป็นตัวประกอบหน้าจอ
- reusable components ต้อง reusable จริง
- state mutation ต้องอยู่ใน state layer
- data access ต้องผ่าน service, adapter, หรือ data hook
- design-system primitives ต้องไม่ fetch ข้อมูลเอง
- user-facing string ต้องผ่าน localization layer

## ตัวอย่าง `AGENTS.md`

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Web Frontend
**Architecture:** Page / Feature / Component / Service / State / Design System
**Localization:** i18n-first
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- <framework>
- <routing solution>
- <state solution>
- <networking solution>
- <test/build commands>

## 3. Architecture Rules

- pages own screen orchestration
- features own business behavior
- components stay reusable
- services own API and external integration
- state mutations stay in the state layer
- design-system primitives stay feature-free
- forms and validation stay explicit
- translations come from the localization layer

## 4. Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify before finalizing
5. Update project memory after durable decisions
```

## เกณฑ์ verify ร่วม

- routing อยู่ในชั้น routing
- state mutation ไม่อยู่ใน leaf component
- networking ไม่ซ่อนอยู่ใน presentation primitive
- auth flow มี boundary ชัด
- forms มี validation และ error handling
- i18n keys ไม่ drift
- design-style ถูกคุมผ่าน token หรือ design system
- lint, test, build ผ่าน
