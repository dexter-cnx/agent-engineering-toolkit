---
tags:
  - tutorial
  - debugging
  - verification
aliases:
  - Failed Agent Runs
---

# Debug Failed Agent Runs

Even with good tutorials, some agent runs will still go sideways.

This page shows how to diagnose the problem systematically.

## Common failure modes

### 1. Scope drift
You asked for login, but the AI also changed routing, theme, and folder structure.

### 2. Hallucinated files
The AI refers to files or scripts that do not exist.

### 3. Fake verification
It claims everything passed even though nothing was actually run.

### 4. Architecture leakage
UI talks directly to network or storage.

### 5. Weak review stage
The review says “looks good” without inspecting actual issues.

## Layered debugging approach

### Layer 1: Check AGENTS.md
Ask:

- is repo identity explicit
- are boundaries explicit
- does the workflow force verification
- are stack-specific rules sufficient

If AGENTS.md is vague, drift becomes more likely.

### Layer 2: Check whether the prompt collapsed stages
If one prompt tries to plan, design, implement, review, and verify at once, accuracy drops quickly.

### Layer 3: Check whether architecture was skipped
If a task touches boundaries and there was no architecture stage, leakage becomes likely.

### Layer 4: Inspect the verification output
A good verify stage says three things:

- what was checked
- what was not checked
- what still requires human or CI validation

### Layer 5: Check for memory pollution
If project memory stores too much temporary detail, the agent may over-reference stale material.

## Useful recovery prompts

### For scope drift

```text
Stop expanding scope.

Re-state the approved task in one paragraph.
List out-of-scope items explicitly.
Continue only with the approved files and boundaries.
```

### For untrustworthy verification

```text
Redo the verification pass.
Only claim checks that were actually performed.
Separate:
- verified
- not verified
- requires human or CI verification
```

### For boundary leakage

```text
Review the implementation for architecture leakage.
Identify every place where presentation, domain, and data boundaries were crossed.
Propose the smallest corrective refactor.
```

## Important rule

When work breaks, do not always restart from zero.
Often you only need to roll back one stage, such as:

- from implement back to architecture
- from finalize back to verify
- from review back to implement

## What success looks like

If you can debug from stages and boundaries instead of guessing, the workflow is becoming mature.
