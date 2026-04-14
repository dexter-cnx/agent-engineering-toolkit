---
tags:
  - agent-engineering-toolkit
  - tutorial
  - example
  - flutter
  - design
aliases:
  - Flutter DESIGN.md Template
---

# เทมเพลต DESIGN.md สำหรับ Flutter

ใช้เทมเพลตนี้เป็นจุดเริ่มต้นสำหรับ repo Flutter ที่ต้องการกติกาด้าน design ที่ชัดเจนและนำไปใช้ซ้ำได้

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
