# Shared Skill Contract

Use this contract for atomic .NET backend skills in this overlay.

## Every skill must define
- purpose
- use when
- do not use when
- inputs required
- outputs expected
- workflow steps
- validation checklist
- references to prompts or examples

## Boundary rules
- keep ASP.NET Core mechanics out of common backend skills
- keep transport handlers thin
- keep DI, EF Core, and middleware decisions explicit
- keep auth and validation visible

