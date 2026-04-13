import 'package:flutter/widgets.dart';

Future<void> bootstrap(Future<Widget> Function() builder) async {
  WidgetsFlutterBinding.ensureInitialized();

  // TODO: initialize Firebase here
  // TODO: initialize environment/config here
  // TODO: initialize logging/observers here

  final app = await builder();
  runApp(app);
}
