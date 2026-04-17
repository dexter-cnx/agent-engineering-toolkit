"""EvaluatorAgent — scores a skill or mutation candidate against the Karpathy rubric.

Input payload (dict):
    skill_id        str   — stable skill identifier
    candidate_id    str   — 'baseline' or a mutation UUID
    mutation_type   str|None
    content         str   — full SKILL.md text
    rubric          dict  — parsed coding_task_rubric.v1.json
    timestamp       str   — ISO 8601

Output (dict):  conforms to evals/schemas/skill_eval.schema.json
"""

from __future__ import annotations

import re
import math
from datetime import datetime, timezone
from typing import Any


# ---------------------------------------------------------------------------
# Scoring weights — must match rubric JSON
# ---------------------------------------------------------------------------
WEIGHTS: dict[str, float] = {
    "correctness":            0.30,
    "scope_discipline":       0.15,
    "simplicity":             0.15,
    "verifiability":          0.15,
    "architecture_alignment": 0.10,
    "token_efficiency":       0.10,
    "docs_hygiene":           0.05,
}

# Required SKILL.md H2 sections in canonical order
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

FORBIDDEN_PATTERNS = ["TODO", "TBD", "FIXME", "{{", "<fill", "coming soon"]

# Architecture anti-patterns (for architecture_alignment scoring)
ARCH_ANTIPATTERNS = [
    r"import\s+firebase_auth.*widget",
    r"directly\s+in\s+(widget|page)",
    r"bypass\s+repository",
    r"shortcut\s+the\s+adapter",
]

# Filler phrases that hurt token_efficiency
FILLER_PHRASES = [
    "as mentioned above",
    "it is important to note that",
    "please ensure",
    "in order to",
    "it should be noted",
    "please be aware",
    "needless to say",
]


