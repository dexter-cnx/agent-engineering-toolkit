import '../../domain/entities/app_user.dart';
import '../../domain/repositories/auth_repository.dart';
import '../datasources/firebase_auth_datasource.dart';

class FirebaseAuthRepository implements AuthRepository {
  final FirebaseAuthDatasource datasource;

  FirebaseAuthRepository(this.datasource);

  @override
  Future<AppUser?> getCurrentUser() async {
    final raw = await datasource.currentUser();
    if (raw == null) return null;
    return AppUser(
      id: raw['id'] as String,
      email: raw['email'] as String?,
      displayName: raw['displayName'] as String?,
    );
  }

  @override
  Future<AppUser> signInWithEmail({
    required String email,
    required String password,
  }) async {
    final raw = await datasource.signInWithEmail(
      email: email,
      password: password,
    );
    return AppUser(
      id: raw['id'] as String,
      email: raw['email'] as String?,
      displayName: raw['displayName'] as String?,
    );
  }

  @override
  Future<void> signOut() => datasource.signOut();
}
