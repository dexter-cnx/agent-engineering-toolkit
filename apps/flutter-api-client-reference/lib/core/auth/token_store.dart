import 'dart:convert';

import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import '../api/api_models.dart';

abstract class TokenStore {
  Future<SessionDto?> readSession();
  Future<void> saveSession(SessionDto session);
  Future<void> clear();
}

class SecureTokenStore implements TokenStore {
  static const _key = 'agent_toolkit_mobile_session';
  final FlutterSecureStorage _storage;

  const SecureTokenStore({FlutterSecureStorage? storage})
      : _storage = storage ?? const FlutterSecureStorage();

  @override
  Future<SessionDto?> readSession() async {
    final raw = await _storage.read(key: _key);
    if (raw == null || raw.isEmpty) return null;
    return SessionDto.fromJson(jsonDecode(raw) as JsonMap);
  }

  @override
  Future<void> saveSession(SessionDto session) {
    return _storage.write(key: _key, value: jsonEncode(session.toJson()));
  }

  @override
  Future<void> clear() {
    return _storage.delete(key: _key);
  }
}
