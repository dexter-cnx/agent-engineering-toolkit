# Strict Audit Prompt

Use this prompt to ask an AI coding tool to perform a strict final audit of the repository.

Canonical alias:
- `prompts/audit_repo.md`

```text
You are auditing the repository as a production-ready public toolkit repo.

Repository identity:
- This repo is a domain-agnostic foundation toolkit.
- It must remain stack-agnostic at the root.
- Stack-specific assumptions must live in overlays only.

Audit goals:
1. Verify repository identity is consistent across:
   - README.md
   - README_TH.md
   - AGENTS.md
   - docs/*
   - overlays/*
   - templates/*
   - examples/*
2. Detect any leakage of mobile-, Flutter-, Node-, or Python-specific assumptions into the foundation layer.
3. Review whether the prompt pipeline is coherent and non-duplicative.
4. Review whether agent_team roles are clearly separated and useful.
5. Review whether skills are narrow, reusable, and non-overlapping.
6. Review whether templates are practical for real project adoption.
7. Review whether overlays are well-scoped extensions instead of identity rewrites.
8. Review whether public repo hygiene is complete:
   - LICENSE
   - CONTRIBUTING.md
   - CHANGELOG.md
   - CODE_OF_CONDUCT.md
   - CODEOWNERS
   - PR template
   - issue templates
   - SECURITY.md
   - CI workflows
9. Identify vague wording, duplicated docs, missing examples, missing adoption guidance, and any weak spots for public release.
10. Propose concrete fixes, with file-by-file recommendations.

Required output format:
- Executive summary
- Critical issues
- Medium issues
- Minor issues
- File-by-file review
- Foundation vs overlay violations
- Public repo readiness assessment
- Recommended exact edits
- Final verdict: ready / almost ready / not ready

Rules:
- Be strict.
- Do not praise without evidence.
- Call out inconsistencies directly.
- Prefer concrete edits over abstract advice.
- If something is missing, say exactly which file should be added or changed.
```
