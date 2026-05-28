# Projektstatus

## Projekt
- Titel: Under stilla vatten
- Undertitel: En Kallviksdeckare
- Författare: Erland Lindmark
- Omslagsbild: Skapad och sparad i `exports/omslag_under_stilla_vatten.png`

## Nuvarande fas

Exportförberedelse v2.1 är genomförd. Kapitelnoteringar har flyttats från kapitelfilerna till `kapitel/kapitelnoteringar.md`, så `kapitel/kapitel-01.md`–`kapitel/kapitel-24.md` nu är rena romantextfiler. Ren exportfil och EPUB ska/har återskapats efter städningen.


## Senast godkända/reviderade del

- Kapitel 1–24 är språk- och scenputsade v2.1.
- Samtliga kapitel 1–24 är reviderade i version 2.
- Synk- och kontinuitetsstädpaket genomfört 2026-05-24.
- Exportförberedelsepaket skapat 2026-05-24.
- Kapitelövergångar kontrollerade och putsade 2026-05-24.
- Kapitelomfång i projektet: 24 kapitel.
- Kapitelnoteringar flyttade till `kapitel/kapitelnoteringar.md` 2026-05-28; kapitelfilerna är rensade från arbetsnoteringar.
- Mindre textkorrigeringar införda 2026-05-28 i kapitel 2, 6, 15, 20, 21 och 24; exportunderlag och EPUB återskapade.

## Exportförberedelse genomförd

- Ren manusfil skapad: `exports/manus_under_stilla_vatten_v2_1_ren.md`.
- Kapitelnoteringar har tagits bort i exportunderlaget, men källkapitlen i `kapitel/` är oförändrade.
- Exportkontroll skapad: `exports/exportkontroll_v2_1.md`.
- Exportlogg uppdaterad: `exports/exportlogg.md`.
- `exports/README.md` uppdaterad med exportstatus.
- EPUB har återskapats med Pandoc efter textkorrigeringar: `exports/Under_stilla_vatten_Erland_Lindmark.epub`. PDF har ännu inte skapats.

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

- Provläs den återskapade EPUB-filen.
- Kör EPUBCheck innan uppladdning till Apple Books.
- Skapa PDF endast om läsexemplar eller parallell export behövs.

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
