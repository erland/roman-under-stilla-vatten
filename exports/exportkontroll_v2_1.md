# Exportförberedelsekontroll v2.1

**Datum:** 2026-05-30
**Projekt:** Under stilla vatten  
**Undertitel:** En Kallviksdeckare  
**Författare:** Erland Lindmark  
**Exportunderlag:** `exports/manus_under_stilla_vatten_v2_1_ren.md`

## Sammanfattning

- Kapitel inkluderade: 1–24.
- Antal saknade kapitelnummer: 0.
- Kapitelnoteringar: borttagna ur exportunderlaget och flyttade från kapitelfilerna till `kapitel/kapitelnoteringar.md`.
- Exportunderlaget har återskapats efter användarens mindre textjusteringar och rekommenderade korrigeringar i kapitel 2, 6, 15, 20, 21 och 24.
- EPUB har återskapats med Pandoc: `exports/Under_stilla_vatten_Erland_Lindmark.epub`.
- EPUB-exporten har en enda egen titelsida med copyrightnotis.
- Pandocs automatiska titelsida är avstängd.
- Synlig innehållsförteckning i EPUB-läsordningen är borttagen; teknisk navigationsfil finns kvar enligt EPUB-formatet.
- Omslag inkluderat i EPUB: `exports/omslag_under_stilla_vatten_apple_books.png`.
- PDF: ännu inte skapad.
- EPUBCheck-fel `RSC-011` i `nav.xhtml` har korrigerats genom att ta bort landmark-/guide-referens till den icke-spine-lagda navigationssidan; teknisk EPUB-navigation finns kvar.

## Ordstatistik

- Ungefärligt antal ord i ren manusfil: 92 114 ord.
- Antal tecken i ren manusfil: 549 017 tecken.

## Kapitelinventering i exportunderlag

| Kapitel | Titel | Ca ord |
|---|---|---|
| 1 | Kroppen vid kallbadhuset | 2 453 |
| 2 | Nora stänger dörren | 3 430 |
| 3 | Änkan vid panoramafönstret | 3 080 |
| 4 | Mannen med kameran | 2 984 |
| 5 | Det saknade kuvertet | 3 900 |
| 6 | Första lögnen faller | 4 184 |
| 7 | Viktor Sahls kontor | 3 491 |
| 8 | Artikeln Adam inte publicerade | 3 947 |
| 9 | Flickan på busshållplatsen | 6 042 |
| 10 | Den hjälpsamma samordnaren | 3 619 |
| 11 | Gamla journaler  nya sår | 3 309 |
| 12 | En kväll på redaktionen | 4 030 |
| 13 | Fel man i rätt ljus | 4 717 |
| 14 | När havet slår mot rutorna | 3 441 |
| 15 | Hotet mot Adam | 3 382 |
| 16 | Tidslinjen som inte håller | 3 391 |
| 17 | Karin kokar kaffe | 3 438 |
| 18 | Nora försvinner i två timmar | 4 836 |
| 19 | Det andra offret som aldrig dog | 4 644 |
| 20 | Alla ljuger av olika skäl | 5 223 |
| 21 | Den felvända detaljen | 2 567 |
| 22 | Kallvik håller andan | 2 752 |
| 23 | Under stilla vatten | 3 210 |
| 24 | Morgon över Kallvik | 5 874 |

## Kontroller

- Titel finns: Ja.
- Undertitel finns: Ja.
- Författare finns: Ja.
- Kapitel 1–24 finns i korrekt ordning: Ja.
- Kapitelnoteringar finns i exportunderlaget: Nej.
- Kända arbetsmarkörer finns i exportunderlaget: Nej.
- Råa markdownrubriker finns kvar i Markdown-underlaget, men dessa är avsiktliga och används av Pandoc för EPUB-struktur.
- Omslagsbild för Apple Books finns: Ja.
- Copyrightnotis på titelsidan: Ja.
- Synlig innehållsförteckning i EPUB-läsordningen: Nej.
- EPUB skapad med Pandoc: Ja.
- Full EPUBCheck-validering: Ej gjord i denna miljö; behöver göras före Apple Books-uppladdning.

## Kommentar

Detta är en exportkontroll efter mindre textkorrigeringar. Kapiteltexterna och den rena exportfilen är synkade. EPUB-filen är återskapad, men bör fortfarande valideras med EPUBCheck innan publicering.

## Senaste EPUB-justering

