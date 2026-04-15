# Architecture Policy

## Principles

- Keep feature boundaries explicit.
- Put business logic in domain, state, or repository layers, not widgets.
- Keep external SDKs behind adapters and repositories.
- Use dependency direction from presentation -> state -> domain -> data.
- Prefer one-way data flow for feature state.

## Rules

- Do not import Firebase, Dio, or storage SDKs directly into presentation widgets.
- Do not let routing code own repository logic.
- Do not let token/theme generation leak into feature behavior.
- Do not add a new state management stack unless the project standard requires it.

## Verification

- Confirm file placement matches the selected architecture.
- Confirm dependencies only point inward.
- Confirm tests cover non-trivial domain and state behavior.
