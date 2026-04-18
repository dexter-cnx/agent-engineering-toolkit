# Workflow: Repo Hardening

## Mission
Increase governance signal and reduce structural drift in an existing repository.

## Inputs
Current repo structure, lint outputs, policy gaps, known debts.

## Outputs
- tightened lint rules
- CI enforcement updates
- memory updates with debt deltas

## Boundaries
- Harden existing system before introducing new subsystems.
- Prefer minimal edits with measurable governance gain.

## Escalation conditions
- policy cannot be enforced with available tooling
- canonical docs conflict with implementation reality
- hardening change introduces contributor friction without benefit
