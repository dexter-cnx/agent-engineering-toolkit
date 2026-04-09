# unity-build-pipeline Skill

Use this skill when Unity builds, versioning, or build profile setup needs structure.

## Rules

- Keep build steps reproducible across local and CI environments.
- Make target-specific settings visible in code or tracked config.
- Treat scripting define symbols and versioning as part of the build contract.
- Separate build profiles from runtime logic.
- Prefer explicit verification for each supported platform.

## Deliverables

- build target plan
- versioning notes
- define-symbol notes
- verification checklist
