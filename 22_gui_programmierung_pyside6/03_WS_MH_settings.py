"""
PySide6 – Workshop 03
Layouts und eine Widget-Tour

Workshop:
Settings-Dialog-Mockup für einen fiktiven Code-Editor.

In diesem Workshop bauen wir ein Einstellungsfenster mit mehreren
verschiedenen Qt-Widgets.

Das wichtigste neue Thema sind LAYOUTS.

Im Gegensatz zu den vorherigen Workshops verwenden wir NICHT mehr
setGeometry(), um jedes Widget mit festen Pixelkoordinaten zu
positionieren.

Stattdessen verwenden wir Layout-Manager.

Verwendete Layouts:
- QVBoxLayout
- QHBoxLayout
- QFormLayout

Verwendete Widgets:
- QWidget
- QGroupBox
- QSpinBox
- QComboBox
- QCheckBox
- QRadioButton
- QButtonGroup
- QPushButton
- QPlainTextEdit

Die Anwendung enthält drei Einstellungsbereiche:

1. Editor
2. Files
3. Keybindings

Der Save-Button liest die aktuellen Werte der Widgets aus
und gibt sie in der Konsole aus.

Stretch-Goal:
Unter "Files" wird zusätzlich ein QPlainTextEdit für ein
"Custom startup script" eingebaut.
"""


# ============================================================
# 1. IMPORTE
# ============================================================

# sys benötigen wir wieder für:
#
# - sys.argv
# - sys.exit()
import sys


# Aus PySide6.QtWidgets importieren wir alle Widgets
# und Layout-Klassen, die wir für diesen Workshop benötigen.
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QGroupBox,
    QSpinBox,
    QComboBox,
    QCheckBox,
    QRadioButton,
    QButtonGroup,
    QPushButton,
    QPlainTextEdit,
)


# ============================================================
# 2. EIGENE FENSTERKLASSE
# ============================================================

