# EPUB-export med Pandoc

**Datum:** 2026-05-31  
**Projekt:** Under stilla vatten  
**Undertitel:** En Kallviksdeckare  
**Författare:** Erland Lindmark  
**Verktyg:** pandoc 3.1.11.1  
**Format:** EPUB 3  
**EPUB-fil:** `exports/Under_stilla_vatten_Erland_Lindmark.epub`  
**Manusunderlag:** `exports/manus_under_stilla_vatten_v2_1_ren.md`  
**Omslag:** `exports/omslag_under_stilla_vatten_apple_books.png`

## Resultat

- EPUB skapad: Ja
- Kapitel inkluderade: 1–24
- Synlig innehållsförteckning i läsordningen: Nej
- EPUB-navigationsfil finns: Ja, som teknisk EPUB-navigering, men den ligger inte i läsordning/spine.
- Pandoc-genererad titelsida: Avstängd med `--epub-title-page=false`
- Egen titelsida i manus: Ja, före kapitel 1
- Copyrightnotis på titelsidan: Ja
- Kapitelnoteringar inkluderade: Nej
- Kapitelnoteringar i källkapitlen: Nej, flyttade till `kapitel/kapitelnoteringar.md`
- Omslagsbild inkluderad: Ja
- Metadata angiven vid Pandoc-export: Ja
- Filstorlek: 3,319,055 byte

## Pandoc-inställningar

- EPUB-format: `epub3`
- Omslag: `--epub-cover-image exports/omslag_under_stilla_vatten_apple_books.png`
- Automatisk Pandoc-titelsida: `--epub-title-page=false`
- Synlig innehållsförteckning: `--toc=false`

## Metadata

- Titel: Under stilla vatten
- Undertitel: En Kallviksdeckare
- Författare: Erland Lindmark
- Språk: sv-SE
- Omslag: högupplöst Apple Books-version

## Kontroll

- EPUB:en har skapats från den rena manusfilen efter att kapitelnoteringarna flyttats till separat fil.
- Sökning i EPUB-innehållet efter `Kapitelnotering` gav ingen träff.
- Kontroll av EPUB-struktur visar att `nav.xhtml` inte ligger i spine/läsordningen.
- `title_page.xhtml` skapades inte.
- Titelsidans copyrightnotis finns i EPUB-innehållet.
- Full EPUBCheck-validering behöver fortfarande göras innan uppladdning till Apple Books.

## Rubrikkontroll

Kapitelrubrikerna har postprocessats i EPUB-XHTML så de visas visuellt två rader: först kapitelnummer, därefter kapiteltitel. EPUB-navfilen behåller navigationslänkarna.

## Kontroll 2026-05-28: justerad EPUB

- EPUB återskapad med Pandoc som EPUB 3.
- `--epub-title-page=false` används för att undvika extra automatisk titelsida.
- Efterbearbetning gjord:
  - titelposten för titelsidan borttagen ur `nav.xhtml`
  - titelposten för titelsidan borttagen ur `toc.ncx`
  - kapitelrubriker konverterade till två visuella rader utan extra `<br />`
  - CSS justerad för mindre avstånd mellan `Kapitel X` och kapiteltitel
- Full EPUBCheck-validering återstår inför Apple Books.

## Senaste CSS-justering 2026-05-28

- Kapitelrubrikernas visuella marginal ovanför rubriken är minskad från `2.5em` till `1.25em`.
- Marginalen efter kapitelrubriken är minskad från `1.8em` till `1.3em`.
- Kapiteltexterna och EPUB-navigationen är oförändrade.

## Senaste CSS-justering 2026-05-28: titelsida

- CSS har uppdaterats så `h2`, stycken och den inre titelsidessektionen centreras explicit.
- Syfte: undertiteln “En Kallviksdeckare” ska inte vänsterjusteras i EPUB-läsare.
- Kapiteltexterna och EPUB-navigationen är oförändrade.

## Efterjustering

- `<itemref idref="nav" />` har tagits bort från `spine` i EPUB-paketet så innehållsförteckningen inte visas som en egen sida i läsflödet.
- `nav.xhtml` ligger kvar i manifestet med `properties="nav"`.


## EPUBCheck-korrigering 2026-05-28

- EPUBCheck rapporterade `ERROR(RSC-011)` i `EPUB/nav.xhtml`: en landmark-länk till `#toc` pekade på `nav.xhtml`, som inte ligger i spine/läsordningen.
- Korrigering: landmark-posten för synlig innehållsförteckning togs bort ur `nav.xhtml`.
- Korrigering: legacy-guide-referensen till `nav.xhtml` togs bort ur `content.opf`.
- Den tekniska `nav.xhtml` finns fortfarande kvar enligt EPUB 3-krav och innehåller länkar till kapitel 1–24.
- Synlig innehållsförteckning ligger fortsatt inte i EPUB:ens läsordning.
- Lokal strukturell kontroll: `nav.xhtml` länkar nu bara kapitelposter till faktiska spine-kapitel; full EPUBCheck behöver köras igen i användarens EPUBCheck-miljö.

## Kontinuitetskorrigering 2026-05-30

EPUB-filen har uppdaterats efter korrigeringen av Karin/Kajsa-spåret:
- Kajsas tidigare felaktiga födelseår är ändrat till 1979.
- Kapitel 19 förtydligar nu att födelseåret inte motsäger kopplingen mellan Karin och Kajsa.
- Sökning i EPUB-innehållet efter `1988` gav ingen träff.

## Kontinuitetsjustering 2026-05-31

- Kapitel 19 uppdaterat: Kajsas/Karins ålder på fotot från 1996 är konsekvent med födelseåret 1979.
- Ren exportfil och EPUB är uppdaterade efter ändringen.

## Kapitel 19-uppdatering 2026-05-31

- Kapitel 19 ersatt med användarens reviderade version.
- Ålderspassagen om fotot är synkad med Kajsa/Karin född 1979.
- Ren exportfil och EPUB återskapade efter ändringen.

## Senaste mindre textjustering

- Kapitel 19: `Det skulle kunna stämma med 1979.` ändrat till `Det skulle kunna stämma med Karin.` i kapitelkälla, ren manusfil och EPUB.
- Kontroll: den äldre frasen förekommer inte längre i EPUB-innehållet.

## Titelsidekontroll

- Titel, undertitel, författare och copyright centreras nu via CSS-regler riktade mot `section#under-stilla-vatten`.
- Kapiteltexterna är oförändrade.
- EPUB:ens tekniska navigation är oförändrad.

## EPUB-navigation korrigerad 2026-05-31

- Synlig innehållsförteckning ligger inte i spine/läsflödet.
- `nav.xhtml` finns kvar som teknisk EPUB 3-navigation.
- `nav.xhtml` innehåller länkar till kapitel 1–24.
- `nav.xhtml` länkar endast till resurser som ligger i spine.
- Legacy-filen `toc.ncx` har uppdaterats med kapitel 1–24.
- Kapiteltexterna är oförändrade.
