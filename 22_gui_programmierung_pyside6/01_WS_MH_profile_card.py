import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
)

# --------------------------------------------------
# 1. PySide6-Anwendung erstellen
# --------------------------------------------------

app = QApplication(sys.argv)


# --------------------------------------------------
# 2. Hauptfenster erstellen
# --------------------------------------------------

window = QWidget()

window.setWindowTitle("Daniel Degenhardt - Profilkarte")

window.resize(360, 220)


# --------------------------------------------------
# 3. Überschrift
# --------------------------------------------------

title_label = QLabel("<b>Meine Profilkarte</b>", parent=window)

title_label.setGeometry(20, 15, 320, 30)


# --------------------------------------------------
# 4. Eingabefeld: Name
# --------------------------------------------------

name_label = QLabel("Name:", parent=window)

name_label.setGeometry(20, 55, 110, 24)


name_edit = QLineEdit(parent=window)

name_edit.setGeometry(140, 55, 190, 24)


# --------------------------------------------------
# 5. Eingabefeld: E-Mail
# --------------------------------------------------

email_label = QLabel("E-Mail:", parent=window)

email_label.setGeometry(20, 95, 110, 24)


email_edit = QLineEdit(parent=window)

email_edit.setGeometry(140, 95, 190, 24)


# --------------------------------------------------
# 6. Eingabefeld: Lieblingsprogrammiersprache
# --------------------------------------------------

language_label = QLabel(
    "Programmiersprache:",
    parent=window
)

language_label.setGeometry(20, 135, 110, 24)


language_edit = QLineEdit(parent=window)

language_edit.setGeometry(140, 135, 190, 24)


# --------------------------------------------------
# 7. Button
# --------------------------------------------------

button = QPushButton(
    "Profil speichern",
    parent=window
)

button.setGeometry(140, 175, 190, 30)


# --------------------------------------------------
# 8. Fenster anzeigen
# --------------------------------------------------

window.show()


# --------------------------------------------------
# 9. Event-Loop starten
# --------------------------------------------------

sys.exit(app.exec())

=======================================================

# Python startet
#     ↓
# QApplication wird erzeugt
#     ↓
# Fenster wird erzeugt
#     ↓
# Labels, Eingabefelder und Button werden erzeugt
#     ↓
# window.show()
#     ↓
# Fenster erscheint
#     ↓
# app.exec()
#     ↓
# EVENT-LOOP LÄUFT
#     ↓
#wartet auf Maus, Tastatur, Schließen usw.