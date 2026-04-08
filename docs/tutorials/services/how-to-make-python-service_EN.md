---
tags:
  - agent-engineering-toolkit
  - tutorial
  - python
  - service
aliases:
  - Python Service Tutorial EN
  - Python Service from Blank Folder EN
---

# How to Make Python Service

Use this tutorial for a Python service, worker, adapter layer, or automation system.

## Start from a Blank Folder

1. Create the folder and initialize git.
2. Bootstrap the toolkit and project memory.
3. Add `AGENTS.md`.
4. Choose the `python-service` overlay.
5. Set up your Python environment.
6. Create the app structure.
7. Keep routers, services, repositories, adapters, and schemas separate.
8. Verify with import, startup, and test checks.
9. Save memory for provider and API contract rules.

Example bootstrap:

```bash
mkdir python-service-app
cd python-service-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
python3 -m venv .venv
```

## What to Read

- [Start from a Blank Folder](../00-common-start_EN.md)
- [AGENTS.md and prompt guide](../agents-and-prompts_EN.md)
- [Python Service overlay README](../../../overlays/python-service/README.md)
- [Python Service overlay rules](../../../overlays/python-service/AGENTS.overlay.md)
- [Python Service worked example](../../../overlays/python-service/examples/python_service_feature.md)

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

- Python
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
Choose the python-service overlay.
Use the prompt pipeline in order.
Keep transport, orchestration, persistence, and adapter boundaries explicit.
```

## Recommended Prompt Flow

| Step | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | task restatement, facts, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` and `skills/dependency-review/README.md` | router/service/repository/adapters/schemas |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Python files and structure |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | thin handlers, clean boundaries |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | import/startup/test evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | none | durable Python rules |

## Suggested Python Service Shape

Use the overlay guidance:

```text
app/
  routers/
  services/
  repositories/
  domain/
  adapters/
  schemas/
tests/
scripts/
```

Rules to keep:

- routers stay thin
- services own orchestration
- repositories own persistence access
- adapters isolate providers and side effects
- schemas define request and response shapes

## Verification

Run the checks your repo supports:

```bash
python -m pytest
python -c "from app.main import app; print(app.title)"
```

If you have lint or static checks, add them too.

## Pitfalls

- mixing transport and business logic
- calling providers directly from unrelated modules
- hiding important contract rules in prose only
- claiming verification without evidence

## Memory Notes

Store durable decisions about:

- provider constraints
- retry and timeout behavior
- contract rules
- background-job behavior assumptions
