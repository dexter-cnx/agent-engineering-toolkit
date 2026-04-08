---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - bloc
  - clean-architecture
aliases:
  - Flutter Clean Architecture Bloc EN
  - Flutter App with BLoC EN
---

# How to Make a Flutter App with Clean Architecture + BLoC

Use this tutorial when you want a Flutter app built with clean architecture and BLoC as state management.

## Start from a Blank Folder

1. Create a new folder.
2. Initialize git.
3. Add the toolkit and project memory.
4. Add `AGENTS.md`.
5. Choose the `mobile-flutter` overlay.
6. Install `flutter_bloc` and `bloc`.
7. Define the clean architecture boundary clearly.
8. Use BLoC only in the presentation/feature layer.
9. Verify with Flutter checks.
10. Save memory about event/state flow.

Example bootstrap:

```bash
mkdir flutter-clean-bloc
cd flutter-clean-bloc
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add flutter_bloc bloc
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
**Architecture:** Clean Architecture + BLoC
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- flutter_bloc
- go_router
- <test command>

## 3. Architecture Rules

- `presentation/` = UI + bloc/cubit
- `domain/` = entities, use cases, repository contracts
- `data/` = models, repository implementations, datasources
- keep events and states thin and readable

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
Keep BLoC events and states thin and keep clean architecture boundaries explicit.
```

## Recommended Prompt Flow

| Step | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | boundary and dependency direction |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | Flutter layers and BLoC classes |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | bloc should not carry too much responsibility |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | analysis/test evidence |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | none | durable BLoC rules |

## Suggested Shape

```text
lib/
  app/
  presentation/
  domain/
  data/
  core/
```

BLoC guidance:

- `presentation` contains widgets and blocs/cubits
- `domain` contains entities, use cases, and business rules
- `data` contains repository implementations and data sources
- `app` contains app bootstrap, routing, and DI wiring

## Using BLoC

- Use `Event` and `State` so the flow stays explicit
- Do not let BLoC become a repository
- Have widgets send events and render state only

Package install:

```bash
flutter pub add flutter_bloc bloc
```

If the team uses value equality, consider `equatable`.

## Verification

```bash
flutter analyze
flutter test
```

Add bloc tests or widget tests if your repo uses them.

## Pitfalls

- bloated blocs
- letting event/state absorb all business logic
- widgets knowing about data sources directly
- using BLoC instead of the domain layer

## Memory Notes

Store durable decisions about:

- the team's event/state style
- the boundary between presentation and domain
- test strategy for blocs
- state ownership conventions
