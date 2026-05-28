# Filrekommendationer för Amazon KDP

## Primära filer

### EPUB

Använd:

`exports/Under_stilla_vatten_Erland_Lindmark.epub`

Status:

- EPUBCheck: passerad enligt användarens test av föregående exportversion.
- Kapitel 1–24 ingår.
- Synlig innehållsförteckning är borttagen från läsflödet.
- Teknisk EPUB-navigation finns kvar.
- Kapitelnoteringar ingår inte.

### Omslag

Använd:

`exports/omslag_under_stilla_vatten_kdp.jpg`

Tekniska data:

- Format: JPEG
- Storlek: 1600 × 2560 px
- Färg: RGB
- DPI-metadata: 300 dpi
- Skapat genom uppskalning/anpassning av befintlig omslagsbild, inte ny generering.
- Ingen rygg, baksida, pris eller streckkod.

## Rekommenderad lokal kontroll

1. Öppna EPUB i Kindle Previewer.
2. Kontrollera boken på mobilvy, surfplattevy och e-reader-vy.
3. Kontrollera att kapitelrubrikerna inte får för stora marginaler.
4. Kontrollera att omslaget inte beskärs konstigt.
5. Kontrollera att titelsidan inte dupliceras.
6. Kontrollera att navigationen fungerar.

## Om KDP visar problem

- Om omslaget beskärs: skapa en alternativ JPEG med något större säkerhetsmarginal.
- Om rubrikerna ser konstiga ut: justera `exports/epub_custom.css` och exportera EPUB på nytt.
- Om Kindle Previewer lägger till en egen TOC-visning: det kan vara intern navigation, inte nödvändigtvis en synlig sida i boken.
