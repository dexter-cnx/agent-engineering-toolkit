---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - offline-first
aliases:
  - Offline First Flutter Tutorial EN
  - Flutter Offline App EN
---

# How to Make an Offline-First Flutter App

Use this tutorial when the app must keep working without network access and sync later.

## Start from a Blank Folder

1. Create the folder and initialize git.
2. Bootstrap the toolkit and project memory.
3. Add `AGENTS.md`.
4. Choose the `mobile-flutter` overlay.
5. Decide the offline data strategy before writing code.
6. Build the app shell and local storage boundary.
7. Install `isar` as the example local database.
8. Add sync or queue rules only after boundaries are clear.
9. Verify both normal and offline behavior.
10. Save memory for sync and conflict decisions.

Example bootstrap:

```bash
mkdir flutter-offline-first-app
cd flutter-offline-first-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add isar isar_flutter_libs
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
**Architecture:** Offline-First / Clean Architecture
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- isar
- <state management>
- <routing>
- <offline storage>

## 3. Architecture Rules

- UI stays thin
- offline data flow is explicit
- keep repository boundary clean

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
Use Isar as the local database and keep it behind a repository or storage adapter.
Use the prompt pipeline in order.
Keep offline-first data flow and widget boundaries explicit.
```

## Recommended Prompt Flow

| Step | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay choice |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | offline assumptions, risks, constraints |
| 3 | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` | local storage, sync boundary, conflict policy |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | app shell, cache, sync adapter, queue boundary |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | leakage checks and boundary review |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | offline evidence, remaining uncertainty |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | none | durable offline rules |

## Suggested Offline-First Shape

Keep a clear separation for:

- presentation
- domain/use cases
- local persistence or cache
- sync adapter or queue processor

Example `isar` setup for the data/storage layer:

```dart
final isar = await Isar.open(
  [MyEntitySchema],
  directory: '/path/to/app/data',
);
```

Use `isar` as the local source of truth or cache layer, then keep sync logic separate from widgets.

Useful questions:

- What is the source of truth when offline?
- What happens when sync conflicts occur?
- What retries are allowed?
- Which actions are queued for later?

## Verification

Use Flutter checks plus an offline smoke test if possible:

```bash
flutter analyze
flutter test
```

Add a manual airplane-mode or disconnected-device check if the app has sync behavior.

## Pitfalls

- assuming the network is always present
- hiding sync logic inside widgets
- letting conflict policy remain undefined
- direct API calls from presentation code

## Memory Notes

Store durable decisions about:

- offline source of truth
- sync rules
- conflict handling
- queue and retry behavior
