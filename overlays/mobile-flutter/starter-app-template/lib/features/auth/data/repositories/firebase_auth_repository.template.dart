// Rename this file to `firebase_auth_repository.dart` after adding firebase_auth.
//
// Suggested packages:
//   firebase_core
//   firebase_auth
//
// This file is intentionally not compiled by default.

import '../../domain/entities/app_user.dart';
import '../../domain/repositories/auth_repository.dart';

class FirebaseAuthRepository implements AuthRepository {
  @override
  Future<AppUser?> getCurrentUser() async {
    // final firebaseUser = FirebaseAuth.instance.currentUser;
    // if (firebaseUser == null) return null;
    // return AppUser(id: firebaseUser.uid, email: firebaseUser.email ?? '');
    throw UnimplementedError('Wire firebase_auth here');
  }

  @override
  Future<AppUser> signIn({required String email, required String password}) async {
    // final credential = await FirebaseAuth.instance.signInWithEmailAndPassword(
    //   email: email,
    //   password: password,
    // );
    // final user = credential.user!;
    // return AppUser(id: user.uid, email: user.email ?? email);
    throw UnimplementedError('Wire firebase_auth here');
  }

  @override
  Future<void> signOut() async {
    // await FirebaseAuth.instance.signOut();
    throw UnimplementedError('Wire firebase_auth here');
  }
}
