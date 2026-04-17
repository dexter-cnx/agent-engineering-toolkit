using Microsoft.EntityFrameworkCore;
using NextjsDotnetApp.Application.Interfaces;
using NextjsDotnetApp.Domain.Entities;
using NextjsDotnetApp.Infrastructure.Persistence;

namespace NextjsDotnetApp.Infrastructure.Security;

public sealed class RefreshTokenStore(AppDbContext db) : IRefreshTokenStore
{
    public async Task StoreAsync(string userId, string tokenHash, DateTimeOffset expiresAt, CancellationToken cancellationToken)
    {
        db.RefreshTokens.Add(new RefreshToken
        {
            UserId = userId,
            TokenHash = tokenHash,
            ExpiresAt = expiresAt,
        });
        await db.SaveChangesAsync(cancellationToken);
    }

    public Task<bool> IsActiveAsync(string tokenHash, CancellationToken cancellationToken) =>
        db.RefreshTokens.AnyAsync(
            token => token.TokenHash == tokenHash && token.RevokedAt == null && token.ExpiresAt > DateTimeOffset.UtcNow,
            cancellationToken);

    public async Task RevokeAsync(string tokenHash, string? replacedByHash, CancellationToken cancellationToken)
    {
        var token = await db.RefreshTokens.FirstOrDefaultAsync(x => x.TokenHash == tokenHash, cancellationToken);
        if (token is null)
        {
            return;
        }

        token.RevokedAt = DateTimeOffset.UtcNow;
        token.ReplacedByTokenHash = replacedByHash;
        await db.SaveChangesAsync(cancellationToken);
    }
}
