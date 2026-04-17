import 'package:flutter/material.dart';

import 'config/app_config.dart';
import 'core/api/api_client.dart';
import 'core/auth/token_store.dart';
import 'features/auth/login_screen.dart';
import 'features/auth/protected_shell.dart';
import 'features/posts/posts_repository.dart';
import 'features/posts/posts_screen.dart';

class FlutterApiClientApp extends StatefulWidget {
  final AppConfig config;

  const FlutterApiClientApp({super.key, required this.config});

  @override
  State<FlutterApiClientApp> createState() => _FlutterApiClientAppState();
}

class _FlutterApiClientAppState extends State<FlutterApiClientApp> {
  void _reload() {
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    final tokenStore = const SecureTokenStore();
    final apiClient = ApiClient(baseUrl: widget.config.apiBaseUrl, tokenStore: tokenStore);
    final repository = PostsRepository(client: apiClient);

    return MaterialApp(
      title: 'Flutter API Client Reference',
      theme: ThemeData(useMaterial3: true),
      home: ProtectedShell(
        tokenStore: tokenStore,
        signedOutBuilder: (context) => LoginScreen(
          client: apiClient,
          tokenStore: tokenStore,
          onSignedIn: _reload,
        ),
        signedInBuilder: (context) => PostsScreen(
          repository: repository,
          tokenStore: tokenStore,
          onSignOut: _reload,
        ),
      ),
    );
  }
}
