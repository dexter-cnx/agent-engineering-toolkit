# Real-World Integration

This guide explains how the toolkit fits into real project workflows.

## 1. Foundation and consuming repos
This toolkit is the foundation. Real projects consume it either as:
- a central reference repo
- a submodule
- a selected-file copy source

Project-specific rules stay in the consuming repo unless they are broadly reusable.

## 2. Codex workflow
Recommended pattern:
1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Read the canonical guide
4. Choose an overlay if needed
5. Run the task through plan, design, implementation, review, verification, finalization, and memory
6. Use `docs/codex-review-prompt.md` for strict auditing

## 3. Claude Code workflow
Recommended pattern:
- LEAD frames the task
- ARCHITECT defines structure
- BUILDER implements
- REVIEWER critiques
- VERIFIER validates
- FINALIZER packages
- MEMORY stores durable context

Use the role model even if one model simulates all roles internally.

## 4. CI/CD workflow
At the foundation level, CI should at least verify repository structure and canonical docs.
In consuming repos, CI should run project-specific verification commands and report evidence clearly.

## 5. Overlay workflow
Choose one overlay based on the consuming repo’s stack.
Do not mix root foundation policy with stack-specific operating rules.

## 6. Practical rule
Do not claim “done” unless review and verification happened distinctly.
That rule matters in real projects more than in toy demos.
