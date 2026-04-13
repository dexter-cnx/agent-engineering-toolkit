import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_overlay_starter/features/auth/data/repositories/mock_auth_repository.dart';

void main() {
  test('mock auth repository signs in and stores current user', () async {
    final repository = MockAuthRepository();
    final user = await repository.signIn(
      email: 'demo@example.com',
      password: 'password123',
    );

    expect(user.email, 'demo@example.com');
    expect((await repository.getCurrentUser())?.email, 'demo@example.com');
  });
}
