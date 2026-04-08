---
tags:
  - tutorial
  - onboarding
  - golden-path
aliases:
  - First 10 Minutes
---

# 10-Minute Golden Path

Use this note when you want to prove quickly that the toolkit works in practice, not just on paper.

## Goal

By the end of this tutorial, you should have:

- a new repo from a blank folder
- the toolkit added
- a short but usable `AGENTS.md`
- minimal project memory
- one real task completed through the lifecycle

## Recommended first outcome

If you are unsure what to build first, use this target:

- one Flutter app skeleton
- one screen
- explicit state and routing choices
- something that can be verified

## Fastest path

1. Create a blank folder and run `git init`
2. Add the toolkit by submodule or copy
3. Create a short `AGENTS.md`
4. copy `project_memory/`
5. choose the overlay
6. run the prompt pipeline once
7. ask the AI for one small, verifiable result

## Minimal AGENTS.md starter

```md
# AGENTS.md

**Project:** Demo starter
**Type:** Flutter app
**Architecture:** Clean architecture with explicit presentation/domain/data boundaries
**Target:** Android, iOS, Web

This file defines the repo-wide operating rules for all agents working in this repository.

## 1. Repository Purpose
Build a maintainable Flutter application using the toolkit lifecycle and overlay conventions.

## 2. Default Tech Stack
- Flutter
- Dart
- Material 3

## 3. Architecture Rules
- Keep presentation, domain, and data separate
- Do not bypass domain rules from UI
- Keep third-party integrations behind adapters

## 4. Workflow Rules
1. Read AGENTS.md first
2. Use canonical prompts in order
3. Verify before finalize
4. Update project memory after durable decisions
```

## Short prompt for first success

```text
We are starting from a blank folder.

Read AGENTS.md first.
Adopt the toolkit into this repository.
Choose the correct overlay for a small Flutter starter app.
Create only the minimum files needed for a first successful pass.
Use the canonical lifecycle in order:
adopt -> plan -> architecture -> implement -> review -> verify -> finalize -> memory.

Goal:
- one Flutter app
- one home screen
- clear folder structure
- one successful verification pass

Do not over-engineer.
Keep the result small but production-shaped.
```

## What counts as success

The first task does not need to be large. It does need these four traits:

- structure is sane
- boundaries are explicit
- the final response is clear
- the verification pass says exactly what was checked

## Common mistakes

- starting with a feature that is too large
- skipping `AGENTS.md`
- implementing before choosing an overlay
- asking the AI to do everything in one jump
- no verification pass

## Where to go next

Continue with:

- [Agent system mental model](./02-agent-mental-model_EN.md)
- [Real workflow: Lead → Architecture → Feature](./03-real-workflow_EN.md)
- the stack tutorial you actually plan to use
