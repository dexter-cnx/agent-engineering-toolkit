# Case Studies

## Case study 1: Authenticated profile update
1. frontend common defines form and error states
2. Next.js overlay places the route and protection
3. backend common defines contract and permission shape
4. python-service implements token/session handling, validation, and persistence
5. review: confirm the UI does not own permission logic and the Python backend rejects unauthorized updates

## Case study 2: CRUD admin table
1. frontend common defines list/detail and loading states
2. Next.js overlay places the page and data fetch boundaries
3. backend common defines the resource contract
4. python-service implements API, repository, and validation behavior
5. review: confirm filters, pagination, and error states stay in the frontend overlay while validation stays on the backend

## Case study 3: Async file processing flow
1. frontend common defines input and failure states
2. Next.js overlay handles UI boundaries
3. backend common defines file safety rules
4. python-service implements upload validation, queueing, and worker processing
5. review: confirm file type and size checks happen before queueing and that access rules stay on the backend
