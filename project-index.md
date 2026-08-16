# Project Index

## Projekt

- Titel: Under stilla vatten
- Undertitel: En Kallviksdeckare
- Författare: Erland Lindmark
- Senast uppdaterad: 2026-08-16
- Nuvarande fas: GitHub Actions-baserad bygg- och publiceringsstruktur
- Senast godkända/reviderade kapitel: Kapitel 19 frasjusterat 2026-05-31; kapitel 1–24 språk- och scenputsade v2.1
- Nästa kapitel: Inget planerat; nästa steg är slutlig provläsning av Actions-genererad EPUB/PDF och eventuell release via tagg
- Omslagsbild: Skapad och flyttad till `publishing/cover.png` som kanonisk byggkälla

## Kapitelinventering

| Kapitel | Fil | Titel | Status |
|---|---|---|---|
| 1 | kapitel/kapitel-01.md | Kroppen vid kallbadhuset | Språk- och scenputsad v2.1 |
| 2 | kapitel/kapitel-02.md | Nora stänger dörren | Språk- och scenputsad v2.1; mindre korrigering 2026-05-28 |
| 3 | kapitel/kapitel-03.md | Änkan vid panoramafönstret | Språk- och scenputsad v2.1 |
| 4 | kapitel/kapitel-04.md | Mannen med kameran | Språk- och scenputsad v2.1 |
| 5 | kapitel/kapitel-05.md | Det saknade kuvertet | Språk- och scenputsad v2.1 |
| 6 | kapitel/kapitel-06.md | Första lögnen faller | Språk- och scenputsad v2.1; mindre korrigering 2026-05-28 |
| 7 | kapitel/kapitel-07.md | Viktor Sahls kontor | Språk- och scenputsad v2.1 |
| 8 | kapitel/kapitel-08.md | Artikeln Adam inte publicerade | Språk- och scenputsad v2.1 |
| 9 | kapitel/kapitel-09.md | Flickan på busshållplatsen | Språk- och scenputsad v2.1 |
| 10 | kapitel/kapitel-10.md | Den hjälpsamma samordnaren | Språk- och scenputsad v2.1; övergångsputsad |
| 11 | kapitel/kapitel-11.md | Gamla journaler, nya sår | Språk- och scenputsad v2.1 |
| 12 | kapitel/kapitel-12.md | En kväll på redaktionen | Språk- och scenputsad v2.1 |
| 13 | kapitel/kapitel-13.md | Fel man i rätt ljus | Språk- och scenputsad v2.1 |
| 14 | kapitel/kapitel-14.md | När havet slår mot rutorna | Språk- och scenputsad v2.1; övergångsputsad |
| 15 | kapitel/kapitel-15.md | Hotet mot Adam | Språk- och scenputsad v2.1; mindre korrigering 2026-05-28 |
| 16 | kapitel/kapitel-16.md | Tidslinjen som inte håller | Språk- och scenputsad v2.1 |
| 17 | kapitel/kapitel-17.md | Karin kokar kaffe | Språk- och scenputsad v2.1 |
| 18 | kapitel/kapitel-18.md | Nora försvinner i två timmar | Språk- och scenputsad v2.1 |
| 19 | kapitel/kapitel-19.md | Det andra offret som aldrig dog | Språk- och scenputsad v2.1; Kajsa/Karin-spår och fras justerade 2026-05-31 |
| 20 | kapitel/kapitel-20.md | Alla ljuger av olika skäl | Språk- och scenputsad v2.1; mindre korrigering 2026-05-28 |
| 21 | kapitel/kapitel-21.md | Den felvända detaljen | Språk- och scenputsad v2.1; mindre korrigering 2026-05-28 |
| 22 | kapitel/kapitel-22.md | Kallvik håller andan | Språk- och scenputsad v2.1 |
| 23 | kapitel/kapitel-23.md | Under stilla vatten | Språk- och scenputsad v2.1 |
| 24 | kapitel/kapitel-24.md | Morgon över Kallvik | Språk- och scenputsad v2.1; mindre korrigering 2026-05-28 |

## Kanoniska projektfiler

