Read overlays/agent-friendly-cli/prompts/local/verify_cli_installation.md and apply it to `toolkit-i18n`.

Also read:

- tools/toolkit-i18n/README.md
- tools/toolkit-i18n/docs/cli_contract.md

Verify in order:

1. the command resolves from outside the source folder
2. usage or help is understandable
3. `toolkit-i18n doctor` works
4. `toolkit-i18n validate <csv-path> --json` works
5. `toolkit-i18n generate <csv-path> --output <dir>` writes files and reports paths
6. outputs remain compact
7. there is no implicit live write behavior

If verification fails, make the minimal fix and rerun verification.

Reply in this exact structure:

1. Command resolution proof
2. Help output review
3. Doctor result
4. Validate result
5. Generate result
6. Output compactness review
7. Write safety review
8. Required fixes
