#!/usr/bin/env python3
from __future__ import annotations

import html
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
    "ncx": "http://www.daisy.org/z3986/2005/ncx/",
}

def register_default_namespace(namespace: str) -> None:
    """ElementTree har global namespace-registrering. Sätt rätt default före varje write()."""
    ET.register_namespace("", namespace)
    ET.register_namespace("epub", NS["epub"])
    ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
    ET.register_namespace("opf", NS["opf"])

def write_xml(tree: ET.ElementTree, path: Path, default_namespace: str) -> None:
    register_default_namespace(default_namespace)
    tree.write(path, encoding="utf-8", xml_declaration=True)

def find_container_root(container_xml: Path) -> Path:
    tree = ET.parse(container_xml)
    rootfile = tree.find(".//container:rootfile", NS)
    if rootfile is None:
        raise RuntimeError("EPUB container saknar rootfile.")
    return Path(rootfile.attrib["full-path"])

def split_chapter_headings(epub_dir: Path) -> int:
    changed = 0
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
            t = ET.SubElement(h1, f"{{{NS['xhtml']}}}span", {"class": "chapter-title-text"})
            t.text = match.group(2)
            local_changed = True
        if local_changed:
            write_xml(tree, xhtml, NS["xhtml"])
            changed += 1
    return changed

def normalize_opf(epub_dir: Path, opf_rel: Path) -> tuple[str, str, str, int, int]:
    """Ta bort nav.xhtml ur spine/läsflöde och guide-toc utan att ta bort teknisk nav."""
    opf_path = epub_dir / opf_rel
    tree = ET.parse(opf_path)
    root = tree.getroot()
    manifest = root.find("opf:manifest", NS)
    spine = root.find("opf:spine", NS)
    if manifest is None or spine is None:
        raise RuntimeError("EPUB OPF saknar manifest eller spine.")

    nav_item = None
    ncx_item = None
    for item in manifest.findall("opf:item", NS):
        if "nav" in item.attrib.get("properties", "").split():
            nav_item = item
        if item.attrib.get("media-type") == "application/x-dtbncx+xml":
            ncx_item = item
    if nav_item is None:
        raise RuntimeError("EPUB OPF saknar manifest-item med properties='nav'.")
    if ncx_item is None:
        raise RuntimeError("EPUB OPF saknar toc.ncx i manifestet.")

    removed_spine = 0
    for itemref in list(spine.findall("opf:itemref", NS)):
        if itemref.attrib.get("idref") == nav_item.attrib["id"]:
            spine.remove(itemref)
            removed_spine += 1

    removed_guide = 0
    for guide in list(root.findall("opf:guide", NS)):
        for ref in list(guide.findall("opf:reference", NS)):
            if ref.attrib.get("type") == "toc" or ref.attrib.get("href", "").endswith("nav.xhtml"):
                guide.remove(ref)
                removed_guide += 1
        if len(list(guide)) == 0:
            root.remove(guide)

    uid = ""
    meta = root.find("opf:metadata", NS)
    if meta is not None:
        ident = meta.find(".//{http://purl.org/dc/elements/1.1/}identifier")
        if ident is not None and ident.text:
            uid = ident.text.strip()
    if not uid:
        uid = "urn:uuid:under-stilla-vatten"

    spine.set("toc", ncx_item.attrib["id"])
    write_xml(tree, opf_path, NS["opf"])
    return nav_item.attrib["href"], ncx_item.attrib["href"], uid, removed_spine, removed_guide

def collect_chapter_nav(epub_dir: Path, opf_rel: Path) -> list[tuple[str, str]]:
    """Hämta kapitelhref och etiketter från XHTML-filerna i spine-ordning."""
    opf_path = epub_dir / opf_rel
    opf = ET.parse(opf_path).getroot()
    manifest = opf.find("opf:manifest", NS)
    spine = opf.find("opf:spine", NS)
    if manifest is None or spine is None:
        raise RuntimeError("EPUB OPF saknar manifest eller spine.")

    id_to_href = {item.attrib["id"]: item.attrib["href"] for item in manifest.findall("opf:item", NS)}
    chapters: list[tuple[str, str]] = []
    for itemref in spine.findall("opf:itemref", NS):
        href = id_to_href.get(itemref.attrib.get("idref", ""))
        if not href or not href.endswith(".xhtml"):
            continue
        full = opf_path.parent / href
        if not full.exists():
            continue
        root = ET.parse(full).getroot()
        h1 = root.find(".//xhtml:h1", NS)
        if h1 is None:
            continue
        number_span = h1.find(".//xhtml:span[@class='chapter-number']", NS)
        title_span = h1.find(".//xhtml:span[@class='chapter-title-text']", NS)
        if number_span is not None and title_span is not None:
            number_text = " ".join("".join(number_span.itertext()).split())
            title_text = " ".join("".join(title_span.itertext()).split())
            text = f"{number_text} – {title_text}"
        else:
            text = " ".join("".join(h1.itertext()).split())
        if not text.startswith("Kapitel "):
            continue
        chapters.append((href, text))
    return chapters

