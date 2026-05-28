# Apple Books-publiceringschecklista
## Under stilla vatten

Senast uppdaterad: 2026-05-24

## 1. Manus och export

- [x] Romanen har 24 kapitel.
- [x] Ren manusfil finns: `exports/manus_under_stilla_vatten_v2_1_ren.md`.
- [x] Kapitelnoteringar är borttagna från exportunderlaget.
- [x] Skapa EPUB-fil: `exports/Under_stilla_vatten_Erland_Lindmark.epub`.
- [x] Kontrollera EPUB-metadata: titel, författare, språk. Undertitel finns i projektmetadata och butikspaket.
- [x] Synlig innehållsförteckning borttagen ur EPUB-läsordningen; teknisk EPUB-navigering finns kvar.
- [x] Kontrollera att alla kapitel 1–24 finns i rätt ordning.
- [x] Copyrightnotis finns på titelsidan.
- [x] Endast en egen titelsida i EPUB-läsordningen.
- [x] Grundkontrollera att svenska tecken finns i EPUB/XHTML.
- [x] Grundkontrollera att inga råa markdownrubriker syns i EPUB.
- [ ] Validera EPUB med EPUBCheck före Apple Books-uppladdning.

## 2. Omslag

- [x] Omslagsbild finns: `exports/omslag_under_stilla_vatten.png`.
- [x] Omslaget innehåller titel, undertitel och författarnamn.
- [x] Kontrollera omslagets upplösning mot Apple Books-krav.
- [x] Skapa högupplöst omslagsversion om kortaste sidan är för liten.
- [x] Kontrollera att omslaget är RGB och lämpligt för butikspresentation.
- [ ] Kontrollera att texten är läsbar i liten förhandsvisning.

Aktuell omslagsnotering: den ursprungliga omslagsbilden är 1055 × 1491 px. En uppskalad RGB-version för Apple Books har skapats som `exports/omslag_under_stilla_vatten_apple_books.png` (1400 × 1979 px, 300 dpi metadata).

## 3. Metadata

- [x] Titel: Under stilla vatten
- [x] Undertitel: En Kallviksdeckare
- [x] Författare: Erland Lindmark
- [x] Språk: svenska
- [x] Genre: deckare
- [x] Sekundära genrer: thriller, romance
- [ ] ISBN beslutat.
- [ ] Utgivare/förlag beslutat.
- [ ] Publiceringsdatum beslutat.
- [ ] Pris beslutat.
- [ ] Regioner/länder beslutat.
- [ ] Explicit content/åldersmarkering kontrollerad.
- [ ] Upphovsrättstext beslutad.
- [ ] Författarpresentation slutgodkänd.

## 4. Butikstext

- [x] Kort säljtext skapad.
- [x] Standardbeskrivning skapad.
- [x] Kortare beskrivning skapad.
- [ ] Välj slutlig Apple Books-beskrivning.
- [ ] Kontrollera att butikstexten inte avslöjar mördaren.
- [ ] Kontrollera att texten matchar ton och genre.
- [ ] Lägg till eventuell serieinformation om boken ska vara del 1.

## 5. Kategorier och pris

- [x] Kategoriförslag skapade.
- [x] Nyckelordsförslag skapade.
- [x] Prisförslag skapade.
- [ ] Välj slutligt pris.
- [ ] Välj huvudkategori.
- [ ] Välj sekundär kategori.
- [ ] Välj nyckelord utifrån Apple Books-fältens begränsningar.

## 6. Slutkontroll före uppladdning

- [ ] Läs EPUB på Apple Books eller motsvarande läsare.
- [ ] Kontrollera sidbrytningar och kapitelrubriker.
- [ ] Kontrollera omslag i biblioteksvy/miniatyr.
- [ ] Kontrollera innehållsförteckningens länkar.
- [ ] Kontrollera att inga projektfiler, kapitelnoteringar eller arbetsloggar råkat följa med.
- [ ] Kontrollera att bokens beskrivning inte innehåller spoilers.
- [ ] Spara slutlig EPUB och eventuell PDF i `exports/`.
- [ ] Uppdatera `exports/exportlogg.md`.


## Uppdatering 2026-05-28

- EPUB-exporten är justerad för Apple Books-läsning:
  - en titelsida
  - copyrightnotis på titelsidan
  - ingen synlig innehållsförteckning i läsordningen
  - titelsidan inte listad i intern TOC
  - högupplöst omslag ingår
- Kvar före uppladdning:
  - kör full EPUBCheck
  - provläs EPUB i Apple Books
  - kontrollera metadata/pris/länder i Apple Books-publiceringsflödet

- [ ] EPUB-layout kontrollerad i Apple Books/Förhandsvisning efter rubrikmarginaljustering.
