using NextjsDotnetApp.Application.Contracts.Auth;
using NextjsDotnetApp.Application.Interfaces;

namespace NextjsDotnetApp.Infrastructure.Services;

public sealed class AuthService(
    ITokenService tokens,
    IRefreshTokenStore refreshTokens) : IAuthService
{
    private static readonly SessionUser DemoUser =
        new("demo-user", "admin@example.com", "Demo Admin", ["admin"]);

    public async Task<SessionResponse> LoginAsync(LoginRequest request, CancellationToken cancellationToken)
    {
        if (request.Email != "admin@example.com" || request.Password != "password123")
        {
            throw new InvalidOperationException("Invalid email or password.");
        }

        var accessToken = tokens.CreateAccessToken(DemoUser, TimeSpan.FromMinutes(15));
        var refreshToken = tokens.CreateRefreshToken(DemoUser, TimeSpan.FromDays(7));
        var refreshHash = tokens.HashToken(refreshToken);
        await refreshTokens.StoreAsync(DemoUser.Id, refreshHash, DateTimeOffset.UtcNow.AddDays(7), cancellationToken);

        return new SessionResponse(
            accessToken,
            refreshToken,
            DateTimeOffset.UtcNow.AddMinutes(15),
            DemoUser);
    }

    public async Task<SessionResponse?> RefreshAsync(string refreshToken, CancellationToken cancellationToken)
    {
        var refreshHash = tokens.HashToken(refreshToken);
        if (!await refreshTokens.IsActiveAsync(refreshHash, cancellationToken))
        {
            return null;
        }

        var rotatedRefresh = tokens.CreateRefreshToken(DemoUser, TimeSpan.FromDays(7));
        var accessToken = tokens.CreateAccessToken(DemoUser, TimeSpan.FromMinutes(15));
        await refreshTokens.RevokeAsync(refreshHash, tokens.HashToken(rotatedRefresh), cancellationToken);
        await refreshTokens.StoreAsync(DemoUser.Id, tokens.HashToken(rotatedRefresh), DateTimeOffset.UtcNow.AddDays(7), cancellationToken);

        return new SessionResponse(
            accessToken,
            rotatedRefresh,
            DateTimeOffset.UtcNow.AddMinutes(15),
            DemoUser);
    }
}
