# Projektstatus

## Projekt

- Titel: Under stilla vatten
- Undertitel: En Kallviksdeckare
- Författare: Erland Lindmark
- Omslagsbild: Skapad; kanonisk byggfil är `publishing/cover.png`

## Nuvarande fas

Projektet är städat för GitHub Actions-baserad export. EPUB och PDF ska inte längre ligga incheckade i repositoryt, utan byggas som Actions-artifacts eller GitHub Release-assets.

## Senast godkända/reviderade del

- Kapitel 19 justerat 2026-05-31: frasen om att fotot kan stämma med 1979 ändrades till att fotot kan stämma med Karin, eftersom födelseåret ännu inte avslöjas för läsaren.
- Kapitel 19 uppdaterat 2026-05-31 med användarens reviderade version; Kajsa/Karin-spåret är synkat mot födelseår 1979.
- Kapitel 1–24 är språk- och scenputsade v2.1.
- Kapitelnoteringar är flyttade till `kapitel/kapitelnoteringar.md`; kapitelfilerna är rensade från arbetsnoteringar.

## GitHub Actions-status

- `.github/` ligger i repositoryts rot, på samma nivå som `README.md`.
- `01-validate.yml` validerar projektet.
- `02-build-preview.yml` bygger EPUB/PDF manuellt som preview-artifact.
- `03-release.yml` bygger EPUB/PDF som release-assets vid `v*`-taggar.
- EPUB-bygget använder Pandoc och efterbearbetning via `publishing/fix-epub-after-pandoc.py`.
- PDF-bygget använder Python/ReportLab för stabil layout utan LaTeX- och systemfontberoenden.

## Exportpolicy

- `exports/` är borttagen ur projektet.
- `*.epub` och `*.pdf` ignoreras via `.gitignore`.
- EPUB/PDF är genererade artefakter, inte kanoniska källor.
- Kanoniska källor är kapitelfilerna, projektfilerna, metadata, omslag och byggskript.
- Previewfiler hämtas från GitHub Actions artifact `under-stilla-vatten-preview`.
- Slutliga publiceringsfiler hämtas från GitHub Releases efter taggad release.

## Viktigt inför slutexport

- Kapiteltexterna i `kapitel/kapitel-01.md` till `kapitel/kapitel-24.md` är kanoniska.
- Ändringar i kapitel kräver ny preview-build via GitHub Actions.
- Kontrollera Actions-genererad EPUB i Apple Books eller motsvarande läsare före publicering.
- Kontrollera Actions-genererad PDF visuellt om den ska användas som korrektur eller extraformat.

## Nästa rekommenderade steg

- Checka in den städade projektstrukturen i GitHub.
- Kör **Validate** eller öppna en PR för att verifiera projektet.
- Kör **Build Preview** och kontrollera EPUB/PDF.
- Skapa release med `v*`-tagg när filerna är slutgodkända.


## Publiceringsstruktur 2026-08-16

- `exports/` är fortsatt borttagen.
- EPUB/PDF checkas inte in utan byggs via GitHub Actions.
- Apple/Google-publiceringsstöd har återskapats under `publishing/platforms/`.
- Amazon KDP är utelämnad eftersom den plattformen inte är aktuell.
- Kanoniskt omslag är `publishing/cover.png` och används för både EPUB och PDF.
