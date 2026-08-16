# Publiceringschecklista för Google Play Books
## Under stilla vatten

Senast uppdaterad: 2026-08-16

## Före uppladdning

- [ ] Kör GitHub Actions-preview och ladda ned `under-stilla-vatten-preview`.
- [ ] Kontrollera att artifact innehåller `under-stilla-vatten.epub` och `under-stilla-vatten.pdf`.
- [ ] Kontrollera att EPUBCheck går igenom.
- [ ] Kontrollera EPUB i Google Play Books/annan EPUB-läsare:
  - [ ] Omslag visas korrekt.
  - [ ] Titelsidan visas en gång.
  - [ ] Copyrightnotis visas korrekt.
  - [ ] Ingen synlig innehållsförteckning ligger som egen sida i läsflödet.
  - [ ] Teknisk navigation visar kapitel 1–24.
  - [ ] Kapitelrubriker visas på två rader med bra marginal.
  - [ ] Svenska tecken visas korrekt.
- [ ] Kontrollera PDF:
  - [ ] Omslag visas först.
  - [ ] Titelsida och copyright visas korrekt.
  - [ ] Innehållsförteckning är ifylld.
  - [ ] PDF-bokmärken finns för kapitel 1–24.
  - [ ] Kapitelrubriker visas på två rader.
- [ ] Bestäm ISBN eller alternativ identifierare.
- [ ] Bestäm pris.
- [ ] Bestäm säljregioner.
- [ ] Bestäm publiceringsdatum.

## Metadata i Partner Center

- [ ] Titel: Under stilla vatten
- [ ] Undertitel: En Kallviksdeckare
- [ ] Författare: Erland Lindmark
- [ ] Språk: Svenska
- [ ] Utgivare: Erland Lindmark, om inget annat beslutas.
- [ ] Kategori: Deckare/kriminalroman/polisroman.
- [ ] Beskrivning: Använd lång beskrivning i `beskrivningar_google_play_books.md`.
- [ ] Explicit innehåll: Nej, om ingen senare bedömning ändrar detta.
- [ ] Serie: Kallviksdeckare, bok 1, om serien ska marknadsföras så.

## Efter uppladdning

- [ ] Förhandsgranska boken i Google Play Books.
- [ ] Kontrollera att omslagsbilden används korrekt i butiksvyn.
- [ ] Kontrollera provläsningen/sample.
- [ ] Kontrollera pris och regioner.
- [ ] Kontrollera att rätt EPUB/PDF-version är aktiv.
- [ ] Spara uppladdningsdatum och versionsnotering i `arbetslogg.md`.
