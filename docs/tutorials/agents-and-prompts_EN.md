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

## 4. Workflow

1. Read this file.
2. Read the canonical docs.
3. Use the lifecycle prompts in order.
4. Verify before finalizing.
5. Update project memory after durable decisions.
```

If you already know the stack, keep the extra notes short and point people to the overlay instead of duplicating the full stack template here.

Stack-specific examples that already live elsewhere:

- Flutter: `docs/tutorials/flutter/how-to-make-basic-flutter-app_EN.md`
- Web frontend: `docs/tutorials/web/how-to-make-web-frontend_EN.md`
- Services: `docs/tutorials/services/how-to-make-backend-node_EN.md`
- Python service: `docs/tutorials/services/how-to-make-python-service_EN.md`

The stack tutorials and overlays carry the concrete platform-specific AGENTS.md examples and prompt starters.

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

## Prompt Starter

```text
We are starting from a blank folder.
Create a short, practical repo-root AGENTS.md first.
Then choose the correct overlay only if the stack is known.
Use the prompt pipeline in order and keep boundaries explicit.
```

## Continue Reading

- [Start from a Blank Folder](./00-common-start_EN.md)
- [Tutorial Hub](./index_EN.md)
- [เริ่มจากโฟลเดอร์เปล่า](./00-common-start.md)
- [docs/prompt-pipeline.md](../prompt-pipeline.md)
- [docs/agent-team-system.md](../agent-team-system.md)
