---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - design
aliases:
  - Integrate DESIGN.md into Web Frontend Projects
  - Web DESIGN.md Workflow
---

# วิธี integrate `DESIGN.md` เข้ากับ Web Frontend project ทั้งแบบโปรเจกต์เก่าและโปรเจกต์ใหม่

ใช้ tutorial นี้เมื่อคุณอยากให้ `DESIGN.md` เป็น design contract ของเว็บโปรเจกต์ตั้งแต่วันแรก หรืออยาก retrofit เข้า frontend ที่มีอยู่แล้ว

## ใช้เมื่อไร

- ต้องการให้ AI อ่าน design rules ก่อนเริ่มแก้ UI
- ต้องการคุม design system, layout, component, และ state boundary ให้ชัด
- ต้องการใช้ template เดียวกับทั้งโปรเจกต์ใหม่และโปรเจกต์เก่า

## เริ่มจากสิ่งที่ควรมี

1. มี web frontend repo อยู่แล้ว หรือกำลังจะสร้างใหม่
2. มี `AGENTS.md` ที่ root
3. มี `docs/prompt-pipeline.md`
4. เลือก `web-frontend` overlay
5. ตัดสินใจว่า `DESIGN.md` จะอยู่ที่ root หรือ under `docs/`

## สร้าง `DESIGN.md` แบบสั้นที่ใช้ได้จริง

ตัวอย่างโครงที่แนะนำ:

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

ถ้าคุณอยากได้ไฟล์ตัวอย่างแยกเพื่อ copy-paste โดยตรง เปิดไฟล์นี้:
- [Tutorial examples hub](../examples/index.md)
- [Design usage patterns](../examples/patterns/design/index.md)
- [Web Frontend DESIGN.md template](../examples/templates/web/design-md-web-frontend-template.md)
- [Web Frontend DESIGN.md template EN](../examples/templates/web/design-md-web-frontend-template_EN.md)

## ตัวอย่าง `DESIGN.md` ฉบับเต็มสำหรับ Web Frontend

ใช้ block นี้ได้ทันที แล้วค่อยปรับชื่อ project, tone, และ token ให้ตรงของจริง:

```md
# DESIGN.md

**Project:** <project-name>
**Platform:** Web Frontend
**Purpose:** A web product that is clear, fast to scan, and easy to operate.
**Design System:** Custom tokens with reusable frontend components
**Tone:** calm, modern, trustworthy

This file defines the visual and interaction rules for this project.

---

## 1. Design Principles

- Keep the UI focused on task completion.
- Prefer clarity and hierarchy over visual noise.
- Reuse components instead of inventing page-specific variants.
- Make loading, empty, and error states explicit.

## 2. Layout Rules

- Use a predictable spacing scale.
- Keep page shells consistent across routes.
- Prefer responsive containers over fixed-width layouts.
- Make content readable at common desktop and laptop widths.
- Do not let page chrome fight with the main content area.

## 3. Typography Rules

- Use one primary font family across the product.
- Keep headings distinct but not oversized.
- Make body text comfortable to scan for long sessions.
- Do not mix too many font sizes or weights in the same surface.

## 4. Color Rules

- Use one primary brand color.
- Use semantic colors for success, warning, and error states.
- Keep surfaces neutral so content stays readable.
- Do not rely on color alone to communicate meaning.

## 5. Component Rules

- Buttons must have clear hierarchy, spacing, and states.
- Forms must expose labels, helper text, and validation feedback.
- Tables or lists must make scanning easy.
- Empty states must explain what happened and what to do next.
- Dialogs must be reserved for interruptive actions.

## 6. Frontend Implementation Notes

- Centralize tokens in the design system or theme layer.
- Keep reusable components free of page-specific logic.
- Keep data fetching out of leaf UI primitives.
- Keep navigation and orchestration in page or route-level code.
- Keep motion subtle and purposeful.

## 7. Accessibility Rules

- Maintain readable contrast for text and interactive controls.
- Support keyboard navigation for interactive surfaces.
- Ensure focus states are visible.
- Keep text scalable without breaking layouts.

## 8. Responsive Rules

- Design for desktop first if the product is desktop-heavy.
- Avoid rigid widths that break on smaller screens.
- Let sidebars, tables, and panels adapt gracefully.
- Preserve readability at narrower widths.

## 9. State and Feedback Rules

- Show loading, empty, success, and error states explicitly.
- Keep feedback messages short and actionable.
- Avoid silent failures.

## 10. Workflow

1. Read `AGENTS.md`.
2. Read this file.
3. Read `docs/prompt-pipeline.md`.
4. Use the prompt pipeline in order.
5. Verify the UI against this design contract.
6. Update project memory after durable decisions.
```

