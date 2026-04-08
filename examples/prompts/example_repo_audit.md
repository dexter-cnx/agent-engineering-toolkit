# Example Repo Audit Prompt

Audit this repository as a reusable engineering toolkit.

## When to use
Use this before publishing a new toolkit release or before adopting the toolkit into a new consuming repo.

## Example invocation
```text
You are auditing this repository as a public, production-ready foundation toolkit repo.
Focus on root identity, overlay boundaries, missing docs, weak verification, and unclear templates.
Return critical, medium, and minor findings with concrete file-by-file edits.
```

## Example scenario
- A team is adding a new overlay and wants to confirm it does not rewrite the foundation identity.
- A maintainer wants a final pre-release sanity check before tagging a new version.

## What good output looks like
- it names exact files
- it separates foundation issues from overlay issues
- it proposes concrete edits instead of generic advice
- it calls out missing or stale documentation