| Fil | Syfte | Status |
|---|---|---|
| README.md | Start, arbetsflöde och GitHub Actions-instruktioner | OK |
| roman-bibel.md | Centrala fakta | OK |
| synopsis.md | Handlingsöversikt | OK |
| kapitelplan.md | Kapitelplan och status | Synkad |
| stilguide.md | Språk, ton och perspektiv | OK |
| tidslinje.md | Händelser i romanen och mordkvällstabell | Synkad |
| kontinuitetsanteckningar.md | Fakta, ledtrådar och beviskedja | Synkad |
| revisionsonskemal.md | Kvarvarande revisionsarbete | Synkad |
| arbetslogg.md | Projektändringar | Synkad |
| projektstatus.md | Senaste status och nästa steg | Synkad |
| karaktarer/huvudperson.md | Huvudperson | OK |
| karaktarer/antagonist.md | Antagonist/Karin-spår | OK |
| karaktarer/bifigurer.md | Bifigurer | OK |
| kapitel/kapitelmall.md | Kapitelmall | OK |
| kapitel/kapitelnoteringar.md | Samlade kapitelnoteringar, exporteras inte | OK |
| publishing/metadata.yaml | Metadata för EPUB/PDF | OK |
| publishing/epub.css | EPUB-stil för Actions-bygget | OK |
| publishing/fix-epub-after-pandoc.py | Efterbearbetning av EPUB-navigation, titelsida och rubriker | OK |
| publishing/cover.png | Kanonisk omslagsbild för EPUB/PDF-byggen | OK |
| publishing/build-notes.md | Dokumentation för GitHub Actions-publicering | OK |
| scripts/validate_project.py | Projekt- och manusvalidering | OK |
| scripts/build_book.py | Bygger EPUB/PDF från kanoniska kapitel | OK |
| .github/workflows/01-validate.yml | Validering vid PR/push | OK |
| .github/workflows/02-build-preview.yml | Manuell preview-build av EPUB/PDF | OK |
| .github/workflows/03-release.yml | Release-build vid `v*`-taggar | OK |
| .gitignore | Ignorerar genererade EPUB/PDF- och exportmappar | OK |

## Synkkontroll

- Kapitel i `kapitel/`: 24 roman-kapitel + kapitelmall + samlad kapitelnoteringsfil
- Senaste kapitel i `kapitelplan.md`: Kapitel 24 – Morgon över Kallvik
- Senaste kapitel i `projektstatus.md`: Kapitel 1–24 språk- och scenputsade v2.1; kapitel 19 frasjusterat
- Senaste ändring i `arbetslogg.md`: Repository cleanup 2026-08-16
- Exporter i repositoryt: Inga incheckade EPUB/PDF-filer
- Generering: EPUB/PDF skapas av GitHub Actions som preview-artifact eller release-assets
- Resultat: Synkad; `exports/` är borttagen och genererade filer ignoreras.

## GitHub Actions och byggfiler

- `.github/workflows/01-validate.yml` – Validerar projektet vid PR/push till main.
- `.github/workflows/02-build-preview.yml` – Manuell preview-build av EPUB/PDF.
- `.github/workflows/03-release.yml` – Release-build vid `v*`-taggar.
- `scripts/validate_project.py` – Projekt- och manusvalidering.
- `scripts/build_book.py` – Bygger EPUB/PDF från kanoniska kapitel.
- `publishing/metadata.yaml` – Metadata för EPUB/PDF.
- `publishing/epub.css` – EPUB-stil.
- `publishing/fix-epub-after-pandoc.py` – Efterbearbetar EPUB-navigation, titelsida och rubriker.
- `publishing/cover.png` – Omslagsbild för Actions-byggen.

## Exportpolicy

- EPUB och PDF är genererade artefakter, inte kanoniska källfiler.
- `exports/` ska inte checkas in.
- Lokalt skapade `*.epub` och `*.pdf` ignoreras via `.gitignore`.
- Previewfiler hämtas från GitHub Actions artifact `under-stilla-vatten-preview`.
- Slutliga filer hämtas från GitHub Releases när en `v*`-tagg har pushats.


## Publiceringsstöd

| Plattform | Katalog | Status |
|---|---|---|
| Apple Books | `publishing/platforms/apple_books/` | Återskapad 2026-08-16 |
| Google Play Books | `publishing/platforms/google_play_books/` | Återskapad 2026-08-16 |
| Amazon KDP | - | Utelämnad enligt beslut |

## Genererade filer

EPUB/PDF ska inte checkas in. De byggs av GitHub Actions som artifacts eller release assets.
