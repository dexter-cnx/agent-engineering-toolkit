---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - design
aliases:
  - วิธี integrate DESIGN.md กับ Web Frontend
  - Web Design Contract Tutorial
---

# วิธี integrate `DESIGN.md` กับ Web Frontend ทั้งโปรเจกต์ใหม่และโปรเจกต์เก่า

ใช้ tutorial นี้เมื่อคุณอยากกำหนด design contract ให้ web frontend ตั้งแต่เริ่ม หรือ retro-fit
design rules เข้า repo ที่มีอยู่แล้ว

## ใช้เมื่อไร

- ต้องการคุม design-style และ design system ให้สม่ำเสมอ
- ต้องการให้ UI, forms, states, และ layout มีข้อตกลงเดียวกัน
- ต้องการให้ทีมและ AI อ่านกติกาเดียวกันก่อนแก้หน้าเว็บ

## สิ่งที่ควรมี

1. มี web frontend repo อยู่แล้ว หรือกำลังจะสร้างใหม่
2. มี `AGENTS.md` ที่ root
3. มี `docs/prompt-pipeline.md`
4. เลือก `web-frontend` overlay
5. ตัดสินใจว่า `DESIGN.md` จะอยู่ที่ root หรือใน `docs/`

## ตัวอย่าง `DESIGN.md`

```md
# DESIGN.md

**Project:** <project-name>
**Platform:** Web Frontend
**Purpose:** <what this product does>
**Design System:** <name of system or none>
**Tone:** <calm, bold, playful, enterprise>

This file defines the visual and interaction rules for this project.

---

## 1. Design Principles

- <principle 1>
- <principle 2>
- <principle 3>

## 2. Layout Rules

- <spacing rule>
- <responsive rule>
- <surface rule>

## 3. Typography Rules

- <font rule>
- <hierarchy rule>

## 4. Color Rules

- <primary color rule>
- <semantic color rule>

## 5. Component Rules

- <button rule>
- <form rule>
- <empty state rule>

## 6. Frontend Implementation Notes

- <theme rule>
- <component reuse rule>
- <asset or icon rule>

## 7. Workflow

1. Read `AGENTS.md`.
2. Read `DESIGN.md`.
3. Use the prompt pipeline in order.
4. Verify the UI against the design contract.
5. Update project memory after durable decisions.
```

## ถ้าเป็นโปรเจกต์ใหม่

1. สร้างโฟลเดอร์เปล่า
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md`
5. เพิ่ม `DESIGN.md`
6. เลือก `web-frontend` overlay
7. สร้างโครง React+Vite หรือ Next.js
8. สร้าง tokens และ component primitives ก่อนค่อยลง feature
9. verify ด้วย lint, test, build
10. บันทึก decision ที่ควรจำ

## ถ้าเป็นโปรเจกต์เก่า

1. ดู layout และ style ที่มีอยู่จริงก่อน
2. สรุป token และ component rule ที่ซ้ำบ่อย
3. ตัดสินใจว่าอะไรควรกลายเป็น shared primitive
4. ย้าย page-specific style ออกจาก component ที่ควร reuse
5. เพิ่ม `DESIGN.md` แล้ว sync กับ `AGENTS.md`

## กติกาที่ควรยึด

- page components ใช้ประกอบหน้าจอ
- design-system primitives ต้อง reusable จริง
- forms ต้องมี label, helper text, error state, focus state
- responsive rule ต้องระบุชัด
- motion ใช้เท่าที่จำเป็น
- semantic HTML ต้องมาก่อนความสวย

## สิ่งที่ควรอ่านต่อ

- [เริ่มจากโฟลเดอร์เปล่า](./00-common-start.md)
- [AGENTS.md และ prompt guide](./agents-and-prompts.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)
- [Web Frontend worked example](../../../overlays/web-frontend/examples/worked_example.md)
