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
- Omslagsbild: Planerad
- Skapad: 2026-05-23

## Rekommenderat arbetsflöde

1. Läs `projektstatus.md` för aktuellt läge.
2. Använd `roman-bibel.md`, `synopsis.md`, `kapitelplan.md` och `kontinuitetsanteckningar.md` som kontinuitetskälla.
3. Skriv ett kapitel i taget i chatten.
4. Godkänn eller justera kapitlet.
5. Spara godkänt kapitel som `kapitel/kapitel-XX.md`.
6. Uppdatera `projektstatus.md`, `arbetslogg.md`, `tidslinje.md`, `kontinuitetsanteckningar.md` och relevanta karaktärsfiler.

## Viktiga filer

- `roman-bibel.md` innehåller projektets centrala fakta.
- `synopsis.md` sammanfattar handling och baksidestext.
- `kapitelplan.md` är färdplanen för romanen.
- `stilguide.md` håller språk, ton och perspektiv konsekvent.
- `projektstatus.md` visar nästa rekommenderade steg.
- `kontinuitetsanteckningar.md` fångar fakta, ledtrådar och öppna trådar.

## GitHub Actions

Projektet innehåller workflows för validering, manuell preview-build och release-build av EPUB/PDF. Se `publishing/build-notes.md`.
PDF-bygget använder Python/ReportLab för att undvika LaTeX- och systemfontberoenden samt för att hålla omslag, titelsida, innehållsförteckning och kapitelrubriker stabila.


## EPUB/PDF-notering

GitHub Actions bygger EPUB och PDF från kapitelfilerna i `kapitel/`. EPUB:en har teknisk navigation via `nav.xhtml` och `toc.ncx` utan synlig innehållsförteckningssida i läsflödet. PDF:en har synlig innehållsförteckning och tvådelade kapitelrubriker.

## GitHub Actions-exporter – korrigering 2026-08-16

GitHub Actions-bygget använder nu en efterbearbetning som återskapar EPUB-navigationen explicit. Den tekniska innehållsförteckningen finns i `nav.xhtml` och `toc.ncx`, men `nav.xhtml` ligger inte i läsflödet som en synlig boksida.
