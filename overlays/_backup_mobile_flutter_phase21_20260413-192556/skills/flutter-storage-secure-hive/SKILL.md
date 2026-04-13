---
name: flutter-storage-secure-hive
category: Framework Reference Docs
summary: Storage guidance for secure values, cache, and offline-friendly local persistence.
---

# flutter-storage-secure-hive

Choose storage by sensitivity and access pattern.

## Use
- Secure storage for tokens and secrets
- Box/database/cache for offline data and preferences
- Repository abstraction to isolate storage choice

## Avoid
- Storing secrets in plain preferences
- Letting widgets manage persistence details
