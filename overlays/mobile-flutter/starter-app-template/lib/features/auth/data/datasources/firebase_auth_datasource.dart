class FirebaseAuthDatasource {
  Future<Map<String, dynamic>?> currentUser() async {
    // TODO: wire firebase_auth here
    return null;
  }

  Future<Map<String, dynamic>> signInWithEmail({
    required String email,
    required String password,
  }) async {
    // TODO: wire firebase_auth sign in
    return {
      'id': 'stub-user',
      'email': email,
      'displayName': null,
    };
  }

  Future<void> signOut() async {
    // TODO: wire firebase_auth sign out
  }
}
