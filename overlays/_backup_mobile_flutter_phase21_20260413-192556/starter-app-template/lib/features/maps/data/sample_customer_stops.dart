import '../domain/entities/coordinates.dart';
import '../domain/entities/customer_stop.dart';

const sampleCustomerStops = [
  CustomerStop(
    id: 'c001',
    name: 'Customer A',
    coordinates: Coordinates(lat: 18.7883, lng: 98.9853),
  ),
  CustomerStop(
    id: 'c002',
    name: 'Customer B',
    coordinates: Coordinates(lat: 18.7950, lng: 98.9980),
  ),
  CustomerStop(
    id: 'c003',
    name: 'Customer C',
    coordinates: Coordinates(lat: 18.7800, lng: 99.0001),
  ),
];
