# Playbook: i18n Workflow

1. validate CSV
2. detect missing/duplicate keys
3. generate JSON files
4. review outputs

Commands:
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/i18n