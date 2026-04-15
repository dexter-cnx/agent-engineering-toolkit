from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from string import Template
from textwrap import indent


ACTIVE_CATEGORIES = [
    "architecture",
    "state",
    "routing",
    "firebase",
    "web",
    "release",
    "performance",
    "tooling",
]

REQUIRED_HEADINGS = [
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

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bFIXME\b", re.IGNORECASE),
    re.compile(r"\bplaceholder\b", re.IGNORECASE),
    re.compile(r"\{\{[^}]+\}\}"),
    re.compile(r"<fill[^>]*>", re.IGNORECASE),
    re.compile(r"\bcoming soon\b", re.IGNORECASE),
]

DEPRECATED_SKILL_NAMES = {
    "flutter-feature-scaffold",
    "flutter-riverpod-feature-state",
    "flutter-getx-mvc-feature",
    "flutter-firebase-auth-flow",
    "flutter-go-router-deeplink",
    "flutter-android-release-signing",
    "flutter-design-token-sync",
}

CANONICAL_TEMPLATE_CHECKS = {
    "feature-module-template.md": ["lib/features/<feature_name>/", "domain/", "data/", "presentation/"],
    "state-management-template.md": ["Riverpod", "GetX"],
    "project-bootstrap-template.md": ["lib/", "app/", "core/", "features/"],
}


@dataclass(frozen=True)
class SkillDoc:
    category: str
    name: str
    path: Path
    title: str
    sections: dict[str, str]

    @property
    def purpose(self) -> str:
        return self.sections.get("Purpose", "").strip()

    @property
    def use_when(self) -> str:
        return self.sections.get("Use when", "").strip()

    @property
    def do_not_use_when(self) -> str:
        return self.sections.get("Do NOT use when", "").strip()

    @property
    def inputs_required(self) -> str:
        return self.sections.get("Inputs required", "").strip()

    @property
    def constraints(self) -> str:
        return self.sections.get("Constraints", "").strip()

    @property
    def workflow(self) -> str:
        return self.sections.get("Step-by-step workflow", "").strip()

    @property
    def output_contract(self) -> str:
        return self.sections.get("Output contract", "").strip()

    @property
    def validation_checklist(self) -> str:
        return self.sections.get("Validation checklist", "").strip()

    @property
    def related_skills(self) -> str:
        return self.sections.get("Related skills", "").strip()

    @property
    def references(self) -> str:
        return self.sections.get("References", "").strip()

    @property
    def real_example(self) -> str:
        return self.sections.get("Real example", "").strip()

    @property
    def real_file_output_sample(self) -> str:
        return self.sections.get("Real file output sample", "").strip()

    @property
    def trigger_text(self) -> str:
        return self.use_when

    @property
    def anti_pattern_text(self) -> str:
        return self.do_not_use_when


def repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def overlay_root(overlay: str | None) -> Path:
    if overlay:
        return (repo_root() / overlay).resolve()
    return (repo_root() / "overlays/mobile-flutter").resolve()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def tokenize(text: str) -> set[str]:
    stopwords = {
        "the", "and", "for", "with", "from", "into", "when", "that", "this",
        "only", "use", "useful", "need", "needs", "skill", "skills", "app",
        "flutter", "create", "create", "add", "build", "one", "new", "task",
        "feature", "file", "files", "route", "routes", "state", "skillgen",
    }
    tokens = {t for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 2}
    return {token for token in tokens if token not in stopwords}


def split_bullets(section: str) -> list[str]:
    return [line[2:].strip() for line in section.splitlines() if line.strip().startswith("- ")]


def split_numbered(section: str) -> list[str]:
    return [re.sub(r"^\d+\.\s*", "", line).strip() for line in section.splitlines() if re.match(r"^\d+\.\s+", line.strip())]


def parse_skill(path: Path) -> SkillDoc:
    lines = read_text(path).splitlines()
    if not lines:
        raise ValueError(f"{path}: file is empty")
    if not lines[0].startswith("# "):
        raise ValueError(f"{path}: missing top-level title")
    title = lines[0][2:].strip()
    sections: dict[str, list[str]] = {}
    current: str | None = None
    buffer: list[str] = []
    for line in lines[1:]:
        if line.startswith("## "):
            if current is not None:
                sections[current] = buffer[:]
            current = line[3:].strip()
            buffer = []
        else:
            buffer.append(line)
    if current is not None:
        sections[current] = buffer[:]
    normalized_sections = {key: "\n".join(value).strip() for key, value in sections.items()}
    category = path.parent.parent.name
    name = path.parent.name
    return SkillDoc(category=category, name=name, path=path, title=title, sections=normalized_sections)


