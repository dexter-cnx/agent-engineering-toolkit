import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../../../core/di/app_providers.dart';
import '../../domain/entities/home_summary.dart';

final homeControllerProvider = FutureProvider<HomeSummary>((ref) async {
  final useCase = ref.read(getHomeSummaryUseCaseProvider);
  return useCase();
});
