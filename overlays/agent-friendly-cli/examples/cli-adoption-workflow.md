---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - adoption
aliases:
  - CLI Adoption Workflow
---

# CLI Adoption Workflow

Use this pattern when a repository has a recurring task that is currently being
solved with ad hoc shell commands.

## Scenario

A team keeps running the same repository task by hand:

- checking environment health
- listing candidate items
- reading one item in detail
- exporting a large report

That flow should become a reusable CLI instead of a one-off script.

## Plan

1. Read the existing CLI contract or companion skill.
2. Propose the command surface before implementation.
3. Keep defaults compact and non-interactive.
4. Separate discovery from exact reads.
5. Add a file-backed export path for large outputs.
6. Keep writes behind draft or dry-run first.
7. Verify the command from outside the source directory.

## Proposed command surface

Example CLI:

```bash
mycli doctor
mycli auth status
mycli search --json --limit 20
mycli read <id> --json
mycli export --output artifacts/report.json --json
mycli draft --json
mycli write --dry-run
```

## Example output

```text
$ mycli doctor
OK  mycli 1.4.0
Config  ~/.config/mycli/config.json
Auth    ready

$ mycli search --json --limit 20
[
  {"id":"item-184","title":"Release 2026-04 audit","status":"open","age":"2h"},
  {"id":"item-191","title":"Release 2026-04 export","status":"queued","age":"5h"}
]

$ mycli read item-184 --json
{"id":"item-184","title":"Release 2026-04 audit","owner":"platform","summary":"Review pending exports and mark the final report path."}

$ mycli export --output artifacts/report.json --json
Exported 24 records to artifacts/report.json
Complete: yes
```

## Good result shape

- `doctor` confirms installation and dependencies.
- `auth status` explains whether credentials are ready.
- `search` returns compact candidate records.
- `read <id>` returns exact details for one stable identifier.
- `export` writes a file and reports the saved path.
- `draft` or `--dry-run` shows the intended mutation without applying it.

## What to watch for

- interactive prompts in routine flows
- huge JSON dumped directly to stdout
- discovery commands that hide IDs
- writes that happen as part of a read command

## Short future prompt

Use the repository CLI first. Start with `doctor`, then discovery, then exact
read, then export, and stop at `draft` or `--dry-run` unless live write was
explicitly requested.