def discover_active_skills(overlay: Path) -> list[SkillDoc]:
    docs: list[SkillDoc] = []
    for category in ACTIVE_CATEGORIES:
        category_dir = overlay / "skills" / category
        if not category_dir.exists():
            continue
        for skill_file in sorted(category_dir.glob("*/SKILL.md")):
            try:
                doc = parse_skill(skill_file)
            except ValueError as exc:
                raise SystemExit(str(exc)) from exc
            if doc.title.lower().startswith("deprecated:"):
                continue
            docs.append(doc)
    return docs


def required_section_errors(skill: SkillDoc) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if heading not in skill.sections:
            errors.append(f"{skill.path}: missing required heading '## {heading}'")
            continue
        if not skill.sections[heading].strip():
            errors.append(f"{skill.path}: section '## {heading}' is empty")
    return errors


def placeholder_errors(skill: SkillDoc) -> list[str]:
    errors: list[str] = []
    for heading, body in skill.sections.items():
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(body):
                errors.append(f"{skill.path}: section '## {heading}' contains placeholder text matched by {pattern.pattern}")
                break
    return errors


def naming_errors(skill: SkillDoc) -> list[str]:
    errors: list[str] = []
    if skill.title != skill.name:
        errors.append(f"{skill.path}: H1 title '{skill.title}' must match folder name '{skill.name}'")
    if slugify(skill.title) != skill.name:
        errors.append(f"{skill.path}: H1 title '{skill.title}' does not normalize to slug '{skill.name}'")
    return errors


def reference_errors(skill: SkillDoc, overlay: Path) -> list[str]:
    refs = skill.references
    if not refs:
        return [f"{skill.path}: missing references section content"]
    links = extract_links(skill.path, refs)
    if not links:
        return [f"{skill.path}: references section must include at least one markdown link"]
    example_or_template = False
    errors: list[str] = []
    for target in links:
        resolved = resolve_link(skill.path, target)
        if not resolved.exists():
            errors.append(f"{skill.path}: broken reference link -> {target}")
        if "examples/" in target or "templates/" in target:
            example_or_template = True
    if not example_or_template:
        errors.append(f"{skill.path}: references must link to at least one example or template")
    return errors


def extract_links(base: Path, text: str) -> list[str]:
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    return [link for link in links if not link.startswith("http://") and not link.startswith("https://")]


def resolve_link(base: Path, link: str) -> Path:
    if link.startswith("/"):
        return Path(link)
    if "#" in link:
        link = link.split("#", 1)[0]
    return (base.parent / link).resolve()


