# Software Engineering – Learning Repository

Willkommen in meinem persönlichen Lern-Repository für Software Engineering, Python und objektorientierte Programmierung.

Dieses Repository begleitet meinen Lernweg im Bereich Softwareentwicklung.  
Hier sammle ich Übungen, Workshop-Aufgaben, Notizen, kleine Projekte und Code-Beispiele aus meinem Kurs.

---

## About this Repository

This repository documents my learning journey in software engineering and Python programming.

It contains exercises, workshop tasks, notes, examples and small projects created while learning fundamental programming concepts, object-oriented programming and version control with Git and GitHub.

The goal is not only to store code, but also to make my progress visible step by step.

---

## Inhalte / Contents

Das Repository ist nach Themenbereichen sortiert:

| Ordner | Inhalt |
|---|---|
| `00_admin_organisation` | Organisatorische Unterlagen und Struktur |
| `01_einfuehrung_software_engineering` | Einführung in Software Engineering |
| `02_entwicklungsumgebung` | Entwicklungsumgebung, VS Code, Setup |
| `03_versionskontrolle_git_kommandozeile` | Git, GitHub und Kommandozeile |
| `04_syntax_datentypen_variablen` | Python-Grundlagen, Variablen und Datentypen |
| `05_kontrollstrukturen_funktionen` | Bedingungen, Schleifen und Funktionen |
| `06_sequenzen` | Listen, Tupel, Strings und Sequenzen |
| `07_weitere_datenstrukturen` | Dictionaries, Sets und weitere Datenstrukturen |
| `08_klassen_objekte_methoden` | Klassen, Objekte und Methoden |
| `11_vererbung_und_polymorphie` | Vererbung, Polymorphie und OOP-Workshops |
| `90_Projekte` | Eigene kleine Projekte |
| `91_spickzettel` | Zusammenfassungen und Lernhilfen |
| `99_archiv_alt_unsortiert` | Archiv und ältere Dateien |

---

## Themen, die ich aktuell lerne

- Python-Grundlagen
- Variablen, Datentypen und Operatoren
- Kontrollstrukturen mit `if`, `elif`, `else`
- Schleifen mit `for` und `while`
- Funktionen und Rückgabewerte
- Listen, Tupel, Sets und Dictionaries
- Objektorientierte Programmierung
- Klassen, Objekte, Attribute und Methoden
- Vererbung und Polymorphie
- Arbeiten mit Git und GitHub
- Strukturierte Projektorganisation in VS Code

---

## My Learning Goals

My main goals are:

- to understand programming concepts step by step
- to write clean and readable Python code
- to document my learning progress
- to practice Git and GitHub regularly
- to build a solid foundation for future software engineering and AI-related topics

---

## Arbeitsweise / Workflow

Ich arbeite hauptsächlich mit:

- Visual Studio Code
- Python
- Jupyter Notebooks
- Git
- GitHub
- Markdown

Typischer Git-Workflow:

