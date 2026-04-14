# 🌐 toolkit-i18n

Use toolkit-i18n for localization workflows.

Flow:
doctor → validate → keys list → keys diff / coverage → generate

Example:
toolkit-i18n validate assets/i18n/translations.csv --json
toolkit-i18n generate assets/i18n/translations.csv --output artifacts/i18n
toolkit-i18n keys diff --used-file artifacts/i18n-used-keys.json --translations assets/i18n/translations.csv --json
