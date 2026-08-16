#!/usr/bin/env python3
"""Snabb deterministisk validering för Under stilla vatten-projektet.

Använder endast Python-standardbiblioteket och kan köras både lokalt och i GitHub Actions.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

CHAPTER_RE = re.compile(r"kapitel-(\d{2})\.md$")
CHAPTER_H1_RE = re.compile(r"^#\s+Kapitel\s+(\d+)\s+[–-]\s+(.+?)\s*$")
MARKERS = ("TODO", "FIXME", "[PLACEHOLDER]", "Kapitelnotering")
REQUIRED_PATHS = (
    "README.md",
    "roman-bibel.md",
    "synopsis.md",
    "kapitelplan.md",
    "projektstatus.md",
    "project-index.md",
    "kapitel",
    "karaktarer",
    "kontinuitetsanteckningar.md",
    "tidslinje.md",
    "publishing/metadata.yaml",
    "publishing/epub.css",
    "publishing/fix-epub-after-pandoc.py",
    "publishing/cover.png",
    "scripts/build_book.py",
)
REQUIRED_METADATA_KEYS = ("title", "subtitle", "author", "language", "rights", "cover-image")

def error(errors: list[str], message: str) -> None:
    errors.append(message)
    print(f"ERROR: {message}", file=sys.stderr)

def parse_simple_yaml_scalars(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        if key:
            values[key] = value
    return values


def png_info(path: Path) -> tuple[int, int, int]:
    """Returnera PNG-bredd, höjd och färgtyp utan externa beroenden."""
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("inte en PNG-fil")
    # Första chunk efter signaturen ska vara IHDR.
    if data[12:16] != b"IHDR":
        raise ValueError("PNG saknar IHDR som första chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    color_type = data[25]
    return width, height, color_type

def validate_cover_image(root: Path, metadata: dict[str, str], errors: list[str]) -> None:
    cover_rel = metadata.get("cover-image", "")
    if not cover_rel:
        return
    cover = root / cover_rel
    if not cover.exists():
        return
    try:
        width, height, color_type = png_info(cover)
    except Exception as exc:
        error(errors, f"Omslagsbilden måste vara en läsbar PNG: {cover_rel} ({exc})")
        return
    if min(width, height) < 1400:
        error(errors, f"Omslagsbildens kortaste sida måste vara minst 1400 px: {cover_rel} är {width}×{height}")
    if max(width, height) > 7200:
        error(errors, f"Omslagsbildens längsta sida får inte överstiga 7200 px för Google Play Books: {cover_rel} är {width}×{height}")
    if color_type not in {2, 6}:
        error(errors, f"Omslagsbilden bör vara RGB/RGBA PNG: {cover_rel} har PNG-färgtyp {color_type}")


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for md in sorted(root.rglob("*.md")):
        if any(part in {".git"} for part in md.relative_to(root).parts):
            continue
        text = md.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            target = target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            if " " in target and not target.startswith(("./", "../")):
                target = target.split(" ", 1)[0]
            target = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not target:
                continue
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                error(errors, f"Trasig intern Markdown-länk i {md.relative_to(root)}: {target}")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors: list[str] = []

    if not root.is_dir():
        error(errors, f"Projektkatalogen finns inte: {root}")
        return 1

    for rel in REQUIRED_PATHS:
        if not (root / rel).exists():
            error(errors, f"Obligatorisk projektsökväg saknas: {rel}")

    metadata_path = root / "publishing/metadata.yaml"
    if metadata_path.exists():
        metadata = parse_simple_yaml_scalars(metadata_path)
        for key in REQUIRED_METADATA_KEYS:
            if not metadata.get(key):
                error(errors, f"Metadata saknar värde: {key}")
        if metadata.get("title") != "Under stilla vatten":
            error(errors, "Metadata titel måste vara: Under stilla vatten")
        if metadata.get("author") != "Erland Lindmark":
            error(errors, "Metadata författare måste vara: Erland Lindmark")
        cover = metadata.get("cover-image")
        if cover and not (root / cover).exists():
            error(errors, f"Metadata cover-image pekar på saknad fil: {cover}")
        validate_cover_image(root, metadata, errors)

    chapter_dir = root / "kapitel"
    chapters = sorted(chapter_dir.glob("kapitel-[0-9][0-9].md")) if chapter_dir.exists() else []
    if not chapters:
        error(errors, "Inga kapitel hittades i kapitel/")
    else:
        numbers = []
        for path in chapters:
            match = CHAPTER_RE.match(path.name)
            if not match:
                continue
            number = int(match.group(1))
            numbers.append(number)
            text = path.read_text(encoding="utf-8")
            lines = text.splitlines()
            if not lines:
                error(errors, f"Tom kapitelfil: {path.relative_to(root)}")
                continue
            h1 = lines[0].strip()
            h1_match = CHAPTER_H1_RE.match(h1)
            if not h1_match:
                error(errors, f"Fel H1-format i {path.relative_to(root)}: {h1!r}")
            elif int(h1_match.group(1)) != number:
                error(errors, f"Kapitelnummer i H1 matchar inte filnamn i {path.relative_to(root)}")
            body = "\n".join(lines[1:]).strip()
            if not body:
                error(errors, f"Kapitlet saknar brödtext: {path.relative_to(root)}")
            for marker in MARKERS:
                if marker in text:
                    error(errors, f"Arbetsmarkör '{marker}' finns kvar i {path.relative_to(root)}")
        expected = list(range(1, max(numbers) + 1)) if numbers else []
        if numbers != expected:
            error(errors, f"Kapitelserien har luckor eller fel ordning: {numbers}")

    validate_markdown_links(root, errors)

    if errors:
        print(f"Validering misslyckades: {len(errors)} fel.", file=sys.stderr)
        return 1
    print(f"OK: projektet validerat. {len(chapters)} kapitel hittades.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
