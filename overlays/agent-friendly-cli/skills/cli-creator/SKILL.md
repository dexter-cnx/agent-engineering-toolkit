---
name: cli-creator
description: Build or refine a reusable agent-friendly CLI with compact output, structured modes where practical, setup checks, read-first flow, and companion skill support.
---

# Purpose

Use this skill when repeated repository work should be turned into a reusable CLI instead of being solved with ad hoc shell commands.

## Best-fit cases

- CI or build investigation
- report export
- API-backed search and read
- architecture validation
- localization generation
- changelog drafting
- local archive inspection

# Principles

Design for repeated agent use.

The CLI should be:

- non-interactive by default
- compact by default
- machine-readable where practical
- explicit about setup and auth
- clear about discovery versus exact read
- able to export large results to files
- safe by default
- separated into read versus write paths

# Recommended command shape

Use this structure unless the repository clearly needs something else:

- `<cli> doctor`
- `<cli> auth status`
- `<cli> search ...`
- `<cli> list ...`
- `<cli> read <id>`
- `<cli> export ...`
- `<cli> download ...`
- `<cli> draft ...`
- `<cli> write ...`

Recommended flags:
- `--json`
- `--limit`
- `--output`
- `--dry-run`

# Required workflow

1. inspect repository conventions
2. propose the command surface before implementation
3. keep defaults small
4. implement discovery output compactly
5. require stable IDs for exact reads
6. route large outputs to files
7. keep live writes separate
8. add or update a companion skill
9. verify the CLI from outside the source directory

# Deliverable format

Return:

1. assumptions
2. proposed command surface
3. files to create or update
4. implementation summary
5. verification proof
6. companion skill content
7. shortest future invocation prompt

# Anti-patterns

Avoid:

- interactive prompts
- giant stdout dumps
- mixed read and write behavior
- hidden state with no way to inspect it
- vague setup failures
- undocumented install paths