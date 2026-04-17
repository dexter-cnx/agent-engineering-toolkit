# Karpathy Ecosystem Index

This index helps maintainers discover which overlays, skills, and compositions are wired
into the Karpathy governance plane.

## Karpathy-integrated overlays

| Overlay | Status | Governed exemplar |
|---|---|---|
| `agent-karpathy` | Integrated | `overlays/agent-karpathy/README.md` |
| `mobile-flutter` | Integrated | `overlays/mobile-flutter/skills/flutter-network-dio/skill.contract.yaml` |
| `backend-node` | Integrated | `overlays/backend-node/skills/node-service-structure/skill.contract.yaml` |
| `backend-dotnet` | Integrated | `overlays/backend-dotnet/skills/jwt-auth-dotnet/skill.contract.yaml` |
| `python-service` | Integrated | `overlays/python-service/skills/python-service-structure/skill.contract.yaml` |
| `web-frontend-nextjs` | Integrated | `overlays/web-frontend-nextjs/skills/server-client-boundaries/skill.contract.yaml` |
| `unity` | Integrated | `overlays/unity/skills/unity-project-structure/skill.contract.yaml` |

## Governance-ready skills

| Skill | Overlay | Eval case |
|---|---|---|
| `flutter-network-dio` | `mobile-flutter` | `overlays/mobile-flutter/skills/flutter-network-dio/eval/cases/governance-smoke/expected_result.json` |
| `node-service-structure` | `backend-node` | `overlays/backend-node/skills/node-service-structure/eval/cases/governance-smoke/expected_result.json` |
| `jwt-auth-dotnet` | `backend-dotnet` | `overlays/backend-dotnet/skills/jwt-auth-dotnet/eval/cases/governance-smoke/expected_result.json` |
| `python-service-structure` | `python-service` | `overlays/python-service/skills/python-service-structure/eval/cases/governance-smoke/expected_result.json` |
| `server-client-boundaries` | `web-frontend-nextjs` | `overlays/web-frontend-nextjs/skills/server-client-boundaries/eval/cases/governance-smoke/expected_result.json` |
| `unity-project-structure` | `unity` | `overlays/unity/skills/unity-project-structure/eval/cases/governance-smoke/expected_result.json` |

## Draft-only overlays

Everything not listed above remains draft-only until it has a contract file and a static
eval case. That includes legacy or shared overlays that do not yet carry a governed skill.

## Composition integration evals

| Composition | Integration doc | Primary checkpoints |
|---|---|---|
| `nextjs-fullstack` | `docs/compositions/nextjs-fullstack/KARPATHY_INTEGRATION.md` | App Router split, contract shape, promotion owner |
| `nextjs-dotnet` | `docs/compositions/nextjs-dotnet/KARPATHY_INTEGRATION.md` | frontend/backend split, auth boundary, promotion owner |
| `nextjs-nodebackend` | `docs/compositions/nextjs-nodebackend/KARPATHY_INTEGRATION.md` | frontend/backend split, service boundary, promotion owner |
| `nextjs-python-service` | `docs/compositions/nextjs-python-service/KARPATHY_INTEGRATION.md` | frontend/backend split, service boundary, promotion owner |
