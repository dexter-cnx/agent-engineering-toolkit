"""MutationAgent — generates controlled single-dimension mutations of a SKILL.md.

Each call to generate_candidates() returns N MutationCandidate dicts,
one per mutation type (up to the number of available types).

Mutation contract:
  - Exactly ONE dimension is changed per candidate.
  - All 13 required SKILL.md sections are preserved.
  - The candidate_id is deterministic: <parent_id>-<mutation_type>.

Input payload keys:
    skill_id        str
    candidate_id    str   — ID of the document being mutated (usually 'baseline')
    content         str   — full SKILL.md text
    n               int   — max number of candidates to generate (default 6)
    timestamp       str   — ISO 8601 (optional)

Output: list of MutationCandidate dicts matching run_report.schema.json#/definitions/MutationCandidate
"""

from __future__ import annotations

import re
import math
import uuid
from typing import Any


MUTATION_TYPES = [
    "prompt_wording",
    "decomposition_steps",
    "verification_ordering",
    "success_criteria_phrasing",
    "refusal_logic",
    "token_budget",
]


class MutationAgent:
    """Generate one mutation candidate per dimension, capped at n."""

    def generate_candidates(
        self,
        skill_id: str,
        parent_id: str,
        content: str,
        n: int = 6,
    ) -> list[dict[str, Any]]:
        """Return up to n MutationCandidate dicts."""
        candidates: list[dict[str, Any]] = []
        for mtype in MUTATION_TYPES[:n]:
            mutated, description = self._apply_mutation(mtype, content)
            token_count = self._count_tokens(mutated)
            candidates.append({
                "candidate_id":         f"{parent_id}-{mtype}",
                "parent_id":            parent_id,
                "mutation_type":        mtype,
                "mutation_description": description,
                "content":              mutated,
                "token_count":          token_count,
            })
        return candidates

    # ------------------------------------------------------------------
    # Mutation dispatch
    # ------------------------------------------------------------------

    def _apply_mutation(self, mtype: str, content: str) -> tuple[str, str]:
        dispatch = {
            "prompt_wording":             self._mutate_prompt_wording,
            "decomposition_steps":        self._mutate_decomposition_steps,
            "verification_ordering":      self._mutate_verification_ordering,
            "success_criteria_phrasing":  self._mutate_success_criteria_phrasing,
            "refusal_logic":              self._mutate_refusal_logic,
            "token_budget":               self._mutate_token_budget,
        }
        return dispatch[mtype](content)

    # ------------------------------------------------------------------
    # Individual mutation strategies
    # ------------------------------------------------------------------

    def _mutate_prompt_wording(self, content: str) -> tuple[str, str]:
        """Make imperative verbs in Purpose and step headers more direct."""
        result = content

        # Replace passive "should be" with active "must be" in Purpose section
        result = re.sub(r"\bshould\s+be\b", "must be", result, flags=re.I)

        # Replace "You can" with the direct imperative in workflow steps
        result = re.sub(r"^\s*(\d+\.)\s+You can ", r"\1 ", result, flags=re.MULTILINE)

        # Replace "It is recommended to" → "Do:"
        result = re.sub(r"It is recommended to\s+", "", result, flags=re.I)

        # Tighten Purpose: remove "This skill" preamble
        result = re.sub(
            r"(##\s+Purpose\s*\n)This skill\s+",
            r"\1",
            result,
            flags=re.I,
        )

        description = (
            "Sharpened imperative voice: replaced 'should be' with 'must be', "
            "removed 'You can' preambles in workflow steps, stripped 'This skill' from Purpose."
        )
        return result, description

    def _mutate_decomposition_steps(self, content: str) -> tuple[str, str]:
        """Split any compound step (containing ' and ') into two discrete steps."""
        lines = content.splitlines()
        new_lines: list[str] = []
        added = 0

        in_workflow = False
        step_counter: dict[str, int] = {"n": 0}

        for line in lines:
            if re.match(r"##\s+Step-by-step workflow", line, re.I):
                in_workflow = True
                new_lines.append(line)
                continue
            if in_workflow and re.match(r"##\s+", line):
                in_workflow = False

            if in_workflow:
                m = re.match(r"^(\s*)(\d+)\.\s+(.+)$", line)
                if m and " and " in m.group(3) and added < 2:
                    indent, num_str, text = m.group(1), int(m.group(2)), m.group(3)
                    parts = text.split(" and ", 1)
                    new_lines.append(f"{indent}{num_str}. {parts[0].strip()}.")
                    new_lines.append(f"{indent}{num_str + 1}. {parts[1].strip().capitalize()}.")
                    added += 1
                    continue
            new_lines.append(line)

        description = (
            f"Decomposed {added} compound step(s) containing ' and ' into two atomic steps each, "
            "making each step independently executable."
        )
        return "\n".join(new_lines), description

    def _mutate_verification_ordering(self, content: str) -> tuple[str, str]:
        """Move the most concrete (grep/run/check) validation bullets to the top of the checklist."""
        section = "Validation checklist"
        lines = content.splitlines()
        new_lines: list[str] = []
        in_section = False
        bullets: list[str] = []
        after_bullets: list[str] = []
        capturing_done = False

        for line in lines:
            if re.match(rf"##\s+{re.escape(section)}", line, re.I):
                in_section = True
                new_lines.append(line)
                continue
            if in_section and re.match(r"##\s+", line):
                # flush sorted bullets
                action_kw = ["run", "grep", "check", "open", "confirm", "assert", "test", "verify"]

                def priority(b: str) -> int:
                    lower = b.lower()
                    return 0 if any(kw in lower for kw in action_kw) else 1

                sorted_bullets = sorted(bullets, key=priority)
                new_lines.extend(sorted_bullets)
                in_section = False
                capturing_done = True
                new_lines.append(line)
                continue
            if in_section and re.match(r"^\s*[-*]", line):
                bullets.append(line)
                continue
            new_lines.append(line)

        if in_section and not capturing_done:
            action_kw = ["run", "grep", "check", "open", "confirm", "assert", "test", "verify"]

            def priority(b: str) -> int:
                lower = b.lower()
                return 0 if any(kw in lower for kw in action_kw) else 1

            sorted_bullets = sorted(bullets, key=priority)
            new_lines.extend(sorted_bullets)

        description = (
            "Reordered validation checklist: concrete executable checks (run/grep/check/verify) "
            "moved to the top, subjective assertions moved down."
        )
        return "\n".join(new_lines), description

    def _mutate_success_criteria_phrasing(self, content: str) -> tuple[str, str]:
        """Rewrite Output contract bullets from 'An X' form to 'Produces X' form."""
        def rewrite_bullet(m: re.Match) -> str:
            indent = m.group(1)
            text = m.group(2)
            # "An audit summary" → "Produces an audit summary"
            if re.match(r"^(A|An)\s+", text, re.I):
                return f"{indent}- Produces {text[0].lower()}{text[1:]}"
            # "The path to the file" → "Writes the path to the file"
            if re.match(r"^The\s+", text, re.I):
                return f"{indent}- Delivers {text[0].lower()}{text[1:]}"
            return m.group(0)

        in_output = False
        lines = content.splitlines()
        new_lines: list[str] = []

        for line in lines:
            if re.match(r"##\s+Output contract", line, re.I):
                in_output = True
                new_lines.append(line)
                continue
            if in_output and re.match(r"##\s+", line):
                in_output = False
            if in_output:
                new_line = re.sub(r"^(\s*[-*]\s+)(.+)$", rewrite_bullet, line)
                new_lines.append(new_line)
                continue
            new_lines.append(line)

        description = (
            "Rephrased Output contract bullets to active delivery form: "
            "'An X' → 'Produces X', 'The X' → 'Delivers X'. Makes success criteria unambiguous."
        )
        return "\n".join(new_lines), description

    def _mutate_refusal_logic(self, content: str) -> tuple[str, str]:
        """Strengthen 'Do NOT use when' section with explicit consequence statements."""
        lines = content.splitlines()
        new_lines: list[str] = []
        in_section = False

        for line in lines:
            if re.match(r"##\s+Do NOT use when", line, re.I):
                in_section = True
                new_lines.append(line)
                continue
            if in_section and re.match(r"##\s+", line):
                in_section = False
            if in_section and re.match(r"^\s*[-*]\s+", line):
                # Append "(use X instead)" if no "use" already present
                if "use " not in line.lower() and "instead" not in line.lower():
                    stripped = line.rstrip()
                    new_lines.append(stripped + " — use a more specific skill instead.")
                    continue
            new_lines.append(line)

        description = (
            "Strengthened refusal logic: each 'Do NOT use when' bullet now ends with "
            "'— use a more specific skill instead.' to make refusal actionable."
        )
        return "\n".join(new_lines), description

    def _mutate_token_budget(self, content: str) -> tuple[str, str]:
        """Tighten verbosity by removing filler sentences and trimming over-long purpose text."""
        filler_patterns = [
            r"It is important to note that[^.]*\.",
            r"Please (ensure|be aware|note) that[^.]*\.",
            r"As mentioned (above|before)[^.]*\.",
            r"In order to[^,]*,\s*",
            r"Needless to say[^.]*\.",
            r"It should be noted that[^.]*\.",
        ]
        result = content
        removed = 0
        for pat in filler_patterns:
            new_result, n = re.subn(pat, "", result, flags=re.I)
            removed += n
            result = new_result

        # Collapse multiple blank lines to one
        result = re.sub(r"\n{3,}", "\n\n", result)

        description = (
            f"Token budget reduction: removed {removed} filler sentence(s) "
            "(e.g., 'It is important to note that…', 'Please ensure that…') "
            "and collapsed excess blank lines."
        )
        return result, description

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _count_tokens(content: str) -> int:
        return math.ceil(len(content.split()) * 1.3)
