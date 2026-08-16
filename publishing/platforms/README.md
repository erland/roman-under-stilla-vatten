# Plattformspublicering

Detta katalogträd innehåller publiceringsstöd för de plattformar som är aktuella för projektet.

## Princip

EPUB- och PDF-filer checkas inte in i projektet. De byggs av GitHub Actions från:

- `kapitel/kapitel-XX.md`
- `publishing/metadata.yaml`
- `publishing/cover.png`
- `publishing/epub.css`
- `scripts/build_book.py`

Preview-build och release-build producerar endast EPUB och PDF. Inga separata publiceringspaket byggs i nuläget.

## Aktuella plattformar

- `apple_books/`
- `google_play_books/`

Amazon KDP är medvetet utelämnat eftersom boken inte ska publiceras där i nuläget.

## Omslag

Samma kanoniska omslagsbild används för EPUB och PDF:

- `publishing/cover.png`
- Aktuell storlek: 1400 × 1979 px
- Färgläge: RGB

Denna bild bäddas in i både EPUB- och PDF-bygget och är avsedd att räcka för både Apple Books och Google Play Books i den nuvarande arbetsprocessen.
