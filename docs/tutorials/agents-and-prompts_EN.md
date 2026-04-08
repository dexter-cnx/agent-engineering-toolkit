---
tags:
  - agent-engineering-toolkit
  - tutorial
  - agents
  - prompts
  - obsidian
aliases:
  - AGENTS and Prompts Guide EN
  - Tutorial Setup Guide EN
---

# AGENTS.md and Prompt Setup for Tutorials

Use this note before starting any tutorial in this folder so you can choose the right `AGENTS.md` shape and the right prompt flow for the platform.

## Core Idea

1. Start with a short, practical `AGENTS.md` that is actually usable.
2. Include just enough information to say what the repo is, what stack it uses, and what is not allowed.
3. Once the stack is known, add overlay-specific rules in that repo.
4. Use prompts in the order defined by `docs/prompt-pipeline.md`.
5. Do not jump straight into implementation before boundaries are set.

## Short AGENTS.md Template

If you want a file that feels like a real project AGENTS.md, start with this shape:

```md
# AGENTS.md

**Project:** <project-name>
**Type:** <platform/project-type>
**Architecture:** <chosen-architecture>
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- <stack item 1>
- <stack item 2>
- <stack item 3>

## 3. Architecture Rules

- <boundary rule 1>
- <boundary rule 2>
- <boundary rule 3>

## 4. Localization Rules

- <localization rule 1>
- <localization rule 2>

## 5. State Management & Routing

- <state rule 1>
- <routing rule 1>

## 6. Development Workflow

1. Read this file.
2. Read the canonical docs.
3. Use the lifecycle prompts in order.
4. Verify before finalizing.
5. Update project memory after durable decisions.

## 7. Output Format

1. Task Summary
2. Files Created / Modified
3. Verification Result
4. Next Recommended Step
5. Artifacts
```

If the project is very small, trim the extra sections, but keep these three:

- repository purpose
- architecture / boundary rules
- workflow + verification rules

If you already know the stack, add short overlay notes at the end:

- Flutter: `mobile-flutter` overlay
- Web frontend: `web-frontend` overlay
- Services: `backend-node` or `python-service` overlay

## Platform Examples for AGENTS.md

### Flutter

If you want a short AGENTS.md that feels like a real project file:

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Flutter App
**Architecture:** Clean Architecture + Riverpod + go_router
**Localization:** CSV-first
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter (latest stable)
- Riverpod
- go_router
- CSV-first localization

## 3. Architecture Rules

- `presentation/` = UI + state
- `domain/` = entities, use cases, repository contracts
- `data/` = models, repository implementations, datasources
- Do not put business logic or API calls in widgets

## 4. Localization Rules

- Use CSV as the source of truth
- Do not hardcode Thai/English strings in code
- Support at least `th` and `en`

## 5. State Management & Routing

- Use Riverpod for state
- Use go_router for routing
- Do not rely on setState or global mutable state as the primary pattern

## 6. Development Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify before finalizing
5. Update project memory when you make a durable decision

## 7. Output Format

1. Task Summary
2. Files Created / Modified
3. Verification Result
4. Next Recommended Step
5. Artifacts
```

### Web Frontend

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

- `pages/` or `app/` = screen orchestration
- `components/` = reusable UI
- `state/` = state ownership
- `services/` = API and external integration

## 4. UI Rules

- design-system primitives must stay reusable
- data fetching must not live in leaf components
- page logic must stay thin

## 5. Workflow

1. Read `AGENTS.md`
2. Choose the overlay
3. Use the lifecycle prompts
4. Verify with lint/build/test
5. Update memory when a durable decision is made
```

### Services

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Service
**Architecture:** Transport / Orchestration / Persistence / Adapter
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- <runtime>
- <framework>
- <database / queue / external provider>
- <test/startup commands>

## 3. Architecture Rules

- transport layer must stay thin
- orchestration layer owns the flow
- persistence layer owns storage
- adapter layer wraps external providers

## 4. Workflow

1. Read `AGENTS.md`
2. Choose the overlay
3. Use the lifecycle prompts
4. Verify with lint/test/startup
5. Update memory when you make a durable decision
```

### Flutter

- use the `mobile-flutter` overlay
- for Flutter tutorials, keep state management, routing, and localization rules short and practical
- keep business logic away from widget boundaries
- list the real test commands in that repo

### Web frontend

- use the `web-frontend` overlay
- for web tutorials, keep page, component, state, and service rules short and practical
- keep design-system or component conventions minimal but clear
- include the lint/build/test commands in the checklist

### Services

- use the `backend-node` or `python-service` overlay, depending on the stack
- for service tutorials, keep route/handler, service/orchestration, repository, and adapter rules short and practical
- keep transport logic out of the domain
- spell out startup, test, and smoke commands clearly

## Prompt Flow to Use

| Stage | Prompt | What It Does |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | Decide how to bootstrap the repo and which overlay to use |
| Plan | `prompts/planning/plan_change.md` | Turn the request into a clear plan |
| Architecture | `prompts/design/architecture_review.md` | Define boundaries and guardrails |
| Implement | `prompts/implementation/implement_change.md` | Create the actual files |
| Review | `prompts/review/review_change.md` | Check for leakage or design debt |
| Verify | `prompts/verification/verification_pass.md` | State what was verified and what is still uncertain |
| Finalize | `prompts/finalization/finalize_change.md` | Package the result for handoff |
| Memory | `prompts/memory/update_project_memory.md` | Save durable decisions and constraints |

## Prompt Starters by Platform

### Flutter

```text
We are starting from a blank folder for a Flutter app.
Create a short, practical repo-root AGENTS.md first in the style of the example in docs/tutorials/agents-and-prompts_EN.md.
Then choose the mobile-flutter overlay.
Use the prompt pipeline in order and keep state management, routing, and localization rules explicit.
```

### Web frontend

```text
We are starting from a blank folder for a web frontend repo.
Create a short, practical repo-root AGENTS.md first in the style of the example in docs/tutorials/agents-and-prompts_EN.md.
Then choose the web-frontend overlay.
Use the prompt pipeline in order and keep page, component, state, and service rules explicit.
```

### Services

```text
We are starting from a blank folder for a service repo.
Create a short, practical repo-root AGENTS.md first in the style of the example in docs/tutorials/agents-and-prompts_EN.md.
Then choose the backend-node or python-service overlay.
Use the prompt pipeline in order and keep transport, orchestration, persistence, and adapter rules explicit.
```

## Continue Reading

- [Start from a Blank Folder](./00-common-start_EN.md)
- [Tutorial Hub](./index_EN.md)
- [เริ่มจากโฟลเดอร์เปล่า](./00-common-start.md)
- [docs/prompt-pipeline.md](../prompt-pipeline.md)
- [docs/agent-team-system.md](../agent-team-system.md)
