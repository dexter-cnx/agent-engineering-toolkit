# AGENTS.md — Agent-Friendly CLI Overlay

When this overlay is present, prefer a reusable repository CLI over one-off shell scripts whenever the task is recurring or maps cleanly to an existing command surface.

## Rules

1. Check whether the repository already has a CLI, wrapper, or companion skill relevant to the task.
2. Prefer read-only commands first.
3. Keep outputs compact.
4. Prefer structured output such as JSON where practical.
5. Use narrowing flags such as `--limit` when available.
6. Use output file paths for large payloads instead of printing them inline.
7. Do not run live write commands unless the user explicitly requested a mutating action.
8. If a required capability is missing and the task is recurring, extend the CLI instead of creating a throwaway script.
9. Verify command usability from outside the source directory when the CLI is intended for reuse.
10. Document the shortest future prompt that should invoke the CLI again.

## Preferred execution order

When applicable, follow this order:

1. read the CLI contract or companion skill
2. run `doctor`
3. run `auth status` if relevant
4. run `search` or `list`
5. run `read <id>`
6. run `download` or `export`
7. stop at `draft` or `--dry-run` for any write flow unless live write was explicitly requested

## Output expectations

- stdout should stay small and high-signal
- large logs, reports, traces, or exports should go to files
- generated file paths should always be reported back
- read flows should be preferred over write flows

## Anti-patterns

Avoid these by default:

- giant JSON dumps in chat
- interactive prompts
- hidden state with no inspect command
- mixed read and write behavior in one command
- live mutation when a draft or dry-run path exists