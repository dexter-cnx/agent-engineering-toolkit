# Audit Repo

## Role
Act as **REVIEWER** and **VERIFIER** in combination.

## Goal
Audit a repository as a reusable engineering system, identifying structural, documentation, and release-readiness issues.

## When to use
- pre-release review
- foundation-vs-overlay compliance check
- adoption readiness check
- repository-wide consistency audit

## Inputs
- repository tree
- README and identity documents
- core docs
- prompts, skills, templates, and examples
- public-repo hygiene files

## Process
1. Verify repository identity is consistent across root, docs, and examples.
2. Check for foundation-vs-overlay boundary violations.
3. Review prompt and skill structural consistency.
4. Review template actionability.
5. Check public-repo hygiene.
6. Identify vague wording, duplication, and missing adoption guidance.
7. Group findings by severity.

## Required output
- Executive summary
- Critical issues
- Medium issues
- Minor issues
- File-by-file notes
- Foundation vs overlay violations
- Public repo readiness assessment
- Recommended exact edits
- Final verdict

## Non-goals
- replacing `architecture-review` for narrow structure analysis
- automatically rewriting the repository
- claiming verified status for unchecked areas
