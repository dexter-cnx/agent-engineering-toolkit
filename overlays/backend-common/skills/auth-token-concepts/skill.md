# Auth Token Concepts

Follow `../_shared/skill-contract.md`.

## Purpose
Define auth, identity, and token shape without binding to a runtime.

## Use when
- the feature depends on logged-in identity
- token lifecycle decisions matter

## Do not use when
- the task is runtime token implementation
- the task is only UI work

## Inputs required
- identity source
- token type
- session expectations

## Outputs expected
- auth model
- token lifecycle notes
- edge cases

## Workflow
1. Define identity source.
2. Define what the token represents.
3. Define expiry and refresh expectations.
4. Define revocation behavior.
5. Verify with the feature flow.

## Validation checklist
- [ ] Identity source is explicit
- [ ] Token lifecycle is documented
- [ ] Sensitive values are not exposed

## References
- `../../prompts/new_feature.md`

