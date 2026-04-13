import 'coordinates.dart';

class CustomerStop {
  final String id;
  final String name;
  final Coordinates coordinates;

  const CustomerStop({
    required this.id,
    required this.name,
    required this.coordinates,
  });
}
