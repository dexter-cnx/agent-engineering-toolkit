---
tags:
  - agent-engineering-toolkit
  - tutorial
  - example
  - web
  - design
aliases:
  - Web Frontend DESIGN.md Template
---

# เทมเพลต DESIGN.md สำหรับ Web Frontend

ใช้เทมเพลตนี้เป็นจุดเริ่มต้นสำหรับ web frontend ที่ต้องการกติกาด้าน design ที่ชัดเจนและนำไปใช้ซ้ำได้

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
