---
tags:
  - agent-engineering-toolkit
  - tutorial
  - flutter
  - prompts
  - firebase
aliases:
  - Prompt Firebase Services for Flutter EN
  - Flutter Firebase Prompt Tutorial EN
---

# How to Prompt AI to Add Firebase Services to Flutter

Use this tutorial when you already have a Flutter app and want to ask AI to add Firebase services with clear boundaries.

## When to Use This

- You want Firebase added incrementally, not directly from widgets
- You want AI to propose packages, adapters, auth flow, and verification first
- You want to keep the repo in a clean or layered architecture

## Before You Start

1. You already have a Flutter repo.
2. The root `AGENTS.md` exists.
3. The repo uses the `mobile-flutter` overlay.
4. Read `docs/prompt-pipeline.md`.
5. Decide which Firebase services you actually need.

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
- firebase_core
- firebase_auth
- cloud_firestore
- <state management>

## 3. Architecture Rules

- Firebase access must stay behind adapter or service layers
- widgets stay thin
- auth/session logic must be explicit
- keep repository boundaries clean

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
We already have a Flutter app.
Add Firebase services behind adapter and service layers only.
Start by proposing the package list, files to create, and verification steps.
Do not put Firebase calls directly inside widgets.
Keep auth, data, and UI boundaries explicit.
```

## Recommended Prompt Flow

| Stage | Prompt | What It Does |
| --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | Check how the repo uses the toolkit and overlay |
| Plan | `prompts/planning/plan_change.md` | Describe where Firebase should be added |
| Architecture | `prompts/design/architecture_review.md` | Define Firebase boundary, auth flow, and data ownership |
| Implement | `prompts/implementation/implement_change.md` | Add packages, adapter, service, and provider code |
| Review | `prompts/review/review_change.md` | Check that Firebase does not leak into widgets |
| Verify | `prompts/verification/verification_pass.md` | Confirm analysis, tests, and smoke checks |
| Finalize | `prompts/finalization/finalize_change.md` | Summarize the result and follow-ups |
| Memory | `prompts/memory/update_project_memory.md` | Record durable rules |

## Firebase-Focused Prompt Example

```text
Add Firebase services to this Flutter app.
Use firebase_core, firebase_auth, and cloud_firestore only if needed.
Keep Firebase behind adapter or service layers.
Update the repo structure first, then list the files to modify, then verify with flutter analyze and flutter test.
```

## Suggested Shape

- `presentation/` for UI
- `domain/` for use cases
- `data/` for Firebase repository implementations
- `services/` or `adapters/` for Firebase client integration

## Pitfalls

- telling AI to put Firebase calls directly into widgets
- forgetting to define auth/session flow
- mixing package installation with architecture decisions
- skipping the verification step

