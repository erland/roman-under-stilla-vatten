# GitHub Actions-publicering

Detta projekt har GitHub Actions enligt Romanskaparens publiceringskoncept.

## Målstruktur

`.github/` ligger i repositoryts rot, på samma nivå som `README.md`.

```text
README.md
.github/
  workflows/
    01-validate.yml
    02-build-preview.yml
    03-release.yml
scripts/
  validate_project.py
  build_book.py
publishing/
  metadata.yaml
  epub.css
  fix-epub-after-pandoc.py
  pdf-template.tex
  pdf-filter.lua
  cover.png
```

## Workflows

### Validate

Körs vid pull request och push till `main` när relevanta projektfiler ändras.

Kontrollerar bland annat:

- obligatoriska projektfiler
- metadata
- kapitelserie utan luckor
- kapitelrubriker enligt `# Kapitel XX – Titel`
- att kapitelfilerna inte innehåller kapitelnoteringar eller arbetsmarkörer
- interna Markdown-länkar

### Build Preview

Startas manuellt via `workflow_dispatch`.

Bygger:

- `under-stilla-vatten.epub`
- `under-stilla-vatten.pdf`

och laddar upp båda i ett gemensamt GitHub Actions-artifact:

- `under-stilla-vatten-preview`

### Release

Körs när en tagg som börjar med `v` pushas, till exempel:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Då byggs EPUB/PDF och publiceras som separata GitHub Release-assets.

## Viktigt

- Kapiteltexterna i `kapitel/kapitel-XX.md` är kanonisk källa.
- Kapitelnoteringar ligger i `kapitel/kapitelnoteringar.md` och exporteras inte.
- EPUB/PDF återskapas från kapitlen vid varje build.
- Pandoc-versionen är låst till `3.1.11.1`.
- PDF byggs med Python/ReportLab i GitHub Actions för att undvika LaTeX- och systemfontberoenden.

## Felsökning: PDF-layout och fontfel

PDF-bygget använder inte längre Pandoc/LaTeX för PDF:en. `scripts/build_book.py` bygger PDF:en med ReportLab och använder endast EPUB-grenen för Pandoc.

Detta korrigerar tidigare PDF-problem:
- ingen extra tom sida före omslaget
- ingen extra tom sida före innehållsförteckningen
- innehållsförteckningen fylls med kapitel 1–24
- endast en titelsida efter omslaget
- copyright finns på titelsidan
- inga automatiska `0.x`-kapitelnummer
- kapitelrubriker visas på två rader: `Kapitel X` och kapitelnamn

GitHub Actions installerar därför Python-beroendet `reportlab` i stället för LaTeX-paket.


## 2026-08-16 – EPUB/PDF stil- och navigationsfix

- Action-EPUB använder nu samma förenklade CSS-princip som den tidigare exports-EPUB:en.
- `nav.xhtml` behålls tekniskt i manifestet med `properties="nav"`, men tas bort ur spine/läsflödet.
- `toc.ncx` valideras med kapitel 1–24 för äldre läsare.
- CSS-regeln som dolde `nav#toc` är borttagen så läsarnas tekniska innehållsförteckning inte blir tom.
- PDF byggs fortsatt med ReportLab, med samma tvådelade kapitelrubriker och serifbaserade bokstil som EPUB:en.

## 2026-08-16 – EPUB-navigation och titelsida

- `fix-epub-after-pandoc.py` skriver nu om `nav.xhtml` och `toc.ncx` som rena, prefixfria filer efter Pandoc.
- `nav.xhtml` tas bort ur spine/läsflödet men behålls i manifestet med `properties="nav"`.
- `toc.ncx` innehåller 24 `navPoint`-poster och spine pekar på `toc="ncx"`.
- Titelsidan normaliseras till samma XHTML-struktur som tidigare export: titel, undertitel, författare och copyright i `section#under-stilla-vatten`.
