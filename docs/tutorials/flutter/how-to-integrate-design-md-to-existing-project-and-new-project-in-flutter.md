---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - design
aliases:
  - Integrate DESIGN.md into Flutter Projects
  - Flutter DESIGN.md Workflow
---

# วิธี integrate `DESIGN.md` เข้ากับ Flutter project ทั้งแบบโปรเจกต์เก่าและโปรเจกต์ใหม่

ใช้ tutorial นี้เมื่อคุณต้องการให้ `DESIGN.md` เป็น design contract ของโปรเจกต์ Flutter ตั้งแต่วันแรก หรือ retro-fit เข้าโปรเจกต์ที่มีอยู่แล้ว

## ใช้เมื่อไร

- ต้องการให้ AI อ่าน design rules ก่อนเริ่มงาน
- ต้องการให้ design system, token, component boundary, และ UI convention ชัดขึ้น
- ต้องการใช้ได้ทั้งกับโปรเจกต์ใหม่และโปรเจกต์เก่า

## เริ่มจากสิ่งที่ควรมี

1. มี Flutter repo อยู่แล้ว หรือกำลังจะสร้างใหม่
2. มี `AGENTS.md` ที่ root
3. มี `docs/prompt-pipeline.md`
4. เลือก `mobile-flutter` overlay
5. ตัดสินใจว่า `DESIGN.md` จะอยู่ที่ root หรือผูกกับ docs/design

## สร้าง `DESIGN.md` แบบสั้นที่ใช้ได้จริง

ตัวอย่างโครงที่แนะนำ:

```md
# DESIGN.md

**Project:** <project-name>
**Platform:** Flutter
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

## 6. Flutter Implementation Notes

- <theme rule>
- <component reuse rule>
- <asset or icon rule>

## 7. Workflow

1. Read `AGENTS.md`.
2. Read `DESIGN.md`.
3. Use the prompt pipeline in order.
4. Verify UI against the design contract.
5. Update project memory after durable decisions.
```

ถ้าคุณอยากได้ไฟล์ตัวอย่างแยกเพื่อ copy-paste โดยตรง เปิดไฟล์นี้:
- [Tutorial examples hub](../examples/index.md)
- [Design usage patterns](../examples/patterns/design/index.md)
- [Flutter DESIGN.md template](../examples/templates/flutter/design-md-flutter-template.md)
- [Flutter DESIGN.md template EN](../examples/templates/flutter/design-md-flutter-template_EN.md)

## ตัวอย่าง `DESIGN.md` ฉบับเต็มสำหรับ Flutter

ใช้ block นี้ได้ทันที แล้วค่อยปรับชื่อ project, tone, และ token ให้ตรงของจริง:

