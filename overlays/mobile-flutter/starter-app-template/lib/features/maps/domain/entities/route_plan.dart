import 'customer_stop.dart';

class RoutePlan {
  final List<CustomerStop> stops;
  final double totalDistanceKm;

  const RoutePlan({
    required this.stops,
    required this.totalDistanceKm,
  });
}
