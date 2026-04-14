# Shared Web Skill Contract

Use this shared contract across web skills.

## Workflow
1. Understand the task and its boundaries.
2. Choose the smallest valid skill set.
3. Keep pages, features, components, services, state, and tests separate.
4. Document tradeoffs and assumptions.
5. Verify behavior before finalizing.
6. Update memory only for durable decisions.

## Guardrails
- Keep feature logic out of reusable UI primitives.
- Keep data access behind services or adapters.
- Keep state changes in the state layer.
- Keep accessibility and responsive behavior in scope.
- Keep CI and build readiness explicit.
