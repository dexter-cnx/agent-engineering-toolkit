---
tags:
  - tutorial
  - onboarding
  - golden-path
aliases:
  - First 10 Minutes
---

# 10-Minute Golden Path

Use this note when you want to prove quickly that the toolkit works in a new repo without tying the foundation to one stack.

## Goal

By the end of this tutorial, you should have:

- a new repo from a blank folder
- the toolkit added
- a short but usable `AGENTS.md`
- minimal project memory
- one small task completed through the lifecycle

## Recommended first outcome

If you are unsure what to build first, use this target:

- one small feature slice
- clear boundaries
- something that can be verified
- no stack assumption baked in yet

## Fastest path

1. Create a blank folder and run `git init`
2. Add the toolkit by submodule or copy
3. Create a short `AGENTS.md`
4. copy `project_memory/`
5. choose the overlay only if the stack is known
6. run the prompt pipeline once
7. ask the AI for one small, verifiable result

## Minimal AGENTS.md starter

```md
# AGENTS.md

**Project:** Demo starter
**Type:** <project-type>
**Architecture:** <chosen-architecture>
**Target:** <target users>

This file defines the repo-wide operating rules for all agents working in this repository.

## 1. Repository Purpose
<what this repo is for>

## 2. Default Tech Stack
- <stack item 1>
- <stack item 2>
- <stack item 3>

## 3. Architecture Rules
- Keep the major boundaries explicit
- Do not bypass domain rules from entry-layer code
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
Choose the correct overlay only if the stack is known.
Create only the minimum files needed for a first successful pass.
Use the canonical lifecycle in order:
adopt -> plan -> architecture -> implement -> review -> verify -> finalize -> memory.

Goal:
- one small feature slice
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

- [Tutorial Hub](./index_EN.md)
- [AGENTS.md and prompt guide](./agents-and-prompts_EN.md)
- the stack tutorial you actually plan to use
