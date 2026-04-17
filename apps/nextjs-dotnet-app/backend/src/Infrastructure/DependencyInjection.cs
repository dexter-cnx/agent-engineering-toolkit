using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using NextjsDotnetApp.Application.Interfaces;
using NextjsDotnetApp.Infrastructure.Persistence;
using NextjsDotnetApp.Infrastructure.Repositories;
using NextjsDotnetApp.Infrastructure.Security;
using NextjsDotnetApp.Infrastructure.Services;

namespace NextjsDotnetApp.Infrastructure;

public static class DependencyInjection
{
    public static IServiceCollection AddInfrastructure(this IServiceCollection services, IConfiguration configuration)
    {
        services.AddDbContext<AppDbContext>(options =>
        {
            options.UseSqlite(configuration.GetConnectionString("DefaultConnection") ?? "Data Source=app.db");
        });

        services.AddScoped<ITokenService, TokenService>();
        services.AddScoped<IRefreshTokenStore, RefreshTokenStore>();
        services.AddScoped<IAuthService, AuthService>();
        services.AddScoped<IPostService, PostService>();

        return services;
    }
}
