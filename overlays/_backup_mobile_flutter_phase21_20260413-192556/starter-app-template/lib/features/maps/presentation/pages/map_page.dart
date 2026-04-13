import 'package:flutter/material.dart';

import '../../data/sample_customer_stops.dart';
import '../widgets/map_summary_card.dart';

class MapPage extends StatelessWidget {
  const MapPage({super.key});

  @override
  Widget build(BuildContext context) {
    final stops = sampleCustomerStops;
    return Scaffold(
      appBar: AppBar(title: const Text('Map')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            Expanded(
              child: Container(
                width: double.infinity,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  border: Border.all(),
                  borderRadius: BorderRadius.circular(16),
                ),
                child: const Text('Map widget adapter goes here'),
              ),
            ),
            const SizedBox(height: 16),
            MapSummaryCard(stops: stops),
          ],
        ),
      ),
    );
  }
}
