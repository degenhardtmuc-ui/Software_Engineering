"""
PySide6 – Session 01
Workshop: Persönliche Profilkarte

Dieses Programm erstellt eine einfache grafische Benutzeroberfläche (GUI)
mit PySide6.

Die Anwendung enthält:
- ein Hauptfenster,
- eine Überschrift,
- drei Beschriftungen (QLabel),
- drei Eingabefelder (QLineEdit),
- einen Button (QPushButton).

Die Positionierung der Widgets erfolgt mit setGeometry().

Der Button besitzt in dieser ersten Session absichtlich noch keine Funktion.
Die Verbindung eines Buttons mit einer Aktion wird später mit
Signals und Slots umgesetzt.

Wichtige Lernziele:
- QApplication verstehen
- QWidget als Hauptfenster verwenden
- Parent-Child-Beziehungen kennenlernen
- QLabel, QLineEdit und QPushButton verwenden
- Widgets mit setGeometry() positionieren
- window.show() verstehen
- die Qt Event-Loop mit app.exec() starten
"""


# ============================================================
# 1. IMPORTE
# ============================================================

# Das Python-Modul "sys" wird benötigt, um:
# - sys.argv an QApplication zu übergeben
# - das Programm später mit sys.exit() sauber zu beenden
import sys


# Aus PySide6.QtWidgets importieren wir alle GUI-Bausteine,
# die wir für unsere Profilkarte benötigen.
from PySide6.QtWidgets import (
    QApplication,   # Verwaltet die gesamte GUI-Anwendung
    QWidget,        # Basis-Widget; wird hier als Hauptfenster verwendet
    QLabel,         # Zeigt Text im Fenster an
    QLineEdit,      # Einzeiliges Texteingabefeld
    QPushButton,    # Anklickbarer Button
)


# ============================================================
# 2. QAPPLICATION ERSTELLEN
# ============================================================

# QApplication ist das zentrale Objekt unserer PySide6-Anwendung.
#
# Jede normale PySide6-GUI benötigt genau eine QApplication-Instanz.
#
# QApplication kümmert sich unter anderem um:
# - die Kommunikation mit dem Betriebssystem,
# - Maus- und Tastaturereignisse,
# - die Verwaltung der Fenster,
# - die Event-Loop.
#
# sys.argv enthält mögliche Kommandozeilenargumente und wird
# an Qt weitergegeben.
app = QApplication(sys.argv)


# ============================================================
# 3. HAUPTFENSTER ERSTELLEN
# ============================================================

# QWidget ist die Basisklasse vieler sichtbarer Elemente in Qt.
#
# Da dieses QWidget keinen Parent besitzt, wird es hier als
# eigenständiges Hauptfenster verwendet.
window = QWidget()


# setWindowTitle() bestimmt den Text, der oben in der
# Titelleiste unseres Fensters angezeigt wird.
window.setWindowTitle("Daniel Degenhardt - Profilkarte")


# resize(Breite, Höhe)
#
# Das Fenster bekommt eine Startgröße von:
#
# 360 Pixel Breite
# 220 Pixel Höhe
window.resize(360, 220)


# ============================================================
# 4. ÜBERSCHRIFT ERSTELLEN
# ============================================================

# QLabel wird verwendet, um Text anzuzeigen.
#
# Der Text "<b>Meine Profilkarte</b>" enthält einfaches HTML.
# <b> bedeutet "bold" und stellt den Text fett dar.
#
# parent=window bedeutet:
# Das Label gehört zu unserem Hauptfenster.
#
# window = Parent
# title_label = Child
title_label = QLabel(
    "<b>Meine Profilkarte</b>",
    parent=window
)


# setGeometry(x, y, Breite, Höhe)
#
# x = Abstand vom linken Fensterrand
# y = Abstand vom oberen Fensterrand
#
# Das Label beginnt also:
# 20 Pixel von links
# 15 Pixel von oben
#
# und bekommt:
# 320 Pixel Breite
# 30 Pixel Höhe
title_label.setGeometry(20, 15, 320, 30)


# ============================================================
# 5. NAME – LABEL UND EINGABEFELD
# ============================================================

# Dieses QLabel zeigt lediglich die Beschriftung "Name:" an.
#
# Durch parent=window wird das Label als Child-Widget
# in unserem Hauptfenster dargestellt.
name_label = QLabel(
    "Name:",
    parent=window
)


