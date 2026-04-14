---
tags:
  - agent-engineering-toolkit
  - overlay
  - cli
  - example
  - failures
aliases:
  - CLI Failure Handling
---

# Failure Handling

Use this pattern when the CLI must fail clearly and helpfully.

## Scenario

The CLI is missing setup, credentials, or a valid identifier.

## Failure cases

### Missing setup

Expected behavior:

- `doctor` says what is missing
- the message tells the operator how to fix it
- the exit code is non-zero

### Missing auth

Expected behavior:

- `auth status` reports the missing credential or session
- the command does not proceed with a hidden fallback
- the output stays compact

### Unknown identifier

Expected behavior:

- `read <id>` says the ID was not found
- the command suggests using `search` or `list` first

### No results

Expected behavior:

- `search` returns an empty result clearly
- the output still includes enough context to adjust the query

## Example messages

```text
Missing configuration: set MYCLI_TOKEN or run mycli auth login.
No results found for "release-2026-04". Try a wider search or use mycli list.
Unknown item id: item-184. Run mycli search --limit 20 to discover valid IDs.
```

## Example responses

```text
$ mycli doctor
Error: missing configuration
Set MYCLI_TOKEN or run `mycli auth login`.
Exit code: 2

$ mycli auth status
Error: authentication required
No valid session found.
Exit code: 3

$ mycli read item-999
Error: unknown item id item-999
Try `mycli search --limit 20` to find valid IDs.
Exit code: 4
```

## Anti-patterns

- raw stack traces for ordinary user mistakes
- silent failure with exit code 0
- vague messages like "error occurred"
- fallback behavior that hides the real problem

## Short future prompt

Make failures explicit, actionable, and compact. Point the operator to the next
safe command.
