---
tags:
  - agent-engineering-toolkit
  - tutorial
  - node
  - backend
aliases:
  - Backend Node Tutorial EN
  - Node Service from Blank Folder EN
---

# How to Make Backend Node

Use this tutorial for a Node backend, API service, or job processor.

## Start from a Blank Folder

1. Create the folder and initialize git.
2. Bootstrap the toolkit and project memory.
3. Add `AGENTS.md`.
4. Choose the `backend-node` overlay.
5. Initialize the Node project.
6. Create the service structure.
7. Keep transport, orchestration, persistence, and adapter concerns separate.
8. Verify with lint, test, and startup checks.
9. Save memory for boundary and provider decisions.

Example bootstrap:

```bash
mkdir backend-node-app
cd backend-node-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
npm init -y
```

## What to Read

- [Start from a Blank Folder](../00-common-start_EN.md)
- [AGENTS.md and prompt guide](../agents-and-prompts_EN.md)
- [Backend Node overlay README](../../../overlays/backend-node/README.md)
- [Backend Node overlay rules](../../../overlays/backend-node/AGENTS.overlay.md)
- [Backend Node worked example](../../../overlays/backend-node/examples/worked_example.md)

## AGENTS.md Example You Can Use

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

- Node.js
- <framework>
- <database / queue / provider>
- <test/startup commands>

## 3. Architecture Rules

- transport layer must stay thin
- orchestration layer owns the flow
- persistence layer owns storage
- adapter layer wraps external providers

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
Choose the backend-node overlay.
Use the prompt pipeline in order.
Keep transport, orchestration, persistence, and adapter boundaries explicit.
```

## Recommended Prompt Flow

| Step | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` and `skills/dependency-review/README.md` | route/service/repository/adapter boundaries |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Node files and boundaries |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | thin routes, no transport leakage |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | lint/test/startup evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | none | durable Node rules |

## Suggested Backend Shape

Keep the overlay structure in mind:

```text
src/
  routes/
  services/
  repositories/
  adapters/
  domain/
  schemas/
```

Rules to keep:

- route handlers stay thin
- services do not import request/response types
- repositories do not mix persistence with transport
- adapters isolate external providers

## Verification

Use the repo-specific checks that exist in the consuming repo:

```bash
npm run lint
npm test
```

If the service has a startup or smoke command, include it.

## Pitfalls

- fat route handlers
- service code that knows transport details
- direct provider calls outside adapters
- config scattered through handlers

## Memory Notes

Store durable decisions about:

- routing style
- service boundary rules
- repository behavior
- adapter and provider rules
