"""
PySide6 – Workshop 05
Model/View-Programmierung I

Workshop:
Ein kleines Adressbuch mit QListView und QStringListModel.

Dieses Programm demonstriert die grundlegende Model/View-Architektur
von Qt.

Die Anwendung enthält:

- ein QMainWindow als Hauptfenster,
- ein QStringListModel als Datenmodell,
- eine QListView zur Darstellung der Kontakte,
- einen Add-Button,
- einen Edit-Button,
- einen Remove-Button,
- eine Statusleiste mit der Anzahl der Kontakte,
- eine QComboBox als optionales Stretch-Goal.

Wichtige Lernziele:

- Model und View voneinander unterscheiden,
- QStringListModel verwenden,
- QListView mit einem Model verbinden,
- Daten im Model verändern,
- QModelIndex verstehen,
- die aktuelle Auswahl einer View auslesen,
- Buttons abhängig von der Auswahl aktivieren,
- mehrere Views mit demselben Model verbinden.

GRUNDIDEE:

    MODEL
      |
      | enthält die Daten
      |
      v
    QStringListModel
      |
      | wird dargestellt von
      |
      +--------------------+
      |                    |
      v                    v
    QListView           QComboBox
"""


# ============================================================
# 1. IMPORTE
# ============================================================

import sys


# QStringListModel gehört zu QtCore.
#
# Es ist ein fertiges Qt-Model für eine einfache Liste
# von Strings.
from PySide6.QtCore import QStringListModel


# Alle Widgets, die wir für unser Adressbuch benötigen.
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QListView,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QInputDialog,
    QMessageBox,
    QComboBox,
)


# ============================================================
# 2. HAUPTFENSTER
# ============================================================

