# Agent Engineering OS Overview

## System layers

1. **Kernel (`system/`)**
   - canonical paths
   - policies and contracts
   - runtime control rules
2. **Runtime (`agents/`, `prompts/`, `memory/`)**
   - role execution model
   - prompt source/pack/compiled model
   - durable decisions + operational state
3. **Governance tooling (`tools/`)**
   - linting, validation, graph/build checks
4. **Execution specialization (`overlays/`)**
   - stack-specific overlays extending root rules
5. **Implementation references (`apps/`, `packages/`)**
   - runnable examples and shared packages

## Architectural guardrails

- Foundation remains stack-neutral.
- Boundaries are explicit and documented.
- Side effects are isolated through policy contracts.
- Every governance rule maps to executable checks when feasible.
