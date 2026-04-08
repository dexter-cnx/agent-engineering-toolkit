---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - design
aliases:
  - Integrate DESIGN.md into Web Frontend Projects EN
  - Web DESIGN.md Workflow EN
---

# How to Integrate `DESIGN.md` into Web Frontend Projects, Both Existing and New

Use this tutorial when you want `DESIGN.md` to act as the design contract for a web project from day one, or when you need to retrofit it into an existing frontend codebase.

## When to Use This

- You want AI to read design rules before touching the UI
- You want design system, layout, component, and state boundaries to stay clear
- You want one template that works for both new and existing projects

## Before You Start

1. You already have a web frontend repo, or you are about to create one.
2. The root `AGENTS.md` exists.
3. You have `docs/prompt-pipeline.md`.
4. You choose the `web-frontend` overlay.
5. You decide whether `DESIGN.md` lives at the root or under `docs/`.

## Short `DESIGN.md` Template You Can Actually Use

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

If you want a separate file you can copy-paste directly, open:
- [Tutorial examples hub](../examples/index_EN.md)
- [Design usage patterns](../examples/patterns/design/index_EN.md)
- [Web Frontend DESIGN.md template](../examples/templates/web/design-md-web-frontend-template.md)
- [Web Frontend DESIGN.md template EN](../examples/templates/web/design-md-web-frontend-template_EN.md)

## Full `DESIGN.md` Example for Web Frontend

You can copy this block as-is, then adjust the project name, tone, and tokens to match the real app:

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

## New Project Flow

1. Create a blank folder.
2. Initialize git.
3. Bootstrap the toolkit and project memory.
4. Add `AGENTS.md` at the root.
5. Add `DESIGN.md` at the root or under `docs/`.
6. Choose the `web-frontend` overlay.
7. Use prompts to scaffold UI against the design contract.
8. Verify with lint and build checks.
9. Record durable decisions in project memory.

Example bootstrap:

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

Then use the framework starter your team prefers.

## Existing Project Flow

1. Add `DESIGN.md` into the root or `docs/`.
2. Summarize the real design rules already used by the app, such as spacing, card style, page shell, and dialog behavior.
3. Sync `AGENTS.md` so it clearly points to the design contract.
4. Ask AI to change one area at a time instead of reshaping the whole UI at once.

## What to Read

- [Start from a Blank Folder](../00-common-start_EN.md)
- [AGENTS.md and prompt guide](../agents-and-prompts_EN.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)
- [Web Frontend worked example](../../../overlays/web-frontend/examples/worked_example.md)

## AGENTS.md Example You Can Use

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

## Example Prompt to Start

```text
Follow AGENTS.md strictly.
Read DESIGN.md before proposing UI changes.
Start from a blank folder or existing web frontend project.
Tell me how to introduce DESIGN.md into the repo and which files to update first.
Keep design tokens, page shell, components, and state boundaries explicit.
```

## Recommended Prompt Flow

| Stage | Prompt | What It Does |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | Check how the repo uses the toolkit and overlay |
| Plan | `prompts/planning/plan_change.md` | Identify what introducing DESIGN.md will affect |
| Architecture | `prompts/design/architecture_review.md` | Define design boundary, page shell, and component rules |
| Implement | `prompts/implementation/implement_change.md` | Update theme, components, layout, and docs |
| Review | `prompts/review/review_change.md` | Check that the UI matches the design contract |
| Verify | `prompts/verification/verification_pass.md` | Confirm with lint, build, and manual checks |
| Finalize | `prompts/finalization/finalize_change.md` | Summarize the result and follow-ups |
| Memory | `prompts/memory/update_project_memory.md` | Record design decisions |

## Pitfalls

- turning `DESIGN.md` into a pretty document nobody uses
- making design rules too broad to be useful
- forgetting to sync `AGENTS.md` with `DESIGN.md`
- letting component primitives contain feature-specific styles

## Memory Notes

Keep only durable items, such as:

- the path to `DESIGN.md`
- design token ownership
- component boundaries
- page shell rules
- accessibility and state feedback rules
