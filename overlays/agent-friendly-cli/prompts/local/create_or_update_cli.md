# Create or Update an Agent-Friendly CLI

You are working inside this repository.

Your goal is to create or update a reusable CLI for a repeated workflow so that future coding-agent sessions can use it reliably.

## Outcome

Build or refine a CLI with these properties:

- non-interactive by default
- compact by default
- machine-readable where practical
- clear setup and auth checks
- explicit read-first flow
- large outputs written to files
- write actions separated from read actions
- reusable from any folder through PATH or a documented wrapper
- accompanied by a companion skill for future tasks

## Constraints

1. Do not design a human-only CLI.
2. Prefer subcommands over ambiguous flag combinations.
3. Separate discovery from exact reads.
4. Keep default output small.
5. Add JSON output where practical.
6. Add output file support for large payloads.
7. Add setup or auth checks if relevant.
8. Keep write paths separate from read paths.
9. Avoid hidden state.
10. Verify reuse from outside the source directory.

## Required workflow

Before implementing:

1. inspect the repository structure
2. propose the command surface first
3. state assumptions
4. identify only real blockers

Then implement.

## Suggested command surface

Use this shape unless a better repo-specific pattern is clearly justified:

- `<cli> doctor`
- `<cli> auth status`
- `<cli> search ...`
- `<cli> read <id>`
- `<cli> download ...`
- `<cli> export ...`
- `<cli> draft ...`
- `<cli> write ...`

Support these where relevant:

- `--json`
- `--limit`
- `--output <path>`
- `--dry-run`

## Deliverables

Produce:

1. the CLI code or updates
2. install and run instructions
3. a companion skill draft
4. verification steps
5. examples of safe future usage

## Verification requirements

Prove all of the following:

- the command resolves from outside the source folder
- help output is understandable
- setup or auth checks behave correctly
- one safe discovery command works
- one exact read command works
- one large-output export writes to a file and returns the path
- write commands are documented but not executed unless explicitly requested

## Response format

Reply in this exact structure:

1. Assumptions
2. Proposed command surface
3. Files to create or update
4. Implementation
5. Verification proof
6. Companion skill
7. Shortest future prompt