class EvaluatorAgent:
    """Score one skill document against a rubric and return a structured result dict."""

    def __init__(self, rubric: dict[str, Any]) -> None:
        self._rubric = rubric

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def evaluate(
        self,
        skill_id: str,
        candidate_id: str,
        content: str,
        mutation_type: str | None = None,
        timestamp: str | None = None,
    ) -> dict[str, Any]:
        """Run full evaluation and return a dict matching skill_eval.schema.json."""
        ts = timestamp or datetime.now(timezone.utc).isoformat()
        token_count = self._count_tokens(content)
        scores = self._score_all_dimensions(content)
        final = self._weighted_final(scores)
        quality = final / (token_count / 1000) if token_count > 0 else 0.0
        binary = self._run_binary_checks(content)
        binary_passed = all(binary.values())

        return {
            "skill_id": skill_id,
            "candidate_id": candidate_id,
            "mutation_type": mutation_type or "baseline",
            "scores": scores,
            "final_score": round(final, 4),
            "token_count": token_count,
            "quality_per_1k_tokens": round(quality, 4),
            "binary_checks": binary,
            "binary_checks_passed": binary_passed,
            "regression_passed": True,   # will be overwritten by RegressionAgent
            "regression_violations": [],
            "token_policy_passed": None,  # will be filled by optimizer
            "evaluator_notes": self._generate_notes(scores, binary, content),
            "timestamp": ts,
        }

    # ------------------------------------------------------------------
    # Dimension scorers
    # ------------------------------------------------------------------

    def _score_all_dimensions(self, content: str) -> dict[str, float]:
        return {
            "correctness":            self._score_correctness(content),
            "scope_discipline":       self._score_scope_discipline(content),
            "simplicity":             self._score_simplicity(content),
            "verifiability":          self._score_verifiability(content),
            "architecture_alignment": self._score_architecture_alignment(content),
            "token_efficiency":       self._score_token_efficiency(content),
            "docs_hygiene":           self._score_docs_hygiene(content),
        }

    def _score_correctness(self, content: str) -> float:
        """Proxy: workflow step count and output contract completeness."""
        steps = self._count_numbered_steps(content)
        has_output = bool(re.search(r"##\s+Output contract", content, re.I))
        has_purpose = bool(re.search(r"##\s+Purpose", content, re.I))
        has_real_example = bool(re.search(r"##\s+Real example", content, re.I))

        score = 0.0
        if has_purpose:      score += 0.2
        if has_output:       score += 0.2
        if has_real_example: score += 0.2
        if steps >= 4:       score += 0.3
        elif steps >= 2:     score += 0.2
        elif steps >= 1:     score += 0.1

        # Penalise if forbidden patterns exist
        for pat in FORBIDDEN_PATTERNS:
            if pat in content:
                score = max(0.0, score - 0.15)
                break

        return min(1.0, round(score, 3))

    def _score_scope_discipline(self, content: str) -> float:
        """Proxy: presence and substance of 'Use when' and 'Do NOT use when'."""
        use_when = self._section_bullet_count(content, "Use when")
        dont_use = self._section_bullet_count(content, "Do NOT use when")
        score = 0.0
        if use_when >= 2:   score += 0.5
        elif use_when == 1: score += 0.3
        if dont_use >= 2:   score += 0.5
        elif dont_use == 1: score += 0.3
        return round(min(1.0, score), 3)

    def _score_simplicity(self, content: str) -> float:
        """Proxy: step count vs content length ratio; penalise filler."""
        steps = self._count_numbered_steps(content)
        words = len(content.split())
        filler_count = sum(1 for p in FILLER_PHRASES if p.lower() in content.lower())

        # Ideal: 4-8 steps, ~400-800 words
        if words == 0:
            return 0.0
        words_per_step = words / max(steps, 1)

        # Score inversely to verbosity per step
        if words_per_step < 60:
            base = 1.0
        elif words_per_step < 120:
            base = 0.8
        elif words_per_step < 200:
            base = 0.6
        elif words_per_step < 300:
            base = 0.4
        else:
            base = 0.2

        penalty = filler_count * 0.1
        return round(max(0.0, base - penalty), 3)

    def _score_verifiability(self, content: str) -> float:
        """Proxy: actionable keywords in Validation checklist section."""
        action_keywords = ["run", "check", "grep", "open", "confirm", "assert",
                           "test", "verify", "inspect", "ensure", "validate"]
        vague_keywords  = ["ensure quality", "looks right", "seems correct", "should be fine"]

        checklist_text = self._extract_section(content, "Validation checklist")
        if not checklist_text:
            return 0.0

        bullets = self._section_bullet_count(content, "Validation checklist")
        if bullets == 0:
            return 0.0

        action_hits = sum(1 for kw in action_keywords if kw.lower() in checklist_text.lower())
        vague_hits  = sum(1 for kw in vague_keywords  if kw.lower() in checklist_text.lower())

        score = min(1.0, (action_hits / max(bullets, 1)) * 1.2)
        score = max(0.0, score - (vague_hits * 0.15))
        return round(score, 3)

    def _score_architecture_alignment(self, content: str) -> float:
        """Proxy: penalise architecture anti-patterns."""
        anti_hits = sum(
            1 for pat in ARCH_ANTIPATTERNS
            if re.search(pat, content, re.I)
        )
        positive_terms = ["adapter", "repository", "domain", "interface", "boundary", "contract"]
        positive_hits = sum(1 for t in positive_terms if t.lower() in content.lower())
        base = min(1.0, 0.5 + positive_hits * 0.1)
        penalty = anti_hits * 0.25
        return round(max(0.0, base - penalty), 3)

    def _score_token_efficiency(self, content: str) -> float:
        """Proxy: penalise filler phrases and redundant sections."""
        filler_hits = sum(1 for p in FILLER_PHRASES if p.lower() in content.lower())
        # Check for duplicated paragraphs (rough dedup)
        paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
        unique_pct = len(set(paragraphs)) / max(len(paragraphs), 1)
        base = unique_pct
        penalty = filler_hits * 0.08
        return round(max(0.0, min(1.0, base - penalty)), 3)

    def _score_docs_hygiene(self, content: str) -> float:
        """Proxy: all 13 sections present, no forbidden patterns, references exist."""
        present = sum(
            1 for sec in REQUIRED_SECTIONS
            if re.search(rf"##\s+{re.escape(sec)}", content, re.I)
        )
        section_score = present / len(REQUIRED_SECTIONS)

        has_forbidden = any(pat in content for pat in FORBIDDEN_PATTERNS)
        has_references = bool(re.search(r"\[.+\]\(.+\.md\)", content))

        score = section_score * 0.7
        if not has_forbidden: score += 0.2
        if has_references:    score += 0.1
        return round(min(1.0, score), 3)

    # ------------------------------------------------------------------
    # Binary checks
    # ------------------------------------------------------------------

    def _run_binary_checks(self, content: str) -> dict[str, bool]:
        return {
            "has_purpose_section":      bool(re.search(r"##\s+Purpose\s*\n\S", content, re.I)),
            "has_workflow_steps":       self._count_numbered_steps(content) >= 2,
            "no_placeholder_text":      not any(p in content for p in FORBIDDEN_PATTERNS),
            "has_validation_checklist": self._section_bullet_count(content, "Validation checklist") >= 1,
            "has_output_contract":      self._section_bullet_count(content, "Output contract") >= 1,
            "has_real_example":         bool(self._extract_section(content, "Real example").strip()),
        }

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _count_tokens(content: str) -> int:
        """Estimate token count: word count * 1.3 (rough GPT-style approximation)."""
        words = len(content.split())
        return math.ceil(words * 1.3)

    @staticmethod
    def _count_numbered_steps(content: str) -> int:
        """Count lines that start with a digit followed by a dot in Step-by-step section."""
        workflow_section = ""
        in_section = False
        for line in content.splitlines():
            if re.match(r"##\s+Step-by-step workflow", line, re.I):
                in_section = True
                continue
            if in_section and re.match(r"##\s+", line):
                break
            if in_section:
                workflow_section += line + "\n"
        return len(re.findall(r"^\s*\d+\.", workflow_section, re.MULTILINE))

    @staticmethod
    def _section_bullet_count(content: str, section_name: str) -> int:
        """Count bullet items (lines starting with - or *) in a named section."""
        section_text = ""
        in_section = False
        pattern = re.compile(rf"##\s+{re.escape(section_name)}", re.I)
        for line in content.splitlines():
            if pattern.match(line):
                in_section = True
                continue
            if in_section and re.match(r"##\s+", line):
                break
            if in_section:
                section_text += line + "\n"
        return len(re.findall(r"^\s*[-*]", section_text, re.MULTILINE))

    @staticmethod
    def _extract_section(content: str, section_name: str) -> str:
        """Return the raw text of a named section (between its ## header and the next ## header)."""
        lines = content.splitlines()
        result: list[str] = []
        in_section = False
        pattern = re.compile(rf"##\s+{re.escape(section_name)}", re.I)
        for line in lines:
            if pattern.match(line):
                in_section = True
                continue
            if in_section and re.match(r"##\s+", line):
                break
            if in_section:
                result.append(line)
        return "\n".join(result)

    @staticmethod
    def _weighted_final(scores: dict[str, float]) -> float:
        return sum(WEIGHTS[k] * scores[k] for k in WEIGHTS)

    @staticmethod
    def _generate_notes(scores: dict, binary: dict, content: str) -> str:
        notes: list[str] = []
        low = [k for k, v in scores.items() if v < 0.5]
        if low:
            notes.append(f"Low-scoring dimensions: {', '.join(low)}.")
        failing = [k for k, v in binary.items() if not v]
        if failing:
            notes.append(f"Failed binary checks: {', '.join(failing)}.")
        if not notes:
            notes.append("All dimensions above threshold; no critical issues detected.")
        return " ".join(notes)
