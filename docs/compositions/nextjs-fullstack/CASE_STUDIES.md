# Case Studies

## Case study 1: Authenticated profile update

1. frontend common defines form and error states
2. Next.js overlay places the route and protection
3. backend common defines contract and permission shape
4. the Next.js app implements auth entry points and persistence updates
5. review: UI must not own permissions; server logic rejects unauthorized updates

## Case study 2: CRUD admin table

1. frontend common defines list/detail and loading states
2. Next.js overlay places the page and data fetch boundaries
3. backend common defines the resource contract
4. the Next.js app implements the route handler, validation, and persistence adapter
5. review: frontend owns filters, pagination, and errors; server code owns validation

## Case study 3: Webhook/job flow

1. frontend common defines trigger and feedback states
2. Next.js overlay handles UI boundaries
3. backend common defines job safety and contract rules
4. the Next.js app implements the server entry point and async processing path
5. review: queueing and external calls stay behind service and adapter boundaries
