---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - export
aliases:
  - CLI Export Large Payload
---

# Large Export Flow

Use this pattern when the result is too large to keep in chat or stdout.

## Scenario

A discovery or validation command produces logs, traces, or reports that are
useful to inspect later, but not useful to print inline.

## Pattern

1. Keep the default output compact.
2. Provide an `--output <path>` flag.
3. Write the full result to a file.
4. Return only a short summary and the saved path.

## Example commands

```bash
mycli search --limit 20 --json
mycli export --output artifacts/report.json --json
mycli export logs --output artifacts/logs.txt
```

## Example output

```text
$ mycli export --output artifacts/report.json --json
Exported 24 records to artifacts/report.json
Bytes written: 18432
Complete: yes

$ mycli export logs --output artifacts/logs.txt
Saved logs to artifacts/logs.txt
Lines written: 1240
```

## Good export result

- the command reports what was exported
- the command reports where it was saved
- the command confirms whether the output is complete
- the file path is stable and easy to reuse in later steps

## Bad export result

- thousands of lines dumped to stdout
- a file written with no confirmation path
- a hidden temp file that the operator cannot inspect
- an export command that also performs an unrelated write

## Short future prompt

Use the CLI export path for large payloads. Keep stdout small and write the
full artifact to a file.
