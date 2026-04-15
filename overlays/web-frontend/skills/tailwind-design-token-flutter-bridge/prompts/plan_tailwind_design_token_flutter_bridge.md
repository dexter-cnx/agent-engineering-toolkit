# Prompt: plan_tailwind_design_token_flutter_bridge

Use this prompt when a repo needs a shared design system for web frontend and Flutter.

## Prompt

Follow AGENTS.md strictly.

Goal:
Create or refactor a shared design language across web frontend and Flutter.

Requirements:
- Tailwind CSS is the default styling layer for web frontend
- design tokens are the visual source of truth
- web and Flutter must share semantic token naming where practical
- repeated styling patterns must become reusable primitives
- avoid hard-coded visual values unless justified

Deliverables:
1. proposed token taxonomy
2. web mapping plan
3. Flutter mapping plan
4. component extraction plan
5. verification checklist
6. migration risks

Constraints:
- keep business logic out of styling layers
- do not break existing feature behavior
- start small with durable tokens
