# flutter-network-dio

## Purpose
Design and implement a governed Dio HTTP boundary for a Flutter app so that transport,
auth headers, retry policy, DTO mapping, and error handling stay behind a typed network layer.

## Use when
- The app needs a reusable Dio client with interceptors, auth headers, retry logic, and error mapping
- Network code should stay out of widgets and presentation state
- The change needs to preserve clean-architecture boundaries
- You need a typed boundary that can be reviewed, tested, and promoted safely

## Do NOT use when
- The task is only adding one-off ad hoc HTTP calls in a prototype
- The app does not use Dio and should keep its current networking stack
- The request is purely about UI rendering, routing, or state management without network boundary changes
- You need a backend API redesign instead of a Flutter client boundary update

## Inputs required
- Current Dio setup file path or the file that will own the HTTP boundary
- Auth source for access tokens or session credentials
- Retry and timeout requirements
- DTO or API contract shape that the client must decode
- Error mapping rules for transport and server failures

## Constraints
- Keep interceptors, auth headers, and retry policy inside the HTTP boundary
- Keep DTO parsing and error mapping typed
- Avoid calling Dio directly from widgets or view models
- Avoid hardcoding environment-specific URLs inside UI code
- Preserve existing clean-architecture layer boundaries

## Step-by-step workflow
1. Locate the current network entry point and identify the file that should own the Dio client.
2. Define the base URL, timeout, auth header strategy, retry strategy, and logging policy.
3. Implement or update the Dio client so interceptors attach auth headers before requests are sent.
4. Add typed DTO parsing and map transport or server failures to a typed domain error.
5. Keep repository or datasource code as the only consumer of the Dio client.
6. Add or update tests for success, unauthorized, timeout, and error-mapping cases.
7. Run Flutter analysis and the relevant tests before any promotion or handoff.

## Output contract
- A Dio client factory or provider in the network layer
- Typed request/response mapping for the API boundary
- Auth and retry interceptors kept behind the boundary
- Typed error mapping for transport and server failures
- Tests that cover the critical boundary behavior

## Validation checklist
- Run `flutter analyze` and confirm there are no dependency or boundary violations
- Run the targeted Flutter tests for the network boundary and confirm they pass
- Grep the presentation layer for direct `Dio()` usage and confirm it is absent
- Confirm the auth header is attached by the network layer and not by widgets
- Inspect the error mapping and confirm network failures become typed failures

## Related skills
- `policy-clean-architecture`
- `policy-no-business-logic-in-widget`
- `policy-testing-minimum`

## References
- [`../../examples/flutter_deeplink_full_cycle.md`](../../examples/flutter_deeplink_full_cycle.md)
- [`../../../docs/karpathy-guide.md`](../../../docs/karpathy-guide.md)
- [`prompts/governance-prompt.md`](prompts/governance-prompt.md)
- [`eval/cases/governance-smoke/README.md`](eval/cases/governance-smoke/README.md)
- [`skill.contract.yaml`](skill.contract.yaml)

## Real example
A Flutter app uses a `DioClient` provider in the data layer. The provider injects a base URL,
adds an auth interceptor that reads the current token, retries idempotent requests once on
transient network errors, and maps `401` responses to a typed `UnauthorizedFailure`.

## Real file output sample
```text
lib/core/network/dio_client.dart
lib/core/network/dio_interceptors.dart
lib/core/network/api_failure.dart
lib/features/orders/data/orders_remote_data_source.dart
test/core/network/dio_client_test.dart
```
