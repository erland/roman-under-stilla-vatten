# Apple Books-publiceringschecklista
## Under stilla vatten

Senast uppdaterad: 2026-08-16

## 1. Manus och build

- [x] Romanen har 24 kapitel.
- [x] Kapitelnoteringar ligger separat och följer inte med i EPUB/PDF.
- [x] EPUB byggs av GitHub Actions som `under-stilla-vatten.epub`.
- [x] PDF byggs av GitHub Actions som `under-stilla-vatten.pdf`.
- [x] Synlig innehållsförteckning är borttagen ur EPUB-läsordningen.
- [x] Teknisk EPUB-navigation finns kvar.
- [x] Kontroll i byggskriptet säkerställer att EPUB-navigationen innehåller kapitel 1–24.
- [x] Titelsidan innehåller titel, undertitel, författare och copyright.
- [x] Kapitelrubriker delas på två rader i EPUB/PDF.
- [ ] Validera slutlig EPUB med EPUBCheck före Apple Books-uppladdning.
- [ ] Läs slutlig EPUB i Apple Books eller motsvarande läsare.

## 2. Omslag

- [x] Kanonisk omslagsbild finns: `publishing/cover.png`.
- [x] Omslaget innehåller titel, undertitel och författarnamn.
- [x] Omslaget är RGB.
- [x] Omslaget är 1400 × 1979 px.
- [x] Samma omslag bäddas in i EPUB och används i PDF.
- [ ] Kontrollera att omslagstexten är läsbar i liten förhandsvisning.

## 3. Metadata

- [x] Titel: Under stilla vatten
- [x] Undertitel: En Kallviksdeckare
- [x] Författare: Erland Lindmark
- [x] Språk: svenska
- [x] Genre: deckare
- [x] Sekundära genrer: thriller, romance
- [ ] ISBN beslutat.
- [ ] Publiceringsdatum beslutat.
- [ ] Pris beslutat.
- [ ] Regioner/länder beslutat.
- [ ] Explicit content/åldersmarkering slutkontrollerad.
- [ ] Författarpresentation slutgodkänd.

## 4. Butikstext

- [x] Kort säljtext skapad.
- [x] Standardbeskrivning skapad.
- [x] Kortare beskrivning skapad.
- [ ] Välj slutlig Apple Books-beskrivning.
- [ ] Kontrollera att butikstexten inte avslöjar mördaren.
- [ ] Kontrollera att texten matchar ton och genre.
- [ ] Lägg till eventuell serieinformation om boken ska vara del 1.

## 5. Slutkontroll före uppladdning

- [ ] Kör GitHub Actions-preview och ladda ned artifact.
- [ ] Kontrollera EPUB-navigation i läsare.
- [ ] Kontrollera att ingen synlig innehållsförteckningssida ligger i EPUB-läsflödet.
- [ ] Kontrollera att alla kapitel 1–24 finns i rätt ordning.
- [ ] Kontrollera att inga projektfiler, kapitelnoteringar eller arbetsloggar råkat följa med.
- [ ] Spara publiceringsdatum och slutligt versionsnummer i `arbetslogg.md`.
