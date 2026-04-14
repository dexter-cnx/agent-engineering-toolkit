---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - safety
aliases:
  - CLI Dry Run Versus Write
---

# Dry-Run Versus Write

Use this pattern when the CLI can mutate state.

## Scenario

A command can change repository state, remote state, or generated artifacts.
That command should make the preview path obvious and separate from the live
write path.

## Safe flow

1. Inspect the current state.
2. Produce a draft or dry-run preview.
3. Review the preview output.
4. Apply the live write only if the user explicitly asked for it.

## Example commands

```bash
mycli draft --json
mycli write --dry-run --json
mycli write --json
```

## Example output

```text
$ mycli draft --json
{
  "action":"archive",
  "target":"item-184",
  "changes":["set status=archived","move to archive index"]
}

$ mycli write --dry-run --json
Dry run only. No changes applied.
Would archive item-184 and update 2 related records.

$ mycli write --json
Applied: archived item-184
Updated 2 related records
```

## Good behavior

- `draft` or `--dry-run` shows intended changes without applying them
- the preview output is compact and machine-readable
- the live write is a separate command or a clearly separate mode
- error messages explain what is missing before mutation is attempted

## Bad behavior

- a read command that silently mutates state
- a write command without any preview path
- mutation triggered by default because a flag was omitted
- large diffs printed inline when a file output would be better

## Short future prompt

Use `draft` or `--dry-run` first, review the result, then run the live write
only when mutation is explicitly requested.
