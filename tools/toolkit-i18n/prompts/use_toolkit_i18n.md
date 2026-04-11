Read overlays/agent-friendly-cli/AGENTS.md and use the cli-operator skill.

Also read:

- tools/toolkit-i18n/AGENTS.md
- tools/toolkit-i18n/docs/cli_contract.md

Use `toolkit-i18n` first for this task.

Execution order:

1. `toolkit-i18n doctor`
2. `toolkit-i18n validate <csv-path> --json`
3. `toolkit-i18n diff <csv-path> --json`
4. `toolkit-i18n keys list <csv-path> --json`
5. `toolkit-i18n keys diff --used-file <file> --translations <csv-path> --json`
6. `toolkit-i18n coverage --used-file <file> --translations <csv-path> --json`
7. `toolkit-i18n generate <csv-path> --output <dir>`

Rules:

- keep stdout compact
- summarize only the highest-signal issues
- compare architecture-exported used keys when available
- report generated file paths
- do not perform any live write step unless explicitly requested

Reply in this exact structure:

1. CLI chosen
2. Commands run
3. Key findings
4. Files generated
5. Next safe command
6. Any blocked write step requiring explicit approval