class SettingsWindow(QWidget):
    """
    Hauptfenster für die Einstellungen unseres fiktiven Code-Editors.

    SettingsWindow erbt von QWidget.

    Das Fenster besteht aus drei Bereichen:

    - Editor
    - Files
    - Keybindings

    Diese Bereiche werden jeweils mit einer QGroupBox dargestellt.

    Innerhalb der Group-Boxes verwenden wir wiederum eigene Layouts.

    Das bedeutet:

        Hauptfenster
            |
            +-- Hauptlayout
                  |
                  +-- Editor GroupBox
                  |
                  +-- Files GroupBox
                  |
                  +-- Keybindings GroupBox
                  |
                  +-- Save-Button

    Genau dieses Verschachteln von Layouts ist eines der wichtigsten
    Lernziele von Workshop 03.
    """

    def __init__(self):
        """
        Initialisiert das Settings-Fenster.

        Hier werden:

        - das Hauptfenster konfiguriert,
        - alle Widgets erstellt,
        - die drei Group-Boxes erstellt,
        - Layouts aufgebaut,
        - Widgets in die Layouts eingefügt,
        - der Save-Button mit einem Slot verbunden.
        """

        # --------------------------------------------------------
        # Konstruktor der Elternklasse QWidget aufrufen
        # --------------------------------------------------------

        super().__init__()


        # ========================================================
        # 3. HAUPTFENSTER
        # ========================================================

        # Titel des Fensters.
        self.setWindowTitle("Code Editor Settings")


        # Wir können weiterhin eine STARTGRÖSSE des Fensters festlegen.
        #
        # Wichtig:
        #
        # resize() für das Hauptfenster ist weiterhin erlaubt.
        #
        # Wir benutzen aber KEIN setGeometry() mehr für die
        # einzelnen Widgets.
        self.resize(500, 500)


        # ========================================================
        # 4. HAUPTLAYOUT
        # ========================================================

        # QVBoxLayout ordnet Elemente VERTIKAL an.
        #
        # Also:
        #
        # Element 1
        # Element 2
        # Element 3
        # Element 4
        #
        # QVBoxLayout(self) bedeutet gleichzeitig:
        #
        # Dieses Layout gehört zu unserem SettingsWindow.
        main_layout = QVBoxLayout(self)


        # Abstand zwischen den Elementen.
        main_layout.setSpacing(12)


        # Innenabstand:
        #
        # links, oben, rechts, unten
        main_layout.setContentsMargins(
            16,
            16,
            16,
            16
        )


        # ========================================================
        # 5. GROUPBOX "EDITOR"
        # ========================================================

        # Eine QGroupBox fasst logisch zusammengehörende
        # Einstellungen optisch zusammen.
        #
        # Sie bekommt einen sichtbaren Titel.
        editor_group = QGroupBox("Editor")


        # Für den Editor-Bereich verwenden wir ein QFormLayout.
        #
        # QFormLayout eignet sich besonders gut für:
        #
        # Label:       Eingabefeld
        # Label:       Eingabefeld
        # Label:       Eingabefeld
        #
        # Also genau für klassische Formulare.
        editor_form = QFormLayout(editor_group)


        # ========================================================
        # 6. SCHRIFTGRÖSSE
        # ========================================================

        # QSpinBox ist ein numerisches Eingabefeld.
        #
        # Der Benutzer kann:
        #
        # - Zahlen eingeben
        # - Pfeil hoch klicken
        # - Pfeil runter klicken
        self.font_size_spin = QSpinBox()


        # Sinnvoller Wertebereich für eine Schriftgröße.
        self.font_size_spin.setRange(
            8,
            48
        )


        # Startwert.
        self.font_size_spin.setValue(14)


        # addRow() fügt eine neue Zeile zum QFormLayout hinzu.
        #
        # Links:
        # "Font size:"
        #
        # Rechts:
        # unsere QSpinBox
        editor_form.addRow(
            "Font size:",
            self.font_size_spin
        )


        # ========================================================
        # 7. TAB-BREITE
        # ========================================================

        self.tab_width_spin = QSpinBox()


        # Mögliche Tab-Breite.
        self.tab_width_spin.setRange(
            1,
            8
        )


        # Typischer Startwert:
        self.tab_width_spin.setValue(4)


        editor_form.addRow(
            "Tab width:",
            self.tab_width_spin
        )


        # ========================================================
        # 8. FARBSCHEMA / THEME
        # ========================================================

        # QComboBox ist ein Dropdown-Menü.
        #
        # Der Benutzer kann genau einen Eintrag auswählen.
        self.theme_combo = QComboBox()


        # addItems() fügt mehrere Auswahlmöglichkeiten hinzu.
        self.theme_combo.addItems(
            [
                "Light",
                "Dark",
                "Monokai",
                "Solarized",
            ]
        )


        editor_form.addRow(
            "Color theme:",
            self.theme_combo
        )


        # ========================================================
        # 9. EDITOR-GRUPPE ZUM HAUPTLAYOUT HINZUFÜGEN
        # ========================================================

        main_layout.addWidget(editor_group)


        # ========================================================
        # 10. GROUPBOX "FILES"
        # ========================================================

        files_group = QGroupBox("Files")


        # Die Files-Einstellungen sollen einfach untereinander stehen.
        #
        # Deshalb verwenden wir hier ein QVBoxLayout.
        files_layout = QVBoxLayout(files_group)


        # ========================================================
        # 11. CHECKBOX "RESTORE LAST SESSION"
        # ========================================================

        # Eine QCheckBox repräsentiert eine unabhängige
        # Ja/Nein-Option.
        self.restore_session_checkbox = QCheckBox(
            "Restore last session"
        )


        # Beispiel:
        #
        # Die Option ist beim Start aktiviert.
        self.restore_session_checkbox.setChecked(True)


        files_layout.addWidget(
            self.restore_session_checkbox
        )


        # ========================================================
        # 12. CHECKBOX "AUTO-SAVE"
        # ========================================================

        self.auto_save_checkbox = QCheckBox(
            "Auto-save every minute"
        )


        # Auch diese Option können wir mit einem Startzustand versehen.
        self.auto_save_checkbox.setChecked(False)


        files_layout.addWidget(
            self.auto_save_checkbox
        )


        # ========================================================
        # 13. STRETCH-GOAL:
        # CUSTOM STARTUP SCRIPT
        # ========================================================

        # Laut Aufgabenstellung ist dieser Teil OPTIONAL.
        #
        # Wir bauen ihn trotzdem ein.
        #
        # QPlainTextEdit ist ein mehrzeiliges Texteingabefeld.
        self.startup_script_edit = QPlainTextEdit()


        # Placeholder-Text wird angezeigt, solange das Feld leer ist.
        self.startup_script_edit.setPlaceholderText(
            "Custom startup script"
        )


        # Wir begrenzen die Höhe etwas, damit das Feld nicht
        # unnötig groß wird.
        self.startup_script_edit.setMaximumHeight(80)


        files_layout.addWidget(
            self.startup_script_edit
        )


        # Files-GroupBox ins Hauptlayout einfügen.
        main_layout.addWidget(files_group)


        # ========================================================
        # 14. GROUPBOX "KEYBINDINGS"
        # ========================================================

        keybindings_group = QGroupBox(
            "Keybindings"
        )


        # Die drei Radio-Buttons sollen untereinander stehen.
        keybindings_layout = QVBoxLayout(
            keybindings_group
        )


        # ========================================================
        # 15. RADIO-BUTTONS
        # ========================================================

        self.default_radio = QRadioButton(
            "Default"
        )

        self.vim_radio = QRadioButton(
            "Vim"
        )

        self.emacs_radio = QRadioButton(
            "Emacs"
        )


        # Laut Aufgabenstellung soll "Default"
        # beim Start ausgewählt sein.
        self.default_radio.setChecked(True)


        # ========================================================
        # 16. QBUTTONGROUP
        # ========================================================

        # QButtonGroup sorgt dafür, dass unsere Radio-Buttons
        # logisch zu EINER Auswahlgruppe gehören.
        #
        # Das bedeutet:
        #
        # Es kann immer nur EIN Radio-Button aktiv sein.
        self.keybinding_group = QButtonGroup(self)


        # Jetzt fügen wir die Radio-Buttons der Gruppe hinzu.
        self.keybinding_group.addButton(
            self.default_radio
        )

        self.keybinding_group.addButton(
            self.vim_radio
        )

        self.keybinding_group.addButton(
            self.emacs_radio
        )


        # Die Buttons müssen zusätzlich noch in das sichtbare
        # Layout eingefügt werden.
        #
        # QButtonGroup ist nämlich KEIN sichtbares Layout.
        keybindings_layout.addWidget(
            self.default_radio
        )

        keybindings_layout.addWidget(
            self.vim_radio
        )

        keybindings_layout.addWidget(
            self.emacs_radio
        )


        # Keybindings-GroupBox ins Hauptlayout.
        main_layout.addWidget(
            keybindings_group
        )


        # ========================================================
        # 17. SAVE-BUTTON-ZEILE
        # ========================================================

        # Der Save-Button soll laut Aufgabenstellung
        # UNTEN RECHTS stehen.
        #
        # Dafür verwenden wir ein horizontales Layout.
        button_layout = QHBoxLayout()


        # addStretch() erzeugt gewissermaßen eine unsichtbare Feder.
        #
        # Sie nimmt den freien Platz ein.
        #
        # Dadurch wird der danach eingefügte Button
        # nach rechts geschoben.
        button_layout.addStretch()


        # Save-Button erstellen.
        save_button = QPushButton(
            "Save"
        )


        # Button ins horizontale Layout einfügen.
        button_layout.addWidget(
            save_button
        )


        # Das komplette horizontale Button-Layout
        # kommt wiederum in unser vertikales Hauptlayout.
        main_layout.addLayout(
            button_layout
        )


        # ========================================================
        # 18. SIGNAL UND SLOT
        # ========================================================

        # Wenn der Benutzer auf Save klickt,
        # soll unsere Methode save_settings() ausgeführt werden.
        #
        # clicked = Signal
        #
        # save_settings = Slot
        save_button.clicked.connect(
            self.save_settings
        )


    # ============================================================
    # 19. SAVE-SLOT
    # ============================================================

    def save_settings(self):
        """
        Liest alle aktuellen Einstellungen aus der Oberfläche.

        Die Werte werden anschließend in der Konsole ausgegeben.

        Verwendete Getter:

        QSpinBox:
            value()

        QComboBox:
            currentText()

        QCheckBox:
            isChecked()

        QRadioButton:
            isChecked()

        QPlainTextEdit:
            toPlainText()

        Wichtig:
        QPlainTextEdit verwendet NICHT .text().

        Für mehrzeilige Textfelder benötigen wir:
            .toPlainText()
        """


        # ========================================================
        # 20. EDITOR-EINSTELLUNGEN AUSLESEN
        # ========================================================

        font_size = self.font_size_spin.value()

        tab_width = self.tab_width_spin.value()

        theme = self.theme_combo.currentText()


        # ========================================================
        # 21. FILE-EINSTELLUNGEN AUSLESEN
        # ========================================================

        restore_session = (
            self.restore_session_checkbox.isChecked()
        )

        auto_save = (
            self.auto_save_checkbox.isChecked()
        )


        # Stretch-Goal:
        #
        # QPlainTextEdit wird mit toPlainText()
        # ausgelesen.
        startup_script = (
            self.startup_script_edit.toPlainText()
        )


        # ========================================================
        # 22. KEYBINDING BESTIMMEN
        # ========================================================

        # Wir prüfen, welcher Radio-Button aktiv ist.
        if self.vim_radio.isChecked():

            keybinding = "Vim"

        elif self.emacs_radio.isChecked():

            keybinding = "Emacs"

        else:

            # Default ist vorausgewählt.
            keybinding = "Default"


        # ========================================================
        # 23. AUSGABE IN DER KONSOLE
        # ========================================================

        print()
        print("=" * 40)
        print("CURRENT SETTINGS")
        print("=" * 40)

        print("Font size:", font_size)
        print("Tab width:", tab_width)
        print("Color theme:", theme)

        print("Restore last session:", restore_session)
        print("Auto-save every minute:", auto_save)

        print("Keybindings:", keybinding)

        print("Custom startup script:")
        print(startup_script)

        print("=" * 40)


# ============================================================
# 24. QAPPLICATION ERSTELLEN
# ============================================================

app = QApplication(sys.argv)


# ============================================================
# 25. SETTINGS-FENSTER ERZEUGEN
# ============================================================

window = SettingsWindow()


# ============================================================
# 26. FENSTER ANZEIGEN
# ============================================================

window.show()


# ============================================================
# 27. EVENT-LOOP STARTEN
# ============================================================

sys.exit(app.exec())