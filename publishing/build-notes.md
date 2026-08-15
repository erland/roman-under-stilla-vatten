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
- PDF byggs med XeLaTeX och TeX Gyre-fontpaketet i GitHub Actions.
