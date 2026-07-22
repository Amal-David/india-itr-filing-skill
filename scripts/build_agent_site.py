#!/usr/bin/env python3
"""Build a deterministic Agent Skills discovery site."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import shutil
import tarfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "india-itr-filing"
SITE_SOURCE = ROOT / "agent-site"
PUBLIC_ORIGIN = "https://india-itr-filing-skill.pages.dev"
SCHEMA = "https://schemas.agentskills.io/discovery/0.2.0/schema.json"


def archive_bytes() -> bytes:
    """Return a deterministic tar.gz with SKILL.md at the archive root."""
    tar_buffer = io.BytesIO()
    with tarfile.open(fileobj=tar_buffer, mode="w") as archive:
        for path in sorted(SKILL.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            relative = path.relative_to(SKILL)
            data = path.read_bytes()
            info = tarfile.TarInfo(relative.as_posix())
            info.size = len(data)
            info.mode = 0o755 if relative.parts[0] == "scripts" else 0o644
            info.mtime = 0
            info.uid = 0
            info.gid = 0
            info.uname = ""
            info.gname = ""
            archive.addfile(info, io.BytesIO(data))

    compressed = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed, mode="wb", filename="", mtime=0) as stream:
        stream.write(tar_buffer.getvalue())
    return compressed.getvalue()


def build(output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(SITE_SOURCE, output)

    discovery = output / ".well-known" / "agent-skills"
    discovery.mkdir(parents=True)
    artifact = archive_bytes()
    artifact_path = discovery / "india-itr-filing.tar.gz"
    artifact_path.write_bytes(artifact)
    digest = hashlib.sha256(artifact).hexdigest()

    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    description = next(
        line.removeprefix("description:").strip()
        for line in skill_text.splitlines()
        if line.startswith("description:")
    )
    index = {
        "$schema": SCHEMA,
        "skills": [
            {
                "name": "india-itr-filing",
                "type": "archive",
                "description": description,
                "url": "/.well-known/agent-skills/india-itr-filing.tar.gz",
                "digest": f"sha256:{digest}",
            }
        ],
    }
    (discovery / "index.json").write_text(
        json.dumps(index, indent=2) + "\n", encoding="utf-8"
    )

    (output / "llms.txt").write_text(
        "# India ITR Filing Agent Skill\n\n"
        "> Privacy-safe assistance for preparing and reviewing Indian individual "
        "income-tax returns.\n\n"
        "## Agent Skill\n\n"
        f"- [{PUBLIC_ORIGIN}/.well-known/agent-skills/index.json]"
        f"({PUBLIC_ORIGIN}/.well-known/agent-skills/index.json): Discovery index\n"
        f"- [{PUBLIC_ORIGIN}/.well-known/agent-skills/india-itr-filing.tar.gz]"
        f"({PUBLIC_ORIGIN}/.well-known/agent-skills/india-itr-filing.tar.gz): "
        "Digest-verifiable skill archive\n\n"
        "## Source\n\n"
        "- [GitHub repository](https://github.com/Amal-David/india-itr-filing-skill)\n",
        encoding="utf-8",
    )
    (output / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{PUBLIC_ORIGIN}/</loc></url>\n"
        f"  <url><loc>{PUBLIC_ORIGIN}/llms.txt</loc></url>\n"
        f"  <url><loc>{PUBLIC_ORIGIN}/.well-known/agent-skills/index.json</loc></url>\n"
        "</urlset>\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path, nargs="?", default=ROOT / "dist" / "agent-site")
    args = parser.parse_args()
    build(args.output.resolve())
    print(f"built agent site: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
