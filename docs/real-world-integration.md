# Real-World Integration

This guide explains how the toolkit fits into real project workflows.

## 1. Foundation and consuming repos
This toolkit is the foundation. Real projects consume it either as:
- a central reference repo
- a submodule
- a selected-file copy source

Project-specific rules stay in the consuming repo unless they are broadly reusable.

## 2. Codex workflow
Use `AGENTS.md` as the contract, `docs/prompt-pipeline.md` as lifecycle source of truth, and `docs/agent-team-system.md` as the role model reference.

## 3. Claude Code workflow
Use the same contract and role model, even if one model simulates all roles internally.

## 4. CI/CD workflow
At the foundation level, CI should verify repository structure and canonical docs.
In consuming repos, CI should run project-specific verification commands and report evidence clearly.

## 5. Overlay workflow
Choose one overlay based on the consuming repo’s stack.
Do not mix root foundation policy with stack-specific operating rules.

## 6. Practical rule
Do not claim “done” unless review and verification happened distinctly.
