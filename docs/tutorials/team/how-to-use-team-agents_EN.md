---
tags:
  - agent-engineering-toolkit
  - tutorial
  - agents
  - team
  - obsidian
aliases:
  - How to Use Team Agents EN
  - Team Agents Workflow EN
---

# How to Use Team Agents

Use this tutorial when you want Codex or Claude to work with explicit roles instead of acting like one undifferentiated assistant.

## Core Idea

1. LEAD frames the task and orders the work.
2. ARCHITECT defines boundaries and structure.
3. BUILDER does the implementation.
4. REVIEWER checks quality and risk.
5. VERIFIER checks real evidence.
6. FINALIZER packages the result.
7. MEMORY records durable decisions.

## Before You Start

1. The repo has an `AGENTS.md`.
2. You have `docs/prompt-pipeline.md`.
3. You have `docs/agent-team-system.md`.
4. You know whether the task is small or large.
5. You know whether you will use Codex, Claude, or both.

## AGENTS.md Example You Can Use

```md
# AGENTS.md

**Project:** <project-name>
**Type:** <platform/project-type>
**Architecture:** <chosen-architecture>
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Canonical References

- docs/prompt-pipeline.md
- docs/agent-team-system.md

## 3. Role Rules

- LEAD handles framing and sequencing
- ARCHITECT handles boundaries and interfaces
- BUILDER handles implementation
- REVIEWER handles critique
- VERIFIER handles evidence
- FINALIZER handles packaging
- MEMORY handles durable notes

## 4. Workflow

1. Read this file.
2. Use the lifecycle prompts in order.
3. Keep review and verification separate.
4. Update project memory after durable decisions.
```

## Example Prompt to Start

```text
Follow AGENTS.md strictly.
Use the team-agent workflow from docs/agent-team-system.md.
Start as LEAD and restate the task.
Then switch to ARCHITECT for boundaries.
Use BUILDER, REVIEWER, VERIFIER, FINALIZER, and MEMORY in order.
Keep each role's output separate.
```

## Example Prompts by Role

### LEAD

```text
Act as LEAD.
Restate the task, list assumptions, identify constraints, and sequence the next steps.
Do not implement yet.
```

### ARCHITECT

```text
Act as ARCHITECT.
Define boundaries, interfaces, layering, and the main structural risks.
Return the safest structure before implementation starts.
```

### BUILDER

```text
Act as BUILDER.
Implement only what the plan and architecture approved.
List files changed and call out deviations.
```

### REVIEWER

```text
Act as REVIEWER.
Critique correctness, readability, maintainability, and hidden risk.
Separate blocking issues from non-blocking issues.
```

### VERIFIER

```text
Act as VERIFIER.
State what was actually checked, what evidence exists, and what remains uncertain.
Do not claim checks that were not run.
```

### FINALIZER

```text
Act as FINALIZER.
Package the result clearly and keep the handoff concise.
```

### MEMORY

```text
Act as MEMORY.
Capture only durable decisions, constraints, patterns, and reminders.
```

## Using It with Codex

- Good for tasks that need repo reading, file edits, and command checks
- Prefer one prompt per role instead of stuffing all roles into a single prompt
- For large tasks, use this sequence: LEAD -> ARCHITECT -> BUILDER -> REVIEWER -> VERIFIER -> FINALIZER -> MEMORY

## Using It with Claude

- Use the same role sequence as Codex
- If you work in a single thread, make role switches explicit
- Keep review and verification separate
- Have Claude respect the same `AGENTS.md` and prompt pipeline

## Recommended Workflow

1. Use LEAD to summarize the task.
2. Use ARCHITECT to define boundaries.
3. Use BUILDER to do the work.
4. Use REVIEWER to find risks.
5. Use VERIFIER to check evidence.
6. Use FINALIZER to package the result.
7. Use MEMORY to save what matters.

## Pitfalls

- skipping LEAD and jumping straight into implementation
- letting one role do everything in one pass
- mixing review and verification
- forgetting to update memory after a durable decision

