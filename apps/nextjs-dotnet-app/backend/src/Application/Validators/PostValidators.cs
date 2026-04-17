using FluentValidation;
using NextjsDotnetApp.Application.Contracts.Posts;

namespace NextjsDotnetApp.Application.Validators;

public sealed class CreatePostRequestValidator : AbstractValidator<CreatePostRequest>
{
    public CreatePostRequestValidator()
    {
        RuleFor(x => x.Title).NotEmpty().MaximumLength(160);
        RuleFor(x => x.Slug).NotEmpty().MaximumLength(180);
        RuleFor(x => x.Body).NotEmpty();
    }
}

public sealed class UpdatePostRequestValidator : AbstractValidator<UpdatePostRequest>
{
    public UpdatePostRequestValidator()
    {
        RuleFor(x => x.Title).MaximumLength(160);
        RuleFor(x => x.Slug).MaximumLength(180);
    }
}
