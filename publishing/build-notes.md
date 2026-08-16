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
  cover.png
  build-notes.md
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

## Exportpolicy

- Kapiteltexterna i `kapitel/kapitel-XX.md` är kanonisk källa.
- Kapitelnoteringar ligger i `kapitel/kapitelnoteringar.md` och exporteras inte.
- EPUB/PDF återskapas från kapitlen vid varje build.
- `exports/` ska inte checkas in.
- Lokalt genererade `*.epub` och `*.pdf` ignoreras via `.gitignore`.
- Omslag, metadata och CSS som behövs för bygge ligger i `publishing/`.

## Tekniska byggval

- Pandoc-versionen är låst till `3.1.11.1`.
- EPUB byggs med Pandoc och efterbearbetas av `publishing/fix-epub-after-pandoc.py`.
- Efterbearbetningen säkerställer teknisk navigation via `nav.xhtml` och `toc.ncx`, men ingen synlig innehållsförteckningssida i läsflödet.
- Titelsidan normaliseras med titel, undertitel, författare och copyright.
- Kapitelrubriker visas på två rader: `Kapitel X` och kapitelnamn.
- PDF byggs med Python/ReportLab för att undvika LaTeX- och systemfontberoenden samt för stabil omslags-, titel-, TOC- och kapitelrubriklayout.

## Felsökning

Om EPUB-läsaren visar tom innehållsförteckning ska `nav.xhtml` och `toc.ncx` kontrolleras i den byggda EPUB:en. Byggskriptet validerar att båda innehåller 24 kapitelposter och att `nav.xhtml` inte ligger i spine/läsflödet.

Om PDF-layouten avviker bör `scripts/build_book.py` kontrolleras, eftersom PDF:en byggs direkt där med ReportLab.


## Plattformspublicering

Plattformsspecifikt publiceringsstöd ligger i `publishing/platforms/`.

- `publishing/platforms/apple_books/`
- `publishing/platforms/google_play_books/`

Amazon KDP ingår inte längre i projektet eftersom den plattformen inte är aktuell.

GitHub Actions bygger endast EPUB och PDF:

- `under-stilla-vatten.epub`
- `under-stilla-vatten.pdf`

Inga separata publiceringspaket byggs i nuläget.

## Omslagskontroll

Den kanoniska omslagsbilden är `publishing/cover.png`.

- Storlek: 1400 × 1979 px
- Färgläge: RGB
- Används i både EPUB och PDF

`validate_project.py` kontrollerar att omslagets kortaste sida är minst 1400 px och att längsta sidan inte överstiger 7200 px.

## PDF-navigation

ReportLab-bygget skapar synlig innehållsförteckning och PDF-bokmärken för kapitel 1–24.
