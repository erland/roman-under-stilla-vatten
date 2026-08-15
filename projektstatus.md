# Projektstatus

## Projekt
- Titel: Under stilla vatten
- Undertitel: En Kallviksdeckare
- Författare: Erland Lindmark
- Omslagsbild: Skapad och uppskalad för Apple Books

## Nuvarande fas

Exportförberedelse v2.1 är genomförd. EPUBCheck har enligt användaren gått igenom efter korrigering. Apple Books-, Google Play Books- och Amazon KDP-publiceringspaket finns i `exports/apple_books/`, `exports/google_play_books/` respektive `exports/amazon_kdp/`.

## Senast godkända/reviderade del

- Kapitel 19 justerat 2026-05-31: frasen om att fotot kan stämma med 1979 ändrades till att fotot kan stämma med Karin, eftersom födelseåret ännu inte avslöjas för läsaren.

- Kapitel 19 uppdaterat 2026-05-31 med användarens reviderade version; Kajsa/Karin-spåret är synkat mot födelseår 1979.

- Kapitel 1–24 är språk- och scenputsade v2.1.
- Samtliga kapitel 1–24 är reviderade i version 2.
- Synk- och kontinuitetsstädpaket genomfört 2026-05-24.
- Exportförberedelsepaket skapat 2026-05-24.
- Kapitelövergångar kontrollerade och putsade 2026-05-24.
- Kapitelomfång i projektet: 24 kapitel.
- Kapitelnoteringar flyttade till `kapitel/kapitelnoteringar.md` 2026-05-28; kapitelfilerna är rensade från arbetsnoteringar.
- Mindre textkorrigeringar införda 2026-05-28 i kapitel 2, 6, 15, 20, 21 och 24; exportunderlag och EPUB återskapade.
- EPUB-export justerad 2026-05-28: en egen titelsida med copyright, ingen synlig innehållsförteckning och ingen extra Pandoc-titelsida.

- Amazon KDP-publiceringspaket skapat 2026-05-28 med metadata, beskrivningar, kategori-/prisförslag, 7 nyckelord, checklista, filrekommendationer och KDP-anpassad JPEG-omslagsbild.

## Exportförberedelse genomförd

- EPUBCheck-fel RSC-011 i `nav.xhtml` korrigerat 2026-05-28; ny EPUB bör valideras igen i EPUBCheck.
- EPUB-layout justerad 2026-05-28: kapitelrubrikernas marginaler minskade för tätare rubriksättning.

- Ren manusfil skapad: `exports/manus_under_stilla_vatten_v2_1_ren.md`.
- Kapitelnoteringar har tagits bort i exportunderlaget, men källkapitlen i `kapitel/` är oförändrade.
- Exportkontroll skapad: `exports/exportkontroll_v2_1.md`.
- Exportlogg uppdaterad: `exports/exportlogg.md`.
- `exports/README.md` uppdaterad med exportstatus.
- EPUB har återskapats med Pandoc efter textkorrigeringar och exportjusteringar: `exports/Under_stilla_vatten_Erland_Lindmark.epub`. Den har en enda egen titelsida med copyrightnotis, ingen synlig innehållsförteckning i läsordningen och ingen extra Pandoc-genererad titelsida. PDF har ännu inte skapats.

## Omslagsbild

- Omslagsbild skapad: `exports/omslag_under_stilla_vatten.png`.
- Högupplöst Apple Books-version skapad: `exports/omslag_under_stilla_vatten_apple_books.png`.
- Innehåller titel, undertitel och författarnamn:
  - Titel: Under stilla vatten
  - Undertitel: En Kallviksdeckare
  - Författare: Erland Lindmark

## Viktigt inför slutexport

- Kapiteltexterna i `kapitel/kapitel-01.md` till `kapitel/kapitel-24.md` är fortfarande kanoniska källor.
- Exportunderlaget i `exports/` har återskapats efter den senaste kapitelövergångsputsen och ska återskapas igen om någon kapiteltext ändras.
- Omslagsbild/framsida är skapad och sparad som `exports/omslag_under_stilla_vatten.png`.

## Nästa rekommenderade steg

- Provläs slutlig EPUB i Apple Books och Google Play Books.
- Ladda upp EPUB och separat omslagsbild i vald publiceringsplattform.
- Bestäm ISBN, pris, regioner och publiceringsdatum.
- Skapa PDF endast om den behövs som extraformat eller korrekturfil.

## Apple Books

- Apple Books-publiceringspaket finns i `exports/apple_books/`.
- Högupplöst omslagsbild för Apple Books/butikspresentation finns i `exports/omslag_under_stilla_vatten_apple_books.png` (1400 × 1979 px, RGB, 300 dpi metadata).
- Omslaget är uppskalat från den befintliga omslagsbilden; ingen ny bild/design har genererats.
- EPUB behöver fortfarande skapas och valideras.

-publiceringspaket

Skapat 2026-05-24 i `exports/apple_books/`.

Innehåll:

- `metadata_apple_books.md`
- `beskrivningar_apple_books.md`
- `kategori_prisforslag.md`
- `publiceringschecklista.md`

## Nästa rekommenderade steg för Apple Books

- Välj slutlig butikstext.
- Välj pris och publiceringsregioner.
- Besluta om ISBN och utgivarnamn.
- Skapa eller skala upp omslaget till Apple Books-lämplig upplösning.
- Skapa EPUB och validera den före uppladdning.

## Risker att bevaka vid export