```bash
git status
git add -A
git commit -m "Update learning files"
git push


# Git auf dem Mac installieren

Diese Anleitung erklärt Schritt für Schritt, wie man **Git auf einem Mac installiert**.

Wir benutzen dafür:

- Terminal
- Homebrew
- Git

Diese Anleitung ist für Kursteilnehmer gedacht, die später gemeinsam mit Git und GitHub an einem Projekt arbeiten möchten.

---

## 1. Terminal öffnen

Zuerst wird auf dem Mac das Terminal geöffnet.

Das geht so:

```text
Cmd + Leertaste drücken
Terminal eingeben
Enter drücken
```

Danach öffnet sich das Terminal.

---

## 2. Prüfen, ob Git schon installiert ist

Im Terminal eingeben:

```bash
git --version
```

Wenn eine Version angezeigt wird, ist Git schon installiert.

Beispiel:

```bash
git version 2.45.0
```

Dann muss Git nicht nochmal installiert werden.

Falls eine Fehlermeldung kommt oder Git nicht gefunden wird, geht es mit dem nächsten Schritt weiter.

Merksatz:

```text
git --version prüft, ob Git auf dem Mac vorhanden ist.
```

---

## 3. Prüfen, ob Homebrew installiert ist

Homebrew ist ein Paketmanager für den Mac.

Damit kann man Programme bequem über das Terminal installieren.

Im Terminal eingeben:

```bash
brew --version
```

Wenn eine Version angezeigt wird, ist Homebrew bereits installiert.

Beispiel:

```bash
Homebrew 4.x.x
```

Falls eine Fehlermeldung kommt, muss Homebrew zuerst installiert werden.

Merksatz:

```text
brew --version prüft, ob Homebrew vorhanden ist.
```

---

## 4. Command Line Tools installieren

Vor Homebrew sollte man die Apple Command Line Tools installieren.

Dazu im Terminal eingeben:

```bash
xcode-select --install
```

Danach öffnet sich ein kleines Fenster von macOS.

Dort die Installation bestätigen.

Wenn die Meldung kommt, dass die Tools bereits installiert sind, ist das in Ordnung.

Merksatz:

```text
Die Command Line Tools geben dem Mac wichtige Entwickler-Werkzeuge.
```

---

## 5. Homebrew installieren

Falls Homebrew noch nicht installiert ist, diesen Befehl in das Terminal kopieren:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Danach Enter drücken.

Während der Installation kann das Mac-Passwort abgefragt werden.

Wichtig:

```text
Beim Eingeben des Passworts sieht man im Terminal keine Zeichen.
Das ist normal.
Einfach das Passwort eingeben und Enter drücken.
```

Homebrew zeigt während der Installation an, was gemacht wird.

Wenn eine Abfrage kommt, mit Enter bestätigen.

Merksatz:

```text
Homebrew installiert Programme über das Terminal.
```

---

## 6. Prüfen, welchen Mac man hat

Nach der Installation sollte man prüfen, ob man einen Apple-Silicon-Mac oder einen Intel-Mac hat.

Im Terminal eingeben:

```bash
uname -m
```

Wenn dort steht:

```text
arm64
```

dann ist es ein Mac mit Apple Silicon, also zum Beispiel M1, M2, M3 oder M4.

Wenn dort steht:

```text
x86_64
```

dann ist es ein Intel-Mac.

---

## 7. Homebrew zum Terminal-Pfad hinzufügen

Nach der Homebrew-Installation zeigt das Terminal meistens sogenannte **Next steps** an.

Diese Schritte sind wichtig.

Wenn man einen Apple-Silicon-Mac hat, also `arm64`, verwendet man:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Wenn man einen Intel-Mac hat, also `x86_64`, verwendet man:

```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

Danach prüfen:

```bash
brew --version
```

Wenn jetzt eine Homebrew-Version angezeigt wird, funktioniert Homebrew.

Merksatz:

```text
Der Pfad sagt dem Terminal, wo es Homebrew finden kann.
```

---

## 8. Homebrew aktualisieren

Wenn Homebrew funktioniert, sollte man es einmal aktualisieren:

```bash
brew update
```

Merksatz:

```text
brew update aktualisiert die Paketlisten von Homebrew.
```

---

## 9. Git mit Homebrew installieren

Jetzt wird Git installiert:

```bash
brew install git
```

Die Installation kann einen Moment dauern.

Danach prüfen:

```bash
git --version
```

Wenn eine Git-Version angezeigt wird, war die Installation erfolgreich.

Beispiel:

```bash
git version 2.55.0
```

Merksatz:

```text
brew install git installiert Git auf dem Mac.
```

---

## 10. Prüfen, welches Git benutzt wird

Mit diesem Befehl kann man prüfen, wo Git liegt:

```bash
which git
```

Bei Apple Silicon sieht man oft:

```text
/opt/homebrew/bin/git
```

Bei Intel-Macs sieht man oft:

```text
/usr/local/bin/git
```

Falls dort steht:

```text
/usr/bin/git
```

wird wahrscheinlich noch die Apple-Version von Git benutzt.

Das ist nicht immer schlimm, aber nach der Homebrew-Installation sollte meistens die Homebrew-Version verwendet werden.

---

## 11. Git einmalig einrichten

Git muss wissen, wer Änderungen macht.

Deshalb trägt man einmalig den eigenen Namen ein:

```bash
git config --global user.name "Dein Name"
```

Beispiel:

```bash
git config --global user.name "Max Mustermann"
```

Danach die eigene E-Mail-Adresse eintragen:

```bash
git config --global user.email "deine.email@example.com"
```

Beispiel:

```bash
git config --global user.email "max@example.com"
```

Merksatz:

```text
user.name und user.email zeigen später, wer einen Commit gemacht hat.
```

---

## 12. Git-Einstellungen prüfen

Mit diesem Befehl kann man prüfen, ob Name und E-Mail gespeichert wurden:

