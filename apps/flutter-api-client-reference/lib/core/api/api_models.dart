import 'dart:convert';

typedef JsonMap = Map<String, dynamic>;

class ApiException implements Exception {
  final String code;
  final String message;

  const ApiException(this.code, this.message);

  factory ApiException.fromEnvelope(JsonMap payload) {
    final error = ApiErrorEnvelope.fromJson(payload);
    return ApiException(error.code, error.message);
  }

  @override
  String toString() => '$code: $message';
}

class ApiErrorEnvelope {
  final String code;
  final String message;
  final String? field;

  const ApiErrorEnvelope({required this.code, required this.message, this.field});

  factory ApiErrorEnvelope.fromJson(JsonMap json) {
    final error = json['error'];
    final errorJson = error is Map<String, dynamic> ? error : <String, dynamic>{};
    return ApiErrorEnvelope(
      code: errorJson['code'] as String? ?? 'UNKNOWN_ERROR',
      message: errorJson['message'] as String? ?? 'Request failed',
      field: errorJson['field'] as String?,
    );
  }
}

class PageMeta {
  final int page;
  final int pageSize;
  final int total;
  final int totalPages;
  final bool hasNextPage;
  final bool hasPreviousPage;

  const PageMeta({
    required this.page,
    required this.pageSize,
    required this.total,
    required this.totalPages,
    required this.hasNextPage,
    required this.hasPreviousPage,
  });

  factory PageMeta.fromJson(JsonMap json) {
    return PageMeta(
      page: json['page'] as int,
      pageSize: json['pageSize'] as int,
      total: json['total'] as int,
      totalPages: json['totalPages'] as int,
      hasNextPage: json['hasNextPage'] as bool,
      hasPreviousPage: json['hasPreviousPage'] as bool,
    );
  }
}

class SessionUserDto {
  final String id;
  final String email;
  final String displayName;
  final List<String> roles;

  const SessionUserDto({
    required this.id,
    required this.email,
    required this.displayName,
    required this.roles,
  });

  factory SessionUserDto.fromJson(JsonMap json) {
    return SessionUserDto(
      id: json['id'] as String,
      email: json['email'] as String,
      displayName: json['displayName'] as String,
      roles: (json['roles'] as List<dynamic>).cast<String>(),
    );
  }
}

class SessionDto {
  final String accessToken;
  final String refreshToken;
  final DateTime expiresAt;
  final SessionUserDto user;

  const SessionDto({
    required this.accessToken,
    required this.refreshToken,
    required this.expiresAt,
    required this.user,
  });

  factory SessionDto.fromJson(JsonMap json) {
    return SessionDto(
      accessToken: json['accessToken'] as String,
      refreshToken: json['refreshToken'] as String,
      expiresAt: DateTime.parse(json['expiresAt'] as String),
      user: SessionUserDto.fromJson(json['user'] as JsonMap),
    );
  }

  JsonMap toJson() => {
        'accessToken': accessToken,
        'refreshToken': refreshToken,
        'expiresAt': expiresAt.toIso8601String(),
        'user': {
          'id': user.id,
          'email': user.email,
          'displayName': user.displayName,
          'roles': user.roles,
        },
      };

  String toStorageValue() => jsonEncode(toJson());

  factory SessionDto.fromStorageValue(String value) {
    return SessionDto.fromJson(jsonDecode(value) as JsonMap);
  }
}

class PostDto {
  final String id;
  final String title;
  final String slug;
  final String body;
  final bool published;
  final String authorId;
  final DateTime createdAt;
  final DateTime updatedAt;

  const PostDto({
    required this.id,
    required this.title,
    required this.slug,
    required this.body,
    required this.published,
    required this.authorId,
    required this.createdAt,
    required this.updatedAt,
  });

  factory PostDto.fromJson(JsonMap json) {
    return PostDto(
      id: json['id'] as String,
      title: json['title'] as String,
      slug: json['slug'] as String,
      body: json['body'] as String,
      published: json['published'] as bool,
      authorId: json['authorId'] as String,
      createdAt: DateTime.parse(json['createdAt'] as String),
      updatedAt: DateTime.parse(json['updatedAt'] as String),
    );
  }
}
