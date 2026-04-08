# Tutorial (English) — Step-by-Step Training Guide

This tutorial shows one concrete first run from start to finish.

## Goal
By the end of this tutorial, you should be able to:
- choose the right overlay
- move a request through the canonical lifecycle
- keep stack-specific rules out of the foundation
- write a durable memory note after the work is done

## Scenario
A consuming repository wants to add an account preferences capability.

Use the foundation toolkit as the workflow spine, then select the appropriate overlay in the consuming repo.

## Step 1 — Read the minimum set
Read these files first:
1. `README.md`
2. `AGENTS.md`
3. `docs/how-to-use.md`
4. `docs/architecture.md`
5. `docs/overlays.md`
6. `docs/agent-team-system.md`
7. `docs/prompt-pipeline.md`

## Step 2 — Choose the adoption path
Pick one:
- central toolkit repo
- submodule in a real project
- copy selected files

For a real repo, the most common path is:
```bash
git submodule add <toolkit-repo-url> toolkit
```

## Step 3 — Choose an overlay
Read the overlay that matches the consuming repo:
- `overlays/mobile-flutter/README.md`
- `overlays/backend-node/README.md`
- `overlays/web-frontend/README.md`
- `overlays/python-service/README.md`

If none fit, stay foundation-only and keep stack-specific rules in the consuming repo.

## Step 4 — Plan the change
Run the planning prompt with this output shape:
- task restatement: add account preferences capability
- facts: the repository is adopting the toolkit as a foundation
- assumptions: the stack is known only after overlay selection
- constraints: root stays stack-agnostic
- risks: boundary leakage, vague ownership, missing verification
- next prompt: architecture review

## Step 5 — Define the structure
Architecture output should name the layers clearly.

Example structure for a consuming repo:
- transport layer: route, handler, or controller file
- orchestration layer: service or use-case file
- persistence layer: repository or data-access file
- adapter layer: external provider boundary

Builder guardrails:
- do not put business rules in transport code
- do not call external providers directly from unrelated modules
- keep response shaping out of repositories

## Step 6 — Implement
The builder changes the consuming repo artifacts.

Expected implementation notes:
- files changed: transport, service, repository, and adapter layers
- deviations: only if the architecture review approved them

## Step 7 — Review
The reviewer should separate strengths from problems.

Example review outcome:
- strength: handlers stay thin
- blocking issue: repository contains business logic
- non-blocking issue: example coverage is missing
- architecture fit: acceptable only after the blocking issue is fixed

## Step 8 — Verify
Verification must name the checks that were actually run.

Example checks:
```bash
bash scripts/check-public-repo.sh
```

If you are checking this toolkit repository, run the public-repo gate.
In a consuming repo, run the local stack checks too, such as lint, tests, or startup sanity.

Example verification summary:
- checks performed: public-repo gate, local tests, startup sanity
- evidence: command output and changed files
- remaining uncertainty: integration coverage is not yet complete
- confidence: medium or high, depending on the evidence

## Step 9 — Finalize
The finalizer should package the result clearly.

Example final summary:
- account preferences capability was added with clear boundaries
- review and verification stayed distinct
- remaining follow-up: add one integration test

## Step 10 — Update memory
Record only durable notes.

Example memory entries:
- account preference handlers must stay thin
- response shaping belongs outside repositories
- the chosen overlay for this repo is `<chosen-overlay>`

## Optional helper
If you want a local bootstrap helper, use the script that copies project memory templates and adds the submodule:
```bash
bash scripts/bootstrap-project-memory.sh
```
