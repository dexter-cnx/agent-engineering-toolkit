# flutter-auth Skill

## Intent

Apply flutter-auth as a reusable capability within the Mobile Flutter overlay.

## Required architecture

- Keep presentation code focused on rendering, interaction wiring, and view state only.
- Keep business orchestration outside widgets and away from plugin-specific code.
- Keep plugin or SDK integration behind services, adapters, repositories, or equivalent boundaries.
- Prefer typed models across boundaries instead of raw maps, platform channels, or SDK objects.
- Document platform-specific requirements when they affect Android, iOS, or web behavior.
- Update project memory only with stable conventions, not one-off implementation details.

## Deliverables

- session policy
- guarded route matrix
- auth state model
- implementation notes tied to the consuming repository structure
- verification notes with clear pass and fail conditions

## Reject when

- widgets directly own provider-specific integration logic
- domain or application contracts leak Flutter or plugin types
- error handling is omitted or left implicit
- documentation references files that do not exist
- the skill redefines the foundation identity instead of extending the overlay

## Suggested composition

Common companion skills:
- `flutter-storage`
- `flutter-networking`
- `flutter-deep-link`