def write_plain_nav(epub_dir: Path, opf_rel: Path, nav_href: str, chapters: list[tuple[str, str]], title: str) -> None:
    nav_path = (epub_dir / opf_rel).parent / nav_href
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<!DOCTYPE html>',
        '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="sv-SE" xml:lang="sv-SE">',
        '<head>',
        '  <meta charset="utf-8" />',
        '  <title>Innehållsförteckning</title>',
        '  <link rel="stylesheet" type="text/css" href="styles/stylesheet1.css" />',
        '</head>',
        '<body epub:type="frontmatter">',
        '  <nav epub:type="toc" id="toc" role="doc-toc">',
        '    <h1>Innehållsförteckning</h1>',
        '    <ol>',
    ]
    for href, label in chapters:
        lines.append(f'      <li><a href="{html.escape(href, quote=True)}">{html.escape(label)}</a></li>')
    lines += [
        '    </ol>',
        '  </nav>',
        '</body>',
        '</html>',
        '',
    ]
    nav_path.write_text("\n".join(lines), encoding="utf-8")

def write_plain_ncx(epub_dir: Path, opf_rel: Path, ncx_href: str, chapters: list[tuple[str, str]], title: str, uid: str) -> None:
    ncx_path = (epub_dir / opf_rel).parent / ncx_href
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<ncx version="2005-1" xmlns="http://www.daisy.org/z3986/2005/ncx/">',
        '  <head>',
        f'    <meta name="dtb:uid" content="{html.escape(uid, quote=True)}" />',
        '    <meta name="dtb:depth" content="1" />',
        '    <meta name="dtb:totalPageCount" content="0" />',
        '    <meta name="dtb:maxPageNumber" content="0" />',
        '  </head>',
        f'  <docTitle><text>{html.escape(title)}</text></docTitle>',
        '  <navMap>',
    ]
    for i, (href, label) in enumerate(chapters, start=1):
        lines += [
            f'    <navPoint id="navPoint-{i}" playOrder="{i}">',
            f'      <navLabel><text>{html.escape(label)}</text></navLabel>',
            f'      <content src="{html.escape(href, quote=True)}" />',
            '    </navPoint>',
        ]
    lines += [
        '  </navMap>',
        '</ncx>',
        '',
    ]
    ncx_path.write_text("\n".join(lines), encoding="utf-8")

def normalize_title_page(epub_dir: Path, opf_rel: Path, title: str, subtitle: str, author: str, rights: str) -> bool:
    """Gör Action-titelsidan strukturellt lik den tidigare exports-EPUB:en."""
    opf_path = epub_dir / opf_rel
    ch001 = opf_path.parent / "text/ch001.xhtml"
    if not ch001.exists():
        return False
    safe_title = html.escape(title)
    safe_subtitle = html.escape(subtitle)
    safe_author = html.escape(author)
    safe_rights = html.escape(rights)
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="sv-SE" xml:lang="sv-SE">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <title>ch001.xhtml</title>
  <style>
  </style>
  <link rel="stylesheet" type="text/css" href="../styles/stylesheet1.css" />
</head>
<body epub:type="bodymatter">
<section id="under-stilla-vatten" class="level1">
<h1>{safe_title}</h1>
<section id="en-kallviksdeckare" class="level2">
<h2>{safe_subtitle}</h2>
<p><strong>{safe_author}</strong></p>
<p><strong>{safe_rights}</strong></p>
</section>
</section>
</body>
</html>
"""
    ch001.write_text(xml, encoding="utf-8")
    return True

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
    if len(sys.argv) < 2 or len(sys.argv) > 6:
        print("Användning: fix-epub-after-pandoc.py <fil.epub> [titel] [undertitel] [författare] [copyright]", file=sys.stderr)
        return 2
    epub = Path(sys.argv[1]).resolve()
    title = sys.argv[2] if len(sys.argv) >= 3 else ""
    subtitle = sys.argv[3] if len(sys.argv) >= 4 else ""
    author = sys.argv[4] if len(sys.argv) >= 5 else ""
    rights = sys.argv[5] if len(sys.argv) >= 6 else ""
    if not epub.exists():
        raise FileNotFoundError(epub)

    with tempfile.TemporaryDirectory(prefix="fix-epub-") as tmp:
        unpacked = Path(tmp)
        with zipfile.ZipFile(epub) as z:
            z.extractall(unpacked)
        opf_rel = find_container_root(unpacked / "META-INF/container.xml")
        title_page_changed = normalize_title_page(unpacked, opf_rel, title, subtitle, author, rights)
        headings = split_chapter_headings(unpacked)
        nav_href, ncx_href, uid, removed_spine, removed_guide = normalize_opf(unpacked, opf_rel)
        chapters = collect_chapter_nav(unpacked, opf_rel)
        if len(chapters) == 0:
            raise RuntimeError("Kunde inte hitta några kapitel för EPUB-navigation.")
        write_plain_nav(unpacked, opf_rel, nav_href, chapters, title)
        write_plain_ncx(unpacked, opf_rel, ncx_href, chapters, title, uid)
        repack(unpacked, epub)

    print(
        f"Efterbearbetad EPUB: {headings} kapitelrubriker, "
        f"nav ur spine: {removed_spine}, "
        f"borttagna guide-toc: {removed_guide}, "
        f"navposter: {len(chapters)}, "
        f"titelsida normaliserad: {title_page_changed}"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
