---
tags:
  - tutorial
  - reuse
  - adoption
aliases:
  - Reuse Patterns
---

# Reuse Toolkit Patterns

This repo becomes more valuable when it can be reused cleanly without polluting downstream projects.

This tutorial helps choose the right adoption model.

## Option A: Use it as a submodule

Best when:

- you want easier upstream sync
- you want a clean separation between foundation and business repo
- you want toolkit updates to be versioned

Pros:

- explicit boundary
- easier updates
- less copy drift

Cons:

- requires submodule literacy
- new contributors may be confused at first

## Option B: Copy only what you need

Best when:

- the downstream repo is small
- you do not want submodule dependency
- you only need some prompts, templates, or docs

Pros:

- easy start
- no submodule overhead

Cons:

- drift happens fast
- maintenance is fully yours

## Option C: Use this as a foundation repo

Best when:

- you want your own toolkit derivative
- many repos in your team will reuse the workflow
- you want an organization-owned foundation layer

Pros:

- stronger standardization
- good for teams and organizations

Cons:

- requires real release discipline
- docs and audits become your responsibility

## Fast decision guide

Ask:

- do I need upstream sync
- can the team handle submodules
- do I want my own foundation layer
- do I only need a few prompts or the whole system

## Practical recommendation

### For a new client or product repo
Start with **submodule**

### For a very short-lived prototype
Copying the minimum may be enough

### For an internal engineering platform
Create your own foundation repo based on this approach

## Always keep these separate

- foundation rules
- stack overlays
- project-specific AGENTS.md
- project memory of the downstream repo

## Patterns to avoid

- moving business-specific rules into foundation root
- copying the whole repo when only a small part is used
- forking without a release and update policy
