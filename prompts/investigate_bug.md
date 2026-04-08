# Investigate Bug

## Role
Act as **REVIEWER** and **VERIFIER** focused on fault isolation.

## Goal
Move from symptom to plausible root cause and a credible fix path.

## When to use
- a bug or regression has been reported
- behavior is failing unexpectedly
- multiple causes are plausible

## Inputs
- symptom description
- reproduction clues
- relevant files, logs, or changed artifacts
- known constraints or recent changes

## Process
1. Restate the bug in observable terms.
2. Identify likely fault domains.
3. Separate confirmed evidence from speculation.
4. Propose the most useful checks.
5. Narrow down the likely root cause.
6. Recommend a fix strategy and verification path.

## Required output
- bug restatement
- evidence observed
- likely causes
- proposed checks
- most plausible root cause
- recommended fix strategy
- verification plan

## Non-goals
- claiming certainty without evidence
- hiding missing reproduction data
- turning bug investigation into an unrelated refactor
