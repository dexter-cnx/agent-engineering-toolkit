import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../../../core/di/app_providers.dart';
import 'auth_state.dart';

final authControllerProvider = NotifierProvider<AuthController, AuthState>(
  AuthController.new,
);

class AuthController extends Notifier<AuthState> {
  @override
  AuthState build() {
    _bootstrap();
    return const AuthState();
  }

  Future<void> _bootstrap() async {
    final getCurrentUser = ref.read(getCurrentUserUseCaseProvider);
    final user = await getCurrentUser();
    state = state.copyWith(user: user);
  }

  Future<void> signIn({required String email, required String password}) async {
    state = state.copyWith(isLoading: true, clearError: true);
    try {
      final signIn = ref.read(signInUseCaseProvider);
      final user = await signIn(email: email, password: password);
      state = state.copyWith(user: user, isLoading: false, clearError: true);
    } catch (_) {
      state = state.copyWith(isLoading: false, errorMessage: 'login_failed');
    }
  }

  Future<void> signOut() async {
    state = state.copyWith(isLoading: true, clearError: true);
    final signOut = ref.read(signOutUseCaseProvider);
    await signOut();
    state = state.copyWith(user: null, isLoading: false);
  }
}
