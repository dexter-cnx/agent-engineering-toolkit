# Release Process

## Suggested process
1. Update docs and changelog.
2. Run the public-repo gate locally: `bash scripts/check-public-repo.sh`.
3. Run CI or the same checks CI uses.
4. Review open issues and pending repo hygiene tasks.
5. Confirm the release notes describe the foundation/overlay impact clearly.
6. Create a version tag.
7. Publish a GitHub release with short release notes.

## Release gate
A release should not be cut until:
- `scripts/check-public-repo.sh` passes
- the public checklist summary in `docs/public-repo-checklist.md` is current
- the machine-readable gate source in `scripts/check-public-repo.paths` is current
- any new docs, prompts, templates, or overlays are reflected in `docs/tree-manifest.txt`
- no private repository URLs are embedded in public files

## Suggested versioning
Use semantic versioning:
- MAJOR for breaking structural changes
- MINOR for new prompts/skills/templates/docs
- PATCH for corrections and small refinements

## Release ownership
Releases should be created by a maintainer who can verify the public checklist and owns the affected content.
