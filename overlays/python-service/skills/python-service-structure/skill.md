# Python Service Structure

## Purpose

Define routers, services, repositories, adapters, domain models, and schemas for a Python
service repository.

## Use when

- starting a new Python service
- separating API transport from service orchestration
- reorganizing a service layer that has grown too flat

## Do NOT use when

- the task is only a one-line route tweak
- the task is only a data model rename

## Inputs required

- API surface
- service responsibilities
- persistence boundaries
- adapter boundaries

## Outputs expected

- folder tree
- boundary map
- ownership notes

## Workflow

1. List routers, services, repositories, adapters, domain, and schema responsibilities.
2. Place the smallest boundary around each responsibility.
3. Keep business logic out of routers.
4. Keep external providers behind adapters.
5. Verify the tree against the intended boundaries.

## Validation checklist

- [ ] Routers are thin
- [ ] Services own orchestration
- [ ] Repositories own persistence access
- [ ] Adapters isolate external providers

## References

- `../../prompts/new_feature.md`
- `../../prompts/new_project.md`

## Karpathy governance

- Contract: `skill.contract.yaml`
- Eval case: `eval/cases/governance-smoke/README.md`
- Expected result: `eval/cases/governance-smoke/expected_result.json`
- Example: `examples/governance-example.md`
- Prompt: `prompts/governance-prompt.md`
