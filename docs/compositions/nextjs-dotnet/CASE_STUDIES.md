# Case Studies

## Case study 1: Authenticated profile update
1. frontend common defines form and error states
2. Next.js overlay places the route and protection
3. backend common defines contract and permission shape
4. backend-dotnet implements JWT, validation, and persistence
5. review: confirm the UI does not own permission logic and the backend rejects unauthorized updates

## Case study 2: CRUD admin table
1. frontend common defines list/detail and loading states
2. Next.js overlay places the page and data fetch boundaries
3. backend common defines the resource contract
4. backend-dotnet implements API, EF Core, and validation
5. review: confirm filters, pagination, and error states stay in the frontend overlay while validation stays on the backend

## Case study 3: File upload flow
1. frontend common defines input and failure states
2. Next.js overlay handles UI boundaries
3. backend common defines file safety rules
4. backend-dotnet implements upload validation and storage
5. review: confirm file type and size checks happen before persistence and that access rules stay on the backend
