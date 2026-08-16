# Exporter

Denna katalog innehåller exportunderlag och metadata för *Under stilla vatten*.

Exporter är inte romanens kanoniska källtext. De kan återskapas från `kapitel/kapitel-XX.md`.

## Projekt

- Titel: Under stilla vatten
- Undertitel: En Kallviksdeckare
- Författare: Erland Lindmark

## Exportunderlag

| Fil | Syfte | Status |
|---|---|---|
| `manus_under_stilla_vatten_v2_1_ren.md` | Ren manusfil för framtida PDF/EPUB-export, utan kapitelnoteringar. | Skapad 2026-05-24 |
| `exportkontroll_v2_1.md` | Kontrollrapport inför export. | Skapad 2026-05-24 |
| `exportlogg.md` | Logg över exporter och exportunderlag. | Uppdaterad 2026-05-24 |
| `omslag_under_stilla_vatten.png` | Omslagsbild/framsida med titel, undertitel och författarnamn. | Skapad och sparad 2026-05-24 |
| `omslag_under_stilla_vatten_apple_books.png` | Högupplöst RGB-version av befintligt omslag för Apple Books/butikspresentation. Kortaste sidan: 1400 px. | Skapad 2026-05-24 |
| `Under_stilla_vatten_Erland_Lindmark.epub` | EPUB 3 skapad med Pandoc från ren manusfil och högupplöst omslag. | Skapad 2026-05-24 |
- Senaste EPUB-versionen har ingen synlig innehållsförteckning i läsflödet; teknisk EPUB-navigation finns kvar.
| `epub_pandoc_kontroll.md` | Grundläggande kontrollrapport för Pandoc-EPUB. | Skapad 2026-05-24 |

| `apple_books/README.md` | Apple Books-publiceringspaket med metadata, butikstexter, kategori-/prisförslag och checklista. | Skapat 2026-05-24 |

## Viktigt

Kapitelfilerna i `kapitel/` är fortsatt kanoniska källor. Den rena manusfilen i `exports/` är ett exportunderlag och ska återskapas om kapiteltexterna ändras.

## Senaste exportstatus 2026-05-28

Ren manusfil och EPUB har återskapats efter mindre textkorrigeringar i kapitel 2, 6, 15, 20, 21 och 24. Full EPUBCheck-validering återstår före Apple Books-uppladdning.


## Kapitelnoteringar

Kapitelnoteringar har flyttats till `kapitel/kapitelnoteringar.md` 2026-05-28. Kapitelfilerna innehåller nu endast romantext och kan användas säkrare som källa för framtida EPUB/PDF-exporter.


## Senaste EPUB-justering 2026-05-28

EPUB-filen `Under_stilla_vatten_Erland_Lindmark.epub` har återskapats med Pandoc efter följande exportjusteringar:

- endast en egen titelsida i läsordningen
- copyrightnotis tillagd på titelsidan
- Pandocs automatiska titelsida avstängd
- synlig innehållsförteckning borttagen ur läsordningen
- teknisk EPUB-navigering (`nav.xhtml`) finns kvar eftersom den hör till EPUB-formatet
- full EPUBCheck-validering återstår före Apple Books-uppladdning


## EPUB-justering: en titelsida

Senaste EPUB-exporten använder en enda titelsida med copyrightnotis. Den synliga innehållsförteckningen är borttagen från läsordningen, men EPUB:ens tekniska navigationsfiler finns kvar. Kapitelrubriker visas på två rader med reducerat avstånd.

## EPUB-layoutjustering 2026-05-28

Kapitelrubrikerna visas fortsatt på två rader, men marginalen ovanför rubriken och marginalen efter kapiteltiteln har minskats för ett tätare och mer balanserat intryck i EPUB-läsare.

## EPUB-layoutjustering 2026-05-28: titelsida

Titelsidans undertitel centreras nu explicit i EPUB-CSS. Kapiteltexterna är oförändrade.

## EPUBCheck-korrigering 2026-05-28

EPUBCheck-fel `RSC-011` i `nav.xhtml` är korrigerat. Den synliga innehållsförteckningen ligger fortfarande inte i läsflödet, men den tekniska EPUB-navigationen finns kvar.


## Google Play Books-publiceringspaket

Google Play Books-paketet finns i `exports/google_play_books/` och innehåller metadata, butikstexter, kategori-/prisförslag, publiceringschecklista och filrekommendationer.

Rekommenderade uppladdningsfiler:
- `exports/Under_stilla_vatten_Erland_Lindmark.epub`
- `exports/omslag_under_stilla_vatten_google_play.png`


| `omslag_under_stilla_vatten_kdp.jpg` | KDP-anpassad omslagsbild för Kindle eBook. JPEG, 1600 × 2560 px, RGB, 300 dpi. | Skapad 2026-05-28 |

## Amazon KDP-publiceringspaket

| Fil | Syfte | Status |
|---|---|---|
| `amazon_kdp/README.md` | Översikt för Kindle eBook-publicering via Amazon KDP. | Skapat 2026-05-28 |
| `amazon_kdp/metadata_amazon_kdp.md` | Metadataförslag för KDP. | Skapat 2026-05-28 |
| `amazon_kdp/beskrivningar_amazon_kdp.md` | KDP-anpassade bokbeskrivningar och säljtexter. | Skapat 2026-05-28 |
| `amazon_kdp/kategori_nyckelord_prisforslag.md` | Kategori-, nyckelords- och prisförslag. | Skapat 2026-05-28 |
| `amazon_kdp/publiceringschecklista.md` | Checklista inför uppladdning i KDP. | Skapat 2026-05-28 |
| `amazon_kdp/filrekommendationer.md` | Rekommenderade filer och teknisk kontroll inför KDP. | Skapat 2026-05-28 |

## Kontinuitetskorrigering 2026-05-30

Ren manusfil och EPUB har uppdaterats efter korrigering av Karin/Kajsa-spåret. Kajsas födelseår är nu 1979 i romantext och projektfiler, och kapitel 19 planterar kopplingen utan att bekräfta den för tidigt.

## Senaste exportstatus 2026-05-31

Ren manusfil och EPUB har synkats efter frasjustering i kapitel 19: `Det skulle kunna stämma med Karin.`


## GitHub Actions-stilfix

`Under_stilla_vatten_Erland_Lindmark.epub` är synkad med Action-byggets EPUB-pipeline. EPUB:en har teknisk navigation i `nav.xhtml` och `toc.ncx`, men ingen synlig innehållsförteckningssida i läsflödet. `Under_stilla_vatten_Erland_Lindmark.pdf` är en PDF-preview med synlig innehållsförteckning och tvådelade kapitelrubriker.
