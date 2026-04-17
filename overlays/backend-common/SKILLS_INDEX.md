# Skills Index

## Core skills
- `api-contracts` — request and response shape design
- `auth-token-concepts` — session, token, and identity shape
- `refresh-token-strategy` — refresh lifecycle and revocation shape
- `role-permission-model` — permissions and authorization rules
- `crud-resource-design` — stable resource design for create/read/update/delete
- `soft-delete-audit` — history, traceability, and deletion semantics
- `file-handling-safety` — uploads, downloads, and storage safety
- `email-reset-flow` — password reset and notification flow shape
- `validation-error-handling` — validation and API error strategy
- `backend-testing-strategy` — testing layers and coverage planning

## Selection guide
- You need the public contract -> `api-contracts`
- You need auth shape -> `auth-token-concepts`
- You need refresh semantics -> `refresh-token-strategy`
- You need permission rules -> `role-permission-model`
- You need resource design -> `crud-resource-design`
- You need safe file flows -> `file-handling-safety`
- You need reset or email flow -> `email-reset-flow`
- You need validation and errors -> `validation-error-handling`
- You need test planning -> `backend-testing-strategy`

## Relationship to backend-node
- backend-node handles Node-specific runtime patterns
- backend-common handles the shared concepts beneath Node and .NET

