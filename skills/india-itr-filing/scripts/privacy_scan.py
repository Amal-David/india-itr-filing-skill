#!/usr/bin/env python3
"""Fail when a skill tree appears to contain personal or secret data."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PATTERNS = {
    "Indian PAN-like identifier": re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"),
    "Aadhaar-like number": re.compile(r"(?<!\d)(?:\d[ -]?){11}\d(?!\d)"),
    "email address": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I),
    "Indian mobile-like number": re.compile(r"(?<!\d)(?:\+?91[ -]?)?[6-9]\d{9}(?!\d)"),
    "private home path": re.compile(r"/(?:Users|home)/[^/\s]+/"),
    "OTP or password assignment": re.compile(r"\b(?:otp|password|passwd|pwd)\s*[:=]\s*\S+", re.I),
    "long account-like number": re.compile(r"(?<!\d)\d{11,18}(?!\d)"),
}

TEXT_SUFFIXES = {".md", ".txt", ".py", ".yaml", ".yml", ".json", ".toml"}


def iter_text_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES and ".git" not in path.parts:
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--deny", action="append", default=[], help="Additional private literal to reject")
    args = parser.parse_args()

    root = args.path.resolve()
    if not root.exists():
        print("privacy scan failed: target does not exist", file=sys.stderr)
        return 2

    findings: list[tuple[Path, int, str]] = []
    deny = [item.casefold() for item in args.deny if item.strip()]

    for path in iter_text_files(root):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for line_number, line in enumerate(lines, 1):
            lowered = line.casefold()
            for label, pattern in PATTERNS.items():
                if pattern.search(line):
                    findings.append((path, line_number, label))
            for literal in deny:
                if literal in lowered:
                    findings.append((path, line_number, "deny-listed literal"))

    if findings:
        print(f"privacy scan failed: {len(findings)} potential issue(s)")
        for path, line_number, label in findings:
            print(f"- {path.relative_to(root)}:{line_number}: {label}")
        return 1

    print(f"privacy scan passed: {sum(1 for _ in iter_text_files(root))} text file(s) checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
