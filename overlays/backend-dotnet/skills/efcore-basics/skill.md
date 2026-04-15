# EF Core Basics

Follow `../_shared/skill-contract.md`.

## Purpose
Define the persistence shape for EF Core without mixing in transport or business orchestration.

## Use when
- database entities or migrations change

## Do not use when
- the task is only API contract work

## Inputs required
- entity model
- persistence rules
- migration expectations

## Outputs expected
- DbContext shape
- mapping notes
- migration guidance

## Workflow
1. Define entities and aggregates.
2. Define DbContext ownership.
3. Map persistence rules.
4. Note query and write behavior.
5. Verify migration impact.

## Validation checklist
- [ ] Entity ownership is clear
- [ ] Mapping is explicit
- [ ] Migration impact is noted

## References
- `../../prompts/generate_dotnet_endpoint.md`