# Position des Labels:
#
# x = 20
# y = 55
# Breite = 110
# Höhe = 24
name_label.setGeometry(20, 55, 110, 24)


# QLineEdit erzeugt ein einzeiliges Texteingabefeld.
#
# Der Benutzer kann hier später seinen Namen eingeben.
name_edit = QLineEdit(
    parent=window
)


# Das Eingabefeld wird rechts neben dem Label positioniert.
#
# Beide besitzen denselben y-Wert (55).
#
# Dadurch befinden sie sich sauber in einer Zeile.
name_edit.setGeometry(140, 55, 190, 24)


# ============================================================
# 6. E-MAIL – LABEL UND EINGABEFELD
# ============================================================

# Beschriftung für das E-Mail-Eingabefeld.
email_label = QLabel(
    "E-Mail:",
    parent=window
)


# Das zweite Label wird 40 Pixel unterhalb des ersten
# Labels positioniert.
email_label.setGeometry(20, 95, 110, 24)


# QLineEdit für die Eingabe der E-Mail-Adresse.
email_edit = QLineEdit(
    parent=window
)


# Das Eingabefeld steht wieder rechts neben seinem Label.
email_edit.setGeometry(140, 95, 190, 24)


# ============================================================
# 7. PROGRAMMIERSPRACHE – LABEL UND EINGABEFELD
# ============================================================

# Das dritte QLabel beschreibt das Eingabefeld für die
# Lieblingsprogrammiersprache.
language_label = QLabel(
    "Programmiersprache:",
    parent=window
)


# Auch dieses Label folgt unserem Raster.
#
# y-Werte:
#
# Name:                  55
# E-Mail:                95
# Programmiersprache:   135
#
# Der Abstand beträgt damit jeweils 40 Pixel.
language_label.setGeometry(20, 135, 110, 24)


# Das dritte Texteingabefeld.
#
# Hier könnte der Benutzer beispielsweise eingeben:
#
# Python
# Java
# C++
# JavaScript
language_edit = QLineEdit(
    parent=window
)


# Position rechts neben der Beschriftung.
language_edit.setGeometry(140, 135, 190, 24)


# ============================================================
# 8. BUTTON ERSTELLEN
# ============================================================

# QPushButton erzeugt einen anklickbaren Button.
#
# Der sichtbare Text auf dem Button lautet:
# "Profil speichern"
#
# WICHTIG:
# Der Button besitzt in dieser Session absichtlich noch
# keine Funktion.
#
# Später kann ein Klick über Signals und Slots mit einer
# Python-Funktion verbunden werden.
button = QPushButton(
    "Profil speichern",
    parent=window
)


# Der Button wird unterhalb der Eingabefelder positioniert.
#
# x = 140
# y = 175
# Breite = 190
# Höhe = 30
button.setGeometry(140, 175, 190, 30)


# ============================================================
# 9. HAUPTFENSTER SICHTBAR MACHEN
# ============================================================

# Das Fenster wurde weiter oben bereits erzeugt.
#
# Ein neu erzeugtes QWidget ist aber nicht automatisch sichtbar.
#
# Erst show() sagt Qt:
#
# "Zeige dieses Fenster auf dem Bildschirm an."
window.show()


# ============================================================
# 10. EVENT-LOOP STARTEN
# ============================================================

# app.exec() startet die sogenannte Event-Loop.
#
# Die Event-Loop wartet während der gesamten Laufzeit
# des Programms auf Ereignisse ("Events").
#
# Beispiele für Events:
#
# - Mausklick
# - Tastendruck
# - Texteingabe
# - Fenster verschieben
# - Fenster vergrößern/verkleinern
# - Fenster schließen
#
# Vereinfacht funktioniert die Event-Loop so:
#
# WARTEN
#   ↓
# Ereignis?
#   ↓
# Ereignis verarbeiten
#   ↓
# wieder WARTEN
#
# Ohne app.exec() würde unsere GUI nicht dauerhaft auf
# Benutzeraktionen reagieren.
#
# sys.exit() sorgt anschließend dafür, dass der Exit-Code
# von Qt sauber an das Betriebssystem weitergegeben wird.
sys.exit(app.exec())