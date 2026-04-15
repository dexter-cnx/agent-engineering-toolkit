# Sample Failures

## Missing skill section

```text
Skill validation failed:
- overlays/mobile-flutter/skills/routing/flutter-go-router-route-map/SKILL.md: missing required heading '## Validation checklist'
```

## Empty section

```text
Skill validation failed:
- overlays/mobile-flutter/skills/firebase/flutter-firebase-auth-adapter/SKILL.md: section '## Purpose' is empty
```

## Section shape error

```text
Skill validation failed:
- overlays/mobile-flutter/skills/architecture/flutter-feature-folder-scaffold/SKILL.md: section '## Step-by-step workflow' must contain at least two numbered steps
```

## Duplicate heading

```text
Skill validation failed:
- overlays/mobile-flutter/skills/routing/flutter-go-router-route-map/SKILL.md: duplicate heading '## References'
```

## Naming mismatch

```text
Skill validation failed:
- overlays/mobile-flutter/skills/release/flutter-ios-release-readiness/SKILL.md: H1 title 'iOS readiness' must match folder name 'flutter-ios-release-readiness'
```

## Category placement error

```text
Skill validation failed:
- overlays/mobile-flutter/skills/legacy/flutter-riverpod-state-skeleton/SKILL.md: category 'legacy' is not in the active routing set ['architecture', 'state', 'routing', 'firebase', 'web', 'release', 'performance', 'tooling']
```

## Duplicate trigger or purpose

```text
Skill validation failed:
- overlays/mobile-flutter/skills/routing/flutter-go-router-deeplink-wireup/SKILL.md: duplicate purpose detected with overlays/mobile-flutter/skills/routing/flutter-go-router-route-map/SKILL.md -> 'Create the go_router route map for one Flutter app or feature slice.'
```

## Missing non-README reference

```text
Skill validation failed:
- overlays/mobile-flutter/skills/architecture/flutter-clean-architecture-audit/SKILL.md: references must link to at least one non-README example or template file
```

## Real file output sample

```text
Skill validation failed:
- overlays/mobile-flutter/skills/architecture/flutter-feature-folder-scaffold/SKILL.md: section '## Real file output sample' must include at least one concrete file or folder path
```

## Broken repository path

```text
Documentation consistency check failed:
- overlays/mobile-flutter/docs/tutorials/build-a-new-project-with-ai.md: broken repository path reference -> overlays/mobile-flutter/templates/missing-template.md
```

## Workflow references a missing skill

```text
Documentation consistency check failed:
- overlays/mobile-flutter/workflows/new-feature/README.md: references non-active skills -> flutter-feature-generator
```
