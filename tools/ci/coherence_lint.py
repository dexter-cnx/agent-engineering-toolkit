#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

CANONICAL_CHAIN = "README.md -> docs/get-started.md -> docs/adoption-paths.md -> docs/overlays.md"
COMPAT_DOCS = [
    "docs/legacy/START_HERE.md",
    "docs/legacy/README_START_HERE.md",
    "docs/legacy/HOW_TO_USE.md",
    "docs/legacy/ONBOARDING_MINIMAL.md",
    "docs/legacy/ONBOARDING_FULL.md",
    "docs/legacy/INDEX_CANONICAL.md",
]
FIRST_CLASS_OVERLAYS = [
    "overlays/agent-karpathy/README.md",
    "overlays/mobile-flutter/README.md",
    "overlays/unity/README.md",
]


def fail(msg: str) -> None:
    print(f"COHERENCE_LINT_FAIL: {msg}")
    sys.exit(1)


def assert_contains(path: str, needle: str, desc: str) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    normalized = text.replace("`", "")
    if needle not in normalized:
        fail(f"{path} missing {desc}: {needle}")


def check_onboarding_chain_consistency() -> None:
    targets = [
        "README.md",
        "AGENTS.md",
        "docs/get-started.md",
        "docs/reference/canonical-doc-map.md",
    ]
    for path in targets:
        assert_contains(path, CANONICAL_CHAIN, "canonical onboarding chain")

    surface_map = (ROOT / "docs/reference/repo-surface-status.md").read_text(encoding="utf-8")
    if "README.md" not in surface_map or "docs/" not in surface_map:
        fail("docs/reference/repo-surface-status.md must classify README.md and docs/ as canonical surfaces")


def check_compat_redirects() -> None:
    for rel in COMPAT_DOCS:
        text = (ROOT / rel).read_text(encoding="utf-8")
        lower = text.lower()
        if not text.startswith("# Compatibility Redirect (Legacy)"):
            fail(f"{rel} must begin with compatibility redirect heading")
        if "not canonical" not in lower:
            fail(f"{rel} must explicitly state non-canonical status")
        if "[README.md](../README.md)" not in text:
            fail(f"{rel} must redirect to README.md")
        if "[docs/get-started.md](../get-started.md)" not in text:
            fail(f"{rel} must redirect to docs/get-started.md")
        if "canonical front door" not in lower:
            fail(f"{rel} must clearly label README.md as canonical front door")


def check_first_class_overlay_contract() -> None:
    required_marker_sets = [
        ["## purpose"],
        ["when to use"],
        ["when not to use"],
        ["## canonical links"],
        ["## expected consuming repo shape", "## expected consuming repository shape"],
        ["## verify commands"],
        ["examples", "templates"],
        ["## memory conventions"],
        ["## review checklist"],
    ]
    for rel in FIRST_CLASS_OVERLAYS:
        lower = (ROOT / rel).read_text(encoding="utf-8").lower()
        for marker_group in required_marker_sets:
            if not any(marker in lower for marker in marker_group):
                fail(f"{rel} missing first-class overlay contract marker group: {marker_group}")


def main() -> None:
    check_onboarding_chain_consistency()
    check_compat_redirects()
    check_first_class_overlay_contract()
    print("COHERENCE_LINT_PASS: onboarding coherence, compatibility redirects, and first-class overlay contracts are consistent.")


if __name__ == "__main__":
    main()
