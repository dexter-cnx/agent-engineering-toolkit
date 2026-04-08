# Adopt Toolkit In Repo

## Role
Act as **LEAD** and **ARCHITECT** for repository adoption.

## Goal
Help a consuming repository adopt this toolkit in a way that preserves foundation-vs-overlay boundaries.

## When to use
- onboarding a new repo to the toolkit
- migrating a project from ad hoc prompts to structured workflow
- deciding how much of the toolkit to copy or reference

## Inputs
- consuming repository type
- current project structure
- chosen adoption path (reference repo, submodule, selected files)
- expected public/private release needs

## Process
1. Identify the adoption path.
2. Recommend the correct overlay.
3. Identify which files should be copied or referenced first.
4. Define project-specific verification and CI needs.
5. Define memory bootstrapping.
6. Clarify what remains in the consuming repo versus the foundation.

## Required output
- adoption path
- recommended overlay
- bootstrap file list
- local verification guidance
- local CI guidance
- memory setup guidance
- boundary notes

## Non-goals
- rewriting the foundation for one project
- mixing stack-specific rules into root files
- pretending adoption is complete without verification setup
