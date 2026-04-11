Read overlays/agent-friendly-cli/AGENTS.md and use the cli-creator skill.

Also read:

- tools/toolkit-i18n/README.md
- tools/toolkit-i18n/AGENTS.md
- tools/toolkit-i18n/docs/cli_contract.md

Create or refine a reusable CLI named `toolkit-i18n` for Flutter localization workflows in this repository.

The source of truth is a CSV file such as `assets/i18n/translations.csv`.

Initial scope:

- doctor
- validate
- diff
- generate

Requirements:

- non-interactive by default
- compact output
- structured output where practical
- detect duplicate keys, malformed rows, missing values, and missing required columns
- support dotted keys for nested JSON generation
- write generated JSON files into a target output directory
- do not add implicit live-write behavior to source files

Before implementation:

1. inspect the repository structure
2. propose the command surface first
3. state assumptions
4. identify only real blockers

Then implement.

Verify that:

- the command can be run from outside the source folder through the documented method
- doctor works
- validate works
- generate writes files to a target directory
- outputs stay compact

Reply in this exact structure:

1. Assumptions
2. Proposed command surface
3. Files to create or update
4. Implementation
5. Verification proof
6. Companion skill
7. Shortest future prompt
