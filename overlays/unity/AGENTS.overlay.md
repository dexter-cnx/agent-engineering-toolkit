# Unity Overlay Rules

## Boundary rules

- Scene objects should stay thin and delegate real behavior to reusable systems.
- MonoBehaviours may compose gameplay, but they should not become the application boundary.
- ScriptableObjects are for config, data, and controlled runtime channels, not loose global state.
- Input, UI, save, analytics, build, and content pipeline code should stay behind explicit adapters or services.
- Platform-specific code should be isolated with assembly boundaries, define symbols, or adapter layers.
- Asset import and build pipeline decisions belong in the overlay, not in shared foundation docs.
- Feature code may compose multiple skills, but skill rules remain capability-scoped.

## Skill usage rules

- Start with the smallest skill set that covers the work.
- Prefer explicit scene, prefab, and assembly ownership over implicit conventions.
- Keep namespaces aligned with feature and assembly boundaries.
- Prefer editor-visible validation for structure, references, and asset rules.
- Update project memory only for stable Unity conventions or known constraints.

## Verification rules

Document and run, where possible:

```bash
Unity Test Runner
Unity build validation
```

Also verify:
- scenes and prefabs still resolve
- asmdef and namespace boundaries still make sense
- platform-specific settings still match the target build
- no documentation points to missing files

## Review rules

Reject changes when:
- bootstrap logic leaks into unrelated gameplay code
- prefabs or scenes own hidden coupling
- Unity editor concerns leak into runtime domain boundaries
- asset pipeline rules are not reflected in the catalog or docs
