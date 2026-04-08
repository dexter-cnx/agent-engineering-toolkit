---
tags:
  - tutorial
  - multi-agent
  - team
aliases:
  - Agent Team Execution
---

# Multi-Agent Execution

When should work be split across multiple agents?

Short answer:

- when the task spans multiple boundaries
- when the outputs are materially different
- when you want to reduce context overload
- when you need role-specific review

## Recommended structures

```text
Lead Agent
 ├─ Architecture Agent
 ├─ Implementation Agent
 ├─ Review Agent
 └─ Verification Agent
```

Or for product work:

```text
Lead Agent
 ├─ UI Agent
 ├─ Backend Agent
 ├─ QA Agent
 └─ Docs Agent
```

## What the lead agent should do

- accept the top-level request
- decompose it into sub-tasks
- define boundaries for each agent
- define handoff artifacts
- decide what can run sequentially vs in parallel

## What each sub-agent should receive

At minimum:

- task statement
- in-scope
- out-of-scope
- relevant files or areas
- output format
- verification expectation

## Example of a good handoff

```text
Sub-agent: UI Agent

In scope:
- login screen
- form validation UI
- loading/error/success state rendering

Out of scope:
- auth provider integration
- token persistence
- analytics

Output:
- list of UI files to create/change
- implementation summary
- UI-specific verification notes
```

## Common pitfalls

- lead agent does not define out-of-scope
- sub-agents edit overlapping files without coordination
- no handoff artifact
- verification ownership is unclear
- too many agents create overhead

## Rule of thumb

- small task: one agent is enough
- medium task: lead + implementation + verify
- large task: lead + role-based agents + final integrator

## Read alongside

- `docs/agent-team-system.md`
- tutorials under `docs/tutorials/team/`
- [Real workflow: Lead → Architecture → Feature](./03-real-workflow_EN.md)