- Copyrighttext: Copyright © 2026 Erland Lindmark. Alla rättigheter reserverade.
- Kapitelrubriker i EPUB visas visuellt på två rader, medan EPUB-nav behåller stabila länkar.
- Ingen synlig innehållsförteckning ligger i läsordningen; `nav.xhtml` finns kvar som teknisk EPUB-navigation.

## EPUB-justering 2026-05-28: titelsida och rubrikavstånd

- Enbart en titelsida används i EPUB-läsordningen.
- Pandocs automatiska titelsida är avstängd med `--epub-title-page=false`.
- Den kvarvarande titelsidan innehåller titel, undertitel, författare och copyrightnotis.
- Titelsidan är borttagen från EPUB:ens interna navigationslista/TOC.
- Synlig innehållsförteckning ligger inte i läsordningen.
- Kapitelrubriker visas på två rader med minskat avstånd mellan kapitelnummer och kapiteltitel.
- Kapiteltexterna är oförändrade.

## EPUB-layoutjustering 2026-05-28

- Kapitelrubriker visas fortsatt på två rader.
- Utrymmet ovanför kapitelrubrikerna har minskats.
- Utrymmet efter kapiteltiteln har minskats något.
- Titelsida, kapiteltexter och EPUB-navigation är oförändrade.

## EPUB-layoutjustering 2026-05-28: titelsidans undertitel

- Undertiteln på titelsidan centreras explicit via CSS.
- Titel, undertitel, författare och copyright ligger fortsatt på en enda titelsida.
- Synlig innehållsförteckning ligger fortsatt inte i läsordningen.
- Kapiteltexterna är oförändrade.

## Justering 2026-05-28 – synlig innehållsförteckning

- Synlig innehållsförteckning är borttagen ur EPUB-läsordningen.
- `nav.xhtml` finns kvar som teknisk navigationsfil enligt EPUB 3.
- Kapiteltexterna är oförändrade.


## Amazon KDP-publiceringspaket

- KDP-paket skapat: `exports/amazon_kdp/`
- KDP-omslag skapat: `exports/omslag_under_stilla_vatten_kdp.jpg`
- EPUB oförändrad i detta steg: `exports/Under_stilla_vatten_Erland_Lindmark.epub`
- Kapiteltexter oförändrade.
- Rekommenderad extern kontroll: öppna EPUB i Kindle Previewer före uppladdning.

## Kontinuitetskorrigering 2026-05-30

- Kajsas tidigare felaktiga födelseår har ändrats till 1979 i kapitel 19 och relevanta projektfiler, så det stämmer med att Karin Holm/Karin Kajsa Andersson senare kan konstateras vara samma person.
- Resonemanget i kapitel 19 har skrivits om så Helena ser en möjlig identitet utan att bekräfta den för tidigt.
- Formuleringen kring fotot från 1996 har justerats från barn/flicka till tonåring/tonårsflicka där åldern annars kunde bli missvisande.
- EPUB och ren manusfil är återskapade/synkade efter korrigeringen.

## Kontinuitetsjustering 2026-05-31

- Kapitel 19 uppdaterat: Kajsas/Karins ålder på fotot från 1996 är konsekvent med födelseåret 1979.
- Ren exportfil och EPUB är uppdaterade efter ändringen.

## Kapitel 19-uppdatering 2026-05-31

- Kapitel 19 ersatt med användarens reviderade version.
- Ålderspassagen om fotot är synkad med Kajsa/Karin född 1979.
- Ren exportfil och EPUB återskapade efter ändringen.

## Kapitel 19 frasjusterad 2026-05-31

- Frasen `Det skulle kunna stämma med 1979.` är ändrad till `Det skulle kunna stämma med Karin.` i kapitel 19, ren exportfil och EPUB.
- Syfte: undvika att läsaren får Karins födelseår innan det är etablerat.

## Titelsida

- Titelsidan har kontrollerats och CSS har uppdaterats så titel, undertitel, författare och copyright centreras.
- Ingen synlig innehållsförteckning har lagts tillbaka i läsflödet.

## Kontroll efter nav-fix 2026-05-31

- Titelsidan är fortsatt centrerad.
- Innehållsförteckningen är inte synlig som egen sida i läsordningen.
- EPUB-navigationen innehåller kapitel 1–24 för läsarens navigationsmeny.
- EPUBCheck-felet om referens till icke-spine-resurs bör inte återkomma.
