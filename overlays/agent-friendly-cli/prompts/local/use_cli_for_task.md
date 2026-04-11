# Use Existing Agent-Friendly CLI Automatically

You are working inside this repository.

Solve the task by using the existing repository CLI first whenever it fits.

## Required behavior

1. Read the relevant CLI contract and companion skill first.
2. Prefer the repository CLI over one-off scripts.
3. Prefer read-only commands first.
4. Keep stdout compact.
5. Save large outputs to files and return the paths.
6. If setup or auth is relevant, run doctor or auth status first.
7. If an exact identifier is needed, do discovery first and then exact read.
8. If the task may mutate state, stop at draft or dry-run unless live write was explicitly requested.

## Never do these by default

- do not dump giant JSON into chat
- do not skip discovery when the ID is unknown
- do not execute live write commands without explicit approval
- do not replace an existing reusable CLI with an ad hoc script unless the CLI is missing a necessary capability

## Response format

Reply in this exact structure:

1. CLI chosen
2. Commands run
3. Key findings
4. Files generated
5. Next safe command
6. Any blocked write step requiring explicit approval