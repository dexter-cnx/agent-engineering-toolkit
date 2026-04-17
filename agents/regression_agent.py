"""RegressionAgent — enforces hard guardrails before promotion.

Raises RegressionViolation on any failure. This is a hard stop.

Input payload:
    candidate   dict  — MutationCandidate
    baseline    dict  — original SkillContent (must have 'content' key)
    skill_path  str   — path to the SKILL.md (for forbidden file logic)

Output:
    RegressionResult dict:
        candidate_id        str
        passed              bool
        violations          list[str]  — empty if passed
"""

from __future__ import annotations

import re
from typing import Any


# The 12 required H2 section names (Purpose counts as 1, Real file output sample as 12th)
REQUIRED_SECTIONS = [
    "Purpose",
    "Use when",
    "Do NOT use when",
    "Inputs required",
    "Constraints",
    "Step-by-step workflow",
    "Output contract",
    "Validation checklist",
    "Related skills",
    "References",
    "Real example",
    "Real file output sample",
]

# Files that must never be modified by a mutation
FORBIDDEN_MUTATION_PATHS = [
    "AGENTS.md",
    "AGENTS.overlay.md",
    "docs/prompt-pipeline.md",
    "docs/agent-team-system.md",
    "evals/rubrics/",
    "evals/schemas/",
    ".github/workflows/",
]

# Architecture violations: patterns that must not appear in a mutated skill
ARCH_VIOLATION_PATTERNS = [
    (r"import\s+firebase_auth\s+directly", "Direct firebase_auth import without adapter"),
    (r"bypass\s+repository", "Repository bypass recommended"),
    (r"directly\s+in\s+(widget|page|screen)", "Logic placed directly in presentation layer"),
    (r"skip\s+the\s+validation", "Validation skipped by mutation"),
]


class RegressionViolation(Exception):
    """Raised when a mutation candidate fails a hard regression check."""
    def __init__(self, candidate_id: str, violations: list[str]) -> None:
        self.candidate_id = candidate_id
        self.violations = violations
        super().__init__(f"Candidate {candidate_id} failed regression: {violations}")


class RegressionAgent:
    """Run all regression checks on a single candidate.  Hard-fail on any violation."""

    def check(
        self,
        candidate: dict[str, Any],
        baseline: dict[str, Any],
        skill_path: str = "",
    ) -> dict[str, Any]:
        """Return RegressionResult dict.  Raises RegressionViolation if any check fails."""
        candidate_id = candidate["candidate_id"]
        content      = candidate["content"]
        base_content = baseline.get("content", "")

        violations: list[str] = []

        violations.extend(self._check_required_sections(content))
        violations.extend(self._check_no_architecture_violations(content))
        violations.extend(self._check_no_forbidden_file_changes(candidate, skill_path))
        violations.extend(self._check_behavior_preserved(content, base_content))
        violations.extend(self._check_section_count_not_reduced(content, base_content))

        passed = len(violations) == 0

        result: dict[str, Any] = {
            "candidate_id": candidate_id,
            "passed":       passed,
            "violations":   violations,
        }

        if not passed:
            raise RegressionViolation(candidate_id, violations)

        return result

    def check_silent(
        self,
        candidate: dict[str, Any],
        baseline: dict[str, Any],
        skill_path: str = "",
    ) -> dict[str, Any]:
        """Same as check() but returns the result dict instead of raising on failure."""
        try:
            return self.check(candidate, baseline, skill_path)
        except RegressionViolation as exc:
            return {
                "candidate_id": exc.candidate_id,
                "passed":       False,
                "violations":   exc.violations,
            }

    # ------------------------------------------------------------------
    # Individual checks
    # ------------------------------------------------------------------

    def _check_required_sections(self, content: str) -> list[str]:
        violations: list[str] = []
        for section in REQUIRED_SECTIONS:
            if not re.search(rf"##\s+{re.escape(section)}", content, re.I):
                violations.append(f"Missing required section: ## {section}")
        return violations

    def _check_no_architecture_violations(self, content: str) -> list[str]:
        violations: list[str] = []
        for pattern, description in ARCH_VIOLATION_PATTERNS:
            if re.search(pattern, content, re.I):
                violations.append(f"Architecture violation: {description}")
        return violations

    def _check_no_forbidden_file_changes(
        self, candidate: dict[str, Any], skill_path: str
    ) -> list[str]:
        """Ensure the mutation_type is not touching a forbidden path."""
        violations: list[str] = []
        for forbidden in FORBIDDEN_MUTATION_PATHS:
            if skill_path and forbidden in skill_path:
                violations.append(
                    f"Mutation targets a forbidden file path: {skill_path} matches {forbidden}"
                )
        return violations

    def _check_behavior_preserved(self, content: str, base_content: str) -> list[str]:
        """Verify that the Purpose and Output contract sections are not degraded."""
        violations: list[str] = []
        if not base_content:
            return violations

        def extract_section(text: str, name: str) -> str:
            result: list[str] = []
            in_section = False
            for line in text.splitlines():
                if re.match(rf"##\s+{re.escape(name)}", line, re.I):
                    in_section = True
                    continue
                if in_section and re.match(r"##\s+", line):
                    break
                if in_section:
                    result.append(line)
            return "\n".join(result).strip()

        base_purpose = extract_section(base_content, "Purpose")
        cand_purpose = extract_section(content,      "Purpose")

        if base_purpose and not cand_purpose:
            violations.append("Purpose section was removed or emptied by mutation.")

        base_outputs = extract_section(base_content, "Output contract")
        cand_outputs = extract_section(content,      "Output contract")

        if base_outputs and not cand_outputs:
            violations.append("Output contract section was removed or emptied by mutation.")

        # Count output bullets — mutation must not reduce them
        base_bullet_count = len(re.findall(r"^\s*[-*]", base_outputs, re.MULTILINE))
        cand_bullet_count = len(re.findall(r"^\s*[-*]", cand_outputs, re.MULTILINE))
        if base_bullet_count > 0 and cand_bullet_count < base_bullet_count:
            violations.append(
                f"Output contract has fewer deliverables after mutation "
                f"({cand_bullet_count} < {base_bullet_count})."
            )

        return violations

    def _check_section_count_not_reduced(self, content: str, base_content: str) -> list[str]:
        """Ensure mutation did not remove any H2 sections that existed in the baseline."""
        violations: list[str] = []
        if not base_content:
            return violations

        base_sections = set(re.findall(r"##\s+(.+)", base_content))
        cand_sections = set(re.findall(r"##\s+(.+)", content))
        removed = base_sections - cand_sections
        if removed:
            for sec in sorted(removed):
                violations.append(f"Section removed by mutation: ## {sec.strip()}")
        return violations
