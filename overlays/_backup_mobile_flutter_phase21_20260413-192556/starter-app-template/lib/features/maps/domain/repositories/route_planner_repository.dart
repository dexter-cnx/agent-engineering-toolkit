import '../entities/customer_stop.dart';
import '../entities/route_plan.dart';

abstract class RoutePlannerRepository {
  Future<RoutePlan> planRoute(List<CustomerStop> stops);
}
