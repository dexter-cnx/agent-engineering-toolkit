# Known Constraints

- Foundation must not silently assume one framework as the default identity.
- Public release files must exist if referenced in README or docs.
- Review and verification must remain distinct concepts in examples and templates.
- Workflow summary files should stay short pointers when `docs/tutorial.md` carries the full walkthrough.
- Entry-point docs should keep the bootstrap helper discoverable without implying it replaces the full bootstrap flow.
- The authoritative tree manifest must be kept in sync with newly saved audit files.
- The audit workflow now has two distinct surfaces: the role-based prompt and the invocation template companion.
- Release notes must be honest about same-day version history when multiple tags are cut on the same date.
- Prompt docs should prefer the stage hub (`prompts/index.md` / `prompts/index_EN.md`) before linking individual stage files.
- Public-release checklist pages are summaries unless they explicitly mirror `scripts/check-public-repo.paths`.
- Foundation navigation pages should remain thin and should not duplicate stack-specific AGENTS templates.
