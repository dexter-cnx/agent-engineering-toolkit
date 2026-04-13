import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../controllers/auth_controller.dart';

class LoginPage extends ConsumerStatefulWidget {
  const LoginPage({super.key});

  @override
  ConsumerState<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends ConsumerState<LoginPage> {
  final _emailController = TextEditingController(text: 'demo@example.com');
  final _passwordController = TextEditingController(text: 'password123');

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final authState = ref.watch(authControllerProvider);

    ref.listen(authControllerProvider, (previous, next) {
      if (next.isAuthenticated && context.mounted) {
        context.go('/');
      }
    });

    return Scaffold(
      appBar: AppBar(title: Text('login_title'.tr())),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: _emailController,
              decoration: InputDecoration(labelText: 'email_label'.tr()),
            ),
            const SizedBox(height: 12),
            TextField(
              controller: _passwordController,
              obscureText: true,
              decoration: InputDecoration(labelText: 'password_label'.tr()),
            ),
            const SizedBox(height: 16),
            FilledButton(
              onPressed: authState.isLoading
                  ? null
                  : () => ref.read(authControllerProvider.notifier).signIn(
                        email: _emailController.text.trim(),
                        password: _passwordController.text,
                      ),
              child: Text(
                authState.isLoading ? 'loading_label'.tr() : 'login_cta'.tr(),
              ),
            ),
            if (authState.errorMessage != null) ...[
              const SizedBox(height: 12),
              Text(authState.errorMessage!.tr()),
            ],
          ],
        ),
      ),
    );
  }
}