## วิธีใช้กับโปรเจกต์ใหม่

1. สร้างโฟลเดอร์เปล่า
2. initialize git
3. เพิ่ม toolkit และ project memory
4. เพิ่ม `AGENTS.md` ที่ root
5. เพิ่ม `DESIGN.md` ที่ root หรือใน `docs/`
6. เลือก `web-frontend` overlay
7. ใช้ prompt ให้ AI scaffold UI ตาม design contract
8. verify ด้วย lint และ build checks
9. บันทึก decision ลง project memory

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

จากนั้นค่อยใช้ starter ของ framework ที่ทีมถนัด

## วิธีใช้กับโปรเจกต์เก่า

1. เพิ่ม `DESIGN.md` เข้าไปใน root หรือ `docs/`
2. สรุป design rules จากของจริง เช่น spacing, card style, page shell, dialog behavior
3. sync `AGENTS.md` ให้ชี้ว่า design contract อยู่ที่ไหน
4. สั่ง AI ให้แก้ทีละส่วน ไม่แก้ layout ทั้งระบบพร้อมกัน

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
**Architecture:** Page / Component / State / Service + Design System
**Localization:** <csv-first / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Canonical References

- docs/prompt-pipeline.md
- docs/agent-team-system.md
- DESIGN.md

## 3. Design Rules

- follow the visual contract in `DESIGN.md`
- keep component primitives reusable
- keep styling consistent with the design system

## 4. Architecture Rules

- pages own screen orchestration
- components stay reusable
- services own API and external integration
- data fetching stays out of leaf UI

## 5. Workflow

1. Read `AGENTS.md`
2. Read `DESIGN.md`
3. Read `docs/prompt-pipeline.md`
4. Use the prompts in order
5. Verify before finalizing
6. Update project memory after durable decisions
```

## ตัวอย่าง prompt เริ่มงาน

```text
Follow AGENTS.md strictly.
Read DESIGN.md before proposing UI changes.
Start from a blank folder or existing web frontend project.
Tell me how to introduce DESIGN.md into the repo and which files to update first.
Keep design tokens, page shell, components, and state boundaries explicit.
```

## prompt flow ที่แนะนำ

| Stage | Prompt | ใช้ทำอะไร |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | ตรวจว่า repo ใช้ toolkit และ overlay อย่างไร |
| Plan | `prompts/planning/plan_change.md` | ระบุว่าการใช้ DESIGN.md จะกระทบอะไร |
| Architecture | `prompts/design/architecture_review.md` | วาง design boundary, page shell, component rules |
| Implement | `prompts/implementation/implement_change.md` | ปรับ theme, components, layout, docs |
| Review | `prompts/review/review_change.md` | ตรวจว่า UI ตรง design contract |
| Verify | `prompts/verification/verification_pass.md` | ยืนยันด้วย lint/build/manual check |
| Finalize | `prompts/finalization/finalize_change.md` | สรุปผลและ follow-up |
| Memory | `prompts/memory/update_project_memory.md` | บันทึก design decisions |

## pitfall

- ทำ `DESIGN.md` ให้เหมือนเอกสารสวยแต่ไม่มีการใช้งานจริง
- เขียน design rules กว้างเกินไปจนไม่ช่วยตัดสินใจ
- ลืม sync `AGENTS.md` กับ `DESIGN.md`
- ปล่อยให้ component primitive มี feature-specific style ปนอยู่

## memory notes

เก็บเฉพาะเรื่องที่ควรจำถาวร เช่น:

- path ของ `DESIGN.md`
- ownership ของ design tokens
- component boundary
- page shell rules
- accessibility and state feedback rules
