# Backend Node Reuse Analysis

## Why this analysis exists
`overlays/backend-node` is the existing backend-specific overlay in the repository. `backend-common` should reuse what is conceptually shared, but it must not copy Node runtime details into a generic backend layer.

## Reusable concepts from backend-node
- thin route handlers
- services as orchestration boundaries
- repositories for persistence boundaries
- adapters for external integrations
- project memory for durable conventions

## Reusable skill style
- narrow, task-based guidance
- explicit boundary rules
- verification notes
- small example-driven documentation

## What stays Node-specific
- Express/Fastify request and response types
- Node package and script commands
- Node middleware mechanics
- filesystem, module, and runtime conventions specific to Node

## How backend-common should align
- describe backend shapes in runtime-neutral terms
- keep the contract/validation/auth vocabulary shared
- keep implementation details in backend-dotnet or backend-node

## How backend-dotnet should align
- adopt the same boundary language
- keep runtime-specific wiring in .NET docs
- reuse the shared contract vocabulary without importing Node assumptions

## Future harmonization opportunities
- shared API contract templates
- shared auth/permission vocabulary
- shared review checklists for backend boundaries

