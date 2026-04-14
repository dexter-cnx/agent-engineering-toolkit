---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - verification
aliases:
  - CLI Verification Checklist
---

# Verification Checklist

Use this checklist to prove that a CLI is actually reusable by agents.

## Required checks

1. The command resolves from outside the source folder.
2. Help output is understandable.
3. `doctor` is available and useful.
4. `auth status` is available when relevant.
5. A discovery flow works.
6. An exact read flow works.
7. A large output export writes to a file.
8. Live write is not triggered implicitly.

## Example proof

```bash
cd /tmp
mycli --help
mycli doctor --json
mycli search --limit 5 --json
mycli read item-184 --json
mycli export --output /tmp/artifact.json --json
```

## Example result

```text
$ cd /tmp
$ mycli --help
Usage: mycli <command> [options]

$ mycli doctor --json
{"status":"ok","config":"~/.config/mycli/config.json","auth":"ready"}

$ mycli export --output /tmp/artifact.json --json
Exported 5 records to /tmp/artifact.json
Complete: yes
```

## What good looks like

- each command has a clear and narrow purpose
- failures explain what to fix
- search output helps pick one stable ID
- export output reports the file path
- no command surprises the operator with a live mutation

## What still needs attention

- commands that only work from inside the repo
- help text that is too long to scan quickly
- missing limits on discovery commands
- ambiguous or unstable identifiers

## Short future prompt

Verify the CLI from outside the source directory. Confirm help, doctor,
discovery, exact read, export, and that live writes are not implicit.
