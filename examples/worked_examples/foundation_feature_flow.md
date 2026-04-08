# Worked Example — Foundation Feature Flow

## Scenario
A repository wants to add a new "account preferences" capability, but the foundation toolkit should remain stack-agnostic.

This example demonstrates how to use the toolkit lifecycle **before** choosing a stack-specific overlay.

## Step 1 — Plan
Use `prompts/plan_change.md`.

Expected output:
- precise task restatement
- facts vs assumptions
- risks
- proposed phases
- recommendation on whether an overlay is needed

Example conclusion:
- the work is not trivial
- architecture review is required
- a stack-specific overlay will be chosen by the consuming repo, not by the foundation

## Step 2 — Architecture
Use `prompts/architecture_review.md`.

Expected output:
- affected boundaries
- proposed responsibilities
- dependency direction
- implementation guardrails

Foundation-safe architecture statement:
- keep transport concerns, business logic, persistence, and external integrations separated
- let the consuming repo map those responsibilities into stack-specific files and modules

## Step 3 — Implement
Use `prompts/implement_change.md`.

Expected output:
- artifacts changed in the consuming repo
- no deviation from the agreed structure without explanation
- notes for review

## Step 4 — Review
Use `prompts/review_change.md`.

Expected output:
- strengths
- blocking issues
- non-blocking issues
- architecture fit assessment

## Step 5 — Verify
Use `prompts/verification_pass.md`.

Expected output:
- checks performed
- evidence
- remaining uncertainty
- confidence level

## Step 6 — Finalize
Use `prompts/finalize_change.md`.

Expected output:
- final summary
- deliverable readiness
- follow-ups
- memory-update handoff

## Step 7 — Memory
Use `prompts/update_project_memory.md`.

Store only durable notes such as:
- boundary decisions
- approved patterns
- constraints that future work must preserve

## Why this example belongs in foundation
This example demonstrates the lifecycle and role model without assuming Python, Flutter, Node, or any concrete framework.
