# Repo Audit Checklist

## Identity
- Is the repository identity explicit?
- Does the root stay stack-agnostic?
- Are overlays clearly separated from foundation?

## Public release hygiene
- Are README, LICENSE, CONTRIBUTING, changelog, and conduct docs present?
- Are CODEOWNERS, SECURITY, PR template, issue templates, and CI present?
- Are there any private URLs or placeholders left?

## Docs
- Is there one canonical guide per language?
- Are cross-references consistent?
- Is the lifecycle defined in one canonical place?

## Prompts and agent model
- Are prompts coherent and complete?
- Are agent roles separated clearly?
- Is there duplication likely to drift?

## Skills, templates, examples
- Are skill contracts explicit?
- Are templates actionable, not just placeholders?
- Do examples cover end-to-end adoption realistically?

## Severity framing
- Critical: release blockers or identity violations
- Medium: adoption friction or drift risks
- Minor: cleanup and polish items
