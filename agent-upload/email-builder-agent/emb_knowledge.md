# E-Mail Builder Agent Knowledge Bundle
Diese Datei ist ein Upload-Bundle fuer den E-Mail-Builder-Agenten.

Sie buendelt die relevanten Projektdateien in einer einzelnen Markdown-Datei. Pfadueberschriften gelten als virtuelle Repo-Dateien.

Fachliche Quelle bleiben immer die Originaldateien im Repository. Diese Bundle-Datei ist nur fuer den Agent-Upload bestimmt.

## email-builder/AGENTS.md

Dateityp: md

```md
ZWECK
Dieses Dokument definiert den Arbeitsprozess für den E-Mail Builder (EMB) und steuert die Zusammenarbeit mit Codex.

---

## SYSTEMKONTEXT

* email-builder/ → E-Mail Erstellung & Export
* design-system/ → Tokens & Design Library
* lp-builder/ → separates System

Gilt ausschließlich für email-builder/.

---

## REGELQUELLE

* `AGENTS.md` ist die einzige operative Regelquelle fuer Codex in `email-builder/`.
* Bestehende `README.md`-Dateien duerfen nicht als operative Regelquelle verwendet werden.
* Codex darf keine neuen `README.md`-Dateien erstellen.
* Bestehende `README.md`-Dateien duerfen nur dann neu angelegt oder gepflegt werden, wenn der User dies ausdruecklich fuer menschliche Dokumentation verlangt.
* Wenn eine neue verbindliche Regel dokumentiert werden muss, dann in `AGENTS.md` und nicht in einer README-Datei.

---

## AGENT-SETUP

* Die kanonische Systemprompt-Datei fuer Custom-GPT-/Agent-Setups ist `agent/systemprompt.md`.
* Standard fuer Agent-Knowledge ist eine einzelne gebuendelte Markdown-Datei, nicht ZIP und nicht lokale Ordnerstruktur.
* Wenn eine gebuendelte Knowledge-Datei mit Abschnitten unter exakten Originalpfaden hochgeladen ist, gelten diese Abschnitte als virtuelle Repo-Dateien.
* Der Agent darf in diesem Fall keinen Zugriff auf lokale Ordner erwarten; massgeblich bleiben die Inhalte unter den jeweiligen Pfadueberschriften.
* `agent/` ist die kanonische Quelle fuer Systemprompt, Regeldateien, Templates und Export-Basis.
* Der Standardordner fuer den Agent-Upload ist `agent-upload/email-builder-agent/`.
* Dieses Upload-Paket ist eine abgeleitete Kopie aus `agent/`.
* In diesem Standardordner liegen genau `systemprompt.md` und `emb_knowledge.md`.
* Nach produktiven Aenderungen an Modulen, Templates, Regeldateien oder `agent/export-map.json` muss dieses Agent-Upload-Bundle neu erzeugt werden.

---

## WAHRHEITSEBENEN

* preview/ = visuelle Wahrheit
* email/ = Produktions-HTML (Quelle für Export)
* design-system/tokens/ = Design-Wahrheit
* agent/ = abgeleiteter Arbeitslayer (keine eigene Wahrheit)

Export basiert nur auf email/ + export-map.json.

---

## GRUNDPRINZIPIEN

1. Neue visuelle oder strukturelle Modulvarianten sind grundsätzlich zu vermeiden, aber ERLAUBT wenn kein bestehendes Modul die Anforderung abbilden kann.

   * Bestehende Patterns sind immer der erste Weg
   * Wenn kein passendes visuelles oder strukturelles Modulmuster existiert, darf eine neue Modulvariante erstellt werden
   * Neue visuelle oder strukturelle Modulvarianten muessen sich an bestehenden Tokens, Spacing-Regeln und Strukturprinzipien orientieren
   * Neue visuelle oder strukturelle Modulvarianten duerfen keine bestehenden Regeln verletzen (Container, Spacing, Background etc.)
   * Neue technische E-Mail-/Responsive-Patterns sind davon ausgenommen und ohne ausdrueckliche User-Freigabe VERBOTEN

2. Neue oder geaenderte Module und Templates starten immer im Review-Layer und werden zuerst nur in zwei Review-Dateien geprueft:

   * `development/review/preview-index.html`
   * `development/review/email-index.html`

3. Diese Review-Dateien sind reine Test-Artefakte:

   * sie duerfen jederzeit ueberschrieben werden
   * sie sind nie fachliche Quelle
   * sie ersetzen keine produktiven Modul-, Template- oder Exportdateien

4. Fachliche Quellen bleiben ausschliesslich:

   * `preview/modules/*`
   * `email/modules/*`
   * `agent/template-*.preview.html`
   * `agent/template-*.definition.json`
   * `email/templates/*.html`
   * `agent/export-map.json`
   * `AGENTS.md`

5. Vor einer eindeutigen Review-Freigabe duerfen keine produktiven Modul-, Template-, Export- oder Library-Dateien veraendert werden.

---

## PATTERN-BINDING (VERBINDLICH)

* Bestehende Patterns aus preview/ MÜSSEN bevorzugt verwendet werden
* "Ähnlich bauen" ist NICHT erlaubt
* Struktur, Klassen und Hierarchie werden übernommen
* Fuer jedes neue Modul sind zwei bestehende produktive Referenzmodule verpflichtend:
  * `preview_reference_module`
  * `email_reference_module`
* Beide Referenzen MUESSEN aus bereits bestehenden produktiven Modulen stammen
* Der User muss diese Referenzen nicht vorgeben
* Codex MUSS die Referenzen automatisch bestimmen, indem es die bestehenden produktiven Module und ihre Agent-Dokumentation prueft
* `preview_reference_module` bestimmt das strukturelle Preview-Muster
* `email_reference_module` bestimmt das technische E-Mail-, Responsive-, CTA- und VML-Muster
* Neue Module duerfen visuell neu sein, aber ihre technische Preview- und E-Mail-Struktur darf nicht frei neu erfunden werden, wenn ein bestehendes Produktionsmuster die Aufgabe bereits tragen kann
* Neue visuelle oder strukturelle Modulvarianten sind erlaubt, wenn kein bestehendes Modul die Anforderung abbildet
* Neue technische E-Mail-/Responsive-Patterns sind ohne ausdrueckliche User-Freigabe verboten
* Fuer diese automatische Referenzwahl MUSS Codex vor neuer Modul- oder Template-Arbeit mindestens pruefen:
  * `preview/modules/`
  * `email/modules/`
  * `agent/preview-module-library.md`
  * `agent/builder-library.md`
  * bei Bedarf `preview/modules/catalog.yaml`
* Ziel dieser Pruefung ist:
  * zu erkennen, welches bestehende Modul dem neuen Modul strukturell, visuell und responsiv am naechsten kommt
* Die Auswahlkriterien fuer `preview_reference_module` und `email_reference_module` sind mindestens:
  * gleicher oder aehnlicher Modultyp
  * gleiche Grundstruktur
  * aehnliche Spaltenlogik
  * aehnliche Bild-/Text-Anordnung
  * aehnliche CTA-Logik
  * aehnliches Mobile-Verhalten
  * gleiche oder aehnliche E-Mail-Responsive-Struktur
  * vorhandene VML-/Outlook-Muster, falls relevant
  * vorhandene Padding-/Spacer-/Container-Logik

AUSNAHME:

* Wenn kein passendes visuelles oder strukturelles Modulmuster existiert, darf eine neue Modulvariante erstellt werden
* In diesem Fall gilt:

  * Aufbau muss sich an bestehender Modul-Architektur orientieren (.module / .module__inner)
  * Tokens und bestehende Utility-Klassen müssen verwendet werden
  * Spacing-Regeln müssen eingehalten werden
  * Kein eigenständiges Design-System erfinden
* Wenn stattdessen ein neues technisches E-Mail-/Responsive-Pattern noetig waere, MUSS Codex stoppen und User-Freigabe einholen

Ziel:

* Erst wiederverwenden
* Nur wenn notwendig erweitern

---

## LAYOUT-GRUNDSTRUKTUR

* Outer: `.module`
* Inner: `.module__inner`
* max-width: 600px (CSS-gesteuert)

NICHT erlaubt:

* eigene Container
* Wrapper verändern

---

## SPACING

Preview:

* keine freien Padding-Werte im HTML definieren
* freie Inline-Padding-Werte (`style="padding: ..."`) sind VERBOTEN
* eigene Padding-Klassen sind VERBOTEN
* Spacing kommt ausschliesslich aus bestehenden Preview-Klassen oder der Struktur des `preview_reference_module`
* Codex MUSS vorhandene Klassen vom Referenz-Modul übernehmen (z. B. module__inner Varianten)

E-Mail:

* Inline-Padding ist erlaubt, wenn es aus dem gewaehlten `email_reference_module` uebernommen wird oder fuer E-Mail-Kompatibilitaet noetig ist
* Codex darf Inline-Padding nicht frei neu erfinden
* Die folgenden Padding-Regeln sind Entwicklungsregeln fuer Codex bei Repo-Arbeit an neuen EMB-Modulen, template-spezifischen Modulen und Review-Modulen
* Sie gelten nicht als Freigabe oder Auftrag, dass der EMB-Agent beim normalen Mail-Bau neue Module konstruieren soll
* Neue EMB-Module, template-spezifische Module und Review-Module verwenden standardmaessig `60 / 40` Desktop und `40 / 20` Mobile
* Mobile `60 / 20` ist KEIN Default und darf nur bei einer dokumentierten Modul-Ausnahme beibehalten werden
* Padding muss dem `email_reference_module` oder dem Standard `60 / 40` Desktop und `40 / 20` Mobile folgen
* Abweichungen brauchen eine Begruendung oder ausdrueckliche User-Freigabe

Allgemein:

* Wenn kein Pattern klar ist:

  * Desktop: 60 / 40
  * Mobile: 40 / 20
* 24px Padding ist NICHT erlaubt
* Historische Mobile-Helper in bestehenden produktiven E-Mail-Modulen oder in `template-main.html` mit `24px` sind KEIN Default fuer neue Module
* Wenn ein Referenz-Modul genutzt wird, MUSS dessen Spacing exakt übernommen werden, aber nur wenn die Abweichung als dokumentierte Modul-Ausnahme belegt ist
* Wenn ein bestehendes Pattern oder Helper dem Standard `40 / 20` Mobile widerspricht und keine dokumentierte Ausnahme belegt ist, MUSS Codex stoppen und berichten
* Codex darf keine Mobile-Padding-Werte aus Desktop-Padding ableiten oder Desktop-Werte nach Mobile kopieren
* Review-spezifische `data-module`-Namen in `preview-index.html` erben mobile `module__inner`-Top-/Bottom-Paddings aus `preview-styles.css` nicht automatisch; Codex MUSS dort mobil explizit `40 / 20` oder eine dokumentierte Ausnahme absichern

DEFAULT (wenn kein Pattern klar ist):

* Desktop: 60 / 40
* Mobile: 40 / 20

Wenn Referenz-Modul gewählt:
→ dessen Spacing 1:1 übernehmen

---

## RICHTEXT-KONTEXTE

* Salutation-/Anredezeilen sind eigene kurze Textkontexte vor einem nachfolgenden Body
* Sie duerfen nie Teil eines `rich_full`-Body-Feldes oder `rich_full`-Wrappers sein
* Sie duerfen keine Listen enthalten
* Sie sind fachlich Plain Text oder hoechstens `rich_inline`, aber niemals `rich_full`
* Der Abstand zwischen Salutation und nachfolgendem Body ist ein externer Kontextabstand und betraegt standardmaessig 16px
* Absaetze, Listen und ihre vertikalen Abstaende innerhalb des Bodys bleiben ausschliesslich Aufgabe des allgemeinen `rich_full`-Flows
* Fuer `rich_full` gilt allgemein:
  * Text zu Text = 16px
  * Text zu Liste = 8px
  * Liste zu Text = 8px
  * Liste zu Liste = 8px
* Der Abstand zwischen einer Headline und dem ersten `rich_full`-Element ist immer externer Kontextabstand und wird nicht durch die interne Listenregel erzeugt
* Wenn eine Liste das erste Element im `rich_full`-Body ist, bekommt sie keinen zusaetzlichen internen Top-Abstand
* Listen bleiben im allgemeinen `rich_full`-Kontext optisch auf 20px eingerueckt
* `p`, `ul` und `ol` tragen im allgemeinen `rich_full`-Kontext keine eigenen allgemeinen Top-/Bottom-Defaults ausserhalb der zentralen Flow-Regeln
* `rich_inline` bleibt davon unberuehrt und erlaubt weiterhin keine Listen

---

## HINTERGRUND

* Module setzen KEINEN Background
* Es ist VERBOTEN:

  * `theme-gray`, `theme-white` oder ähnliche Klassen im Development zu setzen
  * inline background styles zu setzen
* Background wird ausschließlich im Builder gesteuert

VERBINDLICH:

* Wenn ein Referenz-Modul verwendet wird, MUSS Codex ALLE Background-bezogenen Klassen aktiv entfernen
* Dazu gehören insbesondere:

  * `.theme-gray`
  * `.theme-white`
  * jede andere theme-* Klasse

WICHTIG:

* Codex darf Background NICHT "übernehmen" oder "beibehalten"
* Background ist IMMER zu entfernen, auch wenn er im Referenz-Modul vorhanden ist

---

## REVIEW-ARBEITSWEISE

Ziel: Neue oder geaenderte Module und Templates in einem echten Preview- und E-Mail-Kontext pruefen, ohne daraus eine zweite fachliche Quelle zu machen.

Regeln:

* Fuer jede Modul- oder Template-Arbeit werden genau zwei Review-Dateien erzeugt oder aktualisiert:
  * `development/review/preview-index.html`
  * `development/review/email-index.html`
* `development/review/preview-index.html` ist die Browser-Testdatei:
  * nutzt den echten Preview-CSS-Kontext aus `agent/preview-styles.css`
  * zeigt nur das aktuell bearbeitete Preview-Modul oder Preview-Template
  * dient nur der visuellen Pruefung
* `development/review/email-index.html` ist die E-Mail-Testdatei:
  * nutzt den CSS-/Shell-Kontext aus `email/templates/template-main.html`
  * zeigt nur das aktuell bearbeitete E-Mail-Modul oder E-Mail-Template
  * kann direkt als Testmail in Iterable verwendet werden
* Fuer Modul-Arbeit gilt in beiden Review-Dateien ein festes Testgeruest:
  1. `logo`
  2. `hero-image-top`
  3. aktuelles neues oder geaendertes Modul
  4. `footer`
* `logo`, `hero-image-top` und `footer` dienen dort nur als stabiler Testkontext fuer Modul-Arbeit.
* Wenn das aktuell bearbeitete Modul selbst `logo`, `hero-image-top` oder `footer` ist, darf Codex keine doppelte Instanz einbauen und erstellt stattdessen eine sinnvolle Minimal-Testmail mit kurzem Hinweis im Bericht.
* Diese feste Reihenfolge gilt nur fuer Modul-Arbeit; Template-Arbeit nutzt weiterhin die tatsaechlich gewuenschte oder definierte Template-Reihenfolge.
* Review-Dateien sind reine Test-Artefakte:
  * sie duerfen jederzeit ueberschrieben werden
  * sie sind nie fachliche Quelle
  * sie duerfen keine produktive Wahrheit ersetzen
  * sie duerfen vollstaendig zusammengebaute Demo-Mails oder Demo-Templates mit Beispielmodulen und Demo-Content enthalten
  * Demo-Texte und Demo-Bilder sind erlaubt, aber erfundene Styles, Farben, Spacings, CTA-Farben oder Modul-Defaults sind verboten
  * Review-Defaults muessen immer aus bestehenden EMB-Quellen kommen, insbesondere aus `agent/export-map.json`, produktiven Preview-Modulen, produktiven E-Mail-Modulen, `email/templates/template-main.html` und `agent/preview-styles.css`
  * wenn ein benoetigter Default nicht eindeutig aus diesen Quellen ableitbar ist, muss Codex stoppen und den fehlenden Default berichten, statt einen Wert zu erfinden
* Der Ablauf fuer neue Module, Modul-Iterationen, neue Templates und Template-Iterationen ist immer:
  * zuerst nur `development/review/preview-index.html` und `development/review/email-index.html` als Review-Entwurf aktualisieren
  * Review-Dateien aktualisieren
  * User-Freigabe einholen
  * erst danach produktive Integration oder zentrale Dokumentation abschliessen
* Vor ausdruecklicher User-Freigabe des aktuellen Review-Stands sind Aenderungen an produktiven Zielpfaden fuer neue oder geaenderte Module und Templates verboten. Dazu gehoeren insbesondere:
  * `preview/modules/*`
  * `email/modules/*`
  * `agent/template-*.preview.html`
  * `agent/template-*.definition.json`
  * `email/templates/*.html`
  * `agent/export-map.json`
  * `design-system/design-library/index.html`
* Vor dem ersten Review-Schritt MUSS Codex fuer neue Module weiterhin `preview_reference_module` und `email_reference_module` aus bestehenden produktiven Mustern bestimmen und kurz begruenden.
* Referenzmuster, Tokens, Spacing-Regeln und bestehende technische E-Mail-Patterns bleiben verbindlich.
* Ohne ausdrueckliche User-Freigabe darf Codex kein neues technisches E-Mail-/Responsive-Pattern einfuehren.
* Die Review-Dateien duerfen sichtbaren Beispielcontent tragen.
* Produktiv relevantes CSS darf in Review-Dateien nur dann zusaetzlich vorkommen, wenn der vorhandene operative Kontext das Modul nachweislich noch nicht traegt.
* Wenn Review-CSS spaeter produktiv benoetigt wird, MUSS Codex den korrekten Zielort dafuer bestimmen:
  * `agent/preview-styles.css`
  * modulnaher Preview-Styleblock
  * Inline-Styles im E-Mail-Modul
  * `email/templates/template-main.html`
  * passende Design-Library-Dateien

---

## PRODUKTIVE INTEGRATION

Start nur nach eindeutiger User-Freigabe des aktuellen Review-Stands.

Regeln:

* Die produktive Integration arbeitet erst nach ausdruecklicher User-Freigabe direkt in den fachlichen Zielpfaden.
* Review-Dateien bleiben dabei nur Pruefflaechen und werden nicht 1:1 zur fachlichen Quelle umgedeutet.
* Ohne ausdrueckliche User-Freigabe des aktuellen Review-Stands darf Codex keine abschliessende produktive Integration in zentrale Dateien wie Libraries, Kataloge, Export-Maps, Template-Definitionen oder Uebersichten vornehmen.
* Bei der produktiven Integration darf Codex sichtbare Gestaltung oder Struktur nicht frei neu interpretieren.
* Zulaessig sind nur notwendige produktive Schritte wie:
  1. `preview/modules/<module_id>.html` erstellen oder anpassen
  2. `email/modules/emb_<module_id>.html` erstellen oder anpassen
  3. Render-Anbindung herstellen
  4. `export-map.json` ergaenzen oder anpassen
  5. relevante Agent-Dateien aktualisieren
  6. CSS nur wenn noetig an den korrekten produktiven Zielort uebernehmen
  7. `preview/modules/catalog.yaml` nur dann erweitern, wenn das Modul ausdruecklich ein allgemeines Library-/Core-Modul werden soll
* Wenn ein neues Modul im EMB renderbar sein soll, MUSS Codex weiterhin die operative Render-Anbindung herstellen:
  * registrierbares Preview-Markup in `agent/preview-modules.html`
  * Modulvertrag in `agent/preview-module-library.md`
  * Builder-Anbindung in `agent/builder-library.md`, wenn das Modul per Prompt oder Composition direkt ansprechbar sein soll
* Wenn der User ausdruecklich sagt, dass ein Modul nicht in die Library soll, dann gilt:
  * keine Aufnahme als allgemeines Core-/Library-Modul
  * kein automatisches Erweitern von `preview/modules/catalog.yaml`, ausser der User verlangt es ausdruecklich
  * keine automatische Aufnahme in allgemeine Design-Library-Dateien
  * aber weiterhin alle noetigen Agent-Dateien aktualisieren, falls das Modul im EMB renderbar oder per Prompt nutzbar sein soll
* Vor der produktiven Integration MUSS Codex pruefen:
  * ob `preview/modules/<module_id>.html` strukturell auf `preview_reference_module` basiert
  * ob `email/modules/emb_<module_id>.html` technisch und responsiv auf `email_reference_module` basiert
  * ob die responsive Grundstruktur des `email_reference_module` uebernommen wurde
  * ob keine neue Device-Switch-Logik eingefuehrt wurde
  * ob keine neuen globalen Responsive-Regeln ohne Freigabe eingefuehrt wurden
  * ob Review-CSS Development-only oder produktiv relevant ist
* Harte CSS-Regeln fuer die produktive Integration:
  * Development-only CSS darf nicht produktiv uebernommen werden
  * produktiv relevantes Modul-CSS darf nicht nur in Review-Dateien verbleiben
  * kein neues CSS in globale Dateien schreiben, wenn die Regel besser inline oder modulnah geloest werden kann
  * bestehende globale Styles nicht unnoetig aufblasen
* Die produktive E-Mail-Datei MUSS die responsive Grundstruktur des gewaehlten `email_reference_module` uebernehmen.
* Wenn die sichtbare Review-Version technisch nicht sauber auf finale Iterable-Variablen abbildbar ist:
  * produktive Integration stoppen
  * zuerst den Review-Stand korrigieren
  * keine unvollstaendigen Module in produktive Dateien uebernehmen
* Wenn die produktive Integration oder Validierung fehlschlaegt:
  * keine erfolgreiche Integrationsmeldung ausgeben
  * keinen automatischen Reset von Review-Dateien ausfuehren
  * konkret berichten, was fehlt oder korrigiert werden muss

---

## COMPOSITION TEMPLATES

* Auch Template-Arbeit nutzt die beiden Review-Dateien:
  * `development/review/preview-index.html`
  * `development/review/email-index.html`
* Review-Dateien sind auch fuer Templates nie fachliche Quelle.
* Operative Template-Dateien liegen namespacet im flachen Agent-Layer:
  * `agent/template-<template_id>.preview.html`
  * `agent/template-<template_id>.definition.json`
* Generische operative Template-Dateien wie `agent/preview.html` oder `agent/template-definition.json` sind verboten
* Die Preview-Datei darf fertige Preview-Module enthalten und ist die visuelle Startbasis fuer den EMB
* Die Definition ist die verbindliche Agent-Logik
* Operative Template-Dateien duerfen nicht zu vollstaendig zusammengebauten Testmails oder Test-Templates umgebaut werden
* Templates duerfen keine neuen Module einfuehren
* Templates duerfen keine freie Reihenfolge definieren
* Entfernen oder Duplizieren ist nur erlaubt, wenn `template-<template_id>.definition.json` es explizit erlaubt
* Jedes Composition-Template braucht zusaetzlich ein eigenes Iterable-Basistemplate unter `email/templates/<template_id>.html`
* Dieses Basistemplate darf keine festen Module und keine festen Snippet-Calls enthalten
* `email/templates/<template_id>.html` ist die Iterable-Base-/Shell-Datei und enthaelt genau das CSS, das fuer die Module dieses Templates benoetigt wird
* Vollstaendig zusammengebaute Preview- oder E-Mail-Tests fuer Templates gehoeren ausschliesslich in die Review-Dateien unter `development/review/`
* Auch fuer Templates ist die ausdrueckliche User-Freigabe des aktuellen Review-Stands das Gate vor jeder abschliessenden produktiven Integration oder zentralen Dokumentation.
* Nach ausdruecklicher User-Freigabe fuehrt Codex bei neuen Templates oder Template-Iterationen die produktive Integration direkt in den echten Zielpfaden durch.
* Je nach Aenderung betrifft diese Template-Integration:
  * `agent/template-<template_id>.definition.json` als strukturelle Template-Definition und Modulreihenfolge fuer den EMB
  * `agent/template-<template_id>.preview.html` als operative Preview-/Template-Logik
  * `email/templates/<template_id>.html` als Iterable-Base-/Shell-Datei mit genau dem CSS, das fuer die Module dieses Templates benoetigt wird
  * relevante Library-/Regeldateien nur bei konkretem Bedarf, z. B. `agent/builder-library.md` oder `agent/template-definition.contract.md`
  * `development/review/preview-index.html` und `development/review/email-index.html` optional als finalen Teststand
* Auch nach der Integration bleiben die Review-Dateien reine Test-Artefakte; die fachliche Wahrheit liegt in den produktiven Template-Zielpfaden.
* `development/templates/searcher-standard/*` bleibt bis zur finalen Prozessentscheidung als historischer Prozessbeleg erhalten, ist aber kein verpflichtender Startpunkt und keine operative Wahrheit
* Vor Freigabe muss jedes Template end-to-end geprueft werden:
  * Preview funktioniert im EMB
  * Slot-Reihenfolge wird eingehalten
  * locked Module koennen nicht entfernt werden
  * repeatable Module koennen dupliziert werden
  * keine neuen Module entstehen
  * Iterable-Shell enthaelt keine Module oder Snippet-Calls
  * Export nutzt die template-spezifische Iterable Template-ID
  * normaler Export ohne Template bleibt unveraendert

---

## DESIGN LIBRARY INTEGRATION (VERBINDLICH)

Ziel: Die sichtbare E-Mail-Library bleibt konsistent mit dem aktuellen statischen Library-Setup in `design-system/`.

AKTIVE QUELLEN (VERBINDLICH):

* Fuer sichtbare E-Mail-Module in der Library ist `email-builder/preview/modules/` die relevante Quellbasis.
* Der Preview-CSS-Kontext dafuer bleibt `email-builder/agent/preview-styles.css`.
* Die sichtbare Einbettung fuer E-Mail-Module erfolgt statisch in `design-system/design-library/index.html`.
* `design-system/design-library/frames/email/**` ist keine aktive Quelle mehr fuer die sichtbare E-Mail-Library.

INDEX-INTEGRATION (VERBINDLICH):

* Wenn sichtbare E-Mail-Library-Inhalte geaendert werden sollen, ist nach User-Freigabe die statische Einbettung in `design-system/design-library/index.html` an die aktiven Quellen anzupassen.
* Keine alten Frame-Pfade aus `design-system/design-library/frames/email/` neu einfuehren oder pflegen.
* Keine fachlichen Regeln aus `frames/email/**` ableiten.

---

## PUBLISH / GITHUB (VERBINDLICH)

* Veroeffentlichung ist Teil der produktiven Integration und wird automatisch von Codex ausgefuehrt.
* Nach Library-Integration MUSS der Publish-Mirror aktualisiert werden:
  python3 design-system/scripts/sync_design_library_publish.py
* Anschließend MUSS Codex die Änderungen auf GitHub (main) pushen.

VOR DEM PUSH (PFLICHT-CHECK):

* Codex MUSS das Modul visuell validieren – aber NICHT zwingend über echten Browser
* Falls Browser-Rendering (z. B. safaridriver) nicht möglich ist, gilt:

  * Vergleich mit bestehenden funktionierenden statischen E-Mail-Library-Einbettungen
  * Sicherstellen, dass `agent/preview-styles.css` korrekt beruecksichtigt ist
  * Sicherstellen, dass keine neuen Wrapper/Strukturen eingefuehrt wurden
* Modul darf KEINEN eigenen Rendering-Kontext erzeugen

REGEL:

* Push ist erlaubt, wenn strukturelle Gleichheit mit bestehenden statischen E-Mail-Library-Einbettungen sichergestellt ist (auch ohne echten Browser-Render)

EINSCHRÄNKUNG:

* Es dürfen NUR die Änderungen des aktuellen Moduls enthalten sein
* Keine Testreste oder unvollständigen Module mit veröffentlichen
* Keine parallelen oder abgebrochenen Experimente mit pushen

REGEL:

* Push auf main darf nur erfolgen, wenn diese Checks bestanden sind

EINSCHRÄNKUNG:

* Es dürfen NUR die Änderungen des aktuellen Moduls enthalten sein
* Keine Testreste oder unvollständigen Module mit veröffentlichen
* Keine parallelen oder abgebrochenen Experimente mit pushen

---

## VERIFIKATION VOR PUSH (VERBINDLICH)

Vor Veröffentlichung MUSS geprüft werden:

* Modul rendert in der Library identisch zu bestehenden Modulen (Typografie, Spacing, Grid)
* Statische Einbettung in `design-system/design-library/index.html` ist korrekt
* CSS wird korrekt geladen (`agent/preview-styles.css` aktiv)
* Kein Layout-Drift im Grid/Index

Erst danach darf ein Push auf main erfolgen.

---

## EXPORT FLOW — FINAL (VERBINDLICH)

Der Export-Flow ist FINAL definiert und darf nicht verändert werden.

Er besteht ausschließlich aus:

1. createCampaign
2. genau ein Campaign-Read zum Holen der campaign-owned `templateId` und des `campaignState`
3. genau ein Template-Read zum Holen der aktuellen campaign-owned HTML-Shell
4. finaler HTML Write, bei dem nur Subject, Preheader sowie Snippet Calls plus Parameterwerte in die bestehenden Replace-Zonen eingesetzt werden

WICHTIG:

Dieser Flow definiert ausschließlich die fachlichen Business-Schritte.

Er schränkt NICHT ein:

* die echte Tool-Execution des createCampaign API-Calls
* die technische Ausführung des genau einen erlaubten Campaign-Reads
* die technische Ausführung des genau einen erlaubten Template-Reads
* die technische Ausführung des finalen HTML Writes
* das vollständige Response-Handling der verwendeten Tools
* das Auslesen und Validieren der API-Antwort

VERBINDLICH:

* createCampaign MUSS als echter API-Call ausgeführt werden
* die Response MUSS vollständig zurückgegeben werden
* eine verwertbare Campaign-ID MUSS aus der echten API-Response extrahiert und validiert werden
* als erlaubte ID-Kandidaten gelten nur `campaignId`, `id`, `response.campaignId`, `response.id`, `data.campaignId`, `data.id`, `campaign.campaignId` und `campaign.id`
* ein ID-Kandidat ist nur gueltig, wenn er als `number` oder `string` vorliegt; die erste verwertbare ID MUSS intern zu String normalisiert werden
* direkt nach `createCampaign` MUSS genau ein echter Campaign-Read mit dieser `campaignId` ausgeführt werden, um daraus ausschließlich die campaign-owned `templateId` und den aktuellen `campaignState` zu lesen
* aus diesem Campaign-Read darf ausschließlich die campaign-owned `templateId` und der aktuelle `campaignState` zur Status-Validierung vor dem Write gelesen werden
* nach bekanntem `templateId` MUSS genau ein echter Template-Read der aktuellen campaign-owned HTML-Shell ausgeführt werden
* technische Execution, Response-Rückgabe und Response-Parsing dürfen nicht durch Guardrails blockiert oder verkürzt werden
* auf die createCampaign-Response MUSS explizit gewartet werden, bevor der Export weiterläuft
* createCampaign darf nicht offen bleiben, hängen oder ohne abgeschlossene Response-Verarbeitung enden
* der CreateCampaign-Request des Builder-Exports MUSS exakt `name` und `templateId` enthalten und darf keine Versand- oder Scheduling-Felder enthalten
* `listIds`, `sendAt`, `scheduleSend`, `sendMode` und `recipientTimeZone` sind im CreateCampaign-Request des Builder-Exports verboten
* falls spaeter eine Versandliste benoetigt wird, ist das ein separater manueller Iterable-Schritt ausserhalb dieses Export-Flows
* vor dem finalen HTML Write MUSS der eine erlaubte `campaignRead` bestaetigen, dass der `campaignState` explizit editierbar ist; `Ready` ist der bevorzugte erwartete Status
* bei `Scheduled`, `Running`, `Finished`, `Archived`, `Recurring`, `Aborted` oder jedem anderen nicht explizit als editierbar belegten Status MUSS der Export vor dem Write stoppen
* `569946` oder eine alternative `iterable_template_id` darf nur als Basis-`templateId` fuer `createCampaign` verwendet werden, nie als frei neu zu schreibende Minimal-Shell
* die gelesene campaign-owned HTML-Shell MUSS ausserhalb der erlaubten Replace-Zonen vollstaendig erhalten bleiben
* wenn keine verwertbare Campaign-ID extrahierbar ist, MUSS der Export als Tool-Runtime-/Envelope-Fehler, Iterable-API-Fehler oder Parser-Fehler klassifiziert werden und vor jedem Read/Write stoppen
* bei fehlgeschlagenem CreateCampaign MUSS das Logging mindestens finalen Request ohne Secrets, HTTP-Status-Info, Raw-Body-Info, gepruefte ID-Kandidaten, Ablehnungsgrund und den Hinweis auf den unterbliebenen Read/Write enthalten
* ersetzt werden duerfen ausschliesslich Subject, Preheader und der vorhandene modulare Slot beziehungsweise Snippet-Call-Block

--------------------------------------------------
VERBOTENE ÄNDERUNGEN
--------------------------------------------------

Es ist NICHT erlaubt:

* zusätzliche Iterable API Calls einzubauen, die über `createCampaign`, genau einen Campaign-Read fuer die campaign-owned `templateId` und den `campaignState`, genau einen Template-Read der campaign-owned HTML-Shell sowie den finalen HTML Write hinausgehen
* den erlaubten Campaign-Read für andere Daten oder weitere Logik zu nutzen
* mehr als einen Template-Read einzubauen
* zusätzliche Transformationsschritte einzubauen
* HTML mehrfach zu generieren
* alternative Exportpfade zu definieren
* automatische Retries einzubauen
* `listIds` im CreateCampaign-Request des Builder-Exports zu verwenden
* `sendAt` im CreateCampaign-Request zu verwenden
* `scheduleSend` im CreateCampaign-Request des Builder-Exports zu verwenden
* `sendMode` oder `recipientTimeZone` im CreateCampaign-Request des Builder-Exports zu verwenden
* einen nicht offiziell dokumentierten Status-Reset- oder Update-State-Call einzubauen, um `Scheduled` nachtraeglich auf `Ready` oder `Draft` zu setzen
* die campaign-owned HTML-Shell durch eine freie Minimal-Shell, eine lokal neu erfundene Shell oder nackte `SNIPPET_CALLS` als Komplett-HTML zu ersetzen

--------------------------------------------------
REGEL
--------------------------------------------------

Wenn Codex Änderungen am Export-Flow vornimmt:

→ MUSS er prüfen:
„Verändert diese Änderung den definierten Flow?“

Wenn JA:
→ Änderung ist VERBOTEN

--------------------------------------------------
ZIEL
--------------------------------------------------

Der Export-Flow ist:

* minimal
* deterministisch
* reproduzierbar

Er darf nicht erweitert oder „optimiert“ werden.

---

## ITERABLE-PARAMETER-PARITAET (VERBINDLICH)

Fuer jedes Modul gilt:

* Die produktive Integration gilt fuer neue Module nur dann als erfolgreich, wenn die Iterable-Parameter-Paritaet vollstaendig bestanden ist.
* Primaere Quelle fuer die kanonische Variablenliste ist immer das produktive E-Mail-Modul: `email/modules/emb_<module_id>.html`
* Codex MUSS daraus alle `{{...}}` Variablen extrahieren.
* Zusaetzlich MUSS Codex alle Variablen pruefen, die fuer optionale Zustaende, Fallbacks, Background-Farben, Visibility-Flags oder CTA-Logik benoetigt werden, auch wenn sie nicht als einfacher sichtbarer Textknoten erscheinen.
* Diese kanonische Variablenliste MUSS exakt konsistent sein zwischen:
  * `email/modules/emb_<module_id>.html`
  * `agent/export-map.json`
  * `agent/builder-library.md`
  * `agent/preview-module-library.md`
  * weiteren relevanten Agent-Dateien mit Modulvertrag, Defaults oder Exportlogik
  * allen Variablen, die das Snippet erwartet
  * allen Variablen, die der Export-Payload an Iterable uebergeben koennen muss
* Die Parameterreihenfolge in `export-map.json` MUSS exakt der Reihenfolge im Snippet entsprechen.
* Die Anzahl der Parameter MUSS identisch sein.
* Modulvariablen muessen konsistent dem Prefix `emb_<module_id>_...` folgen.
* Abweichungen sind nur fuer ausdruecklich dokumentierte globale Systemfelder erlaubt; fuer modulbezogene Felder sind sie VERBOTEN.
* Es ist NICHT erlaubt:
  * Parameter hinzuzufuegen
  * Parameter zu entfernen
  * Parameter umzubenennen
  * Parameter zu verschieben
  * Modulvariablen ohne gueltigen Prefix einzufuehren
  * Required-Variablen ohne brauchbaren Default oder ohne sichere Befuellungsquelle zu definieren

--------------------------------------------------
VALIDATION PFLICHT
--------------------------------------------------

Nach jeder Änderung an:

* `export-map.json`
* Snippets
* `builder-library`
* `preview-module-library`
* weiteren relevanten Agent-Dateien mit Modulvertrag, Defaults oder Exportlogik

MUSS Codex prüfen:

1. Fuer jedes neue Modul:
   - leite die kanonische Variablenliste primaer aus allen `{{...}}` Variablen in `email/modules/emb_<module_id>.html` ab
   - ergaenze diese Liste um Variablen fuer optionale Zustaende, Fallbacks, Background-Farben, Visibility-Flags und CTA-Logik
   - extrahiere die Variablen aus `export-map.json`
   - extrahiere die Variablenlisten aus `agent/builder-library.md`, `agent/preview-module-library.md` und weiteren relevanten Agent-Dateien
   - pruefe die Variablen, Required-/Default-Definitionen und die exportierbare Iterable-Payload gegeneinander
2. Vergleiche:
   - Anzahl
   - Reihenfolge
   - Namen
   - Prefix
   - Required-/Default-Status
   - Vollstaendigkeit des Iterable-Export-Payloads
3. Wenn Abweichung:

→ Aenderung ist UNGUELTIG
→ Codex MUSS sie korrigieren, bevor er fortfaehrt
→ Codex MUSS die produktive Integration stoppen
→ Codex darf keine erfolgreiche Integrationsmeldung ausgeben

--------------------------------------------------
HARTE FEHLERBEDINGUNGEN
--------------------------------------------------

Die produktive Integration darf NICHT als erfolgreich gelten, wenn:

* eine Variable im E-Mail-Modul existiert, aber in `export-map.json` fehlt
* eine Variable in `export-map.json` existiert, aber im Modul nicht genutzt wird und nicht ausdruecklich begruendet ist
* eine Variable in Agent-/Builder-Dateien inkonsistent oder anders benannt ist
* eine Required-Variable keinen brauchbaren Default und keine sichere Befuellungsquelle hat
* eine Variable nicht dem Prefix `emb_<module_id>_...` folgt
* Variablen doppelt oder inkonsistent vorkommen
* die Anzahl erwarteter Snippet-/Iterable-Parameter nicht mit der Anzahl der Export-Parameter uebereinstimmt
* optionale Parameter, Visibility-Flags oder Fallbacks nicht sauber definiert sind
* der Export-Payload nicht alle von Iterable erwarteten Parameter liefern kann

Wenn eine dieser Pruefungen fehlschlaegt:

* Codex MUSS stoppen
* Codex darf keine erfolgreiche Integrationsmeldung ausgeben
* Codex MUSS konkret berichten:
  * welche Variable fehlt
  * wo sie fehlt
  * ob sie required, defaulted oder optional ist
  * wie sie korrigiert werden muss

--------------------------------------------------
REGEL
--------------------------------------------------

`export-map.json` darf nur existieren, wenn:

→ SNIPPET = EXPORT-MAP (1:1)
→ E-MAIL-MODUL = EXPORT-MAP = BUILDER-/AGENT-VERTRAG = ITERABLE-PAYLOAD

## DO NOT DO

* KEINE Nutzung von modules-Frames für finale E-Mail-Module
* KEIN neuer Frame-Typ ohne Referenz zu bestehenden Modulen
* KEIN Push auf main ohne Sichtprüfung in der Library
* KEIN Mischen von Frame-Typen (z. B. modules + snippets)
* KEINE Veröffentlichung von Testständen oder abgebrochenen Modulen

---

## QA

* Builder testen
* Export prüfen
* visuelle QA

---

## CSS STANDARD

* components.css = deprecated
* `agent/preview-styles.css` bleibt die globale Preview-CSS-Quelle
* Der kanonische oeffentliche Preview-CSS-Link ist `https://s24-creative-ops.github.io/email-builder/preview-styles.css`
* Inhaltliche globale Preview-CSS-Regeln werden nur in `agent/preview-styles.css` gepflegt; weitere Preview-CSS-Dateien als zweite CSS-Wahrheit sind verboten
* modulrelevantes CSS darf zusaetzlich modulnah oder inline definiert werden, wenn das fuer das einzelne Modul oder fuer E-Mail-Kompatibilitaet der richtige Ort ist
* globale CSS-Dateien nur erweitern, wenn die Regel wirklich global benoetigt wird
* Development-only CSS gehoert nie in produktive CSS-Dateien oder produktive Module

---

## KRITISCHE REGELN

* Kein Modul ohne export-map
* Keine neuen Felder ohne Mapping
* Keine inkonsistenten Namen
* Kein Direktzugriff auf .publish

---

## TRIGGER

Die produktive Integration startet nur bei eindeutiger User-Freigabe des aktuellen Review-Stands.
```

## email-builder/agent/guardrails.md

Dateityp: md

```md
# Guardrails

## Scope

- `email-builder/agent/` ist der operative Agent-Satz und der kanonische flache Ordner fuer alle Agent-Dateien.
- Dort liegen `systemprompt.md`, `guardrails.md`, `builder-library.md`, `preview-rules.md`, `preview-module-library.md`, `icon-library.md`, `preview-template.html`, `preview-modules.html`, `export-rules.md`, `tone-of-voice.md` und `content-rules.md` direkt fuer das Agent-Setup.
- `systemprompt.md` gehoert inhaltlich zum Agent-Set, wird praktisch aber als Text-Hinweis eingefuegt und nicht wie eine normale Upload-Datei behandelt.
- `guardrails.md` ist eine aktive operative Agent-Datei im Agent-Satz unter `agent/`.
- `guardrails.md`, `builder-library.md`, `preview-rules.md`, `preview-module-library.md`, `icon-library.md`, `preview-template.html`, `preview-modules.html`, `export-rules.md`, `tone-of-voice.md` und `content-rules.md` bilden den relevanten Datei-Wissenssatz.
- Operative Composition-Templates liegen im flachen `agent/`-Ordner, aber immer namespacet ueber `template_id`.
- Review-Dateien unter `development/review/` sind reine Test-Artefakte und nie operative Builder- oder Export-Wahrheit.
- `development/templates/searcher-standard/*` bleibt bis zur finalen Prozessentscheidung als historischer Prozessbeleg erhalten, ist aber kein verpflichtender Startpunkt fuer neue Template-Arbeit.
- Alles unter `email-builder/deterministic-test/` ist tabu.
- Keine zweite Source of Truth aufbauen.
- Unterordner unter `agent/` sind nicht Teil des operativen flachen Agent-Dateisatzes.
- Alte Legacy-Verweise wie `builder/assets/builder-preview-template.html`, `builder/assets/builder-preview-modules.html`, `builder/assets/builder-preview-modules.css`, `builder/assets/builder-module-library.html`, `builder/system/builder-variables.md` oder alte Resolver-/Runtime-Dateien sind nicht operativ; massgeblich ist heute ausschliesslich der flache Agent-Satz unter `agent/`.

## Sprache

- Antworte immer in der konfigurierten System- oder UI-Sprache des Users.
- Starter-Buttons, Quick Actions und vordefinierte Einstiegsoptionen sind kein Sprachsignal.
- Wenn keine UI-Sprache sichtbar ist, darf die Sprache freier User-Nachrichten als Fallback dienen.

## Operative Wahrheit

- Vor der ersten Preview ist ein leerer Initialzustand zulaessig.
- Nach der ersten HTML-Preview im Canvas ist die Preview die visuelle Kontrollansicht der aktuellen Mail.
- Der parallel gefuehrte `email_state` ist die operative Exportquelle und muss nach jeder Preview denselben fachlichen Stand tragen.
- `export-map.json` ist der technische Exportvertrag fuer erlaubte Module, Felder, Required-Flags und Defaults.
- Export und Save duerfen nie aus alter Template-Logik oder frei erfundenen Defaults rekonstruiert werden, wenn bereits eine Preview existiert.
- Ein strukturierter Export-State ist nur als direkt aus der letzten sichtbaren Preview abgeleitete und aktiv fortgeschriebene Arbeitskopie erlaubt.
- Wenn Preview und strukturierter Export-State voneinander abweichen, ist das ein State-Drift-Fehler: Die Preview bleibt visuelle Referenz, aber der Export darf erst weiterlaufen, wenn der `email_state` wieder deckungsgleich fortgeschrieben wurde.
- Wenn dieselbe Preview fortgeschrieben wird, bleibt ihre bestehende Campaign-Bindung erhalten.
- Wenn eine neue Preview oder neue Startkomposition begonnen wird, startet sie ohne uebernommene Campaign-Bindung.

## Begriffe und Defaults

- Preview = visuelle Kontrollansicht fuer den User, nicht die regulaere Exportquelle.
- `email_state` = operative Exportquelle fuer Subject, Preheader, Template-Kontext, Campaign-Bindung und Modulfelder.
- `export-map.json` = technischer Exportvertrag fuer Modulmapping, Feldtypen, Required-Felder und technische Defaults.
- Defaults sind nur erlaubt, wenn sie eindeutig in `export-map.json` oder in einer dokumentierten technischen Resolver-Quelle definiert sind.
- Dokumentierte technische Resolver-Quellen sind nur:
  - Hintergrund-Rhythmus aus `builder-library.md` plus `preview-styles.css`
  - Icon-Auswahl aus `icon-library.md`
  - finale Button-Farbwerte aus `builder-library.md`
- Werte duerfen im Export nicht aus sichtbarer Darstellung, Button-Klassen, freiem Modulkontext oder unmarkiertem Preview-Styling geraten werden.

## Preview-Basis

- Jede Preview startet mit einer exakten Kopie von `preview-template.html`.
- Ersetze nur den Text in `[data-preview-subject-text]` und `[data-preview-preheader-text]`.
- Setze Modulbloecke nur zwischen die beiden Modul-Slot-Kommentare.
- Verwende ausschliesslich Modul-HTML aus `preview-modules.html`, das in `preview-module-library.md` registriert ist.
- Kein Ersatz-HTML, keine Fantasie-Komponenten, keine improvisierten Sektionen.

## Bildregeln

- Wenn keine echte User-Bild-URL vorliegt, bleibt die Preview bei der grauen Placeholder-Flaeche.
- Placeholder, `data:image`, SVG- oder Text-Fake-Werte duerfen nie als Export-`image_url` verwendet werden.
- Wenn eine echte User-Bild-URL vorhanden ist, gewinnt sie fuer Preview und Export.
- Wenn keine echte User-Bild-URL vorhanden ist, nutzt der Export den formatbasierten Fallback aus `builder-library.md`.

## Iconregeln

- `icon-library.md` ist die einzige erlaubte operative Quelle fuer Benefit-Icons.
- Operative Icon-Slots gibt es aktuell nur im Modul `benefits-3col`.
- Icon-Slots werden in der Preview ueber `data-icon-field="<exportfeld>"` markiert.
- Jede `*_icon_url` fuer `benefits-3col` muss exakt einer in `icon-library.md` hinterlegten URL entsprechen.
- Die Icon-Auswahl erfolgt bucket-basiert anhand des jeweiligen Benefit-Texts.
- Wenn keine klare Bucket-Zuordnung moeglich ist, gilt der kanonische `general-positive`-Fallback aus `icon-library.md`.
- Leere Icon-Slots, freie oder externe Icon-URLs sowie frei erfundene Icon-Namen sind verboten.
- Beispiel- oder Quellblock-Icons aus `preview-modules.html` sind nicht die operative Wahrheit und muessen vor erfolgreichem Preview-Render durch ausgewaehlte oder Fallback-Icons aus `icon-library.md` ersetzt sein.

## Komposition

- Jede Mail enthaelt genau ein Logo, genau ein Hero und genau ein Footer-Modul.
- Logo steht immer an Position `1`, Hero an Position `2`, Footer am Ende.
- `logo`, Hero und `footer` sind fixe Shell-Module.
- `logo`, Hero und `footer` duerfen nicht entfernt, verschoben oder dupliziert werden.
- Direkte User-Module haben Vorrang; fehlende Pflichtmodule werden nur ergaenzt, nie dupliziert.
- Ohne direkte Modulliste gilt zuerst Template-Start, sonst Blueprint-Start aus `builder-library.md`.
- Es duerfen nur Module verwendet werden, die in `preview-module-library.md` registriert sind.
- Der Hintergrund-Rhythmus der finalen Modul-Komposition folgt strikt `builder-library.md`; Hero immer weiss, Footer immer weiss, dazwischen keine freie Abweichung vom definierten Rhythmus.
- Fuer exportfaehige States muss dieser Hintergrund-Rhythmus vor dem Mitschreiben nach `email_state.content` in konkrete Hexwerte aus der verbindlichen technischen Farbquelle aufgeloest werden.
- `theme-white`, `theme-gray` oder andere Preview-Klassen duerfen nie als `*_bg_color`-Exportwerte in `email_state.content` verbleiben.
- Ein Composition-Template darf nur genutzt werden, wenn die operativen Dateien aus `template_id` ableitbar sind und im flachen `agent/`-Ordner vorhanden sind:
  - `template-<template_id>.definition.json`
  - `template-<template_id>.preview.html`
- Generische operative Template-Dateien wie `agent/preview.html` oder `agent/template-definition.json` sind verboten.
- Bei Template-Nutzung ist `template-<template_id>.preview.html` nur die visuelle Preview-Basis.
- `template-<template_id>.definition.json` ist die verbindliche Agent-Logik.
- Regeln duerfen niemals aus `template-<template_id>.preview.html` abgeleitet werden.
- Vorhandene CSS- und Asset-Links aus `template-<template_id>.preview.html` muessen unveraendert uebernommen werden.
- Relative Pfade fuer CSS, JS oder sonstige Assets duerfen nicht geraten, normalisiert oder frei umgeschrieben werden.
- Ein CSS-Link darf nie auf eine JS-Datei zeigen.
- Bei Template-Nutzung duerfen nur Inhalte innerhalb der Modulbereiche geaendert werden.
- Die Slot-Reihenfolge aus `template-<template_id>.definition.json` ist verbindlich.
- Neue Modultypen ausserhalb der Slots sind verboten.
- Entfernen oder Duplizieren ist nur erlaubt, wenn `template-<template_id>.definition.json` es explizit erlaubt.

## Modulstruktur

- Die Grundstruktur eines Moduls darf nicht veraendert werden.
- Innerhalb eines Moduls duerfen keine freien neuen Elemente ergaenzt, keine bestehenden Elemente frei entfernt und keine internen Layouts umgebaut werden.
- Spaltenanzahl, Spaltenverhaeltnis, Bild-/Text-Aufteilung und sonstige Grundlayout-Struktur eines Moduls sind fix.
- Erlaubt sind nur inhaltliche Anpassungen innerhalb der vorgesehenen Modul-Logik.
- Dazu gehoeren insbesondere Textaenderungen, CTA-Textaenderungen, der Tausch des vorgesehenen CTA-Typs sowie das Ausblenden von Headline oder Button, wenn das jeweilige Modul dafuer eine vorgesehene Show-/Hide-Logik hat.
- Wenn eine gewuenschte Aenderung die Modulstruktur brechen wuerde, muss statt eines internen Umbaus ein anderes passendes Modul oder eine passende Modulvariante verwendet werden.

## Content-Balance

- Bei Modulen mit `2` oder `3` nebeneinanderstehenden Spalten sollen die Textmengen pro Spalte moeglichst aehnlich lang sein.
- Exakte Zeichengleichheit ist nicht noetig, aber starke Laengenunterschiede zwischen parallelen Spalten sind zu vermeiden.
- Das Ziel ist ein ruhiges, ausgewogenes Layout ohne optisch ueberladene Einzelspalten.
- Diese Balance-Regel gilt besonders fuer `benefits-3col`, `teaser-2col-horizontal`, `teaser-2col-vertical`, `teaser-2col-alternating`, `teaser-2col-listing` und `table-comparison`.
- Fuer `table-comparison` gilt eine strengere Synchronitaet: beide Spalten-Headlines sollen moeglichst gleich viele Zeilen einnehmen, und die Inhalte eines Zeilenpaars links/rechts sollen in ihrer Laenge moeglichst nah beieinander liegen.
- Bei `table-comparison` sind Kombinationen zu vermeiden, bei denen eine Spalten-Headline einzeilig und die andere zweizeilig wird.
- Bei `table-comparison` sind Kombinationen zu vermeiden, bei denen eine Zelle eines Zeilenpaars sehr kurz und die gegenueberliegende Zelle deutlich laenger ist, weil die Vergleichbarkeit sonst visuell leidet.

## Export

- Export startet nur bei expliziter Anweisung wie `Exportiere die Mail zu Iterable`.
- Eine Preview-Anfrage, eine Template-Auswahl oder ein erfolgreicher Preview-Lauf sind fuer sich allein nie eine Export-Anweisung.
- Nach erfolgreicher Preview darf der Agent nicht selbststaendig in Richtung Iterable wechseln; ohne neue explizite Export-/Upload-/Update-Freigabe bleibt er im Preview-Modus.
- Exportziel ist immer genau eine konkrete Campaign pro fortgeschriebener Preview, nicht Draft und nicht die Template-Bibliothek.
- Preview-HTML ist nie die Export-Payload.
- `DEFAULT_TEMPLATE_ID = 569946`.
- Der CreateCampaign-Schritt ist ein harter Gate-Step und erfordert mindestens eine verwertbare `campaignId`.
- Der externe Export-Flow hat genau vier API-Schritte: `createCampaign`, genau einen `campaignRead` zum Holen der campaign-owned `templateId` und des `campaignState`, genau einen `templateRead` der aktuellen campaign-owned HTML-Shell und den finalen HTML-Write.
- Der CreateCampaign-Basispayload fuer den Builder-Export muss exakt `name` und `templateId` enthalten.
- `listIds`, `sendAt`, `scheduleSend`, `sendMode` und `recipientTimeZone` sind im CreateCampaign-Request des Builder-Exports verboten.
- Der Builder-Export darf keine Scheduling- oder Versandparameter an `createCampaign` uebergeben.
- Falls spaeter eine Versandliste benoetigt wird, ist das ein separater manueller Iterable-Schritt ausserhalb dieses Export-Flows.
- Wenn ein aktives Composition-Template genutzt wird, ist `templateId` im CreateCampaign-Request immer dessen `iterable_template_id` aus `agent/template-<template_id>.definition.json`.
- Wenn kein Composition-Template genutzt wird, ist `templateId` im CreateCampaign-Request immer `569946` aus `DEFAULT_TEMPLATE_ID`.
- Wenn ein aktives Composition-Template genutzt wird und `iterable_template_id = null` ist, darf kein Iterable-Export stattfinden.
- Das zugehoerige Iterable-Basistemplate fuer Composition-Templates liegt immer unter `email/templates/<template_id>.html`.
- Dieses Basistemplate darf keine festen Module und keine festen Snippet-Calls enthalten.
- Fuer `templateContext.mode = default_template` ist `email/templates/template-main.html` die einzige kanonische Repo-Referenz fuer die Default-Shell; andere `email/templates/*.html` sind in diesem Modus keine zulaessigen Ersatz- oder Fallback-Shells.
- Die aktive Basis-`templateId` darf nur im CreateCampaign-Call als Basis-Template verwendet werden.
- Nach dem Campaign-Read muss genau eine aktuelle campaign-owned HTML-Shell fuer diese `templateId` gelesen werden.
- Der finale CreateCampaign-Request ohne Secrets sowie HTTP-Status-Info, Raw-Response-Body-Info und die verwertbare Tool-Antwort-/Envelope-Info muessen bei jedem fehlgeschlagenen Call vollstaendig protokolliert werden.
- Bei erfolgreichem Create ist nur ein Minimal-Log mit `campaignId` und `name` erlaubt.
- Auf die CreateCampaign-Response muss explizit gewartet werden; ohne vollstaendig empfangene Response darf der Export nicht weiterlaufen.
- Eine verwertbare CreateCampaign-ID darf nur aus diesen Kandidaten extrahiert werden: `campaignId`, `id`, `response.campaignId`, `response.id`, `data.campaignId`, `data.id`, `campaign.campaignId`, `campaign.id`.
- Jeder Kandidat ist nur gueltig, wenn er als `number` oder `string` vorliegt.
- Die erste verwertbare extrahierte Campaign-ID muss intern als String normalisiert werden.
- `campaignId` darf nie als `templateId` behandelt werden.
- Direkt nach `createCampaign` ist genau ein `campaignRead` mit dieser `campaignId` erlaubt; daraus duerfen ausschliesslich `response.templateId` als campaign-owned `templateId` und `response.campaignState` fuer die Status-Validierung gelesen werden.
- Der Builder-Export darf nur mit explizit editierbarem `campaignState` fortfahren; `Ready` ist der bevorzugte erwartete Status nach `createCampaign`.
- Bei `Scheduled`, `Running`, `Finished`, `Archived`, `Recurring`, `Aborted` oder jedem anderen nicht explizit als editierbar belegten Status stoppt der Export vor dem HTML-Write.
- Der Write-Step darf nicht implizit sein.
- Der finale HTML-Write darf nur auf dem campaign-owned `templateId` der erzeugten oder bereits gebundenen Campaign laufen.
- Fuer den finalen HTML-Write ist ausschliesslich `POST /api/templates/email/update` erlaubt.
- Der Write-Payload muss exakt `templateId`, `html`, `subject` und `preheaderText` enthalten.
- `subject` und `preheaderText` sind vor dem Write Pflicht.
- Wenn keine campaign-owned `templateId` verfuegbar ist, darf kein Write gestartet werden.
- Wenn die CreateCampaign-Antwort leer, unparsebar, unvollstaendig oder ohne verwertbare extrahierbare Campaign-ID ist, endet der Export sofort.
- Ein CreateCampaign-Fehler muss klar klassifiziert werden als Tool-Runtime-/Envelope-Fehler, Iterable-API-Fehler oder Parser-Fehler.
- Wenn keine verwertbare Campaign-ID extrahierbar ist, muss die Fehlerausgabe exakt `Iterable createCampaign hat keine gueltige campaignId zurueckgegeben` enthalten und zusaetzlich den finalen Request ohne Secrets, die HTTP-Status-Info, die Raw-Response-Body-Info, die geprueften ID-Kandidaten, den Ablehnungsgrund und den Hinweis `Kein Campaign-Read und kein HTML-Write wurden ausgefuehrt.` mitliefern.
- Ohne `campaignId` sind HTML-Write und jeder weitere Exportschritt verboten.
- Nach einem fehlgeschlagenen Create ohne verwertbare `campaignId` darf derselbe Export nicht automatisch erneut gestartet werden.
- Ein neuer Exportversuch ist danach erst wieder zulaessig, wenn der User ihn erneut explizit freigibt.
- Weitere Template-Reads, Schedule, Send, Retry und nicht offiziell dokumentierte Status-Reset-Calls sind im Export verboten.
- Wenn der eine erlaubte `campaignRead` `campaignState = Scheduled` liefert, darf der finale HTML-Write nicht starten.
- Kein Status-Reset, kein Cancel, kein Archive und keine sonstige Reparatur einer nicht editierbaren Campaign per Agent.
- Jeder weitere Campaign-Read ausser diesem einen `campaignRead` fuer die campaign-owned `templateId` ist im Export verboten.
- Alternative Write-Methoden, alternative Write-Endpoints oder alternative Write-Payloads sind verboten.
- Nackte `SNIPPET_CALLS` duerfen nie als komplettes `html` geschrieben werden.
- Die gelesene campaign-owned HTML-Shell muss ausserhalb der erlaubten Replace-Zonen unveraendert bleiben.
- Eine freie Minimal-Shell oder lokal neu erfundene Shell als Write-Payload ist verboten.
- Die Default-Shell darf nie sinngemaess aus Prompt-Wissen, Tests, gekuerzten Wrapper-Beispielen oder template-fremden Shell-Dateien nachgebaut werden.
- Im finalen Shell-Merge duerfen nur Subject, Preheader und der Module-Slot ersetzt werden; Head, CSS, Media Queries, Wrapper-Struktur und Conditional Comments bleiben vollstaendig erhalten.
- Vor dem finalen Write muss lokal klar unterscheidbar sein, ob der Fehler im HTML-Build, in der Payload-Vollstaendigkeit oder erst im Iterable-Write liegt.
- Der finale HTML-Schritt endet nie mit einem unscharfen `HTML fehlgeschlagen`.
- Vor dem finalen Write laeuft genau eine kleine lokale Payload-Pruefung fuer Subject, Preheader, modularem Block, campaign-owned HTML-Shell und finale HTML-Payload.
- Wenn diese lokale Payload-Pruefung scheitert, wird kein Write versucht.
- Fuer bekannte Module gilt der direkte Fast-Path aus `builder-library.md`.
- Im Happy Path wird die letzte sichtbare Preview oder ihr direkt daraus abgeleiteter strukturierter Export-State genau einmal in die finale HTML-Payload uebersetzt.
- Wenn fuer die aktuelle fortgeschriebene Preview bereits eine verwertbare `campaignId` vorliegt, muss genau diese Campaign erneut beschrieben werden.
- Wenn fuer die aktuelle Preview noch keine `campaignId` vorliegt, darf genau eine neue Campaign erzeugt werden.
- Keine doppelte Uebersetzung, keine erneute lange Herleitung lokaler Pflichtwerte, keine Draft-Ausweichlogik und keine unnoetigen Nachschlage-Calls.
- Keine impliziten Reparaturversuche, kein Haengenbleiben und kein erneuter best-effort-Lauf im selben Export, wenn CreateCampaign keine verwertbare Antwort liefert.
- Kein Haengenbleiben und kein weiterer Folgeversuch im selben Export, wenn der finale HTML-Schritt lokal oder beim Write scheitert.
- Wenn ein Modul ausserhalb des Fast-Paths liegt oder Pflichtwerte fehlen, klar fehlschlagen statt teuer zu improvisieren.
- In allen generierten deutschen Texten sind echte Umlaute Pflicht: `ä`, `ö`, `ü`, `Ä`, `Ö`, `Ü`.
- Schreibungen wie `ae`, `oe`, `ue`, `Ae`, `Oe`, `Ue` sind als Umlaut-Ersatz verboten, ausser bei Eigennamen, URLs, E-Mail-Adressen oder technischen Werten.
- Diese Umlaut-Regel gilt fuer Modultexte, Preview-HTML, Template-Texte, Export-Inhalte und alle sonstigen generierten Strings.
- Umlaute duerfen im System nicht nachtraeglich umgewandelt, ASCII-normalisiert oder im Export transformiert werden.
- Vor jeder Ausgabe muessen generierte deutsche Texte auf `ae`, `oe` und `ue` als Umlaut-Ersatz geprueft und vor der Ausgabe direkt korrigiert werden.

## Antwortstil

- Kurze Statusmeldungen statt langer Erklaertexte.
- Nach erfolgreichem Preview- oder Export-Lauf keine Meta-Erklaerung ueber interne Schritte.
- Im normalen Antwortstil keine Datei-Dumps, HTML-Dumps oder aehnliche Vollausgaben ausgeben.
- Technische Debug-Details nur auf ausdrueckliche Anforderung des Users ausgeben.
- Wenn Information fehlt, triff eine kleine sichere Annahme statt Zusatzkomplexitaet aufzubauen.
```

## email-builder/agent/builder-library.md

Dateityp: md

```md
# Builder Library

Diese Datei enthaelt die fachliche Builder-Logik fuer Startkomposition, Pflichtmodule, Templates und Moduluebersicht.
Die technische Export-Wahrheit liegt in `export-map.json`.

## Agent-Upload-Bundle

- Fuer Custom-GPT-/Agent-Setups ist das Standard-Knowledge-Format eine einzelne gebuendelte Markdown-Datei mit exakten Repo-Pfadueberschriften als virtuelle Dateien.
- Der Standardordner dafuer ist `agent-upload/email-builder-agent/` mit `systemprompt.md` und `emb_knowledge.md`.
- `agent/` bleibt die kanonische Quelle; der Upload-Ordner ist nur das daraus abgeleitete Paket.
- Dieses Bundle muss die aktiven Kern-, Preview- und Export-Regeln, die Export-Basis, den Template-Contract, den `email_state`-Contract, die zentrale Salutation-Registry `product-salutations.json`, operative Icon- und Tonalitaetsquellen, `email/templates/template-main.html` sowie alle aktiven `template-<id>.definition.json`, `template-<id>.preview.html` und `email/templates/<id>.html` enthalten.
- Nach produktiven Aenderungen an Modulen, Templates, Regeldateien oder `export-map.json` muss das Bundle neu erzeugt werden.

## Typography-Regeln

- Nur Hero-Headlines duerfen im EMB groessenverstellbar sein.
- Erlaubte Hero-Groessen sind ausschliesslich `s`, `m` und `l`.
- Das Hero-Mapping folgt immer direkt den Typography-Tokens:
  - `s` = `heading-s`
  - `m` = `heading-m`
  - `l` = `heading-l`
- Der reguläre Hero-Default ist `l`.
- Nicht-Hero-Modulheadlines sind nicht usersteuerbar.
- Die erste sichtbare Hauptheadline eines Nicht-Hero-Moduls ist immer `heading-m`.
- Weitere Unter-Headlines, Abschnittstitel oder Zwischenueberschriften innerhalb eines Nicht-Hero-Moduls sind immer `heading-s`.
- Bodytexte bleiben standardmaessig `body-standard`.
- Freie Heading-Klassen, freie CSS-Werte, freie Font-Size-Werte, freies HTML oder freie Style-Werte sind fuer Typography-Steuerung nicht zulaessig.

## Composition-Templates

- Operative Composition-Templates liegen im flachen `agent/`-Ordner, aber immer namespacet ueber `template_id`.
- Die operativen Dateinamen werden immer aus `template_id` abgeleitet:
  - `template-<template_id>.definition.json`
  - `template-<template_id>.preview.html`
- Neue oder geaenderte Templates werden fuer die Pruefung in den Review-Dateien unter `development/review/` dargestellt.
- Review-Dateien sind reine Test-Artefakte und nie operative Builder- oder Export-Wahrheit.
- Review-Dateien duerfen fuer Template-Tests vollstaendig zusammengebaut sein und Demo-Content oder Beispielmodule enthalten.
- Der Ablauf bleibt immer: zuerst nur `development/review/preview-index.html` und `development/review/email-index.html` als Review-Entwurf aktualisieren, User-Freigabe einholen und erst danach operative Zielpfade oder zentrale Builder-/Template-Dokumentation anpassen.
- `development/templates/searcher-standard/*` bleibt bis zur finalen Prozessentscheidung als historischer Prozessbeleg erhalten, ist aber kein verpflichtender Startpunkt fuer neue Template-Arbeit.
- Ein Composition-Template ist nur aktiv nutzbar, wenn diese beiden Dateien vorhanden sind und der Status in `template-<template_id>.definition.json` auf `active` steht.
- Bei Template-Nutzung ist `template-<template_id>.preview.html` die visuelle Preview-Basis.
- `template-<template_id>.definition.json` ist die verbindliche Agent-Logik.
- Regeln duerfen niemals aus `template-<template_id>.preview.html` abgeleitet werden.
- Vorhandene CSS- und Asset-Links aus `template-<template_id>.preview.html` muessen bei Template-Nutzung unveraendert erhalten bleiben.
- Finale EMB-Previews duerfen dabei kein externes Design-Library- oder `preview/token-runtime.js`-Script laden; operative Template-Previews verlassen sich nur auf die EMB-Preview-CSS und statisch materialisierte Werte.
- Die Slot-Reihenfolge aus `template-<template_id>.definition.json` ist verbindlich.
- Neue Modultypen ausserhalb der Slots sind verboten.
- Entfernen oder Duplizieren ist nur erlaubt, wenn `template-<template_id>.definition.json` es erlaubt.
- Jedes Composition-Template braucht zusaetzlich ein eigenes Iterable-Basistemplate unter `email/templates/<template_id>.html`.
- Dieses Iterable-Basistemplate enthaelt nur E-Mail-Shell, benoetigtes CSS und Content-Einfuegepunkt, aber keine festen Module oder festen Snippet-Calls.
- Operative Template-Dateien duerfen nicht zu vollstaendig zusammengebauten Testmails oder Demo-Templates umgebaut werden.
- Vollstaendig zusammengebaute Preview- oder E-Mail-Tests fuer Templates gehoeren ausschliesslich in `development/review/preview-index.html` und `development/review/email-index.html`.
- Ohne ausdrueckliche User-Freigabe des aktuellen Review-Stands duerfen weder operative Template-Zielpfade wie `agent/template-<template_id>.*` und `email/templates/<template_id>.html` noch zentrale Anschlussdateien wie `agent/builder-library.md`, Template-Uebersichten oder weitere Library-Dateien angepasst werden.
- Nach ausdruecklicher User-Freigabe erfolgt die Template-Integration direkt in den operativen Zielpfaden:
  - `agent/template-<template_id>.definition.json`
  - `agent/template-<template_id>.preview.html`
  - `email/templates/<template_id>.html`
- Relevante Library- oder Regeldateien werden dabei nur bei konkretem Bedarf nachgezogen; pauschale Anschlussaenderungen sind verboten.
- Die Review-Dateien koennen nach der Integration als finaler Teststand aktualisiert werden, bleiben aber reine Test-Artefakte und nie operative Builder-Wahrheit.
- Aktuell bekanntes aktives Composition-Template:
  - `loft-snl`
    - `template-loft-snl.definition.json`
    - `template-loft-snl.preview.html`
    - Iterable Template-ID `615576`
    - Preview-first bleibt Pflicht; Iterable-Export startet erst nach expliziter User-Freigabe.
  - `loft-rnl-dev`
    - `template-loft-rnl-dev.definition.json`
    - `template-loft-rnl-dev.preview.html`
    - Iterable Template-ID `618734`
    - Preview-first bleibt Pflicht; Iterable-Export startet erst nach expliziter User-Freigabe.
  - `loft-regio-resi`
    - `template-loft-regio-resi.definition.json`
    - `template-loft-regio-resi.preview.html`
    - Iterable Template-ID `619002`
    - Preview-first bleibt Pflicht; Iterable-Export startet erst nach expliziter User-Freigabe.

- Editable Starter Blueprints:
  - `standard-blueprint`
  - `ho-esg` (`Homeowner | ESG`)
    - Fast-Path-Preview: `starter-ho-esg.preview.html`
    - Fast-Path-State: `starter-ho-esg.state.json`
  - `seeker-mle` (`Seeker | MLE`)
    - Fast-Path-Preview: `starter-seeker-mle.preview.html`
    - Fast-Path-State: `starter-seeker-mle.state.json`

## Startlogik

Der initiale Creation-Mode ist geschlossen.

Nutze beim allerersten Start genau diese Reihenfolge:

1. Explizit angefordertes Fixed Composition Template oder dokumentierter Starter Blueprint
2. Standard-Blueprint

- Der freie Blueprint-Start darf nur Module verwenden, die in `preview-module-library.md` und `preview-modules.html` vorhanden sind.
- Im Bootstrap-Start darf Preview, Composition oder Builder-State noch fehlen.
- Mit dem ersten erfolgreichen Preview-Render wird die Startkomposition zur aktuellen Composition.
- Mit jedem erfolgreichen Preview-Render wird parallel ein strukturierter `email_state` aktualisiert.
- Wenn der User explizit ein bekanntes Fixed Composition Template oder einen dokumentierten Starter Blueprint anfordert, gewinnt diese Startoption vor dem Standard-Blueprint.
- Aktive Composition-Templates sind aktuell nur:
  - `loft-snl`
  - `loft-rnl-dev`
  - `loft-regio-resi`
- Dokumentierte editable Starter Blueprints sind aktuell nur:
  - `ho-esg`
  - `seeker-mle`
- Die Wahl eines Composition-Templates bestimmt nur die Startkomposition und bedeutet nie automatisch Export oder Iterable-Update.
- Ein Starter Blueprint verhaelt sich wie der Standard-Blueprint: feste Erstkomposition, feste Defaults, `default_template`-Flow, direkte erste Preview, danach freie Iteration.
- Wenn der User `Create from scratch`, `from scratch`, `blank`, `frei starten` oder ohne Template-Vorgabe eine neue Mail starten will, startet der normale Mail-Flow immer sofort mit dem Standard-Blueprint.
- Fuer diesen freien Initialstart sind keine Rueckfragen zu Produkt, Thema, Ziel, Tonalitaet oder Inhalt erlaubt; die erste Preview nutzt neutrale Blindtexte und bestehende Moduldefaults.
- Fuer `Start mit Blueprint`, `Create from scratch`, `from scratch`, `blank`, `frei starten` oder sinngemaess freien Start nutzt der Agent als einzige sichtbare Startnachricht: `Ich starte nun mit dem Blueprint-Aufbau und erstelle die erste Vorschau.`
- Wenn der User `Start mit Template`, `Choose template` oder sinngemaess eine Template-Auswahl anfragt, baut der Agent noch keine freie Mail, sondern sagt genau oder sinngemaess:
  - `Bitte nenne mir die Nummer des Templates, mit dem du starten möchtest:`
  - `1. Loft | SNL`
  - `2. Loft | RNL (Dev)`
  - `3. Loft | Regio (Resi)`
  - `4. Homeowner | ESG`
  - `5. Seeker | MLE`
- Internes Template-Mapping fuer die Start-UX:
  - `1` oder `Loft | SNL` oder `loft-snl` -> `loft-snl` -> `template-loft-snl.preview.html`
  - `2` oder `Loft | RNL (Dev)` oder `loft-rnl-dev` -> `loft-rnl-dev` -> `template-loft-rnl-dev.preview.html`
  - `3` oder `Loft | Regio (Resi)` oder `loft-regio-resi` -> `loft-regio-resi` -> `template-loft-regio-resi.preview.html`
  - `4` oder `Homeowner | ESG` oder `ho-esg` -> Starter Blueprint `ho-esg`
  - `5` oder `Seeker | MLE` oder `seeker-mle` -> Starter Blueprint `seeker-mle`
- Wenn der User `1`, `2`, `3`, `4`, `5`, einen Anzeigenamen oder die technische ID nennt, startet der Agent direkt mit diesem Template und nutzt als sichtbaren Startsatz: `Ich starte nun mit dem Template „<Anzeigename>“ und erstelle die erste Vorschau.`
- Beim allerersten Start eines aktiven Composition-Templates ist ausschliesslich die jeweilige `template-<template_id>.preview.html` die visuelle Quelle.
- In diesem initialen Template-Start sind freie Modulplanung, Einzelmodulsuche, Modulrekonstruktion, generische Ersatzmodule und `preview-modules.html` als primaere visuelle Quelle verboten.
- Starter Blueprints nutzen keine `template-*.preview.html`, keine Composition-Template-Pruefung und keine neue Copy-Generierung.
- Wenn fuer einen Starter Blueprint ein fertiges `starter-<id>.preview.html` und `starter-<id>.state.json` vorliegen, uebernimmt der Agent diese beiden Artefakte direkt als erste Preview und als ersten State.
- Fuer `ho-esg` sind diese Fast-Path-Artefakte die einzige kanonische Quelle fuer:
  - die erste sichtbare Preview
  - die feste Erstkomposition
  - die festen Preset-Texte
  - die vier aufgeloesten `servicetiles`-Services `ELE`, `NDG`, `EA48`, `KWATT`
- Beim `ho-esg`-Start darf der Agent deshalb weder Module neu zusammensuchen noch Services neu aufloesen noch die erste Copy neu formulieren.
- Fuer `seeker-mle` sind diese Fast-Path-Artefakte die einzige kanonische Quelle fuer:
  - die erste sichtbare Preview
  - die feste Erstkomposition
  - die festen Preset-Texte
  - die feste Modulfolge `logo-centered`, `hero-fakeform-buttons-image`, `benefits-3col`, `teaser-1col`, `contact-signoff`, `footer`
- Beim `seeker-mle`-Start darf der Agent deshalb weder Module neu zusammensuchen noch die erste Copy neu formulieren.
- Dieser Starter Blueprint ist kein Composition-Template:
  - `templateContext.mode = default_template`
  - `templateContext.resolvedBaseTemplateId = 569946`
  - kein `compositionTemplateId`
  - kein `iterableTemplateId`
- Beim Start von Templates oder Starter Blueprints gibt der Agent nie HTML, Quelltext, sichtbaren State oder Modulmarkup im Chat aus; er sendet nur den kurzen Startsatz und erstellt dann direkt die Preview im Canvas.
- Erst nach der ersten erfolgreichen Template-Preview gelten fuer Modul-Aenderungen wieder die normalen Source-Fidelity-Regeln ueber bestehende Modulquellen.
- Wenn der User beim allerersten Start nur eine freie Modulliste nennt, darf diese Struktur noch nicht direkt gebaut werden; der Agent klaert kurz, ob mit dem Standard-Blueprint oder einem aktiven Composition-Template gestartet werden soll.
- Erst nach dem ersten erfolgreichen Preview-Render darf die bestehende Mail frei um Module erweitert, reduziert, ersetzt oder umsortiert werden.

## Salutation-Kontext

- Die zentrale Registry fuer Anrede-Zuordnungen ist `agent/product-salutations.json`.
- `salutationContext` ist ein eigener Resolver-Kontext fuer Anrede-Logik und getrennt von `templateContext` und vom inhaltlichen Produktkontext.
- Der Resolver arbeitet in genau dieser Reihenfolge:
  1. `salutation_context_id` des aktiven Composition-Templates
  2. explizite User-Nennung ueber `aliases` oder `template_ids` aus `agent/product-salutations.json`
  3. freier Initialstart ohne erkennbare Zuordnung -> `generic`
  4. spaetere explizite User-Nennung oder eindeutige Iteration darf den Kontext weiter verfeinern
- Wenn ein Template eine `salutation_context_id` traegt, wird `salutationContext` automatisch gesetzt; es ist keine Rueckfrage noetig.
- Direkte User-Angaben wie `Mail fuer RLE` oder `Newsletter fuer Loft RNL` muessen ueber die Registry ohne unnoetige Rueckfrage aufgeloest werden.
- `mode = template_builtin` bedeutet: bestehende template- oder snippet-spezifische Anrede-Logik weiterverwenden.
- Eine dokumentierte Ausnahme ist erlaubt, wenn `agent/product-salutations.json` fuer einen bestehenden Template-Kontext genau ein kontrolliertes Feld-Override definiert, das keinen freien User-Raw-Code eroeffnet.
- `mode = hero_snippet_flag` bedeutet: nur das bestehende Hero-Pattern mit sichtbarer Preview-Anrede und technischem Export-Flag nutzen.
- `mode = plain_default` bedeutet: sichtbare Preview-Anrede aus `preview_default`, keine Spezial-Exportlogik.

## Pflichtmodule

- Standard: `logo`, `hero-image-top`, `footer`
- Logo steht immer an Position `1`.
- Hero steht immer an Position `2`.
- Footer steht immer an letzter Position.
- Wenn die finale Modulfolge eines der Center-Hero-Module `hero-image-top-center`, `hero-image-top-bleed-center`, `hero-cta-top-center`, `hero-cta-top-no-bottom-center`, `hero-image-head-copy-bleed-center`, `hero-image-textbox-cta-center` oder `hero-fakeform-buttons-image` enthaelt, muss das Pflicht-Logo an Position `1` als `logo-centered` statt `logo` aufgeloest werden.
- Diese Logo-Normalisierung aendert nur das Logo-Modul; die Reihenfolge der Mail bleibt unveraendert.

## Hintergrund-Rhythmus

- Der Hintergrund-Rhythmus wird erst angewendet, nachdem die finale Modulfolge feststeht und alle Pflichtmodule korrekt eingesetzt wurden.
- Die verbindliche technische Farbquelle fuer die Rhythmus-Aufloesung ist `agent/preview-styles.css`.
- Dort gelten fuer den produktiven Hintergrund-Rhythmus genau diese Flaechenwerte:
  - weiss / white = `#FFFFFF` aus `--surface-white`
  - grau / gray = `#F5F5F5` aus `--surface-gray`
- Alle Hero-Varianten haben immer weissen Hintergrund.
- `logo`, `footer`, `contact` und `contact-signoff` haben immer weissen Hintergrund.
- `logo`, `footer`, `contact` und `contact-signoff` sind feste Struktur-/Utility-Module und nehmen nicht an der Hintergrund-Alternierung teil.
- Footer hat immer weissen Hintergrund.
- Standardfall:
  - Das erste Modul nach dem Hero hat immer grauen Hintergrund.
  - Das zweite Modul nach dem Hero hat immer weissen Hintergrund.
  - Danach wechseln die Modulhintergruende strikt weiter grau, weiss, grau, weiss.
- Ausnahme `hero-cta-top-no-bottom`:
  - Das erste Modul nach diesem Hero hat immer weissen Hintergrund.
  - Das zweite Modul nach diesem Hero hat immer grauen Hintergrund.
  - Danach wechseln die Modulhintergruende strikt weiter weiss, grau, weiss, grau.
- Diese Hintergrundfolge gilt fuer die gesamte Modul-Komposition und darf nicht aus statischen Moduldefaults frei uminterpretiert werden.
- User-Wuensche zur Modulreihenfolge duerfen die Hintergrundfolge nur indirekt ueber die finale Modulposition beeinflussen; der Rhythmus selbst ist nicht frei ueberschreibbar.
- Nach Einfuegen, Entfernen oder Umsortieren von Content-Modulen muss der komplette Hintergrund-Rhythmus fuer die gesamte finale Modulfolge neu materialisiert werden.
- Bei Preview- und State-Erstellung muss dieser Rhythmus vor dem Mitschreiben in `email_state.content` immer in konkrete Hexwerte aufgeloest werden.
- `theme-white`, `theme-gray` oder andere Preview-Klassen sind nur visuelle Preview-Hilfen und nie zulaessige Exportwerte fuer `email_state.content`.
- Wenn fuer ein Modul mit required `*_bg_color` kein konkreter Hexwert aus dieser verbindlichen Farbquelle aufloesbar ist, gilt die Preview als nicht exportfaehig und der Agent muss stoppen.

## Standard-Blueprint

Modulfolge:

1. `logo`
2. `hero-image-top`
3. `steps-3col`
4. `footer`

Inhalt fuer den ersten Entwurf:

- Subject: neutraler Blindtext in einem Satz
- Preheader: neutrale kurze Ergaenzung zum Subject
- Hero: neutrale Blindtext-Headline, kurzer neutraler Einstieg und CTA `Mehr erfahren`
- `steps-3col`: drei kurze neutrale Blindtext-Schritte plus CTA mit bestehendem Standardziel

Wenn kein Thema genannt ist:

- neutrale Blindtexte oder lorem-ipsum-nahe Platzhalter verwenden
- keine Rueckfragepflicht fuer den ersten Wurf
- Fuer Demo-CTAs ohne explizites User-Ziel die kanonische Standard-URL `https://www.immobilienscout24.de/` verwenden.

## Direkte User-Module

- Diese Regeln gelten erst nach der ersten erfolgreichen Preview oder wenn eine bestehende Preview fortgeschrieben wird.
- Vor der ersten Preview ist freie Modulwahl nicht erlaubt; dann gilt ausschliesslich die geschlossene Startlogik aus `## Startlogik`.
- Bei bestehenden Preview-Modulen darf nach der Auswahl des passenden `data-module`-Blocks aus `agent/preview-modules.html` nur Feldinhalt ersetzt werden; Wrapper, Klassen, Responsive-Klassen, Tabellenstruktur und Inline-Styles bleiben unveraendert.
- Umliegende bereits korrekt gesetzte Module bleiben bei spaeteren Aenderungen zustandsbasiert erhalten und duerfen nicht aus aehnlichen Modulen oder Beschreibungen neu konstruiert werden.
- Bei direkter Modulliste die User-Reihenfolge uebernehmen.
- Fehlende Pflichtmodule automatisch ergaenzen.
- Allgemeine Mails nutzen `logo`.
- Center-Hero-Mails nutzen als Logo-Variante `logo-centered`.
- Eine unspezifische `hero`-Anforderung wird immer als `hero-image-top` aufgeloest.
- Bei Hero-Strukturwuenschen immer die passende feste Hero-Variante einsetzen und das Modul austauschen.
- Im Hero sind keine freie Umordnung und keine interne Variantenlogik zulaessig.
- `Bild nach unten` bedeutet Wechsel zu `hero-cta-top`.
- `Bleed` bedeutet Wechsel zu `hero-image-top-bleed`.
- `Bild oben und zentriert` bedeutet Wechsel zu `hero-image-top-center`.
- `Bleed und zentriert` bedeutet Wechsel zu `hero-image-top-bleed-center`.
- `Bild zuerst, zentriert und Bleed` bedeutet Wechsel zu `hero-image-head-copy-bleed-center`.
- `Bild nach unten und zentriert` bedeutet Wechsel zu `hero-cta-top-center`.
- `Bild nach unten ohne unteren Abschluss` bedeutet Wechsel zu `hero-cta-top-no-bottom`.
- `Bild nach unten ohne unteren Abschluss und zentriert` bedeutet Wechsel zu `hero-cta-top-no-bottom-center`.
- Wenn die finale Modulfolge eines der Center-Hero-Module `hero-image-top-center`, `hero-image-top-bleed-center`, `hero-cta-top-center`, `hero-cta-top-no-bottom-center`, `hero-image-head-copy-bleed-center`, `hero-image-textbox-cta-center` oder `hero-fakeform-buttons-image` enthaelt oder eine bestehende Hero-Variante dorthin gewechselt wird, muss ein vorhandenes `logo` an derselben Position zu `logo-centered` normalisiert werden.
- Wenn in diesem Center-Hero-Kontext bereits `logo-centered` vorhanden ist, darf kein zweites Logo eingefuegt werden.
- Wenn in diesem Center-Hero-Kontext kein Logo vorhanden ist, greift nur die normale Pflichtmodul-Ergaenzung mit `logo-centered`; ausserhalb eines Center-Hero-Kontexts bleibt `logo` regulaer zulaessig.
- Pflicht-Ergaenzung:
  - fehlendes Logo an Position `1`
  - fehlendes `hero-image-top` an Position `2`
  - fehlender Footer an letzter Position

## Unterstuetzte Builder-Module

| Builder-Modul | Iterable-Snippet |
| --- | --- |
| `logo` | `emb_logo` |
| `logo-centered` | `emb_logo_centered` |
| `hero-image-top` | `emb_hero_image_top` |
| `hero-image-top-center` | `emb_hero_image_top_center` |
| `hero-image-top-bleed` | `emb_hero_image_top_bleed` |
| `hero-image-top-bleed-center` | `emb_hero_image_top_bleed_center` |
| `hero-image-head-copy-bleed-center` | `emb_hero_image_head_copy_bleed_center` |
| `hero-image-textbox-cta-center` | `emb_hero_image_textbox_cta_center` |
| `hero-fakeform-buttons-image` | `emb_hero_fakeform_buttons_image` |
| `hero-cta-top` | `emb_hero_cta_top` |
| `hero-cta-top-center` | `emb_hero_cta_top_center` |
| `hero-cta-top-no-bottom` | `emb_hero_cta_top_no_bottom` |
| `hero-cta-top-no-bottom-center` | `emb_hero_cta_top_no_bottom_center` |
| `teaser-1col` | `emb_teaser_1col` |
| `loft-snl-copy-cta` | `emb_loft_snl_copy_cta` |
| `loft-snl-copy-sections-cta` | `emb_loft_snl_copy_sections_cta` |
| `loft-rnl-dev-intro` | `emb_loft_rnl_dev_intro` |
| `loft-rnl-dev-teaser-1col` | `emb_loft_rnl_dev_teaser_1col` |
| `loft-regio-resi-intro` | `emb_loft_regio_resi_intro` |
| `loft-regio-resi-teaser-1col` | `emb_loft_regio_resi_teaser_1col` |
| `teaser-2col-horizontal` | `emb_teaser_2col_horizontal` |
| `teaser-2col-vertical` | `emb_teaser_2col_vertical` |
| `teaser-2col-alternating` | `emb_teaser_2col_alternating` |
| `teaser-2col-listing` | `emb_teaser_2col_listing` |
| `teaser-2col-gallery` | `emb_teaser_2col_gallery` |
| `benefits-3col` | `emb_benefits_3col` |
| `servicetiles` | `emb_servicetiles` |
| `steps-3col` | `emb_steps_3col` |
| `steps-horizontal` | `emb_steps_horizontal` |
| `table` | `emb_table` |
| `table-comparison` | `emb_table_comparison` |
| `contact` | `emb_contact` |
| `contact-signoff` | `emb_contact_signoff` |
| `footer` | `emb_footer_marketing` |

Bewusst nicht angebunden:

- `servicetiles-4up`

## Service Products Registry

- Die zentrale Produktquelle fuer das spaetere Modul `servicetiles` ist `agent/service-products.json`.
- Diese Registry enthaelt pro Service genau:
  - `id`
  - `original_snippet_name`
  - `aliases`
  - `title`
  - `description`
  - `icon_url`
  - `target_url`
- User nennen im EMB fachlich genau `4` Services; die Aufloesung erfolgt nur ueber `id` oder `aliases` der Registry.
- Wenn weniger oder mehr als `4` Services genannt werden, muss der Agent nachfragen statt still zu normalisieren.
- Wenn ein genannter Service nicht eindeutig in `agent/service-products.json` vorhanden ist, muss der Agent nachfragen und darf nicht raten.
- Die bestehenden `servicetile_*`-Snippets bleiben nur Migrations- und Datenquelle; sie sind nicht das technische Zielmodell des spaeteren `servicetiles`-Moduls.
- User sehen im regulaeren EMB-Flow keine Iterable-Snippetnamen.

## CTA-Button-Typen

- Kanonische Button-Namen im EMB sind:
  - `button-filled-brand`
  - `button-filled-default`
  - `button-outline-strong`
  - `button-outline-weak`
- Bedeutung:
  - `button-filled-brand`: gefuellter Mint-Button
  - `button-filled-default`: gefuellter Charcoal-Button
  - `button-outline-strong`: Outline-Button mit dunkler Kontur
  - `button-outline-weak`: Outline-Button mit heller Kontur
- `teaser-link` und `contact-link` sind keine Buttons.
- Die alten technischen Klassennamen `button`, `button--outline` und `button--outline-soft` sind nur Legacy-Aliasse und sollen im EMB nicht mehr als kanonische Namen verwendet werden.
- Pro Mail ist genau ein primaerer `button-filled-brand` vorgesehen.
- Wenn ein Hero-Modul einen Button-CTA hat, ist dieser Hero-CTA immer der primaere `button-filled-brand`.
- Fuer Nicht-Hero-Button-CTAs bleibt der Preview-Default `button-outline-strong`.
- Wenn eine Mail ausnahmsweise keinen Hero-Button hat, darf stattdessen genau ein anderer primaerer CTA `button-filled-brand` sein.

## Produktkontext

- Produktkontext ist eine fachliche Start-Default-Logik fuer Inhalte und getrennt von `templateContext` und `salutationContext`.
- `salutationContext` kann ueber `agent/product-salutations.json` mehr Kontexte kennen als der Produktkontext; zusaetzliche Inhaltsdefaults duerfen trotzdem nur aus dokumentierten Produkt-Resolvern kommen.
- Produktkontext darf nur dann aktiviert werden, wenn der User am Chat-Anfang explizit ein Produkt nennt, zum Beispiel `Erstelle ein Mailing fuer RLE`, `Produkt: RLE` oder `fuer rle`.
- Die Erkennung ist strikt case-insensitive, aber nur fuer diesen einen dokumentierten Produktnamen erlaubt:
  - `RLE` -> normalisiert zu `RLE`
- `RLE` steht fuer `Realtor Lead Engine`, aber der ausgeschriebene Name ist aktuell keine zusaetzliche Resolver-Form.
- Weitere Produktnamen, aehnliche Schreibweisen oder freie Produktableitungen sind fuer Produktdefaults verboten.
- Wenn der User explizit einen unbekannten Produktnamen nennt, muss der Agent nachfragen statt zu raten.
- Wenn kein Produkt genannt wird, bleiben die neutralen EMB-Defaults aktiv.
- Produktdefaults sind nur Start-Defaults.
- Wenn der User spaeter konkrete Werte fuer Hero-Salutation, Contact-Felder oder andere Inhalte vorgibt, haben diese User-Vorgaben immer Vorrang.

### `RLE`

- Normalisierter Produktkontext: `RLE`
- Produktname: `Realtor Lead Engine`
- Wenn `RLE` explizit als Produkt genannt oder ueber `salutationContext = rle` aufgeloest wurde, bleibt die Preview-Hero-Anrede in allen elf Hero-Modulen die normale sichtbare Vorschau-Anrede:
  - `Hallo Anrede,`
- Export-Ziel fuer die Hero-Anrede ist fuer `RLE` genau dieser whitelisted Iterable-Logik-Block:
  - `{{#ifContainsStr firstName 'NULL'}} Hallo, {{else if firstName}} Hallo {{firstName}}, {{else}} Hallo, {{/ifContainsStr}}`
- Dieser Export-Zielwert bleibt export-only.
- In der Preview bleibt `*_salutation` sichtbarer Plain Text; fuer RLE wird stattdessen pro Hero-Modul nur das technische Export-Flag `*_use_snippetcall_salutation = true` materialisiert.
- Wenn ein `contact`-Modul in der Mail vorkommt und der User keine abweichenden Contact-Werte vorgibt, muessen diese RLE-Defaults in die bestehenden Contact-Felder materialisiert werden:
  - `emb_contact_show_image` = `true`
  - `emb_contact_image_url` = `https://library.eu.iterable.com/33/98/732ff156cb6b4fc188b76f0e07b2744e-avatar-woman.png`
  - `emb_contact_image_alt` = `Beraterin aus dem ImmoScout24-Team`
  - `emb_contact_headline` = `Hast Du noch Fragen?`
  - `emb_contact_body_intro` = `Unser Experten-Team berät dich gern:`
  - `emb_contact_phone` = `030 24 301 1361`
  - `emb_contact_phone_hours` = `Mo-Fr. von 09:00 - 20:00 Uhr`
  - `emb_contact_email_intro` = `Oder du schreibst uns:`
  - `emb_contact_email_address` = `immobilienberatung@scout24.com`
  - `emb_contact_email_url` = `mailto:immobilienberatung@scout24.com`
  - `emb_contact_closing_line_1` = `Freundliche Grüße`
  - `emb_contact_closing_line_2` = `Dein ImmoScout24-Team`
- Fuer RLE muessen bei Hero-Modulen zusaetzlich diese technischen Export-Flags auf `true` gesetzt werden, wenn die Hero-Anrede sichtbar bleibt:
  - `emb_hero_image_top_use_snippetcall_salutation`
  - `emb_hero_image_top_center_use_snippetcall_salutation`
  - `emb_hero_image_top_bleed_use_snippetcall_salutation`
  - `emb_hero_image_top_bleed_center_use_snippetcall_salutation`
  - `emb_hero_image_head_copy_bleed_center_use_snippetcall_salutation`
  - `emb_hero_image_textbox_cta_center_use_snippetcall_salutation`
  - `emb_hero_cta_top_use_snippetcall_salutation`
  - `emb_hero_cta_top_center_use_snippetcall_salutation`
  - `emb_hero_cta_top_no_bottom_use_snippetcall_salutation`
  - `emb_hero_cta_top_no_bottom_center_use_snippetcall_salutation`

## Export-Ready Resolver

- Ein `email_state` ist nur export-ready, wenn der aktive Template-Kontext bereits vor dem Export eindeutig im State festgehalten wurde.
- Freier Modulbau und Blueprint-Mails nutzen immer:
  - `templateContext.mode = default_template`
  - `templateContext.resolvedBaseTemplateId = 569946`
- Editable Starter Blueprints wie `ho-esg` oder `seeker-mle` nutzen ebenfalls immer:
  - `templateContext.mode = default_template`
  - `templateContext.resolvedBaseTemplateId = 569946`
  - kein `compositionTemplateId`
  - kein `iterableTemplateId`
- Composition-Templates nutzen immer:
  - `templateContext.mode = composition_template`
  - `templateContext.compositionTemplateId = <template_id>`
  - `templateContext.iterableTemplateId = <iterable_template_id>`
  - `templateContext.resolvedBaseTemplateId = <iterable_template_id>`
- Diese Template-Kontextwerte muessen beim Preview-Bau oder spaetestens beim direkten State-Mitschreiben gesetzt werden, nicht erst im Export.
- Exportrelevante technische Resolver duerfen nur aus dokumentierten Quellen kommen:
  - Hintergrund-Rhythmus aus diesem Dokument plus `agent/preview-styles.css`
  - Icon-Auswahl aus `icon-library.md`
  - finale Button-Farbwerte aus diesem Dokument
- Wenn ein required Feld weder im `email_state.content` steht noch einen eindeutigen Default in `export-map.json` hat noch aus einer dokumentierten technischen Resolver-Quelle konkret aufgeloest werden kann, ist der State nicht export-ready.

## Button-Farbaufloesung

- Wenn ein Modul required Button-Farbwerte fuer den Export braucht, muessen diese bereits beim Preview-Bau konkret in `email_state.content` stehen.
- Die Aufloesung erfolgt ausschliesslich aus dem kanonischen Button-Typ:
  - `button-filled-brand` -> `bg_color = #74FFDF`, `border_color = #74FFDF`
  - `button-filled-default` -> `bg_color = #333333`, `border_color = #333333`
  - `button-outline-strong` -> `bg_color = #FFFFFF`, `border_color = #333333`
  - `button-outline-weak` -> `bg_color = #FFFFFF`, `border_color = #D9D9D9`
- Diese Aufloesung ist eine technische Resolver-Regel fuer den `email_state`, kein Freiraum fuer den Export, spaeter aus Klassen oder sichtbarem Styling zu raten.

## Export-Basis

- Freie oder Blueprint-Mails nutzen das Basis-Template `569946`.
- `Exportiere die Mail zu Iterable` nutzt fuer die aktuelle Preview immer genau die bereits zu dieser Preview gehoerende Campaign oder erzeugt beim ersten Export genau eine neue Campaign auf Basis des festen Iterable-Basis-Templates.
- Draft ist kein Standard- und kein Fallback-Ziel.

## Technische Export-Hinweise

- Der technische Export nutzt den parallel gefuehrten `email_state` und `export-map.json`.
- `export-map.json` ist die einzige technische Quelle fuer:
  - erlaubte Module
  - Snippet-Namen
  - erlaubte Feldnamen
  - Feldtypen
  - Required/Optional
  - Defaults
- Der Export arbeitet im Happy Path nicht aus Preview-HTML oder Snippet-HTML.
- Der Export nutzt nur den parallel gefuehrten `email_state`.
- Unknown Fields sind Export-Fehler.
- Felder ohne Content und ohne Default werden nicht frei erfunden.
- Detaillierte Export- und Shell-Logik steht in `export-rules.md`.

## Modulhinweise

### `logo`

- Snippet: `emb_logo`
- Statisches Snippet ohne Export-Parameter.

### `logo-centered`

- Snippet: `emb_logo_centered`
- Pflicht-Logo, wenn die Mail eines der Center-Hero-Module `hero-image-top-center`, `hero-image-top-bleed-center`, `hero-cta-top-center`, `hero-cta-top-no-bottom-center`, `hero-image-head-copy-bleed-center`, `hero-image-textbox-cta-center` oder `hero-fakeform-buttons-image` enthaelt.
- Nur verwenden, wenn das Standard-Logo zentriert statt linksbuendig erscheinen soll.
- Statisches Snippet ohne Export-Parameter.

### Hero-Module

- `hero-image-top`, `hero-image-top-center`, `hero-image-top-bleed`, `hero-image-top-bleed-center`, `hero-image-head-copy-bleed-center`, `hero-image-textbox-cta-center`, `hero-fakeform-buttons-image`, `hero-cta-top`, `hero-cta-top-center`, `hero-cta-top-no-bottom` und `hero-cta-top-no-bottom-center` sind feste Varianten.
- Hero-Strukturwuensche werden nur durch Modultausch geloest, nie durch internes Umordnen.
- `preheadline` und Badge sind gegenseitig exklusiv.
- Alle elf Hero-Module nutzen fuer die optionale Anrede vor dem Body denselben Feldvertrag:
  - `emb_<hero>_show_salutation`
  - `emb_<hero>_use_snippetcall_salutation`
  - `emb_<hero>_salutation`
  - Default ist immer `show_salutation = true` und `salutation = Hallo Anrede,`
  - Die Hero-Anrede ist ein eigener Plain-Text-Block vor dem Body und wird nie in das `rich_*`-Body-Feld integriert.
- `use_snippetcall_salutation` ist ausschliesslich ein technisches Export-Flag fuer freigegebene Produktkontexte wie `RLE`; freie User-Raw-Logik bleibt verboten.
- Fehlende echte Bild-URL nutzt den passenden Hero-Placeholder aus dem technischen Mapping.

### `hero-image-top`

- Snippet: `emb_hero_image_top`
- Verbindlicher Snippet-Call-Vertrag: genau 20 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_image_top_bg_color`
  - `emb_hero_image_top_show_preheadline`
  - `emb_hero_image_top_preheadline`
  - `emb_hero_image_top_show_badge`
  - `emb_hero_image_top_badge_bg_color`
  - `emb_hero_image_top_badge_text_color`
  - `emb_hero_image_top_badge_label`
  - `emb_hero_image_top_show_small_headline`
  - `emb_hero_image_top_show_large_headline`
  - `emb_hero_image_top_headline`
  - `emb_hero_image_top_image_url`
  - `emb_hero_image_top_image_alt`
  - `emb_hero_image_top_show_salutation`
  - `emb_hero_image_top_use_snippetcall_salutation`
  - `emb_hero_image_top_salutation`
  - `emb_hero_image_top_body`
  - `emb_hero_image_top_button_url`
  - `emb_hero_image_top_button_bg_color`
  - `emb_hero_image_top_button_border_color`
  - `emb_hero_image_top_button_label`
- Headline-Groessenvariante:
  - `emb_hero_image_top_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_image_top_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_image_top_show_small_headline = true` und `emb_hero_image_top_show_large_headline = false`
    - `m` => `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = false`
    - `l` => `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_image_top_headline_size = l`, `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = true` erzeugen.
  - `emb_hero_image_top_show_large_headline` ist nur noch ein Legacy-/Bridge-Feld; wenn es ohne kanonisches `headline_size` auf `true` steht, wird zu `headline_size = l` normalisiert, sonst zu `headline_size = m`.
  - `emb_hero_image_top_show_small_headline = true` und `emb_hero_image_top_show_large_headline = true` gleichzeitig sind ungueltig und muessen fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### `hero-image-top-center`

- Snippet: `emb_hero_image_top_center`
- Layout: Eyebrow oder Badge, Headline, Anrede, Body und CTA sind zentriert.
- Verbindlicher Snippet-Call-Vertrag: genau 20 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_image_top_center_bg_color`
  - `emb_hero_image_top_center_show_preheadline`
  - `emb_hero_image_top_center_preheadline`
  - `emb_hero_image_top_center_show_badge`
  - `emb_hero_image_top_center_badge_bg_color`
  - `emb_hero_image_top_center_badge_text_color`
  - `emb_hero_image_top_center_badge_label`
  - `emb_hero_image_top_center_show_small_headline`
  - `emb_hero_image_top_center_show_large_headline`
  - `emb_hero_image_top_center_headline`
  - `emb_hero_image_top_center_image_url`
  - `emb_hero_image_top_center_image_alt`
  - `emb_hero_image_top_center_show_salutation`
  - `emb_hero_image_top_center_use_snippetcall_salutation`
  - `emb_hero_image_top_center_salutation`
  - `emb_hero_image_top_center_body`
  - `emb_hero_image_top_center_button_url`
  - `emb_hero_image_top_center_button_bg_color`
  - `emb_hero_image_top_center_button_border_color`
  - `emb_hero_image_top_center_button_label`
- Headline-Groessenvariante:
  - `emb_hero_image_top_center_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_image_top_center_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_image_top_center_show_small_headline = true` und `emb_hero_image_top_center_show_large_headline = false`
    - `m` => `emb_hero_image_top_center_show_small_headline = false` und `emb_hero_image_top_center_show_large_headline = false`
    - `l` => `emb_hero_image_top_center_show_small_headline = false` und `emb_hero_image_top_center_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_image_top_center_headline_size = l`, `emb_hero_image_top_center_show_small_headline = false` und `emb_hero_image_top_center_show_large_headline = true` erzeugen.
  - `emb_hero_image_top_center_show_large_headline` ist nur noch ein Legacy-/Bridge-Feld; wenn es ohne kanonisches `headline_size` auf `true` steht, wird zu `headline_size = l` normalisiert, sonst zu `headline_size = m`.
  - `emb_hero_image_top_center_show_small_headline = true` und `emb_hero_image_top_center_show_large_headline = true` gleichzeitig sind ungueltig und muessen fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### `hero-image-top-bleed`

- Snippet: `emb_hero_image_top_bleed`
- Verbindlicher Snippet-Call-Vertrag: genau 20 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_image_top_bleed_bg_color`
  - `emb_hero_image_top_bleed_show_preheadline`
  - `emb_hero_image_top_bleed_preheadline`
  - `emb_hero_image_top_bleed_show_badge`
  - `emb_hero_image_top_bleed_badge_bg_color`
  - `emb_hero_image_top_bleed_badge_text_color`
  - `emb_hero_image_top_bleed_badge_label`
  - `emb_hero_image_top_bleed_show_small_headline`
  - `emb_hero_image_top_bleed_show_large_headline`
  - `emb_hero_image_top_bleed_headline`
  - `emb_hero_image_top_bleed_image_url`
  - `emb_hero_image_top_bleed_image_alt`
  - `emb_hero_image_top_bleed_show_salutation`
  - `emb_hero_image_top_bleed_use_snippetcall_salutation`
  - `emb_hero_image_top_bleed_salutation`
  - `emb_hero_image_top_bleed_body`
  - `emb_hero_image_top_bleed_button_url`
  - `emb_hero_image_top_bleed_button_bg_color`
  - `emb_hero_image_top_bleed_button_border_color`
  - `emb_hero_image_top_bleed_button_label`
- Headline-Groessenvariante:
  - `emb_hero_image_top_bleed_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_image_top_bleed_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_image_top_bleed_show_small_headline = true` und `emb_hero_image_top_bleed_show_large_headline = false`
    - `m` => `emb_hero_image_top_bleed_show_small_headline = false` und `emb_hero_image_top_bleed_show_large_headline = false`
    - `l` => `emb_hero_image_top_bleed_show_small_headline = false` und `emb_hero_image_top_bleed_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_image_top_bleed_headline_size = l`, `emb_hero_image_top_bleed_show_small_headline = false` und `emb_hero_image_top_bleed_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### `hero-image-top-bleed-center`

- Snippet: `emb_hero_image_top_bleed_center`
- Layout: Eyebrow oder Badge, Headline, Anrede, Body und CTA sind zentriert.
- Verbindlicher Snippet-Call-Vertrag: genau 20 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_image_top_bleed_center_bg_color`
  - `emb_hero_image_top_bleed_center_show_preheadline`
  - `emb_hero_image_top_bleed_center_preheadline`
  - `emb_hero_image_top_bleed_center_show_badge`
  - `emb_hero_image_top_bleed_center_badge_bg_color`
  - `emb_hero_image_top_bleed_center_badge_text_color`
  - `emb_hero_image_top_bleed_center_badge_label`
  - `emb_hero_image_top_bleed_center_show_small_headline`
  - `emb_hero_image_top_bleed_center_show_large_headline`
  - `emb_hero_image_top_bleed_center_headline`
  - `emb_hero_image_top_bleed_center_image_url`
  - `emb_hero_image_top_bleed_center_image_alt`
  - `emb_hero_image_top_bleed_center_show_salutation`
  - `emb_hero_image_top_bleed_center_use_snippetcall_salutation`
  - `emb_hero_image_top_bleed_center_salutation`
  - `emb_hero_image_top_bleed_center_body`
  - `emb_hero_image_top_bleed_center_button_url`
  - `emb_hero_image_top_bleed_center_button_bg_color`
  - `emb_hero_image_top_bleed_center_button_border_color`
  - `emb_hero_image_top_bleed_center_button_label`
- Headline-Groessenvariante:
  - `emb_hero_image_top_bleed_center_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_image_top_bleed_center_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_image_top_bleed_center_show_small_headline = true` und `emb_hero_image_top_bleed_center_show_large_headline = false`
    - `m` => `emb_hero_image_top_bleed_center_show_small_headline = false` und `emb_hero_image_top_bleed_center_show_large_headline = false`
    - `l` => `emb_hero_image_top_bleed_center_show_small_headline = false` und `emb_hero_image_top_bleed_center_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_image_top_bleed_center_headline_size = l`, `emb_hero_image_top_bleed_center_show_small_headline = false` und `emb_hero_image_top_bleed_center_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### `hero-image-head-copy-bleed-center`

- Snippet: `emb_hero_image_head_copy_bleed_center`
- Verbindlicher Snippet-Call-Vertrag: genau 14 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_image_head_copy_bleed_center_bg_color`
  - `emb_hero_image_head_copy_bleed_center_show_small_headline`
  - `emb_hero_image_head_copy_bleed_center_show_large_headline`
  - `emb_hero_image_head_copy_bleed_center_image_url`
  - `emb_hero_image_head_copy_bleed_center_image_alt`
  - `emb_hero_image_head_copy_bleed_center_headline`
  - `emb_hero_image_head_copy_bleed_center_show_salutation`
  - `emb_hero_image_head_copy_bleed_center_use_snippetcall_salutation`
  - `emb_hero_image_head_copy_bleed_center_salutation`
  - `emb_hero_image_head_copy_bleed_center_body`
  - `emb_hero_image_head_copy_bleed_center_button_url`
  - `emb_hero_image_head_copy_bleed_center_button_bg_color`
  - `emb_hero_image_head_copy_bleed_center_button_border_color`
  - `emb_hero_image_head_copy_bleed_center_button_label`
- Headline-Groessenvariante:
  - `emb_hero_image_head_copy_bleed_center_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_image_head_copy_bleed_center_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_image_head_copy_bleed_center_show_small_headline = true` und `emb_hero_image_head_copy_bleed_center_show_large_headline = false`
    - `m` => `emb_hero_image_head_copy_bleed_center_show_small_headline = false` und `emb_hero_image_head_copy_bleed_center_show_large_headline = false`
    - `l` => `emb_hero_image_head_copy_bleed_center_show_small_headline = false` und `emb_hero_image_head_copy_bleed_center_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_image_head_copy_bleed_center_headline_size = l`, `emb_hero_image_head_copy_bleed_center_show_small_headline = false` und `emb_hero_image_head_copy_bleed_center_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### `hero-image-textbox-cta-center`

- Snippet: `emb_hero_image_textbox_cta_center`
- Verbindlicher Snippet-Call-Vertrag: genau 17 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_image_textbox_cta_center_bg_color`
  - `emb_hero_image_textbox_cta_center_show_small_headline`
  - `emb_hero_image_textbox_cta_center_show_large_headline`
  - `emb_hero_image_textbox_cta_center_headline`
  - `emb_hero_image_textbox_cta_center_image_url`
  - `emb_hero_image_textbox_cta_center_image_alt`
  - `emb_hero_image_textbox_cta_center_show_salutation`
  - `emb_hero_image_textbox_cta_center_use_snippetcall_salutation`
  - `emb_hero_image_textbox_cta_center_salutation`
  - `emb_hero_image_textbox_cta_center_body`
  - `emb_hero_image_textbox_cta_center_question`
  - `emb_hero_image_textbox_cta_center_entry_url`
  - `emb_hero_image_textbox_cta_center_entry_text`
  - `emb_hero_image_textbox_cta_center_button_url`
  - `emb_hero_image_textbox_cta_center_button_bg_color`
  - `emb_hero_image_textbox_cta_center_button_border_color`
  - `emb_hero_image_textbox_cta_center_button_label`
- Headline-Groessenvariante:
  - `emb_hero_image_textbox_cta_center_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_image_textbox_cta_center_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_image_textbox_cta_center_show_small_headline = true` und `emb_hero_image_textbox_cta_center_show_large_headline = false`
    - `m` => `emb_hero_image_textbox_cta_center_show_small_headline = false` und `emb_hero_image_textbox_cta_center_show_large_headline = false`
    - `l` => `emb_hero_image_textbox_cta_center_show_small_headline = false` und `emb_hero_image_textbox_cta_center_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_image_textbox_cta_center_headline_size = l`, `emb_hero_image_textbox_cta_center_show_small_headline = false` und `emb_hero_image_textbox_cta_center_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.
- Export-Hinweis:
  - `entry_url` kommt im produktiven E-Mail-Modul vor dem sichtbaren `entry_text`, weil die Kontur-Flaeche als kompletter Link gerendert wird.
  - Fuer den Export ist genau diese Reihenfolge verbindlich.

### `hero-fakeform-buttons-image`

- Snippet: `emb_hero_fakeform_buttons_image`
- Layout: zentrierte Hero-Headline, vertikal gestapelte Auswahlbuttons, Bild, Anrede, Body und finaler Brand-CTA.
- Verbindlicher Snippet-Call-Vertrag: genau 31 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_fakeform_buttons_image_bg_color`
  - `emb_hero_fakeform_buttons_image_show_small_headline`
  - `emb_hero_fakeform_buttons_image_show_large_headline`
  - `emb_hero_fakeform_buttons_image_headline`
  - `emb_hero_fakeform_buttons_image_choice_button_1_url`
  - `emb_hero_fakeform_buttons_image_choice_button_1_label`
  - `emb_hero_fakeform_buttons_image_show_item_2`
  - `emb_hero_fakeform_buttons_image_choice_button_2_url`
  - `emb_hero_fakeform_buttons_image_choice_button_2_label`
  - `emb_hero_fakeform_buttons_image_show_item_3`
  - `emb_hero_fakeform_buttons_image_choice_button_3_url`
  - `emb_hero_fakeform_buttons_image_choice_button_3_label`
  - `emb_hero_fakeform_buttons_image_show_item_4`
  - `emb_hero_fakeform_buttons_image_choice_button_4_url`
  - `emb_hero_fakeform_buttons_image_choice_button_4_label`
  - `emb_hero_fakeform_buttons_image_show_item_5`
  - `emb_hero_fakeform_buttons_image_choice_button_5_url`
  - `emb_hero_fakeform_buttons_image_choice_button_5_label`
  - `emb_hero_fakeform_buttons_image_show_item_6`
  - `emb_hero_fakeform_buttons_image_choice_button_6_url`
  - `emb_hero_fakeform_buttons_image_choice_button_6_label`
  - `emb_hero_fakeform_buttons_image_image_url`
  - `emb_hero_fakeform_buttons_image_image_alt`
  - `emb_hero_fakeform_buttons_image_show_salutation`
  - `emb_hero_fakeform_buttons_image_use_snippetcall_salutation`
  - `emb_hero_fakeform_buttons_image_salutation`
  - `emb_hero_fakeform_buttons_image_body`
  - `emb_hero_fakeform_buttons_image_button_url`
  - `emb_hero_fakeform_buttons_image_button_bg_color`
  - `emb_hero_fakeform_buttons_image_button_border_color`
  - `emb_hero_fakeform_buttons_image_button_label`
- Headline-Groessenvariante:
  - `emb_hero_fakeform_buttons_image_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_fakeform_buttons_image_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_fakeform_buttons_image_show_small_headline = true` und `emb_hero_fakeform_buttons_image_show_large_headline = false`
    - `m` => `emb_hero_fakeform_buttons_image_show_small_headline = false` und `emb_hero_fakeform_buttons_image_show_large_headline = false`
    - `l` => `emb_hero_fakeform_buttons_image_show_small_headline = false` und `emb_hero_fakeform_buttons_image_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_fakeform_buttons_image_headline_size = l`, `emb_hero_fakeform_buttons_image_show_small_headline = false` und `emb_hero_fakeform_buttons_image_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.
- Button-Regel:
  - Default sichtbar sind `5` Auswahlbuttons; das Modul unterstuetzt technisch `2` bis `6`.
  - Button `1` bleibt immer sichtbar.
  - `show_item_2` bleibt fuer dieses Modul verpflichtend `true`, damit die Mindestanzahl `2` eingehalten wird.
  - `show_item_3..6` steuern die spaeteren Auswahlbuttons.
  - Die Auswahlbuttons nutzen im ersten produktiven Stand das bestehende Pattern `button-outline-strong`.
  - Der finale CTA nutzt wie andere Hero-Module `button-filled-brand`.

### `hero-cta-top`

- Snippet: `emb_hero_cta_top`
- Verbindlicher Snippet-Call-Vertrag: genau 20 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_cta_top_bg_color`
  - `emb_hero_cta_top_show_preheadline`
  - `emb_hero_cta_top_preheadline`
  - `emb_hero_cta_top_show_badge`
  - `emb_hero_cta_top_badge_bg_color`
  - `emb_hero_cta_top_badge_text_color`
  - `emb_hero_cta_top_badge_label`
  - `emb_hero_cta_top_show_small_headline`
  - `emb_hero_cta_top_show_large_headline`
  - `emb_hero_cta_top_headline`
  - `emb_hero_cta_top_show_salutation`
  - `emb_hero_cta_top_use_snippetcall_salutation`
  - `emb_hero_cta_top_salutation`
  - `emb_hero_cta_top_body`
  - `emb_hero_cta_top_button_url`
  - `emb_hero_cta_top_button_bg_color`
  - `emb_hero_cta_top_button_border_color`
  - `emb_hero_cta_top_button_label`
  - `emb_hero_cta_top_image_url`
  - `emb_hero_cta_top_image_alt`
- Headline-Groessenvariante:
  - `emb_hero_cta_top_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_cta_top_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_cta_top_show_small_headline = true` und `emb_hero_cta_top_show_large_headline = false`
    - `m` => `emb_hero_cta_top_show_small_headline = false` und `emb_hero_cta_top_show_large_headline = false`
    - `l` => `emb_hero_cta_top_show_small_headline = false` und `emb_hero_cta_top_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_cta_top_headline_size = l`, `emb_hero_cta_top_show_small_headline = false` und `emb_hero_cta_top_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### `hero-cta-top-center`

- Snippet: `emb_hero_cta_top_center`
- Layout: Eyebrow oder Badge, Headline, Anrede, Body und CTA sind zentriert.
- Verbindlicher Snippet-Call-Vertrag: genau 20 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_cta_top_center_bg_color`
  - `emb_hero_cta_top_center_show_preheadline`
  - `emb_hero_cta_top_center_preheadline`
  - `emb_hero_cta_top_center_show_badge`
  - `emb_hero_cta_top_center_badge_bg_color`
  - `emb_hero_cta_top_center_badge_text_color`
  - `emb_hero_cta_top_center_badge_label`
  - `emb_hero_cta_top_center_show_small_headline`
  - `emb_hero_cta_top_center_show_large_headline`
  - `emb_hero_cta_top_center_headline`
  - `emb_hero_cta_top_center_show_salutation`
  - `emb_hero_cta_top_center_use_snippetcall_salutation`
  - `emb_hero_cta_top_center_salutation`
  - `emb_hero_cta_top_center_body`
  - `emb_hero_cta_top_center_button_url`
  - `emb_hero_cta_top_center_button_bg_color`
  - `emb_hero_cta_top_center_button_border_color`
  - `emb_hero_cta_top_center_button_label`
  - `emb_hero_cta_top_center_image_url`
  - `emb_hero_cta_top_center_image_alt`
- Headline-Groessenvariante:
  - `emb_hero_cta_top_center_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_cta_top_center_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_cta_top_center_show_small_headline = true` und `emb_hero_cta_top_center_show_large_headline = false`
    - `m` => `emb_hero_cta_top_center_show_small_headline = false` und `emb_hero_cta_top_center_show_large_headline = false`
    - `l` => `emb_hero_cta_top_center_show_small_headline = false` und `emb_hero_cta_top_center_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_cta_top_center_headline_size = l`, `emb_hero_cta_top_center_show_small_headline = false` und `emb_hero_cta_top_center_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### `hero-cta-top-no-bottom`

- Snippet: `emb_hero_cta_top_no_bottom`
- Verbindlicher Snippet-Call-Vertrag: genau 20 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_cta_top_no_bottom_bg_color`
  - `emb_hero_cta_top_no_bottom_show_preheadline`
  - `emb_hero_cta_top_no_bottom_preheadline`
  - `emb_hero_cta_top_no_bottom_show_badge`
  - `emb_hero_cta_top_no_bottom_badge_bg_color`
  - `emb_hero_cta_top_no_bottom_badge_text_color`
  - `emb_hero_cta_top_no_bottom_badge_label`
  - `emb_hero_cta_top_no_bottom_show_small_headline`
  - `emb_hero_cta_top_no_bottom_show_large_headline`
  - `emb_hero_cta_top_no_bottom_headline`
  - `emb_hero_cta_top_no_bottom_show_salutation`
  - `emb_hero_cta_top_no_bottom_use_snippetcall_salutation`
  - `emb_hero_cta_top_no_bottom_salutation`
  - `emb_hero_cta_top_no_bottom_body`
  - `emb_hero_cta_top_no_bottom_button_url`
  - `emb_hero_cta_top_no_bottom_button_bg_color`
  - `emb_hero_cta_top_no_bottom_button_border_color`
  - `emb_hero_cta_top_no_bottom_button_label`
  - `emb_hero_cta_top_no_bottom_image_url`
  - `emb_hero_cta_top_no_bottom_image_alt`
- Headline-Groessenvariante:
  - `emb_hero_cta_top_no_bottom_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_cta_top_no_bottom_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_cta_top_no_bottom_show_small_headline = true` und `emb_hero_cta_top_no_bottom_show_large_headline = false`
    - `m` => `emb_hero_cta_top_no_bottom_show_small_headline = false` und `emb_hero_cta_top_no_bottom_show_large_headline = false`
    - `l` => `emb_hero_cta_top_no_bottom_show_small_headline = false` und `emb_hero_cta_top_no_bottom_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_cta_top_no_bottom_headline_size = l`, `emb_hero_cta_top_no_bottom_show_small_headline = false` und `emb_hero_cta_top_no_bottom_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### Teaser-Module

- `loft-rnl-dev-intro` ist ein template-spezifisches Loft-RNL-Dev-Intro mit editierbarer `heading-l`-Headline, kontrolliertem Salutation-Feld und einem frei editierbaren `rich_full`-Body.
- Das Modul nutzt genau diese Builder-Felder:
  - `emb_loft_rnl_dev_intro_headline`
  - `emb_loft_rnl_dev_intro_salutation`
  - `emb_loft_rnl_dev_intro_body`
- In der Preview bleibt `emb_loft_rnl_dev_intro_salutation` menschenlesbarer Plain Text `Hallo Anrede`.
- Die finale EMB-Preview materialisiert die Intro-Headline im Markup explizit als `font-heading-large-bold`, damit die bestehende `heading-l`-Typografie ohne Loft-Sonderannahmen im Preview-Pfad landet.
- Fuer `salutationContext = loft-rnl-dev` wird der produktive Exportwert von `emb_loft_rnl_dev_intro_salutation` kontrolliert aus `agent/product-salutations.json` materialisiert.
- `teaser-1col` behaelt Bild, Richtextbereich und CTA.
- `loft-rnl-dev-teaser-1col` ist ein template-spezifisches Loft-RNL-Dev-Modul mit Badge, `heading-l`-Headline, Bild, Richtext-Body, festem Detailtitel, Richtext-Detailbereich und CTA.
- `loft-rnl-dev-teaser-1col` ist repeatable; neue Instanzen werden direkt nach der letzten vorhandenen Instanz derselben `module_id` eingefuegt.
- `loft-rnl-dev-teaser-1col` nutzt fuer `emb_loft_rnl_dev_teaser_1col_bg_color` immer den globalen Hintergrund-Rhythmus:
  - erste Instanz nach dem Intro = grau `#F5F5F5`
  - zweite Instanz = weiss `#FFFFFF`
  - danach strikt weiter grau, weiss, grau, weiss
- Die Badge-Flaeche von `loft-rnl-dev-teaser-1col` ist keine freie User-Entscheidung; sie ist immer invers zur finalen Hintergrundflaeche des Moduls.
- Die finale EMB-Preview materialisiert diese Badge-Inversion direkt im Markup:
  - graues Modul `#F5F5F5` => `module__badge module__badge--surface-white`
  - weisses Modul `#FFFFFF` => `module__badge module__badge--surface-gray`
- Die finale EMB-Preview materialisiert die Teaser-Headline im Markup explizit als `font-heading-large-bold`, damit die bestehende `heading-l`-Typografie ohne groessere Hero-/XL-Klassen im Preview-Pfad landet.
- `loft-regio-resi-intro` ist ein template-spezifisches Loft-Regio-Resi-Intro mit editierbarer `heading-l`-Headline, kontrolliertem Salutation-Feld und einem frei editierbaren `rich_full`-Body.
- Das Modul nutzt genau diese Builder-Felder:
  - `emb_loft_regio_resi_intro_headline`
  - `emb_loft_regio_resi_intro_salutation`
  - `emb_loft_regio_resi_intro_body`
- In der Preview bleibt `emb_loft_regio_resi_intro_salutation` menschenlesbarer Plain Text `Hallo Anrede`.
- Die finale EMB-Preview materialisiert die Intro-Headline im Markup explizit als `font-heading-large-bold`, damit die bestehende `heading-l`-Typografie ohne Loft-Sonderannahmen im Preview-Pfad landet.
- Fuer `salutationContext = loft-regio-resi` wird der produktive Exportwert von `emb_loft_regio_resi_intro_salutation` kontrolliert aus `agent/product-salutations.json` materialisiert.
- `loft-regio-resi-teaser-1col` ist ein template-spezifisches Loft-Regio-Residential-Modul mit `heading-l`-Headline, Richtext-Body, Bild, drei editierbaren Kennzahlen und CTA.
- `loft-regio-resi-teaser-1col` ist repeatable; neue Instanzen werden direkt nach der letzten vorhandenen Instanz derselben `module_id` eingefuegt.
- `loft-regio-resi-teaser-1col` nutzt fuer `emb_loft_regio_resi_teaser_1col_bg_color` immer den globalen Hintergrund-Rhythmus:
  - erste Instanz nach dem Intro = grau `#F5F5F5`
  - zweite Instanz = weiss `#FFFFFF`
  - danach strikt weiter grau, weiss, grau, weiss
- Die Kennzahlen von `loft-regio-resi-teaser-1col` sind keine getrennten Desktop-/Mobile-Felder; dieselben `metric_1..3_label`- und `metric_1..3_value`-Felder speisen die Desktop-Dreispalter und die mobile Bullet-Liste.
- Die finale EMB-Preview materialisiert die Teaser-Headline im Markup explizit als `font-heading-large-bold`, damit die bestehende `heading-l`-Typografie ohne groessere Hero-/XL-Klassen im Preview-Pfad landet.
- `teaser-2col-horizontal` nutzt bis zu vier Items; `show_item_2..4` folgen exakt der sichtbaren Item-Anzahl.
- `teaser-2col-vertical` nutzt genau zwei Spalten.
- `teaser-2col-alternating` nutzt genau zwei Zeilen.
- `teaser-2col-listing` nutzt bis zu vier Items; sichtbare spaetere Zeilen duerfen nie auf `col_1_*` reduziert werden.
- `teaser-2col-gallery` nutzt immer zwei Bilder in der ersten Reihe; `show_item_3` und `show_item_4` erweitern die untere Reihe.
- `teaser-2col-gallery` erlaubt zusaetzlich `hide_bottom_row_mobile`; damit verschwindet die untere Reihe nur in der mobilen Ausgabe.
- Fehlende echte Bild-URL nutzt den passenden `16:9`- oder `4:3`-Placeholder aus dem technischen Mapping.

### `hero-cta-top-no-bottom-center`

- Snippet: `emb_hero_cta_top_no_bottom_center`
- Layout: Eyebrow oder Badge, Headline, Anrede, Body und CTA sind zentriert.
- Verbindlicher Snippet-Call-Vertrag: genau 20 Snippet-Parameter in dieser Reihenfolge
  - `emb_hero_cta_top_no_bottom_center_bg_color`
  - `emb_hero_cta_top_no_bottom_center_show_preheadline`
  - `emb_hero_cta_top_no_bottom_center_preheadline`
  - `emb_hero_cta_top_no_bottom_center_show_badge`
  - `emb_hero_cta_top_no_bottom_center_badge_bg_color`
  - `emb_hero_cta_top_no_bottom_center_badge_text_color`
  - `emb_hero_cta_top_no_bottom_center_badge_label`
  - `emb_hero_cta_top_no_bottom_center_show_small_headline`
  - `emb_hero_cta_top_no_bottom_center_show_large_headline`
  - `emb_hero_cta_top_no_bottom_center_headline`
  - `emb_hero_cta_top_no_bottom_center_show_salutation`
  - `emb_hero_cta_top_no_bottom_center_use_snippetcall_salutation`
  - `emb_hero_cta_top_no_bottom_center_salutation`
  - `emb_hero_cta_top_no_bottom_center_body`
  - `emb_hero_cta_top_no_bottom_center_button_url`
  - `emb_hero_cta_top_no_bottom_center_button_bg_color`
  - `emb_hero_cta_top_no_bottom_center_button_border_color`
  - `emb_hero_cta_top_no_bottom_center_button_label`
  - `emb_hero_cta_top_no_bottom_center_image_url`
  - `emb_hero_cta_top_no_bottom_center_image_alt`
- Headline-Groessenvariante:
  - `emb_hero_cta_top_no_bottom_center_headline_size` ist das einzige kanonische Groessenfeld.
  - `emb_hero_cta_top_no_bottom_center_headline_size` gehoert zum kanonischen State-/Exportvertrag, ist aber kein direkt gerenderter Snippet-Parameter.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Snippet-Bridge ist fest:
    - `s` => `emb_hero_cta_top_no_bottom_center_show_small_headline = true` und `emb_hero_cta_top_no_bottom_center_show_large_headline = false`
    - `m` => `emb_hero_cta_top_no_bottom_center_show_small_headline = false` und `emb_hero_cta_top_no_bottom_center_show_large_headline = false`
    - `l` => `emb_hero_cta_top_no_bottom_center_show_small_headline = false` und `emb_hero_cta_top_no_bottom_center_show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `emb_hero_cta_top_no_bottom_center_headline_size = l`, `emb_hero_cta_top_no_bottom_center_show_small_headline = false` und `emb_hero_cta_top_no_bottom_center_show_large_headline = true` erzeugen.
  - Legacy-Bridge-Felder sind nur technische Kompatibilitaetsfelder; `true/true` gleichzeitig ist ungueltig und muss fail-closed stoppen.
  - Es gibt kein freies Headline-Style-, HTML- oder CSS-Feld fuer dieses Modul.

### Teaser-Module

- `teaser-1col` behaelt Bild, Richtextbereich und CTA.
- `teaser-2col-horizontal` nutzt bis zu vier Items; `show_item_2..4` folgen exakt der sichtbaren Item-Anzahl.
- `teaser-2col-vertical` nutzt genau zwei Spalten.
- `teaser-2col-alternating` nutzt genau zwei Zeilen.
- `teaser-2col-listing` nutzt bis zu vier Items; sichtbare spaetere Zeilen duerfen nie auf `col_1_*` reduziert werden.
- `teaser-2col-gallery` nutzt immer zwei Bilder in der ersten Reihe; `show_item_3` und `show_item_4` erweitern die untere Reihe.
- `teaser-2col-gallery` erlaubt zusaetzlich `hide_bottom_row_mobile`; damit verschwindet die untere Reihe nur in der mobilen Ausgabe.
- Fehlende echte Bild-URL nutzt den passenden `16:9`- oder `4:3`-Placeholder aus dem technischen Mapping.

### `benefits-3col`

- Vor dem Preview-Render alle drei Icon-URLs bucket-basiert aus `icon-library.md` setzen.
- Erlaubte Icon-URLs duerfen nur aus `icon-library.md` kommen.
- Wenn kein Bucket klar passt, den kanonischen `general-positive`-Fallback aus `icon-library.md` verwenden.
- Die drei Benefit-Texte sollen visuell aehnliche Textmengen ergeben.

### `servicetiles`

- Snippet: `emb_servicetiles`
- Das Modul rendert genau eine Headline und genau vier Service-Cards.
- Fachlich genannte Services werden vor Preview und Export ausschliesslich ueber `agent/service-products.json` via `id` oder `aliases` aufgeloest.
- Wenn nicht genau `4` Services eindeutig aufloesbar sind, muss der Agent nachfragen und darf das Modul nicht stillschweigend normalisieren.
- Der produktive Snippet-Vertrag rendert nur die aufgeloesten Card-Felder:
  - `emb_servicetiles_headline`
  - `emb_servicetiles_col_1_url`
  - `emb_servicetiles_col_1_icon_url`
  - `emb_servicetiles_col_1_title`
  - `emb_servicetiles_col_1_description`
  - `emb_servicetiles_col_2_url`
  - `emb_servicetiles_col_2_icon_url`
  - `emb_servicetiles_col_2_title`
  - `emb_servicetiles_col_2_description`
  - `emb_servicetiles_col_3_url`
  - `emb_servicetiles_col_3_icon_url`
  - `emb_servicetiles_col_3_title`
  - `emb_servicetiles_col_3_description`
  - `emb_servicetiles_col_4_url`
  - `emb_servicetiles_col_4_icon_url`
  - `emb_servicetiles_col_4_title`
  - `emb_servicetiles_col_4_description`
- Fachliche Service-Namen und `original_snippet_name` sind Resolver-Eingaben, aber keine direkten Snippet-Parameter des finalen Moduls.
- Das E-Mail-Markup bleibt ein einzelnes Modul mit `2 x 2` auf Desktop und `1` Spalte auf Mobile; diese Layoutlogik ist reine Renderlogik und kein zweites Export-Signal.

### `steps-3col`

- Die drei Preview-Schritte werden direkt in die drei Export-Schritte uebersetzt.
- Das Modul wird genau einmal ueber `module_id`, `snippet_name` und `content` exportiert.
- Desktop- und Mobile-Markup im echten Snippet sind reine Renderdetails und kein Export-Signal.

### `steps-horizontal`

- Die drei Preview-Schritte werden direkt in die drei Export-Schritte uebersetzt.

### Tabellen-Module

- `table` behaelt genau drei Spalten und drei Datenzeilen.
- `table-comparison` behaelt genau zwei Vergleichsspalten mit je drei Zeilen.
- Struktur und Reihenfolge muessen im Export mit der Preview uebereinstimmen.

### `contact`

- Die Contact-Preview wird direkt ueber den strukturierten `email_state` in den Contact-Snippet-Call uebersetzt.
- `contact` hat immer weissen Hintergrund und nutzt kein editierbares oder alternierendes `bg_color`-Feld.
- Das Contact-Modul nutzt an der bestehenden Placeholder-Position optional genau diese Bildfelder:
  - `emb_contact_show_image`
  - `emb_contact_image_url`
  - `emb_contact_image_alt`
- Ohne echte Bild-URL bleibt in der Preview der vorhandene Avatar-Placeholder sichtbar und im E-Mail-Snippet der neutrale graue Kreis aktiv.

### `footer`

- `emb_footer_marketing` bleibt im Minimal-Setup parameterlos.
```

## email-builder/agent/export-rules.md

Dateityp: md

```md
# Export Rules

Diese Datei ist die einzige operative Export-Regelbasis im flachen Agent-Satz unter `agent/`.
Die uebrigen operativen Agent-Dateien liegen direkt daneben in `agent/`.

## Trigger

- Export startet nur bei einer expliziten Anweisung wie `Exportiere die Mail zu Iterable`.
- Gleichwertige explizite Trigger sind nur klare Export-/Upload-/Update-Anweisungen des Users fuer Iterable.
- Eine Preview-Anfrage, eine Template-Auswahl oder ein erfolgreicher Preview-Lauf gelten nie als Export-Trigger.
- Nach erfolgreicher Preview bleibt der Agent im Preview-Modus, bis der User den Export ausdruecklich bestaetigt oder selbst Export/Upload/Update verlangt.
- Diese Anweisung bedeutet: aktuelle Preview-Komposition in den finalen modularen Snippet-Call-Block uebersetzen, diesen in die vollstaendige campaign-owned HTML-Shell einsetzen und genau diese finale HTML-Payload nach erfolgreichem `createCampaign` genau einmal in die zugehoerige Iterable-Campaign schreiben.
- Sie bedeutet nicht: Preview-HTML speichern, Preview-HTML als Template anlegen, Draft als Standardziel nutzen oder nackte Snippet-Codes als Komplett-HTML schreiben.

## Quelle

- Die operative Exportquelle ist ausschliesslich der aktuelle `email_state` zusammen mit `export-map.json`.
- Wenn noch keine Preview existiert, wird zuerst eine Preview erstellt und dabei parallel ein `email_state` aufgebaut.
- Der `email_state` muss als strukturierte JSON-Arbeitsdatei zur aktuellen Preview verfuegbar bleiben und im Export-Lauf direkt wiederverwendet werden.
- Der Export darf Preview-HTML oder Snippet-HTML nicht regulaer als Quelle rekonstruieren.
- Preview-DOM oder markierte Preview-Knoten sind nur als Debug- oder Recovery-Fallback zulaessig, nicht im regulaeren Happy Path.
- `export-map.json` ist die einzige technische Quelle fuer erlaubte Module, Snippet-Namen, Feldnamen, Feldtypen, Required-Flags und Defaults.
- Jedes Feld im `email_state.content`, das fuer das jeweilige Modul nicht in `export-map.json` registriert ist, ist ein Unknown Field und fuehrt zu einem Export-Fehler.
- Required Felder duerfen nur aus `content` oder aus dem Default der Export-Map befuellt werden.
- Felder ohne Content und ohne Default werden nie frei erfunden.
- Nur Hero-Headlines duerfen im Export-State ueber ein kanonisches Groessenfeld steuerbar sein.
- Erlaubte Hero-Groessen sind ausschliesslich `s`, `m` und `l`; ihr Mapping ist direkt `heading-s`, `heading-m`, `heading-l`.
- Der reguläre Hero-Default ist `l`.
- Nicht-Hero-Modulheadlines sind nicht usersteuerbar:
  - erste Hauptheadline = `heading-m`, ausser eine dokumentierte modulspezifische Ausnahme ist in `preview-module-library.md` oder `builder-library.md` registriert
  - Unter-Headlines, Abschnittstitel und Zwischenueberschriften = `heading-s`
  - Bodytexte = `body-standard`
- Freie Heading-Klassen, freie CSS-Werte, freie Font-Size-Werte, freies HTML oder freie Style-Werte sind fuer Typography-Steuerung unzulaessig.
- Wenn eine Felddefinition in `export-map.json` `allowed_values` definiert, muss der konkrete Feldwert exakt einem dieser erlaubten Werte entsprechen; jeder andere Wert ist ein lokaler State-Fehler und stoppt den Export vor dem Snippet-Build.
- Ein `email_state` ist nur export-ready, wenn `subject`, `preheader` und ein eindeutiger Template-Kontext bereits vorliegen.
- Der aktive Template-Kontext ist nur in diesen beiden Formen zulaessig:
  - freier Modulbau oder Blueprint: `templateContext.mode = default_template` und `templateContext.resolvedBaseTemplateId = 569946`
  - Composition-Template: `templateContext.mode = composition_template`, `templateContext.compositionTemplateId`, `templateContext.iterableTemplateId` und `templateContext.resolvedBaseTemplateId = iterable_template_id`
- Fuer neue regulaere States soll der aufgeloeste `salutationContext` bereits im `email_state` stehen; zulaessige Werte kommen ausschliesslich aus `agent/product-salutations.json`.
- Wenn ein aktives Composition-Template eine `salutation_context_id` traegt, ist diese Zuweisung die dokumentierte Quelle fuer den Export-Kontext und braucht keine zusaetzliche Rueckfrage.
- `salutationContext` steuert nur dokumentierte Anrede-Resolver und ist nie ein freier User-Input fuer Handlebars, Snippetcalls oder Raw-HTML.
- Bei Re-Export duerfen `campaignId` und campaign-owned `templateId` nur wiederverwendet werden, wenn sie im State ueber einen stabilen `previewBranchKey` eindeutig demselben fortgeschriebenen Preview-/Composition-Zweig zugeordnet sind.
- Ein required Feld ist nur dann export-ready, wenn genau eine dieser drei Quellen greift:
  - konkreter Wert in `email_state.content`
  - eindeutiger technischer Default aus `export-map.json`
  - bereits vor dem Export konkret materialisierter Resolver-Wert aus einer dokumentierten technischen Quelle
- Dokumentierte technische Resolver-Quellen sind nur:
  - Hintergrund-Rhythmus aus `builder-library.md` plus `preview-styles.css`
  - Icon-Auswahl aus `icon-library.md`
  - kontrollierte Service-Produkt-Aufloesung fuer `servicetiles` aus `agent/service-products.json`
  - finale Button-Farbwerte aus `builder-library.md`
  - kontrollierte Salutation-Feld-Overrides aus `product-salutations.json`
- Der Export-Happy-Path prueft nur den vorhandenen export-ready State gegen `export-map.json`.
- Der Export darf fehlende required Werte nicht aus Preview-HTML, DOM, sichtbarer Darstellung, Button-Klassen oder freiem Modulkontext raten.
- Wenn `email_state.modules` eines der Center-Hero-Module `hero-image-top-center`, `hero-image-top-bleed-center`, `hero-cta-top-center`, `hero-cta-top-no-bottom-center`, `hero-image-head-copy-bleed-center`, `hero-image-textbox-cta-center` oder `hero-fakeform-buttons-image` enthaelt, muss ein vorhandenes Logo-Modul im export-ready State als `logo-centered` vorliegen.
- Ein plain `logo` ist in diesem Center-Hero-Kontext kein export-ready Endzustand und muss bereits vor dem Export auf `logo-centered` normalisiert worden sein.
- Diese Normalisierung aendert nur das Logo-Modul, fuegt kein zusaetzliches Logo ein und erhaelt die Reihenfolge der Mail.
- Fuer `hero-image-top` ist `emb_hero_image_top_headline_size` das einzige kanonische Groessenfeld fuer die Headline und darf nur `s`, `m` oder `l` tragen.
- Neue reguläre Default-States fuer `hero-image-top` muessen vor dem Export immer `emb_hero_image_top_headline_size = l`, `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = true` enthalten.
- Legacy-Normalisierung fuer `hero-image-top` ist nur vor dem regulären Export-Happy-Path zulaessig:
  - wenn `emb_hero_image_top_headline_size` fehlt oder leer ist und `emb_hero_image_top_show_large_headline = true`, wird kanonisch zu `l` normalisiert
  - wenn `emb_hero_image_top_headline_size` fehlt oder leer ist und `emb_hero_image_top_show_large_headline = false` oder leer ist, wird kanonisch zu `m` normalisiert
- Nach der kanonischen Aufloesung von `emb_hero_image_top_headline_size` muessen die technischen Bridge-Felder fuer `hero-image-top` exakt so gesetzt sein:
  - `s` => `emb_hero_image_top_show_small_headline = true` und `emb_hero_image_top_show_large_headline = false`
  - `m` => `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = false`
  - `l` => `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = true`
- Beim aktuellen Iterable-Snippet `emb_hero_image_top` ist `emb_hero_image_top_headline_size` kein direkter Snippet-Parameter; der Export darf nur die materialisierten Bridge-Felder `emb_hero_image_top_show_small_headline` und `emb_hero_image_top_show_large_headline` in die Snippet-Payload geben.
- Wenn bei `hero-image-top` `emb_hero_image_top_show_small_headline = true` und `emb_hero_image_top_show_large_headline = true` gleichzeitig vorliegen, ist das ein Bridge-Konflikt und der Export stoppt fail-closed vor dem Snippet-Build.
- Wenn die Bridge-Felder von `hero-image-top` nicht exakt zur kanonischen `emb_hero_image_top_headline_size` passen, ist das ein lokaler State-Fehler und der Export stoppt vor dem Snippet-Build.
- Fuer `hero-image-top-center`, `hero-image-top-bleed`, `hero-image-top-bleed-center`, `hero-fakeform-buttons-image`, `hero-cta-top`, `hero-cta-top-center`, `hero-cta-top-no-bottom` und `hero-cta-top-no-bottom-center` gilt dasselbe kanonische Hero-Modell:
  - genau ein `*_headline_size`-Feld mit nur `s`, `m` oder `l`
  - neue reguläre Default-States muessen `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` enthalten
  - die technischen Bridge-Felder muessen exakt aus dem kanonischen `headline_size` abgeleitet werden
  - bei den aktuellen Iterable-Snippets ist `*_headline_size` kein direkter Snippet-Parameter; der Export darf fuer diese Hero-Module nur die materialisierten `show_small_headline`- und `show_large_headline`-Bridge-Felder in die Snippet-Payload geben
  - `show_small_headline = true` und `show_large_headline = true` gleichzeitig ist ein Bridge-Konflikt und stoppt fail-closed vor dem Snippet-Build
- Fuer `hero-image-head-copy-bleed-center` gilt dasselbe kanonische Hero-Modell:
  - genau ein `emb_hero_image_head_copy_bleed_center_headline_size`-Feld mit nur `s`, `m` oder `l`
  - neue reguläre Default-States muessen `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` enthalten
  - die technischen Bridge-Felder muessen exakt aus dem kanonischen `headline_size` abgeleitet werden
  - beim aktuellen Iterable-Snippet `emb_hero_image_head_copy_bleed_center` ist `emb_hero_image_head_copy_bleed_center_headline_size` kein direkter Snippet-Parameter; der Export darf nur die materialisierten Bridge-Felder `emb_hero_image_head_copy_bleed_center_show_small_headline` und `emb_hero_image_head_copy_bleed_center_show_large_headline` in die Snippet-Payload geben
  - `show_small_headline = true` und `show_large_headline = true` gleichzeitig ist ein Bridge-Konflikt und stoppt fail-closed vor dem Snippet-Build
- Fuer `hero-image-textbox-cta-center` gilt dasselbe kanonische Hero-Modell:
  - genau ein `emb_hero_image_textbox_cta_center_headline_size`-Feld mit nur `s`, `m` oder `l`
  - neue reguläre Default-States muessen `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` enthalten
  - die technischen Bridge-Felder muessen exakt aus dem kanonischen `headline_size` abgeleitet werden
  - beim aktuellen Iterable-Snippet `emb_hero_image_textbox_cta_center` ist `emb_hero_image_textbox_cta_center_headline_size` kein direkter Snippet-Parameter; der Export darf nur die materialisierten Bridge-Felder `emb_hero_image_textbox_cta_center_show_small_headline` und `emb_hero_image_textbox_cta_center_show_large_headline` in die Snippet-Payload geben
  - `show_small_headline = true` und `show_large_headline = true` gleichzeitig ist ein Bridge-Konflikt und stoppt fail-closed vor dem Snippet-Build
- Fuer `hero-fakeform-buttons-image` gilt dasselbe kanonische Hero-Modell:
  - genau ein `emb_hero_fakeform_buttons_image_headline_size`-Feld mit nur `s`, `m` und `l`
  - neue reguläre Default-States muessen `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` enthalten
  - die technischen Bridge-Felder muessen exakt aus dem kanonischen `headline_size` abgeleitet werden
  - beim aktuellen Iterable-Snippet `emb_hero_fakeform_buttons_image` ist `emb_hero_fakeform_buttons_image_headline_size` kein direkter Snippet-Parameter; der Export darf nur die materialisierten Bridge-Felder `emb_hero_fakeform_buttons_image_show_small_headline` und `emb_hero_fakeform_buttons_image_show_large_headline` in die Snippet-Payload geben
  - `show_small_headline = true` und `show_large_headline = true` gleichzeitig ist ein Bridge-Konflikt und stoppt fail-closed vor dem Snippet-Build
- Required `*_bg_color` Felder muessen aus dem fachlichen Hintergrund-Rhythmus bereits im `email_state.content` vorliegen; sie werden nicht durch freie Export-Defaults ersetzt.
- Required `*_bg_color` Felder muessen im `email_state.content` bereits als konkrete produktive Hexwerte vorliegen.
- Preview-Klassen wie `theme-white`, `theme-gray` oder andere semantische Rhythmus-Marker sind als Exportwerte fuer `*_bg_color` unzulaessig.
- Wenn ein required `*_bg_color` im `email_state` nicht als konkreter Hexwert aus der verbindlichen Rhythmus-Farbquelle vorliegt, ist das ein lokaler State-Fehler und der Export stoppt vor jedem Write.
- `logo`, `footer`, `contact` und `contact-signoff` sind feste weisse Struktur-/Utility-Module; sie nehmen nicht an der Hintergrund-Alternierung teil und `contact` sowie `contact-signoff` exportieren deshalb kein `bg_color`-Feld.
- Normale Text-Felder im `email_state.content` enthalten Plain Text.
- Salutation-/Anredezeilen sind eigene kurze Textkontexte vor einem nachfolgenden Body und duerfen nicht im HTML-Fragment eines `rich_full`-Feldes mitgefuehrt werden.
- Salutation-/Anredezeilen duerfen keine Listen enthalten und sind im Feldtyp nur Plain Text oder hoechstens `rich_inline`, niemals `rich_full`.
- Der Abstand zwischen Salutation und nachfolgendem Body ist ein externer Kontextabstand und keine Aufgabe des `rich_full`-Feldwerts selbst.
- Fuer alle elf Hero-Module gilt zusaetzlich:
  - `*_show_salutation` ist das kanonische Show-/Hide-Feld fuer die Hero-Anrede
  - `*_salutation` bleibt ein eigener Plain-Text-Kontext vor dem Body
  - `*_use_snippetcall_salutation` ist ausschliesslich ein freigegebenes technisches Export-Flag und nie freier User-HTML- oder Raw-Code-Input
  - neue Hero-Default-States muessen `show_salutation = true` und `salutation = Hallo Anrede,` enthalten
- Fuer `salutationContext = generic` gibt es keine Spezial-Exportlogik; die menschenlesbare Preview-Anrede bleibt der normale Exportwert.
- Fuer `salutationContext = rle` ist genau eine whitelisted export-only Hero-Salutation-Substitution erlaubt:
  - Der Preview-/State-Wert `*_salutation` bleibt sichtbarer Plain Text und darf nie den Raw-Snippetcall enthalten.
  - Wenn fuer eines der elf Hero-Module `*_use_snippetcall_salutation = true` materialisiert wurde, muss das produktive Hero-Snippet im Export statt `*_salutation` exakt diesen fest codierten Iterable-Logik-Block ausgeben:
    - `{{#ifContainsStr firstName 'NULL'}} Hallo, {{else if firstName}} Hallo {{firstName}}, {{else}} Hallo, {{/ifContainsStr}}`
  - Diese Ersetzung ist ausschliesslich fuer dokumentierte Salutation-Kontexte wie `rle` erlaubt.
  - Freie User-Snippetcalls, freie Raw-Logic in `*_salutation`, freie HTML-Interpolation oder andere undokumentierte Roh-Logik-Wege bleiben verboten.
- Fuer `salutationContext = loft-snl` gilt in dieser Minimalstufe weiter `mode = template_builtin`: Der Export nutzt unveraendert die bestehende template- oder snippet-spezifische Anrede-Logik und fuehrt keine zusaetzliche zentrale Raw-Substitution ein.
- Fuer `salutationContext = loft-rnl-dev` gilt genau eine dokumentierte Feld-Materialisierung:
  - wenn das Modul `loft-rnl-dev-intro` exportiert wird, muss `emb_loft_rnl_dev_intro_salutation` als Snippet-Parameterwert kontrolliert auf den in `agent/product-salutations.json` dokumentierten festen Handlebars-Ausdruck gesetzt werden
  - `emb_loft_rnl_dev_intro_headline` und `emb_loft_rnl_dev_intro_body` bleiben normale Builder-Felder
  - der feste Handlebars-Ausdruck darf nie als freier User-Content, nie als Preview-Text und nie als direkt editierbares Feld exponiert werden
- Fuer `salutationContext = loft-regio-resi` gilt genau eine dokumentierte Feld-Materialisierung:
  - wenn das Modul `loft-regio-resi-intro` exportiert wird, muss `emb_loft_regio_resi_intro_salutation` als Snippet-Parameterwert kontrolliert auf den in `agent/product-salutations.json` dokumentierten festen Handlebars-Ausdruck gesetzt werden
  - `emb_loft_regio_resi_intro_headline` und `emb_loft_regio_resi_intro_body` bleiben normale Builder-Felder
  - der feste Handlebars-Ausdruck darf nie als freier User-Content, nie als Preview-Text und nie als direkt editierbares Feld exponiert werden
- `rich_inline`-Felder im `email_state.content` duerfen nur sanitisiertes builder-eigenes Inline-HTML enthalten.
- `rich_full`-Felder im `email_state.content` duerfen nur sanitisiertes builder-eigenes Richtext-HTML enthalten.
- Fuer `rich_inline` sind nur diese Tags erlaubt:
  - `strong`
  - `em`
  - `a`
  - `br`
- Fuer `rich_full` sind nur diese Tags erlaubt:
  - `p`
  - `ul`
  - `ol`
  - `li`
  - `strong`
  - `em`
  - `a`
  - `br`
- Andere Tags, freie Wrapper, Skripte, Styles, Event-Handler, Klassen und freie Attribute sind verboten.
- Erlaubte Attribute in Richtext-Feldern sind auf sichere Link-Attribute begrenzt:
  - bei `a`: `href`, `target`, `rel`
- Wenn ein Modul-Snippet `{{{...}}}` fuer `rich_inline` oder `rich_full` nutzt, muss der Export den bereits sanitisierten HTML-Fragmentwert aus `email_state.content` unveraendert in den Snippet-Call uebernehmen und darf ihn nicht zu Plain Text abwerten.
- Vertikale Abstaende zwischen Absaetzen und Listen innerhalb eines `rich_full`-Felds bleiben ausschliesslich Aufgabe des allgemeinen `rich_full`-Renderkontexts, nicht des Feldinhalts vor oder ausserhalb davon.
- Fuer den allgemeinen `rich_full`-Renderkontext gilt:
  - Text zu Text = 16px
  - Text zu Liste = 8px
  - Liste zu Text = 8px
  - Liste zu Liste = 8px
- Der Abstand zwischen einer Headline und dem ersten `rich_full`-Element ist externer Kontextabstand und keine Aufgabe des `rich_full`-Feldwerts.
- Wenn eine Liste das erste Element im `rich_full`-Feld ist, bekommt sie keinen zusaetzlichen internen Top-Abstand.
- Listen bleiben im allgemeinen `rich_full`-Kontext optisch auf 20px eingerueckt.
- `p`, `ul` und `ol` tragen im allgemeinen `rich_full`-Kontext keine eigenen allgemeinen Top-/Bottom-Defaults ausserhalb der zentralen Flow-Regeln.
- Blueprint-basierte Previews duerfen nur exportiert werden, wenn ihr `email_state` zuvor auf das vollstaendige Feldset der verwendeten Module aus `export-map.json` normalisiert wurde.
- Wenn der `email_state` fehlt oder fuer die aktuelle Preview unvollstaendig ist, darf genau einmal ein enger Recovery-Fallback aus der letzten sichtbaren Preview aufgebaut werden.
- Dieser Recovery-Fallback bleibt streng begrenzt:
  - nur letzte sichtbare Preview
  - nur registrierte Module
  - nur explizit markierte sichtbare Felder, marker-basierte URL-Felder aus `data-export-url-field`, registrierte Icon-Slots, registrierte Bild-Slots, Moduldefaults aus `export-map.json` und dokumentierte technische Resolver-Quellen
  - kein Raten aus Button-Klassen, freiem Modulkontext, sichtbarem CSS-Styling oder unmarkierter DOM-Struktur
  - danach vollstaendige Validierung gegen `export-map.json`
  - anschliessend den reparierten `email_state` wieder als operative JSON-Arbeitsdatei fortschreiben
- Snippet-HTML bleibt auch im Recovery-Fallback verboten als Export-Erkennungsquelle.

## Ziel und Save-Shell

- `DEFAULT_TEMPLATE_ID = 569946`
- Freie und Blueprint-Mails ohne aktives Composition-Template nutzen im Export immer `DEFAULT_TEMPLATE_ID`.
- Fuer `templateContext.mode = default_template` ist `email/templates/template-main.html` die einzige kanonische Repo-Referenz fuer die erwartete Default-Shell-Vollstaendigkeit.
- Andere lokale `email/templates/*.html` sind in diesem Modus ausschliesslich template-spezifische Shells fuer ihren passenden `composition_template`-Kontext und duerfen nie als Ersatz-, Fallback- oder Rekonstruktionsquelle fuer `template-main` genutzt werden.
- Builder-Export erzeugt bewusst keine Blast-/Send-Campaign und uebergibt deshalb keine Versandliste an `createCampaign`.
- Review-Dateien unter `development/review/` sind fuer Modul- und Template-Arbeit reine Test-Artefakte und nie operativ.
- Review-Dateien unter `development/review/` duerfen fuer Template-Tests vollstaendig zusammengebaut sein, sind aber nie Quelle fuer den Export.
- Review-Dateien duerfen Demo-Texte und Demo-Bilder enthalten, aber keine frei erfundenen Styles, Farben, Spacings, CTA-Farben oder Modul-Defaults.
- Wenn Review-Dateien bestehende Defaults brauchen, muessen diese aus den operativen EMB-Quellen kommen, insbesondere aus `export-map.json`, produktiven Modulen, `email/templates/template-main.html` und `agent/preview-styles.css`.
- Wenn ein aktives Composition-Template genutzt wird, wird dessen Definition immer ueber `template_id` adressiert:
  - `agent/template-<template_id>.definition.json`
- Wenn `iterable_template_id` in dieser namespaceten Definition eine Zahl ist, muss diese ID als Basis-`templateId` fuer `createCampaign` verwendet werden.
- Wenn ein aktives Composition-Template genutzt wird und `iterable_template_id = null` ist, darf kein Iterable-Export stattfinden.
- Das zugehoerige Iterable-Basistemplate liegt fuer Composition-Templates immer unter `email/templates/<template_id>.html` und darf keine festen Module oder festen Snippet-Calls enthalten.
- Der erste Export einer Preview erzeugt genau eine neue Campaign.
- Jeder Folge-Export derselben fortgeschriebenen Preview muss dieselbe bereits zugeordnete Campaign wiederverwenden und darf keine zweite Campaign erzeugen.
- Draft ist kein Standard- und kein Fallback-Ziel.
- Im regulaeren Export gibt es genau vier externe Export-Aktionen: `createCampaign`, genau einen `campaignRead` nur fuer die campaign-owned `templateId` und den `campaignState`, genau einen `templateRead` der aktuellen campaign-owned HTML-Shell und den finalen HTML-Write.
- Campaign-Read ist nur direkt nach `createCampaign` zum Holen der campaign-owned `templateId` und zur Status-Validierung erlaubt.
- Template-Read ist genau einmal erlaubt und dient ausschliesslich dazu, die aktuelle campaign-owned HTML-Shell fuer den finalen Shell-Merge zu lesen.
- `SNIPPET_CALLS` duerfen nie als nacktes Komplett-HTML gespeichert werden.
- Das finale `html` fuer den Write-Schritt entsteht lokal genau einmal aus `email_state + export-map.json` plus der genau einmal gelesenen campaign-owned HTML-Shell und wird danach genau einmal auf dem campaign-owned Template geschrieben.
- Die Default-Shell darf nie aus Prompt-Wissen, Tests, gekuerzten Wrapper-Beispielen oder anderen Template-Dateien sinngemaess neu aufgebaut werden; fuer `default_template` bleibt `email/templates/template-main.html` nur die kanonische Repo-Referenz, waehrend die Write-Payload ausschliesslich aus der gelesenen campaign-owned HTML-Shell entsteht.
- Ein Standalone-Template-Save ist verboten, solange der User nicht ausdruecklich `Speichere als Template in Iterable` verlangt.

## Finaler HTML-Schritt

- Der finale HTML-Schritt besteht genau aus zwei lokalen Teilphasen und einem Write:
  1. Modularen Snippet-Call-Block lokal exakt einmal aus `email_state + export-map.json` bauen.
  2. In der genau einmal gelesenen campaign-owned HTML-Shell ausschliesslich die erlaubten Replace-Zonen fuer Subject, Preheader und den modularen Slot identifizieren und nur dort den neuen Inhalt einsetzen.
  3. Genau diese vollstaendige finale HTML-Payload nach Iterable schreiben.
- Die Payload wird lokal nur einmal zusammengefuegt; doppelte HTML-Builds, Shell-Neubauten oder nachgelagerte Rebuilds sind verboten.
- Die campaign-owned HTML-Shell muss ausserhalb der erlaubten Replace-Zonen byte-faithful erhalten bleiben.
- Im regulaeren Full-Mail-Export sind genau diese Replace-Zonen erlaubt: Subject, Preheader und Module-Slot.
- Head, CSS, Media Queries, Wrapper-Struktur und Conditional Comments der gelesenen HTML-Shell duerfen nicht gekuerzt, ersetzt oder neu zusammengesetzt werden.
- Die finale HTML-Payload gilt nur dann als write-faehig, wenn sie lokal vollstaendig gebaut wurde, weiterhin eine vollstaendige HTML-Shell enthaelt und keine freie Minimal-Shell ist.
- Ein lokaler Fehler beim Snippet-Block, beim Shell-Merge oder bei der Payload-Vollstaendigkeit ist kein Write-Fehler, sondern ein lokaler Build-Fehler.

## HTML WRITE - VERBINDLICH

- Nach `createCampaign` und genau einem `campaignRead` gilt fuer den finalen Write-Step ausschliesslich dieser technische Vertrag.
- Die campaign-owned `templateId` muss ausschliesslich aus `response.templateId` der `campaignRead`-Response extrahiert werden.
- Fuer den HTML-Write ist ausschliesslich dieser Endpoint erlaubt:
  - `POST /api/templates/email/update`
- Der Write-Payload muss immer exakt diese Felder enthalten:
  - `templateId`: campaign-owned `templateId` aus `response.templateId`
  - `html`: finale HTML-Payload
  - `subject`: Subject der aktuellen Mail
  - `preheaderText`: Preheader der aktuellen Mail
- Vor dem Write muessen verbindlich genau diese Bedingungen erfuellt sein:
  - `templateId` ist vorhanden
  - `html` ist nicht leer
  - `subject` ist vorhanden
  - `preheaderText` ist vorhanden
- Wenn eine dieser Bedingungen nicht erfuellt ist, endet der Export sofort vor dem Write.
- Nach dem Write muss der HTTP-Status geprueft werden.
- Bei Write-Fehlern muessen HTTP-Status und vollstaendiger Response-Body lokal geloggt werden.
- Der Write gilt nur dann als erfolgreich, wenn kein API-Fehler zurueckkommt.
- Alternative Write-Endpoints, alternative Write-Payloads oder implizite Write-Methoden sind verboten.

## Lokale Payload-Pruefung vor dem Write

- Direkt vor dem finalen Write laeuft genau eine kleine lokale Vorpruefung.
- Diese Vorpruefung muss mindestens bestaetigen:
  - campaign-owned HTML-Shell ist vorhanden
  - Subject ist vorhanden
  - Preheader ist vorhanden
  - modularer Snippet-Call-Block ist vorhanden
  - die finale HTML-Payload wurde lokal genau einmal zusammengefuegt
  - finale HTML-Payload ist nicht leer
  - finale HTML-Payload enthaelt weiterhin eine vollstaendige HTML-Shell
  - finale HTML-Payload ist nicht nur nackter Snippet-Text
  - finale HTML-Payload enthaelt den eingesetzten modularen Block
  - ausserhalb der erlaubten Replace-Zonen gibt es keine Abweichung zur gelesenen campaign-owned HTML-Shell
- Wenn eine dieser Pruefungen scheitert, wird kein Write versucht.
- In diesem Fall endet derselbe Export sofort mit einer klaren lokalen Fehlerklasse.

## CreateCampaign Gate

- `DEFAULT_TEMPLATE_ID = 569946`
- Der CreateCampaign-Schritt ist ein harter Gate-Step.
- CreateCampaign ist nur zulaessig, wenn die aktuelle Preview noch keine zugeordnete verwertbare `campaignId` hat.
- Wenn ein aktives Composition-Template genutzt wird, ist dessen `iterable_template_id` die einzige erlaubte Basis-`templateId` fuer `createCampaign`.
- Wenn kein Composition-Template genutzt wird, bleibt `DEFAULT_TEMPLATE_ID = 569946` die einzige erlaubte Basis-`templateId` fuer `createCampaign`.
- Wenn ein aktives Composition-Template genutzt wird und dessen `iterable_template_id = null` ist, endet der Export sofort vor dem API-Call.
- Der CreateCampaign-Basispayload muss immer exakt diese Felder enthalten:
  - `name`: `CreativeOps_emb_YYYY-MM-DD`
  - `templateId`: aktive Template-ID aus dem Exportkontext:
    - bei aktivem Composition-Template: `iterable_template_id` aus `agent/template-<template_id>.definition.json`
    - sonst: `569946` aus `DEFAULT_TEMPLATE_ID`
- Die fuer `createCampaign` verwendete Basis-`templateId` ist ausschliesslich der Basis-Template-Parameter fuer `createCampaign`.
- Der finale HTML-Write darf nie `569946` oder `campaignId` als `templateId` verwenden.
- `listIds`, `sendAt`, `scheduleSend`, `sendMode` und `recipientTimeZone` sind im CreateCampaign-Request des Builder-Exports verboten.
- Der Builder-Export darf keine Scheduling- oder Versandparameter an `createCampaign` uebergeben.
- Falls spaeter eine Versandliste benoetigt wird, ist das ein separater manueller Iterable-Schritt ausserhalb dieses Export-Flows.
- Platzhalterwerte, leere Arrays und frei erfundene Versand- oder Scheduling-Felder sind im CreateCampaign-Request verboten.
- Der Export darf nur fortgesetzt werden, wenn die CreateCampaign-Antwort verwertbar ist.
- Eine verwertbare CreateCampaign-Antwort braucht genau eine extrahierbare Campaign-ID.
- Als ID-Kandidaten duerfen nur diese Felder geprueft werden:
  - `campaignId`
  - `id`
  - `response.campaignId`
  - `response.id`
  - `data.campaignId`
  - `data.id`
  - `campaign.campaignId`
  - `campaign.id`
- Jeder ID-Kandidat ist nur gueltig, wenn er als `number` oder `string` vorliegt.
- Die erste verwertbare extrahierte Campaign-ID muss intern als String normalisiert werden.
- Wenn aus diesen Kandidaten keine verwertbare ID extrahiert werden kann, ist der Export sofort fehlgeschlagen.
- Direkt nach dem CreateCampaign-Call muessen der finale Request ohne Secrets, die Information ueber vorhandenen oder fehlenden HTTP-Status, die Information ueber vorhandenen oder fehlenden Raw-Response-Body sowie die komplette verwertbare Tool-Antwort lokal erfasst werden.
- Auf den CreateCampaign-Call muss explizit gewartet werden; der Export darf erst weiterlaufen, wenn die vollstaendige Response technisch empfangen und lokal verfuegbar ist.
- Die Response-Verarbeitung von CreateCampaign besteht verbindlich aus:
  1. API-Call echt ausfuehren
  2. Response vollstaendig empfangen
  3. nur die erlaubten ID-Kandidaten pruefen
  4. extrahierte Campaign-ID validieren und intern zu String normalisieren
  5. genau einen `campaignRead` mit dieser normalisierten `campaignId` ausfuehren
  6. aus diesem `campaignRead` ausschliesslich `response.templateId` als campaign-owned `templateId` und `response.campaignState` zur Status-Validierung lesen
  7. genau einen `templateRead` der aktuellen campaign-owned HTML-Shell mit diesem `templateId` ausfuehren
  8. nur dann den HTML-Write starten, wenn `campaignState` explizit editierbar ist; `Ready` ist der bevorzugte erwartete Status
- `campaignId` identifiziert die Campaign-Bindung und darf nie als `templateId` interpretiert oder weitergereicht werden.
- Der finale HTML-Write braucht die campaign-owned `templateId` der neu erstellten oder bereits gebundenen Campaign.
- Bei Erfolg ist nur ein Minimal-Log mit `campaignId` und `name` zulaessig.
- Bei Fehlern ist ein Voll-Log mit finalem Request ohne Secrets, HTTP-Status-Info, Raw-Body-Info, geprueften ID-Kandidaten, Ablehnungsgrund der Kandidaten und Tool-Antwort-/Envelope-Info Pflicht.
- Wenn die Tool-Antwort leer, unparsebar, unvollstaendig oder anderweitig nicht verwertbar ist, endet dieser Export sofort als Tool-Runtime-/Envelope-Fehler.
- Wenn ein HTTP-Status vorliegt, aber der Status oder Body keine verwertbare ID liefert, endet dieser Export sofort als Iterable-API-Fehler.
- Wenn ein Body vorliegt, aber die ID nur in einer unbekannten Struktur liegt, endet dieser Export sofort als Parser-Fehler.
- Ohne `campaignId` darf kein HTML-Write und kein weiterer Exportschritt starten.
- Ohne `campaignId` gibt es keinen zweiten best-effort-Lauf und keinen impliziten Reparaturversuch im selben Export.
- Nach einem fehlgeschlagenen Create ohne verwertbare `campaignId` darf weder automatisch ein neuer Create noch ein Update-/Write-Versuch gestartet werden.
- Ein erneuter Exportversuch ist erst nach neuer expliziter User-Freigabe zulaessig.
- Im Export-Flow sind automatische Send-, Schedule- und weitere Template-Read-Schritte nach `createCampaign` verboten.
- Nach `createCampaign` ist genau ein `campaignRead` erlaubt, und zwar ausschliesslich zum Holen der campaign-owned `templateId` und zur Status-Validierung.
- Nach bekanntem `templateId` ist genau ein `templateRead` der aktuellen campaign-owned HTML-Shell erlaubt.
- Der Builder-Export erwartet nach `createCampaign` bevorzugt `campaignState = Ready`.
- Bei `Scheduled`, `Running`, `Finished`, `Archived`, `Recurring`, `Aborted` oder jedem anderen nicht explizit als editierbar belegten Status stoppt der Export sofort vor dem Write.
- Ein zusaetzlicher Status-Reset-Call ist im Export nicht erlaubt, solange Iterable dafuer keinen offiziell dokumentierten Endpoint fuer `Ready` oder `Draft` bereitstellt.
- Kein Status-Reset, kein Cancel, kein Archive und keine sonstige Reparatur einer nicht editierbaren Campaign per Agent.
- Neue Campaigns muessen beim Create-Schritt standardmaessig nach dem festen Schema `CreativeOps_emb_YYYY-MM-DD` benannt werden.
- Dabei ist `CreativeOps_emb` der feste Prefix; das Datum muss aus dem aktuellen Lauf stammen und im Format `YYYY-MM-DD` gesetzt werden.
- Freie generische Namen wie `Test Mail`, `Preview Mail` oder aehnliche Platzhalter sind fuer neue Campaigns nicht zulaessig.
- Wenn fuer die aktuelle Preview bereits eine verwertbare `campaignId` im aktuellen Export-State vorliegt, ist ein erneuter CreateCampaign-Schritt verboten; dann muss genau diese bestehende Campaign aktualisiert werden.

## Verbindlicher Happy Path

Im direkten Happy Path laeuft der Export genau in dieser Reihenfolge:

1. Aktuellen `email_state` lesen.
2. Wenn dieser `email_state` fehlt oder unvollstaendig ist: genau einmal einen engen Recovery-Fallback aus der letzten sichtbaren Preview aufbauen und anschliessend als `email_state` fortschreiben.
3. Gegen `export-map.json` jedes Modul, `snippet_name` und jedes Feld validieren.
4. Required Felder aus `content` oder den Defaults der Export-Map befuellen.
5. Nur wenn keine verwertbare `campaignId` fuer diese Mail vorliegt: den CreateCampaign-Request exakt mit `name` und der aktiven Basis-`templateId` aus dem Exportkontext bauen.
6. Wenn Schritt `5` lief: genau einen CreateCampaign-Call ausfuehren, explizit auf die vollstaendige Response warten und bei Fehlern finalen Request ohne Secrets, HTTP-Status-Info, Raw-Body-Info und Tool-Antwort-/Envelope-Info lokal erfassen.
7. Wenn Schritt `6` lief: aus der vollstaendig empfangenen Create-Antwort nur die erlaubten ID-Kandidaten pruefen, die erste verwertbare Campaign-ID extrahieren, validieren und intern als String normalisieren. Wenn keine verwertbare ID extrahierbar ist oder die Antwort leer, unparsebar oder unvollstaendig ist: Export sofort abbrechen.
8. Wenn Schritt `6` lief: genau einen `campaignRead` mit dieser `campaignId` ausfuehren und daraus ausschliesslich `response.templateId` als campaign-owned `templateId` sowie `response.campaignState` lesen. Wenn `templateId` fehlt, `campaignState` nicht explizit editierbar ist oder `campaignState` nicht als `Ready` oder anderer belegter editierbarer Status akzeptiert werden kann: Export sofort abbrechen. Bei `Scheduled`, `Running`, `Finished`, `Archived`, `Recurring` oder `Aborted` stoppt der Export immer sofort. Wenn Schritt `6` nicht lief, muss die bereits gebundene campaign-owned `templateId` fuer genau diese Mail im aktuellen Export-State vorliegen; fehlt sie, Export sofort abbrechen.
9. Mit diesem verfuegbaren campaign-owned `templateId` genau einen `templateRead` der aktuellen campaign-owned HTML-Shell ausfuehren. Wenn die Shell leer, unvollstaendig oder nicht lesbar ist, Export sofort abbrechen.
10. Modularen Snippet-Call-Block lokal genau einmal aus `email_state + export-map.json` bauen und nur in die erlaubten Replace-Zonen der gelesenen campaign-owned HTML-Shell einsetzen.
11. Finale HTML-Payload lokal kurz pruefen.
12. Nur wenn `templateId`, `html`, `subject` und `preheaderText` vollstaendig vorliegen, `campaignState` explizit editierbar ist, `campaignState` nicht `Scheduled`, `Running`, `Finished`, `Archived`, `Recurring` oder `Aborted` ist und die campaign-owned HTML-Shell ausserhalb der Replace-Zonen unveraendert blieb: genau einen Write ueber `POST /api/templates/email/update` mit `templateId`, `html`, `subject` und `preheaderText` ausfuehren.
13. Beim Write den HTTP-Status pruefen; bei Fehlern HTTP-Status und vollstaendigen Response-Body loggen und Export sofort abbrechen.
14. Nach einem erfolgreichen erstmaligen Export die `campaignId` und die campaign-owned `templateId` an genau diese aktuelle Mail und ihren `email_state` zurueckschreiben.

- Ein zusaetzlicher QA-Read ist optional, nicht verpflichtend.
- Weitere Iterable-Calls ausser `createCampaign`, genau einem `campaignRead` fuer die campaign-owned `templateId`, genau einem `templateRead` der campaign-owned HTML-Shell und dem finalen HTML-Write sind im Happy Path verboten.

## Happy Path

- Fuer die unterstuetzten Module gilt das statische Export-Mapping aus `export-map.json`.
- Im direkten Happy Path wird der aktuelle `email_state` genau einmal lokal in den modularen Snippet-Call-Block uebersetzt und genau einmal mit der gelesenen campaign-owned HTML-Shell zusammengefuehrt.
- Der `email_state` ist dabei die einzige feldnahe Arbeitskopie fuer den Export.
- `export-map.json` ist die einzige technische Feld- und Modulwahrheit fuer den Export.
- Bekannte Snippet-Namen, Pflichtparameter, feste Werte und Defaults werden nicht erneut lang hergeleitet.
- Keine doppelte Uebersetzung, keine doppelte Rekonstruktion, keine schrittweise Technik-Erklaerung im Chat.
- Keine unnoetigen Iterable-Read-Backs fuer Informationen, die lokal bereits feststehen, ausser dem verpflichtenden einen `templateRead` der campaign-owned HTML-Shell.
- Keine Snippet-Inspection-Schleifen fuer bekannte Module im Fast-Path.
- Keine erneute Signatur-Pruefung einzelner Fast-Path-Module waehrend des Exports.
- Wenn `export-map.json` fuer ein Modul ein vollstaendiges Feldset definiert, ist genau dieses Feldset direkt auszufuehren.
- Preview-HTML oder Snippet-HTML werden im Happy Path nicht gescannt.
- Der Recovery-Fallback ist kein zweiter Happy Path, sondern nur ein einmaliger Reparaturschritt, wenn `email_state` fehlt oder unvollstaendig ist.

## Export Fast Path

- Der normale Export-Happy-Path ist ein Runtime-Fast-Path und bewertet nur die fuer den Write unmittelbar noetigen Quellen und Schritte.
- Dieser Runtime-Fast-Path veraendert den fachlichen Export-Flow nicht, sondern begrenzt nur den regulaeren Pruefkontext im fehlerfreien Exportfall.
- Im normalen Export ohne Fehler und ohne Recovery-Fallback gilt genau diese operative Reihenfolge:
  1. vorhandenen `email_state` verwenden
  2. gegen `export-map.json` validieren
  3. `createCampaign` nur mit `name` und `templateId`, falls keine verwertbare `campaignId` existiert
  4. genau einen `campaignRead`
  5. genau einen `templateRead` der campaign-owned `templateId`
  6. Snippet-Block und finale HTML-Payload lokal bauen
  7. finale Payload lokal pruefen
  8. genau einen HTML-Write ausfuehren
  9. kurze Abschlussmeldung ausgeben
- Solange kein Fehler, kein fehlender `email_state` und kein ausdruecklich benoetigter Recovery-Fallback vorliegt, wertet der Agent fuer den normalen Export-Happy-Path diese Quellen und Kontexte nicht erneut aus:
  - `preview-modules.html`
  - `preview-module-library.md`
  - `preview-template.html`
  - `template-*.preview.html`
  - Preview-HTML-Strukturen der letzten sichtbaren Mail
  - Modul-Design-Dokumentation
  - Parity-, Integrations- oder Modulpflege-Regeln
  - Design-Library-Regeln
- Diese Ausschluesse gelten nur fuer den normalen Export-Happy-Path.
- Fuer Preview-Erstellung, Recovery-Fallback, Modulpflege, Template-Arbeit, Integrationsarbeit und Fehleranalyse bleiben diese Dateien und Regelbereiche weiterhin gueltige Agent-Quellen.
- Wenn der normale Export-Happy-Path wegen fehlendem oder unvollstaendigem `email_state`, Mapping-Fehlern, Payload-Fehlern oder API-/Status-Fehlern verlassen werden muss, greifen wieder die regulaeren Fail-Closed-, Recovery- und Fehlerregeln dieser Datei.
- Auch im Runtime-Fast-Path bleiben alle Sicherheitsstopps, Pflichtvalidierungen, Statuspruefungen, Write-Voraussetzungen und Fail-Closed-Regeln vollstaendig aktiv.

## Exporttreue

- Die technische Iterable-Mail muss dieselbe Mail sein wie die letzte Preview:
  - gleiches Subject
  - gleicher Preheader
  - gleiche Modulfolge
  - gleiche Modultypen
  - gleiche Inhalte
  - gleiche CTA-Ziele
  - gleiche sichtbare Teilbereiche
  - gleiche sichtbare Item-Anzahl

## Text-QA

- Vor dem finalen Campaign-Write muessen generierte deutsche Fliesstexte bereits direkt korrekt mit echten Umlauten vorliegen.
- `ae`, `oe` und `ue` sind als Umlaut-Ersatz in normalem deutschem Fliesstext nicht zulaessig, ausser bei Eigennamen, URLs, E-Mail-Adressen und technischen Werten.
- Im Export gibt es keine nachgelagerte Umlaut-Korrektur, keine ASCII-Normalisierung und keine sonstige Zeichenumwandlung.
- Wenn generierter deutscher Fliesstext vor dem Export noch Umlaut-Ersatzschreibungen enthaelt, ist das ein lokaler Textfehler und der Export blockiert.

## Fail Closed

- Eine bestehende `campaignId` darf nur dann wiederverwendet werden, wenn sie im aktuellen Export-State genau der aktuellen fortgeschriebenen Preview zugeordnet ist.
- Eine Campaign-Bindung aus einer frueheren, verlassenen oder neu gestarteten Preview darf nie auf eine neue Preview uebertragen werden.
- Vor jedem weiteren Exportschritt nach CreateCampaign muss eine verwertbare `campaignId` vorliegen.
- Wenn im Builder-Export `listIds` im CreateCampaign-Request auftaucht, scheitert der Export sofort vor dem API-Call.
- Wenn kein Composition-Template genutzt wird und der CreateCampaign-Request vom Standard-Payload mit `templateId = 569946` ohne weitere Versand- oder Scheduling-Felder abweicht, scheitert der Export sofort vor dem API-Call.
- Wenn ein aktives Composition-Template genutzt wird und der CreateCampaign-Request nicht exakt dessen `iterable_template_id` als `templateId` sowie sonst keine Versand- oder Scheduling-Felder verwendet, scheitert der Export sofort vor dem API-Call.
- Wenn ein aktives Composition-Template genutzt wird und `iterable_template_id = null` ist, scheitert der Export sofort vor dem API-Call.
- Wenn `sendAt` im CreateCampaign-Request auftaucht, scheitert der Export sofort vor dem API-Call.
- Wenn `scheduleSend` im CreateCampaign-Request auftaucht, scheitert der Export sofort vor dem API-Call.
- Wenn `sendMode` oder `recipientTimeZone` im CreateCampaign-Request auftauchen, scheitert der Export sofort vor dem API-Call.
- Wenn die CreateCampaign-Antwort keine verwertbare extrahierbare Campaign-ID in den erlaubten Kandidaten enthaelt, scheitert der Export sofort.
- Wenn die CreateCampaign-Antwort leer, unparsebar oder unvollstaendig ist, scheitert der Export sofort.
- Wenn auf die CreateCampaign-Response nicht explizit gewartet wurde oder die Response-Verarbeitung offen bleibt, scheitert der Export sofort.
- Wenn `campaignId` im Write-Schritt als `templateId` verwendet oder an einen Template-Write gebunden wuerde, scheitert der Export sofort.
- Wenn fuer den Write-Schritt keine campaign-owned `templateId` fuer genau diese Campaign vorliegt, scheitert der Export sofort.
- Wenn die campaign-owned `templateId` nicht explizit aus `response.templateId` des einen erlaubten `campaignRead` stammt, scheitert der Export sofort.
- Wenn der eine erlaubte `campaignRead` nach `createCampaign` nicht ausgefuehrt oder fuer etwas anderes als die campaign-owned `templateId` und den `campaignState` genutzt wird, scheitert der Export sofort.
- Wenn der eine erlaubte `campaignRead` `campaignState = Scheduled` zurueckliefert, scheitert der Export sofort vor dem Write.
- Wenn der eine erlaubte `campaignRead` `campaignState = Running`, `Finished`, `Archived`, `Recurring` oder `Aborted` zurueckliefert oder der Status sonst nicht explizit als editierbar belegbar ist, scheitert der Export sofort vor dem Write.
- Ohne `campaignId` sind HTML-Write und jeder weitere Exportschritt verboten.
- Wenn fuer die aktuelle Preview bereits eine verwertbare `campaignId` vorliegt, darf kein zweiter CreateCampaign-Schritt fuer denselben Preview-Zweig gestartet werden.
- Bei leerer oder unbrauchbarer CreateCampaign-Antwort endet derselbe Lauf sofort; kein spontaner Reparaturversuch, kein zweiter best-effort-Write und kein weiterer Folgeversuch im selben Export.
- Wenn keine verwertbare Campaign-ID extrahiert werden kann, muss die Fehlerausgabe exakt `Iterable createCampaign hat keine gueltige campaignId zurueckgegeben` enthalten, die Fehlerklasse benennen, den finalen Request ohne Secrets, die HTTP-Status-Info, die Raw-Body-Info, die geprueften ID-Kandidaten, den Ablehnungsgrund und den Hinweis `Kein Campaign-Read und kein HTML-Write wurden ausgefuehrt.` enthalten.
- Wenn `campaignId` nach CreateCampaign fehlt, darf der Agent nicht automatisch eine weitere Kampagne anlegen und nicht selbststaendig in einen neuen Exportlauf wechseln.
- Wenn fuer einen Folge-Export mit bereits vorhandener `campaignId` keine bereits gebundene campaign-owned `templateId` im aktuellen Export-State vorliegt, scheitert der Export sofort.
- Wenn kein `templateRead` der aktuellen campaign-owned HTML-Shell ausgefuehrt wurde, scheitert der Export sofort.
- Wenn mehr als ein `templateRead` im selben Export-Lauf ausgefuehrt wurde, scheitert der Export sofort.
- Im selben Export-Lauf ist nur genau ein `campaignRead` erlaubt, und zwar ausschliesslich direkt nach `createCampaign` zum Holen der campaign-owned `templateId`.
- Im selben Export-Lauf ist nur genau ein `templateRead` erlaubt, und zwar ausschliesslich zum Lesen der aktuellen campaign-owned HTML-Shell.
- Vor dem Write muss ein gueltiger `email_state` vorliegen.
- Wenn die finale HTML-Payload lokal mehr als einmal zusammengefuegt wuerde, scheitert der Export sofort.
- Wenn keine Campaign-ID sauber aus den erlaubten ID-Kandidaten der vollstaendig empfangenen CreateCampaign-Response extrahiert und als String normalisiert werden kann, scheitert der Export sofort.
- Wenn die campaign-owned `templateId` nicht verfuegbar ist, darf kein Write mit `campaignId` als Ersatzwert gestartet werden.
- Wenn fuer den Write ein anderer Endpoint als `POST /api/templates/email/update` verwendet wuerde, scheitert der Export sofort.
- Wenn der Write-Payload nicht exakt `templateId`, `html`, `subject` und `preheaderText` enthaelt, scheitert der Export sofort.
- Wenn `subject` oder `preheaderText` vor dem Write fehlen, scheitert der Export sofort.
- Wenn die finale HTML-Payload lokal leer, unvollstaendig oder ohne vollstaendige HTML-Shell ist, scheitert der Export sofort.
- Wenn die finale HTML-Payload die gelesene campaign-owned HTML-Shell ausserhalb der erlaubten Replace-Zonen veraendert, scheitert der Export sofort.
- Wenn die finale HTML-Payload eine freie Minimal-Shell, eine lokal neu erfundene Shell oder nur einen modularen Block ohne vollstaendige Template-Shell enthaelt, scheitert der Export sofort.
- Wenn die finale HTML-Payload lokal nur aus nacktem Snippet-Text besteht, scheitert der Export sofort.
- Wenn die lokale Payload-Pruefung scheitert, wird kein Write versucht.
- Jedes aktive Modul im `email_state` muss genau ein eindeutiges Export-Mapping aus `export-map.json` haben.
- Es duerfen nur Felder geschrieben werden, die fuer dieses Modul dort registriert sind.
- Unknown Fields im `email_state.content` fuehren sofort zu einem Fehler und werden nie exportiert.
- Pflichtfelder muessen ueber `content` oder Defaults der Export-Map vollstaendig befuellt werden.
- Wenn Modultyp, Mapping, Pflichtfelder oder `snippet_name` nicht sauber zusammenpassen, scheitert der Export.
- Wenn ein required `*_bg_color` im `email_state.content` fehlt, scheitert der Export.
- Wenn ein required `*_bg_color` im `email_state.content` nur als `theme-*`-Klasse, semantischer Farbname oder anderer nicht-konkreter Marker vorliegt, scheitert der Export.
- Wenn nach dem einmaligen Recovery-Fallback weiterhin kein vollstaendiger `email_state` vorliegt, scheitert der Export.
- `servicetiles` wird genau einmal ueber `module_id`, `snippet_name` und `content` exportiert; Desktop- und Mobile-Markup im Snippet sind reine Renderdetails.
- Fuer `servicetiles` muessen vor dem Snippet-Build genau vier Services bereits kontrolliert gegen `agent/service-products.json` auf die finalen Felder `emb_servicetiles_col_1..4_(icon_url|title|description|url)` materialisiert sein; fachliche Service-Namen oder `original_snippet_name` sind keine direkten Snippet-Parameter.
- `steps-3col` wird genau einmal ueber `module_id`, `snippet_name` und `content` exportiert; Desktop- und Mobile-Markup im Snippet sind reine Renderdetails.
- Wenn keine vollstaendige finale HTML-Payload lokal vorliegt, scheitert der Export.
- Wenn nur nackte `SNIPPET_CALLS` oder ein isolierter Modulblock geschrieben wuerden, scheitert der Export.
- Bei Write- oder Parameterfehlern endet derselbe Lauf sofort; kein spontaner Reparaturversuch und kein zweiter best-effort-Write.

## Fehlerklassen fuer Schritt 5

- A. `Finale HTML-Payload konnte nicht vollstaendig gebaut werden.`
- B. `Finale HTML-Payload verletzte die Template-Shell-Regel.`
- C. `Finale HTML-Payload wurde lokal gebaut, aber der Iterable-Write ist fehlgeschlagen.`
- D. `Finale HTML-Payload war lokal leer oder unvollstaendig.`
- E. `Finale HTML-Payload verletzt eine Fail-Closed-Regel und wurde nicht geschrieben.`

## Fehlerklassen fuer CreateCampaign

- A. `Tool-Runtime-/Envelope-Fehler bei Iterable createCampaign.` Dieser Fall gilt, wenn kein HTTP-Status, kein Raw-Body und keine sonst verwertbare Tool-Antwort vorliegen.
- B. `Iterable-API-Fehler bei createCampaign.` Dieser Fall gilt, wenn ein HTTP-Status vorliegt, aber der Status oder der Body keine verwertbare extrahierbare Campaign-ID liefert.
- C. `Parser-Fehler bei createCampaign.` Dieser Fall gilt, wenn ein Body vorliegt, aber keine ID in den erlaubten Kandidatenpfaden gefunden oder akzeptiert werden kann.

## Chat-Ausgabe

- Im normalen Exportmodus nur userfreundliche Kurzmeldungen ausgeben.
- Die komplette Preview-HTML oder finale Export-HTML darf im normalen Export-Flow nicht automatisch als grosser Chat-Block ausgegeben werden.
- Vollstaendiges HTML darf nur ausgegeben werden, wenn der User ausdruecklich danach fragt.
- Bei jedem regulären Iterable-Export muessen diese sichtbaren Statuspunkte in genau dieser Reihenfolge ausgegeben werden:
  - `1. Preview-Erstellung gestartet`
  - `2. Preview fertig`
  - `3. Export-Vorbereitung gestartet`
  - `4. Iterable-Export gestartet`
  - `5. Iterable-Export abgeschlossen`
  - `6. Iterable-Ergebnis bereit`
- `4. Iterable-Export gestartet` muss direkt vor dem ersten blockierenden externen Iterable-Schritt sichtbar ausgegeben werden und darf nicht uebersprungen werden.
- Wenn ein Export ohne neue Preview startet, bleiben die Statuspunkte `1` und `2` trotzdem als kurze Referenz auf den bereits vorhandenen Preview-Stand sichtbar; Punkt `4` bleibt weiterhin direkt vor dem eigentlichen Iterable-Call verpflichtend.
- Fuer die Chat-Ausgabe soll die Exportdauer lokal als Wandzeit des Export-Laufs von `3. Export-Vorbereitung gestartet` bis `6. Iterable-Ergebnis bereit` gemessen und nach erfolgreichem Abschluss genannt werden.
- Nach erfolgreichem Export muss die Ergebnis-Ausgabe kompakt bleiben und mindestens enthalten:
  - `campaignId=<id>`
  - `templateId=<id>`
  - `name=<name>`
  - `exportdauer=<dauer>`
  - einen kurzen Hinweis, wenn von der API kein direkter Iterable-UI-Link geliefert wurde
- Optionale technische Kurzpunkte wie `createCampaign: ok`, `campaignRead: ok`, `templateRead: ok` und `htmlWrite: ok` duerfen zusaetzlich erscheinen, aber nur nachgelagert und ohne die Pflicht-Statuspunkte zu ersetzen.
- Bei Fehlern:
  - `Der Export konnte nicht abgeschlossen werden. Grund: <kurze verstaendliche Ursache>.`
- Ausnahme fuer CreateCampaign-Fehler:
  - Wenn `createCampaign` keine gueltige `campaignId` liefert, muessen die Fehlermeldung `Iterable createCampaign hat keine gueltige campaignId zurueckgegeben`, die Fehlerklasse, der finale Request ohne Secrets, die HTTP-Status-Info, die Raw-Response-Body-Info, die geprueften ID-Kandidaten, der Ablehnungsgrund und der Hinweis `Kein Campaign-Read und kein HTML-Write wurden ausgefuehrt.` ausgegeben werden.
- Im normalen Exportmodus keine technischen Zwischenmeldungen ausgeben wie:
  - API-Hostnames
  - Endpoint-Namen
  - Recovery-Fallback
  - `export-map.json`
  - `email_state`
  - campaign-owned Template
  - Template-Shell
  - Replace-Zone
  - Slot-Erkennung
  - Snippet-Call-Block
  - HTML-Shell
  - interne IDs, ausser sie sind fuer den User wirklich noetig
  - technische Aussagen wie `ich lese jetzt`, `ich schreibe nun` oder aehnliche Debug-Schritte
- Auch wenn intern der Recovery-Fallback genutzt wurde, bleibt die Chat-Ausgabe im normalen User-Modus bei denselben kurzen Statusmeldungen und nennt diesen technischen Sonderfall nicht.
- Wenn der User ausdruecklich technische Details anfordert, duerfen Debug-Infos getrennt vom normalen Exportprozess erklaert werden, zum Beispiel zu API-Schritten, Ursache langer Laufzeiten oder technischer Fehleranalyse.
- Interne Speicher-, State-, Recovery- oder Zwischenmeldungen duerfen im normalen User-Flow nicht mehrfach oder ungefiltert sichtbar werden.
```

## email-builder/agent/export-map.json

Dateityp: json

```json
{
  "version": 1,
  "modules": [
    {
      "module_id": "logo",
      "snippet_name": "emb_logo",
      "fields": [],
      "notes": [
        "Static logo snippet. Export without parameters."
      ]
    },
    {
      "module_id": "logo-centered",
      "snippet_name": "emb_logo_centered",
      "fields": [],
      "notes": [
        "Static centered logo snippet. Export without parameters."
      ]
    },
    {
      "module_id": "hero-image-top",
      "snippet_name": "emb_hero_image_top",
      "fields": [
        {
          "name": "emb_hero_image_top_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_image_top_show_preheadline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_preheadline",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_show_badge",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_badge_bg_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_badge_text_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_badge_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_top_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_image_top_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_top_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_image_top_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_top_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_top_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-image-top-center",
      "snippet_name": "emb_hero_image_top_center",
      "fields": [
        {
          "name": "emb_hero_image_top_center_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_image_top_center_show_preheadline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_center_preheadline",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_center_show_badge",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_center_badge_bg_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_center_badge_text_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_center_badge_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_center_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_center_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_top_center_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_center_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_image_top_center_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_center_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_top_center_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_center_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_image_top_center_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_center_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_center_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_top_center_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_top_center_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-image-top-bleed",
      "snippet_name": "emb_hero_image_top_bleed",
      "fields": [
        {
          "name": "emb_hero_image_top_bleed_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_image_top_bleed_show_preheadline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_bleed_preheadline",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_show_badge",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_bleed_badge_bg_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_badge_text_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_badge_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_bleed_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_top_bleed_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_image_top_bleed_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_top_bleed_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_bleed_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_image_top_bleed_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_top_bleed_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_top_bleed_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-image-top-bleed-center",
      "snippet_name": "emb_hero_image_top_bleed_center",
      "fields": [
        {
          "name": "emb_hero_image_top_bleed_center_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_image_top_bleed_center_show_preheadline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_bleed_center_preheadline",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_center_show_badge",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_bleed_center_badge_bg_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_center_badge_text_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_center_badge_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_center_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_bleed_center_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_top_bleed_center_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_center_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_image_top_bleed_center_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_center_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_top_bleed_center_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_top_bleed_center_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_image_top_bleed_center_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_center_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_top_bleed_center_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_top_bleed_center_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_top_bleed_center_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-image-head-copy-bleed-center",
      "snippet_name": "emb_hero_image_head_copy_bleed_center",
      "fields": [
        {
          "name": "emb_hero_image_head_copy_bleed_center_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_head_copy_bleed_center_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-image-textbox-cta-center",
      "snippet_name": "emb_hero_image_textbox_cta_center",
      "fields": [
        {
          "name": "emb_hero_image_textbox_cta_center_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_image_textbox_cta_center_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_textbox_cta_center_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_textbox_cta_center_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_textbox_cta_center_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_image_textbox_cta_center_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_image_textbox_cta_center_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_image_textbox_cta_center_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_image_textbox_cta_center_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_image_textbox_cta_center_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_textbox_cta_center_question",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_textbox_cta_center_entry_url",
          "type": "url",
          "required": true,
          "default": "https://www.immobilienscout24.de/"
        },
        {
          "name": "emb_hero_image_textbox_cta_center_entry_text",
          "type": "text",
          "required": true,
          "default": "z.B. 10115 Berlin"
        },
        {
          "name": "emb_hero_image_textbox_cta_center_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_image_textbox_cta_center_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_textbox_cta_center_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_image_textbox_cta_center_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-fakeform-buttons-image",
      "snippet_name": "emb_hero_fakeform_buttons_image",
      "fields": [
        {
          "name": "emb_hero_fakeform_buttons_image_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_fakeform_buttons_image_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_fakeform_buttons_image_headline",
          "type": "text",
          "required": true,
          "default": "Reicht dein Eigenkapital für deine Wunschimmobilie?"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_1_url",
          "type": "url",
          "required": true,
          "default": "https://www.immobilienscout24.de/"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_1_label",
          "type": "text",
          "required": true,
          "default": "unter 10.000 €"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_show_item_2",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_2_url",
          "type": "url",
          "required": true,
          "default": "https://www.immobilienscout24.de/"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_2_label",
          "type": "text",
          "required": true,
          "default": "10.000–50.000 €"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_show_item_3",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_3_url",
          "type": "url",
          "required": true,
          "default": "https://www.immobilienscout24.de/"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_3_label",
          "type": "text",
          "required": true,
          "default": "50.000–100.000 €"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_show_item_4",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_4_url",
          "type": "url",
          "required": true,
          "default": "https://www.immobilienscout24.de/"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_4_label",
          "type": "text",
          "required": true,
          "default": "100.000–250.000 €"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_show_item_5",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_5_url",
          "type": "url",
          "required": true,
          "default": "https://www.immobilienscout24.de/"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_5_label",
          "type": "text",
          "required": true,
          "default": "über 250.000 €"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_show_item_6",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_6_url",
          "type": "url",
          "required": true,
          "default": "https://www.immobilienscout24.de/"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_choice_button_6_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_fakeform_buttons_image_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_fakeform_buttons_image_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_fakeform_buttons_image_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_fakeform_buttons_image_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_body",
          "type": "rich_full",
          "required": true,
          "default": "<p>Wähle aus, wie viel Eigenkapital du einplanst – wir zeigen dir passende nächste Schritte für deine Finanzierung.</p>"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_button_url",
          "type": "url",
          "required": true,
          "default": "https://www.immobilienscout24.de/"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_fakeform_buttons_image_button_label",
          "type": "text",
          "required": true,
          "default": "Jetzt prüfen"
        }
      ]
    },
    {
      "module_id": "hero-cta-top",
      "snippet_name": "emb_hero_cta_top",
      "fields": [
        {
          "name": "emb_hero_cta_top_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_cta_top_show_preheadline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_preheadline",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_show_badge",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_badge_bg_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_badge_text_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_badge_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_cta_top_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_cta_top_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_cta_top_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_cta_top_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_cta_top_button_label",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_cta_top_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-cta-top-center",
      "snippet_name": "emb_hero_cta_top_center",
      "fields": [
        {
          "name": "emb_hero_cta_top_center_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_cta_top_center_show_preheadline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_center_preheadline",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_center_show_badge",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_center_badge_bg_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_center_badge_text_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_center_badge_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_center_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_center_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_cta_top_center_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_center_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_cta_top_center_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_center_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_cta_top_center_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_center_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_center_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_cta_top_center_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_cta_top_center_button_label",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_center_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_cta_top_center_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-cta-top-no-bottom",
      "snippet_name": "emb_hero_cta_top_no_bottom",
      "fields": [
        {
          "name": "emb_hero_cta_top_no_bottom_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_show_preheadline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_no_bottom_preheadline",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_show_badge",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_no_bottom_badge_bg_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_badge_text_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_badge_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_no_bottom_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_cta_top_no_bottom_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_cta_top_no_bottom_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_no_bottom_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_button_label",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        }
      ]
    },
    {
      "module_id": "hero-cta-top-no-bottom-center",
      "snippet_name": "emb_hero_cta_top_no_bottom_center",
      "fields": [
        {
          "name": "emb_hero_cta_top_no_bottom_center_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_show_preheadline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_preheadline",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_show_badge",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_badge_bg_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_badge_text_color",
          "type": "color",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_badge_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_show_small_headline",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_show_large_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_show_salutation",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_use_snippetcall_salutation",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede,"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_button_border_color",
          "type": "color",
          "required": true,
          "default": "#74FFDF"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_button_label",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_hero_cta_top_no_bottom_center_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        }
      ]
    },
    {
      "module_id": "teaser-1col",
      "snippet_name": "emb_teaser_1col",
      "fields": [
        {
          "name": "emb_teaser_1col_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_1col_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_1col_image_link_url",
          "type": "url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_1col_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_1col_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_1col_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_1col_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_1col_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_teaser_1col_button_border_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_teaser_1col_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "loft-snl-copy-cta",
      "snippet_name": "emb_loft_snl_copy_cta",
      "fields": [
        {
          "name": "emb_loft_snl_copy_cta_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_snl_copy_cta_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_snl_copy_cta_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_loft_snl_copy_cta_button_border_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_loft_snl_copy_cta_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "loft-snl-copy-sections-cta",
      "snippet_name": "emb_loft_snl_copy_sections_cta",
      "fields": [
        {
          "name": "emb_loft_snl_copy_sections_cta_headline_1",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_snl_copy_sections_cta_body_1",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_snl_copy_sections_cta_show_section_2",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_loft_snl_copy_sections_cta_headline_2",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_loft_snl_copy_sections_cta_body_2",
          "type": "rich_full",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_loft_snl_copy_sections_cta_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_snl_copy_sections_cta_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_loft_snl_copy_sections_cta_button_border_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_loft_snl_copy_sections_cta_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "loft-rnl-dev-intro",
      "snippet_name": "emb_loft_rnl_dev_intro",
      "fields": [
        {
          "name": "emb_loft_rnl_dev_intro_headline",
          "type": "text",
          "required": true,
          "default": "Immobilien-Newsletter München"
        },
        {
          "name": "emb_loft_rnl_dev_intro_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede"
        },
        {
          "name": "emb_loft_rnl_dev_intro_body",
          "type": "rich_full",
          "required": true,
          "default": "<p>willkommen zum aktuellen Immobilien-Newsletter für München und Umgebung.</p>"
        }
      ],
      "notes": [
        "Template-specific Loft RNL intro snippet with editable headline, controlled salutation field and rich body.",
        "For salutationContext `loft-rnl-dev`, export materializes `emb_loft_rnl_dev_intro_salutation` from the documented salutation registry instead of exposing free Iterable variables in the snippet."
      ]
    },
    {
      "module_id": "loft-rnl-dev-teaser-1col",
      "snippet_name": "emb_loft_rnl_dev_teaser_1col",
      "fields": [
        {
          "name": "emb_loft_rnl_dev_teaser_1col_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_badge_label",
          "type": "text",
          "required": true,
          "default": "Wohnungen zum Kauf"
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_details",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_button_border_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_loft_rnl_dev_teaser_1col_button_label",
          "type": "text",
          "required": true,
          "default": "Exposé anfordern"
        }
      ],
      "notes": [
        "Template-specific Loft RNL teaser module.",
        "Background color is required but must be resolved from the global background rhythm, not from a free user choice.",
        "Badge surface is derived inversely from the resolved background color inside the productive snippet."
      ]
    },
    {
      "module_id": "loft-regio-resi-intro",
      "snippet_name": "emb_loft_regio_resi_intro",
      "fields": [
        {
          "name": "emb_loft_regio_resi_intro_headline",
          "type": "text",
          "required": true,
          "default": "Ausgewählte Wohnimmobilien aus Ihrer Region"
        },
        {
          "name": "emb_loft_regio_resi_intro_salutation",
          "type": "text",
          "required": true,
          "default": "Hallo Anrede"
        },
        {
          "name": "emb_loft_regio_resi_intro_body",
          "type": "rich_full",
          "required": true,
          "default": "<p>hier finden Sie ausgewaehlte Wohnimmobilien aus Ihrer Region. Das Intro fuehrt bewusst kompakt in die folgenden Objekt-Highlights ein und laesst dem wiederholbaren Residential-Teaser den inhaltlichen Schwerpunkt.</p>"
        }
      ],
      "notes": [
        "Template-specific Loft Regio Resi intro snippet with editable headline, controlled salutation field and rich body.",
        "For salutationContext `loft-regio-resi`, export materializes `emb_loft_regio_resi_intro_salutation` from the documented salutation registry instead of exposing free Iterable variables in the snippet."
      ]
    },
    {
      "module_id": "loft-regio-resi-teaser-1col",
      "snippet_name": "emb_loft_regio_resi_teaser_1col",
      "fields": [
        {
          "name": "emb_loft_regio_resi_teaser_1col_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_body",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_image_url",
          "type": "image_url",
          "required": true,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_metric_1_label",
          "type": "text",
          "required": true,
          "default": "Kaufpreis"
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_metric_1_value",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_metric_2_label",
          "type": "text",
          "required": true,
          "default": "Wohnfläche ca."
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_metric_2_value",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_metric_3_label",
          "type": "text",
          "required": true,
          "default": "Zimmeranzahl"
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_metric_3_value",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_button_border_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_loft_regio_resi_teaser_1col_button_label",
          "type": "text",
          "required": true,
          "default": "Exposé anfordern"
        }
      ],
      "notes": [
        "Template-specific Loft Regio Resi teaser module.",
        "Background color is required but must be resolved from the global background rhythm, not from a free user choice.",
        "Desktop metrics and the mobile bullet list reuse the same metric label/value fields and must stay content-identical."
      ]
    },
    {
      "module_id": "teaser-2col-horizontal",
      "snippet_name": "emb_teaser_2col_horizontal",
      "fields": [
        {
          "name": "emb_teaser_2col_horizontal_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_1_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_horizontal_col_1_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_1_chevron_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_1_chevron_label",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_show_item_2",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_horizontal_show_item_3",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_horizontal_col_2_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_horizontal_col_2_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_2_body",
          "type": "rich_inline",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_2_chevron_url",
          "type": "url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_2_chevron_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_show_item_4",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_horizontal_col_3_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_horizontal_col_3_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_3_body",
          "type": "rich_inline",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_3_chevron_url",
          "type": "url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_3_chevron_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_4_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_horizontal_col_4_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_4_body",
          "type": "rich_inline",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_4_chevron_url",
          "type": "url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_horizontal_col_4_chevron_label",
          "type": "text",
          "required": false,
          "default": ""
        }
      ]
    },
    {
      "module_id": "teaser-2col-vertical",
      "snippet_name": "emb_teaser_2col_vertical",
      "fields": [
        {
          "name": "emb_teaser_2col_vertical_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_col_1_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_vertical_col_1_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_col_1_chevron_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_col_1_chevron_label",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_col_2_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_vertical_col_2_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_col_2_chevron_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_vertical_col_2_chevron_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "teaser-2col-alternating",
      "snippet_name": "emb_teaser_2col_alternating",
      "fields": [
        {
          "name": "emb_teaser_2col_alternating_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_col_1_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/15fd5a27e1b04e209135462087d1e3bd-emb_placeholder_4x3.png"
        },
        {
          "name": "emb_teaser_2col_alternating_col_1_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_col_1_chevron_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_col_1_chevron_label",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_col_2_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/15fd5a27e1b04e209135462087d1e3bd-emb_placeholder_4x3.png"
        },
        {
          "name": "emb_teaser_2col_alternating_col_2_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_col_2_chevron_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_alternating_col_2_chevron_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "teaser-2col-listing",
      "snippet_name": "emb_teaser_2col_listing",
      "fields": [
        {
          "name": "emb_teaser_2col_listing_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_1_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/15fd5a27e1b04e209135462087d1e3bd-emb_placeholder_4x3.png"
        },
        {
          "name": "emb_teaser_2col_listing_col_1_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_1_chevron_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_1_chevron_label",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_show_item_2",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_listing_show_item_3",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_listing_show_item_4",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_listing_col_2_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/15fd5a27e1b04e209135462087d1e3bd-emb_placeholder_4x3.png"
        },
        {
          "name": "emb_teaser_2col_listing_col_2_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_2_body",
          "type": "rich_inline",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_2_chevron_url",
          "type": "url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_2_chevron_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_3_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/15fd5a27e1b04e209135462087d1e3bd-emb_placeholder_4x3.png"
        },
        {
          "name": "emb_teaser_2col_listing_col_3_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_3_body",
          "type": "rich_inline",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_3_chevron_url",
          "type": "url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_3_chevron_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_4_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/15fd5a27e1b04e209135462087d1e3bd-emb_placeholder_4x3.png"
        },
        {
          "name": "emb_teaser_2col_listing_col_4_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_4_body",
          "type": "rich_inline",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_4_chevron_url",
          "type": "url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_col_4_chevron_label",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_show_button",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_listing_button_url",
          "type": "url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_listing_button_bg_color",
          "type": "color",
          "required": false,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_teaser_2col_listing_button_border_color",
          "type": "color",
          "required": false,
          "default": "#333333"
        },
        {
          "name": "emb_teaser_2col_listing_button_label",
          "type": "text",
          "required": false,
          "default": ""
        }
      ]
    },
    {
      "module_id": "teaser-2col-gallery",
      "snippet_name": "emb_teaser_2col_gallery",
      "fields": [
        {
          "name": "emb_teaser_2col_gallery_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_gallery_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_gallery_col_1_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_gallery_col_1_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_gallery_col_2_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_gallery_col_2_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_gallery_show_item_3",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_gallery_col_3_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_gallery_col_3_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_gallery_show_item_4",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_teaser_2col_gallery_col_4_image_url",
          "type": "image_url",
          "required": false,
          "default": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png"
        },
        {
          "name": "emb_teaser_2col_gallery_col_4_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_teaser_2col_gallery_hide_bottom_row_mobile",
          "type": "boolean",
          "required": true,
          "default": false
        }
      ]
    },
    {
      "module_id": "benefits-3col",
      "snippet_name": "emb_benefits_3col",
      "fields": [
        {
          "name": "emb_benefits_3col_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_show_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_benefits_3col_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_col_1_icon_url",
          "type": "icon_url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_col_2_icon_url",
          "type": "icon_url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_col_3_icon_url",
          "type": "icon_url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_col_3_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_show_cta",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_benefits_3col_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_benefits_3col_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_benefits_3col_button_border_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_benefits_3col_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "servicetiles",
      "snippet_name": "emb_servicetiles",
      "fields": [
        {
          "name": "emb_servicetiles_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_1_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_1_icon_url",
          "type": "image_url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_1_title",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_1_description",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_2_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_2_icon_url",
          "type": "image_url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_2_title",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_2_description",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_3_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_3_icon_url",
          "type": "image_url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_3_title",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_3_description",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_4_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_4_icon_url",
          "type": "image_url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_4_title",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_servicetiles_col_4_description",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "steps-3col",
      "snippet_name": "emb_steps_3col",
      "fields": [
        {
          "name": "emb_steps_3col_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_3col_show_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_steps_3col_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_3col_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": "",
          "repeated_item": "step",
          "index_range": [
            1,
            3
          ],
          "notes": "Schritt 1 Text"
        },
        {
          "name": "emb_steps_3col_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": "",
          "repeated_item": "step",
          "index_range": [
            1,
            3
          ],
          "notes": "Schritt 2 Text"
        },
        {
          "name": "emb_steps_3col_col_3_body",
          "type": "rich_inline",
          "required": true,
          "default": "",
          "repeated_item": "step",
          "index_range": [
            1,
            3
          ],
          "notes": "Schritt 3 Text"
        },
        {
          "name": "emb_steps_3col_show_button",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_steps_3col_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_3col_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_steps_3col_button_border_color",
          "type": "color",
          "required": true,
          "default": "#333333"
        },
        {
          "name": "emb_steps_3col_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ],
      "notes": [
        "Dieses Modul wird genau einmal exportiert.",
        "Desktop- und Mobile-Markup im Snippet sind reine Renderdetails.",
        "Export darf nichts aus wiederholtem data-module oder Snippet-HTML ableiten."
      ]
    },
    {
      "module_id": "steps-horizontal",
      "snippet_name": "emb_steps_horizontal",
      "fields": [
        {
          "name": "emb_steps_horizontal_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_horizontal_show_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_steps_horizontal_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_horizontal_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_horizontal_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_horizontal_col_3_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_horizontal_show_button",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_steps_horizontal_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_steps_horizontal_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_steps_horizontal_button_border_color",
          "type": "color",
          "required": true,
          "default": "#D9D9D9"
        },
        {
          "name": "emb_steps_horizontal_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "table",
      "snippet_name": "emb_table",
      "fields": [
        {
          "name": "emb_table_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_show_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_table_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_col_1_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_col_2_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_col_3_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_1_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_1_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_1_col_3_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_2_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_2_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_2_col_3_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_3_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_3_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_row_3_col_3_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_show_button",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_table_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_table_button_border_color",
          "type": "color",
          "required": true,
          "default": "#D9D9D9"
        },
        {
          "name": "emb_table_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "table-comparison",
      "snippet_name": "emb_table_comparison",
      "fields": [
        {
          "name": "emb_table_comparison_bg_color",
          "type": "color",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_show_headline",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_table_comparison_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_col_1_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_row_1_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_row_2_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_row_3_col_1_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_col_2_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_row_1_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_row_2_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_row_3_col_2_body",
          "type": "rich_inline",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_show_button",
          "type": "boolean",
          "required": true,
          "default": true
        },
        {
          "name": "emb_table_comparison_button_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_table_comparison_button_bg_color",
          "type": "color",
          "required": true,
          "default": "#FFFFFF"
        },
        {
          "name": "emb_table_comparison_button_border_color",
          "type": "color",
          "required": true,
          "default": "#D9D9D9"
        },
        {
          "name": "emb_table_comparison_button_label",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "contact",
      "snippet_name": "emb_contact",
      "fields": [
        {
          "name": "emb_contact_show_image",
          "type": "boolean",
          "required": true,
          "default": false
        },
        {
          "name": "emb_contact_image_url",
          "type": "image_url",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_contact_image_alt",
          "type": "text",
          "required": false,
          "default": ""
        },
        {
          "name": "emb_contact_headline",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_contact_body_intro",
          "type": "rich_full",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_contact_phone",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_contact_phone_hours",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_contact_email_intro",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_contact_email_url",
          "type": "url",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_contact_email_address",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_contact_closing_line_1",
          "type": "text",
          "required": true,
          "default": ""
        },
        {
          "name": "emb_contact_closing_line_2",
          "type": "text",
          "required": true,
          "default": ""
        }
      ]
    },
    {
      "module_id": "contact-signoff",
      "snippet_name": "emb_contact_signoff",
      "fields": [],
      "notes": [
        "Static signoff snippet without parameters."
      ]
    },
    {
      "module_id": "footer",
      "snippet_name": "emb_footer_marketing",
      "fields": []
    }
  ],
  "rules": {
    "export_map_is_single_source_of_truth": true,
    "unknown_fields_policy": "error",
    "allow_only_declared_modules": true,
    "allow_only_declared_fields": true
  }
}
```

## email-builder/agent/template-definition.contract.md

Dateityp: md

````md
# Template Definition Contract

Diese Datei beschreibt verbindlich, wie eine `template-<template_id>.definition.json` fuer EMB-Composition-Templates aufgebaut sein muss.

Im flachen Agent-Setup liegen die operativen Template-Dateien direkt in `agent/` und werden immer aus `template_id` abgeleitet:

- `template-<template_id>.definition.json`
- `template-<template_id>.preview.html`
- `template-definition.contract.md`

## Zweck

- `template-<template_id>.definition.json` ist die maschinenlesbare Agent-Logik eines Templates.
- `template-<template_id>.preview.html` ist die visuelle Vorschau-Basis des Templates.
- Der Agent darf Regeln niemals aus `template-<template_id>.preview.html` ableiten.
- `template-<template_id>.preview.html` und `template-<template_id>.definition.json` gehoeren immer zusammen.
- Das zugehoerige Iterable-Basis-Template unter `email/templates/<template_id>.html` ist nur die HTML-Shell fuer den Export.
- Iterable-Basis-Templates duerfen keine festen Module und keine festen Snippet-Calls enthalten.
- `email/templates/<template_id>.html` enthaelt genau das CSS, das fuer die Module dieses Templates benoetigt wird.
- Die konkrete Modul-Komposition kommt ausschliesslich aus `template-<template_id>.definition.json` und wird erst beim Export erzeugt.
- Operative Template-Dateien duerfen nicht zu vollstaendig zusammengebauten Testmails oder Demo-Templates werden.

## Prozess

- Der Contract beschreibt den Aufbau und die operative Nutzung der namespaceten Template-Dateien im Agent-Layer.
- Fuer neue oder geaenderte Templates startet der erste Entwurf ausschliesslich in den Review-Dateien unter `development/review/`.
- Diese Review-Dateien sind reine Test-Artefakte und nie operative Builder- oder Export-Wahrheit.
- Review-Dateien duerfen fuer Template-Tests vollstaendig zusammengebaut sein und Demo-Content oder Beispielmodule enthalten.
- Vollstaendig zusammengebaute Preview- oder E-Mail-Tests gehoeren nur in `development/review/preview-index.html` und `development/review/email-index.html`, nicht in operative Template-Dateien.
- Der Ablauf bleibt auch fuer Templates immer: zuerst nur `development/review/preview-index.html` und `development/review/email-index.html` als Review-Entwurf aktualisieren, User-Freigabe einholen und erst danach die abschliessende Template-Integration oder zentrale Dokumentation nachziehen.
- Vor ausdruecklicher User-Freigabe duerfen `agent/template-<template_id>.definition.json`, `agent/template-<template_id>.preview.html` und `email/templates/<template_id>.html` fuer neue oder geaenderte Templates nicht angepasst werden.
- Nach ausdruecklicher User-Freigabe fuehrt Codex die Template-Integration direkt in den operativen Zielpfaden durch:
  - `agent/template-<template_id>.definition.json` fuer die strukturelle Template-Definition und Modulreihenfolge
  - `agent/template-<template_id>.preview.html` fuer die operative Preview-/Template-Logik
  - `email/templates/<template_id>.html` als Iterable-Base-/Shell-Datei mit genau dem benoetigten Template-CSS
- Relevante Library- oder Regeldateien werden nur bei konkretem Bedarf angepasst.
- `development/review/preview-index.html` und `development/review/email-index.html` koennen danach als finaler Teststand aktualisiert werden, bleiben aber reine Test-Artefakte und nie operative Quelle.
- `development/templates/searcher-standard/*` bleibt bis zur finalen Prozessentscheidung als historischer Prozessbeleg erhalten, ist aber kein verpflichtender Startpunkt fuer neue Template-Arbeit.
- Im operativen Agent-Layer sind nur namespacete Template-Dateien erlaubt.
- Generische operative Template-Dateien wie `agent/preview.html` oder `agent/template-definition.json` sind verboten.

## Operative Dateinamen

- Die Definition MUSS als `template-<template_id>.definition.json` gespeichert werden.
- Die Preview MUSS als `template-<template_id>.preview.html` gespeichert werden.
- `<template_id>` im Dateinamen MUSS exakt dem Wert von `template_id` in der Definition entsprechen.
- Nach dem manuellen Anlegen des zugehoerigen Iterable-Basistemplates wird die echte Iterable-ID in `iterable_template_id` eingetragen.
- Solange `iterable_template_id = null` ist, ist Iterable-Export fuer dieses Template blockiert.

## Pflichtfelder

Jede `template-<template_id>.definition.json` MUSS genau diese Top-Level-Felder enthalten:

- `template_id`
- `template_name`
- `version`
- `status`
- `preview_file`
- `iterable_template_id`
- `rules`
- `slots`

## Feldregeln

### `template_id`

- eindeutige technische ID
- muss `kebab-case` sein
- beschreibt die technische Template-Identitaet des Templates
- MUSS exakt dem `<template_id>` in `template-<template_id>.definition.json` und `template-<template_id>.preview.html` entsprechen

### `template_name`

- lesbarer Name fuer Menschen

### `version`

- Zahl
- startet bei `1`

### `status`

- erlaubte Werte:
  - `draft`
  - `active`
  - `deprecated`

### `preview_file`

- muss immer exakt `template-<template_id>.preview.html` sein
- `<template_id>` darin MUSS exakt dem Feld `template_id` entsprechen
- die Preview-Datei darf fertige Preview-Module enthalten
- CSS- und Asset-Links aus der Preview duerfen nicht frei neu erzeugt, geraten oder normalisiert werden
- der kanonische CSS-Link fuer operative Template-Previews ist `https://s24-creative-ops.github.io/email-builder/preview-styles.css`

### `iterable_template_id`

- erlaubt sind `number` oder `null`
- `null` bedeutet: Template ist lokal vorbereitet, aber noch nicht in Iterable angelegt
- `number` bedeutet: echte Iterable Template-ID

## `rules`

`rules` MUSS genau diese Felder enthalten:

- `order_locked`: `true`
- `forbid_new_modules`: `true`
- `allow_remove_modules`: boolean
- `allow_duplicate_modules`: boolean

Regeln:

- `order_locked` MUSS immer `true` sein.
- `forbid_new_modules` MUSS immer `true` sein.
- `allow_remove_modules` steuert, ob nicht-gesperrte Slots entfernt werden duerfen.
- `allow_duplicate_modules` steuert, ob duplizierbare Slots vervielfaeltigt werden duerfen.

## `slots`

- `slots` ist ein Array.
- Die Reihenfolge im Array ist verbindlich.
- Jeder Slot MUSS genau diese Felder enthalten:
  - `slot_id`
  - `module_id`
  - `locked`
  - `removable`
  - `repeatable`

## Slot-Regeln

### `slot_id`

- eindeutig innerhalb des Templates

### `module_id`

- muss einem bestehenden Modul entsprechen

### `locked`

- `true` bedeutet:
  - Slot darf nicht entfernt werden
  - Slot darf nicht dupliziert werden
  - Slot darf nicht verschoben werden

### `removable`

- darf nur `true` sein, wenn `locked = false`

### `repeatable`

- darf nur `true` sein, wenn `locked = false`

## Template-Regeln

- neue Modultypen ausserhalb der definierten `slots` sind verboten
- Duplikate duerfen nur aus Slots mit `repeatable = true` entstehen
- Duplikate werden direkt nach der letzten Instanz derselben `module_id` eingefuegt

## QA vor Freigabe

- Preview muss im EMB funktionieren.
- Die Slot-Reihenfolge muss eingehalten werden.
- locked Module duerfen nicht entfernbar sein.
- repeatable Module duerfen nur im erlaubten Rahmen dupliziert werden.
- Es duerfen keine neuen Module ausserhalb der Slots entstehen.
- Das Iterable-Basistemplate unter `email/templates/<template_id>.html` darf nur Shell, benoetigtes CSS und Content-Einfuegepunkt enthalten.
- Der Export muss die template-spezifische `iterable_template_id` verwenden.
- Der normale Export ohne Composition-Template muss unveraendert bleiben.

## Minimales JSON-Beispiel

```json
{
  "template_id": "template-example",
  "template_name": "Template Example",
  "version": 1,
  "status": "draft",
  "preview_file": "template-template-example.preview.html",
  "iterable_template_id": null,
  "rules": {
    "order_locked": true,
    "forbid_new_modules": true,
    "allow_remove_modules": false,
    "allow_duplicate_modules": false
  },
  "slots": [
    {
      "slot_id": "logo-1",
      "module_id": "logo",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "hero-1",
      "module_id": "hero-image-top",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "footer-1",
      "module_id": "footer",
      "locked": true,
      "removable": false,
      "repeatable": false
    }
  ]
}
```
````

## email-builder/agent/email-state.schema.json

Dateityp: json

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Email Builder State",
  "type": "object",
  "required": [
    "modules"
  ],
  "properties": {
    "campaignId": {
      "type": [
        "string",
        "null"
      ]
    },
    "templateId": {
      "type": [
        "string",
        "null"
      ]
    },
    "previewBranchKey": {
      "type": [
        "string",
        "null"
      ]
    },
    "templateContext": {
      "type": "object",
      "required": [
        "mode",
        "resolvedBaseTemplateId"
      ],
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "default_template",
            "composition_template"
          ]
        },
        "resolvedBaseTemplateId": {
          "type": "string"
        },
        "compositionTemplateId": {
          "type": [
            "string",
            "null"
          ]
        },
        "iterableTemplateId": {
          "type": [
            "string",
            "null"
          ]
        }
      },
      "additionalProperties": false
    },
    "salutationContext": {
      "type": [
        "string",
        "null"
      ],
      "enum": [
        "generic",
        "rle",
        "loft-snl",
        "loft-rnl-dev",
        null
      ]
    },
    "subject": {
      "type": "string"
    },
    "preheader": {
      "type": "string"
    },
    "modules": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "instance_id",
          "module_id",
          "snippet_name",
          "content"
        ],
        "properties": {
          "instance_id": {
            "type": "string"
          },
          "module_id": {
            "type": "string"
          },
          "snippet_name": {
            "type": "string"
          },
          "content": {
            "type": "object",
            "additionalProperties": true
          },
          "meta": {
            "type": "object",
            "additionalProperties": true
          }
        }
      }
    }
  },
  "x-rules": [
    "Ein email_state ist nur export-ready, wenn subject und preheader vorhanden und nicht leer sind.",
    "Ein export-ready state muss einen eindeutigen templateContext enthalten.",
    "Bei freiem Modulbau, beim Standard-Blueprint und bei editierbaren Starter Blueprints wie ho-esg oder seeker-mle gilt templateContext.mode = default_template und templateContext.resolvedBaseTemplateId = 569946; compositionTemplateId und iterableTemplateId bleiben dabei leer.",
    "Bei Composition-Templates gelten templateContext.mode = composition_template, templateContext.compositionTemplateId, templateContext.iterableTemplateId und templateContext.resolvedBaseTemplateId = templateContext.iterableTemplateId.",
    "salutationContext ist der aufgeloeste Anrede-Kontext aus agent/product-salutations.json oder aus salutation_context_id des aktiven Composition-Templates.",
    "Neue regulaere States sollen salutationContext als registrierte ID tragen; wenn keine eindeutige Zuordnung vorliegt, gilt generic.",
    "campaignId und templateId sind nur die wiederverwendbare Campaign-Bindung; templateContext.resolvedBaseTemplateId bleibt davon getrennt.",
    "Bei Re-Export muessen campaignId, templateId und previewBranchKey eindeutig demselben fortgeschriebenen Preview-/Composition-Zweig zugeordnet sein.",
    "module_id muss in export-map.json existieren.",
    "snippet_name muss zum module_id in export-map.json passen.",
    "Jeder Key in content muss ein erlaubtes Feld fuer dieses Modul in export-map.json sein.",
    "Wenn eine Felddefinition in export-map.json allowed_values definiert, muss der content-Wert exakt einem dieser erlaubten Werte entsprechen.",
    "Required Felder werden nur aus content oder Default der export-map.json befuellt.",
    "Felder ohne content und ohne Default werden nicht erfunden.",
    "Resolver-Werte sind nur zulaessig, wenn sie vor dem Export bereits konkret im state materialisiert wurden oder aus einer dokumentierten technischen Quelle fail-closed ableitbar sind.",
    "Dokumentierte technische Resolver-Quellen sind nur: Hintergrund-Rhythmus aus builder-library.md plus preview-styles.css, Icon-Auswahl aus icon-library.md, finale Button-Farbwerte aus builder-library.md und kontrollierte Salutation-Feld-Overrides aus product-salutations.json.",
    "Wenn modules eines der Center-Hero-Module hero-image-top-center, hero-image-top-bleed-center, hero-cta-top-center, hero-cta-top-no-bottom-center, hero-image-head-copy-bleed-center, hero-image-textbox-cta-center oder hero-fakeform-buttons-image enthalten, muss ein vorhandenes Logo-Modul als logo-centered vorliegen; ein plain logo ist in diesem Kontext vor dem Export zu normalisieren.",
    "Diese Logo-Normalisierung aendert nur das Logo-Modul, fuegt kein zweites Logo ein und erhaelt die Modulreihenfolge.",
    "Nur Hero-Headlines duerfen im state ueber ein kanonisches Groessenfeld steuerbar sein.",
    "Erlaubte Hero-Groessen sind ausschliesslich s, m und l; ihr Mapping ist direkt heading-s, heading-m und heading-l.",
    "Der regulaere Hero-Default ist l.",
    "Nicht-Hero-Modulheadlines sind nicht usersteuerbar: erste Hauptheadline = heading-m, Unter-Headlines und Abschnittstitel = heading-s, Bodytexte = body-standard.",
    "Freie Heading-Klassen, freie CSS-Werte, freie Font-Size-Werte, freies HTML oder freie Style-Werte sind fuer Typography-Steuerung unzulaessig.",
    "Fuer hero-image-top ist emb_hero_image_top_headline_size das einzige kanonische Groessenfeld; zulaessig sind nur s, m und l.",
    "Fuer hero-image-top muessen emb_hero_image_top_show_small_headline und emb_hero_image_top_show_large_headline exakt aus dem kanonischen headline_size abgeleitet werden; true/true ist ungueltig.",
    "Fuer hero-image-top-center, hero-image-top-bleed, hero-image-top-bleed-center, hero-fakeform-buttons-image, hero-cta-top, hero-cta-top-center, hero-cta-top-no-bottom und hero-cta-top-no-bottom-center gilt dasselbe kanonische Hero-Modell: genau ein *_headline_size-Feld mit nur s, m und l sowie exakt daraus abgeleitete show_small_headline- und show_large_headline-Bridge-Felder.",
    "Fuer hero-image-head-copy-bleed-center gilt dasselbe kanonische Hero-Modell: genau ein emb_hero_image_head_copy_bleed_center_headline_size-Feld mit nur s, m und l sowie exakt daraus abgeleitete show_small_headline- und show_large_headline-Bridge-Felder.",
    "Fuer hero-image-textbox-cta-center gilt dasselbe kanonische Hero-Modell: genau ein emb_hero_image_textbox_cta_center_headline_size-Feld mit nur s, m und l sowie exakt daraus abgeleitete show_small_headline- und show_large_headline-Bridge-Felder.",
    "Fuer hero-fakeform-buttons-image gilt dasselbe kanonische Hero-Modell: genau ein emb_hero_fakeform_buttons_image_headline_size-Feld mit nur s, m und l sowie exakt daraus abgeleitete show_small_headline- und show_large_headline-Bridge-Felder.",
    "Required *_bg_color-Felder muessen im content bereits als konkrete Hexwerte aus dem operativen Hintergrund-Rhythmus vorliegen.",
    "theme-white, theme-gray oder andere semantische Preview-Klassen sind keine zulaessigen *_bg_color-Werte im content.",
    "content ist die einzige Exportquelle fuer Iterable-Variablen.",
    "content darf keine freien oder ungeprueften HTML-Werte enthalten.",
    "Normale Text-Felder bleiben Plain Text.",
    "rich_inline darf nur sanitisiertes builder-eigenes Inline-HTML mit den Tags strong, em, a und br enthalten.",
    "rich_full darf nur sanitisiertes builder-eigenes Richtext-HTML mit den Tags p, ul, ol, li, strong, em, a und br enthalten.",
    "Bei a-Tags sind nur href, target und rel erlaubt.",
    "meta enthaelt nur nicht-exportrelevante Informationen wie position oder item_count."
  ]
}
```

## email-builder/agent/product-salutations.json

Dateityp: json

```json
{
  "version": 2,
  "preview_default": "Hallo Anrede,",
  "contexts": [
    {
      "id": "generic",
      "aliases": [],
      "template_ids": [],
      "mode": "plain_default",
      "preview_text": "Hallo Anrede,"
    },
    {
      "id": "rle",
      "aliases": [
        "rle"
      ],
      "template_ids": [],
      "mode": "hero_snippet_flag",
      "preview_text": "Hallo Anrede,"
    },
    {
      "id": "loft-snl",
      "aliases": [
        "loft snl",
        "snl"
      ],
      "template_ids": [
        "loft-snl"
      ],
      "mode": "template_builtin"
    },
    {
      "id": "loft-rnl-dev",
      "aliases": [
        "loft rnl",
        "loft rnl dev",
        "loft rnl (dev)",
        "rnl dev"
      ],
      "template_ids": [
        "loft-rnl-dev"
      ],
      "mode": "template_builtin",
      "field_resolvers": [
        {
          "module_id": "loft-rnl-dev-intro",
          "field": "emb_loft_rnl_dev_intro_salutation",
          "preview_value": "Hallo Anrede",
          "export_value": "{{#if (and (eq salutation 'Frau') (neq lastName 'NULL'))}} Liebe {{salutation}} {{lastName}}, {{else if (and (eq salutation 'Herr') (neq lastName 'NULL'))}} Lieber {{salutation}} {{lastName}}, {{else}} Liebe:r ImmoScout24-Nutzer:in, {{/if}}"
        }
      ]
    },
    {
      "id": "loft-regio-resi",
      "aliases": [
        "loft regio",
        "loft regio resi",
        "loft | regio (resi)",
        "regio resi"
      ],
      "template_ids": [
        "loft-regio-resi"
      ],
      "mode": "template_builtin",
      "field_resolvers": [
        {
          "module_id": "loft-regio-resi-intro",
          "field": "emb_loft_regio_resi_intro_salutation",
          "preview_value": "Hallo Anrede",
          "export_value": "{{#if (and (eq salutation 'Frau') (neq lastName 'NULL'))}} Liebe {{salutation}} {{lastName}}, {{else if (and (eq salutation 'Herr') (neq lastName 'NULL'))}} Lieber {{salutation}} {{lastName}}, {{else}} Liebe:r ImmoScout24-Nutzer:in, {{/if}}"
        }
      ]
    }
  ]
}
```

## email-builder/agent/service-products.json

Dateityp: json

```json
{
  "version": 1,
  "products": [
    {
      "id": "ppa",
      "original_snippet_name": "servicetile_PPA",
      "aliases": [
        "PPA",
        "Ab 0\u20ac inserieren",
        "servicetile_PPA"
      ],
      "title": "Ab 0\u20ac inserieren",
      "description": "Mieter oder K\u00e4ufer finden",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/1u4/6b3/i28/board_sign_white.png",
      "target_url": "https://www.immobilienscout24.de/anbieten/anzeige-schalten/start/"
    },
    {
      "id": "kwatt",
      "original_snippet_name": "servicetile_KWATT",
      "aliases": [
        "KWATT",
        "Dynamischer Stromtarif",
        "servicetile_KWATT"
      ],
      "title": "Dynamischer Stromtarif",
      "description": "Strom sparen, monatlich k\u00fcndbar",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/feo/2fr/t9a/flash.png",
      "target_url": "https://www.immobilienscout24.de/lp/klarwatt.html"
    },
    {
      "id": "ea48",
      "original_snippet_name": "servicetile_EA48",
      "aliases": [
        "EA48",
        "Energieausweis bestellen",
        "servicetile_EA48"
      ],
      "title": "Energieausweis bestellen",
      "description": "Pflicht f\u00fcr Vermietung & Verkauf",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/1is/2t3/zqq/Energieausweiss.png",
      "target_url": "https://www.immobilienscout24.de/energieausweis.html"
    },
    {
      "id": "wplus",
      "original_snippet_name": "servicetile_WPLUS",
      "aliases": [
        "WPLUS",
        "Wohnen+",
        "servicetile_WPLUS"
      ],
      "title": "Wohnen+",
      "description": "Mieterschutz von der Nr. 1",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/kzm/k6m/thb/mietrechtsberatung_white.png",
      "target_url": "https://www.immobilienscout24.de/lp/wohnen-plus.html"
    },
    {
      "id": "kplus",
      "original_snippet_name": "servicetile_KPLUS",
      "aliases": [
        "KPLUS",
        "Suchen+ f\u00fcr Kauf",
        "servicetile_KPLUS"
      ],
      "title": "Suchen+ f\u00fcr Kauf",
      "description": "Das Plus an Informationen",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/ak4/08b/dag/mietzahlungs-einkommensnachweis_white.png",
      "target_url": "https://www.immobilienscout24.de/premium-mitgliedschaft-kauf/leistungen/"
    },
    {
      "id": "mplus",
      "original_snippet_name": "servicetile_MPLUS",
      "aliases": [
        "MPLUS",
        "Suchen+ f\u00fcr Miete",
        "servicetile_MPLUS"
      ],
      "title": "Suchen+ f\u00fcr Miete",
      "description": "Schneller ins Traumzuhause",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/85i/1f7/63k/plus_oben_im_postfach_white.png",
      "target_url": "https://www.immobilienscout24.de/meinkonto/premium-mitgliedschaft/"
    },
    {
      "id": "ibw",
      "original_snippet_name": "servicetile_IBW",
      "aliases": [
        "IBW",
        "Immobilie bewerten",
        "servicetile_IBW"
      ],
      "title": "Immobilie bewerten",
      "description": "Kostenlos Wert berechnen",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/ouv/5d4/0ql/chart_bars_vertical_white.png",
      "target_url": "https://www.immobilienscout24.de/immobilie-bewerten/"
    },
    {
      "id": "ele",
      "original_snippet_name": "servicetile_ELE",
      "aliases": [
        "ELE",
        "Energieberatung",
        "servicetile_ELE"
      ],
      "title": "Energieberatung",
      "description": "Bis zu 70% F\u00f6rderung erhalten",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/txv/cq2/g2k/money_house_white.png",
      "target_url": "https://www.immobilienscout24.de/lp/energieberatung.html"
    },
    {
      "id": "hle",
      "original_snippet_name": "servicetile_HLE",
      "aliases": [
        "HLE",
        "W\u00e4rmepumpe",
        "servicetile_HLE"
      ],
      "title": "W\u00e4rmepumpe",
      "description": "Kostensparend heizen",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/32f/0ps/7hk/gas_pump_white.png",
      "target_url": "https://www.immobilienscout24.de/heizung/"
    },
    {
      "id": "rle",
      "original_snippet_name": "servicetile_RLE",
      "aliases": [
        "RLE",
        "Makler finden",
        "servicetile_RLE"
      ],
      "title": "Makler finden",
      "description": "Passenden Profi finden",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/62q/092/p9h/user_tie_white.png",
      "target_url": "https://www.immobilienscout24.de/maklervergleich/"
    },
    {
      "id": "vplus",
      "original_snippet_name": "servicetile_VPLUS",
      "aliases": [
        "VPLUS",
        "Digital verwalten",
        "servicetile_VPLUS"
      ],
      "title": "Digital verwalten",
      "description": "Mit VermietenPlus",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/9m0/meh/ui2/document_white.png",
      "target_url": "https://www.immobilienscout24.de/anbieten/private-anbieter/lp/vermietetde.html"
    },
    {
      "id": "schufa",
      "original_snippet_name": "servicetile_SCHUFA",
      "aliases": [
        "SCHUFA",
        "SCHUFA-Bonit\u00e4tscheck",
        "servicetile_SCHUFA"
      ],
      "title": "SCHUFA-Bonit\u00e4tscheck",
      "description": "In 3 Minuten online erhalten",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/kgh/edg/68q/plus_SCHUFA_BonitaetsCheck_white.png",
      "target_url": "https://bonitaetscheck.immobilienscout24.de/"
    },
    {
      "id": "relo",
      "original_snippet_name": "servicetile_RELO",
      "aliases": [
        "RELO",
        "Umziehen",
        "servicetile_RELO"
      ],
      "title": "Umziehen",
      "description": "Kostenlose Umzugsangebote",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/8vu/r3t/ero/truck_side_moving_white.png",
      "target_url": "https://www.immobilienscout24.de/umzug/umzugsunternehmen/vergleichen/a.html"
    },
    {
      "id": "ndg",
      "original_snippet_name": "servicetile_NDG",
      "aliases": [
        "NDG",
        "Nutzungsdauer-Rechner",
        "servicetile_NDG"
      ],
      "title": "Nutzungsdauer-Rechner",
      "description": "Kostenlos berechnen",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/t7v/n1z/j9p/calculator_white.png",
      "target_url": "https://www.immobilienscout24.de/lp/nutzungsdauer-quickcheck.html"
    },
    {
      "id": "how",
      "original_snippet_name": "servicetile_HOW",
      "aliases": [
        "HOW",
        "Deine Immobilie im Blick",
        "servicetile_HOW"
      ],
      "title": "Deine Immobilie im Blick",
      "description": "Wert, Prognose, Markttrends",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/4d3/4ar/bip/meine_immobilie_white.png",
      "target_url": "https://www.immobilienscout24.de/lp/meine-immobilien.html"
    },
    {
      "id": "mod",
      "original_snippet_name": "servicetile_MOD",
      "aliases": [
        "MOD",
        "Modernisierungsrechner",
        "servicetile_MOD"
      ],
      "title": "Modernisierungsrechner",
      "description": "Kosten-Nutzen-Rechnung",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/t7v/n1z/j9p/calculator_white.png",
      "target_url": "https://www.immobilienscout24.de/modernisierungsrechner/start/"
    },
    {
      "id": "checkliste",
      "original_snippet_name": "servicetile_Checkliste",
      "aliases": [
        "Checkliste",
        "servicetile_Checkliste"
      ],
      "title": "Checkliste",
      "description": "Tipps zu deiner Besichtigung",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/ypc/e78/4lu/list_white.png",
      "target_url": "https://www.immobilienscout24.de/wissen/mieten/wohnungsbesichtigung.html"
    },
    {
      "id": "klub",
      "original_snippet_name": "servicetile_KLUB",
      "aliases": [
        "KLUB",
        "ImmoKlub",
        "servicetile_KLUB"
      ],
      "title": "ImmoKlub",
      "description": "Schutz f\u00fcr dein Zuhause",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/ned/1h4/ruj/umbrella_white.png",
      "target_url": "https://www.immobilienscout24.de/lp/immoklub.html"
    },
    {
      "id": "isba",
      "original_snippet_name": "servicetile_ISBA",
      "aliases": [
        "ISBA",
        "Bonit\u00e4tsauskunft",
        "servicetile_ISBA"
      ],
      "title": "Bonit\u00e4tsauskunft",
      "description": "von ImmoScout24",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/roq/5bs/m40/bonitaetsauskunft_white.png",
      "target_url": "https://www.immobilienscout24.de/lp/bonitaetsauskunft.html"
    },
    {
      "id": "sle",
      "original_snippet_name": "servicetile_SLE",
      "aliases": [
        "SLE",
        "PV-Vergleich",
        "servicetile_SLE"
      ],
      "title": "PV-Vergleich",
      "description": "PV-Anlage berechnen",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/2lw/wxu/ws3/solar_panel_white.png",
      "target_url": "https://www.immobilienscout24.de/solaranlage/?SME=true"
    },
    {
      "id": "is24ac",
      "original_snippet_name": "servicetile_IS24AC",
      "aliases": [
        "IS24AC",
        "Adresswechsel-Service",
        "servicetile_IS24AC"
      ],
      "title": "Adresswechsel-Service",
      "description": "von ImmoScout24",
      "icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/7ey/s3h/1wu/map_magnifier_white.png",
      "target_url": "https://www.immobilienscout24.de/lp/adresswechsel/"
    }
  ]
}
```

## email-builder/agent/preview-rules.md

Dateityp: md

```md
# Preview Rules

Diese Datei ist die einzige operative Preview-Regelbasis im flachen Agent-Satz unter `agent/`.
Die uebrigen operativen Agent-Dateien liegen direkt daneben in `agent/`.

## Zweck

Die Preview ist die sichtbare HTML-Arbeitsmail im Canvas und die Basis fuer spaetere Iterationen.

## Output

- Jede Preview muss als HTML-Code-Datei im Canvas erstellt oder aktualisiert werden.
- Eine Chat-Outline, Textzusammenfassung oder Blueprint-Antwort ist keine zulaessige Preview.
- Subject, Preheader, Modulfolge und Modulinhalt muessen in der HTML-Preview selbst vorliegen.
- Lokale Review-Dateien unter `development/review/*` sind reine Test-Artefakte und weder operative Preview-Wahrheit noch Exportquelle.

## Render-Regeln

- Starte jede Preview mit einer exakten Kopie von `preview-template.html`.
- Ersetze nur `[data-preview-subject-text]`, `[data-preview-preheader-text]` und den Bereich zwischen den Modul-Slot-Kommentaren.
- `agent/preview-modules.html` ist die kanonische Quelle fuer bestehende Preview-Modulbloecke.
- Die Modulwahl muss in `preview-module-library.md` registriert sein.
- Wenn ein Modul dort nicht angebunden ist, klar fehlschlagen statt Ersatz-HTML zu bauen.
- `preview-module-library.md` dient nur fuer Auswahl, Beschreibung und Feldlogik, nie als Quelle fuer frei rekonstruiertes Markup.
- Vorhandene Marker in `preview-modules.html` duerfen zur konsistenten Preview-Befuellung und fuer Debug oder Recovery genutzt werden, sind aber nicht die regulaere Exportquelle.
- Vor jeder Preview intern Completeness-Check anwenden:
  - Modulblock anhand `data-module` vollstaendig aus `agent/preview-modules.html` uebernehmen.
  - Wrapper, Tabellenstruktur, Klassen, Responsive-Klassen und Inline-Styles nie frei rekonstruieren, kuerzen, neu sortieren oder ersetzen.
  - Nur Feldwerte und Inhalte austauschen.
  - Bestehende Module nie aus Beschreibung, Erinnerung oder aehnlichen Modulen neu konstruieren.
  - Pflichtbestandteile eines Moduls nie auslassen.
  - `footer` immer vollstaendig rendern; es ist ein Strukturmodul und darf nie vereinfacht oder teilweise ausgelassen werden.
  - `logo`, `footer`, `contact` und `contact-signoff` immer weiss halten.
  - Normale Content-Module strikt nach dem operativen Hintergrund-Rhythmus materialisieren.
  - Nach Einfuegen, Entfernen oder Umsortieren von Modulen den gesamten Hintergrund-Rhythmus neu materialisieren.
  - Beim Einfuegen, Entfernen oder Umsortieren angeforderter Module duerfen umliegende bestehende Module nicht neu konstruiert oder vereinfacht werden.
  - Wenn ein Modul bereits korrekt in der Preview existiert, bleibt seine Struktur bei spaeteren Aenderungen zustandsbasiert erhalten.
  - Nach dem Einsetzen pruefen, dass die responsive Struktur des Moduls erhalten ist.
  - Wenn ein Modul nicht sicher vollstaendig renderbar ist, kurz nachfragen statt ein gekuertztes Modul auszugeben.
- Nach dem Einsetzen der finalen Modulfolge muessen die Modulhintergruende in der Preview exakt dem operativen Hintergrund-Rhythmus aus `builder-library.md` folgen.
- Statische `theme-white`- oder `theme-gray`-Annahmen einzelner Quellbloecke aus `preview-modules.html` sind dafuer nicht bindend und muessen bei Bedarf fuer die finale Preview normalisiert werden.
- `logo`, `footer`, `contact` und `contact-signoff` sind feste weisse Struktur-/Utility-Module; sie nehmen in der Preview nie an der Hintergrund-Alternierung teil und muessen immer weiss bleiben.
- Die konkrete technische Aufloesung dieses Rhythmus erfolgt ueber `agent/preview-styles.css`:
  - weiss / white = `#FFFFFF` aus `--surface-white`
  - grau / gray = `#F5F5F5` aus `--surface-gray`
- Die oeffentliche Canvas-/Preview-HTML-Ausgabe verwendet fuer das globale Preview-CSS immer exakt `https://s24-creative-ops.github.io/email-builder/preview-styles.css`.
- `agent/preview-styles.css` bleibt dabei die interne Repo-Quelldatei; die oeffentliche Preview darf nicht auf `/agent/preview-styles.css` zeigen.
- Finale EMB-Previews duerfen kein externes Design-Library- oder `preview/token-runtime.js`-Script laden.
- Token-, Link- und Asset-Werte fuer finale EMB-Previews muessen bereits statisch im Preview-Markup oder ueber die geladene EMB-Preview-CSS vorliegen; eine nachgelagerte Runtime darf weder Tokens noch Typography noch Badge-Surfaces ueberschreiben.
- Auch bei schnellem Modellbetrieb gilt: Vollstaendigkeit der Preview vor Kuerze der Antwort.

## Typography-Regeln

- Nur Hero-Headlines duerfen im Preview-/State-Flow ueber ein kanonisches Groessenfeld steuerbar sein.
- Erlaubte Hero-Groessen sind ausschliesslich `s`, `m` und `l`; ihr Mapping ist direkt `heading-s`, `heading-m`, `heading-l`.
- Der reguläre Hero-Default ist `l`.
- Die finale Preview-HTML muss die aufgeloeste Hero-Groesse direkt als echte Klasse am Headline-Element materialisieren:
  - `s` => `module__title module__title--hero-small`
  - `m` => `module__title` ohne zusaetzliche Hero-Groessenklasse
  - `l` => `module__title module__title--hero-large`
- `data-preview-size-*`-, `data-preview-size-legacy-*`- und `data-preview-size-*-class`-Attribute sind nur dokumentierende Metadaten und nie die einzige Renderquelle.
- Nach Entfernung von `token-runtime.js` darf keine Preview fuer Hero-Groessen auf nachgelagerte Runtime-Klassenmutation angewiesen sein.
- Nicht-Hero-Modulheadlines sind nicht usersteuerbar:
  - erste Hauptheadline = `heading-m`, ausser eine dokumentierte modulspezifische Ausnahme ist in `preview-module-library.md` registriert
  - Unter-Headlines, Abschnittstitel und Zwischenueberschriften = `heading-s`
  - Bodytexte = `body-standard`
- Freie Heading-Klassen, freie CSS-Werte, freie Font-Size-Werte, freies HTML oder freie Style-Werte sind fuer Typography-Steuerung unzulaessig.

## Icons

- Icon-Slots duerfen nur fuer Module verwendet werden, die in `preview-module-library.md` ausdruecklich Icon-Felder registrieren.
- Wenn ein `data-icon-field` vorhanden ist, muss die Preview dort eine gueltige Icon-URL aus `icon-library.md` tragen.
- Vor erfolgreichem Preview-Render muessen Beispiel- oder Quellblock-Icons aus `preview-modules.html` durch die operative Auswahl aus `icon-library.md` ersetzt sein.
- Wenn keine klare semantische Bucket-Zuordnung moeglich ist, nutzt die Preview den kanonischen `general-positive`-Fallback aus `icon-library.md`.
- Ein leerer Icon-Slot ist in der Preview nie zulaessig.

## Bilder

- Ohne echte User-Bild-URL bleibt die graue Placeholder-Flaeche aus `preview-modules.html` sichtbar.
- Mit echter User-Bild-URL wird genau diese URL in den passenden Slot eingebaut.
- Fuer fehlende Bilder darf die Preview keine technische Placeholder-URL oder `data:image`-Werte materialisieren.
- Hero-Placeholder:
  - `16:9 | 960 x 540 px`
  - `(Hi-Res 1920 x 1080)`
- Alle anderen Bild-Placeholder:
  - `16:9 | 960 x 540 px`
  - oder `4:3 | 800 x 600 px`

## Ablauf

1. Startkomposition bestimmen.
2. Inhalte fuer diese Komposition erzeugen.
3. HTML-Preview im Canvas erstellen oder aktualisieren.
4. Diese Preview zur operativen Wahrheit machen.
5. Parallel direkt einen strukturierten `email_state` aktualisieren.

- Im Initiallauf darf Preview, Composition oder State noch fehlen.
- Der Initiallauf ist ein Erzeugungsfall, kein Validierungsfall.
- Beim allerersten Start ist der Creation-Mode geschlossen:
  - explizit angefordertes Fixed Composition Template oder dokumentierter Starter Blueprint
  - sonst Standard-Blueprint
- Wenn der User `Create from scratch`, `from scratch`, `blank`, `frei starten` oder ohne Template-Vorgabe eine neue Mail starten will, beginnt die erste Preview immer sofort mit dem Standard-Blueprint.
- Fuer diesen freien Initialstart stellt der Agent keine Rueckfragen zu Produkt, Thema, Ziel, Tonalitaet oder Inhalt.
- Fuer diesen freien Initialstart nutzt die erste Preview neutrale Blindtexte oder lorem-ipsum-nahe Platzhalter, neutrale Subject-/Preheader-Werte, das bestehende Hero-CTA-Default und nur bestehende Moduldefaults.
- Die sichtbare Startantwort fuer diesen freien Initialstart ist nur: `Ich starte nun mit dem Blueprint-Aufbau und erstelle die erste Vorschau.`
- Wenn der User `Start mit Template`, `Choose template` oder sinngemaess eine Template-Auswahl anfragt, baut der Agent noch keine freie Mail, sondern sagt sichtbar exakt nur:
  - `Bitte nenne mir die Nummer des Templates, mit dem du starten möchtest:`
  - `1. Loft | SNL`
  - `2. Loft | RNL (Dev)`
  - `3. Loft | Regio (Resi)`
  - `4. Homeowner | ESG`
  - `5. Seeker | MLE`
- Wenn der User `1`, `2`, `3`, `4`, `5`, einen dieser Anzeigenamen oder die zugehoerige technische ID nennt, startet der Agent direkt mit dem passenden Template und nutzt sichtbar nur: `Ich starte nun mit dem Template „<Anzeigename>“ und erstelle die erste Vorschau.`
- Beim initialen Start eines aktiven Templates ist nur die zugehoerige `template-<template_id>.preview.html` die visuelle Quelle der ersten Template-Preview:
  - `loft-snl` -> `template-loft-snl.preview.html`
  - `loft-rnl-dev` -> `template-loft-rnl-dev.preview.html`
  - `loft-regio-resi` -> `template-loft-regio-resi.preview.html`
- In diesem initialen Template-Start sind freie Modulplanung, Einzelmodulsuche, Modulrekonstruktion, generische Ersatzmodule und `preview-modules.html` als primaere Quelle verboten.
- Starter Blueprints nutzen keine `template-*.preview.html`, keine Composition-Template-Pruefung, keine neue Copy-Generierung und keine sichtbare State-Ausgabe oder `EMB_EMAIL_STATE`-Kommentare in der Preview.
- Wenn fuer einen Starter Blueprint ein fertiges `starter-<id>.preview.html` und `starter-<id>.state.json` vorliegen, nutzt der Agent diese beiden Artefakte direkt als ersten Preview-/State-Stand.
- Fuer `ho-esg` sind diese Fast-Path-Artefakte die einzige kanonische Quelle fuer die erste Preview, die festen Preset-Texte und die bereits aufgeloesten `servicetiles`-Services `ELE`, `NDG`, `EA48`, `KWATT`.
- Beim `ho-esg`-Start darf der Agent deshalb weder Module neu zusammensuchen noch Services neu aufloesen noch die erste Copy neu formulieren.
- Fuer `seeker-mle` sind diese Fast-Path-Artefakte die einzige kanonische Quelle fuer die erste Preview, die festen Preset-Texte und die feste Modulfolge `logo-centered`, `hero-fakeform-buttons-image`, `benefits-3col`, `teaser-1col`, `contact-signoff`, `footer`.
- Beim `seeker-mle`-Start darf der Agent deshalb weder Module neu zusammensuchen noch die erste Copy neu formulieren.
- Dieser `ho-esg`-Start bleibt im normalen `default_template`-Flow und ist kein Composition-Template.
- Dieser `seeker-mle`-Start bleibt im normalen `default_template`-Flow und ist kein Composition-Template.
- Erst nach der ersten erfolgreichen Template-Preview gelten fuer Modul-Aenderungen wieder die normalen Source-Fidelity-Regeln ueber bestehende Modulquellen.
- Bei Template- oder Starter-Blueprint-Starts gibt der Agent nie HTML, Quelltext, sichtbaren State oder Modulmarkup im Chat aus; sichtbar bleibt nur der kurze Startsatz, danach folgt die Preview im Canvas.
- Wenn der User beim allerersten Start nur eine freie Modulliste nennt, darf diese Struktur noch nicht direkt in die erste Preview uebernommen werden; stattdessen klaert der Agent kurz: Standard-Blueprint oder aktives Composition-Template.
- Erst nach dem ersten erfolgreichen Preview-Render darf die bestehende Preview frei um Module erweitert, reduziert, ersetzt oder umsortiert werden.
- Nach jeder inhaltlichen oder strukturellen Aenderung wird genau die bestehende Preview fortgeschrieben.

## email_state

- Nach jedem erfolgreichen Preview-Render muss der Agent unmittelbar einen strukturierten `email_state` parallel direkt mitschreiben.
- Dieser `email_state` ist die leichte, feldnahe Arbeitskopie der aktuellen E-Mail und die vorgesehene Happy-Path-Quelle fuer den Export.
- Der `email_state` muss nicht nur konzeptionell bestehen, sondern als eigene strukturierte JSON-Arbeitsdatei neben der aktuellen Preview fortgeschrieben werden.
- Diese JSON-Arbeitsdatei muss nach jedem erfolgreichen Preview-Render denselben Stand wie die sichtbare Preview haben und im spaeteren Export-Lauf direkt wiederverwendbar sein.
- Bei blueprintbasierter Startkomposition muessen die Blueprint-Module vor oder spaetestens mit dem ersten erfolgreichen Preview-Render in einen vollstaendigen `email_state` normalisiert werden.
- Vor dem ersten erfolgreichen Preview-Render muss die Modulfolge auf Logo-Hero-Konsistenz normalisiert werden:
  - Wenn die finale Modulfolge eines der Center-Hero-Module `hero-image-top-center`, `hero-image-top-bleed-center`, `hero-cta-top-center`, `hero-cta-top-no-bottom-center`, `hero-image-head-copy-bleed-center`, `hero-image-textbox-cta-center` oder `hero-fakeform-buttons-image` enthaelt, wird ein vorhandenes `logo` an derselben Position zu `logo-centered` normalisiert.
  - Wenn in diesem Center-Hero-Kontext bereits `logo-centered` vorhanden ist, darf kein zweites Logo eingefuegt werden.
  - Wenn in diesem Center-Hero-Kontext kein Logo vorhanden ist, darf nur die bestehende Pflichtmodul-Logik das passende Logo ergaenzen.
  - Ohne Center-Hero-Kontext bleibt `logo` regulaer zulaessig.
- Blueprint-Module duerfen nie nur als sichtbare Preview ohne gleichwertigen `email_state` weiterlaufen.
- Der `email_state` soll mindestens enthalten:
  - Subject
  - Preheader
  - eindeutigen Template-Kontext
  - aufgeloesten `salutationContext`
  - Modulfolge
  - Modultyp pro Block
  - alle exportrelevanten Felder pro Modul
  - sichtbare Item-Anzahl pro Multi-Item-Modul
  - relevante Show-Flags sowie Bild- und Iconquellen pro Slot
  - die aktuell zugeordnete Iterable-`campaignId` und das campaign-owned `templateId`, sobald fuer genau diese Preview bereits ein erfolgreicher Export vorliegt
- Fuer exportfaehige States muessen `subject` und `preheader` bereits vor dem Export als konkrete String-Werte im State vorliegen.
- Der aktive Template-Kontext muss bereits beim Preview-Bau eindeutig im State stehen:
  - Standard-Blueprint oder spaetere freie Moduliteration -> `templateContext.mode = default_template` und `templateContext.resolvedBaseTemplateId = 569946`
  - editable Starter Blueprints wie `ho-esg` oder `seeker-mle` -> `templateContext.mode = default_template` und `templateContext.resolvedBaseTemplateId = 569946`; kein `compositionTemplateId`, kein `iterableTemplateId`
  - Composition-Template -> `templateContext.mode = composition_template`, `templateContext.compositionTemplateId`, `templateContext.iterableTemplateId` und `templateContext.resolvedBaseTemplateId = iterable_template_id`
- Der aufgeloeste Salutation-Kontext soll bereits beim Preview-Bau eindeutig im State stehen:
  - aktives Composition-Template mit `salutation_context_id` -> exakt dieser Wert
  - explizite User-Nennung -> Resolver ueber `agent/product-salutations.json`
  - freier Initialstart ohne erkennbare Zuordnung -> `generic`
- `salutationContext` steuert nur dokumentierte Anrede-Resolver und ist nie ein freies User-HTML-, Handlebars- oder Snippet-Feld.
- Wenn dieselbe Preview fortgeschrieben wird, muss ihre Campaign-Bindung ueber einen stabilen `previewBranchKey` im State nachvollziehbar bleiben; Re-Export darf `campaignId` und campaign-owned `templateId` nur fuer genau diesen Zweig wiederverwenden.
- Exportrelevante technische Werte muessen bereits beim Preview-Bau in `email_state.content` geschrieben werden und duerfen nicht erst im Export rekonstruiert werden.
- Der Salutation-Kontext-Resolver kommt ausschliesslich aus `agent/product-salutations.json` und aktiven Template-Definitionen.
- Aktuell sind als `salutationContext` nur `generic`, `rle`, `loft-snl`, `loft-rnl-dev` und `loft-regio-resi` erlaubt; unbekannte explizite Team- oder Produktnennungen muessen vor dem Preview geklaert werden.
- Inhaltliche Produktdefaults jenseits der Anrede bleiben aktuell nur fuer `RLE` erlaubt und muessen bereits vor oder spaetestens waehrend des Preview-Baus in die bestehenden Modulfelder materialisiert werden; ein freies Produkt-Raten waehrend des State-Baus ist verboten.
- Dazu gehoeren insbesondere:
  - alle required `*_bg_color`
  - alle required `show_*`- und `hide_*`-Flags
  - alle required `*_icon_url`
  - alle required finalen `*_button_bg_color`- und `*_button_border_color`-Werte
  - getrennte `salutation`- und `rich_*`-Werte, wenn ein Modul beides nutzt
- Fuer alle elf Hero-Module ist die Anrede ein optionaler eigener Textblock vor dem Body:
  - `*_show_salutation` ist das kanonische Show-/Hide-Feld
  - `*_salutation` bleibt Plain Text
  - `*_use_snippetcall_salutation` ist nur ein technisches Export-Flag fuer freigegebene Produktkontexte und wird in der Preview nie roh sichtbar
  - neue Hero-Default-States muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren
- Unabhaengig vom `salutationContext` darf die Preview nie Raw-Handlebars, freie Snippetcalls oder Iterable-Logik sichtbar machen.
- Wenn der aktive `salutationContext` `rle` ist, bleibt die sichtbare Preview-Hero-Anrede trotzdem unveraendert `Hallo Anrede,`; der spaetere RLE-Export-Zielwert darf in der Preview nie sichtbar werden.
- Wenn der aktive `salutationContext` `rle` ist, muessen fuer Hero-Module zusaetzlich die passenden technischen Export-Flags `*_use_snippetcall_salutation = true` in den `email_state` materialisiert werden, ohne die sichtbare Preview-Anrede zu veraendern.
- Wenn der aktive `salutationContext` `loft-snl`, `loft-rnl-dev` oder `loft-regio-resi` ist, bleibt die bestehende template- oder modulspezifische menschenlesbare Preview-Anrede erhalten; es wird keine neue freie Export-Logik in die Preview eingeblendet.
- Fuer `loft-rnl-dev-intro` muss die Preview diese Builder-Felder materialisieren:
  - `emb_loft_rnl_dev_intro_headline = Immobilien-Newsletter München` oder User-Wert
  - `emb_loft_rnl_dev_intro_salutation = Hallo Anrede`
  - `emb_loft_rnl_dev_intro_body` als `rich_full`
- Fuer `loft-rnl-dev-intro` muss die finale EMB-Preview-HTML die Hauptheadline direkt mit der bestehenden `heading-l`-Semantik `font-heading-large-bold` materialisieren; eine groessere Hero-/XL-Klasse oder ein reiner Loft-Sonderselector ohne diese Klasse ist unzulaessig.
- Der spaetere produktive Exportwert von `emb_loft_rnl_dev_intro_salutation` fuer `salutationContext = loft-rnl-dev` darf in der Preview nie roh sichtbar werden.
- Fuer `loft-rnl-dev-teaser-1col` muss die finale EMB-Preview-HTML die Hauptheadline direkt mit der bestehenden `heading-l`-Semantik `font-heading-large-bold` materialisieren; groessere Hero-/XL-Klassen sind unzulaessig.
- Fuer `loft-rnl-dev-teaser-1col` darf die Badge-Inversion in der finalen EMB-Preview nicht von statischen `theme-*`-Annahmen am Modulwrapper abhaengen.
- Die Badge-Inversion fuer `loft-rnl-dev-teaser-1col` muss in der finalen Preview direkt aus `emb_loft_rnl_dev_teaser_1col_bg_color` materialisiert werden:
  - `#F5F5F5` Modulhintergrund => `module__badge module__badge--surface-white`
  - `#FFFFFF` Modulhintergrund => `module__badge module__badge--surface-gray`
- Fuer weitere wiederholte `loft-rnl-dev-teaser-1col`-Instanzen bleibt diese Badge-Regel strikt an den finalen alternierenden Hintergrund-Rhythmus gekoppelt.
- Fuer `loft-regio-resi-intro` muss die Preview diese Builder-Felder materialisieren:
  - `emb_loft_regio_resi_intro_headline = Ausgewählte Wohnimmobilien aus Ihrer Region` oder User-Wert
  - `emb_loft_regio_resi_intro_salutation = Hallo Anrede`
  - `emb_loft_regio_resi_intro_body` als `rich_full`
- Fuer `loft-regio-resi-intro` muss die finale EMB-Preview-HTML die Hauptheadline direkt mit der bestehenden `heading-l`-Semantik `font-heading-large-bold` materialisieren; eine groessere Hero-/XL-Klasse oder ein reiner Loft-Sonderselector ohne diese Klasse ist unzulaessig.
- Der spaetere produktive Exportwert von `emb_loft_regio_resi_intro_salutation` fuer `salutationContext = loft-regio-resi` darf in der Preview nie roh sichtbar werden.
- Fuer `loft-regio-resi-teaser-1col` muss die finale EMB-Preview-HTML die Hauptheadline direkt mit der bestehenden `heading-l`-Semantik `font-heading-large-bold` materialisieren; groessere Hero-/XL-Klassen sind unzulaessig.
- Die Desktop-Kennzahlen und die mobile Bullet-Liste von `loft-regio-resi-teaser-1col` muessen dieselben Felder `emb_loft_regio_resi_teaser_1col_metric_1..3_label` und `emb_loft_regio_resi_teaser_1col_metric_1..3_value` verwenden.
- In der mobilen Liste von `loft-regio-resi-teaser-1col` bleibt das Label normaler Text; nur der jeweilige Wert ist fett.
- Wenn der aktive Produktkontext `RLE` ist und ein `contact`-Modul genutzt wird, muessen ohne explizite User-Overrides diese bestehenden Contact-Felder im Preview-/State-Bau mit den RLE-Defaults materialisiert werden:
  - `emb_contact_show_image`
  - `emb_contact_image_url`
  - `emb_contact_image_alt`
  - `emb_contact_headline`
  - `emb_contact_body_intro`
  - `emb_contact_phone`
  - `emb_contact_phone_hours`
  - `emb_contact_email_intro`
  - `emb_contact_email_address`
  - `emb_contact_email_url`
  - `emb_contact_closing_line_1`
  - `emb_contact_closing_line_2`
- Fuer RLE nutzt das Contact-Modul an der bestehenden Placeholder-Position ein normales Bildslot:
  - `emb_contact_show_image = true`
  - `emb_contact_image_url = https://library.eu.iterable.com/33/98/732ff156cb6b4fc188b76f0e07b2744e-avatar-woman.png`
  - `emb_contact_image_alt = Beraterin aus dem ImmoScout24-Team`
- Das Contact-Modul bleibt dabei immer auf weissem Hintergrund und bekommt kein alternierendes oder usersteuerbares `bg_color`-Feld.
- Finale required Button-Farbwerte muessen beim Preview-Bau ueber die dokumentierte Button-Farbaufloesung aus `builder-library.md` konkret in `email_state.content` materialisiert werden.
- Fehlende required Werte duerfen beim Preview-Bau nur aus zwei eng begrenzten Quellen ergaenzt werden:
  - aus einem eindeutigen technischen Default der `export-map.json`
  - aus einer dokumentierten technischen Resolver-Quelle
- Fuer `servicetiles` zaehlt `agent/service-products.json` als zulaessige dokumentierte technische Resolver-Quelle, aber nur fuer die kontrollierte Aufloesung von fachlich genau `4` Services in die finalen Card-Felder `emb_servicetiles_col_1..4_(icon_url|title|description|url)`.
- Wenn fuer `servicetiles` weniger oder mehr als `4` Services vorliegen oder ein Service nicht eindeutig ueber `id` oder `aliases` der Registry aufloesbar ist, ist die Preview nicht export-ready und der Agent muss vor dem Rendern nachfragen.
- Wenn eine Felddefinition in `export-map.json` `allowed_values` definiert, muss der beim Preview-Bau materialisierte Feldwert exakt einem dieser erlaubten Werte entsprechen; jeder andere Wert ist ein lokaler State-Fehler und die Preview ist nicht export-ready.
- Wenn ein required Wert weder aus dem State-Inhalt noch aus einem eindeutigen technischen Default der `export-map.json` noch aus einer dokumentierten technischen Resolver-Quelle konkret befuellt werden kann, ist die Preview nicht export-ready und der Agent muss vor dem Export stoppen.
- Fuer `hero-image-top` ist `emb_hero_image_top_headline_size` das einzige kanonische Groessenfeld fuer die Headline und darf nur `s`, `m` oder `l` tragen.
- Neue reguläre Default-States fuer `hero-image-top` muessen schon beim Preview-Bau `emb_hero_image_top_headline_size = l`, `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = true` materialisieren.
- Legacy-Normalisierung fuer `hero-image-top` ist nur waehrend des Preview-Baus zulaessig:
  - wenn `emb_hero_image_top_headline_size` fehlt oder leer ist und `emb_hero_image_top_show_large_headline = true`, wird kanonisch zu `l` normalisiert
  - wenn `emb_hero_image_top_headline_size` fehlt oder leer ist und `emb_hero_image_top_show_large_headline = false` oder leer ist, wird kanonisch zu `m` normalisiert
- Nach der kanonischen Aufloesung von `emb_hero_image_top_headline_size` muessen die technischen Bridge-Felder fuer `hero-image-top` direkt in `email_state.content` materialisiert werden:
  - `s` => `emb_hero_image_top_show_small_headline = true` und `emb_hero_image_top_show_large_headline = false`
  - `m` => `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = false`
  - `l` => `emb_hero_image_top_show_small_headline = false` und `emb_hero_image_top_show_large_headline = true`
- Wenn bei `hero-image-top` `emb_hero_image_top_show_small_headline = true` und `emb_hero_image_top_show_large_headline = true` gleichzeitig vorliegen, ist die Preview nicht export-ready und der Agent muss vor dem Export stoppen.
- Wenn die Bridge-Felder von `hero-image-top` nicht exakt zur kanonischen `emb_hero_image_top_headline_size` passen, ist das ein lokaler State-Fehler und die Preview ist nicht export-ready.
- Fuer `hero-image-top-center`, `hero-image-top-bleed`, `hero-image-top-bleed-center`, `hero-fakeform-buttons-image`, `hero-cta-top`, `hero-cta-top-center`, `hero-cta-top-no-bottom` und `hero-cta-top-no-bottom-center` gilt dasselbe kanonische Hero-Modell:
  - genau ein `*_headline_size`-Feld mit nur `s`, `m` oder `l`
  - neue reguläre Default-States muessen `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` materialisieren
  - die technischen Bridge-Felder muessen exakt aus dem kanonischen `headline_size` abgeleitet werden
  - `show_small_headline = true` und `show_large_headline = true` gleichzeitig ist ungueltig und macht die Preview nicht export-ready
- Fuer `hero-image-head-copy-bleed-center` gilt dasselbe kanonische Hero-Modell:
  - genau ein `emb_hero_image_head_copy_bleed_center_headline_size`-Feld mit nur `s`, `m` oder `l`
  - neue reguläre Default-States muessen `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` materialisieren
  - die technischen Bridge-Felder muessen exakt aus dem kanonischen `headline_size` abgeleitet werden
  - `show_small_headline = true` und `show_large_headline = true` gleichzeitig ist ungueltig und macht die Preview nicht export-ready
- Fuer jedes Modul mit required `*_bg_color` in `export-map.json` muss der `email_state` dieses Feld direkt aus dem operativen Hintergrund-Rhythmus in `content` mitschreiben.
- Required `*_bg_color`-Felder muessen dabei immer als konkrete produktive Hexwerte in `content` stehen, nicht als semantische Farbnamen, nicht als `theme-*`-Klassen und nicht als offene Rhythmus-Markierung.
- Wenn ein required `*_bg_color` fuer ein Modul nicht gesetzt werden kann, ist das ein Fehler und kein Default-Fallback-Fall.
- Wenn der operative Hintergrund-Rhythmus fuer ein required `*_bg_color` nicht eindeutig bis zu einem konkreten Hexwert aufgeloest werden kann, gilt die Preview als nicht exportfaehig und der Agent muss vor dem Mitschreiben oder Fortfuehren stoppen.
- Normale Text-Felder im `email_state.content` enthalten Plain Text.
- `rich_inline`-Felder im `email_state.content` duerfen nur sanitisiertes builder-eigenes Inline-HTML enthalten.
- `rich_full`-Felder im `email_state.content` duerfen nur sanitisiertes builder-eigenes Richtext-HTML enthalten.
- Beim Mitschreiben des `email_state` muessen `rich_inline`- und `rich_full`-Felder ihre sichtbare Struktur aus dem gerenderten Modul in sanitisiertem Builder-HTML behalten.
- Fuer `rich_inline` sind nur diese Tags erlaubt:
  - `strong`
  - `em`
  - `a`
  - `br`
- Fuer `rich_full` sind nur diese Tags erlaubt:
  - `p`
  - `ul`
  - `ol`
  - `li`
  - `strong`
  - `em`
  - `a`
  - `br`
- Andere Tags, freie Wrapper, Skripte, Styles, Event-Handler, Klassen und freie Attribute sind verboten.
- Erlaubte Attribute in Richtext-Feldern sind auf sichere Link-Attribute begrenzt:
  - bei `a`: `href`, `target`, `rel`
- Recovery-Fallback aus der letzten sichtbaren Preview darf fuer `rich_inline` und `rich_full` genau diese erlaubten HTML-Fragmente rekonstruieren.
- Die technische Felddefinition je Modul kommt ausschliesslich aus `export-map.json`.
- Bei Multi-Item-Modulen folgen Feldzuordnung und sichtbare Item-Anzahl direkt den markierten sichtbaren Items mit ihren Indizes.
- Bei blueprintbasierten Mails muessen alle required Felder pro Modul direkt aus Blueprint-Inhalt, erlaubten Defaults aus `export-map.json`, dem operativen Hintergrund-Rhythmus oder den kanonischen Builder-Defaults befuellt werden.
- Bei blueprintbasierten Mails duerfen required `*_bg_color`-Felder nicht als `theme-white`, `theme-gray` oder aehnliche Preview-Zustaende im `email_state` verbleiben; sie muessen vor dem Speichern konkret zu `#FFFFFF` oder `#F5F5F5` aus der verbindlichen Farbquelle aufgeloest sein.
- Fuer `hero-image-top` im Standard-Blueprint muessen mindestens `emb_hero_image_top_headline_size`, `emb_hero_image_top_show_small_headline`, `emb_hero_image_top_show_large_headline`, `emb_hero_image_top_show_salutation`, `emb_hero_image_top_headline`, `emb_hero_image_top_salutation`, `emb_hero_image_top_body`, `emb_hero_image_top_button_label`, `emb_hero_image_top_button_url` und `emb_hero_image_top_bg_color` sicher im `email_state` vorliegen; `image_url`, `image_alt` und Button-Farben duerfen ueber die erlaubten Defaults aus `export-map.json` kommen.
- Fuer `hero-image-textbox-cta-center` muessen mindestens `emb_hero_image_textbox_cta_center_bg_color`, `emb_hero_image_textbox_cta_center_headline_size`, `emb_hero_image_textbox_cta_center_show_small_headline`, `emb_hero_image_textbox_cta_center_show_large_headline`, `emb_hero_image_textbox_cta_center_show_salutation`, `emb_hero_image_textbox_cta_center_headline`, `emb_hero_image_textbox_cta_center_image_url`, `emb_hero_image_textbox_cta_center_salutation`, `emb_hero_image_textbox_cta_center_body`, `emb_hero_image_textbox_cta_center_question`, `emb_hero_image_textbox_cta_center_entry_url`, `emb_hero_image_textbox_cta_center_entry_text`, `emb_hero_image_textbox_cta_center_button_label` und `emb_hero_image_textbox_cta_center_button_url` sicher im `email_state` vorliegen; `image_alt`, `button_bg_color` und `button_border_color` duerfen ueber die erlaubten Defaults aus `export-map.json` kommen.
- Fuer `hero-image-textbox-cta-center` gilt dasselbe kanonische Hero-Modell:
  - genau ein `emb_hero_image_textbox_cta_center_headline_size`-Feld mit nur `s`, `m` oder `l`
  - neue reguläre Default-States muessen `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` materialisieren
  - die technischen Bridge-Felder muessen exakt aus dem kanonischen `headline_size` abgeleitet werden
  - `show_small_headline = true` und `show_large_headline = true` gleichzeitig ist ungueltig und macht die Preview nicht export-ready
- Fuer `hero-fakeform-buttons-image` muessen mindestens `emb_hero_fakeform_buttons_image_bg_color`, `emb_hero_fakeform_buttons_image_headline_size`, `emb_hero_fakeform_buttons_image_show_small_headline`, `emb_hero_fakeform_buttons_image_show_large_headline`, `emb_hero_fakeform_buttons_image_show_item_2`, `emb_hero_fakeform_buttons_image_show_item_3`, `emb_hero_fakeform_buttons_image_show_item_4`, `emb_hero_fakeform_buttons_image_show_item_5`, `emb_hero_fakeform_buttons_image_show_item_6`, `emb_hero_fakeform_buttons_image_show_salutation`, `emb_hero_fakeform_buttons_image_headline`, `emb_hero_fakeform_buttons_image_choice_button_1_label`, `emb_hero_fakeform_buttons_image_choice_button_1_url`, `emb_hero_fakeform_buttons_image_choice_button_2_label`, `emb_hero_fakeform_buttons_image_choice_button_2_url`, `emb_hero_fakeform_buttons_image_image_url`, `emb_hero_fakeform_buttons_image_salutation`, `emb_hero_fakeform_buttons_image_body`, `emb_hero_fakeform_buttons_image_button_label` und `emb_hero_fakeform_buttons_image_button_url` sicher im `email_state` vorliegen; `image_alt`, spaetere sichtbare Choice-Button-Felder sowie `button_bg_color` und `button_border_color` duerfen ueber die erlaubten Defaults aus `export-map.json` kommen.
- Fuer `hero-fakeform-buttons-image` gilt dasselbe kanonische Hero-Modell:
  - genau ein `emb_hero_fakeform_buttons_image_headline_size`-Feld mit nur `s`, `m` oder `l`
  - neue reguläre Default-States muessen `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` materialisieren
  - die technischen Bridge-Felder muessen exakt aus dem kanonischen `headline_size` abgeleitet werden
  - `show_small_headline = true` und `show_large_headline = true` gleichzeitig ist ungueltig und macht die Preview nicht export-ready
  - Default sichtbar sind genau `5` Auswahlbuttons; `show_item_6` bleibt initial `false`
  - Button `1` bleibt immer sichtbar und `show_item_2` darf nie `false` werden, weil die Mindestanzahl `2` verbindlich bleibt
- Fuer die regulare Standard-Testkombination `logo`, `hero-image-top`, `steps-3col`, `footer` muss der `email_state` nach dem Preview-Bau mindestens sicher enthalten:
  - fuer `logo`: leeres `content` ist zulaessig, weil `emb_logo` aktuell als statisches Snippet ohne Export-Parameter aufgerufen wird
  - fuer `hero-image-top`: alle required Content-Felder plus `emb_hero_image_top_bg_color`
  - fuer `steps-3col`: `emb_steps_3col_bg_color`, Headline, alle drei Step-Bodies sowie CTA-Felder
  - fuer `footer`: leeres `content` ist zulaessig
- Nach einem erfolgreichen ersten Export wird die erzeugte `campaignId` fest an genau diese bestehende Preview und ihren aktuellen `email_state` gebunden.
- Solange dieselbe Preview nur fortgeschrieben wird, bleibt diese Campaign-Bindung erhalten und ist beim Re-Export wiederzuverwenden.
- Wenn eine wirklich neue Preview oder neue Startkomposition begonnen wird, darf keine alte Campaign-Bindung uebernommen werden; der neue Preview-Zweig startet ohne `campaignId`.
- Preview-DOM oder markierte Preview-Knoten duerfen nur als Debug- oder Recovery-Fallback erwaehnt werden, nicht als regulaerer Happy Path.
- Wenn kein vollstaendiger `email_state` vorhanden ist, darf genau einmal ein enger Recovery-Fallback aus der letzten sichtbaren Preview erzeugt werden.
- Dieser Recovery-Fallback darf nur aus der letzten sichtbaren Preview, ihren markierten Knoten, markierten URL-Feldern ueber `data-export-url-field`, den registrierten Icon-Slots, den Bild-Slots, den Moduldefaults aus `export-map.json` und dem operativen Hintergrund-Rhythmus ableiten.
- Auch im Recovery-Fallback muessen required `*_bg_color`-Felder vor dem Fortschreiben des reparierten `email_state` wieder als konkrete Hexwerte und nie als `theme-*`-Klassen vorliegen.
- Danach muss der reparierte `email_state` wieder als JSON-Arbeitsdatei fortgeschrieben werden.

## Erfolg

- `Preview-Erfolg` liegt nur vor, wenn die HTML-Preview-Datei im Canvas erstellt oder aktualisiert wurde.
- Eine Textvorschau im Chat ist nie `Preview-Erfolg`.

## Chat-Ausgabe

- Die komplette HTML-Preview darf im normalen Preview-/Export-Flow nicht automatisch vollstaendig im Chat ausgegeben werden.
- Wenn die Laufzeit eine kompakte Preview-Karte, Canvas-Preview oder andere kurze Vorschauform bietet, soll diese statt eines grossen HTML-Blocks genutzt werden.
- Wenn keine kompakte Kartenansicht verfuegbar ist, bleibt die Chat-Ausgabe bei einer kurzen Bestaetigung plus Hinweis auf die erstellte Preview-Datei oder Vorschau.
- Vollstaendiges Preview-HTML darf nur ausgegeben werden, wenn der User ausdruecklich danach fragt.
- Vor dem eigentlichen Preview-Bau sind keine technischen Prozessmeldungen wie `1. Preview`, `Preview-Erstellung gestartet` oder Modulauflistungen zulaessig.
- Nach erfolgreicher Preview darf kein automatischer Exportversuch, kein automatischer Iterable-Connect und kein impliziter CreateCampaign-Start folgen.
- Hoechstens eine kurze Anschlussfrage zum Export ist zulaessig, z. B. ob diese Version nach Iterable exportiert werden soll.
- Deutsch:
  - `Die Preview-Mail wurde erstellt. Wenn Sie moechten, koennen wir Komponenten, Reihenfolge oder Texte weiter anpassen.`
  - `Einen Ueberblick ueber alle verfuegbaren Komponenten finden Sie hier: [E-Mail component library](https://s24-creative-ops.github.io/builder-library/#email-logo)`
- Englisch:
  - `The preview mail has been created. If you like, we can further adjust components, order, or texts.`
  - `You can find an overview of all available components here: [E-Mail component library](https://s24-creative-ops.github.io/builder-library/#email-logo)`
- Interne Speicher-, State-, Recovery- oder Zwischenmeldungen duerfen im normalen User-Flow nicht als eigene Chat-Ereignisse sichtbar werden.
```

## email-builder/agent/preview-module-library.md

Dateityp: md

```md
# Preview Module Library

Diese Datei beschreibt die Preview-Module, ihre sichtbaren Eingaben und ihre Render-Bedeutung.
Die technische Export-Wahrheit liegt ausschliesslich in `export-map.json`.

## Render-Regel

- `agent/preview-modules.html` ist die kanonische strukturelle Quelle fuer bestehende Preview-Module.
- Diese Datei dient nur fuer Auswahl, Beschreibung, sichtbare Felder und Feldlogik, nicht zum freien Nachbauen von HTML.
- Jedes Modul muss mit seiner HTML-Struktur aus `preview-modules.html` gerendert werden.
- Die Preview beginnt immer mit `preview-template.html`.
- Wenn ein Modul hier nicht registriert ist, darf es nicht gerendert werden.
- Wenn fuer einen registrierten Bild-Slot keine echte User-Bild-URL vorliegt, bleibt in der Preview die graue Placeholder-Flaeche aus `preview-modules.html` sichtbar.
- Wenn fuer einen registrierten Bild-Slot eine echte User-Bild-URL vorliegt, ersetzt diese URL in der Preview die graue Placeholder-Flaeche fuer genau diesen Slot.
- Die Preview dient der visuellen Iteration. Die regulaere Exportlogik arbeitet nicht aus Preview-HTML.
- Kritische responsive Gruppen als Warnhinweis: `teaser-2col-*`, `servicetiles`, `teaser-2col-gallery` sowie Module mit Row-/Grid-/Stack-Klassen.

## Technische Trennung

- `export-map.json` ist die einzige technische Quelle fuer erlaubte Export-Felder, Defaults und Snippet-Namen.
- `email_state.content` ist die einzige Exportquelle fuer Iterable-Variablen.
- Exportrelevante technische Werte muessen bereits beim Preview-Bau konkret in `email_state.content` materialisiert werden und duerfen nicht erst im Export aus Preview-Darstellung oder Modulkontext rekonstruiert werden.
- Dazu gehoeren insbesondere:
  - required `*_bg_color`
  - required `show_*`- und `hide_*`-Flags
  - required `*_icon_url`
  - required finale Button-Farbwerte
  - getrennte `salutation`- und `rich_*`-Werte fuer Module, die beides nutzen
- Required `*_bg_color`-Felder muessen dort als konkrete Hexwerte aus dem operativen Hintergrund-Rhythmus vorliegen.
- `theme-white`, `theme-gray` oder andere Preview-Klassen sind in `email_state.content` keine zulaessigen Exportwerte.
- Normale Text-Felder bleiben Plain Text.
- `rich_inline` und `rich_full` duerfen dort nur als sanitisiertes builder-eigenes HTML-Fragment liegen, nicht als freier HTML-Block.
- Salutation-/Anredezeilen sind eigene kurze Textkontexte vor einem Body und gehoeren nicht in ein `rich_full`-HTML-Fragment.
- Salutation-/Anredezeilen duerfen keine Listen enthalten und sind in der Feldtypisierung nur Plain Text oder hoechstens `rich_inline`, niemals `rich_full`.
- Der Abstand zwischen Salutation und nachfolgendem Body ist ein externer Kontextabstand; Absatz-/Listen-Abstaende innerhalb des Bodys bleiben Aufgabe des allgemeinen `rich_full`-Flows.
- Fuer den allgemeinen `rich_full`-Flow gilt:
  - Text zu Text = 16px
  - Text zu Liste = 8px
  - Liste zu Text = 8px
  - Liste zu Liste = 8px
- Der Abstand zwischen einer Headline und dem ersten `rich_full`-Element bleibt externer Kontextabstand und entsteht nicht aus der internen Listenregel.
- Wenn eine Liste das erste Element im `rich_full`-Body ist, bekommt sie keinen zusaetzlichen internen Top-Abstand.
- Listen bleiben im allgemeinen `rich_full`-Kontext optisch auf 20px eingerueckt.
- `p`, `ul` und `ol` tragen im allgemeinen `rich_full`-Kontext keine eigenen allgemeinen Top-/Bottom-Defaults ausserhalb der zentralen Flow-Regeln.
- Review-Dateien unter `development/review/*` sind nur Test-Artefakte und nie technische oder fachliche Quelle.
- Preview-Marker oder Preview-DOM duerfen hoechstens fuer Debug oder Recovery erwaehnt werden, nie als regulaerer Happy Path.

## Typography-Regeln

- Nur Hero-Headlines duerfen in der Preview ueber ein kanonisches Groessenfeld steuerbar sein.
- Erlaubte Hero-Groessen sind ausschliesslich `s`, `m` und `l`.
- Das Hero-Mapping folgt immer direkt den Typography-Tokens:
  - `s` = `heading-s`
  - `m` = `heading-m`
  - `l` = `heading-l`
- Der reguläre Hero-Default ist `l`.
- Nicht-Hero-Modulheadlines sind nicht usersteuerbar.
- Die erste sichtbare Hauptheadline eines Nicht-Hero-Moduls ist immer `heading-m`, ausser eine dokumentierte modulspezifische Ausnahme in dieser Datei erlaubt fest `heading-l`.
- Weitere Unter-Headlines, Abschnittstitel oder Zwischenueberschriften innerhalb eines Nicht-Hero-Moduls sind immer `heading-s`.
- Bodytexte bleiben standardmaessig `body-standard`.
- Freie Heading-Klassen, freie CSS-Werte, freie Font-Size-Werte, freies HTML oder freie Style-Werte sind fuer Typography-Steuerung nicht zulaessig.

## Iconslot-Registry

- `benefits-3col`
  - `emb_benefits_3col_col_1_icon_url`
  - `emb_benefits_3col_col_2_icon_url`
  - `emb_benefits_3col_col_3_icon_url`

Regeln:

- Erlaubte Icon-URLs duerfen nur aus `icon-library.md` kommen.
- Wenn ein Modul mit registrierten Icon-Slots gerendert wird, muessen alle diese Slots befuellt werden.
- Wenn kein Bucket klar passt, nutze den kanonischen `general-positive`-Fallback aus `icon-library.md`.

## Bildslot-Registry

### 16:9-Slots

- `hero-image-top`
  - `emb_hero_image_top_image_url`
- `hero-image-top-center`
  - `emb_hero_image_top_center_image_url`
- `hero-image-top-bleed`
  - `emb_hero_image_top_bleed_image_url`
- `hero-image-top-bleed-center`
  - `emb_hero_image_top_bleed_center_image_url`
- `hero-image-head-copy-bleed-center`
  - `emb_hero_image_head_copy_bleed_center_image_url`
- `hero-image-textbox-cta-center`
  - `emb_hero_image_textbox_cta_center_image_url`
- `hero-fakeform-buttons-image`
  - `emb_hero_fakeform_buttons_image_image_url`
- `hero-cta-top`
  - `emb_hero_cta_top_image_url`
- `hero-cta-top-center`
  - `emb_hero_cta_top_center_image_url`
- `hero-cta-top-no-bottom`
  - `emb_hero_cta_top_no_bottom_image_url`
- `hero-cta-top-no-bottom-center`
  - `emb_hero_cta_top_no_bottom_center_image_url`
- `teaser-1col`
  - `emb_teaser_1col_image_url`
- `loft-rnl-dev-teaser-1col`
  - `emb_loft_rnl_dev_teaser_1col_image_url`
- `loft-regio-resi-teaser-1col`
  - `emb_loft_regio_resi_teaser_1col_image_url`
- `teaser-2col-vertical`
  - `emb_teaser_2col_vertical_col_1_image_url`
  - `emb_teaser_2col_vertical_col_2_image_url`
- `teaser-2col-horizontal`
  - `emb_teaser_2col_horizontal_col_1_image_url`
  - `emb_teaser_2col_horizontal_col_2_image_url`
  - `emb_teaser_2col_horizontal_col_3_image_url`
  - `emb_teaser_2col_horizontal_col_4_image_url`
- `teaser-2col-gallery`
  - `emb_teaser_2col_gallery_col_1_image_url`
  - `emb_teaser_2col_gallery_col_2_image_url`
  - `emb_teaser_2col_gallery_col_3_image_url`
  - `emb_teaser_2col_gallery_col_4_image_url`

### 4:3-Slots

- `teaser-2col-alternating`
  - `emb_teaser_2col_alternating_col_1_image_url`
  - `emb_teaser_2col_alternating_col_2_image_url`
- `teaser-2col-listing`
  - `emb_teaser_2col_listing_col_1_image_url`
  - `emb_teaser_2col_listing_col_2_image_url`
  - `emb_teaser_2col_listing_col_3_image_url`
  - `emb_teaser_2col_listing_col_4_image_url`

### Avatar-Slots

- `contact`
  - `emb_contact_image_url`

### Service-Produkt-Slots

- `servicetiles`
  - `emb_servicetiles_col_1_icon_url`
  - `emb_servicetiles_col_2_icon_url`
  - `emb_servicetiles_col_3_icon_url`
  - `emb_servicetiles_col_4_icon_url`

## Unterstuetzte Module

### `logo`

- Snippet: `emb_logo`
- Preview-Quelle: `preview-modules.html`, Block `data-module="logo"`
- Sichtbare Felder:
  - Logo
- Fuellhinweis: unveraendert verwenden
- Technische Regel: statisches Export-Snippet ohne Parameter.

### `logo-centered`

- Snippet: `emb_logo_centered`
- Preview-Quelle: `preview-modules.html`, Block `data-module="logo-centered"`
- Sichtbare Felder:
  - Logo
- Fuellhinweis: verwenden, wenn das Standard-Logo zentriert statt linksbuendig erscheinen soll; bei den Center-Hero-Modulen `hero-image-top-center`, `hero-image-top-bleed-center`, `hero-cta-top-center`, `hero-cta-top-no-bottom-center`, `hero-image-head-copy-bleed-center`, `hero-image-textbox-cta-center` und `hero-fakeform-buttons-image` ist dies die verbindliche Logo-Variante
- Technische Regel: statisches Export-Snippet ohne Parameter.

### `hero-image-top`

- Snippet: `emb_hero_image_top`
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-image-top"`
- Sichtbare Felder:
  - Eyebrow
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
  - Bild-URL
  - Bild-Alt
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: feste Hero-Variante mit Bild oberhalb von Body und Brand-CTA beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_image_top_show_salutation` und `emb_hero_image_top_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_image_top_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_image_top_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_image_top_show_small_headline` und `emb_hero_image_top_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Legacy gilt nur fuer Normalisierung beim Preview-Bau:
    - `emb_hero_image_top_show_large_headline = true` ohne kanonisches `headline_size` => `headline_size = l`
    - `emb_hero_image_top_show_large_headline = false` oder leer ohne kanonisches `headline_size` => `headline_size = m`
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - Freie px-, CSS-, HTML- oder Inline-Style-Werte sind fuer diese Headline-Groesse nicht zulaessig.

### `hero-image-top-center`

- Snippet: `emb_hero_image_top_center`
- Ausrichtung: Eyebrow oder Badge, Headline, Anrede, Body und CTA sind zentriert.
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-image-top-center"`
- Sichtbare Felder:
  - Eyebrow
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
  - Bild-URL
  - Bild-Alt
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: feste zentrierte Hero-Variante mit zentrierte Meta-, Headline-, Copy- und CTA-Ausrichtung mit Bild oberhalb von Body und Brand-CTA beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_image_top_center_show_salutation` und `emb_hero_image_top_center_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_image_top_center_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_image_top_center_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_image_top_center_show_small_headline` und `emb_hero_image_top_center_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Legacy gilt nur fuer Normalisierung beim Preview-Bau:
    - `emb_hero_image_top_center_show_large_headline = true` ohne kanonisches `headline_size` => `headline_size = l`
    - `emb_hero_image_top_center_show_large_headline = false` oder leer ohne kanonisches `headline_size` => `headline_size = m`
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - Freie px-, CSS-, HTML- oder Inline-Style-Werte sind fuer diese Headline-Groesse nicht zulaessig.

### `hero-image-top-bleed`

- Snippet: `emb_hero_image_top_bleed`
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-image-top-bleed"`
- Sichtbare Felder:
  - Eyebrow
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
  - Bild-URL
  - Bild-Alt
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: feste Hero-Variante mit Bleed-Bild oberhalb von Body und Brand-CTA beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_image_top_bleed_show_salutation` und `emb_hero_image_top_bleed_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_image_top_bleed_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_image_top_bleed_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_image_top_bleed_show_small_headline` und `emb_hero_image_top_bleed_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - Freie px-, CSS-, HTML- oder Inline-Style-Werte sind fuer diese Headline-Groesse nicht zulaessig.

### `hero-image-top-bleed-center`

- Snippet: `emb_hero_image_top_bleed_center`
- Ausrichtung: Eyebrow oder Badge, Headline, Anrede, Body und CTA sind zentriert.
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-image-top-bleed-center"`
- Sichtbare Felder:
  - Eyebrow
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
  - Bild-URL
  - Bild-Alt
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: feste zentrierte Hero-Variante mit Bleed-zentrierte Meta-, Headline-, Copy- und CTA-Ausrichtung mit Bild oberhalb von Body und Brand-CTA beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_image_top_bleed_center_show_salutation` und `emb_hero_image_top_bleed_center_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_image_top_bleed_center_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_image_top_bleed_center_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_image_top_bleed_center_show_small_headline` und `emb_hero_image_top_bleed_center_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - Freie px-, CSS-, HTML- oder Inline-Style-Werte sind fuer diese Headline-Groesse nicht zulaessig.

### `hero-image-head-copy-bleed-center`

- Snippet: `emb_hero_image_head_copy_bleed_center`
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-image-head-copy-bleed-center"`
- Sichtbare Felder:
  - Bild-URL
  - Bild-Alt
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
- Bildformat in der Preview: `16:9 | 1200 x 600 px`
- Fuellhinweis: feste Hero-Variante mit Bleed-Bild oben, zentrierter Headline, zentriertem Body und gefuelltem Brand-CTA beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_image_head_copy_bleed_center_show_salutation` und `emb_hero_image_head_copy_bleed_center_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_image_head_copy_bleed_center_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_image_head_copy_bleed_center_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_image_head_copy_bleed_center_show_small_headline` und `emb_hero_image_head_copy_bleed_center_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.

### `hero-image-textbox-cta-center`

- Snippet: `emb_hero_image_textbox_cta_center`
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-image-textbox-cta-center"`
- Sichtbare Felder:
  - Hintergrundfarbe
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Bild-URL
  - Bild-Alt
  - Anrede
  - Body
  - Kurzfrage
  - Link der Kontur-Flaeche
  - Feldtext in der Kontur-Flaeche
  - Button-Label
  - Button-URL
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: zentrierte Headline, Bild, zweistufiger Copy-Bereich, Kontur-Flaeche und gefuellter Brand-CTA bleiben in dieser Reihenfolge erhalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Verbindlicher Snippet-Call-Vertrag: genau 14 direkt gerenderte Parameter in dieser Reihenfolge
  - `emb_hero_image_textbox_cta_center_bg_color`
  - `emb_hero_image_textbox_cta_center_headline`
  - `emb_hero_image_textbox_cta_center_image_url`
  - `emb_hero_image_textbox_cta_center_image_alt`
  - `emb_hero_image_textbox_cta_center_show_salutation`
  - `emb_hero_image_textbox_cta_center_salutation`
  - `emb_hero_image_textbox_cta_center_body`
  - `emb_hero_image_textbox_cta_center_question`
  - `emb_hero_image_textbox_cta_center_entry_url`
  - `emb_hero_image_textbox_cta_center_entry_text`
  - `emb_hero_image_textbox_cta_center_button_url`
  - `emb_hero_image_textbox_cta_center_button_bg_color`
  - `emb_hero_image_textbox_cta_center_button_border_color`
  - `emb_hero_image_textbox_cta_center_button_label`
  - Die Hero-Anrede wird ueber `emb_hero_image_textbox_cta_center_show_salutation` und `emb_hero_image_textbox_cta_center_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_image_textbox_cta_center_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_image_textbox_cta_center_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_image_textbox_cta_center_show_small_headline` und `emb_hero_image_textbox_cta_center_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - `button_bg_color` und `button_border_color` duerfen aus den erlaubten Defaults der `export-map.json` kommen.

### `hero-fakeform-buttons-image`

- Snippet: `emb_hero_fakeform_buttons_image`
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-fakeform-buttons-image"`
- Sichtbare Felder:
  - Hintergrundfarbe
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Auswahlbutton 1 bis 6
  - Bild-URL
  - Bild-Alt
  - Anrede
  - Body
  - finales CTA-Label
  - finale CTA-URL
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: Hero-Modul mit zentrierter Headline, vertikal gestapelten Auswahlbuttons, Bild, Anrede, Richtext-Body und Brand-CTA; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Sichtbarkeitsregel:
  - Default sichtbar sind genau `5` Auswahlbuttons.
  - Das Modul unterstuetzt insgesamt `2` bis `6` Auswahlbuttons.
  - Button `1` bleibt immer sichtbar.
  - `show_item_2` bleibt fuer dieses Modul verpflichtend `true`, damit die Mindestanzahl `2` nicht unterschritten wird.
  - `show_item_3`, `show_item_4`, `show_item_5` und `show_item_6` erweitern oder reduzieren die sichtbaren spaeteren Buttons zustandsbasiert.
- Button-Regel:
  - Die Auswahlbuttons nutzen im ersten produktiven Stand das bestehende Pattern `button-outline-strong`.
  - Der finale CTA nutzt das bestehende Pattern `button-filled-brand`.
  - Freie neue Button-Styles, freie Farben, freie Formen oder freie CTA-Varianten sind unzulaessig.
- Technische Export-Regel:
  - Verbindlicher Snippet-Call-Vertrag: genau 31 direkt gerenderte Parameter in dieser Reihenfolge
  - `emb_hero_fakeform_buttons_image_bg_color`
  - `emb_hero_fakeform_buttons_image_show_small_headline`
  - `emb_hero_fakeform_buttons_image_show_large_headline`
  - `emb_hero_fakeform_buttons_image_headline`
  - `emb_hero_fakeform_buttons_image_choice_button_1_url`
  - `emb_hero_fakeform_buttons_image_choice_button_1_label`
  - `emb_hero_fakeform_buttons_image_show_item_2`
  - `emb_hero_fakeform_buttons_image_choice_button_2_url`
  - `emb_hero_fakeform_buttons_image_choice_button_2_label`
  - `emb_hero_fakeform_buttons_image_show_item_3`
  - `emb_hero_fakeform_buttons_image_choice_button_3_url`
  - `emb_hero_fakeform_buttons_image_choice_button_3_label`
  - `emb_hero_fakeform_buttons_image_show_item_4`
  - `emb_hero_fakeform_buttons_image_choice_button_4_url`
  - `emb_hero_fakeform_buttons_image_choice_button_4_label`
  - `emb_hero_fakeform_buttons_image_show_item_5`
  - `emb_hero_fakeform_buttons_image_choice_button_5_url`
  - `emb_hero_fakeform_buttons_image_choice_button_5_label`
  - `emb_hero_fakeform_buttons_image_show_item_6`
  - `emb_hero_fakeform_buttons_image_choice_button_6_url`
  - `emb_hero_fakeform_buttons_image_choice_button_6_label`
  - `emb_hero_fakeform_buttons_image_image_url`
  - `emb_hero_fakeform_buttons_image_image_alt`
  - `emb_hero_fakeform_buttons_image_show_salutation`
  - `emb_hero_fakeform_buttons_image_use_snippetcall_salutation`
  - `emb_hero_fakeform_buttons_image_salutation`
  - `emb_hero_fakeform_buttons_image_body`
  - `emb_hero_fakeform_buttons_image_button_url`
  - `emb_hero_fakeform_buttons_image_button_bg_color`
  - `emb_hero_fakeform_buttons_image_button_border_color`
  - `emb_hero_fakeform_buttons_image_button_label`
  - Die Hero-Anrede wird ueber `emb_hero_fakeform_buttons_image_show_salutation` und `emb_hero_fakeform_buttons_image_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_fakeform_buttons_image_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_fakeform_buttons_image_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_fakeform_buttons_image_show_small_headline` und `emb_hero_fakeform_buttons_image_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - `button_bg_color` und `button_border_color` des finalen CTA duerfen aus den erlaubten Defaults der `export-map.json` kommen.

### `hero-cta-top`

- Snippet: `emb_hero_cta_top`
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-cta-top"`
- Sichtbare Felder:
  - Eyebrow
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
  - Bild-URL
  - Bild-Alt
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: feste Hero-Variante mit Bild unterhalb von Body und Brand-CTA beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_cta_top_show_salutation` und `emb_hero_cta_top_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_cta_top_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_cta_top_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_cta_top_show_small_headline` und `emb_hero_cta_top_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - Freie px-, CSS-, HTML- oder Inline-Style-Werte sind fuer diese Headline-Groesse nicht zulaessig.

### `hero-cta-top-center`

- Snippet: `emb_hero_cta_top_center`
- Ausrichtung: Eyebrow oder Badge, Headline, Anrede, Body und CTA sind zentriert.
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-cta-top-center"`
- Sichtbare Felder:
  - Eyebrow
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
  - Bild-URL
  - Bild-Alt
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: feste zentrierte Hero-Variante mit zentrierte Meta-, Headline-, Copy- und CTA-Ausrichtung mit Bild unterhalb von Body und Brand-CTA beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_cta_top_center_show_salutation` und `emb_hero_cta_top_center_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_cta_top_center_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_cta_top_center_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_cta_top_center_show_small_headline` und `emb_hero_cta_top_center_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - Freie px-, CSS-, HTML- oder Inline-Style-Werte sind fuer diese Headline-Groesse nicht zulaessig.

### `hero-cta-top-no-bottom`

- Snippet: `emb_hero_cta_top_no_bottom`
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-cta-top-no-bottom"`
- Sichtbare Felder:
  - Eyebrow
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
  - Bild-URL
  - Bild-Alt
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: feste Hero-Variante ohne unteren Modulabschluss und mit Brand-CTA beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_cta_top_no_bottom_show_salutation` und `emb_hero_cta_top_no_bottom_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_cta_top_no_bottom_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_cta_top_no_bottom_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_cta_top_no_bottom_show_small_headline` und `emb_hero_cta_top_no_bottom_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - Freie px-, CSS-, HTML- oder Inline-Style-Werte sind fuer diese Headline-Groesse nicht zulaessig.

### `hero-cta-top-no-bottom-center`

- Snippet: `emb_hero_cta_top_no_bottom_center`
- Ausrichtung: Eyebrow oder Badge, Headline, Anrede, Body und CTA sind zentriert.
- Preview-Quelle: `preview-modules.html`, Block `data-module="hero-cta-top-no-bottom-center"`
- Sichtbare Felder:
  - Eyebrow
  - Headline
  - Headline-Groesse: `s`, `m` oder `l`
  - Anrede
  - Body
  - Button-Label
  - Button-URL
  - Bild-URL
  - Bild-Alt
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: feste zentrierte Hero-Variante ohne unteren Modulabschluss sowie mit zentrierter Meta-, Headline-, Copy- und CTA-Ausrichtung beibehalten; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Export-Regel:
  - Die Hero-Anrede wird ueber `emb_hero_cta_top_no_bottom_center_show_salutation` und `emb_hero_cta_top_no_bottom_center_salutation` als eigener Plain-Text-Block vor dem Body materialisiert.
  - `emb_hero_cta_top_no_bottom_center_use_snippetcall_salutation` ist ein rein technisches Export-Flag fuer freigegebene Produktkontexte und bleibt in der Preview unsichtbar.
  - Neue Default-States fuer dieses Modul muessen `show_salutation = true` und `salutation = Hallo Anrede,` materialisieren.
  - `emb_hero_cta_top_no_bottom_center_headline_size` ist das einzige kanonische Groessenfeld fuer diese Hero-Headline.
  - Erlaubte Werte sind nur `s`, `m` und `l`; Default ist `l`.
  - Das Groessen-Mapping folgt festen Typography-Tokens:
    - Desktop:
      - `s` => `heading-s` => `20px / 30px`
      - `m` => `heading-m` => `26px / 36px`
      - `l` => `heading-l` => `34px / 44px`
    - Mobile:
      - `s` => `heading-s mobile` => `20px / 30px`
      - `m` => `heading-m mobile` => `24px / 34px`
      - `l` => `heading-l mobile` => `28px / 36px`
  - Die Preview materialisiert zusaetzlich die technischen Bridge-Felder `emb_hero_cta_top_no_bottom_center_show_small_headline` und `emb_hero_cta_top_no_bottom_center_show_large_headline` im `email_state.content`.
  - Die Bridge ist fest:
    - `s` => `show_small_headline = true`, `show_large_headline = false`
    - `m` => `show_small_headline = false`, `show_large_headline = false`
    - `l` => `show_small_headline = false`, `show_large_headline = true`
  - Neue Default-States fuer dieses Modul muessen immer `headline_size = l`, `show_small_headline = false` und `show_large_headline = true` erzeugen.
  - Wenn `show_small_headline = true` und `show_large_headline = true` gleichzeitig vorliegen oder nicht exakt zur kanonischen `headline_size` passen, ist der State nicht export-ready.
  - Freie px-, CSS-, HTML- oder Inline-Style-Werte sind fuer diese Headline-Groesse nicht zulaessig.

### `teaser-1col`

- Snippet: `emb_teaser_1col`
- Preview-Quelle: `preview-modules.html`, Block `data-module="teaser-1col"`
- Sichtbare Felder:
  - Headline
  - Bild-URL
  - Bild-Alt
  - Body
  - Button-Label
  - Button-URL
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: Bild, Richtextbereich und CTA beibehalten

### `loft-snl-copy-cta`

- Snippet: `emb_loft_snl_copy_cta`
- Preview-Quelle: `preview-modules.html`, Block `data-module="loft-snl-copy-cta"`
- Sichtbare Felder:
  - feste Preview-Anrede
  - Body
  - Button-Label
  - Button-URL
- Fuellhinweis: team-spezifisches Loft/SNL-Modul mit freiem Richtext und gefuelltem Charcoal-CTA; die Preview-Anrede bleibt immer `Hallo Anrede,`
- Technische Regel: operativ renderbar fuer Loft/SNL-Kompositionen, aber kein allgemeines Core-Library-Modul.

### `loft-snl-copy-sections-cta`

- Snippet: `emb_loft_snl_copy_sections_cta`
- Preview-Quelle: `preview-modules.html`, Block `data-module="loft-snl-copy-sections-cta"`
- Sichtbare Felder:
  - Headline 1
  - Body 1
  - optionale Headline 2
  - optionaler Body 2
  - Button-Label
  - Button-URL
- Fuellhinweis: team-spezifisches Loft/SNL-Modul mit zwei Textsektionen und gefuelltem Charcoal-CTA; der zweite Abschnitt kann exportseitig ausgeblendet werden
- Technische Regel: operativ renderbar fuer Loft/SNL-Kompositionen, aber kein allgemeines Core-Library-Modul.

### `loft-rnl-dev-intro`

- Snippet: `emb_loft_rnl_dev_intro`
- Preview-Quelle: `preview-modules.html`, Block `data-module="loft-rnl-dev-intro"`
- Sichtbare Felder:
  - Headline
  - Preview-Anrede
  - Introtext
- Fuellhinweis: template-spezifischer fixer Introblock fuer Loft RNL (Dev) ohne CTA und ohne freie Background-Variation
- Technische Regel:
  - Die Hauptheadline dieses Moduls ist eine dokumentierte modulspezifische Ausnahme und nutzt fest `heading-l`.
  - Die finale EMB-Preview muss diese Headline im Markup explizit als `font-heading-large-bold` materialisieren; ein reiner Loft-Sonderselector ohne `heading-l`-Klasse ist nicht ausreichend.
  - `emb_loft_rnl_dev_intro_headline` ist ein normales Textfeld und kein `rich_full`.
  - `emb_loft_rnl_dev_intro_salutation` ist in der Preview ein menschenlesbares Textfeld und kein freier Raw-Logic-Slot.
  - `emb_loft_rnl_dev_intro_body` ist ein `rich_full`-Kontext hinter der sichtbaren Preview-Anrede.
  - Fuer `salutationContext = loft-rnl-dev` materialisiert der Export den produktiven Wert von `emb_loft_rnl_dev_intro_salutation` kontrolliert aus `agent/product-salutations.json`.

### `loft-rnl-dev-teaser-1col`

- Snippet: `emb_loft_rnl_dev_teaser_1col`
- Preview-Quelle: `preview-modules.html`, Block `data-module="loft-rnl-dev-teaser-1col"`
- Sichtbare Felder:
  - Badge-Label
  - Headline
  - Bild-URL
  - Bild-Alt
  - Body
  - Details
  - Button-Label
  - Button-URL
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: template-spezifisches Loft-RNL-Dev-Projektmodul mit wiederholbarer Einspalten-Struktur fuer Neubauprojekte
- Technische Regel:
  - Die Hauptheadline dieses Moduls ist eine dokumentierte modulspezifische Ausnahme und nutzt fest `heading-l`.
  - Die finale EMB-Preview muss diese Headline im Markup explizit als `font-heading-large-bold` materialisieren; groessere Hero- oder XL-Klassen sind fuer dieses Modul unzulaessig.
  - `emb_loft_rnl_dev_teaser_1col_body` und `emb_loft_rnl_dev_teaser_1col_details` sind `rich_full`-Kontexte und muessen Richtext fuer Absaetze, Listen, Hervorhebungen und Links transportieren.
  - Die Modulhintergruende folgen nicht einem User-Feld, sondern dem globalen Hintergrund-Rhythmus.
  - Die Badge-Flaeche ist immer invers zur finalen Modul-Flaeche und wird technisch aus dem konkreten `*_bg_color` abgeleitet.
  - Die finale EMB-Preview muss diese Inversion im Markup explizit ueber `module__badge--surface-white` oder `module__badge--surface-gray` materialisieren; eine reine Ableitung ueber statische `theme-*`-Wrapper ist nicht ausreichend.

### `loft-regio-resi-intro`

- Snippet: `emb_loft_regio_resi_intro`
- Preview-Quelle: `preview-modules.html`, Block `data-module="loft-regio-resi-intro"`
- Sichtbare Felder:
  - Headline
  - Preview-Anrede
  - Introtext
- Fuellhinweis: template-spezifischer fixer Introblock fuer Loft | Regio (Resi) ohne CTA und ohne freie Background-Variation
- Technische Regel:
  - Die Hauptheadline dieses Moduls ist eine dokumentierte modulspezifische Ausnahme und nutzt fest `heading-l`.
  - Die finale EMB-Preview muss diese Headline im Markup explizit als `font-heading-large-bold` materialisieren; ein reiner Loft-Sonderselector ohne `heading-l`-Klasse ist nicht ausreichend.
  - `emb_loft_regio_resi_intro_headline` ist ein normales Textfeld und kein `rich_full`.
  - `emb_loft_regio_resi_intro_salutation` ist in der Preview ein menschenlesbares Textfeld und kein freier Raw-Logic-Slot.
  - `emb_loft_regio_resi_intro_body` ist ein `rich_full`-Kontext hinter der sichtbaren Preview-Anrede.
  - Fuer `salutationContext = loft-regio-resi` materialisiert der Export den produktiven Wert von `emb_loft_regio_resi_intro_salutation` kontrolliert aus `agent/product-salutations.json`.

### `loft-regio-resi-teaser-1col`

- Snippet: `emb_loft_regio_resi_teaser_1col`
- Preview-Quelle: `preview-modules.html`, Block `data-module="loft-regio-resi-teaser-1col"`
- Sichtbare Felder:
  - Headline
  - Body
  - Bild-URL
  - Bild-Alt
  - Kennzahl 1 Label
  - Kennzahl 1 Wert
  - Kennzahl 2 Label
  - Kennzahl 2 Wert
  - Kennzahl 3 Label
  - Kennzahl 3 Wert
  - Button-Label
  - Button-URL
- Bildformat in der Preview: `16:9 | 960 x 540 px`
- Fuellhinweis: template-spezifisches Loft-Regio-Residential-Projektmodul mit wiederholbarer Einspalten-Struktur fuer Objekt-Highlights
- Technische Regel:
  - Die Hauptheadline dieses Moduls ist eine dokumentierte modulspezifische Ausnahme und nutzt fest `heading-l`.
  - Die finale EMB-Preview muss diese Headline im Markup explizit als `font-heading-large-bold` materialisieren; groessere Hero- oder XL-Klassen sind fuer dieses Modul unzulaessig.
  - `emb_loft_regio_resi_teaser_1col_body` ist ein `rich_full`-Kontext und muss Richtext fuer Absaetze, Listen, Hervorhebungen und Links transportieren.
  - Die Modulhintergruende folgen nicht einem User-Feld, sondern dem globalen Hintergrund-Rhythmus.
  - Die drei Desktop-Kennzahlen und die mobile Bullet-Liste muessen dieselben Felder `metric_1..3_label` und `metric_1..3_value` nutzen; die mobile Liste zeigt das Label normal und den Wert fett.
  - Die mobile Liste ist nur Darstellung und darf keine zweite fachliche Pflege eigener Inhalte einfuehren.

### `teaser-2col-vertical`

- Snippet: `emb_teaser_2col_vertical`
- Preview-Quelle: `preview-modules.html`, Block `data-module="teaser-2col-vertical"`
- Sichtbare Felder:
  - Headline
  - linke Spalte: Bild-URL, Bild-Alt, Body, Link-Label, Link-URL
  - rechte Spalte: Bild-URL, Bild-Alt, Body, Link-Label, Link-URL
- Bildformat in der Preview: `16:9 | 960 x 540 px` pro Spalte
- Fuellhinweis: feste Zweispalten-Struktur mit gemeinsamer Headline beibehalten

### `teaser-2col-horizontal`

- Snippet: `emb_teaser_2col_horizontal`
- Preview-Quelle: `preview-modules.html`, Block `data-module="teaser-2col-horizontal"`
- Sichtbare Felder:
  - Headline
  - bis zu vier Items mit je Bild-URL, Bild-Alt, Body, Link-Label und Link-URL
- Bildformat in der Preview: `16:9 | 960 x 540 px` pro Item
- Fuellhinweis: die hinterlegte Vier-Item-Struktur beibehalten

### `teaser-2col-alternating`

- Snippet: `emb_teaser_2col_alternating`
- Preview-Quelle: `preview-modules.html`, Block `data-module="teaser-2col-alternating"`
- Sichtbare Felder:
  - Headline
  - erste Zeile: Bild-URL, Bild-Alt, Body, Link-Label, Link-URL
  - zweite Zeile: Bild-URL, Bild-Alt, Body, Link-Label, Link-URL
- Bildformat in der Preview: `4:3 | 800 x 600 px` pro Zeile
- Fuellhinweis: die feste zweizeilige Alternating-Struktur beibehalten

### `teaser-2col-listing`

- Snippet: `emb_teaser_2col_listing`
- Preview-Quelle: `preview-modules.html`, Block `data-module="teaser-2col-listing"`
- Sichtbare Felder:
  - Headline
  - bis zu vier Items mit je Bild-URL, Bild-Alt, Body, Link-Label und Link-URL
  - optionaler Abschluss-CTA mit Button-Label und Button-URL
- Bildformat in der Preview: `4:3 | 800 x 600 px` pro Item
- Fuellhinweis: die hinterlegte Listing-Struktur mit `listing-rows`, `listing-row`, `media--listing` und `listing-row__copy` unveraendert beibehalten; den Abschluss-CTA nur bei Bedarf einblenden und sonst verborgen lassen

### `teaser-2col-gallery`

- Snippet: `emb_teaser_2col_gallery`
- Preview-Quelle: `preview-modules.html`, Block `data-module="teaser-2col-gallery"`
- Sichtbare Felder:
  - Headline
  - zwei bis vier Bild-URLs
  - zwei bis vier Bild-Alt-Texte
  - optionales Mobile-Flag fuer die untere Bildreihe
- Bildformat in der Preview: `16:9 | 960 x 540 px` pro Bild
- Fuellhinweis: obere Reihe immer mit zwei Bildern befuellen; die untere Reihe nur ueber `show_item_3` und `show_item_4` erweitern

### `benefits-3col`

- Snippet: `emb_benefits_3col`
- Preview-Quelle: `preview-modules.html`, Block `data-module="benefits-3col"`
- Sichtbare Felder:
  - Headline
  - drei Benefit-Texte
  - drei Icon-URLs
  - Button-Label
  - Button-URL
- Fuellhinweis: Dreierkarten-Struktur mit einem CTA darunter beibehalten; Icons nie leer lassen

### `servicetiles`

- Snippet: `emb_servicetiles`
- Preview-Quelle: `preview-modules.html`, Block `data-module="servicetiles"`
- Sichtbare Felder:
  - Headline
  - vier Card-Icon-URLs
  - vier Card-Titel
  - vier Card-Descriptions
  - vier Card-URLs
- Fuellhinweis: feste Viererkarten-Struktur mit `2 x 2` auf Desktop und `1` Spalte auf Mobile beibehalten
- Technische Regel:
  - Vor dem Preview-Render muessen fachlich genannte Services zuerst eindeutig ueber `agent/service-products.json` aufgeloest werden.
  - Wenn nicht genau `4` Services eindeutig aufloesbar sind, darf das Modul nicht stillschweigend gerendert werden.
  - Der finale Preview-/State-Vertrag materialisiert nur `emb_servicetiles_headline` sowie die vier konkreten Card-Feldsets `emb_servicetiles_col_1..4_(icon_url|title|description|url)`.

### `steps-3col`

- Snippet: `emb_steps_3col`
- Preview-Quelle: `preview-modules.html`, Block `data-module="steps-3col"`
- Sichtbare Felder:
  - Headline
  - drei Schritt-Texte
  - Button-Label
  - Button-URL
- Fuellhinweis: feste Drei-Schritte-Struktur mit CTA beibehalten
- Technische Regel: Das Modul wird genau einmal exportiert. Desktop- und Mobile-Markup im echten Snippet sind reine Renderdetails und kein Export-Signal.

### `steps-horizontal`

- Snippet: `emb_steps_horizontal`
- Preview-Quelle: `preview-modules.html`, Block `data-module="steps-horizontal"`
- Sichtbare Felder:
  - Headline
  - drei Schritt-Texte
  - Button-Label
  - Button-URL
- Fuellhinweis: feste vertikale Step-Line mit drei Schritten und CTA beibehalten

### `table`

- Snippet: `emb_table`
- Preview-Quelle: `preview-modules.html`, Block `data-module="table"`
- Sichtbare Felder:
  - Headline
  - drei Spalten-Headlines
  - drei Tabellenzeilen mit je drei Zellen
  - Button-Label
  - Button-URL
- Fuellhinweis: feste Dreispalten-Tabelle mit drei Datenzeilen und CTA beibehalten

### `table-comparison`

- Snippet: `emb_table_comparison`
- Preview-Quelle: `preview-modules.html`, Block `data-module="table-comparison"`
- Sichtbare Felder:
  - Headline
  - linke Vergleichsspalte: Spalten-Headline und drei Textzeilen
  - rechte Vergleichsspalte: Spalten-Headline und drei Textzeilen
  - Button-Label
  - Button-URL
- Fuellhinweis: feste Zweispalten-Vergleichsstruktur mit je drei Punkten und CTA beibehalten

### `contact`

- Snippet: `emb_contact`
- Preview-Quelle: `preview-modules.html`, Block `data-module="contact"`
- Das Modul bleibt immer auf weissem Hintergrund und nimmt nicht an der Hintergrund-Alternierung teil.
- Sichtbare Felder:
  - Bild-URL
  - Bild-Alt
  - Headline
  - Intro-Text
  - Telefonnummer
  - Telefonzeiten
  - E-Mail-Intro
  - E-Mail-URL
  - E-Mail-Adresse
  - Abschlusszeile 1
  - Abschlusszeile 2
- Fuellhinweis: feste Kontaktstruktur mit bestehender Avatar-Position, Intro, Telefon, E-Mail und Abschluss beibehalten
- Bei aktivem Produktkontext `RLE` muessen ohne explizite User-Overrides die dokumentierten RLE-Defaults in genau diese bestehenden Contact-Felder materialisiert werden.
- Wenn fuer den registrierten Avatar-Slot keine echte Bild-URL vorliegt, bleibt in der Preview der graue Placeholder sichtbar.

### `contact-signoff`

- Snippet: `emb_contact_signoff`
- Preview-Quelle: `preview-modules.html`, Block `data-module="contact-signoff"`
- Das Modul bleibt immer auf weissem Hintergrund und nimmt nicht an der Hintergrund-Alternierung teil.
- Sichtbare Felder:
  - Abschluss
- Fuellhinweis: feste zweizeilige Abschlussformel ohne Bild, Telefonnummer, E-Mail-Adresse oder CTA unveraendert beibehalten
- Technische Regel: statisches Export-Snippet ohne Parameter.

### `footer`

- Snippet: `emb_footer_marketing`
- Preview-Quelle: `preview-modules.html`, Block `data-module="footer"`
- Sichtbare Felder:
  - Footer
- Fuellhinweis: unveraendert und vollstaendig verwenden; nie vereinfachen, kuerzen oder teilweise auslassen
```

## email-builder/agent/preview-template.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>E-Mail Vorschau</title>
  <!-- PREVIEW TEMPLATE RULE: Keep this file as the exact shell source for every preview. -->
  <!-- PREVIEW TEMPLATE RULE: Keep this stylesheet reference unchanged in the copied preview output. -->
  <link rel="stylesheet" href="https://s24-creative-ops.github.io/email-builder/preview-styles.css" />
</head>
<body>
  <div class="preview-shell">
    <main class="preview-canvas">
      <section class="module preview-subject" data-preview-slot="subject">
        <div class="module__inner">
          <!-- PREVIEW TEMPLATE RULE: Only the text inside [data-preview-subject-text] and [data-preview-preheader-text] may be replaced. -->
          <div class="preview-subject__stack">
            <p class="preview-subject__line preview-subject__line--subject">Subject: <span data-preview-subject-text>Hier steht der Vorschlag für Subject</span></p>
            <p class="preview-subject__line preview-subject__line--preheader">Preheader: <span data-preview-preheader-text>Hier steht der Vorschlag für Preheader</span></p>
          </div>
        </div>
      </section>
      <!-- PREVIEW TEMPLATE RULE: Insert module blocks only between the two module slot markers below. -->
      <!-- MODULE SLOT: Insert the selected module blocks from preview-modules.html here. -->
      <!-- Keep the active module composition in builder logic, not hardcoded in this shell. -->
    </main>
  </div>
</body>
</html>
```

## email-builder/agent/template-loft-regio-resi.definition.json

Dateityp: json

```json
{
  "template_id": "loft-regio-resi",
  "template_name": "Loft | Regio (Resi)",
  "version": 1,
  "status": "active",
  "preview_file": "template-loft-regio-resi.preview.html",
  "iterable_template_id": 619002,
  "salutation_context_id": "loft-regio-resi",
  "rules": {
    "order_locked": true,
    "forbid_new_modules": true,
    "allow_remove_modules": true,
    "allow_duplicate_modules": true
  },
  "slots": [
    {
      "slot_id": "logo-1",
      "module_id": "logo",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "intro-1",
      "module_id": "loft-regio-resi-intro",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "teaser-1",
      "module_id": "loft-regio-resi-teaser-1col",
      "locked": false,
      "removable": true,
      "repeatable": true
    },
    {
      "slot_id": "footer-1",
      "module_id": "footer",
      "locked": true,
      "removable": false,
      "repeatable": false
    }
  ]
}
```

## email-builder/agent/template-loft-regio-resi.preview.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>E-Mail Vorschau | Loft | Regio (Resi)</title>
  <link rel="stylesheet" href="https://s24-creative-ops.github.io/email-builder/preview-styles.css" />
</head>
<body>
  <div class="preview-shell">
    <main class="preview-canvas">
      <section class="module preview-subject" data-preview-slot="subject">
        <div class="module__inner">
          <div class="preview-subject__stack">
            <p class="preview-subject__line preview-subject__line--subject">Subject: <span data-preview-subject-text>Loft | Regio (Resi): Ausgewählte Wohnimmobilien aus Ihrer Region</span></p>
            <p class="preview-subject__line preview-subject__line--preheader">Preheader: <span data-preview-preheader-text>Ausgewaehlte Wohnimmobilien aus Ihrer Region mit kompaktem Intro und wiederholbarem Residential-Teaser.</span></p>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="logo" data-snippet="emb_logo">
        <div class="module__inner module__inner--logo">
          <a class="module__logo-link" href="https://www.immobilienscout24.de/" title="ImmoScout24">
            <img
              class="module__logo-image"
              src="https://www.static-immobilienscout24.de/fro/ite/_/IS24-Logo_horizontal_left_white.png"
              alt="Logo ImmoScout24"
              width="185"
              height="47"
            />
          </a>
        </div>
      </section>

      <section class="module theme-white" data-module="loft-regio-resi-intro" data-snippet="emb_loft_regio_resi_intro">
        <div class="module__inner">
          <div class="teaser-single">
            <div class="intro-richtext">
              <h2 class="module__title font-heading-large-bold loft-regio-resi-intro__headline" data-export-field="emb_loft_regio_resi_intro_headline" data-export-role="headline">Ausgewählte Wohnimmobilien aus Ihrer Region</h2>
              <p class="module__body" data-export-field="emb_loft_regio_resi_intro_salutation" data-export-role="salutation">Hallo Anrede</p>
              <div class="module__teaser-richtext" data-export-field="emb_loft_regio_resi_intro_body" data-export-role="richtext">
                <p class="module__body" data-export-role="body-paragraph" data-export-index="1">hier finden Sie ausgewaehlte Wohnimmobilien aus Ihrer Region. Das Intro fuehrt bewusst kompakt in die folgenden Objekt-Highlights ein und laesst dem wiederholbaren Residential-Teaser den inhaltlichen Schwerpunkt.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-gray" data-module="loft-regio-resi-teaser-1col" data-snippet="emb_loft_regio_resi_teaser_1col">
        <div class="module__inner">
          <div class="teaser-single">
            <div class="module__head">
              <h2 class="module__title font-heading-large-bold loft-regio-resi-teaser-1col__headline" data-export-field="emb_loft_regio_resi_teaser_1col_headline" data-export-role="headline">Historischer Charme trifft modernen Wohnkomfort</h2>
            </div>
            <div class="module__teaser-richtext" data-export-field="emb_loft_regio_resi_teaser_1col_body" data-export-role="richtext">
              <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Das sanierte Einfamilienhaus in Naunhof bei Leipzig aus dem Jahr 1900 bietet eine luxurioese Ausstattung mit Fussbodenheizung, Keller und Einliegerwohnung. Die ruhige Lage im idyllischen Ortsteil Lindhardt ermoeglicht naturnahes Wohnen nahe mehrerer Seen und vielfaeltiger Freizeitmoeglichkeiten.</p>
              <p class="module__body" data-export-role="body-paragraph" data-export-index="2">Besondere Merkmale sind der Pool, Jacuzzi sowie die hochwertige Aussenanlage mit moderner Technik und dreifach verglasten Fenstern.</p>
            </div>
            <div class="media media--hero">
              <div
                class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                data-image-field="emb_loft_regio_resi_teaser_1col_image_url"
                data-image-alt-field="emb_loft_regio_resi_teaser_1col_image_alt"
              >
                <div class="preview-image-placeholder__text">
                  <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                </div>
              </div>
            </div>
            <div class="loft-regio-resi-teaser-1col__stats mobile_hide">
              <div class="loft-regio-resi-teaser-1col__stat">
                <p class="loft-regio-resi-teaser-1col__stat-value" data-export-field="emb_loft_regio_resi_teaser_1col_metric_1_value" data-export-role="metric-value" data-export-index="1">1.250.000 €</p>
                <p class="loft-regio-resi-teaser-1col__stat-label" data-export-field="emb_loft_regio_resi_teaser_1col_metric_1_label" data-export-role="metric-label" data-export-index="1">Kaufpreis</p>
              </div>
              <div class="loft-regio-resi-teaser-1col__stat">
                <p class="loft-regio-resi-teaser-1col__stat-value" data-export-field="emb_loft_regio_resi_teaser_1col_metric_2_value" data-export-role="metric-value" data-export-index="2">357,2 m²</p>
                <p class="loft-regio-resi-teaser-1col__stat-label" data-export-field="emb_loft_regio_resi_teaser_1col_metric_2_label" data-export-role="metric-label" data-export-index="2">Wohnfläche ca.</p>
              </div>
              <div class="loft-regio-resi-teaser-1col__stat">
                <p class="loft-regio-resi-teaser-1col__stat-value" data-export-field="emb_loft_regio_resi_teaser_1col_metric_3_value" data-export-role="metric-value" data-export-index="3">7</p>
                <p class="loft-regio-resi-teaser-1col__stat-label" data-export-field="emb_loft_regio_resi_teaser_1col_metric_3_label" data-export-role="metric-label" data-export-index="3">Zimmeranzahl</p>
              </div>
            </div>
            <ul class="module__list--teaser loft-regio-resi-teaser-1col__stats-list">
              <li><span data-export-field="emb_loft_regio_resi_teaser_1col_metric_1_label" data-export-role="metric-label" data-export-index="1">Kaufpreis</span>: <strong data-export-field="emb_loft_regio_resi_teaser_1col_metric_1_value" data-export-role="metric-value" data-export-index="1">1.250.000 €</strong></li>
              <li><span data-export-field="emb_loft_regio_resi_teaser_1col_metric_2_label" data-export-role="metric-label" data-export-index="2">Wohnfläche ca.</span>: <strong data-export-field="emb_loft_regio_resi_teaser_1col_metric_2_value" data-export-role="metric-value" data-export-index="2">357,2 m²</strong></li>
              <li><span data-export-field="emb_loft_regio_resi_teaser_1col_metric_3_label" data-export-role="metric-label" data-export-index="3">Zimmeranzahl</span>: <strong data-export-field="emb_loft_regio_resi_teaser_1col_metric_3_value" data-export-role="metric-value" data-export-index="3">7</strong></li>
            </ul>
            <div class="module__cta-row module__cta-row--compact">
              <a class="button-filled-default" href="https://www.immobilienscout24.de/expose/152345678" target="_blank" rel="noreferrer" data-export-field="emb_loft_regio_resi_teaser_1col_button_label" data-export-url-field="emb_loft_regio_resi_teaser_1col_button_url" data-export-role="cta">Exposé anfordern</a>
            </div>
          </div>
        </div>
      </section>

      <footer class="module theme-white" data-module="footer" data-snippet="emb_footer_marketing">
        <div class="module__inner module__inner--compact">
          <div class="footer-marketing">
            <p class="footer-marketing__headline">Kostenlose App herunterladen</p>
            <div class="footer-marketing__badges">
              <a class="footer-badge" href="https://itunes.apple.com/de/app/immobilienscout24/id342157367?mt=8" target="_blank" rel="noreferrer" data-token-attr-href="links.app_store">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/i36/uhu/m14/d1284a48-db27-4f3b-a434-ab9a625d0dd4.png"
                  data-token-attr-src="assets.app_store_badge"
                  alt="Download on the App Store"
                  width="115"
                  height="37"
                />
              </a>
              <a class="footer-badge" href="https://play.google.com/store/apps/details?id=de.is24.android&amp;hl=de" target="_blank" rel="noreferrer" data-token-attr-href="links.google_play">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/nrd/s3d/49k/b78e3fcd-6303-429c-a29d-691d73c0d01d.png"
                  data-token-attr-src="assets.google_play_badge"
                  alt="Get it on Google Play"
                  width="130"
                  height="37"
                />
              </a>
            </div>
            <div class="footer-marketing__copy">
              <p class="footer-marketing__text">ImmoScout24 informiert ueber Aktuelles aus der Immobilienwelt. Wenn kein Interesse mehr besteht, ist es moeglich, sich <a href="#" target="_blank" rel="noreferrer">hier abzumelden</a>. Die Abmeldung betrifft nicht gegebenenfalls bestehende Suchauftragsbenachrichtigungen.</p>
              <p class="footer-marketing__text">Immobilien Scout GmbH - Ein Unternehmen der Scout24-Gruppe, Invalidenstr. 65, 10557 Berlin · <a class="footer-marketing__plain-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.website" data-token-text="links.website_label">immobilienscout24.de</a> · Geschaeftsfuehrung: Dr. Gesa Crockford, Daniel Hendel · Vorsitzender des Aufsichtsrats: Ralf Weitz · Handelsregister: Amtsgericht Charlottenburg, HRB 69108 · Sitz der Gesellschaft: Berlin · USt-IdNr. DE200269419</p>
              <p class="footer-marketing__links">
                <a href="https://www.immobilienscout24.de/agb/datenschutz.html" target="_blank" rel="noreferrer" data-token-attr-href="links.privacy">Datenschutz</a><span class="footer-marketing__links-separator">|</span><a href="https://www.immobilienscout24.de/impressum.html" target="_blank" rel="noreferrer" data-token-attr-href="links.imprint">Impressum</a>
              </p>
              <p class="footer-marketing__text">&copy; 1999 - 2026 Immobilien Scout GmbH</p>
            </div>
          </div>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
```

## email-builder/email/templates/loft-regio-resi.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <title>E-Mail Builder | Loft | Regio (Resi)</title>
  <!--[if mso]>
  <xml>
    <w:WordDocument xmlns:w="urn:schemas-microsoft-com:office:word"><w:DontUseAdvancedTypographyReadingMail/></w:WordDocument>
    <o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings>
  </xml>
  <![endif]-->
  <link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/make-it-better/1.0.0/makeitbetter.css">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; padding: 0; }
    a[x-apple-data-detectors] { color: inherit !important; text-decoration: inherit !important; }
    #MessageViewBody a { color: inherit; text-decoration: none; }
    p { line-height: inherit; }
    .desktop_hide, .desktop_hide table { mso-hide: all; display: none; max-height: 0; overflow: hidden; }
    .module-rich-full-body--hero {
      display: grid;
      gap: 0;
    }
    .module-rich-full-body--hero p,
    .module-rich-full-body--hero ul,
    .module-rich-full-body--hero ol {
      margin: 0;
    }
    .module-rich-full-body--hero p + p {
      margin-top: 16px;
    }
    .module-rich-full-body--hero p + ul,
    .module-rich-full-body--hero p + ol,
    .module-rich-full-body--hero ul + p,
    .module-rich-full-body--hero ul + ul,
    .module-rich-full-body--hero ul + ol,
    .module-rich-full-body--hero ol + p,
    .module-rich-full-body--hero ol + ul,
    .module-rich-full-body--hero ol + ol {
      margin-top: 8px;
    }
    .module-rich-full-body--hero ul,
    .module-rich-full-body--hero ol {
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--hero li {
      margin: 0 0 4px;
    }
    .module-rich-full-body--hero li:last-child {
      margin-bottom: 0;
    }
    .module-rich-full-body--teaser-1col p {
      margin: 0;
    }
    .module-rich-full-body--teaser-1col ul,
    .module-rich-full-body--teaser-1col ol {
      margin: 0;
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--teaser-1col p + ul,
    .module-rich-full-body--teaser-1col p + ol,
    .module-rich-full-body--teaser-1col ul + p,
    .module-rich-full-body--teaser-1col ul + ul,
    .module-rich-full-body--teaser-1col ul + ol,
    .module-rich-full-body--teaser-1col ol + p,
    .module-rich-full-body--teaser-1col ol + ul,
    .module-rich-full-body--teaser-1col ol + ol {
      margin-top: 8px;
    }
    .module-rich-full-body--teaser-1col p + p {
      margin-top: 16px;
    }
    .module-rich-full-body--teaser-1col li {
      margin: 0 0 4px;
    }
    .module-rich-full-body--teaser-1col li:last-child {
      margin-bottom: 0;
    }
    @media (max-width:620px) {
      .row-content { width: 100% !important; }
      .stack .column { width: 100% !important; display: block !important; }
      .desktop_hide, .desktop_hide table { display: table !important; max-height: none !important; }
      .mobile_hide { display: none !important; min-height: 0; max-height: 0; max-width: 0; overflow: hidden; font-size: 0; }
      .font-heading-large-bold { font-size: 28px !important; line-height: 36px !important; }
      .font-heading-medium-regular,
      .font-heading-medium-bold { font-size: 24px !important; line-height: 34px !important; }
      .font-heading-small-regular,
      .font-heading-small-bold { font-size: 20px !important; line-height: 30px !important; }
      .module-12-heading h1 { font-size: 28px !important; line-height: 36px !important; }
      .module-logo-pad { padding: 24px 20px 0 !important; }
      .module-footer-pad { padding: 60px 20px 60px !important; }
      .module-table-pad { padding: 40px 20px !important; }
      .module-block[data-module="loft-regio-resi-teaser-1col"] .module-12-head-pad { padding: 40px 20px 0 !important; }
      .module-block[data-module="loft-regio-resi-teaser-1col"] .module-teaser-1col-body-pad-spaced { padding: 20px 20px 40px !important; }
    }
  </style>
</head>
<body style="background-color:#FFFFFF;margin:0;padding:0;-webkit-text-size-adjust:none;text-size-adjust:none;">
  <table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;background-color:#FFFFFF;">
    <tbody>
      <tr>
        <td>

          <!-- EMB CONTENT INSERTION POINT: Export inserts the generated module HTML or snippet calls here. -->
          <!-- This Iterable basis template must remain a shell without fixed modules. -->

        </td>
      </tr>
    </tbody>
  </table>
</body>
</html>
```

## email-builder/agent/starter-ho-esg.preview.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>E-Mail Vorschau | Homeowner | ESG</title>
  <link rel="stylesheet" href="https://s24-creative-ops.github.io/email-builder/preview-styles.css" />
</head>
<body>
  <div class="preview-shell">
    <main class="preview-canvas">
      <section class="module preview-subject" data-preview-slot="subject">
        <div class="module__inner">
          <div class="preview-subject__stack">
            <p class="preview-subject__line preview-subject__line--subject">Subject: <span data-preview-subject-text>Ihre Vorlage für Energie- und Immobilienservices</span></p>
            <p class="preview-subject__line preview-subject__line--preheader">Preheader: <span data-preview-preheader-text>Eine kurze Beispielmail mit passenden Services rund um Ihre Immobilie.</span></p>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="logo-centered" data-snippet="emb_logo_centered">
        <div class="module__inner module__inner--logo module__inner--logo-centered">
          <a class="module__logo-link" href="https://www.immobilienscout24.de/" title="ImmoScout24" style="display:inline-block;">
            <img
              class="module__logo-image"
              src="https://www.static-immobilienscout24.de/fro/ite/_/IS24-Logo_horizontal_center_white.png"
              alt="Logo ImmoScout24"
              width="198"
              height="47"
              style="display:block;padding:0;text-align:center;background:rgba(255,255,255,0);"
            />
          </a>
        </div>
      </section>

      <section class="module theme-white" data-module="hero-image-top-center" data-snippet="emb_hero_image_top_center">
        <div class="module__inner">
          <div class="module__hero-area module__hero-area--head">
            <div class="module__head module__head--center">
              <div class="module__hero-meta">
                <p class="module__eyebrow" data-export-field="emb_hero_image_top_center_preheadline" data-export-role="preheadline">Homeowner Services</p>
                <span class="module__badge is-hidden" data-export-field="emb_hero_image_top_center_badge_label" data-export-role="badge">Badge</span>
              </div>
              <span class="is-hidden" data-export-field="emb_hero_image_top_center_show_small_headline" data-export-role="technical-flag">false</span>
              <span class="is-hidden" data-export-field="emb_hero_image_top_center_show_large_headline" data-export-role="technical-flag">true</span>
              <span class="is-hidden" data-export-field="emb_hero_image_top_center_show_salutation" data-export-role="technical-flag">true</span>
              <span class="is-hidden" data-export-field="emb_hero_image_top_center_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
              <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_image_top_center_headline" data-export-role="headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large">Hilfreiche Services rund um Ihre Immobilie</h2>
            </div>
            <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
          </div>
          <div class="module__hero-flow">
            <div class="module__hero-area module__hero-area--image">
              <div class="media media--hero">
                <div
                  class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                  data-image-field="emb_hero_image_top_center_image_url"
                  data-image-alt-field="emb_hero_image_top_center_image_alt"
                >
                  <div class="preview-image-placeholder__text">
                    <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
                  </div>
                </div>
              </div>
              <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
            </div>
            <div class="module__hero-area module__hero-area--copy">
              <div class="module__copy module__copy--center">
                <p class="module__body" data-export-field="emb_hero_image_top_center_salutation" data-export-role="salutation">Hallo Anrede,</p>
                <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
                <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_image_top_center_body" data-export-role="richtext">
                  <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Diese Vorlage zeigt eine mögliche Struktur für Ihre E-Mail.</p>
                </div>
                <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
                <div class="module__cta-row module__cta-row--center">
                  <a class="button-filled-brand" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_image_top_center_button_label" data-export-url-field="emb_hero_image_top_center_button_url" data-export-role="cta">Mehr erfahren</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-gray" data-module="benefits-3col" data-snippet="emb_benefits_3col">
        <div class="module__inner">
          <div class="stack">
            <div class="module__head">
              <h2 class="module__title module__title--medium" data-export-field="emb_benefits_3col_headline" data-export-role="headline">Ihre Vorteile auf einen Blick</h2>
            </div>
            <div class="benefits-columns">
              <article class="benefit-item" data-export-item="benefit-card" data-export-index="1">
                <img
                  class="benefit-item__icon"
                  src="https://www.static-immobilienscout24.de/fro/emb/_/s24_lightbulb_48.png"
                  alt=""
                  width="48"
                  height="48"
                  data-icon-field="emb_benefits_3col_col_1_icon_url"
                />
                <p class="module__body" data-export-field="emb_benefits_3col_col_1_body" data-export-role="item-body"><strong>Orientierung gewinnen</strong><br />Erhalten Sie einen schnellen Überblick über passende Services.</p>
              </article>
              <article class="benefit-item" data-export-item="benefit-card" data-export-index="2">
                <img
                  class="benefit-item__icon"
                  src="https://www.static-immobilienscout24.de/fro/emb/_/s24_calendar_checkmark_48.png"
                  alt=""
                  width="48"
                  height="48"
                  data-icon-field="emb_benefits_3col_col_2_icon_url"
                />
                <p class="module__body" data-export-field="emb_benefits_3col_col_2_body" data-export-role="item-body"><strong>Nächste Schritte planen</strong><br />Nutzen Sie die Vorlage als klaren Startpunkt für Ihre Mail.</p>
              </article>
              <article class="benefit-item" data-export-item="benefit-card" data-export-index="3">
                <img
                  class="benefit-item__icon"
                  src="https://www.static-immobilienscout24.de/fro/emb/_/s24_checkmark_circle_48.png"
                  alt=""
                  width="48"
                  height="48"
                  data-icon-field="emb_benefits_3col_col_3_icon_url"
                />
                <p class="module__body" data-export-field="emb_benefits_3col_col_3_body" data-export-role="item-body"><strong>Services direkt anbieten</strong><br />Binden Sie relevante Angebote einfach in die Kommunikation ein.</p>
              </article>
            </div>
            <div class="module__cta-row">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/meinsuchprofil/meinsuchprofilanlage/" target="_blank" rel="noreferrer" data-token-attr-href="links.mein_suchprofil" data-export-field="emb_benefits_3col_button_label" data-export-url-field="emb_benefits_3col_button_url" data-export-role="cta">Suchprofil anlegen</a>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="teaser-1col" data-snippet="emb_teaser_1col">
        <div class="module__inner">
          <div class="teaser-single">
            <h2 class="module__title module__title--medium" data-export-field="emb_teaser_1col_headline" data-export-role="headline">Alles Wichtige kompakt gebündelt</h2>
            <a class="media-link" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-url-field="emb_teaser_1col_image_link_url" data-export-role="image-link">
              <div class="media media--hero">
                <div
                  class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                  data-image-field="emb_teaser_1col_image_url"
                  data-image-alt-field="emb_teaser_1col_image_alt"
                >
                  <div class="preview-image-placeholder__text">
                    <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                  </div>
                </div>
              </div>
            </a>
            <div class="module__teaser-richtext" data-export-field="emb_teaser_1col_body" data-export-role="richtext">
              <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Die Vorlage kann nach der ersten Vorschau frei angepasst und mit weiteren Modulen erweitert werden.</p>
            </div>
            <div class="module__cta-row module__cta-row--compact">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_teaser_1col_button_label" data-export-url-field="emb_teaser_1col_button_url" data-export-role="cta">Mehr erfahren</a>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-gray" data-module="servicetiles" data-snippet="emb_servicetiles">
        <div class="module__inner">
          <div class="stack">
            <div class="module__head">
              <h2 class="module__title module__title--medium" data-export-field="emb_servicetiles_headline" data-export-role="headline">Passende Services für Ihre Immobilie</h2>
            </div>
            <div class="servicetiles-grid">
              <article class="servicetiles-card" data-export-item="service-card" data-export-index="1">
                <a class="servicetiles-card__link" href="https://www.immobilienscout24.de/lp/energieberatung.html" target="_blank" rel="noreferrer" data-export-url-field="emb_servicetiles_col_1_url">
                  <div class="servicetiles-card__panel">
                    <div class="servicetiles-card__header">
                      <img class="servicetiles-card__icon" src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/txv/cq2/g2k/money_house_white.png" alt="" width="32" height="32" data-image-field="emb_servicetiles_col_1_icon_url" />
                    </div>
                    <h3 class="servicetiles-card__title" data-export-field="emb_servicetiles_col_1_title">Energieberatung</h3>
                    <p class="module__body servicetiles-card__body" data-export-field="emb_servicetiles_col_1_description">Bis zu 70% Förderung erhalten</p>
                  </div>
                </a>
              </article>
              <article class="servicetiles-card" data-export-item="service-card" data-export-index="2">
                <a class="servicetiles-card__link" href="https://www.immobilienscout24.de/lp/nutzungsdauer-quickcheck.html" target="_blank" rel="noreferrer" data-export-url-field="emb_servicetiles_col_2_url">
                  <div class="servicetiles-card__panel">
                    <div class="servicetiles-card__header">
                      <img class="servicetiles-card__icon" src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/t7v/n1z/j9p/calculator_white.png" alt="" width="32" height="32" data-image-field="emb_servicetiles_col_2_icon_url" />
                    </div>
                    <h3 class="servicetiles-card__title" data-export-field="emb_servicetiles_col_2_title">Nutzungsdauer-Rechner</h3>
                    <p class="module__body servicetiles-card__body" data-export-field="emb_servicetiles_col_2_description">Kostenlos berechnen</p>
                  </div>
                </a>
              </article>
              <article class="servicetiles-card" data-export-item="service-card" data-export-index="3">
                <a class="servicetiles-card__link" href="https://www.immobilienscout24.de/energieausweis.html" target="_blank" rel="noreferrer" data-export-url-field="emb_servicetiles_col_3_url">
                  <div class="servicetiles-card__panel">
                    <div class="servicetiles-card__header">
                      <img class="servicetiles-card__icon" src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/1is/2t3/zqq/Energieausweiss.png" alt="" width="32" height="32" data-image-field="emb_servicetiles_col_3_icon_url" />
                    </div>
                    <h3 class="servicetiles-card__title" data-export-field="emb_servicetiles_col_3_title">Energieausweis bestellen</h3>
                    <p class="module__body servicetiles-card__body" data-export-field="emb_servicetiles_col_3_description">Pflicht für Vermietung &amp; Verkauf</p>
                  </div>
                </a>
              </article>
              <article class="servicetiles-card" data-export-item="service-card" data-export-index="4">
                <a class="servicetiles-card__link" href="https://www.immobilienscout24.de/lp/klarwatt.html" target="_blank" rel="noreferrer" data-export-url-field="emb_servicetiles_col_4_url">
                  <div class="servicetiles-card__panel">
                    <div class="servicetiles-card__header">
                      <img class="servicetiles-card__icon" src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/feo/2fr/t9a/flash.png" alt="" width="32" height="32" data-image-field="emb_servicetiles_col_4_icon_url" />
                    </div>
                    <h3 class="servicetiles-card__title" data-export-field="emb_servicetiles_col_4_title">Dynamischer Stromtarif</h3>
                    <p class="module__body servicetiles-card__body" data-export-field="emb_servicetiles_col_4_description">Strom sparen, monatlich kündbar</p>
                  </div>
                </a>
              </article>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="contact-signoff" data-snippet="emb_contact_signoff">
        <div class="module__inner">
          <div class="contact-card">
            <div class="contact-copy">
              <p class="contact-signoff">Freundliche Grüße<br />Ihr ImmoScout24-Team</p>
            </div>
          </div>
        </div>
      </section>

      <footer class="module theme-white" data-module="footer" data-snippet="emb_footer_marketing">
        <div class="module__inner module__inner--compact">
          <div class="footer-marketing">
            <p class="footer-marketing__headline">Kostenlose App herunterladen</p>
            <div class="footer-marketing__badges">
              <a class="footer-badge" href="https://itunes.apple.com/de/app/immobilienscout24/id342157367?mt=8" target="_blank" rel="noreferrer" data-token-attr-href="links.app_store">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/i36/uhu/m14/d1284a48-db27-4f3b-a434-ab9a625d0dd4.png"
                  data-token-attr-src="assets.app_store_badge"
                  alt="Download on the App Store"
                  width="115"
                  height="37"
                />
              </a>
              <a class="footer-badge" href="https://play.google.com/store/apps/details?id=de.is24.android&amp;hl=de" target="_blank" rel="noreferrer" data-token-attr-href="links.google_play">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/nrd/s3d/49k/b78e3fcd-6303-429c-a29d-691d73c0d01d.png"
                  data-token-attr-src="assets.google_play_badge"
                  alt="Get it on Google Play"
                  width="130"
                  height="37"
                />
              </a>
            </div>
            <div class="footer-marketing__copy">
              <p class="footer-marketing__text">ImmoScout24 informiert ueber Aktuelles aus der Immobilienwelt. Wenn kein Interesse mehr besteht, ist es moeglich, sich <a href="#" target="_blank" rel="noreferrer">hier abzumelden</a>. Die Abmeldung betrifft nicht gegebenenfalls bestehende Suchauftragsbenachrichtigungen.</p>
              <p class="footer-marketing__text">Immobilien Scout GmbH - Ein Unternehmen der Scout24-Gruppe, Invalidenstr. 65, 10557 Berlin · <a class="footer-marketing__plain-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.website" data-token-text="links.website_label">immobilienscout24.de</a> · Geschaeftsfuehrung: Dr. Gesa Crockford, Daniel Hendel · Vorsitzender des Aufsichtsrats: Ralf Weitz · Handelsregister: Amtsgericht Charlottenburg, HRB 69108 · Sitz der Gesellschaft: Berlin · USt-IdNr. DE200269419</p>
              <p class="footer-marketing__links">
                <a href="https://www.immobilienscout24.de/agb/datenschutz.html" target="_blank" rel="noreferrer" data-token-attr-href="links.privacy">Datenschutz</a><span class="footer-marketing__links-separator">|</span><a href="https://www.immobilienscout24.de/impressum.html" target="_blank" rel="noreferrer" data-token-attr-href="links.imprint">Impressum</a>
              </p>
              <p class="footer-marketing__text">&copy; 1999 - 2026 Immobilien Scout GmbH</p>
            </div>
          </div>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
```

## email-builder/agent/starter-ho-esg.state.json

Dateityp: json

```json
{
  "campaignId": null,
  "templateId": null,
  "previewBranchKey": null,
  "templateContext": {
    "mode": "default_template",
    "resolvedBaseTemplateId": "569946",
    "compositionTemplateId": null,
    "iterableTemplateId": null
  },
  "salutationContext": "generic",
  "subject": "Ihre Vorlage für Energie- und Immobilienservices",
  "preheader": "Eine kurze Beispielmail mit passenden Services rund um Ihre Immobilie.",
  "modules": [
    {
      "instance_id": "logo-centered-1",
      "module_id": "logo-centered",
      "snippet_name": "emb_logo_centered",
      "content": {}
    },
    {
      "instance_id": "hero-image-top-center-1",
      "module_id": "hero-image-top-center",
      "snippet_name": "emb_hero_image_top_center",
      "content": {
        "emb_hero_image_top_center_bg_color": "#FFFFFF",
        "emb_hero_image_top_center_show_preheadline": true,
        "emb_hero_image_top_center_preheadline": "Homeowner Services",
        "emb_hero_image_top_center_show_badge": false,
        "emb_hero_image_top_center_show_small_headline": false,
        "emb_hero_image_top_center_show_large_headline": true,
        "emb_hero_image_top_center_headline": "Hilfreiche Services rund um Ihre Immobilie",
        "emb_hero_image_top_center_image_url": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png",
        "emb_hero_image_top_center_image_alt": "",
        "emb_hero_image_top_center_show_salutation": true,
        "emb_hero_image_top_center_use_snippetcall_salutation": false,
        "emb_hero_image_top_center_salutation": "Hallo Anrede,",
        "emb_hero_image_top_center_body": "<p>Diese Vorlage zeigt eine mögliche Struktur für Ihre E-Mail.</p>",
        "emb_hero_image_top_center_button_url": "https://www.immobilienscout24.de/",
        "emb_hero_image_top_center_button_bg_color": "#74FFDF",
        "emb_hero_image_top_center_button_border_color": "#74FFDF",
        "emb_hero_image_top_center_button_label": "Mehr erfahren"
      }
    },
    {
      "instance_id": "benefits-3col-1",
      "module_id": "benefits-3col",
      "snippet_name": "emb_benefits_3col",
      "content": {
        "emb_benefits_3col_bg_color": "#F5F5F5",
        "emb_benefits_3col_show_headline": true,
        "emb_benefits_3col_headline": "Ihre Vorteile auf einen Blick",
        "emb_benefits_3col_col_1_icon_url": "https://www.static-immobilienscout24.de/fro/emb/_/s24_lightbulb_48.png",
        "emb_benefits_3col_col_1_body": "<strong>Orientierung gewinnen</strong><br>Erhalten Sie einen schnellen Überblick über passende Services.",
        "emb_benefits_3col_col_2_icon_url": "https://www.static-immobilienscout24.de/fro/emb/_/s24_calendar_checkmark_48.png",
        "emb_benefits_3col_col_2_body": "<strong>Nächste Schritte planen</strong><br>Nutzen Sie die Vorlage als klaren Startpunkt für Ihre Mail.",
        "emb_benefits_3col_col_3_icon_url": "https://www.static-immobilienscout24.de/fro/emb/_/s24_checkmark_circle_48.png",
        "emb_benefits_3col_col_3_body": "<strong>Services direkt anbieten</strong><br>Binden Sie relevante Angebote einfach in die Kommunikation ein.",
        "emb_benefits_3col_show_cta": true,
        "emb_benefits_3col_button_url": "https://www.immobilienscout24.de/meinsuchprofil/meinsuchprofilanlage/",
        "emb_benefits_3col_button_bg_color": "#FFFFFF",
        "emb_benefits_3col_button_border_color": "#333333",
        "emb_benefits_3col_button_label": "Suchprofil anlegen"
      }
    },
    {
      "instance_id": "teaser-1col-1",
      "module_id": "teaser-1col",
      "snippet_name": "emb_teaser_1col",
      "content": {
        "emb_teaser_1col_bg_color": "#FFFFFF",
        "emb_teaser_1col_headline": "Alles Wichtige kompakt gebündelt",
        "emb_teaser_1col_image_link_url": "https://www.immobilienscout24.de/",
        "emb_teaser_1col_image_url": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png",
        "emb_teaser_1col_image_alt": "",
        "emb_teaser_1col_body": "<p>Die Vorlage kann nach der ersten Vorschau frei angepasst und mit weiteren Modulen erweitert werden.</p>",
        "emb_teaser_1col_button_url": "https://www.immobilienscout24.de/",
        "emb_teaser_1col_button_bg_color": "#FFFFFF",
        "emb_teaser_1col_button_border_color": "#333333",
        "emb_teaser_1col_button_label": "Mehr erfahren"
      }
    },
    {
      "instance_id": "servicetiles-1",
      "module_id": "servicetiles",
      "snippet_name": "emb_servicetiles",
      "content": {
        "emb_servicetiles_bg_color": "#F5F5F5",
        "emb_servicetiles_headline": "Passende Services für Ihre Immobilie",
        "emb_servicetiles_col_1_url": "https://www.immobilienscout24.de/lp/energieberatung.html",
        "emb_servicetiles_col_1_icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/txv/cq2/g2k/money_house_white.png",
        "emb_servicetiles_col_1_title": "Energieberatung",
        "emb_servicetiles_col_1_description": "Bis zu 70% Förderung erhalten",
        "emb_servicetiles_col_2_url": "https://www.immobilienscout24.de/lp/nutzungsdauer-quickcheck.html",
        "emb_servicetiles_col_2_icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/t7v/n1z/j9p/calculator_white.png",
        "emb_servicetiles_col_2_title": "Nutzungsdauer-Rechner",
        "emb_servicetiles_col_2_description": "Kostenlos berechnen",
        "emb_servicetiles_col_3_url": "https://www.immobilienscout24.de/energieausweis.html",
        "emb_servicetiles_col_3_icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/1is/2t3/zqq/Energieausweiss.png",
        "emb_servicetiles_col_3_title": "Energieausweis bestellen",
        "emb_servicetiles_col_3_description": "Pflicht für Vermietung & Verkauf",
        "emb_servicetiles_col_4_url": "https://www.immobilienscout24.de/lp/klarwatt.html",
        "emb_servicetiles_col_4_icon_url": "https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/feo/2fr/t9a/flash.png",
        "emb_servicetiles_col_4_title": "Dynamischer Stromtarif",
        "emb_servicetiles_col_4_description": "Strom sparen, monatlich kündbar"
      }
    },
    {
      "instance_id": "contact-signoff-1",
      "module_id": "contact-signoff",
      "snippet_name": "emb_contact_signoff",
      "content": {}
    },
    {
      "instance_id": "footer-1",
      "module_id": "footer",
      "snippet_name": "emb_footer_marketing",
      "content": {}
    }
  ]
}
```

## email-builder/agent/starter-seeker-mle.preview.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>E-Mail Vorschau | Seeker | MLE</title>
  <link rel="stylesheet" href="https://s24-creative-ops.github.io/email-builder/preview-styles.css" />
</head>
<body>
  <div class="preview-shell">
    <main class="preview-canvas">
      <section class="module preview-subject" data-preview-slot="subject">
        <div class="module__inner">
          <div class="preview-subject__stack">
            <p class="preview-subject__line preview-subject__line--subject">Subject: <span data-preview-subject-text>Finanzierung prüfen für deine Wunschimmobilie</span></p>
            <p class="preview-subject__line preview-subject__line--preheader">Preheader: <span data-preview-preheader-text>Eine kurze Beispielmail mit Einstieg, Auswahl und passenden nächsten Schritten.</span></p>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="logo-centered" data-snippet="emb_logo_centered">
        <div class="module__inner module__inner--logo module__inner--logo-centered">
          <a class="module__logo-link" href="https://www.immobilienscout24.de/" title="ImmoScout24" style="display:inline-block;">
            <img
              class="module__logo-image"
              src="https://www.static-immobilienscout24.de/fro/ite/_/IS24-Logo_horizontal_center_white.png"
              alt="Logo ImmoScout24"
              width="198"
              height="47"
              style="display:block;padding:0;text-align:center;background:rgba(255,255,255,0);"
            />
          </a>
        </div>
      </section>

      <section class="module theme-white" data-module="hero-fakeform-buttons-image" data-snippet="emb_hero_fakeform_buttons_image">
        <div class="module__inner">
          <div class="module__hero-area module__hero-area--head">
            <div class="module__head module__head--center">
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_headline_size" data-export-role="technical-variant">l</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_small_headline" data-export-role="technical-flag">false</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_large_headline" data-export-role="technical-flag">true</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_salutation" data-export-role="technical-flag">true</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_2" data-export-role="technical-flag">true</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_3" data-export-role="technical-flag">true</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_4" data-export-role="technical-flag">true</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_5" data-export-role="technical-flag">true</span>
              <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_6" data-export-role="technical-flag">false</span>
              <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_fakeform_buttons_image_headline" data-export-role="headline" data-preview-size-field="emb_hero_fakeform_buttons_image_headline_size" data-preview-size-legacy-small-field="emb_hero_fakeform_buttons_image_show_small_headline" data-preview-size-legacy-large-field="emb_hero_fakeform_buttons_image_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Reicht dein Eigenkapital für deine Wunschimmobilie?</h2>
            </div>
            <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
          </div>
          <div class="module__hero-flow">
            <div class="module__hero-area module__hero-area--copy">
              <div class="module__copy module__copy--center">
                <div class="card">
                  <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="1">
                    <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_1_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_1_url" data-export-role="choice-button">unter 10.000 €</a>
                  </div>
                  <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="2">
                    <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_2_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_2_url" data-export-role="choice-button">10.000–50.000 €</a>
                  </div>
                  <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="3">
                    <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_3_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_3_url" data-export-role="choice-button">50.000–100.000 €</a>
                  </div>
                  <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="4">
                    <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_4_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_4_url" data-export-role="choice-button">100.000–250.000 €</a>
                  </div>
                  <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="5">
                    <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_5_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_5_url" data-export-role="choice-button">über 250.000 €</a>
                  </div>
                  <div class="module__cta-row module__cta-row--center is-hidden" data-export-item="hero-fakeform-choice-button" data-export-index="6">
                    <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_6_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_6_url" data-export-role="choice-button">Button 6</a>
                  </div>
                </div>
                <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
                <div class="media media--hero">
                  <div
                    class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                    data-image-field="emb_hero_fakeform_buttons_image_image_url"
                    data-image-alt-field="emb_hero_fakeform_buttons_image_image_alt"
                  >
                    <div class="preview-image-placeholder__text">
                      <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
                    </div>
                  </div>
                </div>
                <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
                <p class="module__body" data-export-field="emb_hero_fakeform_buttons_image_salutation" data-export-role="salutation">Hallo Anrede,</p>
                <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
                <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_fakeform_buttons_image_body" data-export-role="richtext">
                  <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Wähle aus, wie viel Eigenkapital du einplanst – wir zeigen dir passende nächste Schritte für deine Finanzierung.</p>
                </div>
                <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
                <div class="module__cta-row module__cta-row--center">
                  <a class="button-filled-brand" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_button_label" data-export-url-field="emb_hero_fakeform_buttons_image_button_url" data-export-role="cta">Jetzt prüfen</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-gray" data-module="benefits-3col" data-snippet="emb_benefits_3col">
        <div class="module__inner">
          <div class="stack">
            <div class="module__head">
              <h2 class="module__title module__title--medium" data-export-field="emb_benefits_3col_headline" data-export-role="headline">Deine Vorteile auf einen Blick</h2>
            </div>
            <div class="benefits-columns">
              <article class="benefit-item" data-export-item="benefit-card" data-export-index="1">
                <img
                  class="benefit-item__icon"
                  src="https://www.static-immobilienscout24.de/fro/emb/_/s24_lightbulb_48.png"
                  alt=""
                  width="48"
                  height="48"
                  data-icon-field="emb_benefits_3col_col_1_icon_url"
                />
                <p class="module__body" data-export-field="emb_benefits_3col_col_1_body" data-export-role="item-body"><strong>Finanzierung einschätzen</strong><br />Erhalte eine erste Orientierung für dein Budget.</p>
              </article>
              <article class="benefit-item" data-export-item="benefit-card" data-export-index="2">
                <img
                  class="benefit-item__icon"
                  src="https://www.static-immobilienscout24.de/fro/emb/_/s24_calendar_checkmark_48.png"
                  alt=""
                  width="48"
                  height="48"
                  data-icon-field="emb_benefits_3col_col_2_icon_url"
                />
                <p class="module__body" data-export-field="emb_benefits_3col_col_2_body" data-export-role="item-body"><strong>Nächste Schritte planen</strong><br />Nutze die Vorlage als klaren Startpunkt für deine Mail.</p>
              </article>
              <article class="benefit-item" data-export-item="benefit-card" data-export-index="3">
                <img
                  class="benefit-item__icon"
                  src="https://www.static-immobilienscout24.de/fro/emb/_/s24_checkmark_circle_48.png"
                  alt=""
                  width="48"
                  height="48"
                  data-icon-field="emb_benefits_3col_col_3_icon_url"
                />
                <p class="module__body" data-export-field="emb_benefits_3col_col_3_body" data-export-role="item-body"><strong>Passende Angebote finden</strong><br />Zeige relevante Optionen für den Weg zur Wunschimmobilie.</p>
              </article>
            </div>
            <div class="module__cta-row">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/meinsuchprofil/meinsuchprofilanlage/" target="_blank" rel="noreferrer" data-token-attr-href="links.mein_suchprofil" data-export-field="emb_benefits_3col_button_label" data-export-url-field="emb_benefits_3col_button_url" data-export-role="cta">Mehr erfahren</a>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="teaser-1col" data-snippet="emb_teaser_1col">
        <div class="module__inner">
          <div class="teaser-single">
            <h2 class="module__title module__title--medium" data-export-field="emb_teaser_1col_headline" data-export-role="headline">Gut vorbereitet zur passenden Finanzierung</h2>
            <a class="media-link" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-url-field="emb_teaser_1col_image_link_url" data-export-role="image-link">
              <div class="media media--hero">
                <div
                  class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                  data-image-field="emb_teaser_1col_image_url"
                  data-image-alt-field="emb_teaser_1col_image_alt"
                >
                  <div class="preview-image-placeholder__text">
                    <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                  </div>
                </div>
              </div>
            </a>
            <div class="module__teaser-richtext" data-export-field="emb_teaser_1col_body" data-export-role="richtext">
              <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Die Vorlage kann nach der ersten Vorschau frei angepasst und mit weiteren Modulen erweitert werden.</p>
            </div>
            <div class="module__cta-row module__cta-row--compact">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_teaser_1col_button_label" data-export-url-field="emb_teaser_1col_button_url" data-export-role="cta">Mehr erfahren</a>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="contact-signoff" data-snippet="emb_contact_signoff">
        <div class="module__inner">
          <div class="contact-card">
            <div class="contact-copy">
              <p class="contact-signoff">Freundliche Grüße<br />Ihr ImmoScout24-Team</p>
            </div>
          </div>
        </div>
      </section>

      <footer class="module theme-white" data-module="footer" data-snippet="emb_footer_marketing">
        <div class="module__inner module__inner--compact">
          <div class="footer-marketing">
            <p class="footer-marketing__headline">Kostenlose App herunterladen</p>
            <div class="footer-marketing__badges">
              <a class="footer-badge" href="https://itunes.apple.com/de/app/immobilienscout24/id342157367?mt=8" target="_blank" rel="noreferrer" data-token-attr-href="links.app_store">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/i36/uhu/m14/d1284a48-db27-4f3b-a434-ab9a625d0dd4.png"
                  data-token-attr-src="assets.app_store_badge"
                  alt="Download on the App Store"
                  width="115"
                  height="37"
                />
              </a>
              <a class="footer-badge" href="https://play.google.com/store/apps/details?id=de.is24.android&amp;hl=de" target="_blank" rel="noreferrer" data-token-attr-href="links.google_play">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/nrd/s3d/49k/b78e3fcd-6303-429c-a29d-691d73c0d01d.png"
                  data-token-attr-src="assets.google_play_badge"
                  alt="Get it on Google Play"
                  width="130"
                  height="37"
                />
              </a>
            </div>
            <div class="footer-marketing__copy">
              <p class="footer-marketing__text">ImmoScout24 informiert ueber Aktuelles aus der Immobilienwelt. Wenn kein Interesse mehr besteht, ist es moeglich, sich <a href="#" target="_blank" rel="noreferrer">hier abzumelden</a>. Die Abmeldung betrifft nicht gegebenenfalls bestehende Suchauftragsbenachrichtigungen.</p>
              <p class="footer-marketing__text">Immobilien Scout GmbH - Ein Unternehmen der Scout24-Gruppe, Invalidenstr. 65, 10557 Berlin · <a class="footer-marketing__plain-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.website" data-token-text="links.website_label">immobilienscout24.de</a> · Geschaeftsfuehrung: Dr. Gesa Crockford, Daniel Hendel · Vorsitzender des Aufsichtsrats: Ralf Weitz · Handelsregister: Amtsgericht Charlottenburg, HRB 69108 · Sitz der Gesellschaft: Berlin · USt-IdNr. DE200269419</p>
              <p class="footer-marketing__links">
                <a href="https://www.immobilienscout24.de/agb/datenschutz.html" target="_blank" rel="noreferrer" data-token-attr-href="links.privacy">Datenschutz</a><span class="footer-marketing__links-separator">|</span><a href="https://www.immobilienscout24.de/impressum.html" target="_blank" rel="noreferrer" data-token-attr-href="links.imprint">Impressum</a>
              </p>
              <p class="footer-marketing__text">&copy; 1999 - 2026 Immobilien Scout GmbH</p>
            </div>
          </div>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
```

## email-builder/agent/starter-seeker-mle.state.json

Dateityp: json

```json
{
  "campaignId": null,
  "templateId": null,
  "previewBranchKey": null,
  "templateContext": {
    "mode": "default_template",
    "resolvedBaseTemplateId": "569946",
    "compositionTemplateId": null,
    "iterableTemplateId": null
  },
  "salutationContext": "generic",
  "subject": "Finanzierung prüfen für deine Wunschimmobilie",
  "preheader": "Eine kurze Beispielmail mit Einstieg, Auswahl und passenden nächsten Schritten.",
  "modules": [
    {
      "instance_id": "logo-centered-1",
      "module_id": "logo-centered",
      "snippet_name": "emb_logo_centered",
      "content": {}
    },
    {
      "instance_id": "hero-fakeform-buttons-image-1",
      "module_id": "hero-fakeform-buttons-image",
      "snippet_name": "emb_hero_fakeform_buttons_image",
      "content": {
        "emb_hero_fakeform_buttons_image_bg_color": "#FFFFFF",
        "emb_hero_fakeform_buttons_image_show_small_headline": false,
        "emb_hero_fakeform_buttons_image_show_large_headline": true,
        "emb_hero_fakeform_buttons_image_headline": "Reicht dein Eigenkapital für deine Wunschimmobilie?",
        "emb_hero_fakeform_buttons_image_choice_button_1_url": "https://www.immobilienscout24.de/",
        "emb_hero_fakeform_buttons_image_choice_button_1_label": "unter 10.000 €",
        "emb_hero_fakeform_buttons_image_show_item_2": true,
        "emb_hero_fakeform_buttons_image_choice_button_2_url": "https://www.immobilienscout24.de/",
        "emb_hero_fakeform_buttons_image_choice_button_2_label": "10.000–50.000 €",
        "emb_hero_fakeform_buttons_image_show_item_3": true,
        "emb_hero_fakeform_buttons_image_choice_button_3_url": "https://www.immobilienscout24.de/",
        "emb_hero_fakeform_buttons_image_choice_button_3_label": "50.000–100.000 €",
        "emb_hero_fakeform_buttons_image_show_item_4": true,
        "emb_hero_fakeform_buttons_image_choice_button_4_url": "https://www.immobilienscout24.de/",
        "emb_hero_fakeform_buttons_image_choice_button_4_label": "100.000–250.000 €",
        "emb_hero_fakeform_buttons_image_show_item_5": true,
        "emb_hero_fakeform_buttons_image_choice_button_5_url": "https://www.immobilienscout24.de/",
        "emb_hero_fakeform_buttons_image_choice_button_5_label": "über 250.000 €",
        "emb_hero_fakeform_buttons_image_show_item_6": false,
        "emb_hero_fakeform_buttons_image_choice_button_6_url": "https://www.immobilienscout24.de/",
        "emb_hero_fakeform_buttons_image_choice_button_6_label": "",
        "emb_hero_fakeform_buttons_image_image_url": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png",
        "emb_hero_fakeform_buttons_image_image_alt": "",
        "emb_hero_fakeform_buttons_image_show_salutation": true,
        "emb_hero_fakeform_buttons_image_use_snippetcall_salutation": false,
        "emb_hero_fakeform_buttons_image_salutation": "Hallo Anrede,",
        "emb_hero_fakeform_buttons_image_body": "<p>Wähle aus, wie viel Eigenkapital du einplanst – wir zeigen dir passende nächste Schritte für deine Finanzierung.</p>",
        "emb_hero_fakeform_buttons_image_button_url": "https://www.immobilienscout24.de/",
        "emb_hero_fakeform_buttons_image_button_bg_color": "#74FFDF",
        "emb_hero_fakeform_buttons_image_button_border_color": "#74FFDF",
        "emb_hero_fakeform_buttons_image_button_label": "Jetzt prüfen"
      }
    },
    {
      "instance_id": "benefits-3col-1",
      "module_id": "benefits-3col",
      "snippet_name": "emb_benefits_3col",
      "content": {
        "emb_benefits_3col_bg_color": "#F5F5F5",
        "emb_benefits_3col_show_headline": true,
        "emb_benefits_3col_headline": "Deine Vorteile auf einen Blick",
        "emb_benefits_3col_col_1_icon_url": "https://www.static-immobilienscout24.de/fro/emb/_/s24_lightbulb_48.png",
        "emb_benefits_3col_col_1_body": "<strong>Finanzierung einschätzen</strong><br>Erhalte eine erste Orientierung für dein Budget.",
        "emb_benefits_3col_col_2_icon_url": "https://www.static-immobilienscout24.de/fro/emb/_/s24_calendar_checkmark_48.png",
        "emb_benefits_3col_col_2_body": "<strong>Nächste Schritte planen</strong><br>Nutze die Vorlage als klaren Startpunkt für deine Mail.",
        "emb_benefits_3col_col_3_icon_url": "https://www.static-immobilienscout24.de/fro/emb/_/s24_checkmark_circle_48.png",
        "emb_benefits_3col_col_3_body": "<strong>Passende Angebote finden</strong><br>Zeige relevante Optionen für den Weg zur Wunschimmobilie.",
        "emb_benefits_3col_show_cta": true,
        "emb_benefits_3col_button_url": "https://www.immobilienscout24.de/meinsuchprofil/meinsuchprofilanlage/",
        "emb_benefits_3col_button_bg_color": "#FFFFFF",
        "emb_benefits_3col_button_border_color": "#333333",
        "emb_benefits_3col_button_label": "Mehr erfahren"
      }
    },
    {
      "instance_id": "teaser-1col-1",
      "module_id": "teaser-1col",
      "snippet_name": "emb_teaser_1col",
      "content": {
        "emb_teaser_1col_bg_color": "#FFFFFF",
        "emb_teaser_1col_headline": "Gut vorbereitet zur passenden Finanzierung",
        "emb_teaser_1col_image_link_url": "https://www.immobilienscout24.de/",
        "emb_teaser_1col_image_url": "https://library.eu.iterable.com/33/98/b9799c74eec5412c8fb0c995dd52f19c-emb_placeholder_16x9.png",
        "emb_teaser_1col_image_alt": "",
        "emb_teaser_1col_body": "<p>Die Vorlage kann nach der ersten Vorschau frei angepasst und mit weiteren Modulen erweitert werden.</p>",
        "emb_teaser_1col_button_url": "https://www.immobilienscout24.de/",
        "emb_teaser_1col_button_bg_color": "#FFFFFF",
        "emb_teaser_1col_button_border_color": "#333333",
        "emb_teaser_1col_button_label": "Mehr erfahren"
      }
    },
    {
      "instance_id": "contact-signoff-1",
      "module_id": "contact-signoff",
      "snippet_name": "emb_contact_signoff",
      "content": {}
    },
    {
      "instance_id": "footer-1",
      "module_id": "footer",
      "snippet_name": "emb_footer_marketing",
      "content": {}
    }
  ]
}
```

## email-builder/agent/preview-modules.html

Dateityp: html

```html
<!-- MODULE: logo | SNIPPET: emb_logo -->
<section class="module theme-white" data-module="logo" data-snippet="emb_logo">
  <div class="module__inner module__inner--logo">
    <a class="module__logo-link" href="https://www.immobilienscout24.de/" title="ImmoScout24">
      <img
        class="module__logo-image"
        src="https://www.static-immobilienscout24.de/fro/ite/_/IS24-Logo_horizontal_left_white.png"
        alt="Logo ImmoScout24"
        width="185"
        height="47"
      />
    </a>
  </div>
</section>


<!-- MODULE: logo-centered | SNIPPET: emb_logo_centered -->
<section class="module theme-white" data-module="logo-centered" data-snippet="emb_logo_centered">
  <div class="module__inner module__inner--logo module__inner--logo-centered">
    <a class="module__logo-link" href="https://www.immobilienscout24.de/" title="ImmoScout24" style="display:inline-block;">
      <img
        class="module__logo-image"
        src="https://www.static-immobilienscout24.de/fro/ite/_/IS24-Logo_horizontal_center_white.png"
        alt="Logo ImmoScout24"
        width="198"
        height="47"
        style="display:block;padding:0;text-align:center;background:rgba(255,255,255,0);"
      />
    </a>
  </div>
</section>

<!-- MODULE: hero-image-top | SNIPPET: emb_hero_image_top -->
<section class="module theme-white" data-module="hero-image-top" data-snippet="emb_hero_image_top">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head">
        <div class="module__hero-meta">
          <p class="module__eyebrow" data-export-field="emb_hero_image_top_preheadline" data-export-role="preheadline">Digitales Immobilienprodukt</p>
          <span class="module__badge is-hidden">Badge</span>
        </div>
        <span class="is-hidden" data-export-field="emb_hero_image_top_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_image_top_headline" data-export-role="headline" data-preview-size-field="emb_hero_image_top_headline_size" data-preview-size-legacy-small-field="emb_hero_image_top_show_small_headline" data-preview-size-legacy-large-field="emb_hero_image_top_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Vermarkten Sie Ihre Immobilie digital, klar und zeitsparend</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_image_top_image_url"
            data-image-alt-field="emb_hero_image_top_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
        <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
      </div>
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy">
          <p class="module__body" data-export-field="emb_hero_image_top_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_image_top_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Mit einem digitalen Vermarktungspaket gewinnen Sie mehr Übersicht und bringen Ihre Vermarktung einfacher in den Alltag.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_image_top_button_label" data-export-url-field="emb_hero_image_top_button_url" data-export-role="cta">Lorem ipsum dolor</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- MODULE: hero-image-top-center | SNIPPET: emb_hero_image_top_center -->
<section class="module theme-white" data-module="hero-image-top-center" data-snippet="emb_hero_image_top_center">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head module__head--center">
        <div class="module__hero-meta">
          <p class="module__eyebrow" data-export-field="emb_hero_image_top_center_preheadline" data-export-role="preheadline">Digitales Immobilienprodukt</p>
          <span class="module__badge is-hidden" data-export-field="emb_hero_image_top_center_badge_label" data-export-role="badge">Badge</span>
        </div>
        <span class="is-hidden" data-export-field="emb_hero_image_top_center_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_center_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_center_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_center_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_center_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_image_top_center_headline" data-export-role="headline" data-preview-size-field="emb_hero_image_top_center_headline_size" data-preview-size-legacy-small-field="emb_hero_image_top_center_show_small_headline" data-preview-size-legacy-large-field="emb_hero_image_top_center_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Vermarkten Sie Ihre Immobilie digital, klar und zeitsparend</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_image_top_center_image_url"
            data-image-alt-field="emb_hero_image_top_center_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
        <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
      </div>
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy module__copy--center">
          <p class="module__body" data-export-field="emb_hero_image_top_center_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_image_top_center_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Mit einem digitalen Vermarktungspaket gewinnen Sie mehr Übersicht und bringen Ihre Vermarktung einfacher in den Alltag.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row module__cta-row--center">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_image_top_center_button_label" data-export-url-field="emb_hero_image_top_center_button_url" data-export-role="cta">Lorem ipsum dolor</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>



<!-- MODULE: hero-image-top-bleed | SNIPPET: emb_hero_image_top_bleed -->
<section class="module theme-white" data-module="hero-image-top-bleed" data-snippet="emb_hero_image_top_bleed">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head">
        <div class="module__hero-meta">
          <p class="module__eyebrow" data-export-field="emb_hero_image_top_bleed_preheadline" data-export-role="preheadline">Digitales Immobilienprodukt</p>
          <span class="module__badge is-hidden">Badge</span>
        </div>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_image_top_bleed_headline" data-export-role="headline" data-preview-size-field="emb_hero_image_top_bleed_headline_size" data-preview-size-legacy-small-field="emb_hero_image_top_bleed_show_small_headline" data-preview-size-legacy-large-field="emb_hero_image_top_bleed_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Vermarkten Sie Ihre Immobilie digital, klar und zeitsparend</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero media--bleed">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_image_top_bleed_image_url"
            data-image-alt-field="emb_hero_image_top_bleed_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
        <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
      </div>
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy">
          <p class="module__body" data-export-field="emb_hero_image_top_bleed_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_image_top_bleed_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Mit einem digitalen Vermarktungspaket gewinnen Sie mehr Übersicht und bringen Ihre Vermarktung einfacher in den Alltag.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_hero_image_top_bleed_button_label" data-export-url-field="emb_hero_image_top_bleed_button_url" data-export-role="cta">Lorem ipsum dolor</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- MODULE: hero-image-top-bleed-center | SNIPPET: emb_hero_image_top_bleed_center -->
<section class="module theme-white" data-module="hero-image-top-bleed-center" data-snippet="emb_hero_image_top_bleed_center">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head module__head--center">
        <div class="module__hero-meta">
          <p class="module__eyebrow" data-export-field="emb_hero_image_top_bleed_center_preheadline" data-export-role="preheadline">Digitales Immobilienprodukt</p>
          <span class="module__badge is-hidden" data-export-field="emb_hero_image_top_bleed_center_badge_label" data-export-role="badge">Badge</span>
        </div>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_center_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_center_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_center_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_center_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_image_top_bleed_center_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_image_top_bleed_center_headline" data-export-role="headline" data-preview-size-field="emb_hero_image_top_bleed_center_headline_size" data-preview-size-legacy-small-field="emb_hero_image_top_bleed_center_show_small_headline" data-preview-size-legacy-large-field="emb_hero_image_top_bleed_center_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Vermarkten Sie Ihre Immobilie digital, klar und zeitsparend</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero media--bleed">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_image_top_bleed_center_image_url"
            data-image-alt-field="emb_hero_image_top_bleed_center_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
        <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
      </div>
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy module__copy--center">
          <p class="module__body" data-export-field="emb_hero_image_top_bleed_center_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_image_top_bleed_center_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Mit einem digitalen Vermarktungspaket gewinnen Sie mehr Übersicht und bringen Ihre Vermarktung einfacher in den Alltag.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row module__cta-row--center">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_image_top_bleed_center_button_label" data-export-url-field="emb_hero_image_top_bleed_center_button_url" data-export-role="cta">Lorem ipsum dolor</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>



<!-- MODULE: hero-image-head-copy-bleed-center | SNIPPET: emb_hero_image_head_copy_bleed_center -->
<section class="module theme-white" data-module="hero-image-head-copy-bleed-center" data-snippet="emb_hero_image_head_copy_bleed_center">
  <div class="module__inner">
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero media--bleed">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_image_head_copy_bleed_center_image_url"
            data-image-alt-field="emb_hero_image_head_copy_bleed_center_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 1200 x 600 px<br />(Hi-Res 2400 x 1200)</p>
            </div>
          </div>
        </div>
        <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
      </div>
      <div class="module__hero-area module__hero-area--head">
        <div class="module__head module__head--center">
          <span class="is-hidden" data-export-field="emb_hero_image_head_copy_bleed_center_headline_size" data-export-role="technical-variant">l</span>
          <span class="is-hidden" data-export-field="emb_hero_image_head_copy_bleed_center_show_small_headline" data-export-role="technical-flag">false</span>
          <span class="is-hidden" data-export-field="emb_hero_image_head_copy_bleed_center_show_large_headline" data-export-role="technical-flag">true</span>
          <span class="is-hidden" data-export-field="emb_hero_image_head_copy_bleed_center_show_salutation" data-export-role="technical-flag">true</span>
          <span class="is-hidden" data-export-field="emb_hero_image_head_copy_bleed_center_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
          <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_image_head_copy_bleed_center_headline" data-export-role="headline" data-preview-size-field="emb_hero_image_head_copy_bleed_center_headline_size" data-preview-size-legacy-small-field="emb_hero_image_head_copy_bleed_center_show_small_headline" data-preview-size-legacy-large-field="emb_hero_image_head_copy_bleed_center_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Lorem ipsum dolor sit amet cum</h2>
        </div>
        <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
      </div>
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy module__copy--center">
          <p class="module__body" data-export-field="emb_hero_image_head_copy_bleed_center_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_image_head_copy_bleed_center_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Lorem ipsum dolor sit amet cum</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row module__cta-row--center">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_hero_image_head_copy_bleed_center_button_label" data-export-url-field="emb_hero_image_head_copy_bleed_center_button_url" data-export-role="cta">Mehr erfahren</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: hero-image-textbox-cta-center | SNIPPET: emb_hero_image_textbox_cta_center -->
<section class="module theme-white" data-module="hero-image-textbox-cta-center" data-snippet="emb_hero_image_textbox_cta_center">
  <div class="module__inner">
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--head">
        <div class="module__head module__head--center">
          <span class="is-hidden" data-export-field="emb_hero_image_textbox_cta_center_headline_size" data-export-role="technical-variant">l</span>
          <span class="is-hidden" data-export-field="emb_hero_image_textbox_cta_center_show_small_headline" data-export-role="technical-flag">false</span>
          <span class="is-hidden" data-export-field="emb_hero_image_textbox_cta_center_show_large_headline" data-export-role="technical-flag">true</span>
          <span class="is-hidden" data-export-field="emb_hero_image_textbox_cta_center_show_salutation" data-export-role="technical-flag">true</span>
          <span class="is-hidden" data-export-field="emb_hero_image_textbox_cta_center_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
          <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_image_textbox_cta_center_headline" data-export-role="headline" data-preview-size-field="emb_hero_image_textbox_cta_center_headline_size" data-preview-size-legacy-small-field="emb_hero_image_textbox_cta_center_show_small_headline" data-preview-size-legacy-large-field="emb_hero_image_textbox_cta_center_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Lorem ipsum dolor sit amet cum ventus laudare estere</h2>
        </div>
        <div class="module__hero-spacer module__hero-spacer--24" aria-hidden="true"></div>
      </div>
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero-entry">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_image_textbox_cta_center_image_url"
            data-image-alt-field="emb_hero_image_textbox_cta_center_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
        <div class="module__hero-spacer module__hero-spacer--32" aria-hidden="true"></div>
      </div>
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy module__copy--center">
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_image_textbox_cta_center_body" data-export-role="richtext">
            <p class="module__body" data-export-field="emb_hero_image_textbox_cta_center_salutation" data-export-role="salutation">Hallo Anrede,</p>
            <p class="module__body">Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean este commodo ligula eget dolor. Aenean massa. Cum sociis natoque eanis penatibus et magnis dis parturient montes.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--32" aria-hidden="true"></div>
          <p class="module__body"><strong data-export-field="emb_hero_image_textbox_cta_center_question" data-export-role="question">Lorem ipsum dolor sit amet cum laudarte?</strong></p>
          <div class="module__hero-spacer module__hero-spacer--16" aria-hidden="true"></div>
          <a class="module__entry-box" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-url-field="emb_hero_image_textbox_cta_center_entry_url" data-export-role="entry-link" style="display:block;width:100%;max-width:214px;padding:15px 24px;border:1px solid #333333;border-radius:8px;background:#ffffff;text-align:left;text-decoration:none;">
            <p class="module__entry-text" style="margin:0;color:#ADADAD;" data-export-field="emb_hero_image_textbox_cta_center_entry_text" data-export-role="entry-text">z.B. 10115 Berlin</p>
          </a>
          <div class="module__hero-spacer module__hero-spacer--16" aria-hidden="true"></div>
          <div class="module__cta-row module__cta-row--center">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_image_textbox_cta_center_button_label" data-export-url-field="emb_hero_image_textbox_cta_center_button_url" data-export-role="cta">Button filled brand</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: hero-fakeform-buttons-image | SNIPPET: emb_hero_fakeform_buttons_image -->
<section class="module theme-white" data-module="hero-fakeform-buttons-image" data-snippet="emb_hero_fakeform_buttons_image">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head module__head--center">
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_2" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_3" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_4" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_5" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_fakeform_buttons_image_show_item_6" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_fakeform_buttons_image_headline" data-export-role="headline" data-preview-size-field="emb_hero_fakeform_buttons_image_headline_size" data-preview-size-legacy-small-field="emb_hero_fakeform_buttons_image_show_small_headline" data-preview-size-legacy-large-field="emb_hero_fakeform_buttons_image_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Reicht dein Eigenkapital für deine Wunschimmobilie?</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy module__copy--center">
          <div class="card">
            <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="1">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_1_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_1_url" data-export-role="choice-button">unter 10.000 €</a>
            </div>
            <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="2">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_2_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_2_url" data-export-role="choice-button">10.000–50.000 €</a>
            </div>
            <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="3">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_3_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_3_url" data-export-role="choice-button">50.000–100.000 €</a>
            </div>
            <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="4">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_4_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_4_url" data-export-role="choice-button">100.000–250.000 €</a>
            </div>
            <div class="module__cta-row module__cta-row--center" data-export-item="hero-fakeform-choice-button" data-export-index="5">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_5_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_5_url" data-export-role="choice-button">über 250.000 €</a>
            </div>
            <div class="module__cta-row module__cta-row--center is-hidden" data-export-item="hero-fakeform-choice-button" data-export-index="6">
              <a class="button-outline-strong" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_choice_button_6_label" data-export-url-field="emb_hero_fakeform_buttons_image_choice_button_6_url" data-export-role="choice-button">Button 6</a>
            </div>
          </div>
          <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
          <div class="media media--hero">
            <div
              class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
              data-image-field="emb_hero_fakeform_buttons_image_image_url"
              data-image-alt-field="emb_hero_fakeform_buttons_image_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
              </div>
            </div>
          </div>
          <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
          <p class="module__body" data-export-field="emb_hero_fakeform_buttons_image_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_fakeform_buttons_image_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Wähle aus, wie viel Eigenkapital du einplanst – wir zeigen dir passende nächste Schritte für deine Finanzierung.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row module__cta-row--center">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de/" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_fakeform_buttons_image_button_label" data-export-url-field="emb_hero_fakeform_buttons_image_button_url" data-export-role="cta">Jetzt prüfen</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: hero-cta-top | SNIPPET: emb_hero_cta_top -->
<section class="module theme-white" data-module="hero-cta-top" data-snippet="emb_hero_cta_top">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head">
        <div class="module__hero-meta">
          <p class="module__eyebrow" data-export-field="emb_hero_cta_top_preheadline" data-export-role="preheadline">Digitales Immobilienprodukt</p>
          <span class="module__badge is-hidden">Badge</span>
        </div>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_cta_top_headline" data-export-role="headline" data-preview-size-field="emb_hero_cta_top_headline_size" data-preview-size-legacy-small-field="emb_hero_cta_top_show_small_headline" data-preview-size-legacy-large-field="emb_hero_cta_top_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Vermarkten Sie Ihre Immobilie digital, klar und zeitsparend</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy">
          <p class="module__body" data-export-field="emb_hero_cta_top_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_cta_top_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Mit einem digitalen Vermarktungspaket gewinnen Sie mehr Übersicht und bringen Ihre Vermarktung einfacher in den Alltag.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_hero_cta_top_button_label" data-export-url-field="emb_hero_cta_top_button_url" data-export-role="cta">Lorem ipsum dolor</a>
          </div>
          <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
        </div>
      </div>
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_cta_top_image_url"
            data-image-alt-field="emb_hero_cta_top_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- MODULE: hero-cta-top-center | SNIPPET: emb_hero_cta_top_center -->
<section class="module theme-white" data-module="hero-cta-top-center" data-snippet="emb_hero_cta_top_center">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head module__head--center">
        <div class="module__hero-meta">
          <p class="module__eyebrow" data-export-field="emb_hero_cta_top_center_preheadline" data-export-role="preheadline">Digitales Immobilienprodukt</p>
          <span class="module__badge is-hidden" data-export-field="emb_hero_cta_top_center_badge_label" data-export-role="badge">Badge</span>
        </div>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_center_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_center_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_center_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_center_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_center_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_cta_top_center_headline" data-export-role="headline" data-preview-size-field="emb_hero_cta_top_center_headline_size" data-preview-size-legacy-small-field="emb_hero_cta_top_center_show_small_headline" data-preview-size-legacy-large-field="emb_hero_cta_top_center_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Vermarkten Sie Ihre Immobilie digital, klar und zeitsparend</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy module__copy--center">
          <p class="module__body" data-export-field="emb_hero_cta_top_center_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_cta_top_center_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Mit einem digitalen Vermarktungspaket gewinnen Sie mehr Übersicht und bringen Ihre Vermarktung einfacher in den Alltag.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row module__cta-row--center">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_cta_top_center_button_label" data-export-url-field="emb_hero_cta_top_center_button_url" data-export-role="cta">Lorem ipsum dolor</a>
          </div>
          <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
        </div>
      </div>
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_cta_top_center_image_url"
            data-image-alt-field="emb_hero_cta_top_center_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: hero-cta-top-no-bottom | SNIPPET: emb_hero_cta_top_no_bottom -->
<section class="module theme-white" data-module="hero-cta-top-no-bottom" data-snippet="emb_hero_cta_top_no_bottom">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head">
        <div class="module__hero-meta">
          <p class="module__eyebrow" data-export-field="emb_hero_cta_top_no_bottom_preheadline" data-export-role="preheadline">Digitales Immobilienprodukt</p>
          <span class="module__badge is-hidden">Badge</span>
        </div>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_cta_top_no_bottom_headline" data-export-role="headline" data-preview-size-field="emb_hero_cta_top_no_bottom_headline_size" data-preview-size-legacy-small-field="emb_hero_cta_top_no_bottom_show_small_headline" data-preview-size-legacy-large-field="emb_hero_cta_top_no_bottom_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Vermarkten Sie Ihre Immobilie digital, klar und zeitsparend</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy">
          <p class="module__body" data-export-field="emb_hero_cta_top_no_bottom_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_cta_top_no_bottom_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Mit einem digitalen Vermarktungspaket gewinnen Sie mehr Übersicht und bringen Ihre Vermarktung einfacher in den Alltag.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_hero_cta_top_no_bottom_button_label" data-export-url-field="emb_hero_cta_top_no_bottom_button_url" data-export-role="cta">Lorem ipsum dolor</a>
          </div>
          <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
        </div>
      </div>
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_cta_top_no_bottom_image_url"
            data-image-alt-field="emb_hero_cta_top_no_bottom_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- Source: email-builder/agent/preview-modules.html -->
<!-- MODULE: teaser-1col | SNIPPET: emb_teaser_1col -->
<section class="module theme-gray" data-module="teaser-1col" data-snippet="emb_teaser_1col">
  <div class="module__inner">
    <div class="teaser-single">
      <h2 class="module__title module__title--medium" data-export-field="emb_teaser_1col_headline" data-export-role="headline">Lorem ipsum dolor sit amet consectetur adipiscing elit</h2>
      <a class="media-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-url-field="emb_teaser_1col_image_link_url" data-export-role="image-link">
        <div class="media media--hero">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_teaser_1col_image_url"
            data-image-alt-field="emb_teaser_1col_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
            </div>
          </div>
        </div>
      </a>
      <div class="module__teaser-richtext" data-export-field="emb_teaser_1col_body" data-export-role="richtext">
        <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Lorem ipsum dolor sit amet, consetetur sadipscing elitr.</p>
        <ul class="module__list--teaser">
          <li data-export-item="teaser-list-item" data-export-index="1">Lorem ipsum dolor sit amet</li>
          <li data-export-item="teaser-list-item" data-export-index="2">Consetetur sadipscing elitr</li>
          <li data-export-item="teaser-list-item" data-export-index="3">Sed diam nonumy eirmod</li>
        </ul>
      </div>
      <div class="module__cta-row module__cta-row--compact">
        <a class="button-outline-strong" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_1col_button_label" data-export-url-field="emb_teaser_1col_button_url" data-export-role="cta">button-outline-strong</a>
      </div>
    </div>
  </div>
</section>
<!-- MODULE: loft-snl-copy-cta | SNIPPET: emb_loft_snl_copy_cta -->
<section class="module theme-gray" data-module="loft-snl-copy-cta" data-snippet="emb_loft_snl_copy_cta">
  <div class="module__inner">
    <div class="teaser-single">
      <p class="module__body" data-export-role="salutation">Hallo Anrede,</p>
      <div class="module__teaser-richtext" data-export-field="emb_loft_snl_copy_cta_body" data-export-role="richtext">
        <p class="module__body" data-export-role="body-paragraph" data-export-index="1">in der Pufendorfstraße in Berlin-Friedrichshain wurden <strong>65 Wohnungen realisiert</strong>, von denen bereits rund 70 % vermietet sind. Die Einheiten umfassen <strong>2 bis 4 Zimmer mit ca. 46 m² bis 120 m²</strong> und sind sofort bezugsfrei.</p>
        <p class="module__body" data-export-role="body-paragraph" data-export-index="2">Die Lage in Friedrichshain bietet kurze Wege zum Volkspark sowie zum Boxhagener Platz. Zugleich besteht eine schnelle Anbindung: Der Alexanderplatz ist nach wenigen U-Bahn- oder Tram-Stationen erreichbar.</p>
        <ul class="module__list--teaser">
          <li data-export-item="teaser-list-item" data-export-index="1">Beispiel für frei einsetzbare Listen innerhalb des Richtext-Bereichs</li>
          <li data-export-item="teaser-list-item" data-export-index="2"><a href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer">Links</a> können direkt im Copy-Bereich stehen</li>
          <li data-export-item="teaser-list-item" data-export-index="3"><strong>Fettungen</strong> bleiben ebenfalls Teil des freien Inhalts</li>
        </ul>
        <p class="module__body" data-export-role="body-paragraph" data-export-index="3"><strong>Nutzen Sie den Tag der offenen Tür</strong> für einen persönlichen Eindruck vor Ort und informieren Sie sich zu den noch verfügbaren Wohnungen.</p>
      </div>
      <div class="module__cta-row module__cta-row--compact">
        <a class="button-filled-default" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_loft_snl_copy_cta_button_label" data-export-url-field="emb_loft_snl_copy_cta_button_url" data-export-role="cta">Mehr erfahren</a>
      </div>
    </div>
  </div>
</section>
<!-- MODULE: loft-snl-copy-sections-cta | SNIPPET: emb_loft_snl_copy_sections_cta -->
<section class="module theme-gray" data-module="loft-snl-copy-sections-cta" data-snippet="emb_loft_snl_copy_sections_cta">
  <div class="module__inner">
    <div class="stack">
      <section>
        <h2 class="module__title module__title--small" data-export-field="emb_loft_snl_copy_sections_cta_headline_1" data-export-role="headline">Highlights</h2>
        <div class="module__teaser-richtext" data-export-field="emb_loft_snl_copy_sections_cta_body_1" data-export-role="richtext">
          <ul class="module__list--teaser">
            <li data-export-item="teaser-list-item" data-export-index="1"><strong>Zentrale Lage:</strong> Friedrichshain mit Nähe zu Volkspark und Boxhagener Platz</li>
            <li data-export-item="teaser-list-item" data-export-index="2"><strong>Wohnungsvielfalt:</strong> 2 bis 4 Zimmer auf ca. 46 m² bis 120 m²</li>
            <li data-export-item="teaser-list-item" data-export-index="3"><strong>Ausstattung:</strong> Parkett, Fußbodenheizung, bodentiefe Fenster und Aufzug</li>
            <li data-export-item="teaser-list-item" data-export-index="4"><strong>Außenbereiche:</strong> Balkone, Terrassen sowie Gartenanteile im Erdgeschoss</li>
          </ul>
        </div>
      </section>
      <section>
        <h2 class="module__title module__title--small" data-export-field="emb_loft_snl_copy_sections_cta_headline_2" data-export-role="headline">Wohnbeispiele</h2>
        <div class="module__teaser-richtext" data-export-field="emb_loft_snl_copy_sections_cta_body_2" data-export-role="richtext">
          <ul class="module__list--teaser">
            <li data-export-item="teaser-list-item" data-export-index="1">2 Zimmer, 4. OG, ca. 50,76 m², 1.552 € Kaltmiete</li>
            <li data-export-item="teaser-list-item" data-export-index="2">3 Zimmer, 2. OG, ca. 78,21 m², 2.168 € Kaltmiete</li>
            <li data-export-item="teaser-list-item" data-export-index="3">4 Zimmer, 1. OG, ca. 98,11 m², 2.594 € Kaltmiete</li>
          </ul>
        </div>
      </section>
      <div class="module__cta-row module__cta-row--compact">
        <a class="button-filled-default" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_loft_snl_copy_sections_cta_button_label" data-export-url-field="emb_loft_snl_copy_sections_cta_button_url" data-export-role="cta">Mehr erfahren</a>
      </div>
    </div>
  </div>
</section>
<!-- MODULE: loft-rnl-dev-intro | SNIPPET: emb_loft_rnl_dev_intro -->
<section class="module theme-white" data-module="loft-rnl-dev-intro" data-snippet="emb_loft_rnl_dev_intro">
  <div class="module__inner">
    <div class="teaser-single">
      <div class="intro-richtext">
        <h2 class="module__title font-heading-large-bold loft-rnl-dev-intro__headline" data-export-field="emb_loft_rnl_dev_intro_headline" data-export-role="headline">Immobilien-Newsletter München</h2>
        <p class="module__body" data-export-field="emb_loft_rnl_dev_intro_salutation" data-export-role="salutation">Hallo Anrede</p>
        <div class="module__teaser-richtext" data-export-field="emb_loft_rnl_dev_intro_body" data-export-role="richtext">
          <p class="module__body" data-export-role="body-paragraph" data-export-index="1">willkommen zum aktuellen Immobilien-Newsletter für München und Umgebung.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<!-- MODULE: loft-rnl-dev-teaser-1col | SNIPPET: emb_loft_rnl_dev_teaser_1col -->
<section class="module theme-gray" data-module="loft-rnl-dev-teaser-1col" data-snippet="emb_loft_rnl_dev_teaser_1col">
  <div class="module__inner">
    <div class="teaser-single">
      <div class="module__head">
        <div class="module__hero-meta">
          <span class="module__badge module__badge--surface-white" data-export-field="emb_loft_rnl_dev_teaser_1col_badge_label" data-export-role="badge">Wohnungen zum Kauf</span>
        </div>
        <h2 class="module__title font-heading-large-bold loft-rnl-dev-teaser-1col__headline" data-export-field="emb_loft_rnl_dev_teaser_1col_headline" data-export-role="headline">Urbanes Wohnen am Stadtpark in Berlin-Pankow</h2>
      </div>
      <div class="media media--hero">
        <div
          class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
          data-image-field="emb_loft_rnl_dev_teaser_1col_image_url"
          data-image-alt-field="emb_loft_rnl_dev_teaser_1col_image_alt"
        >
          <div class="preview-image-placeholder__text">
            <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
          </div>
        </div>
      </div>
      <div class="module__teaser-richtext" data-export-field="emb_loft_rnl_dev_teaser_1col_body" data-export-role="richtext">
        <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Das Projekt verbindet eine ruhige Lage am Grünzug mit einer direkten Anbindung in die Innenstadt. Großzügige Wohnbereiche, bodentiefe Fenster und private Außenflächen schaffen ein helles Wohngefühl.</p>
        <p class="module__body" data-export-role="body-paragraph" data-export-index="2">Die Projektkarte nutzt eine einheitliche Struktur für Badge, Headline, Bild, Copy, Detailblock und CTA, damit sich mehrere Neubauprojekte im Template konsistent aufbauen lassen.</p>
      </div>
      <section class="loft-rnl-dev-teaser-1col__details">
        <h2 class="module__title module__title--small">Details zum Projekt</h2>
        <div class="module__teaser-richtext" data-export-field="emb_loft_rnl_dev_teaser_1col_details" data-export-role="richtext">
          <ul class="module__list--teaser">
            <li data-export-item="teaser-list-item" data-export-index="1">2 bis 4 Zimmer mit Grundrissen für unterschiedliche Lebensphasen</li>
            <li data-export-item="teaser-list-item" data-export-index="2">Balkone, Terrassen und gemeinschaftliche Außenbereiche</li>
            <li data-export-item="teaser-list-item" data-export-index="3">Gute Anbindung an ÖPNV, Kitas und Nahversorgung im Quartier</li>
          </ul>
        </div>
      </section>
      <div class="module__cta-row module__cta-row--compact">
        <a class="button-filled-default" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_loft_rnl_dev_teaser_1col_button_label" data-export-url-field="emb_loft_rnl_dev_teaser_1col_button_url" data-export-role="cta">Exposé anfordern</a>
      </div>
    </div>
  </div>
</section>
<!-- MODULE: loft-regio-resi-intro | SNIPPET: emb_loft_regio_resi_intro -->
<section class="module theme-white" data-module="loft-regio-resi-intro" data-snippet="emb_loft_regio_resi_intro">
  <div class="module__inner">
    <div class="teaser-single">
      <div class="intro-richtext">
        <h2 class="module__title font-heading-large-bold loft-regio-resi-intro__headline" data-export-field="emb_loft_regio_resi_intro_headline" data-export-role="headline">Ausgewählte Wohnimmobilien aus Ihrer Region</h2>
        <p class="module__body" data-export-field="emb_loft_regio_resi_intro_salutation" data-export-role="salutation">Hallo Anrede</p>
        <div class="module__teaser-richtext" data-export-field="emb_loft_regio_resi_intro_body" data-export-role="richtext">
          <p class="module__body" data-export-role="body-paragraph" data-export-index="1">hier finden Sie ausgewaehlte Wohnimmobilien aus Ihrer Region. Das Intro fuehrt bewusst kompakt in die folgenden Objekt-Highlights ein und laesst dem wiederholbaren Residential-Teaser den inhaltlichen Schwerpunkt.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<!-- MODULE: loft-regio-resi-teaser-1col | SNIPPET: emb_loft_regio_resi_teaser_1col -->
<section class="module theme-gray" data-module="loft-regio-resi-teaser-1col" data-snippet="emb_loft_regio_resi_teaser_1col">
  <div class="module__inner">
    <div class="teaser-single">
      <div class="module__head">
        <h2 class="module__title font-heading-large-bold loft-regio-resi-teaser-1col__headline" data-export-field="emb_loft_regio_resi_teaser_1col_headline" data-export-role="headline">Historischer Charme trifft modernen Wohnkomfort</h2>
      </div>
      <div class="module__teaser-richtext" data-export-field="emb_loft_regio_resi_teaser_1col_body" data-export-role="richtext">
        <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Das sanierte Einfamilienhaus in Naunhof bei Leipzig aus dem Jahr 1900 bietet eine luxurioese Ausstattung mit Fussbodenheizung, Keller und Einliegerwohnung. Die ruhige Lage im idyllischen Ortsteil Lindhardt ermoeglicht naturnahes Wohnen nahe mehrerer Seen und vielfaeltiger Freizeitmoeglichkeiten.</p>
        <p class="module__body" data-export-role="body-paragraph" data-export-index="2">Besondere Merkmale sind der Pool, Jacuzzi sowie die hochwertige Aussenanlage mit moderner Technik und dreifach verglasten Fenstern.</p>
      </div>
      <div class="media media--hero">
        <div
          class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
          data-image-field="emb_loft_regio_resi_teaser_1col_image_url"
          data-image-alt-field="emb_loft_regio_resi_teaser_1col_image_alt"
        >
          <div class="preview-image-placeholder__text">
            <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
          </div>
        </div>
      </div>
      <div class="loft-regio-resi-teaser-1col__stats mobile_hide">
        <div class="loft-regio-resi-teaser-1col__stat">
          <p class="loft-regio-resi-teaser-1col__stat-value" data-export-field="emb_loft_regio_resi_teaser_1col_metric_1_value" data-export-role="metric-value" data-export-index="1">1.250.000 €</p>
          <p class="loft-regio-resi-teaser-1col__stat-label" data-export-field="emb_loft_regio_resi_teaser_1col_metric_1_label" data-export-role="metric-label" data-export-index="1">Kaufpreis</p>
        </div>
        <div class="loft-regio-resi-teaser-1col__stat">
          <p class="loft-regio-resi-teaser-1col__stat-value" data-export-field="emb_loft_regio_resi_teaser_1col_metric_2_value" data-export-role="metric-value" data-export-index="2">357,2 m²</p>
          <p class="loft-regio-resi-teaser-1col__stat-label" data-export-field="emb_loft_regio_resi_teaser_1col_metric_2_label" data-export-role="metric-label" data-export-index="2">Wohnfläche ca.</p>
        </div>
        <div class="loft-regio-resi-teaser-1col__stat">
          <p class="loft-regio-resi-teaser-1col__stat-value" data-export-field="emb_loft_regio_resi_teaser_1col_metric_3_value" data-export-role="metric-value" data-export-index="3">7</p>
          <p class="loft-regio-resi-teaser-1col__stat-label" data-export-field="emb_loft_regio_resi_teaser_1col_metric_3_label" data-export-role="metric-label" data-export-index="3">Zimmeranzahl</p>
        </div>
      </div>
      <ul class="module__list--teaser loft-regio-resi-teaser-1col__stats-list">
        <li><span data-export-field="emb_loft_regio_resi_teaser_1col_metric_1_label" data-export-role="metric-label" data-export-index="1">Kaufpreis</span>: <strong data-export-field="emb_loft_regio_resi_teaser_1col_metric_1_value" data-export-role="metric-value" data-export-index="1">1.250.000 €</strong></li>
        <li><span data-export-field="emb_loft_regio_resi_teaser_1col_metric_2_label" data-export-role="metric-label" data-export-index="2">Wohnfläche ca.</span>: <strong data-export-field="emb_loft_regio_resi_teaser_1col_metric_2_value" data-export-role="metric-value" data-export-index="2">357,2 m²</strong></li>
        <li><span data-export-field="emb_loft_regio_resi_teaser_1col_metric_3_label" data-export-role="metric-label" data-export-index="3">Zimmeranzahl</span>: <strong data-export-field="emb_loft_regio_resi_teaser_1col_metric_3_value" data-export-role="metric-value" data-export-index="3">7</strong></li>
      </ul>
      <div class="module__cta-row module__cta-row--compact">
        <a class="button-filled-default" href="https://www.immobilienscout24.de/expose/152345678" target="_blank" rel="noreferrer" data-export-field="emb_loft_regio_resi_teaser_1col_button_label" data-export-url-field="emb_loft_regio_resi_teaser_1col_button_url" data-export-role="cta">Exposé anfordern</a>
      </div>
    </div>
  </div>
</section>
<!-- MODULE: teaser-2col-horizontal | SNIPPET: emb_teaser_2col_horizontal -->
<section class="module theme-gray" data-module="teaser-2col-horizontal" data-snippet="emb_teaser_2col_horizontal">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_teaser_2col_horizontal_headline" data-export-role="headline">Lorem ipsum dolor sit amet</h2>
      </div>
      <div class="alternating-teasers">
        <article class="teaser-split" data-export-item="teaser-2col-horizontal-item" data-export-index="1">
          <div class="media media--teaser-horizontal teaser-split__media">
            <div
              class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
              data-image-field="emb_teaser_2col_horizontal_col_1_image_url"
              data-image-alt-field="emb_teaser_2col_horizontal_col_1_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
              </div>
            </div>
          </div>
          <div class="teaser-split__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_horizontal_col_1_body" data-export-role="item-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_2col_horizontal_col_1_chevron_label" data-export-url-field="emb_teaser_2col_horizontal_col_1_chevron_url" data-export-role="item-link">Lorem ipsum</a>
          </div>
        </article>
        <article class="teaser-split" data-export-item="teaser-2col-horizontal-item" data-export-index="2">
          <div class="media media--teaser-horizontal teaser-split__media">
            <div
              class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
              data-image-field="emb_teaser_2col_horizontal_col_2_image_url"
              data-image-alt-field="emb_teaser_2col_horizontal_col_2_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
              </div>
            </div>
          </div>
          <div class="teaser-split__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_horizontal_col_2_body" data-export-role="item-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_2col_horizontal_col_2_chevron_label" data-export-url-field="emb_teaser_2col_horizontal_col_2_chevron_url" data-export-role="item-link">Lorem ipsum</a>
          </div>
        </article>
        <article class="teaser-split" data-export-item="teaser-2col-horizontal-item" data-export-index="3">
          <div class="media media--teaser-horizontal teaser-split__media">
            <div
              class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
              data-image-field="emb_teaser_2col_horizontal_col_3_image_url"
              data-image-alt-field="emb_teaser_2col_horizontal_col_3_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
              </div>
            </div>
          </div>
          <div class="teaser-split__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_horizontal_col_3_body" data-export-role="item-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam quis nostrud exercitation.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_2col_horizontal_col_3_chevron_label" data-export-url-field="emb_teaser_2col_horizontal_col_3_chevron_url" data-export-role="item-link">Lorem ipsum</a>
          </div>
        </article>
        <article class="teaser-split" data-export-item="teaser-2col-horizontal-item" data-export-index="4">
          <div class="media media--teaser-horizontal teaser-split__media">
            <div
              class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
              data-image-field="emb_teaser_2col_horizontal_col_4_image_url"
              data-image-alt-field="emb_teaser_2col_horizontal_col_4_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
              </div>
            </div>
          </div>
          <div class="teaser-split__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_horizontal_col_4_body" data-export-role="item-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_2col_horizontal_col_4_chevron_label" data-export-url-field="emb_teaser_2col_horizontal_col_4_chevron_url" data-export-role="item-link">Lorem ipsum</a>
          </div>
        </article>
      </div>
    </div>
  </div>
</section>


<!-- Source: email-builder/agent/preview-modules.html -->
<section class="module theme-white" data-module="teaser-2col-vertical" data-snippet="emb_teaser_2col_vertical">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_teaser_2col_vertical_headline" data-export-role="headline">Digitale Werkzeuge für Vermarktung und Kommunikation</h2>
      </div>
      <div class="teaser-columns">
        <article class="teaser-column" data-export-item="teaser-2col-vertical-item" data-export-index="1">
          <div class="media media--teaser-horizontal">
            <div
              class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
              data-image-field="emb_teaser_2col_vertical_col_1_image_url"
              data-image-alt-field="emb_teaser_2col_vertical_col_1_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
              </div>
            </div>
          </div>
          <div class="teaser-column__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_vertical_col_1_body" data-export-role="item-body">Planen Sie Ihren Start digital, behalten Sie Aufgaben im Blick und kommunizieren Sie direkt mit Interessierten.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_2col_vertical_col_1_chevron_label" data-export-url-field="emb_teaser_2col_vertical_col_1_chevron_url" data-export-role="item-link">Mehr erfahren</a>
          </div>
        </article>
        <article class="teaser-column" data-export-item="teaser-2col-vertical-item" data-export-index="2">
          <div class="media media--teaser-horizontal">
            <div
              class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
              data-image-field="emb_teaser_2col_vertical_col_2_image_url"
              data-image-alt-field="emb_teaser_2col_vertical_col_2_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
              </div>
            </div>
          </div>
          <div class="teaser-column__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_vertical_col_2_body" data-export-role="item-body">Bereiten Sie Exposé, Unterlagen und Rückmeldungen so vor, dass Ihr Prozess klar und einfach steuerbar bleibt.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_2col_vertical_col_2_chevron_label" data-export-url-field="emb_teaser_2col_vertical_col_2_chevron_url" data-export-role="item-link">Zum Überblick</a>
          </div>
        </article>
      </div>
    </div>
  </div>
</section>

<!-- MODULE: hero-cta-top-no-bottom-center | SNIPPET: emb_hero_cta_top_no_bottom_center -->
<section class="module theme-white" data-module="hero-cta-top-no-bottom-center" data-snippet="emb_hero_cta_top_no_bottom_center">
  <div class="module__inner">
    <div class="module__hero-area module__hero-area--head">
      <div class="module__head module__head--center">
        <div class="module__hero-meta">
          <p class="module__eyebrow" data-export-field="emb_hero_cta_top_no_bottom_center_preheadline" data-export-role="preheadline">Digitales Immobilienprodukt</p>
          <span class="module__badge is-hidden" data-export-field="emb_hero_cta_top_no_bottom_center_badge_label" data-export-role="badge">Badge</span>
        </div>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_center_headline_size" data-export-role="technical-variant">l</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_center_show_small_headline" data-export-role="technical-flag">false</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_center_show_large_headline" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_center_show_salutation" data-export-role="technical-flag">true</span>
        <span class="is-hidden" data-export-field="emb_hero_cta_top_no_bottom_center_use_snippetcall_salutation" data-export-role="technical-flag">false</span>
        <h2 class="module__title module__title--hero-large" data-export-field="emb_hero_cta_top_no_bottom_center_headline" data-export-role="headline" data-preview-size-field="emb_hero_cta_top_no_bottom_center_headline_size" data-preview-size-legacy-small-field="emb_hero_cta_top_no_bottom_center_show_small_headline" data-preview-size-legacy-large-field="emb_hero_cta_top_no_bottom_center_show_large_headline" data-preview-size-small-class="module__title--hero-small" data-preview-size-large-class="module__title--hero-large" data-preview-size-invalid-class="module__title--hero-invalid">Vermarkten Sie Ihre Immobilie digital, klar und zeitsparend</h2>
      </div>
      <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
    </div>
    <div class="module__hero-flow">
      <div class="module__hero-area module__hero-area--copy">
        <div class="module__copy module__copy--center">
          <p class="module__body" data-export-field="emb_hero_cta_top_no_bottom_center_salutation" data-export-role="salutation">Hallo Anrede,</p>
          <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
          <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_cta_top_no_bottom_center_body" data-export-role="richtext">
            <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Mit einem digitalen Vermarktungspaket gewinnen Sie mehr Übersicht und bringen Ihre Vermarktung einfacher in den Alltag.</p>
          </div>
          <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
          <div class="module__cta-row module__cta-row--center">
            <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_cta_top_no_bottom_center_button_label" data-export-url-field="emb_hero_cta_top_no_bottom_center_button_url" data-export-role="cta">Lorem ipsum dolor</a>
          </div>
          <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
        </div>
      </div>
      <div class="module__hero-area module__hero-area--image">
        <div class="media media--hero">
          <div
            class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
            data-image-field="emb_hero_cta_top_no_bottom_center_image_url"
            data-image-alt-field="emb_hero_cta_top_no_bottom_center_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px<br />(Hi-Res 1920 x 1080)</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: teaser-2col-alternating | SNIPPET: emb_teaser_2col_alternating -->
<section class="module theme-white" data-module="teaser-2col-alternating" data-snippet="emb_teaser_2col_alternating">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_teaser_2col_alternating_headline" data-export-role="headline">Zwei starke Bereiche für Ihre nächsten Schritte</h2>
      </div>
      <div class="alternating-teasers">
        <article class="teaser-split" data-export-item="teaser-2col-alternating-item" data-export-index="1">
          <div class="media media--teaser-alternating teaser-split__media">
            <div
              class="preview-image-placeholder preview-image-placeholder--4x3 preview-image-placeholder--pad-lg"
              data-image-field="emb_teaser_2col_alternating_col_1_image_url"
              data-image-alt-field="emb_teaser_2col_alternating_col_1_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">4:3 | 800 x 600 px</p>
              </div>
            </div>
          </div>
          <div class="teaser-split__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_alternating_col_1_body" data-export-role="item-body">Richten Sie Ihre Vermarktung so ein, dass Inhalt, Zeitplan und Interessentenkommunikation sauber aufeinander abgestimmt bleiben.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_2col_alternating_col_1_chevron_label" data-export-url-field="emb_teaser_2col_alternating_col_1_chevron_url" data-export-role="item-link">Zur Einführung</a>
          </div>
        </article>
        <article class="teaser-split teaser-split--reverse" data-export-item="teaser-2col-alternating-item" data-export-index="2">
          <div class="media media--teaser-alternating teaser-split__media">
            <div
              class="preview-image-placeholder preview-image-placeholder--4x3 preview-image-placeholder--pad-lg"
              data-image-field="emb_teaser_2col_alternating_col_2_image_url"
              data-image-alt-field="emb_teaser_2col_alternating_col_2_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">4:3 | 800 x 600 px</p>
              </div>
            </div>
          </div>
          <div class="teaser-split__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_alternating_col_2_body" data-export-role="item-body">Nutzen Sie klare Statusschritte, um Vermarktungsfortschritte sichtbar zu machen und die nächsten Aufgaben schnell abzuleiten.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_teaser_2col_alternating_col_2_chevron_label" data-export-url-field="emb_teaser_2col_alternating_col_2_chevron_url" data-export-role="item-link">Mehr Details</a>
          </div>
        </article>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: teaser-2col-listing | SNIPPET: emb_teaser_2col_listing -->
<section class="module theme-gray" data-module="teaser-2col-listing" data-snippet="emb_teaser_2col_listing">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_teaser_2col_listing_headline" data-export-role="headline">Lorem ipsum dolor sit amet</h2>
      </div>
      <div class="listing-rows">
        <article class="listing-row" data-export-item="teaser-2col-listing-item" data-export-index="1">
          <div class="media media--listing">
            <div
              class="preview-image-placeholder preview-image-placeholder--4x3 preview-image-placeholder--pad-sm"
              data-image-field="emb_teaser_2col_listing_col_1_image_url"
              data-image-alt-field="emb_teaser_2col_listing_col_1_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">4:3 | 800 x 600 px</p>
              </div>
            </div>
          </div>
          <div class="listing-row__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_listing_col_1_body" data-export-role="item-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_teaser_2col_listing_col_1_chevron_label" data-export-url-field="emb_teaser_2col_listing_col_1_chevron_url" data-export-role="item-link">Lorem ipsum</a>
          </div>
        </article>
        <article class="listing-row" data-export-item="teaser-2col-listing-item" data-export-index="2">
          <div class="media media--listing">
            <div
              class="preview-image-placeholder preview-image-placeholder--4x3 preview-image-placeholder--pad-sm"
              data-image-field="emb_teaser_2col_listing_col_2_image_url"
              data-image-alt-field="emb_teaser_2col_listing_col_2_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">4:3 | 800 x 600 px</p>
              </div>
            </div>
          </div>
          <div class="listing-row__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_listing_col_2_body" data-export-role="item-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_teaser_2col_listing_col_2_chevron_label" data-export-url-field="emb_teaser_2col_listing_col_2_chevron_url" data-export-role="item-link">Lorem ipsum</a>
          </div>
        </article>
        <article class="listing-row" data-export-item="teaser-2col-listing-item" data-export-index="3">
          <div class="media media--listing">
            <div
              class="preview-image-placeholder preview-image-placeholder--4x3 preview-image-placeholder--pad-sm"
              data-image-field="emb_teaser_2col_listing_col_3_image_url"
              data-image-alt-field="emb_teaser_2col_listing_col_3_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">4:3 | 800 x 600 px</p>
              </div>
            </div>
          </div>
          <div class="listing-row__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_listing_col_3_body" data-export-role="item-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_teaser_2col_listing_col_3_chevron_label" data-export-url-field="emb_teaser_2col_listing_col_3_chevron_url" data-export-role="item-link">Lorem ipsum</a>
          </div>
        </article>
        <article class="listing-row" data-export-item="teaser-2col-listing-item" data-export-index="4">
          <div class="media media--listing">
            <div
              class="preview-image-placeholder preview-image-placeholder--4x3 preview-image-placeholder--pad-sm"
              data-image-field="emb_teaser_2col_listing_col_4_image_url"
              data-image-alt-field="emb_teaser_2col_listing_col_4_image_alt"
            >
              <div class="preview-image-placeholder__text">
                <p class="preview-image-placeholder__meta">4:3 | 800 x 600 px</p>
              </div>
            </div>
          </div>
          <div class="listing-row__copy">
            <p class="module__body" data-export-field="emb_teaser_2col_listing_col_4_body" data-export-role="item-body">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.</p>
            <a class="teaser-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_teaser_2col_listing_col_4_chevron_label" data-export-url-field="emb_teaser_2col_listing_col_4_chevron_url" data-export-role="item-link">Lorem ipsum</a>
          </div>
        </article>
      </div>
      <div class="module__cta-row is-hidden">
        <a class="button-outline-strong" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_teaser_2col_listing_button_label" data-export-url-field="emb_teaser_2col_listing_button_url" data-export-role="cta">Mehr erfahren</a>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: teaser-2col-gallery | SNIPPET: emb_teaser_2col_gallery -->
<section class="module theme-white" data-module="teaser-2col-gallery" data-snippet="emb_teaser_2col_gallery">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_teaser_2col_gallery_headline" data-export-role="headline">Impressionen</h2>
      </div>
      <div class="gallery-grid">
        <div class="gallery-grid__row">
          <article class="gallery-grid__item" data-export-item="teaser-2col-gallery-item" data-export-index="1">
            <div class="media media--teaser-horizontal gallery-grid__media">
              <div
                class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                data-image-field="emb_teaser_2col_gallery_col_1_image_url"
                data-image-alt-field="emb_teaser_2col_gallery_col_1_image_alt"
              >
                <div class="preview-image-placeholder__text">
                  <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                </div>
              </div>
            </div>
          </article>
          <article class="gallery-grid__item" data-export-item="teaser-2col-gallery-item" data-export-index="2">
            <div class="media media--teaser-horizontal gallery-grid__media">
              <div
                class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                data-image-field="emb_teaser_2col_gallery_col_2_image_url"
                data-image-alt-field="emb_teaser_2col_gallery_col_2_image_alt"
              >
                <div class="preview-image-placeholder__text">
                  <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                </div>
              </div>
            </div>
          </article>
        </div>
        <div class="gallery-grid__row gallery-grid__row--mobile-hide">
          <article class="gallery-grid__item" data-export-item="teaser-2col-gallery-item" data-export-index="3">
            <div class="media media--teaser-horizontal gallery-grid__media">
              <div
                class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                data-image-field="emb_teaser_2col_gallery_col_3_image_url"
                data-image-alt-field="emb_teaser_2col_gallery_col_3_image_alt"
              >
                <div class="preview-image-placeholder__text">
                  <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                </div>
              </div>
            </div>
          </article>
          <article class="gallery-grid__item" data-export-item="teaser-2col-gallery-item" data-export-index="4">
            <div class="media media--teaser-horizontal gallery-grid__media">
              <div
                class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                data-image-field="emb_teaser_2col_gallery_col_4_image_url"
                data-image-alt-field="emb_teaser_2col_gallery_col_4_image_alt"
              >
                <div class="preview-image-placeholder__text">
                  <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                </div>
              </div>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: benefits-3col | SNIPPET: emb_benefits_3col -->
<section class="module theme-white" data-module="benefits-3col" data-snippet="emb_benefits_3col">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_benefits_3col_headline" data-export-role="headline">Darum lohnt sich Ihr Suchprofil</h2>
      </div>
      <div class="benefits-columns">
        <article class="benefit-item" data-export-item="benefit-card" data-export-index="1">
          <img
            class="benefit-item__icon"
            src="https://library.eu.iterable.com/33/98/d8ed736f1b5f427a92b67270fdd44469-s24_thump_up_48.png"
            alt=""
            width="48"
            height="48"
            data-icon-field="emb_benefits_3col_col_1_icon_url"
          />
          <p class="module__body" data-export-field="emb_benefits_3col_col_1_body" data-export-role="item-body">Neue Angebote landen direkt bei Ihnen, sobald sie zu Ihrer Suche passen.</p>
        </article>
        <article class="benefit-item" data-export-item="benefit-card" data-export-index="2">
          <img
            class="benefit-item__icon"
            src="https://library.eu.iterable.com/33/98/d8ed736f1b5f427a92b67270fdd44469-s24_thump_up_48.png"
            alt=""
            width="48"
            height="48"
            data-icon-field="emb_benefits_3col_col_2_icon_url"
          />
          <p class="module__body" data-export-field="emb_benefits_3col_col_2_body" data-export-role="item-body">Filtern Sie nach Lage, Preis und Groesse und sehen Sie nur relevante Treffer.</p>
        </article>
        <article class="benefit-item" data-export-item="benefit-card" data-export-index="3">
          <img
            class="benefit-item__icon"
            src="https://library.eu.iterable.com/33/98/d8ed736f1b5f427a92b67270fdd44469-s24_thump_up_48.png"
            alt=""
            width="48"
            height="48"
            data-icon-field="emb_benefits_3col_col_3_icon_url"
          />
          <p class="module__body" data-export-field="emb_benefits_3col_col_3_body" data-export-role="item-body">Merken Sie Angebote vor und starten Sie Ihre Anfrage mit nur wenigen Klicks.</p>
        </article>
      </div>
      <div class="module__cta-row">
        <a class="button-outline-strong" href="https://www.immobilienscout24.de/meinsuchprofil/meinsuchprofilanlage/" target="_blank" rel="noreferrer" data-export-field="emb_benefits_3col_button_label" data-export-url-field="emb_benefits_3col_button_url" data-export-role="cta">Suchprofil anlegen</a>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: servicetiles | SNIPPET: emb_servicetiles -->
<section class="module theme-white" data-module="servicetiles" data-snippet="emb_servicetiles">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_servicetiles_headline" data-export-role="headline">Passende Services fuer Ihre Immobiliensuche</h2>
      </div>
      <div class="servicetiles-grid">
        <article class="servicetiles-card" data-export-item="service-card" data-export-index="1">
          <a class="servicetiles-card__link" href="https://www.immobilienscout24.de/anbieten/anzeige-schalten/start/" target="_blank" rel="noreferrer" data-export-url-field="emb_servicetiles_col_1_url">
            <div class="servicetiles-card__panel">
              <div class="servicetiles-card__header">
                <img
                  class="servicetiles-card__icon"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/1u4/6b3/i28/board_sign_white.png"
                  alt=""
                  width="32"
                  height="32"
                  data-image-field="emb_servicetiles_col_1_icon_url"
                />
              </div>
              <h3 class="servicetiles-card__title" data-export-field="emb_servicetiles_col_1_title">Ab 0&euro; inserieren</h3>
              <p class="module__body servicetiles-card__body" data-export-field="emb_servicetiles_col_1_description">Mieter oder K&auml;ufer finden</p>
            </div>
          </a>
        </article>
        <article class="servicetiles-card" data-export-item="service-card" data-export-index="2">
          <a class="servicetiles-card__link" href="https://www.immobilienscout24.de/energieausweis.html" target="_blank" rel="noreferrer" data-export-url-field="emb_servicetiles_col_2_url">
            <div class="servicetiles-card__panel">
              <div class="servicetiles-card__header">
                <img
                  class="servicetiles-card__icon"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/1is/2t3/zqq/Energieausweiss.png"
                  alt=""
                  width="32"
                  height="32"
                  data-image-field="emb_servicetiles_col_2_icon_url"
                />
              </div>
              <h3 class="servicetiles-card__title" data-export-field="emb_servicetiles_col_2_title">Energieausweis bestellen</h3>
              <p class="module__body servicetiles-card__body" data-export-field="emb_servicetiles_col_2_description">Pflicht f&uuml;r Vermietung &amp; Verkauf</p>
            </div>
          </a>
        </article>
        <article class="servicetiles-card" data-export-item="service-card" data-export-index="3">
          <a class="servicetiles-card__link" href="https://www.immobilienscout24.de/premium-mitgliedschaft-kauf/leistungen/" target="_blank" rel="noreferrer" data-export-url-field="emb_servicetiles_col_3_url">
            <div class="servicetiles-card__panel">
              <div class="servicetiles-card__header">
                <img
                  class="servicetiles-card__icon"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/ak4/08b/dag/mietzahlungs-einkommensnachweis_white.png"
                  alt=""
                  width="32"
                  height="32"
                  data-image-field="emb_servicetiles_col_3_icon_url"
                />
              </div>
              <h3 class="servicetiles-card__title" data-export-field="emb_servicetiles_col_3_title">Suchen+ f&uuml;r Kauf</h3>
              <p class="module__body servicetiles-card__body" data-export-field="emb_servicetiles_col_3_description">Das Plus an Informationen</p>
            </div>
          </a>
        </article>
        <article class="servicetiles-card" data-export-item="service-card" data-export-index="4">
          <a class="servicetiles-card__link" href="https://www.immobilienscout24.de/maklervergleich/" target="_blank" rel="noreferrer" data-export-url-field="emb_servicetiles_col_4_url">
            <div class="servicetiles-card__panel">
              <div class="servicetiles-card__header">
                <img
                  class="servicetiles-card__icon"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/62q/092/p9h/user_tie_white.png"
                  alt=""
                  width="32"
                  height="32"
                  data-image-field="emb_servicetiles_col_4_icon_url"
                />
              </div>
              <h3 class="servicetiles-card__title" data-export-field="emb_servicetiles_col_4_title">Makler finden</h3>
              <p class="module__body servicetiles-card__body" data-export-field="emb_servicetiles_col_4_description">Passenden Profi finden</p>
            </div>
          </a>
        </article>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: steps-3col | SNIPPET: emb_steps_3col -->
<section class="module theme-gray" data-module="steps-3col" data-snippet="emb_steps_3col">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_steps_3col_headline" data-export-role="headline">So starten Sie in drei klaren Schritten</h2>
      </div>
      <div class="steps-grid">
        <article class="step" data-export-item="steps-3col-item" data-export-index="1">
          <div class="step__line"><span class="step__number">1</span></div>
          <p class="module__body" data-export-field="emb_steps_3col_col_1_body" data-export-role="item-body">Definieren Sie Ziel, Timing und die wichtigsten Vermarktungsinhalte für Ihre Mail.</p>
        </article>
        <article class="step" data-export-item="steps-3col-item" data-export-index="2">
          <div class="step__line"><span class="step__number">2</span></div>
          <p class="module__body" data-export-field="emb_steps_3col_col_2_body" data-export-role="item-body">Ordnen Sie Vorteile, Inhalte und CTAs so an, dass der Mehrwert direkt erkennbar ist.</p>
        </article>
        <article class="step" data-export-item="steps-3col-item" data-export-index="3">
          <div class="step__line"><span class="step__number">3</span></div>
          <p class="module__body" data-export-field="emb_steps_3col_col_3_body" data-export-role="item-body">Exportieren Sie den finalen Stand nach Iterable und behalten Sie dieselbe Modulfolge wie in der Preview.</p>
        </article>
      </div>
      <div class="module__cta-row">
        <a class="button-outline-strong" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_steps_3col_button_label" data-export-url-field="emb_steps_3col_button_url" data-export-role="cta">Jetzt starten</a>
      </div>
    </div>
  </div>
</section>



<!-- MODULE: steps-horizontal | SNIPPET: emb_steps_horizontal -->
<section class="module theme-gray" data-module="steps-horizontal" data-snippet="emb_steps_horizontal">
  <div class="module__inner">
    <div class="stack">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_steps_horizontal_headline" data-export-role="headline">Lorem ipsum dolor sit amet</h2>
      </div>
      <div class="steps-vertical">
        <article class="step-vertical" data-export-item="steps-horizontal-item" data-export-index="1">
          <div class="step-vertical__line"><span class="step__number">1</span></div>
          <p class="module__body" data-export-field="emb_steps_horizontal_col_1_body" data-export-role="item-body"><strong>Lorem ipsum dolor.</strong><br />Sit amet, consetetur sadipscing elitr.</p>
        </article>
        <article class="step-vertical" data-export-item="steps-horizontal-item" data-export-index="2">
          <div class="step-vertical__line"><span class="step__number">2</span></div>
          <p class="module__body" data-export-field="emb_steps_horizontal_col_2_body" data-export-role="item-body"><strong>Lorem ipsum dolor.</strong><br />Sit amet, consetetur sadipscing elitr.</p>
        </article>
        <article class="step-vertical" data-export-item="steps-horizontal-item" data-export-index="3">
          <div class="step-vertical__line"><span class="step__number">3</span></div>
          <p class="module__body" data-export-field="emb_steps_horizontal_col_3_body" data-export-role="item-body"><strong>Lorem ipsum dolor.</strong><br />Sit amet, consetetur sadipscing elitr.</p>
        </article>
      </div>
      <div class="module__cta-row">
        <a class="button-outline-strong" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_steps_horizontal_button_label" data-export-url-field="emb_steps_horizontal_button_url" data-export-role="cta">Lorem ipsum</a>
      </div>
    </div>
  </div>
</section>



<!-- MODULE: table | SNIPPET: emb_table -->
<section class="module theme-white" data-module="table" data-snippet="emb_table">
  <div class="module__inner">
    <div class="table-card">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_table_headline" data-export-role="headline">Leistungsüberblick für Ihre Vermarktung</h2>
      </div>
      <table class="data-table" role="presentation">
        <thead>
          <tr>
            <th scope="col" data-export-field="emb_table_col_1_headline">Lorem</th>
            <th scope="col" data-export-field="emb_table_col_2_headline">2024</th>
            <th scope="col" data-export-field="emb_table_col_3_headline">2025</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td data-export-field="emb_table_row_1_col_1_body">Lorem ipsum dolor</td>
            <td data-export-field="emb_table_row_1_col_2_body">+5%</td>
            <td data-export-field="emb_table_row_1_col_3_body">+8%</td>
          </tr>
          <tr>
            <td data-export-field="emb_table_row_2_col_1_body">Lorem ipsum dolor</td>
            <td data-export-field="emb_table_row_2_col_2_body">-2%</td>
            <td data-export-field="emb_table_row_2_col_3_body">+5%</td>
          </tr>
          <tr>
            <td data-export-field="emb_table_row_3_col_1_body">Lorem ipsum dolor</td>
            <td data-export-field="emb_table_row_3_col_2_body">+8%</td>
            <td data-export-field="emb_table_row_3_col_3_body">-2%</td>
          </tr>
        </tbody>
      </table>
      <div class="module__cta-row">
        <a class="button-outline-strong" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_table_button_label" data-export-url-field="emb_table_button_url" data-export-role="cta">Pakete vergleichen</a>
      </div>
    </div>
  </div>
</section>



<!-- MODULE: table-comparison | SNIPPET: emb_table_comparison -->
<section class="module theme-white" data-module="table-comparison" data-snippet="emb_table_comparison">
  <div class="module__inner">
    <div class="table-card">
      <div class="module__head">
        <h2 class="module__title module__title--medium" data-export-field="emb_table_comparison_headline" data-export-role="headline">Zwei Wege im direkten Vergleich</h2>
      </div>
      <div class="comparison-grid">
        <section class="comparison-column" data-export-item="table-comparison-column" data-export-index="1">
          <h3 class="module__title module__title--small" data-export-field="emb_table_comparison_col_1_headline">Selbst organisieren</h3>
          <div class="comparison-column__rule" aria-hidden="true"></div>
          <div class="comparison-list">
            <p class="comparison-item" data-export-field="emb_table_comparison_row_1_col_1_body" data-export-index="1">Sie koordinieren Inhalte, Rückfragen und Freigaben manuell.</p>
            <p class="comparison-item" data-export-field="emb_table_comparison_row_2_col_1_body" data-export-index="2">Status und Resonanz müssen über mehrere Kanäle zusammengeführt werden.</p>
            <p class="comparison-item" data-export-field="emb_table_comparison_row_3_col_1_body" data-export-index="3">Anpassungen kosten mehr Abstimmung im laufenden Prozess.</p>
          </div>
        </section>
        <section class="comparison-column" data-export-item="table-comparison-column" data-export-index="2">
          <h3 class="module__title module__title--small" data-export-field="emb_table_comparison_col_2_headline">Digital begleitet</h3>
          <div class="comparison-column__rule" aria-hidden="true"></div>
          <div class="comparison-list">
            <p class="comparison-item" data-export-field="emb_table_comparison_row_1_col_2_body" data-export-index="1">Sie behalten Inhalte, Sichtbarkeit und Reaktionen in einem Ablauf im Blick.</p>
            <p class="comparison-item" data-export-field="emb_table_comparison_row_2_col_2_body" data-export-index="2">Resonanz und nächste Schritte bleiben für alle Beteiligten nachvollziehbar.</p>
            <p class="comparison-item" data-export-field="emb_table_comparison_row_3_col_2_body" data-export-index="3">Optimierungen lassen sich schneller und klarer in die Mail übernehmen.</p>
          </div>
        </section>
      </div>
      <div class="module__cta-row">
        <a class="button-outline-strong" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_table_comparison_button_label" data-export-url-field="emb_table_comparison_button_url" data-export-role="cta">Beratung anfragen</a>
      </div>
    </div>
  </div>
</section>



<!-- MODULE: contact | SNIPPET: emb_contact -->
<section class="module theme-white" data-module="contact" data-snippet="emb_contact">
  <div class="module__inner">
    <div class="contact-card">
      <span class="is-hidden" data-export-field="emb_contact_show_image" data-export-role="technical-flag">false</span>
      <div class="contact-head">
        <div class="contact-media">
          <div
            class="preview-image-placeholder preview-image-placeholder--contact-avatar"
            data-image-field="emb_contact_image_url"
            data-image-alt-field="emb_contact_image_alt"
          >
            <div class="preview-image-placeholder__text">
              <p class="preview-image-placeholder__meta">104 x 104 px</p>
            </div>
          </div>
        </div>
        <div class="contact-head__copy">
          <h2 class="module__title module__title--medium" data-export-field="emb_contact_headline" data-export-role="headline">Wir sind für Sie da</h2>
          <p class="module__body" data-export-field="emb_contact_body_intro" data-export-role="intro">Sie möchten Ihre Mail oder Ihren Builder-Stand gemeinsam schärfen? Unser Team unterstützt Sie gern beim nächsten Schritt.</p>
        </div>
      </div>
      <div class="contact-copy">
        <p class="contact-phone" data-export-field="emb_contact_phone" data-export-role="phone">030 12345678</p>
        <p class="module__body" data-export-field="emb_contact_phone_hours" data-export-role="phone-hours">Montag bis Freitag, 9 bis 18 Uhr</p>
        <p class="module__body" data-export-field="emb_contact_email_intro" data-export-role="email-intro">Oder schreiben Sie uns direkt per E-Mail:</p>
        <p class="module__body"><a class="contact-link" href="mailto:beratung@immobilienscout24.de" data-export-field="emb_contact_email_address" data-export-url-field="emb_contact_email_url" data-export-role="email-link">beratung@immobilienscout24.de</a></p>
        <p class="contact-signoff"><span data-export-field="emb_contact_closing_line_1" data-export-role="closing-line" data-export-index="1">Viele Grüße</span><br><span data-export-field="emb_contact_closing_line_2" data-export-role="closing-line" data-export-index="2">Ihr Builder-Team</span></p>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: contact-signoff | SNIPPET: emb_contact_signoff -->
<section class="module theme-white" data-module="contact-signoff" data-snippet="emb_contact_signoff">
  <div class="module__inner">
    <div class="contact-card">
      <div class="contact-copy">
        <p class="contact-signoff">Freundliche Grüße<br />Ihr ImmoScout24-Team</p>
      </div>
    </div>
  </div>
</section>


<!-- MODULE: footer | SNIPPET: emb_footer_marketing -->
<footer class="module theme-white" data-module="footer" data-snippet="emb_footer_marketing">
  <div class="module__inner module__inner--compact">
    <div class="footer-marketing">
      <p class="footer-marketing__headline">Kostenlose App herunterladen</p>
      <div class="footer-marketing__badges">
        <a class="footer-badge" href="https://itunes.apple.com/de/app/immobilienscout24/id342157367?mt=8" target="_blank" rel="noreferrer">
          <img
            class="footer-badge__image"
            src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/i36/uhu/m14/d1284a48-db27-4f3b-a434-ab9a625d0dd4.png"
            alt="Download on the App Store"
            width="115"
            height="37"
          />
        </a>
        <a class="footer-badge" href="https://play.google.com/store/apps/details?id=de.is24.android&hl=de" target="_blank" rel="noreferrer">
          <img
            class="footer-badge__image"
            src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/nrd/s3d/49k/b78e3fcd-6303-429c-a29d-691d73c0d01d.png"
            alt="Get it on Google Play"
            width="130"
            height="37"
          />
        </a>
      </div>
      <div class="footer-marketing__copy">
        <p class="footer-marketing__text">ImmoScout24 informiert ueber Aktuelles aus der Immobilienwelt. Wenn kein Interesse mehr besteht, ist es moeglich, sich <a href="#" target="_blank" rel="noreferrer">hier abzumelden</a>. Die Abmeldung betrifft nicht gegebenenfalls bestehende Suchauftragsbenachrichtigungen.</p>
        <p class="footer-marketing__text">Immobilien Scout GmbH - Ein Unternehmen der Scout24-Gruppe, Invalidenstr. 65, 10557 Berlin · <a class="footer-marketing__plain-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer">immobilienscout24.de</a> · Geschaeftsfuehrung: Dr. Gesa Crockford, Daniel Hendel · Vorsitzender des Aufsichtsrats: Ralf Weitz · Handelsregister: Amtsgericht Charlottenburg, HRB 69108 · Sitz der Gesellschaft: Berlin · USt-IdNr. DE200269419</p>
        <p class="footer-marketing__links">
          <a href="https://www.immobilienscout24.de/agb/datenschutz.html" target="_blank" rel="noreferrer">Datenschutz</a><span class="footer-marketing__links-separator">|</span><a href="https://www.immobilienscout24.de/impressum.html" target="_blank" rel="noreferrer">Impressum</a>
        </p>
        <p class="footer-marketing__text">&copy; 1999 - 2026 Immobilien Scout GmbH</p>
      </div>
    </div>
  </div>
</footer>
```

## email-builder/agent/icon-library.md

Dateityp: md

```md
# Purpose

Builder-interne Single Source of Truth fuer erlaubte Benefit-Icons im E-Mail Builder.

# Usage

- Diese Datei ist eine reine Datenquelle.
- Keine Renderlogik.
- Keine freie Auswahl- oder Renderlogik ausserhalb des hier definierten kanonischen Fallbacks.
- Keine HTML-Ausgabe.
- Erlaubte Icon-URLs duerfen nur aus dieser Datei kommen.
- Operativ wird diese Datei aktuell nur fuer `benefits-3col` verwendet.

# Canonical Fallback

- Wenn kein Bucket klar passt, nutze `icon-11` aus `general-positive` als kanonischen neutralen Fallback.
- Fallback-URL: `https://www.static-immobilienscout24.de/fro/emb/_/s24_checkmark_circle_48.png`

# Buckets

- `security-trust`: Sicherheit, Vertrauen, gepruefte Qualitaet
- `general-positive`: allgemeiner Vorteil, neutraler positiver Fallback
- `price-saving`: Preis, Sparen, transparente Kosten
- `speed-process`: Geschwindigkeit, effizienter Ablauf, strukturierter Prozess
- `performance-success`: Leistung, Sichtbarkeit, Erfolg
- `expertise-advice`: Fachwissen, Beratung, professionelle Begleitung
- `communication-service`: Kontakt, Betreuung, Service, Kommunikation
- `reach-location`: Reichweite, Lage, Zielerreichung
- `home-property`: Immobilie, Zuhause, Objektbezug
- `target-group`: Nutzerinnen, Nutzer, Zielgruppe
- `documents-contract`: Unterlagen, Dokumente, Vertrag
- `calendar-time`: Termin, Planung, Zeit
- `support-clarity`: Hilfe, Orientierung, Klarheit
- `digital-comfort`: digitale, komfortable Abwicklung

# Icons

## security-trust

- `icon-09`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_shield_checkmark_48.png`
  - meaning: `Sicherheit und gepruefte Anbieter`
- `icon-17`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_lock_close_48.png`
  - meaning: `Sicherheit und Schutz`
- `icon-18`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_user_tie_48.png`
  - meaning: `Vertrauensvolle Begleitung`

## general-positive

- `icon-10`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_smiley_positive_48.png`
  - meaning: `Allgemeiner positiver Vorteil`
- `icon-11`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_checkmark_circle_48.png`
  - meaning: `Allgemeiner Vorteil bestaetigt`
- `icon-12`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_thump_up_48.png`
  - meaning: `Positiver Servicevorteil`
- `icon-13`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_checkmark_48.png`
  - meaning: `Allgemeiner Nutzen`
- `icon-38`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_checkmark_48.png`
  - meaning: `Allgemeiner Vorteil`
- `icon-39`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_smiley_positive_48.png`
  - meaning: `Allgemeiner Servicevorteil`

## price-saving

- `icon-14`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_piggy_bank_48.png`
  - meaning: `Sparvorteil`
- `icon-15`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_euro_circle_48.png`
  - meaning: `Preisvorteile`
- `icon-16`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_plus_nebenkosten_check_48.png`
  - meaning: `Transparente Kosten`

## speed-process

- `icon-19`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_stopwatch_48.png`
  - meaning: `Schneller Ablauf`
- `icon-20`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_arrows_cycle_48.png`
  - meaning: `Strukturierter Prozess`
- `icon-21`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_timer_48.png`
  - meaning: `Zuegiger Abschluss`

## performance-success

- `icon-22`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_chart_48.png`
  - meaning: `Starke Performance`
- `icon-23`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_chart_bars_vertical_48.png`
  - meaning: `Mehr Sichtbarkeit`
- `icon-24`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_thump_up_48.png`
  - meaning: `Erfolgreiche Vermarktung`

## expertise-advice

- `icon-25`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_user_tie_48.png`
  - meaning: `Fachkundige Beratung`
- `icon-26`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_user_checkmark_48.png`
  - meaning: `Professionelle Unterstuetzung`

## communication-service

- `icon-27`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_chat_bubble_2_48.png`
  - meaning: `Kommunikation und Kontakt`
- `icon-28`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_user_tie_48.png`
  - meaning: `Persoenliche Betreuung`
- `icon-42`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_letter_sent_48.png`
  - meaning: `E-Mail-Kommunikation`

## reach-location

- `icon-29`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_location_pin_2_48.png`
  - meaning: `Immobilie und Lage`
- `icon-30`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_users_three_48.png`
  - meaning: `Reichweite und Zielgruppen`

## home-property

- `icon-41`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_map_magnifier_48.png`
  - meaning: `Immobilie und Zuhause`

## target-group

- `icon-43`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_users_three_48.png`
  - meaning: `Zielgruppen und Nutzerinnen`

## documents-contract

- `icon-31`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_document_check_48.png`
  - meaning: `Unterlagen und Dokumente`
- `icon-32`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_document_lock_48.png`
  - meaning: `Vertrag und Vereinbarungen`
- `icon-33`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_document_pdf_48.png`
  - meaning: `Dokumente und Formulare`

## calendar-time

- `icon-34`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_calendar_checkmark_48.png`
  - meaning: `Termin und Planung`
- `icon-35`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_timer_48.png`
  - meaning: `Schnelle Terminprozesse`

## support-clarity

- `icon-36`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_lightbulb_48.png`
  - meaning: `Hilfe und Unterstuetzung`

## digital-comfort

- `icon-40`
  - url: `https://www.static-immobilienscout24.de/fro/emb/_/s24_arrows_cycle_48.png`
  - meaning: `Digitale und komfortable Abwicklung`
```

## email-builder/agent/tone-of-voice.md

Dateityp: md

```md
# Tone Of Voice

## Grundhaltung

- Prinzip ist `health selling` statt `hard selling`.
- Ueberzeugen durch Klarheit, Nutzen und Vertrauen.
- Kein Druckaufbau.
- Keine kuenstliche Verknappung.
- Keine aggressive Verkaufssprache.
- Fokus auf Mehrwert, Orientierung und Kompetenz.

## Sprachpersoenlichkeit

- Wir sind klar, positiv, kompetent, nahbar, loesungsorientiert, strukturiert und vertrauenswuerdig.
- Wir sind nicht laut, reisserisch, uebertrieben emotional, kompliziert, marketing-getrieben, belehrend oder arrogant.

## Stilregeln

- Kurze bis mittellange Saetze.
- Aktiv statt Passiv.
- Konkrete Aussagen statt vager Formulierungen.
- Keine unnoetig verschachtelten Konstruktionen.
- Verstaendliche Alltagssprache.
- Fachbegriffe nur, wenn notwendig.
- Keine Buzzwords.
- Keine leeren Versprechen.
- Keine unbelegten Superlative.
- Keine unnoetigen Fuellwoerter.
- Positiv, aber kontrolliert.
- Keine Dramatisierung.

## Zielgruppen-Ansprache

### Seeker

- Konsequente Du-Form verwenden, zum Beispiel `Du` und `Dein`.
- Tonalitaet ist nahbar, klar und unterstuetzend.

### Homeowner

- Konsequente Du-Form verwenden, zum Beispiel `Du` und `Dein`.
- Tonalitaet ist persoenlich, verbindlich und partnerschaftlich.

### Agents

- Konsequente Sie-Form verwenden, zum Beispiel `Sie` und `Ihr`.
- Tonalitaet ist sachlich, kompetent und nutzenorientiert.

### System-Default

- Bei Zielgruppe `Seeker` ist die Du-Form zu erzwingen.
- Bei Zielgruppe `Homeowner` ist die Du-Form zu erzwingen.
- Bei Zielgruppe `Agents` ist die Sie-Form zu erzwingen.
- Wenn keine Zielgruppe definiert ist, darf nur ein expliziter Fallback greifen; bevorzugt wird dann die Sie-Form.

## Do Und Don't

- Do: konkreter Nutzen, klare Aussagen, transparente Argumentation, relevante Beispiele, strukturierte Absaetze.
- Don't: `Jetzt zugreifen!`, `Unglaublich`, `Revolutionaer`, `Einmalige Chance`, `Verpassen Sie nicht`, reine Behauptungen ohne Substanz oder Druck durch kuenstliche Verknappung.

## Gender Und Inklusion

- Geschlechtergerechte Sprache verwenden.
- Wenn moeglich neutral formulieren.
- Doppelpunkt-Form nur bei projektspezifischer Vorgabe.

## Schreibweisen

### Marke

- Bevorzugt `ImmoScout24`.
- Ebenfalls korrekt `ImmobilienScout24`.
- Innerhalb eines Textes einheitlich bleiben.
- Nicht verwenden: `ImmoScout`, `Immobilienscout`, `IS24`.

### Umlaute

- Deutsche Umlaute im finalen Text immer korrekt schreiben.
- Im generierten deutschen Mail-Content duerfen nur `ä`, `ö`, `ü`, `Ä`, `Ö`, `Ü` und `ß` verwendet werden.
- Umschreibungen wie `ae`, `oe`, `ue`, `Ae`, `Oe`, `Ue` oder `ss` sind im normalen deutschen Fliesstext nicht zulaessig.
- Ausnahmen sind nur erlaubt, wenn die Schreibweise Teil eines echten Eigennamens, einer URL, einer E-Mail-Adresse oder eines technischen Werts ist.

### Zahlen

- Zahlen `1` bis `12` als Woerter, ab `13` als Ziffern.
- Bei fachlichen Angaben immer Ziffern.
- Gruppen von drei Ziffern mit Punkt trennen, zum Beispiel `1.250.000`.

### Masseinheiten

- Leerzeichen zwischen Zahl und Masseinheit, zum Beispiel `10 km/h`.
- Im Fliesstext `Quadratmeter` ausschreiben.
- In technischen Angaben `m²` verwenden, wenn keine projektspezifische Abweichung definiert ist.

### Waehrungen

- Bevorzugt das Waehrungssymbol vor dem Betrag verwenden, zum Beispiel `€250`.
- Kein Leerzeichen zwischen Waehrungssymbol und Betrag.
- Gruppen von drei Ziffern mit Punkt trennen, zum Beispiel `€250.000`.
- Innerhalb eines Textes einheitlich bleiben, entweder `Euro` oder `€`.

### Datum Und Zeit

- Datumsformat `DD.MM.YYYY` oder `D. Monat YYYY`.
- Uhrzeiten mit Doppelpunkt schreiben.
- Nach Uhrzeiten folgt `Uhr`.
- Fuer Zeitspannen den Halbgeviertstrich verwenden, zum Beispiel `7:00–11:00 Uhr`.

## Builder-Constraints

- Keine aggressive Verkaufssprache.
- Keine kuenstliche Verknappung.
- Keine unbelegten Superlative.
- Keine Buzzwords.
- Nutzen vor Produktbeschreibung.
- Kurze, klar strukturierte Absaetze.
- Pro Modul ein klarer inhaltlicher Fokus statt Landingpage-Langform.
- Betreffzeilen, Headlines, Bodytexte und CTA-Texte folgen denselben Tonregeln.
- Zielgruppen-Ansprache strikt einhalten: `Seeker` und `Homeowner` immer Du, `Agents` immer Sie.
```

## email-builder/agent/content-rules.md

Dateityp: md

```md
# Content Rules

## Zweck

- Diese Datei sammelt inhaltliche Regeln fuer die Content-Erstellung im EMB.
- Sie ergaenzt `guardrails.md` um Content-spezifische Layout-, Balance- und Textvorgaben.
- Technische Struktur-, Preview- und Exportregeln bleiben in `guardrails.md`.
- Sprachstil, Ansprache und Schreibweisen bleiben in `tone-of-voice.md`.

## Allgemeine Content-Regeln

- Sichtbarer Mail-Content fuer Preview und Iterable-Export ist standardmaessig Deutsch, wenn der User keine andere Mail-Sprache ausdruecklich verlangt.
- Englische Arbeitsanweisungen oder Tool-Begriffe allein sind kein Sprachsignal fuer englischen Mail-Content.
- Inhalte muessen pro Modul klar fokussiert und leicht erfassbar bleiben.
- Ein Modul soll keine Landingpage-Langform werden.
- Pflichtinhalte duerfen nicht leer, sinnlos oder rein generisch sein.

## Salutation-Kontext

- Die zentrale Registry fuer Anrede-Zuordnungen ist `agent/product-salutations.json`.
- `salutationContext` ist ein technischer Resolver fuer Anrede-Logik und kein sichtbares User-Textfeld.
- Wenn ein aktives Composition-Template eine `salutation_context_id` traegt, wird dieser Kontext automatisch gesetzt; es ist keine Rueckfrage noetig.
- Wenn der User explizit `Mail fuer RLE`, `Loft SNL` oder `Loft RNL` sagt, muss der EMB die Zuordnung ueber `aliases` oder `template_ids` der Registry ohne unnoetige Rueckfrage aufloesen.
- Wenn beim freien Initialstart kein Team, Produkt oder Kontext erkennbar ist, gilt ohne Rueckfrage `salutationContext = generic`.
- Sichtbare Preview-Anreden muessen menschenlesbar bleiben; Raw-Handlebars, freie Snippetcalls oder freie Iterable-Logik im User-Content bleiben verboten.
- Fuer `salutationContext = loft-rnl-dev` bleibt die sichtbare Intro-Anrede im Builder `Hallo Anrede`; der produktive Handlebars-Ausdruck ist ein kontrollierter Exportwert und kein editierbarer User-Text.

## Produktkontext

- Produktdefaults duerfen nur aus den dokumentierten Resolver-Regeln in `builder-library.md` kommen.
- Aktuell ist nur der Produktkontext `RLE` fuer zusaetzliche Inhaltsdefaults erlaubt; andere Registry-Kontexte aktivieren keine weiteren Produktdefaults.
- Wenn der User einen unbekannten expliziten Produktnamen nennt, muss der Agent nachfragen statt zu raten.
- Produktdefaults sind Start-Defaults und nie staerker als explizite spaetere User-Vorgaben fuer konkrete Felder.
- Wenn `RLE` aktiv ist und der User keine abweichenden Contact-Werte vorgibt, muessen fuer das `contact`-Modul exakt die dokumentierten RLE-Defaults aus `builder-library.md` verwendet werden.
- Das `contact`-Modul ist immer weiss und hat kein usersteuerbares oder alternierendes Background-Feld.
- Wenn `RLE` aktiv ist, darf der Hero-Salutation-Snippetcall nur ueber die dokumentierten technischen Export-Flags `*_use_snippetcall_salutation` aktiviert werden.
- Freie User-Snippetcalls, freie Raw-Logik oder freier HTML-Code in Hero-Salutations bleiben verboten.

## Servicetiles

- Das spaetere Modul `servicetiles` nutzt `agent/service-products.json` als einzige zentrale Produktquelle.
- User nennen fuer `servicetiles` fachlich genau `4` Services.
- Die Aufloesung erfolgt nur ueber `id` oder `aliases` der Registry.
- Wenn weniger oder mehr als `4` Services genannt werden, muss der Agent nachfragen.
- Wenn ein Service unbekannt ist oder nicht eindeutig aufloesbar ist, darf der Agent nicht raten.
- User sehen im regulaeren EMB-Flow keine Iterable-Snippetnamen.

## Hero

- Im Hero ist nur eines von beiden erlaubt: `eyebrow` oder `badge`.
- `eyebrow` und `badge` duerfen nie gleichzeitig sichtbar sein.
- Wenn der User fuer ein Hero-Modul ein Badge verlangt, muss eine vorhandene `eyebrow` ausgeblendet werden.
- Wenn der User fuer ein Hero-Modul eine `eyebrow` verlangt, muss ein vorhandenes Badge ausgeblendet werden.

## CTA-Buttons

- Pro Mail ist genau ein primaerer `button-filled-brand` vorgesehen.
- Wenn ein Hero-Modul einen Button-CTA hat, ist dieser Hero-CTA immer der primaere `button-filled-brand`.
- Weitere Button-CTAs in derselben Mail muessen auf andere erlaubte Button-Typen ausweichen.
- Fuer Nicht-Hero-Button-CTAs bleibt der Preview-Standard `button-outline-strong`.
- Wenn eine Mail ausnahmsweise keinen Hero-Button hat, darf stattdessen genau ein anderer primaerer CTA `button-filled-brand` sein.

## Mehrspaltige Module

- Bei Modulen mit `2` oder `3` nebeneinanderstehenden Spalten sollen die Textmengen pro Spalte moeglichst aehnlich lang sein.
- Exakte Zeichengleichheit ist nicht noetig, aber starke Laengenunterschiede sind zu vermeiden.
- Das Ziel ist ein ruhiges, visuell ausgewogenes Layout.

## Benefits-3col

- Die drei Benefit-Texte sollen moeglichst aehnliche Textmengen haben.
- Es darf keine deutlich ueberladene Einzelspalte neben zwei sehr kurzen Spalten geben.
- Unterschiede sind erlaubt, solange das Modul visuell ausgewogen bleibt.

## Table-Comparison

- Fuer `table-comparison` gilt eine strengere Balance-Regel als fuer andere Mehrspalter.
- Beide Spalten-Headlines sollen in ihrer Laenge so nah beieinander liegen, dass sie moeglichst gleich viele Zeilen einnehmen.
- Es soll vermieden werden, dass eine Spalten-Headline einzeilig und die andere zweizeilig ist.
- Inhalte desselben Zeilenpaars links und rechts sollen moeglichst aehnlich lang sein.
- Es soll vermieden werden, dass eine Zelle eines Zeilenpaars sehr kurz und die gegenueberliegende Zelle deutlich laenger ist.
- Ziel ist, dass beide Vergleichsspalten visuell synchron und direkt vergleichbar bleiben.
```

## email-builder/email/templates/template-main.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <title>E-Mail Builder | Template Main</title>
  <!--[if mso]>
  <xml>
    <w:WordDocument xmlns:w="urn:schemas-microsoft-com:office:word"><w:DontUseAdvancedTypographyReadingMail/></w:WordDocument>
    <o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings>
  </xml>
  <![endif]-->
  <link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/make-it-better/1.0.0/makeitbetter.css">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; padding: 0; }
    a[x-apple-data-detectors] { color: inherit !important; text-decoration: inherit !important; }
    #MessageViewBody a { color: inherit; text-decoration: none; }
    p { line-height: inherit; }
    .desktop_hide, .desktop_hide table { mso-hide: all; display: none; max-height: 0px; overflow: hidden; }
    .module-rich-full-body--hero {
      display: grid;
      gap: 0;
    }
    .module-rich-full-body--hero-image-textbox-cta-center {
      display: grid;
      gap: 0;
    }
    .module-rich-full-body--hero-image-textbox-cta-center > * + * {
      margin-top: 16px;
    }
    .module-rich-full-body--hero-image-textbox-cta-center > p:first-child + * {
      margin-top: 8px;
    }
    .module-rich-full-body--hero p,
    .module-rich-full-body--hero ul,
    .module-rich-full-body--hero ol {
      margin: 0;
    }
    .module-rich-full-body--hero p + p {
      margin-top: 16px;
    }
    .module-rich-full-body--hero p + ul,
    .module-rich-full-body--hero p + ol,
    .module-rich-full-body--hero ul + p,
    .module-rich-full-body--hero ul + ul,
    .module-rich-full-body--hero ul + ol,
    .module-rich-full-body--hero ol + p,
    .module-rich-full-body--hero ol + ul,
    .module-rich-full-body--hero ol + ol {
      margin-top: 8px;
    }
    .module-rich-full-body--hero-image-textbox-cta-center p,
    .module-rich-full-body--hero-image-textbox-cta-center ul,
    .module-rich-full-body--hero-image-textbox-cta-center ol {
      margin: 0;
    }
    .module-rich-full-body--hero ul,
    .module-rich-full-body--hero ol {
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--hero li {
      margin: 0 0 4px;
    }
    .module-rich-full-body--hero li:last-child {
      margin-bottom: 0;
    }
    .module-rich-full-body--hero-image-textbox-cta-center ul,
    .module-rich-full-body--hero-image-textbox-cta-center ol {
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--teaser-1col p {
      margin: 0;
    }
    .module-rich-full-body--teaser-1col ul,
    .module-rich-full-body--teaser-1col ol {
      margin: 0;
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--teaser-1col p + ul,
    .module-rich-full-body--teaser-1col p + ol,
    .module-rich-full-body--teaser-1col ul + p,
    .module-rich-full-body--teaser-1col ul + ul,
    .module-rich-full-body--teaser-1col ul + ol,
    .module-rich-full-body--teaser-1col ol + p,
    .module-rich-full-body--teaser-1col ol + ul,
    .module-rich-full-body--teaser-1col ol + ol {
      margin-top: 8px;
    }
    .module-rich-full-body--teaser-1col p + p {
      margin-top: 16px;
    }
    .module-rich-full-body--teaser-1col li {
      margin: 0 0 4px;
    }
    .module-rich-full-body--teaser-1col li:last-child {
      margin-bottom: 0;
    }
    @media (max-width:620px) {
      .row-content { width: 100% !important; }
      .stack .column { width: 100% !important; display: block !important; }
      .desktop_hide, .desktop_hide table { display: table !important; max-height: none !important; }
      .mobile_hide { display: none !important; min-height: 0; max-height: 0; max-width: 0; overflow: hidden; font-size: 0px; }
      .font-heading-large-bold { font-size: 28px !important; line-height: 36px !important; }
      .font-heading-medium-regular,
      .font-heading-medium-bold { font-size: 24px !important; line-height: 34px !important; }
      .font-heading-small-regular,
      .font-heading-small-bold { font-size: 20px !important; line-height: 30px !important; }
      .module-12-heading h1 { font-size: 28px !important; line-height: 36px !important; }
      .module-block[data-module="hero-image-top"] .module-12-heading h1.hero-headline-size-s,
      .module-block[data-module="hero-image-top-center"] .module-12-heading h1.hero-headline-size-s { font-size: 20px !important; line-height: 30px !important; }
      .module-block[data-module="hero-image-top"] .module-12-heading h1.hero-headline-size-m,
      .module-block[data-module="hero-image-top-center"] .module-12-heading h1.hero-headline-size-m { font-size: 24px !important; line-height: 34px !important; }
      .module-block[data-module="hero-image-top"] .module-12-heading h1.hero-headline-size-l,
      .module-block[data-module="hero-image-top-center"] .module-12-heading h1.hero-headline-size-l { font-size: 28px !important; line-height: 36px !important; }
      .module-block[data-module="hero-image-top-bleed"] .module-12-heading h1.hero-headline-size-s,
      .module-block[data-module="hero-image-top-bleed-center"] .module-12-heading h1.hero-headline-size-s,
      .module-block[data-module="hero-button-top"] .module-12-no-bottom-heading h1.hero-headline-size-s,
      .module-block[data-module="hero-cta-top-center"] .module-12-no-bottom-heading h1.hero-headline-size-s,
      .module-block[data-module="hero-button-top-no-bottom"] .module-12-no-bottom-heading h1.hero-headline-size-s,
      .module-block[data-module="hero-cta-top-no-bottom-center"] .module-12-no-bottom-heading h1.hero-headline-size-s { font-size: 20px !important; line-height: 30px !important; }
      .module-block[data-module="hero-image-top-bleed"] .module-12-heading h1.hero-headline-size-m,
      .module-block[data-module="hero-image-top-bleed-center"] .module-12-heading h1.hero-headline-size-m,
      .module-block[data-module="hero-button-top"] .module-12-no-bottom-heading h1.hero-headline-size-m,
      .module-block[data-module="hero-cta-top-center"] .module-12-no-bottom-heading h1.hero-headline-size-m,
      .module-block[data-module="hero-button-top-no-bottom"] .module-12-no-bottom-heading h1.hero-headline-size-m,
      .module-block[data-module="hero-cta-top-no-bottom-center"] .module-12-no-bottom-heading h1.hero-headline-size-m { font-size: 24px !important; line-height: 34px !important; }
      .module-block[data-module="hero-image-top-bleed"] .module-12-heading h1.hero-headline-size-l,
      .module-block[data-module="hero-image-top-bleed-center"] .module-12-heading h1.hero-headline-size-l,
      .module-block[data-module="hero-button-top"] .module-12-no-bottom-heading h1.hero-headline-size-l,
      .module-block[data-module="hero-cta-top-center"] .module-12-no-bottom-heading h1.hero-headline-size-l,
      .module-block[data-module="hero-button-top-no-bottom"] .module-12-no-bottom-heading h1.hero-headline-size-l,
      .module-block[data-module="hero-cta-top-no-bottom-center"] .module-12-no-bottom-heading h1.hero-headline-size-l { font-size: 28px !important; line-height: 36px !important; }
      .module-block[data-module="hero-image-textbox-cta-center"] .module-12-heading h1.hero-headline-size-s { font-size: 20px !important; line-height: 30px !important; }
      .module-block[data-module="hero-image-textbox-cta-center"] .module-12-heading h1.hero-headline-size-m { font-size: 24px !important; line-height: 34px !important; }
      .module-block[data-module="hero-image-textbox-cta-center"] .module-12-heading h1.hero-headline-size-l { font-size: 28px !important; line-height: 36px !important; }
      .module-block[data-module="hero-image-head-copy-bleed-center"] .module-12-heading h1.hero-headline-size-s { font-size: 20px !important; line-height: 30px !important; }
      .module-block[data-module="hero-image-head-copy-bleed-center"] .module-12-heading h1.hero-headline-size-m { font-size: 24px !important; line-height: 34px !important; }
      .module-block[data-module="hero-image-head-copy-bleed-center"] .module-12-heading h1.hero-headline-size-l { font-size: 28px !important; line-height: 36px !important; }
      .module-12-head-pad { padding: 24px 20px 0 !important; }
      .module-12-body-pad { padding: 12px 20px 0 !important; }
      .module-hero-variant-body-pad { padding: 12px 20px 40px !important; }
      .module-block[data-module="hero-image-top"] .module-12-head-pad,
      .module-block[data-module="hero-image-top-center"] .module-12-head-pad,
      .module-block[data-module="hero-image-textbox-cta-center"] .module-12-head-pad { padding: 40px 20px 0 !important; }
      .module-block[data-module="hero-image-top"] .module-12-body-pad.module-hero-variant-body-pad,
      .module-block[data-module="hero-image-top-center"] .module-12-body-pad.module-hero-variant-body-pad,
      .module-block[data-module="hero-button-top"] .module-12-body-pad.module-hero-variant-body-pad,
      .module-block[data-module="hero-cta-top-center"] .module-12-body-pad.module-hero-variant-body-pad,
      .module-block[data-module="hero-image-textbox-cta-center"] .module-hero-variant-body-pad { padding: 20px 20px 40px !important; }
      .module-teaser-1col-body-pad { padding: 12px 20px 40px !important; }
      .module-teaser-1col-body-pad-spaced { padding: 24px 20px 40px !important; }
      .module-12-no-bottom-heading h1 { font-size: 28px !important; line-height: 36px !important; }
      .module-12-no-bottom-head-pad { padding: 24px 20px 0 !important; }
      .module-12-no-bottom-body-pad { padding: 12px 20px 0 !important; }
      .module-block[data-module="hero-button-top"] .module-12-no-bottom-head-pad,
      .module-block[data-module="hero-cta-top-center"] .module-12-no-bottom-head-pad,
      .module-block[data-module="hero-button-top-no-bottom"] .module-12-no-bottom-head-pad,
      .module-block[data-module="hero-cta-top-no-bottom-center"] .module-12-no-bottom-head-pad { padding: 40px 20px 0 !important; }
      .module-block[data-module="hero-button-top-no-bottom"] .module-12-no-bottom-body-pad,
      .module-block[data-module="hero-cta-top-no-bottom-center"] .module-12-no-bottom-body-pad { padding: 20px 20px 0 !important; }
      .module-12-bleed-heading h1 { font-size: 24px !important; line-height: 34px !important; }
      .module-12-bleed-head-pad { padding: 40px 20px 0 !important; }
      .module-12-bleed-image-pad { padding: 24px 0 0 !important; }
      .module-block[data-module="hero-image-head-copy-bleed-center"] .module-12-bleed-image-pad { padding-top: 20px !important; }
      .module-12-bleed-text-pad { padding: 24px 20px 40px !important; }
      .module-block[data-module="hero-image-head-copy-bleed-center"] .module-12-bleed-text-pad { padding-top: 0 !important; }
      .module-hero-variant-bleed-text-pad { padding: 24px 20px 40px !important; }
      .module-hero-spacer-25 { height: 24px !important; line-height: 24px !important; font-size: 24px !important; }
      .module-hero-spacer-35 { height: 30px !important; line-height: 30px !important; font-size: 30px !important; }
      .module-hero-spacer-button { height: 24px !important; line-height: 24px !important; font-size: 24px !important; }
      .module-logo-pad { padding: 24px 20px 0 !important; }
      .module-6-6-vertical-heading h1 { font-size: 24px !important; line-height: 34px !important; }
      .module-6-6-vertical-head-pad { padding: 40px 20px 0 !important; }
      .module-6-6-vertical-col-1-pad { padding: 24px 20px 32px !important; }
      .module-6-6-vertical-col-2-pad { padding: 0 20px 40px !important; }
      .module-6-6-vertical-image-pad { padding: 0 !important; }
      .module-6-6-horizontal-row-1-image-pad { padding: 40px 20px 24px !important; }
      .module-6-6-horizontal-row-1-text-pad { padding: 0 20px 32px !important; }
      .module-6-6-horizontal-row-mid-image-pad { padding: 0 20px 24px !important; }
      .module-6-6-horizontal-row-mid-text-pad { padding: 0 20px 32px !important; }
      .module-6-6-horizontal-row-2-image-pad { padding: 0 20px 24px !important; }
      .module-6-6-horizontal-row-2-text-pad { padding: 0 20px 40px !important; }
      .module-6-6-horizontal-image-pad { padding: 0 !important; }
      .module-6-6-horizontal-heading h1 { font-size: 24px !important; line-height: 34px !important; }
      .module-6-6-horizontal-head-pad { padding: 40px 20px 0 !important; }
      .module-6-6-alternating-head-pad { padding: 40px 20px 0 !important; }
      .module-6-6-alternating-row-1-image-pad { padding: 40px 20px 24px !important; }
      .module-6-6-alternating-row-1-text-pad { padding: 0 20px 32px !important; }
      .module-6-6-alternating-row-2-text-pad { padding: 0 20px 24px !important; }
      .module-6-6-alternating-row-2-image-pad { padding: 0 20px 40px !important; }
      .module-6-6-alternating-image-pad { padding: 0 !important; }
      .module-4-8-3-col-1-pad-first { padding: 24px 20px 24px !important; }
      .module-4-8-3-col-2-pad-first { padding: 0 20px 32px !important; }
      .module-4-8-3-col-1-pad-mid { padding: 0 20px 24px !important; }
      .module-4-8-3-col-2-pad-mid { padding: 0 20px 32px !important; }
      .module-4-8-3-col-1-pad-last { padding: 0 20px 24px !important; }
      .module-4-8-3-col-2-pad-last { padding: 0 20px 40px !important; }
      .module-4-8-3-image-pad { padding: 0 !important; }
      .module-4-8-3-image-pad img { max-width: 125px !important; height: auto !important; }
      .module-4-8-3-heading h1 { font-size: 24px !important; line-height: 34px !important; }
      .module-4-8-3-head-pad { padding: 40px 20px 0 !important; }
      .module-4-4-4-heading h1 { font-size: 24px !important; line-height: 34px !important; }
      .module-4-4-4-head-pad { padding: 40px 20px 0 !important; }
      .module-4-4-4-col-pad-first { padding: 24px 20px 32px !important; }
      .module-4-4-4-col-pad { padding: 0 20px 32px !important; }
      .module-4-4-4-col-pad-last { padding: 0 20px 40px !important; }
      .module-4-4-4-cta-pad { padding: 0 20px 40px !important; }
      .module-4-4-4-icon-slot { height: 68px !important; }
      .module-4-4-4-icon-wrap { margin: 0 auto 20px 0 !important; }
      .module-2-10-heading h1 { font-size: 24px !important; line-height: 34px !important; }
      .module-2-10-head-pad { padding: 40px 20px 0 !important; }
      .module-2-10-content-pad { padding: 24px 20px 40px !important; }
      .module-2-10-step-gap { padding-top: 12px !important; }
      .module-2-10-cta-gap { padding-top: 24px !important; }
      .module-2-10-connector-line { height: 72px !important; }
      .module-footer-pad { padding: 60px 20px 60px !important; }
      .module-table-pad { padding: 40px 20px !important; }
      .module-table-grid { table-layout: fixed !important; }
      .module-table-col-label { width: 44% !important; }
      .module-table-col-value { width: 28% !important; }
      .module-table-copy { font-size: 16px !important; line-height: 24px !important; word-break: break-word !important; overflow-wrap: anywhere !important; }
      .module-table-copy--head { font-size: 16px !important; line-height: 24px !important; }
      .legacy-list-col { display: block !important; width: 100% !important; box-sizing: border-box !important; }
      .legacy-list-col-left { padding-right: 0 !important; }
      .legacy-list-col-right { padding-left: 0 !important; padding-top: 24px !important; }
    }
  </style>
</head>
<body style="background-color:#FFFFFF;margin:0;padding:0;-webkit-text-size-adjust:none;text-size-adjust:none;">
  <table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;background-color:#FFFFFF;">
    <tbody>
      <tr>
        <td>

          <!-- MODULE SLOT: Insert one or more module blocks from modules.html below. -->
          <!-- Keep module order campaign-specific. Preserve table structure and conditional comments. -->

        </td>
      </tr>
    </tbody>
  </table>
</body>
</html>
```

## email-builder/agent/template-loft-snl.definition.json

Dateityp: json

```json
{
  "template_id": "loft-snl",
  "template_name": "Loft SNL",
  "version": 1,
  "status": "active",
  "preview_file": "template-loft-snl.preview.html",
  "iterable_template_id": 615576,
  "salutation_context_id": "loft-snl",
  "rules": {
    "order_locked": true,
    "forbid_new_modules": true,
    "allow_remove_modules": false,
    "allow_duplicate_modules": false
  },
  "slots": [
    {
      "slot_id": "logo-1",
      "module_id": "logo-centered",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "hero-1",
      "module_id": "hero-image-head-copy-bleed-center",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "copy-1",
      "module_id": "loft-snl-copy-cta",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "gallery-1",
      "module_id": "teaser-2col-gallery",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "copy-sections-1",
      "module_id": "loft-snl-copy-sections-cta",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "footer-1",
      "module_id": "footer",
      "locked": true,
      "removable": false,
      "repeatable": false
    }
  ]
}
```

## email-builder/agent/template-loft-snl.preview.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>E-Mail Vorschau | Loft SNL</title>
  <link rel="stylesheet" href="https://s24-creative-ops.github.io/email-builder/preview-styles.css" />
</head>
<body>
  <div class="preview-shell">
    <main class="preview-canvas">
      <section class="module preview-subject" data-preview-slot="subject">
        <div class="module__inner">
          <div class="preview-subject__stack">
            <p class="preview-subject__line preview-subject__line--subject">Subject: <span data-preview-subject-text>Neue Perspektiven für Ihr Loft-Projekt in Berlin</span></p>
            <p class="preview-subject__line preview-subject__line--preheader">Preheader: <span data-preview-preheader-text>Zentrierter Einstieg, freier Loft-Text, Bildergalerie und weitere Wohnbeispiele in einem neuen Template-Entwurf.</span></p>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="logo-centered" data-snippet="emb_logo_centered">
        <div class="module__inner module__inner--logo module__inner--logo-centered">
          <a
            class="module__logo-link"
            href="https://www.immobilienscout24.de/"
            title="ImmoScout24"
            data-token-attr-href="links.website"
            data-token-attr-title="logo.default.title"
            style="display:inline-block;"
          >
            <img
              class="module__logo-image"
              src="https://www.static-immobilienscout24.de/fro/ite/_/IS24-Logo_horizontal_center_white.png"
              alt="Logo ImmoScout24"
              width="198"
              height="47"
              style="display:block;padding:0;text-align:center;background:rgba(255,255,255,0);"
              data-token-attr-src="logo.centered.src"
              data-token-attr-alt="logo.centered.alt"
              data-token-attr-width="logo.centered.width"
              data-token-attr-height="logo.centered.height"
            />
          </a>
        </div>
      </section>

      <section class="module theme-white" data-module="hero-image-head-copy-bleed-center" data-snippet="emb_hero_image_head_copy_bleed_center">
        <div class="module__inner">
          <div class="module__hero-flow">
            <div class="module__hero-area module__hero-area--image">
              <div class="media media--hero media--bleed">
                <div
                  class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                  data-image-field="emb_hero_image_head_copy_bleed_center_image_url"
                  data-image-alt-field="emb_hero_image_head_copy_bleed_center_image_alt"
                >
                  <div class="preview-image-placeholder__text">
                    <p class="preview-image-placeholder__meta">16:9 | 1200 x 600 px<br />(Hi-Res 2400 x 1200)</p>
                  </div>
                </div>
              </div>
              <div class="module__hero-spacer module__hero-spacer--35" aria-hidden="true"></div>
            </div>
            <div class="module__hero-area module__hero-area--head">
              <div class="module__head module__head--center">
                <h2 class="module__title module__title--medium" data-export-field="emb_hero_image_head_copy_bleed_center_headline" data-export-role="headline">Ein neuer Blick auf modernes Wohnen in Friedrichshain</h2>
              </div>
              <div class="module__hero-spacer module__hero-spacer--25" aria-hidden="true"></div>
            </div>
            <div class="module__hero-area module__hero-area--copy">
              <div class="module__copy module__copy--center">
                <p class="module__body" data-export-field="emb_hero_image_head_copy_bleed_center_salutation" data-export-role="salutation">Hallo Anrede,</p>
                <div class="module__hero-spacer module__hero-spacer--salutation" aria-hidden="true"></div>
                <div class="module-rich-full-body module-rich-full-body--hero" data-export-field="emb_hero_image_head_copy_bleed_center_body" data-export-role="richtext">
                  <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Entdecken Sie ein Projekt, das <strong>klare Grundrisse</strong>, urbane Lage und hochwertige Details miteinander verbindet.</p>
                </div>
                <div class="module__hero-spacer module__hero-spacer--button" aria-hidden="true"></div>
                <div class="module__cta-row module__cta-row--center">
                  <a class="button-filled-brand" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.default_cta" data-export-field="emb_hero_image_head_copy_bleed_center_button_label" data-export-url-field="emb_hero_image_head_copy_bleed_center_button_url" data-export-role="cta">Projekt entdecken</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-gray" data-module="loft-snl-copy-cta" data-snippet="emb_loft_snl_copy_cta">
        <div class="module__inner">
          <div class="teaser-single">
            <div class="intro-richtext">
              <p class="module__body" data-export-role="salutation">Hallo Anrede,</p>
              <div class="module__teaser-richtext" data-export-field="emb_loft_snl_copy_cta_body" data-export-role="richtext">
                <p class="module__body" data-export-role="body-paragraph" data-export-index="1">in der Pufendorfstraße entstehen Wohnräume, die ruhige Rückzugsorte und ein lebendiges Umfeld zusammenbringen. <strong>Offene Wohnbereiche</strong>, bodentiefe Fenster und klare Materialien prägen den Charakter des Projekts.</p>
                <p class="module__body" data-export-role="body-paragraph" data-export-index="2">Der Standort in Friedrichshain verbindet kurze Wege ins Grüne mit einer schnellen Anbindung in die Innenstadt. So entsteht ein Wohnkonzept, das Alltag und Freizeit gut miteinander verzahnt.</p>
                <ul class="module__list--teaser">
                  <li data-export-item="teaser-list-item" data-export-index="1">Wohnungen mit 2 bis 4 Zimmern für unterschiedliche Lebensphasen</li>
                  <li data-export-item="teaser-list-item" data-export-index="2">Durchdachte Grundrisse mit viel Tageslicht und klaren Linien</li>
                  <li data-export-item="teaser-list-item" data-export-index="3"><a href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer">Weitere Informationen</a> direkt im Expose</li>
                </ul>
                <p class="module__body" data-export-role="body-paragraph" data-export-index="3">Wenn Sie einen ersten Eindruck gewinnen möchten, führt der schnellste Weg direkt in die Projektübersicht.</p>
              </div>
            </div>
            <div class="module__cta-row module__cta-row--compact">
              <a class="button-filled-default" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_loft_snl_copy_cta_button_label" data-export-url-field="emb_loft_snl_copy_cta_button_url" data-export-role="cta">Mehr erfahren</a>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="teaser-2col-gallery" data-snippet="emb_teaser_2col_gallery">
        <div class="module__inner">
          <div class="stack">
            <div class="module__head">
              <h2 class="module__title module__title--medium" data-export-field="emb_teaser_2col_gallery_headline" data-export-role="headline">Impressionen aus dem Projekt</h2>
            </div>
            <div class="gallery-grid">
              <div class="gallery-grid__row">
                <article class="gallery-grid__item" data-export-item="teaser-2col-gallery-item" data-export-index="1">
                  <div class="media media--teaser-horizontal gallery-grid__media">
                    <div
                      class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                      data-image-field="emb_teaser_2col_gallery_col_1_image_url"
                      data-image-alt-field="emb_teaser_2col_gallery_col_1_image_alt"
                    >
                      <div class="preview-image-placeholder__text">
                        <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                      </div>
                    </div>
                  </div>
                </article>
                <article class="gallery-grid__item" data-export-item="teaser-2col-gallery-item" data-export-index="2">
                  <div class="media media--teaser-horizontal gallery-grid__media">
                    <div
                      class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                      data-image-field="emb_teaser_2col_gallery_col_2_image_url"
                      data-image-alt-field="emb_teaser_2col_gallery_col_2_image_alt"
                    >
                      <div class="preview-image-placeholder__text">
                        <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                      </div>
                    </div>
                  </div>
                </article>
              </div>
              <div class="gallery-grid__row gallery-grid__row--mobile-hide">
                <article class="gallery-grid__item" data-export-item="teaser-2col-gallery-item" data-export-index="3">
                  <div class="media media--teaser-horizontal gallery-grid__media">
                    <div
                      class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                      data-image-field="emb_teaser_2col_gallery_col_3_image_url"
                      data-image-alt-field="emb_teaser_2col_gallery_col_3_image_alt"
                    >
                      <div class="preview-image-placeholder__text">
                        <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                      </div>
                    </div>
                  </div>
                </article>
                <article class="gallery-grid__item" data-export-item="teaser-2col-gallery-item" data-export-index="4">
                  <div class="media media--teaser-horizontal gallery-grid__media">
                    <div
                      class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                      data-image-field="emb_teaser_2col_gallery_col_4_image_url"
                      data-image-alt-field="emb_teaser_2col_gallery_col_4_image_alt"
                    >
                      <div class="preview-image-placeholder__text">
                        <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                      </div>
                    </div>
                  </div>
                </article>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-gray" data-module="loft-snl-copy-sections-cta" data-snippet="emb_loft_snl_copy_sections_cta">
        <div class="module__inner">
          <div class="stack">
            <section>
              <h2 class="module__title module__title--small" data-export-field="emb_loft_snl_copy_sections_cta_headline_1" data-export-role="headline">Highlights</h2>
              <div class="module__teaser-richtext" data-export-field="emb_loft_snl_copy_sections_cta_body_1" data-export-role="richtext">
                <ul class="module__list--teaser">
                  <li data-export-item="teaser-list-item" data-export-index="1"><strong>Zentrale Lage:</strong> Friedrichshain mit kurzen Wegen zum Volkspark und Boxhagener Platz</li>
                  <li data-export-item="teaser-list-item" data-export-index="2"><strong>Wohnungsvielfalt:</strong> Grundrisse für 2 bis 4 Zimmer und unterschiedliche Nutzungsprofile</li>
                  <li data-export-item="teaser-list-item" data-export-index="3"><strong>Ausstattung:</strong> Parkett, Fußbodenheizung und großzügige Fensterflächen</li>
                  <li data-export-item="teaser-list-item" data-export-index="4"><strong>Außenbereiche:</strong> Balkone, Terrassen und private Rückzugsorte im Freien</li>
                </ul>
              </div>
            </section>
            <section>
              <h2 class="module__title module__title--small" data-export-field="emb_loft_snl_copy_sections_cta_headline_2" data-export-role="headline">Wohnbeispiele</h2>
              <div class="module__teaser-richtext" data-export-field="emb_loft_snl_copy_sections_cta_body_2" data-export-role="richtext">
                <ul class="module__list--teaser">
                  <li data-export-item="teaser-list-item" data-export-index="1">2 Zimmer, ca. 50,76 m2, ideal für einen kompakten Stadtalltag</li>
                  <li data-export-item="teaser-list-item" data-export-index="2">3 Zimmer, ca. 78,21 m2, mit Platz für Homeoffice und Alltag</li>
                  <li data-export-item="teaser-list-item" data-export-index="3">4 Zimmer, ca. 98,11 m2, für großzügiges Wohnen mit Familie</li>
                </ul>
              </div>
            </section>
            <div class="module__cta-row module__cta-row--compact">
              <a class="button-filled-default" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_loft_snl_copy_sections_cta_button_label" data-export-url-field="emb_loft_snl_copy_sections_cta_button_url" data-export-role="cta">Mehr erfahren</a>
            </div>
          </div>
        </div>
      </section>

      <footer class="module theme-white" data-module="footer" data-snippet="emb_footer_marketing">
        <div class="module__inner module__inner--compact">
          <div class="footer-marketing">
            <p class="footer-marketing__headline">Kostenlose App herunterladen</p>
            <div class="footer-marketing__badges">
              <a class="footer-badge" href="https://itunes.apple.com/de/app/immobilienscout24/id342157367?mt=8" target="_blank" rel="noreferrer" data-token-attr-href="links.app_store">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/i36/uhu/m14/d1284a48-db27-4f3b-a434-ab9a625d0dd4.png"
                  data-token-attr-src="assets.app_store_badge"
                  alt="Download on the App Store"
                  width="115"
                  height="37"
                />
              </a>
              <a class="footer-badge" href="https://play.google.com/store/apps/details?id=de.is24.android&hl=de" target="_blank" rel="noreferrer" data-token-attr-href="links.google_play">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/nrd/s3d/49k/b78e3fcd-6303-429c-a29d-691d73c0d01d.png"
                  data-token-attr-src="assets.google_play_badge"
                  alt="Get it on Google Play"
                  width="130"
                  height="37"
                />
              </a>
            </div>
            <div class="footer-marketing__copy">
              <p class="footer-marketing__text">ImmoScout24 informiert ueber Aktuelles aus der Immobilienwelt. Wenn kein Interesse mehr besteht, ist es moeglich, sich <a href="#" target="_blank" rel="noreferrer">hier abzumelden</a>. Die Abmeldung betrifft nicht gegebenenfalls bestehende Suchauftragsbenachrichtigungen.</p>
              <p class="footer-marketing__text">Immobilien Scout GmbH - Ein Unternehmen der Scout24-Gruppe, Invalidenstr. 65, 10557 Berlin · <a class="footer-marketing__plain-link" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-token-attr-href="links.website" data-token-text="links.website_label">immobilienscout24.de</a> · Geschaeftsfuehrung: Dr. Gesa Crockford, Daniel Hendel · Vorsitzender des Aufsichtsrats: Ralf Weitz · Handelsregister: Amtsgericht Charlottenburg, HRB 69108 · Sitz der Gesellschaft: Berlin · USt-IdNr. DE200269419</p>
              <p class="footer-marketing__links">
                <a href="https://www.immobilienscout24.de/agb/datenschutz.html" target="_blank" rel="noreferrer" data-token-attr-href="links.privacy">Datenschutz</a><span class="footer-marketing__links-separator">|</span><a href="https://www.immobilienscout24.de/impressum.html" target="_blank" rel="noreferrer" data-token-attr-href="links.imprint">Impressum</a>
              </p>
              <p class="footer-marketing__text">&copy; 1999 - 2026 Immobilien Scout GmbH</p>
            </div>
          </div>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
```

## email-builder/email/templates/loft-snl.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <title>E-Mail Builder | Loft SNL</title>
  <!--[if mso]>
  <xml>
    <w:WordDocument xmlns:w="urn:schemas-microsoft-com:office:word"><w:DontUseAdvancedTypographyReadingMail/></w:WordDocument>
    <o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings>
  </xml>
  <![endif]-->
  <link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/make-it-better/1.0.0/makeitbetter.css">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; padding: 0; }
    a[x-apple-data-detectors] { color: inherit !important; text-decoration: inherit !important; }
    #MessageViewBody a { color: inherit; text-decoration: none; }
    p { line-height: inherit; }
    .desktop_hide, .desktop_hide table { mso-hide: all; display: none; max-height: 0; overflow: hidden; }
    .module-rich-full-body--hero {
      display: grid;
      gap: 0;
    }
    .module-rich-full-body--hero p,
    .module-rich-full-body--hero ul,
    .module-rich-full-body--hero ol {
      margin: 0;
    }
    .module-rich-full-body--hero p + p {
      margin-top: 16px;
    }
    .module-rich-full-body--hero p + ul,
    .module-rich-full-body--hero p + ol,
    .module-rich-full-body--hero ul + p,
    .module-rich-full-body--hero ul + ul,
    .module-rich-full-body--hero ul + ol,
    .module-rich-full-body--hero ol + p,
    .module-rich-full-body--hero ol + ul,
    .module-rich-full-body--hero ol + ol {
      margin-top: 8px;
    }
    .module-rich-full-body--hero ul,
    .module-rich-full-body--hero ol {
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--hero li {
      margin: 0 0 4px;
    }
    .module-rich-full-body--hero li:last-child {
      margin-bottom: 0;
    }
    .module-rich-full-body--teaser-1col p {
      margin: 0;
    }
    .module-rich-full-body--teaser-1col ul,
    .module-rich-full-body--teaser-1col ol {
      margin: 0;
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--teaser-1col p + ul,
    .module-rich-full-body--teaser-1col p + ol,
    .module-rich-full-body--teaser-1col ul + p,
    .module-rich-full-body--teaser-1col ul + ul,
    .module-rich-full-body--teaser-1col ul + ol,
    .module-rich-full-body--teaser-1col ol + p,
    .module-rich-full-body--teaser-1col ol + ul,
    .module-rich-full-body--teaser-1col ol + ol {
      margin-top: 8px;
    }
    .module-rich-full-body--teaser-1col p + p {
      margin-top: 16px;
    }
    .module-rich-full-body--teaser-1col li {
      margin: 0 0 4px;
    }
    .module-rich-full-body--teaser-1col li:last-child {
      margin-bottom: 0;
    }
    @media (max-width:620px) {
      .row-content { width: 100% !important; }
      .stack .column { width: 100% !important; display: block !important; }
      .desktop_hide, .desktop_hide table { display: table !important; max-height: none !important; }
      .mobile_hide { display: none !important; min-height: 0; max-height: 0; max-width: 0; overflow: hidden; font-size: 0; }
      .font-heading-medium-bold { font-size: 24px !important; line-height: 34px !important; }
      .font-heading-small-bold { font-size: 20px !important; line-height: 30px !important; }
      .module-12-bleed-image-pad { padding: 24px 0 0 !important; }
      .module-block[data-module="hero-image-head-copy-bleed-center"] .module-12-bleed-image-pad { padding-top: 20px !important; }
      .module-12-bleed-text-pad { padding: 24px 20px 40px !important; }
      .module-block[data-module="hero-image-head-copy-bleed-center"] .module-12-bleed-text-pad { padding-top: 0 !important; }
      .module-hero-spacer-35 { height: 30px !important; line-height: 30px !important; font-size: 30px !important; }
      .module-hero-spacer-button { height: 24px !important; line-height: 24px !important; font-size: 24px !important; }
      .module-logo-pad { padding: 24px 20px 0 !important; }
      .module-footer-pad { padding: 60px 20px 60px !important; }
      .module-table-pad { padding: 40px 20px !important; }
      .module-table-grid { table-layout: fixed !important; }
      .module-table-col-label { width: 44% !important; }
      .module-table-col-value { width: 28% !important; }
      .module-table-copy { font-size: 16px !important; line-height: 24px !important; word-break: break-word !important; overflow-wrap: anywhere !important; }
      .module-table-copy--head { font-size: 16px !important; line-height: 24px !important; }
      .legacy-list-col { display: block !important; width: 100% !important; box-sizing: border-box !important; }
      .legacy-list-col-left { padding-right: 0 !important; }
      .legacy-list-col-right { padding-left: 0 !important; padding-top: 24px !important; }
    }
  </style>
</head>
<body style="background-color:#FFFFFF;margin:0;padding:0;-webkit-text-size-adjust:none;text-size-adjust:none;">
  <table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;background-color:#FFFFFF;">
    <tbody>
      <tr>
        <td>

          <!-- EMB CONTENT INSERTION POINT: Export inserts the generated module HTML or snippet calls here. -->
          <!-- This Iterable basis template must remain a shell without fixed modules. -->

        </td>
      </tr>
    </tbody>
  </table>
</body>
</html>
```

## email-builder/agent/template-loft-rnl-dev.definition.json

Dateityp: json

```json
{
  "template_id": "loft-rnl-dev",
  "template_name": "Loft RNL (Dev)",
  "version": 1,
  "status": "active",
  "preview_file": "template-loft-rnl-dev.preview.html",
  "iterable_template_id": 618734,
  "salutation_context_id": "loft-rnl-dev",
  "rules": {
    "order_locked": true,
    "forbid_new_modules": true,
    "allow_remove_modules": true,
    "allow_duplicate_modules": true
  },
  "slots": [
    {
      "slot_id": "logo-1",
      "module_id": "logo",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "intro-1",
      "module_id": "loft-rnl-dev-intro",
      "locked": true,
      "removable": false,
      "repeatable": false
    },
    {
      "slot_id": "teaser-1",
      "module_id": "loft-rnl-dev-teaser-1col",
      "locked": false,
      "removable": true,
      "repeatable": true
    },
    {
      "slot_id": "footer-1",
      "module_id": "footer",
      "locked": true,
      "removable": false,
      "repeatable": false
    }
  ]
}
```

## email-builder/agent/template-loft-rnl-dev.preview.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>E-Mail Vorschau | Loft RNL (Dev)</title>
  <link rel="stylesheet" href="https://s24-creative-ops.github.io/email-builder/preview-styles.css" />
</head>
<body>
  <div class="preview-shell">
    <main class="preview-canvas">
      <section class="module preview-subject" data-preview-slot="subject">
        <div class="module__inner">
          <div class="preview-subject__stack">
            <p class="preview-subject__line preview-subject__line--subject">Subject: <span data-preview-subject-text>Loft Regional Newsletter: Neubauprojekte in Ihrer Region</span></p>
            <p class="preview-subject__line preview-subject__line--preheader">Preheader: <span data-preview-preheader-text>Zwei neue Projektkarten im Loft-RNL-Entwurf, aufgebaut aus bestehenden Loft-SNL- und EMB-Patterns.</span></p>
          </div>
        </div>
      </section>

      <section class="module theme-white" data-module="logo" data-snippet="emb_logo">
        <div class="module__inner module__inner--logo">
          <a class="module__logo-link" href="https://www.immobilienscout24.de/" title="ImmoScout24">
            <img
              class="module__logo-image"
              src="https://www.static-immobilienscout24.de/fro/ite/_/IS24-Logo_horizontal_left_white.png"
              alt="Logo ImmoScout24"
              width="185"
              height="47"
            />
          </a>
        </div>
      </section>

      <section class="module theme-white" data-module="loft-rnl-dev-intro" data-snippet="emb_loft_rnl_dev_intro">
        <div class="module__inner">
          <div class="teaser-single">
            <div class="intro-richtext">
              <h2 class="module__title font-heading-large-bold loft-rnl-dev-intro__headline" data-export-field="emb_loft_rnl_dev_intro_headline" data-export-role="headline">Immobilien-Newsletter München</h2>
              <p class="module__body" data-export-field="emb_loft_rnl_dev_intro_salutation" data-export-role="salutation">Hallo Anrede</p>
              <div class="module__teaser-richtext" data-export-field="emb_loft_rnl_dev_intro_body" data-export-role="richtext">
                <p class="module__body" data-export-role="body-paragraph" data-export-index="1">willkommen zum aktuellen Immobilien-Newsletter für München und Umgebung.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="module theme-gray" data-module="loft-rnl-dev-teaser-1col" data-snippet="emb_loft_rnl_dev_teaser_1col">
        <div class="module__inner">
          <div class="teaser-single">
            <div class="module__head">
              <div class="module__hero-meta">
                <span class="module__badge module__badge--surface-white" data-export-field="emb_loft_rnl_dev_teaser_1col_badge_label" data-export-role="badge">Wohnungen zum Kauf</span>
              </div>
              <h2 class="module__title font-heading-large-bold loft-rnl-dev-teaser-1col__headline" data-export-field="emb_loft_rnl_dev_teaser_1col_headline" data-export-role="headline">Urbanes Wohnen am Stadtpark in Berlin-Pankow</h2>
            </div>
            <div class="media media--hero">
              <div
                class="preview-image-placeholder preview-image-placeholder--16x9 preview-image-placeholder--pad-lg"
                data-image-field="emb_loft_rnl_dev_teaser_1col_image_url"
                data-image-alt-field="emb_loft_rnl_dev_teaser_1col_image_alt"
              >
                <div class="preview-image-placeholder__text">
                  <p class="preview-image-placeholder__meta">16:9 | 960 x 540 px</p>
                </div>
              </div>
            </div>
            <div class="module__teaser-richtext" data-export-field="emb_loft_rnl_dev_teaser_1col_body" data-export-role="richtext">
              <p class="module__body" data-export-role="body-paragraph" data-export-index="1">Das Projekt verbindet eine ruhige Lage am Grünzug mit einer direkten Anbindung in die Innenstadt. Großzügige Wohnbereiche, bodentiefe Fenster und private Außenflächen schaffen ein helles Wohngefühl.</p>
              <p class="module__body" data-export-role="body-paragraph" data-export-index="2">Die Projektkarte nutzt eine einheitliche Struktur für Badge, Headline, Bild, Copy, Detailblock und CTA, damit sich mehrere Neubauprojekte im Template konsistent aufbauen lassen.</p>
            </div>
            <section class="loft-rnl-dev-teaser-1col__details">
              <h2 class="module__title module__title--small">Details zum Projekt</h2>
              <div class="module__teaser-richtext" data-export-field="emb_loft_rnl_dev_teaser_1col_details" data-export-role="richtext">
                <ul class="module__list--teaser">
                  <li data-export-item="teaser-list-item" data-export-index="1">2 bis 4 Zimmer mit Grundrissen für unterschiedliche Lebensphasen</li>
                  <li data-export-item="teaser-list-item" data-export-index="2">Balkone, Terrassen und gemeinschaftliche Außenbereiche</li>
                  <li data-export-item="teaser-list-item" data-export-index="3">Gute Anbindung an ÖPNV, Kitas und Nahversorgung im Quartier</li>
                </ul>
              </div>
            </section>
            <div class="module__cta-row module__cta-row--compact">
              <a class="button-filled-default" href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer" data-export-field="emb_loft_rnl_dev_teaser_1col_button_label" data-export-url-field="emb_loft_rnl_dev_teaser_1col_button_url" data-export-role="cta">Exposé anfordern</a>
            </div>
          </div>
        </div>
      </section>

      <footer class="module theme-white" data-module="footer" data-snippet="emb_footer_marketing">
        <div class="module__inner module__inner--compact">
          <div class="footer-marketing">
            <p class="footer-marketing__headline">Kostenlose App herunterladen</p>
            <div class="footer-marketing__badges">
              <a class="footer-badge" href="https://itunes.apple.com/de/app/immobilienscout24/id342157367?mt=8" target="_blank" rel="noreferrer" data-token-attr-href="links.app_store">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/i36/uhu/m14/d1284a48-db27-4f3b-a434-ab9a625d0dd4.png"
                  data-token-attr-src="assets.app_store_badge"
                  alt="Download on the App Store"
                  width="115"
                  height="37"
                />
              </a>
              <a class="footer-badge" href="https://play.google.com/store/apps/details?id=de.is24.android&amp;hl=de" target="_blank" rel="noreferrer" data-token-attr-href="links.google_play">
                <img
                  class="footer-badge__image"
                  src="https://d15k2d11r6t6rl.cloudfront.net/pub/bfra/tgru1zsx/nrd/s3d/49k/b78e3fcd-6303-429c-a29d-691d73c0d01d.png"
                  data-token-attr-src="assets.google_play_badge"
                  alt="Get it on Google Play"
                  width="130"
                  height="37"
                />
              </a>
            </div>
            <div class="footer-marketing__copy">
              <p class="footer-marketing__text">ImmoScout24 informiert über Aktuelles aus der Immobilienwelt. Wenn Sie keine Tipps und Angebote mehr erhalten möchten, können Sie sich <a href="#" target="_blank" rel="noreferrer">hier abmelden</a>.</p>
              <p class="footer-marketing__text">Immobilien Scout GmbH, Invalidenstr. 65, 10557 Berlin · <a href="https://www.immobilienscout24.de" target="_blank" rel="noreferrer">immobilienscout24.de</a> · Geschäftsführung: Dr. Gesa Crockford, Daniel Hendel · Registergericht: Amtsgericht Charlottenburg · Registernummer: HRB 69108 B</p>
              <p class="footer-marketing__links">
                <a href="https://www.immobilienscout24.de/agb/datenschutz.html" target="_blank" rel="noreferrer" data-token-attr-href="links.privacy">Datenschutz</a><span class="footer-marketing__links-separator">|</span><a href="https://www.immobilienscout24.de/impressum.html" target="_blank" rel="noreferrer" data-token-attr-href="links.imprint">Impressum</a>
              </p>
              <p class="footer-marketing__text">&copy; 1999 - 2026 Immobilien Scout GmbH</p>
            </div>
          </div>
        </div>
      </footer>
    </main>
  </div>
</body>
</html>
```

## email-builder/email/templates/loft-rnl-dev.html

Dateityp: html

```html
<!DOCTYPE html>
<html lang="de" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <title>E-Mail Builder | Loft RNL (Dev)</title>
  <!--[if mso]>
  <xml>
    <w:WordDocument xmlns:w="urn:schemas-microsoft-com:office:word"><w:DontUseAdvancedTypographyReadingMail/></w:WordDocument>
    <o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings>
  </xml>
  <![endif]-->
  <link rel="stylesheet" href="https://www.static-immobilienscout24.de/fro/make-it-better/1.0.0/makeitbetter.css">
  <style>
    * { box-sizing: border-box; }
    body { margin: 0; padding: 0; }
    a[x-apple-data-detectors] { color: inherit !important; text-decoration: inherit !important; }
    #MessageViewBody a { color: inherit; text-decoration: none; }
    p { line-height: inherit; }
    .desktop_hide, .desktop_hide table { mso-hide: all; display: none; max-height: 0; overflow: hidden; }
    .module-rich-full-body--hero {
      display: grid;
      gap: 0;
    }
    .module-rich-full-body--hero p,
    .module-rich-full-body--hero ul,
    .module-rich-full-body--hero ol {
      margin: 0;
    }
    .module-rich-full-body--hero p + p {
      margin-top: 16px;
    }
    .module-rich-full-body--hero p + ul,
    .module-rich-full-body--hero p + ol,
    .module-rich-full-body--hero ul + p,
    .module-rich-full-body--hero ul + ul,
    .module-rich-full-body--hero ul + ol,
    .module-rich-full-body--hero ol + p,
    .module-rich-full-body--hero ol + ul,
    .module-rich-full-body--hero ol + ol {
      margin-top: 8px;
    }
    .module-rich-full-body--hero ul,
    .module-rich-full-body--hero ol {
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--hero li {
      margin: 0 0 4px;
    }
    .module-rich-full-body--hero li:last-child {
      margin-bottom: 0;
    }
    .module-rich-full-body--teaser-1col p {
      margin: 0;
    }
    .module-rich-full-body--teaser-1col ul,
    .module-rich-full-body--teaser-1col ol {
      margin: 0;
      padding-left: 20px;
      padding-inline-start: 20px;
      margin-left: 0;
    }
    .module-rich-full-body--teaser-1col p + ul,
    .module-rich-full-body--teaser-1col p + ol,
    .module-rich-full-body--teaser-1col ul + p,
    .module-rich-full-body--teaser-1col ul + ul,
    .module-rich-full-body--teaser-1col ul + ol,
    .module-rich-full-body--teaser-1col ol + p,
    .module-rich-full-body--teaser-1col ol + ul,
    .module-rich-full-body--teaser-1col ol + ol {
      margin-top: 8px;
    }
    .module-rich-full-body--teaser-1col p + p {
      margin-top: 16px;
    }
    .module-rich-full-body--teaser-1col li {
      margin: 0 0 4px;
    }
    .module-rich-full-body--teaser-1col li:last-child {
      margin-bottom: 0;
    }
    @media (max-width:620px) {
      .row-content { width: 100% !important; }
      .stack .column { width: 100% !important; display: block !important; }
      .desktop_hide, .desktop_hide table { display: table !important; max-height: none !important; }
      .mobile_hide { display: none !important; min-height: 0; max-height: 0; max-width: 0; overflow: hidden; font-size: 0; }
      .font-heading-large-bold { font-size: 28px !important; line-height: 36px !important; }
      .font-heading-medium-bold { font-size: 24px !important; line-height: 34px !important; }
      .font-heading-small-bold { font-size: 20px !important; line-height: 30px !important; }
      .module-12-heading h1 { font-size: 28px !important; line-height: 36px !important; }
      .module-12-head-pad { padding: 24px 20px 0 !important; }
      .module-12-body-pad { padding: 12px 20px 0 !important; }
      .module-teaser-1col-body-pad-spaced { padding: 24px 20px 40px !important; }
      .module-block[data-module="loft-rnl-dev-teaser-1col"] .module-12-head-pad { padding: 40px 20px 0 !important; }
      .module-block[data-module="loft-rnl-dev-teaser-1col"] .module-teaser-1col-body-pad-spaced { padding: 20px 20px 40px !important; }
      .module-logo-pad { padding: 24px 20px 0 !important; }
      .module-footer-pad { padding: 60px 20px 60px !important; }
      .module-table-pad { padding: 40px 20px !important; }
    }
  </style>
</head>
<body style="background-color:#FFFFFF;margin:0;padding:0;-webkit-text-size-adjust:none;text-size-adjust:none;">
  <table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace:0pt;mso-table-rspace:0pt;background-color:#FFFFFF;">
    <tbody>
      <tr>
        <td>

          <!-- EMB CONTENT INSERTION POINT: Export inserts the generated module HTML or snippet calls here. -->
          <!-- This Iterable basis template must remain a shell without fixed modules. -->

        </td>
      </tr>
    </tbody>
  </table>
</body>
</html>
```