def validate_skills(overlay: Path) -> int:
    docs = discover_active_skills(overlay)
    issues: list[str] = []
    purpose_index: dict[str, SkillDoc] = {}
    trigger_index: dict[str, SkillDoc] = {}

    for skill in docs:
        issues.extend(required_section_errors(skill))
        issues.extend(placeholder_errors(skill))
        issues.extend(naming_errors(skill))
        issues.extend(reference_errors(skill, overlay))

        purpose_key = normalize(skill.purpose)
        if purpose_key:
            if purpose_key in purpose_index:
                other = purpose_index[purpose_key]
                issues.append(
                    f"{skill.path}: duplicate purpose detected with {other.path} -> '{skill.purpose}'"
                )
            else:
                purpose_index[purpose_key] = skill

        trigger_key = normalize(" | ".join(split_bullets(skill.use_when)))
        if trigger_key:
            if trigger_key in trigger_index:
                other = trigger_index[trigger_key]
                issues.append(
                    f"{skill.path}: duplicate trigger set detected with {other.path} -> '{skill.use_when}'"
                )
            else:
                trigger_index[trigger_key] = skill

    if issues:
        print("Skill validation failed:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print(f"Validated {len(docs)} active skills against SKILL_SCHEMA.md")
    return 0


def similarity_score(left: str, right: str) -> float:
    return difflib.SequenceMatcher(None, normalize(left), normalize(right)).ratio()


def pairwise_overlap_report(docs: list[SkillDoc]) -> list[str]:
    findings: list[str] = []
    for index, left in enumerate(docs):
        for right in docs[index + 1 :]:
            purpose_score = similarity_score(left.purpose, right.purpose)
            trigger_score = similarity_score(left.trigger_text, right.trigger_text)
            combined_left = f"{left.purpose}\n{left.trigger_text}\n{left.anti_pattern_text}"
            combined_right = f"{right.purpose}\n{right.trigger_text}\n{right.anti_pattern_text}"
            combined_score = similarity_score(combined_left, combined_right)

            if max(purpose_score, trigger_score, combined_score) >= 0.88:
                guidance = "merge or rename"
                if left.category != right.category:
                    guidance = "split responsibilities or tighten the category boundary"
                findings.append(
                    f"- {left.path} <-> {right.path}: overlap score={max(purpose_score, trigger_score, combined_score):.2f}; guidance: {guidance}"
                )
    return findings


def workflow_skills(overlay: Path) -> list[tuple[Path, list[str]]]:
    workflows: list[tuple[Path, list[str]]] = []
    for path in sorted((overlay / "workflows").glob("*/README.md")):
        lines = read_text(path).splitlines()
        skills: list[str] = []
        in_execution_order = False
        for line in lines:
            if line.startswith("## "):
                in_execution_order = line == "## Execution order"
                continue
            if not in_execution_order:
                continue
            if line.startswith("## "):
                break
            skills.extend(re.findall(r"`([a-z0-9-]+)`", line))
        workflows.append((path, skills))
    return workflows


def detect_workflow_duplicates(overlay: Path) -> list[str]:
    findings: list[str] = []
    workflows = workflow_skills(overlay)
    seen_sequences: dict[tuple[str, ...], Path] = {}
    for path, skills in workflows:
        skill_names = tuple(skills)
        if not skill_names:
            findings.append(f"- {path}: could not parse any skills from the execution-order section")
            continue
        if len(skill_names) != len(set(skill_names)):
            findings.append(f"- {path}: repeated skill entries detected in workflow sequence")
        if skill_names in seen_sequences:
            findings.append(f"- {path}: workflow duplicates exact skill logic from {seen_sequences[skill_names]}")
        else:
            seen_sequences[skill_names] = path
    return findings


def detect_template_drift(overlay: Path) -> list[str]:
    findings: list[str] = []
    for template_name, required_fragments in CANONICAL_TEMPLATE_CHECKS.items():
        matches = list((overlay / "templates").glob(template_name))
        if not matches:
            continue
        template_path = matches[0]
        text = read_text(template_path)
        for fragment in required_fragments:
            if fragment not in text:
                findings.append(f"- {template_path}: missing canonical guidance fragment '{fragment}'")
    return findings


def overlap_command(overlay: Path, report_path: Path | None, fail_on_overlap: bool) -> int:
    docs = discover_active_skills(overlay)
    findings = pairwise_overlap_report(docs)
    findings.extend(detect_workflow_duplicates(overlay))
    findings.extend(detect_template_drift(overlay))

    report_lines = [
        "# Skill Overlap Report",
        "",
        f"Overlay: `{overlay}`",
        "",
    ]
    if findings:
        report_lines.append("## Findings")
        report_lines.extend(findings)
        report_lines.append("")
        report_lines.append("## Guidance")
        report_lines.append("- Merge skills that share the same primary responsibility.")
        report_lines.append("- Split skills when one file mixes folder creation, contracts, and implementation.")
        report_lines.append("- Keep workflows orchestration-only; move logic back into atomic skills.")
    else:
        report_lines.append("No overlap findings detected.")

    if report_path is None:
        report_path = overlay / "docs" / "skill-overlap-report.md"
    write_text(report_path, "\n".join(report_lines) + "\n")
    print(f"Wrote overlap report to {report_path}")

    if findings and fail_on_overlap:
        print("Skill overlap quality gate failed:", file=sys.stderr)
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1
    return 0


def generate_index(overlay: Path) -> str:
    docs = discover_active_skills(overlay)
    docs = sorted(docs, key=lambda doc: (ACTIVE_CATEGORIES.index(doc.category), doc.name))
    lines = [
        "# SKILLS_INDEX",
        "",
        "This index is generated from active skill metadata by `tools/skillgen/`.",
        "",
        "## Routing rules",
        "",
        "- If the request is about structure, boundaries, or compliance, start with an architecture skill.",
        "- If the request is about domain contracts, start with contract scaffolding.",
        "- If the request is about state holder shape, start with the appropriate state skeleton.",
        "- If the request touches navigation, route maps, redirects, or deep links, split the routing work by responsibility.",
        "- If the request touches auth SDK wrapping, auth state, or repository wiring, use the matching Firebase skill.",
        "- If the request is about startup UX on web, start with the web loading skill.",
        "- If the request is about release readiness, separate signing config from release validation.",
        "- If the request is about performance symptoms or regressions, start with performance audit.",
        "- If the request is about design token mapping or localization sync, start with tooling.",
        "",
        "## Decision matrix",
        "",
        "| Category | Skill | Goal | Triggers | Input type | Output type | Difficulty | Related skills | Anti-patterns |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for skill in docs:
        lines.append(
            "| "
            + " | ".join(
                [
                    skill.category,
                    f"`skills/{skill.category}/{skill.name}/SKILL.md`",
                    summarize(skill.purpose),
                    summarize(list_to_summary(split_bullets(skill.use_when))),
                    summarize(list_to_summary(split_bullets(skill.inputs_required))),
                    summarize(list_to_summary(split_bullets(skill.output_contract))),
                    difficulty_for(skill),
                    summarize(list_to_summary(split_bullets(skill.related_skills))),
                    summarize(list_to_summary(split_bullets(skill.do_not_use_when))),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Selection hints",
            "",
            "- New app from scratch usually starts with folder scaffold, then contract scaffold, then state and routing skills.",
            "- Legacy cleanup usually starts with `flutter-clean-architecture-audit`, then the matching contract or state skill.",
            "- Release work should separate signing config from validation and iOS readiness.",
        ]
    )
    return "\n".join(lines) + "\n"


def summarize(text: str, limit: int = 84) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) > limit:
        cleaned = cleaned[: limit - 1].rstrip() + "…"
    return cleaned.replace("|", "\\|")


def list_to_summary(items: list[str]) -> str:
    return "; ".join(item for item in items if item)


def difficulty_for(skill: SkillDoc) -> str:
    name = skill.name.lower()
    if any(token in name for token in ["audit", "validate", "check"]):
        return "Medium"
    if any(token in name for token in ["repository", "auth", "performance", "deeplink", "release"]):
        return "Hard"
    return "Low"


def sync_index_command(overlay: Path, write: bool, check: bool) -> int:
    generated = generate_index(overlay)
    index_path = overlay / "SKILLS_INDEX.md"
    if write:
        write_text(index_path, generated)
        print(f"Wrote {index_path}")
        return 0
    current = read_text(index_path)
    if current != generated:
        if check:
            print("SKILLS_INDEX.md is out of sync with skill metadata:", file=sys.stderr)
            diff = difflib.unified_diff(
                current.splitlines(),
                generated.splitlines(),
                fromfile=str(index_path),
                tofile="generated",
                lineterm="",
            )
            for line in diff:
                print(line, file=sys.stderr)
            return 1
        print(generated)
        return 0
    print(f"{index_path} is in sync")
    return 0


def discover_doc_files(overlay: Path) -> list[Path]:
    docs: list[Path] = [
        overlay / "README.md",
        overlay / "AGENTS.overlay.md",
        overlay / "HOW_TO_USE.md",
        overlay / "SKILLS_INDEX.md",
        overlay / "SKILL_SCHEMA.md",
        overlay / "AGENT_CONTRIBUTION_RULES.md",
        overlay / "docs" / "tutorials" / "README.md",
        overlay / "docs" / "tutorials" / "getting-started.md",
        overlay / "docs" / "tutorials" / "how-skills-work.md",
        overlay / "docs" / "tutorials" / "real-use-cases.md",
        overlay / "docs" / "tutorials" / "add-a-new-skill.md",
        overlay / "docs" / "architecture" / "skill-change-impact-map.md",
        overlay / "examples" / "README.md",
        overlay / "examples" / "full-feature-implementation.md",
        overlay / "examples" / "firebase-integration-example.md",
        overlay / "examples" / "routing-example.md",
        overlay / "examples" / "release-config-example.md",
    ]
    docs.extend(sorted((overlay / "workflows").glob("*/README.md")))
    docs.extend(sorted((overlay / "templates").glob("*.md")))
    docs.extend(sorted((overlay / "policies").glob("*/*.md")))
    docs.extend(sorted((overlay / "checklists").glob("*.md")))
    docs.extend(
        [
            repo_root() / "tools/skillgen/README.md",
        ]
    )
    return [path for path in docs if path.exists()]


def docs_check_command(overlay: Path) -> int:
    issues: list[str] = []
    docs = discover_doc_files(overlay)
    for path in docs:
        text = read_text(path)
        for deprecated in sorted(DEPRECATED_SKILL_NAMES):
            if re.search(rf"(?<![A-Za-z0-9-]){re.escape(deprecated)}(?![A-Za-z0-9-])", text):
                issues.append(f"{path}: stale reference to deprecated skill name '{deprecated}'")
        for link in extract_links(path, text):
            if link.startswith("http://") or link.startswith("https://"):
                continue
            if "#" in link:
                link = link.split("#", 1)[0]
            target = resolve_link(path, link)
            if not target.exists():
                issues.append(f"{path}: broken internal link -> {link}")
    if issues:
        print("Documentation consistency check failed:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(f"Validated docs consistency across {len(docs)} files")
    return 0


def scaffold_skill(
    overlay: Path,
    category: str,
    name: str,
    purpose: str,
    inputs: str,
    outputs: str,
    triggers: str = "",
    related_skills: str = "",
    anti_patterns: str = "",
) -> int:
    category_dir = overlay / "skills" / category / name
    if category_dir.exists():
        print(f"{category_dir} already exists", file=sys.stderr)
        return 1

    template = Template((repo_root() / "tools/skillgen/templates/skill.md.template").read_text(encoding="utf-8"))
    content = template.substitute(
        skill_name=name,
        purpose=purpose or "Describe the purpose of this skill.",
        use_when=format_bullets(split_semicolon_list(triggers), default="Describe the situations that require this skill."),
        do_not_use_when=format_bullets(
            split_semicolon_list(anti_patterns),
            default="Describe when this skill should not be used.",
        ),
        inputs_required=format_bullets(split_semicolon_list(inputs), default="List the required inputs."),
        constraints="- Keep the scope atomic.\n- Avoid duplicate responsibility with neighboring skills.",
        workflow="1. Inspect the request.\n2. Create or modify only the files in this responsibility.\n3. Return the output contract.\n4. Verify the result.",
        output_contract=format_bullets(split_semicolon_list(outputs), default="Describe the exact files or artifacts this skill must produce."),
        validation_checklist="- The skill stays atomic.\n- The output is deterministic.\n- The files referenced in references exist.",
        related_skills=format_bullets(split_semicolon_list(related_skills), default="Link to neighboring skills or leave this skill as a standalone unit."),
        references=(
            f"- [`examples/README.md`](examples/README.md)\n"
            f"- [`checklists/README.md`](checklists/README.md)\n"
            f"- [`references/README.md`](references/README.md)\n"
            f"- [`../../../examples/full-feature-implementation.md`](../../../examples/full-feature-implementation.md)\n"
            f"- [`../../../templates/feature-module-template.md`](../../../templates/feature-module-template.md)"
        ),
        real_example=f"- {name.replace('-', ' ')} applied to a Flutter feature or app slice.",
        real_file_output_sample=(
            f"skills/{category}/{name}/SKILL.md\n"
            f"skills/{category}/{name}/examples/README.md\n"
            f"skills/{category}/{name}/checklists/README.md\n"
            f"skills/{category}/{name}/references/README.md"
        ),
    )
    write_text(category_dir / "SKILL.md", content)
    write_text(category_dir / "examples" / "README.md", f"# {name} Examples\n\nPlaceholder examples for {name}.\n")
    write_text(category_dir / "checklists" / "README.md", f"# {name} Checklists\n\nPlaceholder checklist guidance for {name}.\n")
    write_text(category_dir / "references" / "README.md", f"# {name} References\n\nPlaceholder reference links for {name}.\n")
    print(f"Created {category_dir}")
    return 0


def split_semicolon_list(text: str) -> list[str]:
    if not text:
        return []
    return [item.strip() for item in re.split(r"[;\n]", text) if item.strip()]


def format_bullets(items: list[str], default: str) -> str:
    if not items:
        return f"- {default}"
    return "\n".join(f"- {item}" for item in items)


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value or default


def new_command(args: argparse.Namespace) -> int:
    overlay = overlay_root(args.overlay)
    category = args.category or ask("Skill category", "routing")
    name = args.name or ask("Skill name", "flutter-new-skill")
    purpose = args.purpose or ask("Purpose", "Describe the skill purpose.")
    inputs = args.inputs or ask("Inputs", "Input 1; Input 2")
    outputs = args.outputs or ask("Outputs", "Output file 1; Output file 2")
    triggers = args.triggers or ask("Triggers", "")
    related_skills = args.related_skills or ask("Related skills", "")
    anti_patterns = args.anti_patterns or ask("Anti-patterns", "")
    return scaffold_skill(
        overlay,
        category=category,
        name=name,
        purpose=purpose,
        inputs=inputs,
        outputs=outputs,
        triggers=triggers,
        related_skills=related_skills,
        anti_patterns=anti_patterns,
    )


def check_command(args: argparse.Namespace) -> int:
    overlay = overlay_root(args.overlay)
    results = [
        validate_skills(overlay),
        sync_index_command(overlay, write=False, check=True),
        overlap_command(overlay, report_path=None, fail_on_overlap=True),
        docs_check_command(overlay),
    ]
    return 0 if all(code == 0 for code in results) else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="skillgen", description="Generate and validate Flutter overlay skills")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_overlay_arg(command_parser: argparse.ArgumentParser) -> None:
        command_parser.add_argument("--overlay", default="overlays/mobile-flutter", help="Overlay path relative to repo root")

    new_parser = subparsers.add_parser("new", help="Create a new skill folder from the standard template")
    add_overlay_arg(new_parser)
    new_parser.add_argument("--category")
    new_parser.add_argument("--name")
    new_parser.add_argument("--purpose")
    new_parser.add_argument("--inputs")
    new_parser.add_argument("--outputs")
    new_parser.add_argument("--triggers")
    new_parser.add_argument("--related-skills")
    new_parser.add_argument("--anti-patterns")
    new_parser.set_defaults(func=new_command)

    validate_parser = subparsers.add_parser("validate", help="Validate skill structure and content quality")
    add_overlay_arg(validate_parser)
    validate_parser.set_defaults(func=lambda args: validate_skills(overlay_root(args.overlay)))

    sync_parser = subparsers.add_parser("sync-index", help="Generate or check the skill index")
    add_overlay_arg(sync_parser)
    sync_parser.add_argument("--write", action="store_true", help="Write the generated index to SKILLS_INDEX.md")
    sync_parser.add_argument("--check", action="store_true", help="Fail if the current index differs from generated output")
    sync_parser.set_defaults(func=lambda args: sync_index_command(overlay_root(args.overlay), args.write, args.check))

    overlap_parser = subparsers.add_parser("overlap", help="Generate overlap report and optionally fail on findings")
    add_overlay_arg(overlap_parser)
    overlap_parser.add_argument("--report", help="Write the overlap report to this path")
    overlap_parser.add_argument("--fail-on-overlap", action="store_true", help="Exit non-zero when overlap findings exist")
    overlap_parser.set_defaults(
        func=lambda args: overlap_command(
            overlay_root(args.overlay),
            Path(args.report) if args.report else None,
            args.fail_on_overlap,
        )
    )

    docs_parser = subparsers.add_parser("docs-check", help="Check docs consistency and internal links")
    add_overlay_arg(docs_parser)
    docs_parser.set_defaults(func=lambda args: docs_check_command(overlay_root(args.overlay)))

    check_parser = subparsers.add_parser("check", help="Run validation, index sync, overlap, and docs checks")
    add_overlay_arg(check_parser)
    check_parser.set_defaults(func=check_command)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except BrokenPipeError:
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
