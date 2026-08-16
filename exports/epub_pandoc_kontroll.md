# EPUB-kontroll – GitHub Actions nav/title fix

Datum: 2026-08-16

## Resultat

- EPUB skapad från GitHub Actions-pipelinen.
- `nav.xhtml` finns och innehåller 24 kapitelposter.
- `nav.xhtml` ligger inte i spine/läsflödet.
- `toc.ncx` finns och innehåller 24 `navPoint`-poster.
- `toc.ncx` skrivs utan `ns0:`-prefix.
- `nav.xhtml` skrivs utan `html:`-prefix.
- Titelsidan är normaliserad till samma XHTML-struktur som den tidigare fungerande exports-EPUB:en.
- Kapitelrubrikerna är tvådelade: `Kapitel X` och kapitelnamn.
