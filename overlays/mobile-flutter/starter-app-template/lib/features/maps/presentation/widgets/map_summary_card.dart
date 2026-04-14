import 'package:flutter/material.dart';

import '../../domain/entities/customer_stop.dart';

class MapSummaryCard extends StatelessWidget {
  final List<CustomerStop> stops;

  const MapSummaryCard({
    super.key,
    required this.stops,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Route summary',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            Text('Stops: ${stops.length}'),
            const SizedBox(height: 8),
            for (final stop in stops) Text('- ${stop.name}'),
          ],
        ),
      ),
    );
  }
}
