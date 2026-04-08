---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - design
aliases:
  - Integrate DESIGN.md into Flutter Projects EN
  - Flutter DESIGN.md Workflow EN
---

# How to Integrate `DESIGN.md` into Flutter Projects, Both Existing and New

Use this tutorial when you want `DESIGN.md` to act as the design contract for a Flutter project from day one, or when you need to retrofit it into an existing codebase.

## When to Use This

- You want AI to read design rules before starting work
- You want design system, token, component boundary, and UI conventions to stay clear
- You want one approach that works for both new and existing projects

## Before You Start

1. You already have a Flutter repo, or you are about to create one.
2. The root `AGENTS.md` exists.
3. You have `docs/prompt-pipeline.md`.
4. You choose the `mobile-flutter` overlay.
5. You decide whether `DESIGN.md` lives at the root or under `docs/`.

## Short `DESIGN.md` Template You Can Actually Use

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
4. Verify the UI against the design contract.
5. Update project memory after durable decisions.
```

If you want a separate file you can copy-paste directly, open:
- [Tutorial examples hub](../examples/index_EN.md)
- [Design usage patterns](../examples/patterns/design/index_EN.md)
- [Flutter DESIGN.md template](../examples/templates/flutter/design-md-flutter-template.md)
- [Flutter DESIGN.md template EN](../examples/templates/flutter/design-md-flutter-template_EN.md)

## Full `DESIGN.md` Example for Flutter

You can copy this block as-is, then adjust the project name, tone, and tokens to match the real app:

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

## New Project Flow

1. Create a blank folder.
2. Initialize git.
3. Bootstrap the toolkit and project memory.
4. Add `AGENTS.md` at the root.
5. Add `DESIGN.md` at the root or under `docs/`.
6. Choose the `mobile-flutter` overlay.
7. Use prompts to scaffold UI against the design contract.
8. Verify with `flutter analyze` and `flutter test`.
9. Record durable decisions in project memory.

Example bootstrap:

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

## Existing Project Flow

1. Add `DESIGN.md` into the root or `docs/`.
2. Summarize the real design rules already used by the app, such as theme, component style, and layout patterns.
3. Sync `AGENTS.md` so it clearly points to the design contract.
4. Ask AI to change one layer at a time instead of reshaping UI randomly.

## What to Read

- [Start from a Blank Folder](../00-common-start_EN.md)
- [AGENTS.md and prompt guide](../agents-and-prompts_EN.md)
- [Mobile Flutter overlay README](../../../overlays/mobile-flutter/README.md)
- [Mobile Flutter overlay rules](../../../overlays/mobile-flutter/AGENTS.overlay.md)
- [Mobile Flutter worked example](../../../overlays/mobile-flutter/examples/worked_example.md)

## AGENTS.md Example You Can Use

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

## Example Prompt to Start

```text
Follow AGENTS.md strictly.
Read DESIGN.md before proposing UI changes.
Start from a blank folder or existing Flutter project.
Tell me how to introduce DESIGN.md into the repo and which files to update first.
Keep design tokens, theme, and widget boundaries explicit.
```

## Recommended Prompt Flow

| Stage | Prompt | What It Does |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | Check how the repo uses the toolkit and overlay |
| Plan | `prompts/planning/plan_change.md` | Identify what introducing DESIGN.md will affect |
| Architecture | `prompts/design/architecture_review.md` | Define design boundary, theme ownership, and component rules |
| Implement | `prompts/implementation/implement_change.md` | Update theme, components, layout, and docs |
| Review | `prompts/review/review_change.md` | Check that the UI matches the design contract |
| Verify | `prompts/verification/verification_pass.md` | Confirm with analysis, tests, and manual checks |
| Finalize | `prompts/finalization/finalize_change.md` | Summarize the result and follow-ups |
| Memory | `prompts/memory/update_project_memory.md` | Record design decisions |

## Pitfalls

- turning `DESIGN.md` into a pretty file nobody uses
- making design rules too broad to be useful
- forgetting to sync `AGENTS.md` with `DESIGN.md`
- letting feature widgets own styles that do not belong in the design contract

## Memory Notes

Keep only durable items, such as:

- the path to `DESIGN.md`
- theme ownership
- component boundaries
- design token naming
- accessibility and state feedback rules
