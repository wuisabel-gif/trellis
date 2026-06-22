#!/usr/bin/env python3
"""Scaffold an Obsidian vault from a folder of TubeScribe transcripts.

Takes the per-video transcript files TubeScribe writes (e.g. `tubescribe URL
-o transcripts/`) and turns each into a Markdown note with YAML frontmatter and
the transcript as the body. The semantic part - adding #topic tags and
[[wikilinks]] between related videos - is left to Claude (see SKILL.md), because
that is what turns a folder of notes into a knowledge graph.

Usage:
    python build_vault.py --input transcripts/ --output vault/
    python build_vault.py --input transcripts/ --output vault/ --titles titles.json

`titles.json` (optional) maps a video id to a human title:
    { "dQw4w9WgXcQ": "Never Gonna Give You Up" }
Without it, the note is titled after the file name.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def safe_filename(name: str) -> str:
    name = re.sub(r"[\\/:*?\"<>|]+", " ", name).strip()
    name = re.sub(r"\s+", " ", name)
    return name[:120] or "untitled"


def main() -> int:
    ap = argparse.ArgumentParser(description="Build an Obsidian vault from transcripts.")
    ap.add_argument("--input", required=True, type=Path, help="Folder of transcript files.")
    ap.add_argument("--output", required=True, type=Path, help="Vault folder to create.")
    ap.add_argument("--titles", type=Path, help="Optional JSON map of video id -> title.")
    ap.add_argument(
        "--ext",
        default="txt",
        help="Transcript file extension to read (default: txt).",
    )
    args = ap.parse_args()

    titles: dict[str, str] = {}
    if args.titles and args.titles.exists():
        titles = json.loads(args.titles.read_text(encoding="utf-8"))

    files = sorted(args.input.glob(f"*.{args.ext}"))
    if not files:
        print(f"No *.{args.ext} files found in {args.input}")
        return 1

    args.output.mkdir(parents=True, exist_ok=True)
    written = 0
    for f in files:
        vid = f.stem
        title = titles.get(vid, vid)
        body = f.read_text(encoding="utf-8").strip()
        note = (
            "---\n"
            f"title: {title}\n"
            f"video_id: {vid}\n"
            f"source: https://www.youtube.com/watch?v={vid}\n"
            "type: transcript\n"
            "tags: []   # Claude fills these with #topic tags\n"
            "---\n\n"
            f"# {title}\n\n"
            "> Related: <!-- Claude adds [[wikilinks]] to related videos here -->\n\n"
            f"{body}\n"
        )
        out = args.output / f"{safe_filename(title)}.md"
        out.write_text(note, encoding="utf-8")
        written += 1

    print(f"Wrote {written} notes to {args.output}/")
    print("Next: have Claude read the notes and add #tags + [[wikilinks]], then open the folder in Obsidian.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
