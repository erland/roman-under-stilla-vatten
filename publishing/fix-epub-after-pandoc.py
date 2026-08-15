#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "opf": "http://www.idpf.org/2007/opf",
    "xhtml": "http://www.w3.org/1999/xhtml",
    "container": "urn:oasis:names:tc:opendocument:xmlns:container",
    "epub": "http://www.idpf.org/2007/ops",
}
ET.register_namespace("", NS["opf"])

def find_container_root(container_xml: Path) -> Path:
    tree = ET.parse(container_xml)
    rootfile = tree.find(".//container:rootfile", NS)
    if rootfile is None:
        raise RuntimeError("EPUB container saknar rootfile.")
    return Path(rootfile.attrib["full-path"])

def split_chapter_headings(epub_dir: Path) -> int:
    changed = 0
    # Matchar både "Kapitel 8 – Titel" och "Kapitel 8 - Titel".
    pattern = re.compile(r"^\s*Kapitel\s+(\d+)\s+[–-]\s+(.+?)\s*$")
    for xhtml in epub_dir.rglob("*.xhtml"):
        tree = ET.parse(xhtml)
        root = tree.getroot()
        local_changed = False
        for h1 in root.findall(".//xhtml:h1", NS):
            text = "".join(h1.itertext()).strip()
            match = pattern.match(text)
            if not match:
                continue
            ident = h1.attrib.get("id")
            klass = h1.attrib.get("class", "")
            h1.clear()
            if ident:
                h1.set("id", ident)
            h1.set("class", (klass + " chapter-heading").strip())
            n = ET.SubElement(h1, f"{{{NS['xhtml']}}}span", {"class": "chapter-number"})
            n.text = f"Kapitel {int(match.group(1))}"
            t = ET.SubElement(h1, f"{{{NS['xhtml']}}}span", {"class": "chapter-title"})
            t.text = match.group(2)
            local_changed = True
        if local_changed:
            tree.write(xhtml, encoding="utf-8", xml_declaration=True)
            changed += 1
    return changed

def set_nav_non_linear(epub_dir: Path, opf_rel: Path) -> bool:
    opf_path = epub_dir / opf_rel
    tree = ET.parse(opf_path)
    root = tree.getroot()
    manifest = root.find("opf:manifest", NS)
    spine = root.find("opf:spine", NS)
    if manifest is None or spine is None:
        raise RuntimeError("EPUB OPF saknar manifest eller spine.")
    nav_ids = {
        item.attrib["id"] for item in manifest.findall("opf:item", NS)
        if "nav" in item.attrib.get("properties", "").split()
    }
    changed = False
    for itemref in spine.findall("opf:itemref", NS):
        if itemref.attrib.get("idref") in nav_ids and itemref.attrib.get("linear") != "no":
            itemref.set("linear", "no")
            changed = True
    if changed:
        tree.write(opf_path, encoding="utf-8", xml_declaration=True)
    return changed

def remove_title_from_toc(epub_dir: Path, opf_rel: Path, title: str) -> int:
    opf_path = epub_dir / opf_rel
    opf = ET.parse(opf_path).getroot()
    manifest = opf.find("opf:manifest", NS)
    if manifest is None:
        return 0
    removed = 0
    for nav_item in manifest.findall("opf:item", NS):
        if "nav" not in nav_item.attrib.get("properties", "").split():
            continue
        nav_path = opf_path.parent / nav_item.attrib["href"]
        nav_tree = ET.parse(nav_path)
        nav_root = nav_tree.getroot()
        parent_map = {child: parent for parent in nav_root.iter() for child in parent}
        for anchor in list(nav_root.findall(".//xhtml:nav[@epub:type='toc']//xhtml:a", NS)):
            label = "".join(anchor.itertext()).strip()
            if label == title:
                li = parent_map.get(anchor)
                if li is not None:
                    ol = parent_map.get(li)
                    if ol is not None:
                        ol.remove(li)
                        removed += 1
        if removed:
            nav_tree.write(nav_path, encoding="utf-8", xml_declaration=True)
    return removed

def repack(epub_dir: Path, output: Path) -> None:
    if output.exists():
        output.unlink()
    with zipfile.ZipFile(output, "w") as z:
        mimetype = epub_dir / "mimetype"
        z.write(mimetype, "mimetype", compress_type=zipfile.ZIP_STORED)
        for path in sorted(epub_dir.rglob("*")):
            if not path.is_file() or path == mimetype:
                continue
            z.write(path, path.relative_to(epub_dir).as_posix(), compress_type=zipfile.ZIP_DEFLATED)

def main() -> int:
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Användning: fix-epub-after-pandoc.py <fil.epub> [titel]", file=sys.stderr)
        return 2
    epub = Path(sys.argv[1]).resolve()
    title = sys.argv[2] if len(sys.argv) == 3 else ""
    if not epub.exists():
        raise FileNotFoundError(epub)

    with tempfile.TemporaryDirectory(prefix="fix-epub-") as tmp:
        unpacked = Path(tmp)
        with zipfile.ZipFile(epub) as z:
            z.extractall(unpacked)
        opf_rel = find_container_root(unpacked / "META-INF/container.xml")
        headings = split_chapter_headings(unpacked)
        nav_changed = set_nav_non_linear(unpacked, opf_rel)
        removed = remove_title_from_toc(unpacked, opf_rel, title) if title else 0
        repack(unpacked, epub)

    print(
        f"Efterbearbetad EPUB: {headings} kapitelrubriker, "
        f"nav linear=no: {nav_changed}, borttagna titelsideposter i TOC: {removed}"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
