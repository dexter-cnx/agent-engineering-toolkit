# Secrets Policy

## Rules

- Never commit keystores, provisioning profiles, API keys, or service account JSON.
- Keep secrets in environment variables or managed secret storage.
- Use placeholder files such as `.env.example` for structure only.
- Document secret setup without printing secret values.

## Release-specific rules

- Android signing material stays local or in CI secret storage.
- iOS signing material stays in Xcode/CI managed signing workflows.
- Firebase admin credentials never go into the repository.

## Verification

- Search for accidental secret literals before release.
- Confirm `.gitignore` covers local secret files.
