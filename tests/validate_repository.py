#!/usr/bin/env python3
"""Validate the portable skill repository using only the Python standard library."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "india-itr-filing"
SKILL_MD = SKILL / "SKILL.md"


def fail(message: str) -> None:
    print(f"validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    if not SKILL_MD.exists():
        fail("missing skills/india-itr-filing/SKILL.md")

    text = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail("SKILL.md has no YAML frontmatter")

    frontmatter = match.group(1)
    if "name: india-itr-filing" not in frontmatter:
        fail("frontmatter name is missing or mismatched")
    if "description:" not in frontmatter or "Use for" not in frontmatter:
        fail("description must explain what the skill does and when to use it")
    if "TODO" in text:
        fail("SKILL.md still contains TODO text")

    required_guardrails = [
        "primary route plus every applicable modifier",
        "Taxpayer personally",
        "do not submit yet",
        "Form 10-IEA branch only after",
        "confirmed`, `prefilled-only`, `derived`, `unresolved`, `unknown`, or `blocked",
    ]
    lowered_text = text.casefold()
    for guardrail in required_guardrails:
        if guardrail.casefold() not in lowered_text:
            fail(f"missing required guardrail: {guardrail}")

    references = sorted((SKILL / "references").glob("*.md"))
    if len(references) < 6:
        fail("expected at least six focused reference files")
    for reference in references:
        if reference.name not in text:
            fail(f"SKILL.md does not route to {reference.name}")

    privacy = SKILL / "scripts" / "privacy_scan.py"
    result = subprocess.run([sys.executable, str(privacy), str(ROOT)], check=False)
    if result.returncode:
        fail("privacy scan reported potential personal data")

    classifier_test = ROOT / "tests" / "test_case_classifier.py"
    result = subprocess.run([sys.executable, str(classifier_test)], check=False)
    if result.returncode:
        fail("synthetic classifier scenarios failed")

    print("repository validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
