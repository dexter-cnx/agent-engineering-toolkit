---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - online
aliases:
  - Online Flutter Tutorial EN
  - Flutter Online App EN
---

# How to Make an Online Flutter App

Use this tutorial when the Flutter app depends on server-backed features and online APIs.

## Start from a Blank Folder

1. Create the folder and initialize git.
2. Bootstrap the toolkit and project memory.
3. Add `AGENTS.md`.
4. Choose the `mobile-flutter` overlay.
5. Pick the API boundary before building UI.
6. Create the Flutter app shell.
7. Install `dio` as the example HTTP client.
8. Put network and session logic behind adapters or services.
9. Verify with online-focused checks.
10. Save memory for API and transport decisions.

Example bootstrap:

```bash
mkdir flutter-online-app
cd flutter-online-app
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
flutter create .
flutter pub add dio
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
**Architecture:** Online App / Clean Architecture
**Localization:** <csv-first / none / other>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- Flutter
- dio
- <state management>
- <routing>
- <api client>

## 3. Architecture Rules

- widgets stay thin
- API calls live outside widgets
- keep routes, state, and data boundaries explicit

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
Use dio as the HTTP client and keep it behind an adapter or service.
Use the prompt pipeline in order.
Keep API, state, and widget boundaries explicit.
```

## Recommended Prompt Flow

| Step | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| 1 | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay |
| 2 | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | API assumptions, risks, constraints |
| 3 | `prompts/design/architecture_review.md` | `skills/dependency-review/README.md` | API boundary, adapter placement, provider risk |
| 4 | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | app shell, network layer, state flow |
| 5 | `prompts/review/review_change.md` | `skills/architecture-review/README.md` | thin UI, no transport leakage |
| 6 | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | API smoke evidence and uncertainty |
| 7 | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| 8 | `prompts/memory/update_project_memory.md` | none | durable API conventions |

## Suggested Online-First Shape

Keep these responsibilities separate:

- presentation widgets
- feature or state layer
- API service or adapter
- domain/use-case layer

Example `dio` setup for the service or adapter layer:

```dart
final dio = Dio(
  BaseOptions(
    baseUrl: 'https://api.example.com',
    connectTimeout: const Duration(seconds: 10),
    receiveTimeout: const Duration(seconds: 10),
  ),
);
```

Use `dio` as the HTTP client behind an adapter or service, then map the response to a model or entity in the appropriate layer.

If auth, session, or retry behavior matters, write it down early in architecture review.

## Verification

Use the normal Flutter checks plus whatever online smoke test your repo supports:

```bash
flutter analyze
flutter test
```

If you have a mock server or staging API, include a small smoke check.

## Pitfalls

- making widgets call network APIs directly
- scattering API helpers through the UI
- letting loading/error states disappear into unrelated components
- leaving auth/session handling implicit

## Memory Notes

Store durable decisions about:

- API contract expectations
- auth/session rules
- retry and error-handling behavior
- adapter boundaries
