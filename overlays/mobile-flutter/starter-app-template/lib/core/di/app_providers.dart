import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../features/auth/data/repositories/mock_auth_repository.dart';
import '../../features/auth/domain/repositories/auth_repository.dart';
import '../../features/auth/domain/usecases/get_current_user_usecase.dart';
import '../../features/auth/domain/usecases/sign_in_usecase.dart';
import '../../features/auth/domain/usecases/sign_out_usecase.dart';
import '../../features/home/data/repositories/mock_home_repository.dart';
import '../../features/home/domain/repositories/home_repository.dart';
import '../../features/home/domain/usecases/get_home_summary_usecase.dart';
import '../network/dio_client.dart';

final dioProvider = Provider((ref) => buildDioClient());

final authRepositoryProvider = Provider<AuthRepository>((ref) {
  return MockAuthRepository();
});

final getCurrentUserUseCaseProvider = Provider((ref) {
  return GetCurrentUserUseCase(ref.read(authRepositoryProvider));
});

final signInUseCaseProvider = Provider((ref) {
  return SignInUseCase(ref.read(authRepositoryProvider));
});

final signOutUseCaseProvider = Provider((ref) {
  return SignOutUseCase(ref.read(authRepositoryProvider));
});

final homeRepositoryProvider = Provider<HomeRepository>((ref) {
  return MockHomeRepository();
});

final getHomeSummaryUseCaseProvider = Provider((ref) {
  return GetHomeSummaryUseCase(ref.read(homeRepositoryProvider));
});
