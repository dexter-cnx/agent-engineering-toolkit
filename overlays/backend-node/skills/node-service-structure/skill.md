# Node Service Structure

## Purpose

Define transport, service, repository, and adapter boundaries for a Node backend or job
processor.

## Use when

- starting a new Node backend
- reorganizing a service layer that has grown too flat
- separating API transport from business orchestration

## Do NOT use when

- the task is only route copy or a single handler tweak
- the task is only database migration authoring

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

1. List transport, service, repository, and adapter responsibilities.
2. Place the smallest boundary around each responsibility.
3. Keep business logic out of route handlers.
4. Keep external providers behind adapters.
5. Verify the tree against the intended boundaries.

## Validation checklist

- [ ] Transport is thin
- [ ] Business logic stays in services or domain code
- [ ] Persistence access stays behind repositories
- [ ] External providers stay behind adapters

## References

- `../../prompts/new_feature.md`
- `../../prompts/new_project.md`

## Karpathy governance

- Contract: `skill.contract.yaml`
- Eval case: `eval/cases/governance-smoke/README.md`
- Expected result: `eval/cases/governance-smoke/expected_result.json`
- Example: `examples/governance-example.md`
- Prompt: `prompts/governance-prompt.md`
