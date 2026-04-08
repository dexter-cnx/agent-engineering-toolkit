---
tags:
  - tutorial
  - flutter
  - full-example
aliases:
  - Flutter End to End Example
---

# Full Example: Flutter Project

This page ties the toolkit together for one realistic Flutter adoption path.

## Example scenario

You have a blank repo and want a Flutter app with:

- clean architecture
- explicit state management
- explicit routing
- explicit localization
- one first feature that can be verified

## Recommended path

### Phase 1: Bootstrap
Use:

- [Start from Blank Folder](./00-common-start_EN.md)
- [10-minute golden path](./01-golden-path_EN.md)

Goal:
- initialize the repo
- add the toolkit
- create AGENTS.md
- choose the `mobile-flutter` overlay
- prepare project memory

### Phase 2: Mental model + workflow
Use:

- [Agent system mental model](./02-agent-mental-model_EN.md)
- [Real workflow: Lead → Architecture → Feature](./03-real-workflow_EN.md)

Goal:
- understand the stages
- avoid one-shot prompting

### Phase 3: Flutter-specific build
Use the tutorials under `docs/tutorials/flutter/`

Start with:
- basic Flutter app
- clean architecture + Riverpod / GetX / BLoC
- localization
- DESIGN.md integration as needed

### Phase 4: First production feature
Use:
- [Build a production feature](./04-build-production-feature_EN.md)

Choose a first feature that is small but meaningful, such as:
- login
- profile
- settings
- onboarding

### Phase 5: Multi-agent as complexity grows
Use:
- [Multi-agent execution](./07-multi-agent-execution_EN.md)

For example:
- UI agent
- state/domain agent
- backend integration agent
- QA / verification agent

### Phase 6: Debug and stabilize the workflow
Use:
- [Debug failed agent runs](./06-debugging-agent-runs_EN.md)

## Prompt starter for a new Flutter repo

```text
We are starting from a blank folder for a Flutter app.

Read AGENTS.md first.
Adopt the toolkit into this repository.
Choose the mobile-flutter overlay.
Create a short but production-usable AGENTS.md.
Set up project memory.
Use the canonical lifecycle in order.

Initial goal:
- production-shaped Flutter project structure
- explicit architecture boundaries
- chosen state management and routing
- one small verified feature
- no unnecessary extras
```

## Expected outcome

- a Flutter repo with clear boundaries
- a tutorial path that a new team can follow
- predictable prompt usage
- verification discipline
- memory discipline
