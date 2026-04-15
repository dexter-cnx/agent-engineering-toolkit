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

## Contribution checklist

- [ ] I checked for a closer existing skill.
- [ ] I explained why a new skill is needed.
- [ ] I used the generator instead of creating files manually.
- [ ] I completed every required field in `SKILL.md`.
- [ ] I linked examples and templates.
- [ ] I ran index sync and validation.

## Maintainer review checklist

- [ ] The skill is atomic.
- [ ] The skill does not duplicate another active skill.
- [ ] The naming is consistent.
- [ ] The references exist and are current.
- [ ] CI passes after the change.
