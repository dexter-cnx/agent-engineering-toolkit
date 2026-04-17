import 'package:flutter/material.dart';

import '../../core/api/api_client.dart';
import '../../core/api/api_models.dart';
import '../../core/auth/token_store.dart';

class LoginScreen extends StatefulWidget {
  final ApiClient client;
  final TokenStore tokenStore;
  final VoidCallback onSignedIn;

  const LoginScreen({
    super.key,
    required this.client,
    required this.tokenStore,
    required this.onSignedIn,
  });

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _email = TextEditingController(text: 'admin@example.com');
  final _password = TextEditingController(text: 'password123');
  String? _error;
  bool _loading = false;

  @override
  void dispose() {
    _email.dispose();
    _password.dispose();
    super.dispose();
  }

  Future<void> _submit() async {
    setState(() {
      _loading = true;
      _error = null;
    });

    try {
      final payload = await widget.client.postJson(
        '/auth/login',
        <String, dynamic>{
          'email': _email.text,
          'password': _password.text,
        },
        authenticated: false,
      );
      final session = SessionDto.fromJson(payload['data'] as JsonMap);
      await widget.tokenStore.saveSession(session);
      widget.onSignedIn();
    } on ApiException catch (error) {
      setState(() => _error = error.message);
    } finally {
      if (mounted) {
        setState(() => _loading = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 420),
          child: Padding(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                TextField(controller: _email, decoration: const InputDecoration(labelText: 'Email')),
                const SizedBox(height: 12),
                TextField(
                  controller: _password,
                  decoration: const InputDecoration(labelText: 'Password'),
                  obscureText: true,
                ),
                const SizedBox(height: 16),
                if (_error != null) Text(_error!, style: const TextStyle(color: Colors.red)),
                const SizedBox(height: 8),
                ElevatedButton(
                  onPressed: _loading ? null : _submit,
                  child: Text(_loading ? 'Signing in...' : 'Sign in'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
