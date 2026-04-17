import 'package:flutter/material.dart';

import '../../core/auth/token_store.dart';

class ProtectedShell extends StatelessWidget {
  final TokenStore tokenStore;
  final WidgetBuilder signedOutBuilder;
  final WidgetBuilder signedInBuilder;

  const ProtectedShell({
    super.key,
    required this.tokenStore,
    required this.signedOutBuilder,
    required this.signedInBuilder,
  });

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: tokenStore.readSession(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const Scaffold(body: Center(child: CircularProgressIndicator()));
        }

        final session = snapshot.data;
        return session == null ? signedOutBuilder(context) : signedInBuilder(context);
      },
    );
  }
}
