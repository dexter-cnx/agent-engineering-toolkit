# Real-World Integration

This guide explains how the toolkit fits into real project workflows.

## 1. Foundation and consuming repos
This toolkit is the foundation. Real projects consume it either as:
- a central reference repo
- a submodule
- a selected-file copy source

Project-specific rules stay in the consuming repo unless they are broadly reusable.

## 2. AI coding tool workflow
Use `AGENTS.md` as the contract, `docs/prompt-pipeline.md` as the lifecycle source of truth, and `docs/agent-team-system.md` as the role model reference.

Tooling differences only change how you deliver that contract:
- if the tool supports persistent instructions, keep the contract there
- if the tool works best from a pasted prompt, start with the same contract in the first turn
- if the tool can simulate roles internally, still keep the lead/architect/builder/reviewer/verifier/finalizer/memory sequence visible

## 3. CI/CD workflow
At the foundation level, CI should verify repository structure and canonical docs.
In consuming repos, CI should run project-specific verification commands and report evidence clearly.

## 4. Overlay workflow
Choose one overlay based on the consuming repo’s stack.
Do not mix root foundation policy with stack-specific operating rules.

## 5. Practical rule
Do not claim “done” unless review and verification happened distinctly.
