namespace NextjsDotnetApp.Application.Contracts.Auth;

public sealed record LoginRequest(string Email, string Password);
public sealed record RegisterRequest(string Email, string Password, string DisplayName);
public sealed record SessionResponse(
    string AccessToken,
    string RefreshToken,
    DateTimeOffset ExpiresAt,
    SessionUser User);

public sealed record SessionUser(string Id, string Email, string DisplayName, IReadOnlyList<string> Roles);
