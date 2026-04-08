---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - frontend
aliases:
  - Web Frontend Tutorial EN
  - Frontend from Blank Folder EN
---

# How to Make Web Frontend

Use this tutorial for a web UI, admin dashboard, or product frontend.

## Start from a Blank Folder

1. Create the folder and initialize git.
2. Bootstrap the toolkit and project memory.
3. Add `AGENTS.md`.
4. Choose the `web-frontend` overlay.
5. Initialize your web app with the starter your team uses.
6. Separate page orchestration from reusable components.
7. Keep data access and state flow out of presentation primitives.
8. Verify with lint and build checks.
9. Save memory for design-system and state rules.

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

Then run your preferred web starter, such as the official starter for your framework.

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
**Architecture:** Page / Component / State / Service
**Localization:** <csv-first / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- <framework>
- <state solution>
- <routing solution>
- <test/build commands>

## 3. Architecture Rules

- pages own screen orchestration
- components stay reusable
- services own API and external integration
- data fetching stays out of leaf UI

## 4. Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify before finalizing
5. Update project memory after durable decisions
```

## Example Prompt to Start

```text
Follow AGENTS.md strictly.
Start from a blank folder.
Create a short, practical repo-root AGENTS.md.
Choose the web-frontend overlay.
Use the prompt pipeline in order.
Keep page, component, state, and service boundaries explicit.
```

## Recommended Prompt Flow

| Step | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` and `skills/dependency-review/README.md` | page/component/state/service boundaries |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | frontend files and structure |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | thin pages and clean boundaries |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | lint/build evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | none | durable frontend rules |

## Suggested Frontend Shape

Keep the overlay structure in mind:

```text
src/
  pages/ or app/
  components/
  features/
  services/
  state/
  design-system/
```

Rules to keep:

- page components assemble the screen
- reusable components stay reusable
- data fetching stays out of presentational components
- design-system primitives stay free of feature logic

## Verification

Use the checks your frontend repo supports:

```bash
npm run lint
npm run build
```

Add test commands if the repo has them.

## Pitfalls

- moving page logic into reusable components
- hiding data fetching inside leaf UI primitives
- letting design-system drift happen silently
- adding framework assumptions to the foundation root

## Memory Notes

Store durable decisions about:

- component boundaries
- state ownership
- design-system rules
- API access boundaries
