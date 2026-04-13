import '../entities/app_user.dart';

abstract class AuthRepository {
  Future<AppUser?> getCurrentUser();
  Future<AppUser> signIn({required String email, required String password});
  Future<void> signOut();
}
