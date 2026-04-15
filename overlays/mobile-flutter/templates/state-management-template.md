# State Management Template

## Riverpod

```dart
final profileControllerProvider =
    AsyncNotifierProvider<ProfileController, ProfileState>(
  ProfileController.new,
);
```

## GetX

```dart
class ProfileController extends GetxController {
  final RxBool isLoading = false.obs;
}
```

## Output sample

- `lib/features/profile/presentation/controllers/profile_controller.dart`
- `lib/features/profile/presentation/providers/profile_providers.dart`
