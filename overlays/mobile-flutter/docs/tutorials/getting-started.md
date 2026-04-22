# Getting Started

## Purpose

Use this overlay end-to-end without prior context. Start here when you need to pick a skill, follow a workflow, and ship a change safely.

## Prerequisites

- Repository checked out locally
- Access to `overlays/mobile-flutter/`
- A clear task goal: new app, new feature, release, or architecture fix

## Exact repository paths

- `overlays/mobile-flutter/README.md`
- `overlays/mobile-flutter/AGENTS.overlay.md`
- `overlays/mobile-flutter/SKILLS_INDEX.md`
- `overlays/mobile-flutter/SKILL_SCHEMA.md`
- `overlays/mobile-flutter/workflows/`
- `overlays/mobile-flutter/examples/`
- `overlays/mobile-flutter/examples/real-world/README.md`
- `overlays/mobile-flutter/templates/`
- `overlays/mobile-flutter/ci/validate_skills.sh`
- `overlays/mobile-flutter/docs/tutorials/app-log-and-production-logging.md`

## Step-by-step instructions

1. Read [README.md](../../README.md) to confirm the overlay purpose.
2. Read [AGENTS.overlay.md](../../AGENTS.overlay.md) to understand the operating rules.
3. Open [SKILLS_INDEX.md](../../SKILLS_INDEX.md) and choose the smallest skill that fits.
4. Open the matching workflow in `../../workflows/` if the task spans more than one skill.
5. Open the linked example and template files before editing code.
6. If you want a concrete end-to-end shape, start with `examples/real-world/README.md`.
7. Make the smallest file change that satisfies the workflow output.
8. Run `bash overlays/mobile-flutter/ci/validate_skills.sh` before handing off the result.

## What skills to use

- Use `SKILLS_INDEX.md` to pick the smallest active skill.
- Use `workflows/new-project/README.md` for a new app.
- Use `workflows/new-feature/README.md` for a feature module.
- Use `docs/tutorials/app-log-and-production-logging.md` for app logging and observability guidance.
- Use `workflows/release-app/README.md` for release readiness.
- Use `workflows/migrate-project/README.md` for legacy refactors.

## Expected inputs

- Task description
- Target repository path
- Feature or app name
- State management choice when relevant
- Platform scope when relevant

## Expected outputs

- Clear skill selection
- Exact file list to change
- Updated docs or templates when needed
- Validation results from the overlay checker

## Common mistakes

- Reading every skill before acting
- Using a workflow when one skill is enough
- Editing code before checking the overlay path
- Skipping the validation command

## Troubleshooting

- If the task is unclear, start with `flutter-clean-architecture-audit`.
- If the project uses GetX, choose the GetX state skill instead of Riverpod.
- If the task touches routing, split route map, redirects, and deep links into separate skills.
- If validation fails, fix the file paths first, then rerun the checker.

## Copy-paste prompt for Claude Code / Codex

```text
Follow overlays/mobile-flutter/AGENTS.overlay.md.
Use overlays/mobile-flutter/SKILLS_INDEX.md to select the smallest active skill.
If the task spans multiple steps, use the matching workflow from overlays/mobile-flutter/workflows/.

Task:
<describe the change>

Deliver:
1. assumptions
2. exact files to update
3. chosen skills
4. implementation plan
5. validation checklist
```

## Thai

ดู `getting-started_TH.md` สำหรับเวอร์ชันภาษาไทยที่ใช้โครงสร้างเดียวกัน