- Kapitelnoteringar ska inte följa med i färdig PDF/EPUB.
- Rå markdown ska normaliseras vid PDF/EPUB-export.
- Kapitelordning ska vara 1–24.
- Titel, undertitel och författare ska finnas i exporten.
- Omslag ska bara skapas/exporteras om titel, undertitel och författarnamn är fastställda.

## Senaste exportkontroll

- Datum: 2026-05-24
- Ren exportfil kontrollerad: `exports/manus_under_stilla_vatten_v2_1_ren.md`
- Kapitelnoteringar och arbetsmarkörer: inga hittade i exportmanuset.
- Originalkapitel: oförändrade.


## EPUB-export

- EPUB skapad: `exports/Under_stilla_vatten_Erland_Lindmark.epub`
- Skapad med: Pandoc 3.1.11.1
- Kapitel: 1–24
- Omslag: `exports/omslag_under_stilla_vatten_apple_books.png`
- Full EPUBCheck-validering kvarstår inför Apple Books-publicering.

## Senaste exportjustering

EPUB-exporten har uppdaterats med copyrighttexten “Alla rättigheter reserverade” och kapitelrubriker som visas på två rader i bokens läsning. Kapiteltexterna är oförändrade.


## Exportjustering 2026-05-28

EPUB-exporten har justerats efter läsarkontroll:
- endast en titelsida i läsordningen
- copyrightnotis på titelsidan
- ingen synlig innehållsförteckning i läsordningen
- titelsidan är inte längre listad i EPUB:ens interna TOC
- kapitelrubriker visas på två rader med mindre avstånd
- kapiteltexterna är oförändrade

Nästa rekommenderade steg: granska den nya EPUB:en i Apple Books eller annan EPUB-läsare och därefter köra EPUBCheck inför publicering.

## Exportjustering 2026-05-28: titelsidans undertitel

EPUB-exportens CSS har uppdaterats så undertiteln på titelsidan centreras explicit. Kapiteltexterna är oförändrade.

Nästa rekommenderade steg: granska den nya EPUB:en i Apple Books eller annan EPUB-läsare och därefter köra EPUBCheck inför publicering.

## Senaste exportjustering

EPUB: Synlig innehållsförteckning är borttagen ur läsflödet. Teknisk navigationsfil finns kvar. Kapiteltexterna är oförändrade.


## Amazon KDP

- KDP-paket: `exports/amazon_kdp/`.
- Rekommenderad EPUB: `exports/Under_stilla_vatten_Erland_Lindmark.epub`.
- Rekommenderat KDP-omslag: `exports/omslag_under_stilla_vatten_kdp.jpg`.
- Nästa steg för KDP: kontrollera EPUB i Kindle Previewer före uppladdning.

## Uppdatering 2026-05-30

Karin/Kajsa-spåret är kontinuitetskorrigerat: Kajsas födelseår är ändrat till 1979, kapitel 19:s resonemang är justerat, och ren manusfil samt EPUB är synkade efter ändringen. Inga övriga kapitelintriger har ändrats.

## Senaste kontinuitetsjustering

- 2026-05-31: Kapitel 19 har justerats så Kajsa/Karin-spåret är konsekvent: fotot från 1996 beskriver K. som tonåring, inte som ett barn på sju–åtta år. Exportmanus och EPUB är uppdaterade.

## Senaste exportjustering

EPUB-titelsidan har justerats så titel, undertitel, författare och copyright är centrerade. Kapiteltexter oförändrade.

## Senaste exportjustering 2026-05-31

EPUB-navigationen är korrigerad: ingen synlig innehållsförteckning i läsflödet, men teknisk navigation till kapitel 1–24 finns kvar.

## GitHub Actions

GitHub Actions-publicering införd 2026-08-15:

- `.github/workflows/01-validate.yml` validerar projektstruktur och kapitel.
- `.github/workflows/02-build-preview.yml` bygger EPUB/PDF manuellt och laddar upp ett preview-artifact.
- `.github/workflows/03-release.yml` bygger EPUB/PDF vid `v*`-taggar och laddar upp dem som GitHub Release-assets.
- Bygglogik finns i `scripts/build_book.py` och `scripts/validate_project.py`.
- Publiceringsmetadata och EPUB/PDF-stilar finns i `publishing/`.

## Senaste GitHub Actions-fix 2026-08-15

Preview-bygget korrigerades efter PDF-fel där XeLaTeX inte hittade fonten `TeXGyrePagella`.

Ändringar:
- PDF-bygget använder nu `pdflatex` i stället för `xelatex`.
- `publishing/pdf-template.tex` använder `inputenc`, `fontenc` och `lmodern` i stället för `fontspec`.
- PDF-omslaget hämtas från metadatafältet `cover-image`.
- Pandoc-hjälpkommandot `\tightlist` finns i PDF-mallen.
- Preview- och release-workflows installerar nu `texlive-latex-extra`, `texlive-fonts-recommended` och `lmodern`.
- Lokal testbuild av `python3 scripts/build_book.py --output-dir /mnt/data/test_github_fix_dist3` gav både EPUB och PDF.


## Senaste GitHub Actions PDF-layoutfix 2026-08-15

PDF-bygget i `scripts/build_book.py` är ändrat från Pandoc/LaTeX till Python/ReportLab.

Åtgärdat:
- borttagna extra tomma sidor före omslag och innehållsförteckning
- ifylld innehållsförteckning med kapitel 1–24
- endast en titelsida efter omslaget
- copyright på titelsidan
- borttagna automatiska `0.x`-kapitelnummer
- tvådelade kapitelrubriker i PDF: `Kapitel X` på första raden och kapitelnamn på andra raden
- EPUB-bygget lämnat oförändrat, med teknisk navigation men utan synlig TOC i läsflödet
