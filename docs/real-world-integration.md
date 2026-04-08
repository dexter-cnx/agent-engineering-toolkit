# Real-World Integration

This guide explains how the toolkit fits into real project workflows.

## 1. With Codex
Use `AGENTS.md` as the root contract and `docs/prompt-pipeline.md` as the lifecycle source of truth.

Recommended flow:
1. Read `AGENTS.md`
2. Read the canonical guide
3. Choose an overlay if needed
4. Execute a task through the lifecycle
5. Update memory when durable decisions are made

## 2. With Claude Code
Use the role model in `agent_team/`.
A strong default flow is:
- LEAD frames the task
- ARCHITECT defines structure
- BUILDER implements
- REVIEWER critiques
- VERIFIER validates
- FINALIZER packages the result
- MEMORY stores durable notes

## 3. With CI/CD
CI should validate repository structure and, in consuming repos, the project-specific verification commands.
Do not claim work is complete if verification has not happened.

## 4. With submodules
This repo works well as a central toolkit consumed from real repositories.
Keep project-specific rules in the consuming repo.
Move something back to foundation only if it is broadly reusable.

## 5. With AI runtime diversity
The foundation can be consumed by multiple AI coding tools.
That is acceptable at the foundation layer because these references describe usage surfaces, not framework identity.
