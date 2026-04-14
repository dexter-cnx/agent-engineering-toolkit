# unity-ci-cd Skill

Use this skill when Unity build automation or repository gates need CI/CD conventions.

## Rules

- Cache only what helps and does not hide broken state.
- Name artifacts clearly by branch, platform, and build intent.
- Fail the pipeline when scene, prefab, or meta drift is detected.
- Keep runner setup deterministic and easy to reproduce.
- Preserve logs and build outputs that help triage a failed Unity build.

## Deliverables

- pipeline outline
- artifact naming plan
- cache policy
- failure criteria
