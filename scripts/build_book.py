#!/usr/bin/env python3
"""Bygg EPUB och/eller PDF från projektets kanoniska Markdown-kapitel."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

PANDOC_VERSION = "3.1.11.1"
XHTML_NS = "http://www.w3.org/1999/xhtml"
EPUB_NS = "http://www.idpf.org/2007/ops"
OPF_NS = "http://www.idpf.org/2007/opf"

def simple_metadata(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        values[key.strip()] = value
    return values

def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_value).strip("-")

def pandoc_version() -> str:
    result = subprocess.run(["pandoc", "--version"], text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError("Pandoc finns inte i PATH.")
    first = result.stdout.splitlines()[0]
    match = re.search(r"pandoc\s+([0-9][^\s]*)", first)
    return match.group(1) if match else first

def validate_epub(path: Path, expected_chapters: int, title: str) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            raise RuntimeError("EPUB-fel: mimetype ligger inte först.")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise RuntimeError("EPUB-fel: mimetype är komprimerad.")
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = container.find(
            ".//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile"
        )
        if rootfile is None:
            raise RuntimeError("EPUB-fel: OPF-root saknas.")
        opf_name = rootfile.attrib["full-path"]
        opf = ET.fromstring(archive.read(opf_name))
        ns = {"opf": OPF_NS}
        manifest = opf.find("opf:manifest", ns)
        spine = opf.find("opf:spine", ns)
        if manifest is None or spine is None:
            raise RuntimeError("EPUB-fel: manifest/spine saknas.")
        nav_item = next(
            (
                item for item in manifest.findall("opf:item", ns)
                if "nav" in item.attrib.get("properties", "").split()
            ),
            None,
        )
        if nav_item is None:
            raise RuntimeError("EPUB-fel: nav.xhtml saknas i manifestet.")
        nav_path = (Path(opf_name).parent / nav_item.attrib["href"]).as_posix()
        nav_root = ET.fromstring(archive.read(nav_path))
        nav_ns = {"x": XHTML_NS, "epub": EPUB_NS}
        anchors = nav_root.findall(".//x:nav[@epub:type='toc']//x:a", nav_ns)
        labels = ["".join(anchor.itertext()).strip() for anchor in anchors]
        chapter_labels = [label for label in labels if label.startswith("Kapitel ")]
        if len(chapter_labels) != expected_chapters:
            raise RuntimeError(
                f"EPUB-fel: TOC har {len(chapter_labels)} kapitelposter, väntat {expected_chapters}."
            )
        if title in labels:
            raise RuntimeError("EPUB-fel: titelsidan finns felaktigt med i TOC.")
        nav_id = nav_item.attrib["id"]
        nav_refs = [
            ref for ref in spine.findall("opf:itemref", ns)
            if ref.attrib.get("idref") == nav_id
        ]
        if nav_refs:
            raise RuntimeError("EPUB-fel: nav.xhtml ligger i spine/läsflödet.")
        # Guide-reference till nav.xhtml kan ge tomt/konstigt TOC-index i vissa läsare.
        guide = opf.find("opf:guide", ns)
        if guide is not None:
            for ref in guide.findall("opf:reference", ns):
                if ref.attrib.get("type") == "toc" or ref.attrib.get("href", "").endswith("nav.xhtml"):
                    raise RuntimeError("EPUB-fel: guide pekar på nav.xhtml som synlig TOC.")
        # Äldre läsare använder toc.ncx. Den ska också innehålla kapitel 1–24.
        ncx_item = next((item for item in manifest.findall("opf:item", ns) if item.attrib.get("media-type") == "application/x-dtbncx+xml"), None)
        if ncx_item is None:
            raise RuntimeError("EPUB-fel: toc.ncx saknas.")
        ncx_path = (Path(opf_name).parent / ncx_item.attrib["href"]).as_posix()
        ncx_root = ET.fromstring(archive.read(ncx_path))
        ncx_ns = {"ncx": "http://www.daisy.org/z3986/2005/ncx/"}
        ncx_labels = ["".join(node.itertext()).strip() for node in ncx_root.findall(".//ncx:navLabel/ncx:text", ncx_ns)]
        ncx_chapters = [label for label in ncx_labels if label.startswith("Kapitel ")]
        if len(ncx_chapters) != expected_chapters:
            raise RuntimeError(
                f"EPUB-fel: toc.ncx har {len(ncx_chapters)} kapitelposter, väntat {expected_chapters}."
            )
        if title in ncx_labels:
            raise RuntimeError("EPUB-fel: titelsidan finns felaktigt med i toc.ncx.")
        split_headings = 0
        for name in names:
            if not name.endswith(".xhtml"):
                continue
            data = archive.read(name).decode("utf-8", errors="replace")
            if 'class="chapter-number"' in data and ('class="chapter-title-text"' in data or 'class="chapter-title"' in data):
                split_headings += 1
        if split_headings != expected_chapters:
            raise RuntimeError(
                f"EPUB-fel: {split_headings} formaterade kapitelrubriker, väntat {expected_chapters}."
            )


def chapter_info(path: Path) -> tuple[int, str, str]:
    """Returnera kapitelnummer, kapiteltitel och brödtext utan H1-rubrik."""
    raw = path.read_text(encoding="utf-8").strip()
    lines = raw.splitlines()
    if not lines:
        raise RuntimeError(f"Tom kapitelfil: {path}")
    heading = lines[0].strip()
    match = re.match(r"^#\s*Kapitel\s+(\d+)\s+[–-]\s+(.+?)\s*$", heading)
    if not match:
        raise RuntimeError(f"Kapitlet saknar väntad rubrik: {path}")
    number = int(match.group(1))
    title = match.group(2).strip()
    body = "\n".join(lines[1:]).strip()
    return number, title, body

def markdown_inline_to_reportlab(text: str) -> str:
    """Minimal Markdown-inlinekonvertering för romanprosa i ReportLab-paragrafer."""
    import html
    escaped = html.escape(text, quote=False)
    escaped = escaped.replace("  \n", "<br/>").replace("\n", "<br/>")
    # Fetstil före kursiv.
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", escaped)
    escaped = re.sub(r"__(.+?)__", r"<b>\1</b>", escaped)
    escaped = re.sub(r"(?<!_)_(?!_)(.+?)(?<!_)_(?!_)", r"<i>\1</i>", escaped)
    return escaped

def markdown_blocks(body: str) -> list[tuple[str, str]]:
    """Dela kapiteltext i enkla block: paragraph eller scene_break."""
    blocks: list[tuple[str, str]] = []
    current: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped in {"---", "***", "* * *"}:
            if current:
                blocks.append(("paragraph", "\n".join(current).strip()))
                current = []
            blocks.append(("scene_break", stripped))
            continue
        if not stripped:
            if current:
                blocks.append(("paragraph", "\n".join(current).strip()))
                current = []
            continue
        current.append(line.rstrip())
    if current:
        blocks.append(("paragraph", "\n".join(current).strip()))
    return blocks

def build_pdf_reportlab(
    pdf: Path,
    chapters: list[Path],
    *,
    title: str,
    subtitle: str,
    author: str,
    rights: str,
    cover: Path,
) -> None:
    """Bygg tryckbar preview-PDF utan LaTeX, med korrekt omslag, titelsida, TOC och kapitelrubriker."""
    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        from reportlab.lib.pagesizes import mm
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.platypus import (
            BaseDocTemplate,
            Frame,
            PageTemplate,
            PageBreak,
            Paragraph,
            Spacer,
            Image,
            KeepTogether,
            Flowable,
            NextPageTemplate,
        )
        from reportlab.platypus.tableofcontents import TableOfContents
        from reportlab.pdfbase.pdfmetrics import stringWidth
    except Exception as exc:  # pragma: no cover - miljöberoende
        raise RuntimeError("ReportLab krävs för PDF-bygget. Installera med: pip install reportlab") from exc

    page_width, page_height = 140 * mm, 216 * mm
    left_margin, right_margin = 18 * mm, 16 * mm
    top_margin, bottom_margin = 18 * mm, 20 * mm

    class FullPageCover(Flowable):
        def __init__(self, image_path: Path):
            super().__init__()
            self.image_path = str(image_path)
            self.width = page_width
            self.height = page_height

        def wrap(self, avail_width, avail_height):
            return page_width, page_height

        def draw(self):
            self.canv.drawImage(
                self.image_path,
                0,
                0,
                width=page_width,
                height=page_height,
                preserveAspectRatio=False,
                mask="auto",
            )

    class TitlePage(Flowable):
        def wrap(self, avail_width, avail_height):
            return avail_width, avail_height

        def draw(self):
            canv = self.canv
            text_width = page_width - left_margin - right_margin
            y = page_height * 0.62

            def centered_line(value: str, font: str, size: float, leading: float, dy_after: float):
                nonlocal y
                canv.setFont(font, size)
                x = (page_width - stringWidth(value, font, size)) / 2
                canv.drawString(x, y, value)
                y -= dy_after

            centered_line(title, "Times-Bold", 25, 30, 18)
            if subtitle:
                centered_line(subtitle, "Times-Roman", 13, 16, 58)
            else:
                y -= 58
            centered_line(author, "Times-Roman", 13, 16, 42)
            # Copyright närmare sidans nederdel, centrerad och radbruten vid behov.
            from reportlab.platypus import Paragraph
            copyright_style = ParagraphStyle(
                "Copyright",
                fontName="Times-Roman",
                fontSize=8.5,
                leading=10.5,
                alignment=TA_CENTER,
                textColor=colors.black,
            )
            p = Paragraph(markdown_inline_to_reportlab(rights), copyright_style)
            w, h = p.wrap(text_width, 30 * mm)
            p.drawOn(canv, left_margin, page_height * 0.21)

    class RomanDocTemplate(BaseDocTemplate):
        def beforeDocument(self):
            self._first_chapter_page = None

        def afterFlowable(self, flowable):
            bookmark = getattr(flowable, "_bookmarkName", None)
            toc_entry = getattr(flowable, "_tocEntry", None)
            if bookmark and toc_entry:
                self.canv.bookmarkPage(bookmark)
                self.canv.addOutlineEntry(toc_entry, bookmark, level=0, closed=False)
                if self._first_chapter_page is None:
                    self._first_chapter_page = self.page
                printed_page = self.page - self._first_chapter_page + 1
                self.notify("TOCEntry", (0, toc_entry, printed_page, bookmark))

    doc = RomanDocTemplate(
        str(pdf),
        pagesize=(page_width, page_height),
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin,
        title=title,
        author=author,
    )
    frame = Frame(
        left_margin,
        bottom_margin,
        page_width - left_margin - right_margin,
        page_height - top_margin - bottom_margin,
        id="normal",
    )

    def page_number(canv, document):
        first_chapter_page = getattr(document, "_first_chapter_page", None)
        if first_chapter_page is None or document.page < first_chapter_page:
            return
        canv.setFont("Times-Roman", 8)
        canv.drawCentredString(page_width / 2, 8 * mm, str(document.page - first_chapter_page + 1))

    full_frame = Frame(0, 0, page_width, page_height, id="full", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[full_frame]),
        PageTemplate(id="title", frames=[full_frame]),
        PageTemplate(id="main", frames=[frame], onPageEnd=page_number),
    ])

    styles = getSampleStyleSheet()
    story = [
        FullPageCover(cover),
        NextPageTemplate("title"),
        PageBreak(),
        TitlePage(),
        NextPageTemplate("main"),
        PageBreak(),
    ]

    toc_title = ParagraphStyle(
        "TOCTitle",
        parent=styles["Title"],
        fontName="Times-Bold",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        spaceAfter=12 * mm,
    )
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOCLevel0",
            fontName="Times-Roman",
            fontSize=10.5,
            leading=15,
            leftIndent=0,
            firstLineIndent=0,
            spaceBefore=2,
        )
    ]
    story += [Paragraph("Innehåll", toc_title), toc, PageBreak()]

    chapter_number_style = ParagraphStyle(
        "ChapterNumber",
        fontName="Times-Roman",
        fontSize=12.2,
        leading=15,
        alignment=TA_CENTER,
        spaceBefore=0,
        spaceAfter=1.5 * mm,
        keepWithNext=True,
    )
    chapter_title_style = ParagraphStyle(
        "ChapterTitle",
        fontName="Times-Roman",
        fontSize=11,
        leading=13,
        alignment=TA_CENTER,
        spaceBefore=0,
        spaceAfter=8 * mm,
        keepWithNext=True,
    )
    body_style = ParagraphStyle(
        "Body",
        fontName="Times-Roman",
        fontSize=10.3,
        leading=14.3,
        alignment=TA_LEFT,
        spaceBefore=0,
        spaceAfter=4.5,
        firstLineIndent=0,
    )
    scene_style = ParagraphStyle(
        "SceneBreak",
        fontName="Times-Roman",
        fontSize=12,
        leading=14,
        alignment=TA_CENTER,
        spaceBefore=8,
        spaceAfter=8,
    )

    for idx, chapter in enumerate(chapters):
        number, chapter_title, body = chapter_info(chapter)
        if idx > 0:
            story.append(PageBreak())
        bookmark = f"chapter-{number:02d}"
        heading = Paragraph(f"Kapitel {number}", chapter_number_style)
        heading._bookmarkName = bookmark
        heading._tocEntry = f"Kapitel {number}. {chapter_title}"
        story.append(heading)
        story.append(Paragraph(markdown_inline_to_reportlab(chapter_title), chapter_title_style))
        for kind, value in markdown_blocks(body):
            if kind == "scene_break":
                story.append(Paragraph("•", scene_style))
            else:
                story.append(Paragraph(markdown_inline_to_reportlab(value), body_style))

    # multiBuild krävs för att innehållsförteckningen ska få sidnummer.
    doc.multiBuild(story)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--name", default="")
    parser.add_argument(
        "--formats",
        default="epub,pdf",
        help="Kommaseparerade format: epub,pdf (standard: båda).",
    )
    parser.add_argument(
        "--allow-pandoc-version-mismatch",
        action="store_true",
        help="Tillåt annan Pandoc-version än projektets låsta version.",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir).resolve()

    validation = subprocess.run([sys.executable, "scripts/validate_project.py", "."], cwd=root)
    if validation.returncode != 0:
        return validation.returncode

    version = pandoc_version()
    if version != PANDOC_VERSION and not args.allow_pandoc_version_mismatch:
        print(
            f"ERROR: Pandoc {PANDOC_VERSION} krävs för reproducerbart bygge; hittade {version}.",
            file=sys.stderr,
        )
        return 2

    metadata = simple_metadata(root / "publishing/metadata.yaml")
    title = metadata["title"]
    subtitle = metadata.get("subtitle", "")
    author = metadata["author"]
    rights = metadata.get("rights", "")
    cover = root / metadata.get("cover-image", "publishing/cover.png")
    base_name = args.name or slugify(title)
    base_name = re.sub(r"\.(epub|pdf)$", "", base_name, flags=re.IGNORECASE)
    formats = [item.strip().lower() for item in args.formats.split(",") if item.strip()]
    invalid = sorted(set(formats) - {"epub", "pdf"})
    if invalid or not formats:
        print("ERROR: --formats måste innehålla epub och/eller pdf.", file=sys.stderr)
        return 2

    chapters = sorted((root / "kapitel").glob("kapitel-[0-9][0-9].md"))
    output_dir.mkdir(parents=True, exist_ok=True)

    if "epub" in formats:
        output = output_dir / f"{base_name}.epub"
        with tempfile.TemporaryDirectory(prefix="roman-build-") as tmp:
            temp = Path(tmp)
            title_page = temp / "00-title.md"
            title_page.write_text(
                f"# {title}\n\n"
                f"## {subtitle}\n\n"
                f"**{author}**\n\n"
                f"**{rights}**\n",
                encoding="utf-8",
            )
            command = [
                "pandoc",
                str(title_page),
                *[str(path) for path in chapters],
                "--from=markdown+raw_html",
                "--to=epub3",
                "--output", str(output),
                "--metadata-file", str(root / "publishing/metadata.yaml"),
                "--css", str(root / "publishing/epub.css"),
                "--epub-cover-image", str(cover),
                "--epub-title-page=false",
                "--toc",
                "--toc-depth=1",
                "--split-level=1",
            ]
            subprocess.run(command, cwd=root, check=True)
            subprocess.run(
                [
                    sys.executable,
                    str(root / "publishing/fix-epub-after-pandoc.py"),
                    str(output),
                    title,
                    subtitle,
                    author,
                    rights,
                ],
                cwd=root,
                check=True,
            )
        validate_epub(output, len(chapters), title)
        print(f"OK: EPUB skapad och verifierad: {output}")

    if "pdf" in formats:
        pdf = output_dir / f"{base_name}.pdf"
        build_pdf_reportlab(
            pdf,
            chapters,
            title=title,
            subtitle=subtitle,
            author=author,
            rights=rights,
            cover=cover,
        )
        print(f"OK: PDF skapad och verifierad: {pdf}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
