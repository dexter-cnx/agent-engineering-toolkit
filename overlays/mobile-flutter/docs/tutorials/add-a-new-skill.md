# Add a New Skill

## Goal

Add one atomic Flutter skill safely without duplicating existing responsibilities.

## Use this when

- A new capability needs a reusable skill capsule
- A current skill is too broad and should be split
- An agent is contributing a new skill in a controlled way

## Do not do this when

- The work belongs in a policy, template, workflow, or example
- An existing skill can be updated instead of creating a new one
- The request is not a standalone responsibility

## Steps

1. Check `SKILLS_INDEX.md` for the closest existing skill.
2. Read `AGENT_CONTRIBUTION_RULES.md` and the maintainer checklist.
3. Run the generator.
4. Fill in every required section in `SKILL.md`.
5. Add one example and one template reference.
6. Update `SKILLS_INDEX.md` by running the sync command.
7. Run validation, overlap detection, and docs sync.
8. Update workflows or tutorials only if the new skill changes orchestration.

## Canonical review docs

- Contributor rules: `overlays/mobile-flutter/CONTRIBUTING_SKILLS.md`
- Maintainer review criteria: `overlays/mobile-flutter/MAINTAINER_REVIEW_GUIDE.md`

## Example command

```bash
bash tools/skillgen/bin/skillgen new \
  --overlay overlays/mobile-flutter \
  --category routing \
  --name flutter-go-router-shell-route \
  --purpose "Create a shell route for a Flutter feature area." \
  --inputs "Route list; shell navigation requirements" \
  --outputs "Router file; page builder paths"
```

## Keep in mind

- The tutorial shows the creation flow.
- The canonical checklists live in the contributor and maintainer docs above.
- Do not duplicate checklist content here.