```bash
git config --global --list
```

Beispielausgabe:

```text
user.name=Max Mustermann
user.email=max@example.com
```

---

## 13. Mini-Test

Zum Schluss noch einmal prüfen:

```bash
git --version
brew --version
git config --global --list
```

Wenn alle drei Befehle eine sinnvolle Ausgabe zeigen, ist alles bereit.

---

## 14. Häufige Probleme

### Problem: brew command not found

Wenn diese Meldung kommt:

```text
brew: command not found
```

dann wurde Homebrew wahrscheinlich nicht zum Terminal-Pfad hinzugefügt.

Bei Apple Silicon:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Bei Intel:

```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

Danach erneut prüfen:

```bash
brew --version
```

---

### Problem: Passwort wird nicht angezeigt

Wenn das Terminal nach dem Passwort fragt, sieht man beim Tippen keine Zeichen.

Das ist normal.

Einfach das Passwort eingeben und Enter drücken.

---

### Problem: Git ist schon installiert

Wenn bei:

```bash
git --version
```

bereits eine Version angezeigt wird, ist Git schon vorhanden.

Man kann Git trotzdem über Homebrew aktualisieren:

```bash
brew install git
```

oder später:

```bash
brew upgrade git
```

---

## 15. Wichtigste Befehle als Spickzettel

```bash
git --version

brew --version

xcode-select --install

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

uname -m

brew update

brew install git

git --version

which git

git config --global user.name "Dein Name"

git config --global user.email "deine.email@example.com"