```md
# DESIGN.md

**Project:** <project-name>
**Platform:** Flutter
**Purpose:** A Flutter app that delivers a clear, calm, and reliable user experience.
**Design System:** Custom tokens with reusable Flutter components
**Tone:** calm, clean, trustworthy

This file defines the visual and interaction rules for this project.

---

## 1. Design Principles

- Keep the interface simple and task-focused.
- Prefer readable hierarchy over decorative complexity.
- Reuse components instead of creating one-off widget styles.
- Make empty states, loading states, and error states explicit.

## 2. Layout Rules

- Use an 8pt spacing system.
- Keep consistent page padding across screens.
- Prefer vertical rhythm and aligned content blocks.
- Respect safe areas and device insets.
- Avoid nested layout stacks that make spacing hard to predict.

## 3. Typography Rules

- Use one primary font family across the app.
- Reserve bold weight for headings and high-priority labels.
- Keep body text at a readable size with sufficient line height.
- Do not mix too many font sizes in one screen.

## 4. Color Rules

- Use one primary brand color.
- Use semantic colors for success, warning, and error states.
- Keep neutral surfaces quiet and high-contrast text readable.
- Do not encode meaning with color alone.

## 5. Component Rules

- Buttons must use consistent sizes, shapes, and states.
- Forms must have clear labels, helper text, and validation feedback.
- Cards must have one clear purpose and one dominant action.
- Empty states must explain what happened and what to do next.
- Dialogs must be used only for interruption-worthy actions.

## 6. Flutter Implementation Notes

- Centralize theme tokens in `ThemeData` or a shared design token layer.
- Prefer reusable widgets over ad-hoc styling in feature screens.
- Keep icon usage consistent and purposeful.
- Keep animation subtle and short unless the screen explicitly needs motion.
- Separate presentation widgets from state and business logic.

## 7. Accessibility Rules

- Maintain readable contrast for text and interactive controls.
- Support text scaling without layout collapse.
- Ensure touch targets are large enough on mobile devices.
- Provide labels for icon-only controls.

## 8. Responsive Rules

- Design first for mobile width, then scale up responsibly.
- Avoid fixed widths that break on smaller screens.
- Allow content to reflow cleanly on tablet or desktop-sized screens.

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
6. เลือก `mobile-flutter` overlay
7. ใช้ prompt ให้ AI scaffold UI ตาม design contract
8. verify ด้วย `flutter analyze` และ `flutter test`
9. บันทึก decision ลง project memory

ตัวอย่าง bootstrap:

```bash
mkdir flutter-app
cd flutter-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
```

## วิธีใช้กับโปรเจกต์เก่า

1. เพิ่ม `DESIGN.md` เข้าไปใน root หรือ `docs/`
2. สรุป design rules จากสิ่งที่มีอยู่จริง เช่น theme, component style, layout pattern
3. ค่อย sync `AGENTS.md` ให้ชี้ว่า design contract อยู่ที่ไหน
4. ใช้ prompt ให้ AI เปลี่ยนทีละ layer ไม่แก้ UI แบบสุ่ม

## สิ่งที่ควรอ่าน

- [เริ่มจากโฟลเดอร์เปล่า](../00-common-start.md)
- [AGENTS.md และ prompt guide](../agents-and-prompts.md)
- [Mobile Flutter overlay README](../../../overlays/mobile-flutter/README.md)
- [Mobile Flutter overlay rules](../../../overlays/mobile-flutter/AGENTS.overlay.md)
- [Mobile Flutter worked example](../../../overlays/mobile-flutter/examples/worked_example.md)

## ตัวอย่าง AGENTS.md ที่ใช้ได้เลย

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Flutter App
**Architecture:** Clean Architecture + Design System
**Localization:** <csv-first / none / other>
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
- keep theme and component tokens centralized
- avoid one-off UI styling in feature widgets

## 4. Architecture Rules

- widgets stay focused on UI
- keep business logic out of widgets
- keep routing and state boundaries explicit

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
Start from a blank folder or existing Flutter project.
Tell me how to introduce DESIGN.md into the repo and which files to update first.
Keep design tokens, theme, and widget boundaries explicit.
```

## prompt flow ที่แนะนำ

| Stage | Prompt | ใช้ทำอะไร |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | ตรวจว่า repo ใช้ toolkit และ overlay อย่างไร |
| Plan | `prompts/planning/plan_change.md` | ระบุว่าการใช้ DESIGN.md จะกระทบอะไร |
| Architecture | `prompts/design/architecture_review.md` | วาง design boundary, theme ownership, component rules |
| Implement | `prompts/implementation/implement_change.md` | ปรับ theme, components, layout, docs |
| Review | `prompts/review/review_change.md` | ตรวจว่า UI ตรง design contract |
| Verify | `prompts/verification/verification_pass.md` | ยืนยันด้วย analysis/test/manual check |
| Finalize | `prompts/finalization/finalize_change.md` | สรุปผลและ follow-up |
| Memory | `prompts/memory/update_project_memory.md` | บันทึก design decisions |

## pitfall

- ให้ `DESIGN.md` กลายเป็นไฟล์สวยแต่ไม่มีใครใช้
- เขียน design rules กว้างเกินไปจนไม่ช่วยตัดสินใจ
- ลืม sync `AGENTS.md` กับ `DESIGN.md`
- ปล่อยให้ feature widget มี styling ที่ไม่อยู่ใน design contract

## memory notes

เก็บเฉพาะเรื่องที่ควรจำถาวร เช่น:

- path ของ `DESIGN.md`
- theme ownership
- component boundary
- design token naming
- accessibility and state feedback rules
