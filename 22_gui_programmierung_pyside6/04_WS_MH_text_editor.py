"""
PySide6 – Workshop 04
Hauptfenster und Dialoge: Ein echter Texteditor

Dieses Programm erstellt einen kleinen, aber bereits tatsächlich
benutzbaren Texteditor mit PySide6.

Die Anwendung enthält:

- ein QMainWindow als Hauptfenster,
- einen QPlainTextEdit als zentralen Editor,
- eine Menüleiste,
- ein File-Menü,
- eine Toolbar,
- QActions für New, Open, Save und Quit,
- Standard-Tastenkürzel,
- QFileDialog zum Öffnen und Speichern von Dateien,
- eine Statusleiste,
- Dirty-Tracking für ungespeicherte Änderungen,
- QMessageBox zum Schutz vor Datenverlust,
- eine Hilfsmethode maybe_save(),
- optional ein überschriebenes closeEvent().

Wichtige Lernziele:

- QMainWindow verstehen
- setCentralWidget() verwenden
- QAction verstehen
- QAction in Menü und Toolbar wiederverwenden
- QFileDialog verwenden
- QMessageBox verwenden
- Dateien mit Python lesen und schreiben
- Dirty-Tracking verstehen
- Benutzerentscheidungen Save / Discard / Cancel behandeln
- closeEvent() überschreiben
"""


# ============================================================
# 1. IMPORTE
# ============================================================

# sys benötigen wir wie bisher für:
#
# - sys.argv
# - sys.exit()
import sys


# Path erleichtert uns die Arbeit mit Dateipfaden.
#
# Beispiel:
#
# /Users/daniel/test.txt
#
# Path kann daraus bequem nur:
#
# test.txt
#
# ermitteln.
from pathlib import Path


# QKeySequence enthält standardisierte Tastenkürzel.
#
# Beispiele:
#
# New  -> Ctrl+N / Cmd+N
# Open -> Ctrl+O / Cmd+O
# Save -> Ctrl+S / Cmd+S
from PySide6.QtGui import (
    QAction,
    QKeySequence,
)


# Die benötigten Qt-Widgets.
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPlainTextEdit,
    QFileDialog,
    QMessageBox,
)


# ============================================================
# 2. EDITOR-FENSTER
# ============================================================

