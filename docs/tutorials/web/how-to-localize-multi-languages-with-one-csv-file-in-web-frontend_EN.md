---
tags:
  - agent-engineering-toolkit
  - tutorial
  - web
  - localization
aliases:
  - Web CSV Localization EN
  - Multi Language CSV in Web Frontend EN
---

# How to Localize Multiple Languages in Web Frontend with One CSV File

Use this tutorial when a web frontend must use one CSV file as the source of truth for multiple languages.

## What to Read

- [Start from a Blank Folder](../00-common-start_EN.md)
- [AGENTS.md and prompt guide](../agents-and-prompts_EN.md)
- [Web Frontend overlay README](../../../overlays/web-frontend/README.md)
- [Web Frontend overlay rules](../../../overlays/web-frontend/AGENTS.overlay.md)

## AGENTS.md Example You Can Use

```md
# AGENTS.md

**Project:** <project-name>
**Type:** Web Frontend
**Architecture:** CSV-first Localization
**Localization:** CSV-first
**Target:** <target users>

This file defines the repo-wide operating rules for all Agent Teams that work in this project.

---

## 1. Repository Purpose

<what this repo is for>

## 2. Default Tech Stack

- <framework>
- <state solution>
- <routing solution>
- CSV localization builder or loader

## 3. Architecture Rules

- CSV is the source of truth
- keep localization setup in the app/bootstrap layer
- do not hardcode translated strings in components

## 4. Workflow

1. Read `AGENTS.md`
2. Read `docs/prompt-pipeline.md`
3. Use the prompts in order
4. Verify key coverage and fallback behavior
5. Update project memory after durable decisions
```

## Example Prompt to Start

```text
Follow AGENTS.md strictly.
Start from a blank folder.
Create a short, practical repo-root AGENTS.md.
Choose the web-frontend overlay.
Use a CSV localization workflow.
Use the prompt pipeline in order and verify translation coverage.
```

## Start from a Blank Folder

1. Create the project folder.
2. Initialize git.
3. Add the toolkit and project memory.
4. Add `AGENTS.md`.
5. Choose the `web-frontend` overlay.
6. Decide how CSV will become locale assets.
7. Create the web structure and localization folder.
8. Add a script to generate or validate translation files.
9. Verify key coverage and fallback behavior.
10. Save memory about naming and fallback.

Example bootstrap:

```bash
mkdir web-csv-localization
cd web-csv-localization
git init
git submodule add <toolkit-repo-url> toolkit
mkdir -p project_memory src/i18n tool
cp toolkit/templates/project_memory/decisions.md project_memory/decisions.md
cp toolkit/templates/project_memory/known_constraints.md project_memory/known_constraints.md
cp toolkit/templates/project_memory/patterns.md project_memory/patterns.md
```

## Suggested CSV Shape

Keep one file as the source of truth, for example:

```text
key,en,th,ja
nav.home,Home,หน้าหลัก,ホーム
cta.save,Save,บันทึก,保存
```

Keep these rules:

- `key` values must be stable and meaningful
- each column is one locale
- generated files are outputs, not the source of truth
- the CSV must be a shared contract for the team

## Prompts to Use

| Stage | Prompt | Skill to Consider | Output |
| --- | --- | --- | --- |
| Adopt | `prompts/adoption/adopt_toolkit_in_repo.md` | `skills/skill-router/README.md` | adoption path and overlay |
| Plan | `prompts/planning/plan_change.md` | `skills/risk-scoring/README.md` | facts, assumptions, risks, phases |
| Architecture | `prompts/design/architecture_review.md` | `skills/architecture-review/README.md` + `skills/dependency-review/README.md` | localization boundary, file placement, package choice |
| Implement | `prompts/implementation/implement_change.md` | `skills/safe-refactor/README.md` | CSV, generator, generated assets |
| Review | `prompts/review/review_change.md` | `skills/docs-update/README.md` | string coverage and boundary clarity |
| Verify | `prompts/verification/verification_pass.md` | `skills/verification-pass/README.md` | key coverage, fallback checks, evidence |
| Finalize | `prompts/finalization/finalize_change.md` | `skills/docs-update/README.md` | final summary and follow-ups |
| Memory | `prompts/memory/update_project_memory.md` | none | durable localization rules |

## Skills to Read

- `skills/skill-router/README.md`
- `skills/risk-scoring/README.md`
- `skills/architecture-review/README.md`
- `skills/dependency-review/README.md`
- `skills/safe-refactor/README.md`
- `skills/docs-update/README.md`
- `skills/verification-pass/README.md`

## Scripts to Keep in the Consuming Repo

There is no shared toolkit script for this. Create repo-local commands such as:

```bash
npm run i18n:build
npm run lint
npm run build
```

If you add CSV validation, include a command like this:

```bash
npm run i18n:validate
```

## Suggested Web Frontend Shape

Separate these responsibilities clearly:

- CSV source
- generator script
- generated locale assets
- runtime localization loader
- fallback language handling

## Pitfalls

- letting generated files become the source of truth
- drifting keys across languages
- hardcoding strings in components without a localization layer
- not testing fallback language behavior

## Verification

- check that the CSV contains all keys for every locale
- check that generation does not drop keys
- run `npm run lint`
- run `npm run build`
- run the CSV validation command if you add one

## Memory Notes

Store durable decisions about:

- CSV shape
- key naming convention
- fallback language
- the script used to generate or validate localization files
