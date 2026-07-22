#!/usr/bin/env python3
"""Validate the generated Agent Skills discovery site."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import tarfile
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts" / "build_agent_site.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_agent_site", BUILD_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    builder = load_builder()
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "site"
        builder.build(output)

        index = json.loads(
            (output / ".well-known" / "agent-skills" / "index.json").read_text()
        )
        assert index["$schema"] == builder.SCHEMA
        assert len(index["skills"]) == 1
        skill = index["skills"][0]
        assert skill["name"] == "india-itr-filing"
        assert skill["type"] == "archive"
        skill_description = next(
            line.removeprefix("description:").strip()
            for line in (ROOT / "skills" / "india-itr-filing" / "SKILL.md")
            .read_text()
            .splitlines()
            if line.startswith("description:")
        )
        assert skill["description"] == skill_description

        archive_path = output / skill["url"].lstrip("/")
        actual_digest = "sha256:" + hashlib.sha256(archive_path.read_bytes()).hexdigest()
        assert actual_digest == skill["digest"]

        with tarfile.open(archive_path, "r:gz") as archive:
            names = archive.getnames()
            assert "SKILL.md" in names
            assert "agents/openai.yaml" in names
            assert any(name.startswith("references/") for name in names)
            assert any(name.startswith("scripts/") for name in names)
            assert all(not name.startswith("/") and ".." not in Path(name).parts for name in names)
            assert all(not member.issym() and not member.islnk() for member in archive.getmembers())

        assert "Content-Signal:" in (output / "robots.txt").read_text()
        assert "agent-skills/index.json" in (output / "llms.txt").read_text()
        assert "text/markdown" in (output / "_worker.js").read_text()

    print("agent site validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
