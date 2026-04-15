# Firebase Integration Example

Example feature: sign-in flow with Firebase Auth and repository indirection.

## Reference files

- [`../templates/repository-template.md`](../templates/repository-template.md)
- [`../templates/state-management-template.md`](../templates/state-management-template.md)
- [`../skills/firebase/flutter-firebase-auth-adapter/SKILL.md`](../skills/firebase/flutter-firebase-auth-adapter/SKILL.md)
- [`../skills/firebase/flutter-firebase-auth-state/SKILL.md`](../skills/firebase/flutter-firebase-auth-state/SKILL.md)
- [`../skills/routing/flutter-go-router-redirect-guard/SKILL.md`](../skills/routing/flutter-go-router-redirect-guard/SKILL.md)

## Output tree

```text
lib/features/auth/
  data/datasources/firebase_auth_data_source.dart
  data/repositories/auth_repository_impl.dart
  domain/repositories/auth_repository.dart
  presentation/controllers/auth_controller.dart
  presentation/pages/sign_in_page.dart
```

## Flutter-specific implementation

```dart
class FirebaseAuthDataSource {
  FirebaseAuthDataSource(this._auth);

  final FirebaseAuth _auth;

  Future<User?> signInWithEmail(String email, String password) {
    return _auth.signInWithEmailAndPassword(
      email: email,
      password: password,
    ).then((result) => result.user);
  }
}
```

## Validation

- Firebase SDK usage is contained in the data layer.
- The controller consumes the repository, not Firebase directly.
- Auth redirects are handled by routing, not by the view.
