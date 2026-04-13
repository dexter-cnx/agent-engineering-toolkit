# Phase 4: Repo-ready additions

This phase turns the overlay from a documentation pack into a stronger execution starter.

## Added in this phase

- A compile-oriented starter feature under `starter-app-template/lib/features/home/`
- A mock auth feature under `starter-app-template/lib/features/auth/`
- A simple dashboard shell with navigation to login
- Repository/use case/state layering examples
- Basic widget and unit tests
- A CSV-to-JSON localization generator script
- A stricter CI sample with policy checks
- A lightweight policy-check script for repo hygiene

## Why this matters

Earlier phases gave the agent guidance, prompts, and templates. This phase adds concrete, copyable implementation structure so new repositories start from working patterns rather than empty folders.

## What is still intentionally left open

- Real backend wiring
- Real Firebase configuration values
- Production map provider keys
- FCM project-specific setup
- Flavor-specific secrets and release signing

Those should be adapted per repository using `repo-customization/repo-profile.example.yaml`.
