import 'package:flutter_test/flutter_test.dart';
import 'package:starter_app_template/features/auth/data/datasources/firebase_auth_datasource.dart';
import 'package:starter_app_template/features/auth/data/repositories/firebase_auth_repository.dart';

void main() {
  test('signInWithEmail returns mapped user', () async {
    final repo = FirebaseAuthRepository(FirebaseAuthDatasource());
    final user = await repo.signInWithEmail(
      email: 'demo@example.com',
      password: 'secret',
    );

    expect(user.id, 'stub-user');
    expect(user.email, 'demo@example.com');
  });
}
