import '../../domain/entities/home_summary.dart';
import '../../domain/repositories/home_repository.dart';

class MockHomeRepository implements HomeRepository {
  @override
  Future<HomeSummary> loadSummary() async {
    return const HomeSummary(title: 'Overlay Starter Dashboard', pendingTasks: 3);
  }
}