class EditorWindow(QMainWindow):
    """
    Hauptfenster unseres Texteditors.

    Diese Klasse erbt von QMainWindow.

    QMainWindow ist speziell für klassische Desktop-Anwendungen
    gedacht.

    Es besitzt bereits Bereiche für:

    - Menüleiste
    - Toolbars
    - zentrales Widget
    - Statusleiste

    Unser eigentliches Texteingabefeld wird später mit
    setCentralWidget() in die Mitte des Fensters gesetzt.
    """

    def __init__(self):
        """
        Initialisiert das Editor-Fenster.

        Hier werden:

        - der Zustand der Anwendung angelegt,
        - der Texteditor erzeugt,
        - Dirty-Tracking eingerichtet,
        - Menü und Toolbar aufgebaut,
        - Actions erstellt,
        - die Statusleiste initialisiert.
        """

        super().__init__()


        # ====================================================
        # 3. GRUNDZUSTAND
        # ====================================================

        # Am Anfang wurde noch keine Datei geöffnet.
        #
        # Deshalb gibt es noch keinen Dateipfad.
        self.current_path = None


        # dirty bedeutet:
        #
        # Gibt es Änderungen, die noch NICHT gespeichert wurden?
        #
        # False:
        # Alles gespeichert.
        #
        # True:
        # Ungespeicherte Änderungen vorhanden.
        self.dirty = False


        # Fenstertitel für eine neue, noch unbenannte Datei.
        self.setWindowTitle("Untitled — Editor")


        # ====================================================
        # 4. TEXTEDITOR
        # ====================================================

        # QPlainTextEdit ist ein mehrzeiliges Texteingabefeld.
        #
        # Es eignet sich gut für normalen Text bzw. Quellcode.
        self.editor = QPlainTextEdit()


        # Wenn sich der Text verändert, sendet QPlainTextEdit
        # das Signal:
        #
        # textChanged
        #
        # Dieses verbinden wir mit unserer Methode:
        #
        # on_text_changed
        self.editor.textChanged.connect(
            self.on_text_changed
        )


        # ====================================================
        # 5. CENTRAL WIDGET
        # ====================================================

        # QMainWindow funktioniert anders als unser bisheriges
        # QWidget.
        #
        # Das große Haupt-Widget in der Mitte wird über
        # setCentralWidget() festgelegt.
        self.setCentralWidget(
            self.editor
        )


        # ====================================================
        # 6. STATUSLEISTE
        # ====================================================

        # QMainWindow besitzt bereits eine Statusleiste.
        #
        # showMessage() zeigt dort einen Text an.
        self.statusBar().showMessage(
            "Ready"
        )


        # ====================================================
        # 7. ACTION: NEW
        # ====================================================

        # QAction beschreibt eine Aktion bzw. einen Befehl.
        #
        # Eine QAction kann gleichzeitig in:
        #
        # - einem Menü
        # - einer Toolbar
        #
        # verwendet werden.
        self.new_action = QAction(
            "New",
            self
        )


        # Standard-Tastenkürzel für "Neue Datei".
        self.new_action.setShortcut(
            QKeySequence.StandardKey.New
        )


        # Wenn die Action ausgelöst wird:
        #
        # -> new_file()
        self.new_action.triggered.connect(
            self.new_file
        )


        # ====================================================
        # 8. ACTION: OPEN
        # ====================================================

        self.open_action = QAction(
            "Open…",
            self
        )


        self.open_action.setShortcut(
            QKeySequence.StandardKey.Open
        )


        self.open_action.triggered.connect(
            self.open_file
        )


        # ====================================================
        # 9. ACTION: SAVE
        # ====================================================

        self.save_action = QAction(
            "Save",
            self
        )


        self.save_action.setShortcut(
            QKeySequence.StandardKey.Save
        )


        self.save_action.triggered.connect(
            self.save_file
        )


        # ====================================================
        # 10. ACTION: QUIT
        # ====================================================

        self.quit_action = QAction(
            "Quit",
            self
        )


        # Laut Kursunterlage soll Quit explizit Ctrl+Q bekommen.
        self.quit_action.setShortcut(
            "Ctrl+Q"
        )


        self.quit_action.triggered.connect(
            self.quit_editor
        )


        # ====================================================
        # 11. FILE-MENÜ
        # ====================================================

        # menuBar() liefert die Menüleiste des QMainWindow.
        #
        # addMenu() fügt dort ein Menü hinzu.
        file_menu = self.menuBar().addMenu(
            "File"
        )


        # Jetzt verwenden wir unsere Actions im Menü.
        file_menu.addAction(
            self.new_action
        )

        file_menu.addAction(
            self.open_action
        )

        file_menu.addAction(
            self.save_action
        )


        # Eine optische Trennlinie.
        file_menu.addSeparator()


        file_menu.addAction(
            self.quit_action
        )


        # ====================================================
        # 12. TOOLBAR
        # ====================================================

        # QMainWindow kann Toolbars verwalten.
        toolbar = self.addToolBar(
            "File"
        )


        # Wir verwenden DIESELBEN Actions erneut.
        toolbar.addAction(
            self.new_action
        )

        toolbar.addAction(
            self.open_action
        )

        toolbar.addAction(
            self.save_action
        )


    # ========================================================
    # 13. DIRTY-TRACKING
    # ========================================================

    def on_text_changed(self):
        """
        Wird ausgeführt, sobald sich der Text im Editor verändert.

        dirty wird auf True gesetzt.

        Damit weiß das Programm:

        Es existieren Änderungen, die noch nicht gespeichert wurden.
        """

        self.dirty = True

        self.statusBar().showMessage(
            "Modified"
        )


    # ========================================================
    # 14. NEUE DATEI
    # ========================================================

    def new_file(self):
        """
        Erstellt ein neues leeres Dokument.

        Bevor der vorhandene Text gelöscht wird, wird mit
        maybe_save() geprüft, ob ungespeicherte Änderungen
        vorhanden sind.

        Gibt der Benutzer Cancel zurück, wird die Aktion
        abgebrochen.
        """

        # Schutz vor Datenverlust.
        if not self.maybe_save():
            return


        # Editor leeren.
        self.editor.clear()


        # Neue Datei besitzt noch keinen Pfad.
        self.current_path = None


        # Nach dem Leeren hat unser textChanged-Signal
        # möglicherweise dirty=True gesetzt.
        #
        # Deshalb setzen wir es anschließend wieder zurück.
        self.dirty = False


        # Fenstertitel zurücksetzen.
        self.setWindowTitle(
            "Untitled — Editor"
        )


        self.statusBar().showMessage(
            "New file"
        )


    # ========================================================
    # 15. DATEI ÖFFNEN
    # ========================================================

    def open_file(self):
        """
        Öffnet eine Textdatei.

        Ablauf:

        1. Ungespeicherte Änderungen prüfen.
        2. QFileDialog anzeigen.
        3. Abbruch des Dialogs erkennen.
        4. Datei lesen.
        5. Text im Editor anzeigen.
        6. Dateipfad speichern.
        7. Fenstertitel aktualisieren.
        8. dirty wieder auf False setzen.
        """

        # Erst prüfen:
        #
        # Darf die aktuelle Datei verlassen werden?
        if not self.maybe_save():
            return


        # QFileDialog öffnet den nativen Datei-Auswahldialog.
        #
        # Rückgabe:
        #
        # path   -> ausgewählter Dateipfad
        # filter -> ausgewählter Dateifilter
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "Text Files (*.txt);;All Files (*)",
        )


        # Wenn der Benutzer Cancel gedrückt hat,
        # ist path leer.
        #
        # Dann machen wir NICHTS.
        if not path:
            return


        # Datei öffnen und lesen.
        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()


        # Text in den Editor schreiben.
        #
        # WICHTIG:
        #
        # setPlainText() löst textChanged aus.
        #
        # Dadurch wird dirty zunächst automatisch True.
        self.editor.setPlainText(text)


        # Aktuellen Dateipfad speichern.
        self.current_path = path


        # Weil die Datei gerade frisch geladen wurde,
        # gibt es KEINE ungespeicherten Änderungen.
        #
        # Deshalb setzen wir dirty NACH setPlainText()
        # wieder auf False.
        self.dirty = False


        # Fenstertitel aktualisieren.
        self.update_window_title()


        self.statusBar().showMessage(
            f"Opened {Path(path).name}"
        )


    # ========================================================
    # 16. DATEI SPEICHERN
    # ========================================================

    def save_file(self):
        """
        Speichert den aktuellen Text.

        Wenn bereits ein Dateipfad existiert, wird direkt
        in diese Datei geschrieben.

        Wenn current_path None ist, wurde die Datei noch nie
        gespeichert.

        Dann verhält sich Save automatisch wie "Save As".
        """

        # Gibt es noch keinen Dateipfad?
        if self.current_path is None:

            # Dann benötigen wir zunächst einen Dateinamen.
            path, _ = QFileDialog.getSaveFileName(
                self,
                "Save File",
                "",
                "Text Files (*.txt);;All Files (*)",
            )


            # Benutzer hat den Speicherdialog abgebrochen.
            if not path:
                return False


            # Gewählten Pfad merken.
            self.current_path = path


        # Aktuellen Editorinhalt auslesen.
        text = self.editor.toPlainText()


        # Datei zum Schreiben öffnen.
        with open(
            self.current_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(text)


        # Jetzt ist alles gespeichert.
        self.dirty = False


        # Fenstertitel aktualisieren.
        self.update_window_title()


        self.statusBar().showMessage(
            f"Saved {Path(self.current_path).name}"
        )


        # True bedeutet:
        #
        # Speichern war erfolgreich.
        return True


    # ========================================================
    # 17. FENSTERTITEL AKTUALISIEREN
    # ========================================================

    def update_window_title(self):
        """
        Aktualisiert den Fenstertitel.

        Existiert ein Dateipfad:

            beispiel.txt — Editor

        Existiert noch kein Dateipfad:

            Untitled — Editor
        """

        if self.current_path:

            filename = Path(
                self.current_path
            ).name

            self.setWindowTitle(
                f"{filename} — Editor"
            )

        else:

            self.setWindowTitle(
                "Untitled — Editor"
            )


    # ========================================================
    # 18. MAYBE_SAVE
    # ========================================================

    def maybe_save(self):
        """
        Prüft, ob ungespeicherte Änderungen vorhanden sind.

        Rückgabe:
            True:
                Die aufrufende Aktion darf fortfahren.

            False:
                Die aufrufende Aktion muss abgebrochen werden.

        Möglichkeiten des Benutzers:

        SAVE
            Änderungen speichern und anschließend fortfahren.

        DISCARD
            Änderungen verwerfen und fortfahren.

        CANCEL
            Gesamte Aktion abbrechen.
        """

        # Wenn nichts verändert wurde, müssen wir
        # den Benutzer überhaupt nicht fragen.
        if not self.dirty:
            return True


        # QMessageBox.question zeigt eine Frage an.
        answer = QMessageBox.question(
            self,
            "Unsaved Changes",
            "The document has unsaved changes.\n"
            "Do you want to save them?",
            (
                QMessageBox.StandardButton.Save
                | QMessageBox.StandardButton.Discard
                | QMessageBox.StandardButton.Cancel
            ),
            QMessageBox.StandardButton.Save,
        )


        # ----------------------------------------------------
        # Benutzer wählt SAVE
        # ----------------------------------------------------

        if answer == QMessageBox.StandardButton.Save:

            # save_file() liefert True oder False.
            #
            # False kann beispielsweise entstehen,
            # wenn der Benutzer den Save-Dialog abbricht.
            return self.save_file()


        # ----------------------------------------------------
        # Benutzer wählt CANCEL
        # ----------------------------------------------------

        if answer == QMessageBox.StandardButton.Cancel:

            return False


        # ----------------------------------------------------
        # Benutzer wählt DISCARD
        # ----------------------------------------------------

        # Wenn weder Save noch Cancel gewählt wurde,
        # bleibt hier Discard.
        #
        # Die aufrufende Aktion darf fortfahren.
        return True


    # ========================================================
    # 19. QUIT
    # ========================================================

    def quit_editor(self):
        """
        Beendet die Anwendung.

        Vorher werden ungespeicherte Änderungen geprüft.
        """

        if not self.maybe_save():
            return


        QApplication.quit()


    # ========================================================
    # 20. STRETCH-GOAL: CLOSE EVENT
    # ========================================================

    def closeEvent(self, event):
        """
        Wird von Qt automatisch aufgerufen, wenn der Benutzer
        versucht, das Fenster über das X zu schließen.

        Ohne diese Methode würde unsere Sicherheitsabfrage nur
        beim Menüpunkt Quit greifen.

        Mit closeEvent() schützen wir auch das normale Schließen
        des Fensters.

        event.accept():
            Fenster darf geschlossen werden.

        event.ignore():
            Schließen wird abgebrochen.
        """

        if self.maybe_save():

            event.accept()

        else:

            event.ignore()


# ============================================================
# 21. QAPPLICATION
# ============================================================

app = QApplication(sys.argv)


# ============================================================
# 22. EDITOR-FENSTER ERZEUGEN
# ============================================================

window = EditorWindow()


# ============================================================
# 23. STARTGRÖSSE
# ============================================================

window.resize(
    600,
    400
)


# ============================================================
# 24. FENSTER ANZEIGEN
# ============================================================

window.show()


# ============================================================
# 25. EVENT-LOOP
# ============================================================

sys.exit(app.exec())