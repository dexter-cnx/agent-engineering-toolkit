---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - operator
aliases:
  - CLI Operator Workflow
---

# CLI Operator Workflow

Use this pattern when a reusable CLI already exists and should be used before
falling back to shell commands.

## Scenario

You need to inspect a repository task without mutating anything yet.

## Execution order

1. Read the CLI contract and companion skill.
2. Run `doctor`.
3. Run `auth status` if the workflow depends on credentials.
4. Run `search` or `list`.
5. Run `read <id>` on one stable identifier.
6. Run `download` or `export` if you need a large artifact.
7. Stop before `draft` or `--dry-run` for write flows unless mutation was
   explicitly requested.

## Example session

```bash
mycli doctor
mycli auth status
mycli search --limit 10 --json
mycli read item-184 --json
mycli export item-184 --output artifacts/item-184.json --json
```

## Example output

```text
$ mycli doctor
OK  mycli 1.4.0
Config  ~/.config/mycli/config.json
Auth    ready

$ mycli auth status
Authenticated as build-bot
Token expires in 14 days

$ mycli search --limit 10 --json
[
  {"id":"item-184","title":"Release 2026-04 audit","status":"open"},
  {"id":"item-191","title":"Release 2026-04 export","status":"queued"}
]

$ mycli read item-184 --json
{"id":"item-184","title":"Release 2026-04 audit","owner":"platform","updatedAt":"2026-04-14T08:30:00Z"}

$ mycli export item-184 --output artifacts/item-184.json --json
Saved item-184 to artifacts/item-184.json
Bytes written: 4821
```

## Expected behavior

- stdout stays compact
- the search step gives enough data to choose one ID
- the read step returns exact details for that ID
- the export step writes a file and reports the path

## Common mistakes

- jumping straight to a write command
- using a discovery command that prints too much
- relying on hidden state instead of an inspectable command
- mixing read and write behavior in one command

## Short future prompt

Use the existing repository CLI first. Follow doctor, auth status if relevant,
discovery, exact read, and export. Do not perform live writes by default.
