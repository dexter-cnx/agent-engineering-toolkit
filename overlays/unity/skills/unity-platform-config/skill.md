# unity-platform-config Skill

Use this skill when platform-specific Unity settings need to be selected or audited.

## Rules

- Keep platform settings isolated from gameplay logic.
- Document mobile, desktop, or web assumptions where they matter.
- Make orientation, permissions, stripping, and backend choices explicit.
- Track quality tiers and platform overrides as part of the release contract.
- Prefer settings that are predictable across editor and build environments.

## Deliverables

- platform settings plan
- backend and stripping notes
- quality-tier notes
- verification checklist
