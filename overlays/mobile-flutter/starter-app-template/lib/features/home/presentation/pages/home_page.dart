import 'package:easy_localization/easy_localization.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../../auth/presentation/controllers/auth_controller.dart';
import '../controllers/home_controller.dart';

class HomePage extends ConsumerWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final summaryAsync = ref.watch(homeControllerProvider);
    final authState = ref.watch(authControllerProvider);

    return Scaffold(
      appBar: AppBar(
        title: Text('home_title'.tr()),
        actions: [
          if (authState.isAuthenticated)
            IconButton(
              onPressed: () => ref.read(authControllerProvider.notifier).signOut(),
              icon: const Icon(Icons.logout),
              tooltip: 'logout_cta'.tr(),
            )
          else
            TextButton(
              onPressed: () => context.go('/login'),
              child: Text('login_cta'.tr()),
            ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: summaryAsync.when(
          data: (summary) => Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(summary.title, style: Theme.of(context).textTheme.headlineSmall),
              const SizedBox(height: 8),
              Text('welcome_message'.tr(args: [summary.pendingTasks.toString()])),
              const SizedBox(height: 24),
              Card(
                child: ListTile(
                  leading: const Icon(Icons.login),
                  title: Text('auth_feature_title'.tr()),
                  subtitle: Text('auth_feature_subtitle'.tr()),
                  trailing: const Icon(Icons.chevron_right),
                  onTap: () => context.go('/login'),
                ),
              ),
            ],
          ),
          error: (error, stack) => Center(child: Text('generic_error'.tr())),
          loading: () => const Center(child: CircularProgressIndicator()),
        ),
      ),
    );
  }
}
