# flutter-performance-audit

## Purpose

Audit Flutter performance symptoms and produce prioritized fixes with measurable validation steps.

## Use when

- The app janks, stutters, or loads slowly
- A screen is heavy or rebuilds too often
- You need a performance review before release

## Do NOT use when

- The issue is purely semantic or copy related
- You have not observed a performance symptom yet
- The requested change is unrelated to rendering or startup cost

## Inputs required

- Screen or flow name
- Symptom description
- Trace, profile, or suspicion list
- Target platform

## Constraints

- Measure before recommending optimization
- Prioritize user-visible issues over micro-optimizations
- Keep fixes aligned with architecture
- Avoid speculative caching or memoization without evidence

## Step-by-step workflow

1. Identify the user-visible symptom.
2. Inspect widget rebuilds, startup cost, and expensive async work.
3. Rank causes by impact and confidence.
4. Propose specific code or asset fixes.
5. Add verification steps such as profile traces or build checks.

## Output contract

- Performance findings
- Prioritized fix list
- Verification method for each fix
- Notes on residual risk

## Validation checklist

- The symptom is tied to a concrete screen or flow
- The proposed fix is testable
- No premature optimization is suggested
- The architecture stays intact

## Related skills

- `flutter-web-loading-shell`
- `flutter-clean-architecture-audit`

## References

- [`../../../examples/full-feature-implementation.md`](../../../examples/full-feature-implementation.md)
- [`../../../canonical/web_loading.md`](../../../canonical/web_loading.md)

## Real example

If a profile page rebuilds on every stream tick, move expensive derived work out of the page and into the controller or provider, then confirm with a frame trace.

## Real file output sample

```text
docs/audits/profile-performance-audit.md
lib/features/profile/presentation/pages/profile_page.dart
lib/features/profile/presentation/controllers/profile_controller.dart
```
