---
tags:
  - tutorial
  - workflow
  - lead-agent
aliases:
  - Lead to Feature
---

# Real Workflow: Lead → Architecture → Feature

This tutorial answers one of the most common questions:

> In real work, do I start with lead/planning, then architecture, then feature work?

In most cases, yes.
More importantly, each stage should produce something concrete for the next stage to consume.

## Recommended workflow shape

```text
Request
  ↓
Lead / Planning
  ↓
Architecture / Boundary Review
  ↓
Implementation
  ↓
Review
  ↓
Verification
  ↓
Finalize
  ↓
Memory
```

## Stage 1: Lead / Planning

Goal:

- turn the request into a plan
- break down scope
- identify risks
- propose files likely to change

Example prompt:

```text
Read AGENTS.md first.
Use the planning stage of the canonical lifecycle.

Task:
Add an account preferences capability to the consuming repo.

Need:
- scope breakdown
- architecture impact
- files likely to change
- risks
- recommended order of implementation

Do not implement yet.
```

Expected output:

- size of the task
- dependencies
- whether it should be split
- risky parts

## Stage 2: Architecture

Goal:

- decide boundaries
- prevent leakage
- choose adapters and abstractions
- settle state, routing, or persistence decisions where needed

Example prompt:

```text
Read AGENTS.md first.
Use the architecture stage of the canonical lifecycle.

We already have the plan.
Review the boundary for the account preferences capability.

Decide:
- entry/domain/data split or the equivalent layers in this repo
- provider abstraction boundary
- navigation or handoff impact
- state management impact
- testing and verification expectations

Do not implement yet.
```

Expected output:

- boundary decisions
- guardrails
- explicit non-goals

## Stage 3: Implement

Goal:

- create or change files according to plan
- stay inside the agreed boundaries
- avoid scope expansion

Example prompt:

```text
Read AGENTS.md first.
Use the implementation stage of the canonical lifecycle.

Implement the approved account preferences capability.
Stay within the agreed boundaries.
Do not add unrelated improvements.
```

## Stage 4: Review

Goal:

- find mistakes
- find over-engineering
- catch leakage or missing verification

## Stage 5: Verify

Goal:

- say what was checked
- say what was not checked
- never pretend something passed if it was not actually run

## Stage 6: Finalize + Memory

Goal:

- produce a handoff-ready summary
- record only durable decisions

## Workflow shapes to avoid

### One giant prompt
Planning, design, coding, review, and verification all in one step.
This is hard to inspect and easy to derail.

### Skipping architecture
Only acceptable for trivial tasks.
If the work touches boundaries, add the architecture stage.

### No review and no verify
This feels faster but makes quality random.

## Rule of thumb

- very small task: plan + implement + verify may be enough
- boundary-touching task: include architecture
- multi-system task: use multi-agent execution or at least explicit sub-tasking

## Read next

- [Build a production feature](./04-build-production-feature_EN.md)
- [Multi-agent execution](./07-multi-agent-execution_EN.md)
