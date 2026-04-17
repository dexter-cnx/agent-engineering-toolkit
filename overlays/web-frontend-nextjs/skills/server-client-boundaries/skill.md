# Server Client Boundaries

Follow `../_shared/skill-contract.md`.

## Purpose
Decide what runs on the server and what stays in the client.

## Use when
- data loading and interactivity need separation
- a feature is mixing server and client logic

## Do not use when
- the task is only routing placement
- the task is backend implementation

## Inputs required
- interactive behavior
- initial data needs
- server-only constraints

## Outputs expected
- boundary map
- component split
- state flow notes

## Workflow
1. List server-only responsibilities.
2. List client-only responsibilities.
3. Push shared logic into a reusable boundary.
4. Keep client components focused on interaction.
5. Verify that server code does not leak into client code.

## Validation checklist
- [ ] Client code is interactive only
- [ ] Server code owns initial reads where appropriate
- [ ] Boundaries are documented

## References
- `../../prompts/refactor_feature.md`
- `../../examples/account-settings-nextjs.md`

## Karpathy governance

- Contract: `skill.contract.yaml`
- Eval case: `eval/cases/governance-smoke/README.md`
- Expected result: `eval/cases/governance-smoke/expected_result.json`
- Example: `examples/governance-example.md`
- Prompt: `prompts/governance-prompt.md`
