---
tags:
  - tutorial
  - mental-model
  - agents
aliases:
  - Agent Thinking
---

# Agent System Mental Model

This toolkit becomes much easier to use once you stop thinking of it as one giant prompt.

This tutorial explains the layers.

## The distinctions that matter

### 1. Agent
An agent is a role-based worker, not just a text generator.

It should have:

- a scope
- operating rules
- a decision order
- an output shape

### 2. Prompt
A prompt is an instruction for one stage, not the whole system.

Examples:

- adopt
- plan
- architecture
- implement
- review
- verify
- finalize
- memory

### 3. Skill
A skill is a focused capability that should be pulled in only when needed.

Examples:

- architecture review
- repo audit
- safe refactor
- docs update

Skills should not be invoked automatically for every task if they are not relevant.

### 4. Overlay
An overlay is the specialization layer for a stack or platform.

Examples:

- mobile-flutter
- web-frontend
- backend-node
- python-service

The foundation toolkit should not quietly become a Flutter repo.
Stack-specific assumptions belong in overlays or in the consuming repo.

### 5. Project Memory
Project memory exists for durable cross-task facts, such as:

- architecture decisions
- known constraints
- agreed patterns

It is not a place to store every log line.

## The model to keep in your head

```text
User Request
  ↓
AGENTS.md
  ↓
Prompt Pipeline
  ↓
Overlay Selection
  ↓
Optional Skills
  ↓
Verification
  ↓
Project Memory Update
```

## Core ideas

### Do not start with implementation
Start with boundaries.

### Do not assume one prompt is enough
Real work is staged.

### Do not mix stack-specific rules into foundation
That creates drift and hurts reuse.

### Do not memorize everything
Memory should store durable decisions only.

## Short checklist before work starts

- what is this repo
- which overlay applies
- what are the architecture boundaries
- which extra skills are needed, if any
- how will verification happen
- what should be remembered after the work is done

## Read next

- [Real workflow: Lead → Architecture → Feature](./03-real-workflow_EN.md)
- [Debug failed agent runs](./06-debugging-agent-runs_EN.md)
- [Multi-agent execution](./07-multi-agent-execution_EN.md)
