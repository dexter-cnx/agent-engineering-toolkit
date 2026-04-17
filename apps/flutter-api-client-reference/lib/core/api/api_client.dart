import 'dart:convert';

import 'package:http/http.dart' as http;

import 'api_models.dart';
import '../auth/token_store.dart';

class ApiClient {
  final Uri baseUrl;
  final TokenStore tokenStore;
  final http.Client _client;

  ApiClient({
    required this.baseUrl,
    required this.tokenStore,
    http.Client? client,
  }) : _client = client ?? http.Client();

  Future<JsonMap> getJson(String path, {bool authenticated = true}) async {
    return _requestJson('GET', path, authenticated: authenticated);
  }

  Future<JsonMap> postJson(
    String path,
    JsonMap body, {
    bool authenticated = true,
  }) async {
    return _requestJson('POST', path, body: body, authenticated: authenticated);
  }

  Future<JsonMap> putJson(
    String path,
    JsonMap body, {
    bool authenticated = true,
  }) async {
    return _requestJson('PUT', path, body: body, authenticated: authenticated);
  }

  Future<JsonMap> deleteJson(String path, {bool authenticated = true}) async {
    return _requestJson('DELETE', path, authenticated: authenticated);
  }

  Future<JsonMap> _requestJson(
    String method,
    String path, {
    JsonMap? body,
    bool authenticated = true,
  }) async {
    final uri = baseUrl.resolve(path.startsWith('/') ? path.substring(1) : path);
    final headers = <String, String>{'Accept': 'application/json'};

    if (body != null) {
      headers['Content-Type'] = 'application/json';
    }

    if (authenticated) {
      final session = await tokenStore.readSession();
      final token = session?.accessToken;
      if (token != null && token.isNotEmpty) {
        headers['Authorization'] = 'Bearer $token';
      }
    }

    final response = await _client.send(
      http.Request(method, uri)
        ..headers.addAll(headers)
        ..body = body == null ? '' : jsonEncode(body),
    );

    final raw = await response.stream.bytesToString();
    final decoded = raw.isEmpty ? <String, dynamic>{} : jsonDecode(raw) as JsonMap;

    if (response.statusCode >= 400) {
      throw ApiException.fromEnvelope(decoded);
    }

    return decoded;
  }
}
