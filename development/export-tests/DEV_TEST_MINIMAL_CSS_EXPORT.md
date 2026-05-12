# DEV_TEST_MINIMAL_CSS_EXPORT

Dev-only Diagnose fuer den Vergleich:

- Standard-Default-Shell mit voller CSS-Laenge
- lokale Minimal-Shell mit stark reduziertem Inline-CSS

Keine produktive Integration. Keine Aenderung an `email/templates/template-main.html`. Keine Aenderung an Snippets, Modulen, Design-Library oder regulaeren Exportregeln.

## Dateien

- Shell: `email-builder/development/export-tests/template-main-minimal-css.html`
- Test-State: `email-builder/development/export-tests/dev-test-minimal-css-export.state.json`

## Minimal noetige Shell-Struktur aus `email/templates/template-main.html`

Die produktive Default-Shell zeigt fuer diesen Test eine sehr kleine Struktur und einen sehr grossen CSS-Block. Fuer den Diagnosefall bleiben nur diese Bausteine erhalten:

1. `head`
   - `doctype`, `html`, `meta charset`, `viewport`, `X-UA-Compatible`
   - Outlook-XML-Block
   - bestehender externer CSS-Link bleibt als risikoarme Basiskomponente erhalten
2. Basis-CSS
   - globale Reset-Regeln fuer `body`, `p`, Apple-Detectors und `MessageViewBody`
   - Richtext-Flows fuer `module-rich-full-body--hero` und `module-rich-full-body--teaser-1col`
   - mobile Regeln nur fuer die im Test verwendeten Klassen:
     - `row-content`
     - `module-logo-pad`
     - `module-12-head-pad`
     - `module-12-body-pad`
     - `module-hero-variant-body-pad`
     - `module-hero-spacer-35`
     - `module-hero-spacer-button`
     - `module-teaser-1col-body-pad-spaced`
     - `module-footer-pad`
     - mobile Hero-Headline-Regeln fuer `hero-image-top`
3. Wrapper
   - `body`
   - `table.nl-container`
   - `tbody > tr > td`
4. Modul-Slot
   - eindeutige Marker:
     - `EMB-DEV-TEST-MODULE-SLOT:START`
     - `EMB-DEV-TEST-MODULE-SLOT:END`
5. Footer-/Snippetfaehigkeit
   - keine festen Module in der Shell
   - Footer bleibt ein normales Modul im Modul-Slot

## Trigger

Nur fuer Dev-/Diagnosefaelle:

`DEV_TEST_MINIMAL_CSS_EXPORT`

## Verhalten im Dev-Testmodus

Wenn dieser Trigger explizit fuer einen Dev-Agenten oder ein temporaeres Custom-GPT-Setup freigegeben ist, gilt nur fuer diesen Test:

1. Den Test-State aus `dev-test-minimal-css-export.state.json` verwenden.
2. Den modularen Snippet-Call-Block wie gewohnt aus `email_state + export-map.json` bauen.
3. Keine produktive `template-main.html` lesen oder ersetzen.
4. Kein `templateRead` fuer die Shell.
5. Stattdessen die lokale Shell `template-main-minimal-css.html` verwenden.
6. Nur in den markierten Dev-Test-Modul-Slot einsetzen.
7. Keine produktiven Exportregeln aendern oder ueberschreiben.

Der regulaere Exportpfad bleibt unveraendert:

- normale Default-Shell weiter nur `email/templates/template-main.html`
- regulaere Exportregeln weiter unveraendert
- keine automatische Aktivierung dieses Dev-Modus

## Test-Mail-Definition

Die Diagnosemail ist absichtlich klein und nutzt genau diese Modulfolge:

1. `logo` -> `emb_logo`
2. `hero-image-top` -> `emb_hero_image_top`
3. `teaser-1col` -> `emb_teaser_1col`
4. `footer` -> `emb_footer_marketing`

Wichtig:

- Das Mail-Artefakt ist state-basiert definiert, nicht als expandiertes Modul-HTML.
- Der Export muss daraus einen modularen Snippet-Call-Block erzeugen.
- In diesem Ordner liegt absichtlich keine expandierte Vollmail mit Modul-HTML.

## Validierungsziel

Verglichen werden sollen:

1. Dateigroesse der produktiven Default-Shell gegen die Minimal-Shell
2. syntaktische Gueltigkeit der Minimal-Shell
3. klare Trennung des Dev-Modus vom regulaeren Export
4. identische Modulfolge bei deutlich kleinerem Shell-CSS

## Optional fuer temporaeren Custom-GPT-Test

Nur wenn der Dev-Test wirklich im Custom GPT ausgefuehrt werden soll:

1. diese Dev-Datei zusaetzlich zum normalen Wissen laden
2. die lokale Minimal-Shell als reines Dev-Artefakt verfuegbar machen
3. das Upload-Paket nur fuer diesen expliziten Dev-Test neu erzeugen

Ohne diese explizite Dev-Freigabe bleibt alles lokal im Repo und ohne Upload-Bundle-Regeneration.
