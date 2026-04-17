# Job Contract Check

This tool validates the async worker contract layer and its reference usage.

## What it checks

- the job contract package exists and exports the required schemas
- the reference app points at the shared job contract package
- the job-oriented docs are present and linked

## Commands

```bash
npm run check
```

## Read next

- `packages/job-contracts/README.md`
- `apps/ai-workflow-reference/README.md`
