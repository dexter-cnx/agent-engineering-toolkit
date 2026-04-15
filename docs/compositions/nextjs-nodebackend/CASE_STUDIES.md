# Case Studies

## Case study 1: Authenticated profile update
1. frontend common defines form and error states
2. Next.js overlay places the route and protection
3. backend common defines contract and permission shape
4. backend-node implements token issuance, validation, and persistence
5. review: confirm the UI does not own permission logic and the Node backend rejects unauthorized updates

## Case study 2: CRUD admin table
1. frontend common defines list/detail and loading states
2. Next.js overlay places the page and data fetch boundaries
3. backend common defines the resource contract
4. backend-node implements API, repositories, and validation behavior
5. review: confirm filters, pagination, and error states stay in the frontend overlay while validation stays on the backend

## Case study 3: Webhook/job flow
1. frontend common defines trigger and feedback states
2. Next.js overlay handles UI boundaries
3. backend common defines job safety and contract rules
4. backend-node implements handler, service orchestration, and async processing
5. review: confirm queueing and external calls happen behind service and adapter boundaries
