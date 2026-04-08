# Scaffold Overlay

## Role
Act as **ARCHITECT** and **BUILDER**.

## Goal
Create or significantly improve an overlay for a specific stack, extending the foundation without redefining it.

## When to use
- adding a new stack overlay
- expanding a thin overlay to production quality
- aligning an overlay with updated foundation rules

## Inputs
- stack identity
- current overlay state, if any
- foundation rules from `AGENTS.md`
- relevant examples or benchmark overlays

## Process
1. Define the stack identity explicitly.
2. Specify stack-specific architecture rules.
3. Map a recommended directory structure with responsibilities.
4. Define stack-specific verification commands.
5. Write review guidance with rejection criteria.
6. Add memory guidance for recurring stack-specific decisions.
7. Create or update `AGENTS.overlay.md`.
8. Create or update `README.md`.
9. Add at least one worked example.

## Required output
- updated `AGENTS.overlay.md`
- updated overlay `README.md`
- verification command examples
- review rejection criteria
- worked example summary or file target

## Non-goals
- rewriting the foundation identity
- adding project-specific rules that belong in the consuming repo
- covering every possible stack variation
