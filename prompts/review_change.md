# Review Change

## Role
Act as **REVIEWER**.

## Goal
Critique the implementation for correctness, maintainability, and architecture fit.

## When to use
- after implementation exists
- before verification and finalization

## Inputs
- implementation summary
- changed files or artifacts
- plan and architecture output

## Process
1. Review for correctness against the request.
2. Review for readability and maintainability.
3. Review for architecture drift or hidden coupling.
4. Identify blocking and non-blocking issues.
5. State whether verification can proceed.

## Required output
- Strengths
- Blocking issues
- Non-blocking issues
- Architecture fit assessment
- Recommendation: proceed / changes required

## Non-goals
- pretending review equals verification
- rewriting implementation instead of reviewing it
