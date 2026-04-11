---
name: {{skill_name}}
description: Use the {{cli_name}} CLI for repeated {{domain}} tasks with compact outputs, exact reads by ID, exported large results, and approval-gated writes.
---

# When to use

Use this skill when the task involves {{domain}} and the {{cli_name}} CLI is available in the repository.

# Read-first workflow

1. `{{cli_name}} doctor`
2. `{{cli_name}} auth status`
3. `{{cli_name}} search ... --limit N`
4. `{{cli_name}} read <id>`
5. `{{cli_name}} export ... --output <path>`

# Output rules

- keep stdout compact
- prefer structured output where practical
- write large results to files
- always report generated file paths

# Write safety

For mutable actions:

- prefer `draft`
- prefer `--dry-run`
- do not run live writes unless explicitly requested

# Common prompts

- Use {{skill_name}} to search for ...
- Use {{skill_name}} to read item ID ...
- Use {{skill_name}} to export ... into artifacts and summarize the result.
