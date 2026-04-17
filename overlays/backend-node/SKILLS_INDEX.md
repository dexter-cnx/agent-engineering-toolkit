# Skills Index

## Core skills
- `node-service-structure` — src/routes, services, repositories, adapters, domain, schemas
- `route-boundaries` — thin transport handlers and request parsing
- `service-orchestration` — use-case flow and business orchestration
- `repository-boundaries` — persistence access without business logic
- `adapter-boundaries` — external provider isolation

## Selection guide
- Starting a new service -> `node-service-structure`
- Transport or API entry concerns -> `route-boundaries`
- Use-case flow -> `service-orchestration`
- Data access or persistence -> `repository-boundaries`
- External APIs or side effects -> `adapter-boundaries`

## Karpathy-governed exemplar

- `skills/node-service-structure/skill.md`
- `skills/node-service-structure/skill.contract.yaml`
- `skills/node-service-structure/eval/cases/governance-smoke/expected_result.json`
