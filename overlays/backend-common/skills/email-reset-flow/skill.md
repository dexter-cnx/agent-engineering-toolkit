# Email Reset Flow

Follow `../_shared/skill-contract.md`.

## Purpose
Define account recovery and reset flows that are clear and auditable.

## Use when
- password reset or account recovery is needed

## Do not use when
- the task is unrelated to user recovery

## Inputs required
- trigger
- delivery channel
- expiry and recovery rules

## Outputs expected
- reset flow
- user-facing messages
- failure and expiry behavior

## Workflow
1. Define the trigger.
2. Define the token or code lifecycle.
3. Define delivery behavior.
4. Define expired and invalid behavior.
5. Verify recovery scenarios.

## Validation checklist
- [ ] Trigger is explicit
- [ ] Expiry is stated
- [ ] Failure messages are safe

## References
- `../../prompts/new_feature.md`

