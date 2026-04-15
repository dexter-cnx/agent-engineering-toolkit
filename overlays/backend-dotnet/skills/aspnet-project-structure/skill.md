# ASP.NET Project Structure

Follow `../_shared/skill-contract.md`.

## Purpose
Place solutions, projects, and folders in a maintainable ASP.NET Core structure.

## Use when
- starting a .NET backend
- reorganizing the project tree

## Do not use when
- the task is only endpoint logic

## Inputs required
- solution goals
- project count
- feature modules

## Outputs expected
- folder tree
- project map
- ownership notes

## Workflow
1. List solution boundaries.
2. Place application and infrastructure projects.
3. Separate transport from business logic.
4. Document test project placement.
5. Verify the tree against the planned boundaries.

## Validation checklist
- [ ] Project boundaries are explicit
- [ ] Transport and business layers are separate
- [ ] Test projects have a home

## References
- `../../prompts/new_project.md`

