# Romanprojekt: Under stilla vatten

Detta är projektarkivet för romanen **Under stilla vatten**.

## Metadata

- Titel: Under stilla vatten
- Undertitel: En Kallviksdeckare
- Författare: Erland Lindmark
- Genre: Deckare
- Undergenrer: Thriller, romance
- Målgrupp: Vuxen
- Plats: Kallvik, fiktiv svensk kuststad
- Perspektiv: Tredje person nära Helena Norén
- Omslagsbild: Skapad; kanonisk byggfil är `publishing/cover.png`
- Skapad: 2026-05-23

## Rekommenderat arbetsflöde

1. Läs `projektstatus.md` för aktuellt läge.
2. Använd `roman-bibel.md`, `synopsis.md`, `kapitelplan.md` och `kontinuitetsanteckningar.md` som kontinuitetskälla.
3. Skriv eller revidera ett kapitel i taget.
4. Spara godkända kapitel som `kapitel/kapitel-XX.md`.
5. Uppdatera `projektstatus.md`, `arbetslogg.md`, `tidslinje.md`, `kontinuitetsanteckningar.md` och relevanta karaktärsfiler.

## Viktiga filer

- `kapitel/` innehåller romanens kanoniska kapiteltexter.
- `roman-bibel.md` innehåller projektets centrala fakta.
- `synopsis.md` sammanfattar handling och baksidestext.
- `kapitelplan.md` är färdplanen för romanen.
- `stilguide.md` håller språk, ton och perspektiv konsekvent.
- `projektstatus.md` visar nästa rekommenderade steg.
- `kontinuitetsanteckningar.md` fångar fakta, ledtrådar och öppna trådar.
- `publishing/` innehåller metadata, omslag, EPUB-CSS, byggdokumentation och publiceringsstöd.
- `publishing/platforms/` innehåller Apple Books- och Google Play Books-underlag.
- `scripts/` innehåller validerings- och byggskript.
- `.github/workflows/` innehåller GitHub Actions för validering, preview och release.

## GitHub Actions

Projektet innehåller workflows för validering, manuell preview-build och release-build av EPUB/PDF. Se `publishing/build-notes.md`.

### Preview-build

Kör workflowt **Build Preview** manuellt i GitHub Actions. Det bygger EPUB och PDF från de kanoniska kapitelfilerna och laddar upp dem som artifact:

- `under-stilla-vatten-preview`

### Release-build

Pusha en tagg som börjar med `v`, till exempel:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Då bygger GitHub Actions EPUB/PDF och laddar upp dem som GitHub Release-assets.

## Exportpolicy

EPUB och PDF ska inte längre checkas in i repositoryt. De skapas av GitHub Actions.

- `exports/` är borttagen.
- Lokala `*.epub` och `*.pdf` ignoreras via `.gitignore`.
- Kapiteltexterna i `kapitel/` är alltid kanonisk källa.
- EPUB:en har teknisk navigation via `nav.xhtml` och `toc.ncx`, men ingen synlig innehållsförteckningssida i läsflödet.
- PDF:en har synlig innehållsförteckning och tvådelade kapitelrubriker.


## Publiceringsstöd

Plattformsspecifika metadata, beskrivningar, kategoriförslag och checklistor ligger under:

- `publishing/platforms/apple_books/`
- `publishing/platforms/google_play_books/`

Amazon KDP är inte med i nuvarande struktur eftersom boken inte ska publiceras där. EPUB/PDF byggs av GitHub Actions och ligger inte incheckade i projektet.
