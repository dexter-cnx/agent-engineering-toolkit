# Full Stack Selection Matrix

Choose the composition by product shape first, not by framework preference alone.

| Product shape | Recommended composition | Why | Tradeoffs | Likely evolution path | When to switch |
|---|---|---|---|---|---|
| Internal Admin CRUD | `nextjs-fullstack-app` | Fast delivery, single deploy, low operational overhead | Tighter coupling between frontend and backend | Modular monolith, then split backend if needed | When multiple backend consumers appear or auth/persistence complexity grows |
| SaaS MVP | `nextjs-fullstack-app` | Fast iteration, one team can own the whole stack, schema-first contracts remain simple | Can become overloaded if the backend grows too quickly | Split frontend/backend while keeping shared contracts | When release cadence or runtime needs diverge |
| Enterprise API Platform | `nextjs-dotnet-app` | Clear backend layering, JWT/refresh flow, EF Core, validation, and explicit API ownership | More setup cost than a monolith starter | Backend becomes reusable platform; frontend can be swapped or expanded | When the frontend is thin and backend policies dominate |
| Mobile-first Product | `mobile-flutter` plus `backend-dotnet` or `backend-node` | Mobile UX stays native while backend can scale independently | More moving parts than a monolith | Add shared contracts and governed skills for each domain | When the mobile client outgrows the starter path |
| AI-heavy Workflow System | `backend-node` or `backend-dotnet` with `agent-karpathy` governance | Strong runtime control, automation hooks, and governed content generation | Requires careful token and regression discipline | Add composition-specific contracts and eval cases | When workflow steps become user-facing product surfaces |
| Public Content/Product Site with authenticated dashboard | `nextjs-nodebackend` or `nextjs-dotnet-app` | Public pages stay simple, authenticated dashboard has a clean API boundary | Split deployment adds coordination cost | Start with split frontend/backend, then consolidate shared contracts | When content pages and dashboard need different release cycles |

## Choosing the right path

- Pick `nextjs-fullstack-app` when one team owns the product and speed matters most.
- Pick `nextjs-dotnet-app` when you want a long-lived backend with explicit layering and a
  typed frontend client.
- Pick the overlay-specific starter when the repo already has a strong stack identity.

## Switching architectures

Switch when one of these becomes true:

- the backend has different scaling or release requirements than the frontend
- auth and permission logic become central enough to deserve a separate deployable unit
- the contract layer has stabilized and multiple clients now depend on it
- the team needs runtime-specific operational ownership

Do not switch just because the codebase feels large; switch when the business shape says the
current composition is no longer the right unit of ownership.
