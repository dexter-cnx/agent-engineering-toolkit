using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Security.Cryptography;
using System.Text;
using Microsoft.Extensions.Configuration;
using Microsoft.IdentityModel.Tokens;
using NextjsDotnetApp.Application.Contracts.Auth;
using NextjsDotnetApp.Application.Interfaces;

namespace NextjsDotnetApp.Infrastructure.Security;

public sealed class TokenService(IConfiguration configuration) : ITokenService
{
    private readonly byte[] _accessKey = Encoding.UTF8.GetBytes(configuration["Jwt:AccessSecret"] ?? "dev-access-secret-32-chars-minimum!");
    private readonly byte[] _refreshKey = Encoding.UTF8.GetBytes(configuration["Jwt:RefreshSecret"] ?? "dev-refresh-secret-32-chars-min!");
    private readonly string _issuer = configuration["Jwt:Issuer"] ?? "NextjsDotnetApp";
    private readonly string _audience = configuration["Jwt:Audience"] ?? "NextjsDotnetApp.Web";

    public string CreateAccessToken(SessionUser user, TimeSpan lifetime)
    {
        var credentials = new SigningCredentials(new SymmetricSecurityKey(_accessKey), SecurityAlgorithms.HmacSha256);
        var claims = new List<Claim>
        {
            new(JwtRegisteredClaimNames.Sub, user.Id),
            new(JwtRegisteredClaimNames.Email, user.Email),
            new("displayName", user.DisplayName),
            new(ClaimTypes.Role, string.Join(",", user.Roles)),
        };

        var token = new JwtSecurityToken(
            issuer: _issuer,
            audience: _audience,
            claims: claims,
            expires: DateTime.UtcNow.Add(lifetime),
            signingCredentials: credentials);

        return new JwtSecurityTokenHandler().WriteToken(token);
    }

    public string CreateRefreshToken(SessionUser user, TimeSpan lifetime)
    {
        var credentials = new SigningCredentials(new SymmetricSecurityKey(_refreshKey), SecurityAlgorithms.HmacSha256);
        var token = new JwtSecurityToken(
            issuer: _issuer,
            audience: _audience,
            claims: [new Claim(JwtRegisteredClaimNames.Sub, user.Id), new Claim("tokenType", "refresh")],
            expires: DateTime.UtcNow.Add(lifetime),
            signingCredentials: credentials);

        return new JwtSecurityTokenHandler().WriteToken(token);
    }

    public string HashToken(string token)
    {
        var bytes = SHA256.HashData(Encoding.UTF8.GetBytes(token));
        return Convert.ToHexString(bytes);
    }
}
