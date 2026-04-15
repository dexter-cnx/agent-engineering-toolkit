# Full Feature Implementation Example

Example feature: profile screen with remote repository and Riverpod state.

## Reference files

- [`../templates/feature-module-template.md`](../templates/feature-module-template.md)
- [`../templates/repository-template.md`](../templates/repository-template.md)
- [`../templates/state-management-template.md`](../templates/state-management-template.md)
- [`../skills/architecture/flutter-clean-architecture-audit/SKILL.md`](../skills/architecture/flutter-clean-architecture-audit/SKILL.md)
- [`../skills/architecture/flutter-feature-folder-scaffold/SKILL.md`](../skills/architecture/flutter-feature-folder-scaffold/SKILL.md)
- [`../skills/architecture/flutter-feature-contract-scaffold/SKILL.md`](../skills/architecture/flutter-feature-contract-scaffold/SKILL.md)
- [`../skills/state/flutter-riverpod-state-skeleton/SKILL.md`](../skills/state/flutter-riverpod-state-skeleton/SKILL.md)
- [`../skills/firebase/flutter-firestore-repository/SKILL.md`](../skills/firebase/flutter-firestore-repository/SKILL.md)

## Output tree

```text
lib/features/profile/
  data/datasources/profile_remote_data_source.dart
  data/repositories/profile_repository_impl.dart
  domain/entities/profile.dart
  domain/repositories/profile_repository.dart
  domain/usecases/load_profile_usecase.dart
  presentation/controllers/profile_controller.dart
  presentation/pages/profile_page.dart
```

## Flutter-specific implementation

```dart
class ProfilePage extends ConsumerWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final state = ref.watch(profileControllerProvider);
    return state.when(
      data: (profile) => Text(profile.name),
      loading: () => const CircularProgressIndicator(),
      error: (error, stackTrace) => Text(error.toString()),
    );
  }
}
```

## Validation

- The page does not call the network directly.
- The controller owns loading state.
- The repository returns domain entities.