git config --global --list
```

---

## 16. Wichtigster Merksatz

```text
Homebrew installiert Programme auf dem Mac.
Git speichert Änderungen an Dateien.
GitHub teilt diese Änderungen später mit der Gruppe.
```

---

## 17. Nächster Schritt

Nach der Git-Installation kann man später ein GitHub-Repository erstellen, herunterladen und mit dem Terminal verbinden.

Das passiert später mit Befehlen wie:

```bash
git clone
git pull
git add
git commit
git push
```
## Nützliche Lernressourcen und Entwicklungswerkzeuge

In diesem Abschnitt befinden sich hilfreiche Internetseiten zum Lernen und Vertiefen von Python, Git, Software Engineering und weiterführenden Entwicklungsthemen.

---

### Python-Grundlagen und Nachschlagewerke

#### Python – Eingebaute Funktionen

[Python-Dokumentation: Built-in Functions](https://docs.python.org/3/library/functions.html)

Die offizielle Python-Dokumentation zu den eingebauten Funktionen. Sie erklärt unter anderem Funktionen wie `print()`, `input()`, `len()`, `sum()`, `min()`, `max()`, `sorted()`, `isinstance()` und `open()`.

---

#### String-Formatierung mit f-Strings

[Python Morsels: Python f-string Tips and Cheat Sheets](https://www.pythonmorsels.com/string-formatting/)

Eine ausführliche Einführung in die Formatierung von Texten und Zahlen mit f-Strings. Die Seite zeigt unter anderem Dezimalstellen, Prozentangaben, Ausrichtungen, Abstände und formatierte Konsolenausgaben.

---

#### Kostenloser Python-Kurs von Google

[Google for Developers: Python-Klasse](https://developers.google.com/edu/python?hl=de)

Ein kostenloser Python-Kurs mit schriftlichen Erklärungen, Lernvideos und praktischen Übungen. Behandelt werden unter anderem Strings, Listen, Dictionaries, Dateien, Sortierung und reguläre Ausdrücke.

---

#### Python-Lernvideos von Indently

[Indently auf YouTube](https://www.youtube.com/@Indently)

Ein YouTube-Kanal mit kurzen Videos zu Python-Grundlagen und weiterführenden Themen. Dazu gehören beispielsweise Funktionen, Klassen, objektorientierte Programmierung, Type Hints, Fehlerbehandlung und saubere Programmierweisen.

---

#### Kostenlose IT-Fachbücher

[Rheinwerk Openbook](https://www.rheinwerk-verlag.de/openbook/)

Eine Sammlung kostenlos online verfügbarer Fachbücher zu Python, Programmierung, Datenbanken und weiteren IT-Themen. Die Bücher eignen sich zum Vertiefen und Nachschlagen.

> **Hinweis:** Einige Openbooks basieren auf älteren Buchauflagen. Deshalb sollte bei technischen Einzelheiten zusätzlich die aktuelle offizielle Dokumentation geprüft werden.

---

### Code verstehen und visualisieren

#### Python Tutor

[Python Tutor: Code Visualizer](https://pythontutor.com/visualize.html#mode=display)

Python Tutor führt Programmcode Schritt für Schritt aus und zeigt dabei Variablen, Datenstrukturen, Funktionsaufrufe und Objekte grafisch an. Das Werkzeug hilft dabei, den Ablauf eines Programms besser zu verstehen und Fehler zu finden.

---

### Git und Versionsverwaltung

#### Learn Git Branching

[Learn Git Branching – deutsche Version](https://learngitbranching.js.org/?locale=de_DE)

Eine interaktive Lernplattform für Git. Befehle wie `git branch`, `git switch`, `git checkout`, `git merge`, `git rebase` und `git cherry-pick` können direkt ausprobiert werden. Die Auswirkungen werden grafisch dargestellt.

---

#### Pro Git

[Pro Git – offizielles Git-Handbuch](https://git-scm.com/book/en/v2)

Ein kostenloses und umfassendes Nachschlagewerk zu Git. Es behandelt unter anderem Repositories, Commits, Branches, Remotes, Merges, Rebasing, Tags und die interne Arbeitsweise von Git.

---

### Benutzereingaben und Tastatursteuerung

#### Auf einen Tastendruck warten

[Pierian Training: How to Wait for a Keypress in Python](https://pieriantraining.com/how-to-wait-for-a-keypress-in-python/)

Der Artikel zeigt verschiedene Möglichkeiten, ein Python-Programm anzuhalten, bis eine Eingabe oder ein Tastendruck erfolgt. Für einfache und plattformübergreifende Konsolenprogramme eignet sich häufig die eingebaute Funktion `input()`.

---

#### Tastendrücke mit Python simulieren

[Nitratine: Simulate Keypresses in Python](https://nitratine.net/blog/post/simulate-keypresses-in-python/)

Eine Einführung in die automatische Tastatursteuerung mit dem externen Python-Paket `pynput`. Gezeigt werden einzelne Tasten, Sondertasten, Tastenkombinationen und das automatische Schreiben von Text.

> **Abgrenzung:** Diese Seite behandelt das automatische Auslösen von Tastendrücken. Sie ist nicht mit dem bloßen Warten auf eine Benutzereingabe zu verwechseln.

---

### Fortgeschrittene Python-Themen

#### Multiprocessing in Python

[SuperFastPython: Multiprocessing in Python](https://superfastpython.com/multiprocessing-in-python/)

Ein ausführlicher Leitfaden zur parallelen Ausführung von Aufgaben mit mehreren Prozessen. Behandelt werden unter anderem `Process`, `start()`, `join()`, Process Pools sowie die Unterschiede zwischen Prozessen, Threads, Nebenläufigkeit und Parallelität.

> **Hinweis:** Multiprocessing ist ein fortgeschrittenes Thema und für kleinere Einsteigerprojekte normalerweise noch nicht erforderlich.
>
> ---

## Nützliche Lernressourcen für Software Engineering

In diesem Abschnitt befinden sich hilfreiche Internetseiten, Dokumentationen,
Lernplattformen und Werkzeuge zu Python, Git, Versionsverwaltung,
Programmabläufen und weiterführenden Software-Engineering-Themen.

---

### Python-Grundlagen

#### Eingebaute Python-Funktionen

[Python-Dokumentation – Built-in Functions](https://docs.python.org/3/library/functions.html)

Diese offizielle Python-Dokumentation erklärt die eingebauten Funktionen von
Python.

Dazu gehören zum Beispiel:

- `print()`
- `input()`
- `len()`
- `sum()`
- `min()`
- `max()`
- `sorted()`
- `isinstance()`
- `open()`

Die Seite eignet sich sehr gut als Nachschlagewerk, wenn man wissen möchte,
welche Funktionen Python bereits von Haus aus bereitstellt.

---

#### String-Formatierung mit Python

[Python Morsels – String Formatting](https://www.pythonmorsels.com/string-formatting/)

Diese Seite erklärt, wie Texte, Zahlen, Dezimalstellen und Prozentwerte mit
f-Strings formatiert werden können.

Sie ist besonders hilfreich für:

- übersichtliche Konsolenausgaben
- Tabellen
- Dezimalzahlen
- Prozentwerte
- Abstände und Ausrichtungen
- gut lesbare Ergebnisse

---

### Kostenlose Python-Kurse und Lernmaterialien

#### Google Python-Kurs

[Google for Developers – Python-Klasse](https://developers.google.com/edu/python?hl=de)

Diese Seite bietet einen kostenlosen Python-Kurs von Google.

Der Kurs enthält:

- schriftliche Erklärungen
- Lernvideos
- Übungen
- Beispielprogramme

Behandelt werden unter anderem:

- Strings
- Listen
- Dictionaries
- Dateien
- Sortierung
- reguläre Ausdrücke

---

#### Indently auf YouTube

[Indently – Python-Lernvideos](https://www.youtube.com/@Indently)

Indently ist ein YouTube-Kanal mit kurzen Videos zu Python und
Softwareentwicklung.

Die Videos behandeln unter anderem:

- Python-Grundlagen
- Funktionen
- Klassen
- objektorientierte Programmierung
- Type Hints
- Fehlerbehandlung
- Testing
- virtuelle Umgebungen
- saubere Programmierweisen

---

#### Rheinwerk Openbook

[Rheinwerk Openbook – Kostenlose Fachbücher](https://www.rheinwerk-verlag.de/openbook/)

Rheinwerk Openbook stellt ausgewählte Fachbücher kostenlos als
Online-Version zur Verfügung.

Dort gibt es Bücher zu Themen wie:

- Python
- Programmierung
- Datenbanken
- Linux
- Netzwerke
- Softwareentwicklung

Einige Bücher basieren auf älteren Auflagen. Deshalb sollten technische
Einzelheiten zusätzlich mit aktueller Dokumentation verglichen werden.

---

### Code und Speicher visualisieren

#### Python Tutor

[Python Tutor – Python-Code visualisieren](https://pythontutor.com/visualize.html#mode=display)

Python Tutor führt Python-Code Schritt für Schritt aus.

Dabei werden grafisch dargestellt:

- Variablen
- Listen
- Dictionaries
- Funktionsaufrufe
- Klassen
- Objekte
- Rückgabewerte
- Veränderungen während der Ausführung

Die Seite eignet sich besonders gut, um Programmabläufe besser zu verstehen
und Fehler zu suchen.

---

#### Memory Graph

[Memory Graph – Objekte und Referenzen visualisieren](https://memory-graph.com/#breakpoints=8&continues=1&play)

Memory Graph zeigt, wie Python-Objekte und Variablen im Speicher miteinander
verbunden sind.

Damit kann man besser verstehen:

- welche Variable auf welches Objekt verweist
- wie Listen aufgebaut sind
- wie Dictionaries gespeichert werden
- wie Objekte miteinander verbunden sind
- wie Klasseninstanzen Beziehungen besitzen

Python Tutor zeigt stärker den zeitlichen Ablauf eines Programms. Memory Graph
zeigt stärker die Struktur der Objekte im Speicher.

---

### Git und Versionsverwaltung

#### Learn Git Branching

[Learn Git Branching – deutsche Version](https://learngitbranching.js.org/?locale=de_DE)

Learn Git Branching ist eine interaktive Lernplattform für Git.

Man kann dort Git-Befehle direkt ausprobieren und sieht grafisch, wie sich
Branches und Commits verändern.

Behandelt werden zum Beispiel:

- `git branch`
- `git switch`
- `git checkout`
- `git merge`
- `git rebase`
- `git cherry-pick`

Die Seite eignet sich besonders gut, um Branches und Zusammenführungen
verständlich zu lernen.

---

#### Pro Git

[Pro Git – offizielles Git-Handbuch](https://git-scm.com/book/en/v2)

Pro Git ist ein kostenloses und umfangreiches Fachbuch über Git.

Es erklärt unter anderem:

- Git-Repositories
- Commits
- Branches
- Remotes
- GitHub-Verbindungen
- Merges
- Rebasing
- Tags
- die interne Arbeitsweise von Git

Das Buch eignet sich sowohl zum Lernen als auch zum Nachschlagen.

---

### Tastatur und Benutzereingaben

#### Auf eine Eingabe warten

[Pierian Training – How to Wait for a Keypress in Python](https://pieriantraining.com/how-to-wait-for-a-keypress-in-python/)

Diese Seite zeigt verschiedene Möglichkeiten, ein Python-Programm anzuhalten,
bis eine Taste gedrückt oder eine Eingabe bestätigt wurde.

Für einfache Konsolenprogramme eignet sich häufig:

```python
input("Drücke Enter, um fortzufahren.")
