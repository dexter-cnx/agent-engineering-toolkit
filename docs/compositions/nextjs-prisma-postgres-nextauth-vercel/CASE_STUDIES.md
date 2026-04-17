# Case Studies

## Case study 1: authenticated profile update

1. frontend common defines form and error states
2. Next.js overlay places the route and protection
3. backend common defines session and permission shape
4. the Next.js app implements NextAuth.js checks, the server action, and the Prisma update
5. review: UI must not own permissions; server logic rejects unauthorized updates

## Case study 2: CRUD admin table

1. frontend common defines list/detail and loading states
2. Next.js overlay places the page and server-action boundary
3. backend common defines the resource contract
4. the Next.js app implements validation, Prisma queries, and mutation handling
5. review: frontend owns filters, pagination, and errors; server code owns data integrity

## Case study 3: organization access control

1. frontend common defines gated UI states
2. Next.js overlay places the protected route
3. backend common defines the role and membership rule
4. the Next.js app checks the session and loads allowed data only
5. review: access control stays server-side and is not inferred from client state
