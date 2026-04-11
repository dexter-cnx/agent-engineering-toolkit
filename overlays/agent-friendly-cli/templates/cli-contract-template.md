# {{cli_name}} CLI Contract

## Purpose

{{one_sentence_purpose}}

## Command families

- `{{cli_name}} doctor`
- `{{cli_name}} auth status`
- `{{cli_name}} search ...`
- `{{cli_name}} read <id>`
- `{{cli_name}} export ...`
- `{{cli_name}} draft ...`
- `{{cli_name}} write ...`

## Output rules

- keep default output compact
- provide structured output where practical
- export large payloads to files
- report saved file paths

## Safety rules

- read-only flows first
- exact read after discovery
- draft or dry-run before live write
- live write only on explicit request

## Verification

The CLI should be verified by proving:

1. command resolution from outside the source folder
2. usable help output
3. setup or auth checks
4. working discovery
5. working exact read
6. file export
7. gated write behavior