class AddressBookWindow(QMainWindow):
    """
    Hauptfenster unseres kleinen Adressbuchs.

    Der wichtigste Punkt dieser Klasse ist die Trennung zwischen:

    MODEL:
        self.model

        Enthält die eigentlichen Kontaktdaten.

    VIEW:
        self.list_view

        Zeigt die Daten des Models an.

    Die View besitzt also nicht selbst unsere Kontaktliste.

    Änderungen werden am Model durchgeführt.
    Die View aktualisiert sich anschließend automatisch.
    """

    def __init__(self):
        """
        Initialisiert das Adressbuch.

        Hier werden:

        - das Hauptfenster eingerichtet,
        - das QStringListModel erzeugt,
        - die QListView erzeugt,
        - Model und View verbunden,
        - Add/Edit/Remove-Buttons erstellt,
        - Signals und Slots verbunden,
        - die Statusleiste initialisiert.
        """

        super().__init__()


        # ====================================================
        # 3. FENSTER KONFIGURIEREN
        # ====================================================

        self.setWindowTitle(
            "Address Book"
        )

        self.resize(
            450,
            400
        )


        # ====================================================
        # 4. ZENTRALES WIDGET
        # ====================================================

        # Bei QMainWindow legen wir unser eigenes QWidget
        # als zentralen Inhaltsbereich an.
        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )


        # ====================================================
        # 5. HAUPTLAYOUT
        # ====================================================

        # Die Kontaktliste soll oben stehen.
        #
        # Die Buttons kommen darunter.
        #
        # Deshalb verwenden wir ein vertikales Layout.
        main_layout = QVBoxLayout(
            central_widget
        )


        # ====================================================
        # 6. MODEL ERSTELLEN
        # ====================================================

        # Jetzt kommt das wichtigste neue Objekt:
        #
        # QStringListModel
        #
        # Dieses Model kann eine Liste von Strings verwalten.
        #
        # Wir geben ihm zunächst einige Beispielkontakte.
        self.model = QStringListModel(
            [
                "Anna Schmidt",
                "Ben Müller",
                "Clara Fischer",
            ]
        )


        # ====================================================
        # 7. VIEW ERSTELLEN
        # ====================================================

        # QListView ist die Darstellung unserer Liste.
        #
        # Wichtig:
        #
        # QListView enthält NICHT unsere eigentlichen Daten.
        #
        # Sie zeigt lediglich Daten aus einem Model an.
        self.list_view = QListView()


        # ====================================================
        # 8. MODEL UND VIEW VERBINDEN
        # ====================================================

        # Mit setModel() sagen wir der QListView:
        #
        # "Zeige die Daten aus diesem Model an."
        self.list_view.setModel(
            self.model
        )


        # Die View kommt in unser Layout.
        main_layout.addWidget(
            self.list_view
        )


        # ====================================================
        # 9. BUTTON-LAYOUT
        # ====================================================

        # Add, Edit und Remove sollen nebeneinander stehen.
        #
        # Deshalb verwenden wir ein horizontales Layout.
        button_layout = QHBoxLayout()


        # ====================================================
        # 10. ADD-BUTTON
        # ====================================================

        self.add_button = QPushButton(
            "Add"
        )


        button_layout.addWidget(
            self.add_button
        )


        # ====================================================
        # 11. EDIT-BUTTON
        # ====================================================

        self.edit_button = QPushButton(
            "Edit"
        )


        button_layout.addWidget(
            self.edit_button
        )


        # ====================================================
        # 12. REMOVE-BUTTON
        # ====================================================

        self.remove_button = QPushButton(
            "Remove"
        )


        button_layout.addWidget(
            self.remove_button
        )


        # Button-Zeile in das Hauptlayout einfügen.
        main_layout.addLayout(
            button_layout
        )


        # ====================================================
        # 13. STRETCH-GOAL:
        # ZWEITE VIEW AUF DASSELBE MODEL
        # ====================================================

        # Eine QComboBox kann ebenfalls ein Model verwenden.
        #
        # Das ist ein sehr schönes Beispiel für Model/View:
        #
        # EIN Model
        #
        # aber ZWEI unterschiedliche Darstellungen.
        self.contact_combo = QComboBox()


        # Dieselben Daten werden auch hier angezeigt.
        self.contact_combo.setModel(
            self.model
        )


        main_layout.addWidget(
            self.contact_combo
        )


        # ====================================================
        # 14. SIGNALS UND SLOTS
        # ====================================================

        # Klick auf Add:
        #
        # -> add_contact()
        self.add_button.clicked.connect(
            self.add_contact
        )


        # Klick auf Edit:
        #
        # -> edit_contact()
        self.edit_button.clicked.connect(
            self.edit_contact
        )


        # Klick auf Remove:
        #
        # -> remove_contact()
        self.remove_button.clicked.connect(
            self.remove_contact
        )


        # ====================================================
        # 15. AUSWAHL ÜBERWACHEN
        # ====================================================

        # selectionModel() verwaltet die aktuelle Auswahl
        # innerhalb der QListView.
        #
        # selectionChanged wird ausgelöst, wenn der Benutzer
        # einen anderen Kontakt auswählt.
        self.list_view.selectionModel().selectionChanged.connect(
            self.update_button_states
        )


        # ====================================================
        # 16. ANFANGSZUSTAND DER BUTTONS
        # ====================================================

        # Beim Programmstart ist normalerweise noch kein
        # Kontakt ausgewählt.
        #
        # Deshalb sollen Edit und Remove zunächst deaktiviert sein.
        self.update_button_states()


        # ====================================================
        # 17. STATUSLEISTE INITIALISIEREN
        # ====================================================

        self.update_status_bar()


    # ========================================================
    # 18. KONTAKT HINZUFÜGEN
    # ========================================================

    def add_contact(self):
        """
        Fügt einen neuen Kontakt zum Model hinzu.

        Der Name wird über einen QInputDialog abgefragt.

        Wichtig:

        Wir verändern NICHT direkt die QListView.

        Stattdessen:

            Model lesen
                ↓
            Daten verändern
                ↓
            Model aktualisieren
                ↓
            View aktualisiert sich automatisch
        """

        # QInputDialog.getText() öffnet einen kleinen Dialog
        # mit einem Texteingabefeld.
        #
        # Wir erhalten zwei Werte zurück:
        #
        # name:
        #     eingegebener Text
        #
        # ok:
        #     True  -> Benutzer bestätigt
        #     False -> Benutzer bricht ab
        name, ok = QInputDialog.getText(
            self,
            "Add Contact",
            "Name:",
        )


        # Wenn der Benutzer Cancel drückt:
        if not ok:
            return


        # Leerzeichen am Anfang und Ende entfernen.
        name = name.strip()


        # Leeren Namen nicht hinzufügen.
        if not name:
            return


        # ====================================================
        # MODEL AUSLESEN
        # ====================================================

        # stringList() gibt uns die aktuelle Liste
        # der Strings aus dem Model.
        contacts = self.model.stringList()


        # ====================================================
        # DATEN VERÄNDERN
        # ====================================================

        contacts.append(
            name
        )


        # ====================================================
        # MODEL AKTUALISIEREN
        # ====================================================

        # Jetzt geben wir die veränderte Liste wieder
        # an das Model zurück.
        self.model.setStringList(
            contacts
        )


        # Statusleiste aktualisieren.
        self.update_status_bar()


    # ========================================================
    # 19. KONTAKT BEARBEITEN
    # ========================================================

    def edit_contact(self):
        """
        Bearbeitet den aktuell ausgewählten Kontakt.

        Dazu benötigen wir zuerst den QModelIndex der
        aktuellen Auswahl.

        Über diesen Index können wir herausfinden:

        - welche Zeile ausgewählt ist,
        - welche Daten dort stehen.
        """

        # currentIndex() liefert den aktuell ausgewählten
        # QModelIndex.
        index = self.list_view.currentIndex()


        # Prüfen, ob der Index gültig ist.
        if not index.isValid():
            return


        # ====================================================
        # AKTUELLEN NAMEN AUS DEM MODEL LESEN
        # ====================================================

        # data(index) liest die Daten an dieser Position.
        current_name = self.model.data(
            index
        )


        # Dialog öffnen.
        #
        # text=current_name sorgt dafür, dass der bisherige
        # Name bereits im Eingabefeld steht.
        new_name, ok = QInputDialog.getText(
            self,
            "Edit Contact",
            "Name:",
            text=current_name,
        )


        # Benutzer hat Cancel gedrückt.
        if not ok:
            return


        new_name = new_name.strip()


        # Leeren Namen nicht übernehmen.
        if not new_name:
            return


        # ====================================================
        # MODEL DIREKT VERÄNDERN
        # ====================================================

        # setData() verändert die Daten an einem QModelIndex.
        #
        # Danach informiert das Model die angeschlossenen Views
        # automatisch über die Änderung.
        self.model.setData(
            index,
            new_name
        )


        # Statusleiste aktualisieren.
        self.update_status_bar()


    # ========================================================
    # 20. KONTAKT LÖSCHEN
    # ========================================================

    def remove_contact(self):
        """
        Entfernt den aktuell ausgewählten Kontakt.

        Vor dem Löschen wird mit QMessageBox nachgefragt.

        Auch hier verändern wir wieder das Model
        und nicht direkt die View.
        """

        # Aktuelle Auswahl.
        index = self.list_view.currentIndex()


        # Keine gültige Auswahl?
        if not index.isValid():
            return


        # Name des ausgewählten Kontakts lesen.
        name = self.model.data(
            index
        )


        # ====================================================
        # SICHERHEITSABFRAGE
        # ====================================================

        answer = QMessageBox.question(
            self,
            "Remove Contact",
            f"Remove '{name}'?",
            (
                QMessageBox.StandardButton.Yes
                | QMessageBox.StandardButton.No
            ),
            QMessageBox.StandardButton.No,
        )


        # Wenn der Benutzer nicht Yes auswählt:
        if answer != QMessageBox.StandardButton.Yes:
            return


        # ====================================================
        # ZEILENNUMMER ERMITTELN
        # ====================================================

        # QModelIndex.row() liefert die Zeile.
        #
        # Beispiel:
        #
        # Anna   -> row 0
        # Ben    -> row 1
        # Clara  -> row 2
        row = index.row()


        # ====================================================
        # ZEILE AUS DEM MODEL ENTFERNEN
        # ====================================================

        # removeRow() entfernt eine Zeile aus dem Model.
        self.model.removeRow(
            row
        )


        # Button-Zustände aktualisieren.
        self.update_button_states()


        # Statusleiste aktualisieren.
        self.update_status_bar()


    # ========================================================
    # 21. BUTTON-ZUSTÄNDE AKTUALISIEREN
    # ========================================================

    def update_button_states(self, *args):
        """
        Aktiviert oder deaktiviert Edit und Remove.

        Edit und Remove sollen nur verfügbar sein,
        wenn tatsächlich ein Kontakt ausgewählt wurde.

        *args erlaubt dieser Methode, auch als Slot für ein
        Signal verwendet zu werden, das Argumente mitsendet,
        obwohl wir diese Argumente hier nicht benötigen.
        """

        # Aktuell ausgewählten Index holen.
        index = self.list_view.currentIndex()


        # True, wenn eine gültige Auswahl existiert.
        has_selection = index.isValid()


        # Edit aktivieren/deaktivieren.
        self.edit_button.setEnabled(
            has_selection
        )


        # Remove aktivieren/deaktivieren.
        self.remove_button.setEnabled(
            has_selection
        )


    # ========================================================
    # 22. STATUSLEISTE AKTUALISIEREN
    # ========================================================

    def update_status_bar(self):
        """
        Zeigt die aktuelle Anzahl der Kontakte an.

        Beispiel:

            3 contacts

        Die Anzahl wird direkt aus dem Model ermittelt.
        """

        # rowCount() gibt die Anzahl der Zeilen
        # des Models zurück.
        count = self.model.rowCount()


        self.statusBar().showMessage(
            f"{count} contacts"
        )


# ============================================================
# 23. QAPPLICATION ERSTELLEN
# ============================================================

app = QApplication(
    sys.argv
)


# ============================================================
# 24. ADRESSBUCH ERZEUGEN
# ============================================================

window = AddressBookWindow()


# ============================================================
# 25. FENSTER ANZEIGEN
# ============================================================

window.show()


# ============================================================
# 26. EVENT-LOOP STARTEN
# ============================================================

sys.exit(
    app.exec()
)