---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - mobile
aliases:
  - Basic Flutter App Tutorial EN
  - Flutter App from Blank Folder EN
---

# How to Make a Basic Flutter App

Use this tutorial when you want a normal Flutter app with clean foundation boundaries.

## Start from a Blank Folder

1. Create a blank folder for the app.
2. Initialize git.
3. Bootstrap the toolkit and project memory.
4. Add a repo-root `AGENTS.md`.
5. Choose the `mobile-flutter` overlay.
6. Create the Flutter app shell.
7. Run the lifecycle prompts in order.
8. Verify with Flutter commands.
9. Finalize and save memory.

Example bootstrap:

```bash
mkdir flutter-basic-app
cd flutter-basic-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
```

## What to Read

- [Start from a Blank Folder](../00-common-start_EN.md)
- [AGENTS.md and prompt guide](../agents-and-prompts_EN.md)
- [Mobile Flutter overlay README](../../../overlays/mobile-flutter/README.md)
- [Mobile Flutter overlay rules](../../../overlays/mobile-flutter/AGENTS.overlay.md)
- [Mobile Flutter worked example](../../../overlays/mobile-flutter/examples/worked_example.md)
- [docs/tutorial.md](../../tutorial.md)

## AGENTS.md Example You Can Use

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Flutter App
**Architecture:** <chosen-architecture>
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- <state management>
- <routing>
- <test command>

## 3. Architecture Rules

- widgets stay focused on UI
- keep business logic out of widgets
- keep routing and state boundaries explicit

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
Keep widget, state, and routing boundaries explicit.
```

## Recommended Prompt Flow

| Step | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path, overlay, bootstrap files |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | task restatement, facts, assumptions, risks |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | boundaries, structure, guardrails |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` if cleanup is needed | Flutter files and app structure |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | strengths, blocking issues, non-blocking issues |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | checks, evidence, uncertainty |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary, follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | none | durable notes |

## Suggested Flutter Shape

Use the mobile overlay structure as the starting point:

```text
lib/
  presentation/
  domain/
  data/
  app/
  core/
```

Keep these boundaries:

- widgets stay focused on UI
- domain holds business rules
- data owns persistence or API access
- navigation stays out of leaf widgets

## Verification

Run the project-specific checks that apply to the Flutter app:

```bash
flutter analyze
flutter test
```

If you have a startup or device smoke test, add it here.

## Pitfalls

- putting business logic inside widgets
- calling APIs directly from presentation code
- letting navigation drift into unrelated widgets
- adding Flutter assumptions to foundation docs

## Memory Notes

Store only durable notes such as:

- preferred widget boundary patterns
- navigation rules
- state management conventions
- testing rules for this Flutter repo
