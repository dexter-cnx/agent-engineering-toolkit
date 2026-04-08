# Prompt Runner Scaffold

This folder is intentionally lightweight. It exists to standardize how internal teams run staged prompts.

Suggested usage:
1. Copy the prompt into your preferred agent environment
2. Save the result in `artifacts/runs/<date>/<stage>.md`
3. Pass the handoff block into the next stage
4. Attach review output to the PR

Recommended stages:
- 01_lead
- 02_architecture
- 03_implementation
- 04_review

The toolkit does not enforce a specific agent runtime here; it enforces the sequence and artifacts.
