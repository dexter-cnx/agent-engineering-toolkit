---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - getx
  - clean-architecture
aliases:
  - Flutter Clean Architecture GetX EN
  - Flutter App with GetX EN
---

# How to Make a Flutter App with Clean Architecture + GetX

Use this tutorial when you want a Flutter app built with clean architecture and GetX for state management / DI / routing assistance.

## Start from a Blank Folder

1. Create a new folder.
2. Initialize git.
3. Add the toolkit and project memory.
4. Add `AGENTS.md`.
5. Choose the `mobile-flutter` overlay.
6. Install `get`.
7. Define the clean architecture boundary clearly.
8. Use GetX only in the app/presentation layer.
9. Verify with Flutter checks.
10. Save memory about controller and route boundaries.

Example bootstrap:

```bash
mkdir flutter-clean-getx
cd flutter-clean-getx
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add get
```

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
**Architecture:** Clean Architecture + GetX
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- get
- go_router or GetX routing
- <test command>

## 3. Architecture Rules

- `presentation/` = UI + controller
- `domain/` = entities, use cases, repository contracts
- `data/` = models, repository implementations, datasources
- keep controllers thin and readable

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
Choose the mobile-flutter overlay.
Use the prompt pipeline in order.
Keep GetX controllers thin and keep clean architecture boundaries explicit.
```

## Recommended Prompt Flow

| Step | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | boundary and dependency direction |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Flutter layers and GetX controllers |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | controller should not become a god object |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | analysis/test evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | none | durable GetX rules |

## Suggested Shape

```text
lib/
  app/
  presentation/
  domain/
  data/
  core/
```

GetX guidance:

- `presentation` contains widgets and controllers
- `app` contains routing, bindings, and app bootstrap
- `domain` contains entities, use cases, and business rules
- `data` contains repository implementations and data sources

## Using GetX

- Use `GetMaterialApp` and bindings to manage only the dependency wiring you need
- Do not let controllers absorb all business logic
- Keep routing and DI in the app/presentation layer only

Package install:

```bash
flutter pub add get
```

## Verification

```bash
flutter analyze
flutter test
```

Add widget tests or integration tests if your repo uses them.

## Pitfalls

- bloated controllers
- letting GetX become the architecture itself
- using global state to bypass boundaries
- mixing routing with domain logic

## Memory Notes

Store durable decisions about:

- controller and binding style
- the boundary between presentation and domain
- test strategy for GetX
- route ownership conventions
