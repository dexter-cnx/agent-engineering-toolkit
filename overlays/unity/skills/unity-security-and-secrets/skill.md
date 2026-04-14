# unity-security-and-secrets Skill

Use this skill when secrets, auth tokens, or client-side security boundaries need review.

## Rules

- Never hardcode keys or credentials in client code or assets.
- Prefer build-time injection or external secret stores.
- Keep client auth flow boundaries explicit and minimal.
- Treat multiplayer or backend tokens as sensitive data paths.
- Document what the client may know versus what must remain server-owned.

## Deliverables

- secret-handling plan
- injection notes
- auth boundary notes
- verification checklist
