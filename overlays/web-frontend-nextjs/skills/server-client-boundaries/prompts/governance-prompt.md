Follow `AGENTS.md` and `overlays/web-frontend-nextjs/AGENTS.overlay.md`.
Use the `server-client-boundaries` skill contract before implementation.

Task:
Update the consuming Next.js repository with a governed server/client split.

Requirements:
- keep server-only reads on the server
- keep client-only interaction in the client
- keep the implementation regression-safe
- keep token growth under the Karpathy policy

Deliver:
1. file plan
2. boundary plan
3. implementation notes
4. verification notes
