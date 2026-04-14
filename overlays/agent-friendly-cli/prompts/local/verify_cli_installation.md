# Verify Agent-Friendly CLI Installation

You are verifying that a repository CLI is genuinely reusable by future coding-agent sessions.

## Verification checklist

Verify these in order:

1. the command resolves from outside the source folder
2. help output clearly exposes the main subcommands
3. setup or auth checks run and fail clearly if configuration is missing
4. one safe discovery command works
5. one exact read command works using an ID from the discovery step
6. one large-output export writes to a file and returns the path
7. write-capable commands are documented and gated, but not executed without explicit approval

## Rules

- prefer deterministic commands
- keep example outputs compact
- if the command is not globally installed, verify the documented wrapper from another folder
- if verification fails, make the minimal fix and rerun verification

## Response format

Reply in this exact structure:

1. Command resolution proof
2. Help output review
3. Setup or auth check result
4. Discovery command result
5. Exact read result
6. File export result
7. Write safety review
8. Required fixes