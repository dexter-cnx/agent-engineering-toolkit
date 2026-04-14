# Auth Baseline

- Keep auth state separate from presentation.
- Gate protected routes in the routing layer or guard layer.
- Store tokens and session details in the approved persistence layer.
- Do not couple auth flow directly to reusable components.
