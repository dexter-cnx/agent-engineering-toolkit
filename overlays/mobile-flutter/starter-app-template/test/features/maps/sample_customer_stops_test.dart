import 'package:flutter_test/flutter_test.dart';
import 'package:starter_app_template/features/maps/data/sample_customer_stops.dart';

void main() {
  test('sample customer stops is seeded', () {
    expect(sampleCustomerStops.isNotEmpty, true);
    expect(sampleCustomerStops.first.id, 'c001');
  });
}
