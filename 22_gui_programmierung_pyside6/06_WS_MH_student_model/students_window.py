"""
Workshop 06 – Model/View II: Eigene Models
Datei: students_window.py

Diese Datei enthält die grafische Benutzeroberfläche.

Verwendet werden:

- QTableView
- StudentModel
- Add student
- Remove selected
- Statusleisten-Label für den Notendurchschnitt

Architektur:

    Student-Objekte
          ↓
    StudentModel
          ↓
     QTableView
"""

import sys


from PySide6.QtWidgets import (
    QApplication,
    QAbstractItemView,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)


# Unsere eigenen Klassen aus student_model.py.
from student_model import (
    Student,
    StudentModel,
)


# ============================================================
# 1. HAUPTFENSTER
# ============================================================

class StudentsWindow(QMainWindow):
    """
    Hauptfenster für unsere Studenten-Tabelle.

    Das Fenster übernimmt:

    - Darstellung
    - Student hinzufügen
    - Student entfernen
    - Durchschnitt anzeigen

    Die Daten selbst verwaltet StudentModel.
    """


    # ========================================================
    # 2. KONSTRUKTOR
    # ========================================================

    def __init__(self):
        """
        Erstellt Model, Tabelle, Buttons und Statusanzeige.
        """

        super().__init__()


        # ----------------------------------------------------
        # Fenster
        # ----------------------------------------------------

        self.setWindowTitle(
            "Students"
        )


        self.resize(
            720,
            450
        )


        # ----------------------------------------------------
        # Zentrales Widget
        # ----------------------------------------------------

        central_widget = QWidget()


        self.setCentralWidget(
            central_widget
        )


        main_layout = QVBoxLayout(
            central_widget
        )


        # ====================================================
        # 3. STARTDATEN
        # ====================================================

        students = [

            Student(
                "Ada Lovelace",
                "s001",
                91.5,
                True,
            ),

            Student(
                "Grace Hopper",
                "s002",
                88.0,
                True,
            ),

        ]


        # ====================================================
        # 4. EIGENES MODEL
        # ====================================================

        self.model = StudentModel(
            students
        )


        # ====================================================
        # 5. QTABLEVIEW
        # ====================================================

        self.table = QTableView()


        # Model mit View verbinden.
        self.table.setModel(
            self.model
        )


        # Wenn etwas ausgewählt wird,
        # wählen wir die ganze Zeile.
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )


        # Nur eine Zeile gleichzeitig auswählen.
        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )


        # Spaltenbreite an Inhalt anpassen.
        self.table.resizeColumnsToContents()


        main_layout.addWidget(
            self.table
        )


        # ====================================================
        # 6. BUTTON-ZEILE
        # ====================================================

        button_layout = QHBoxLayout()


        self.add_button = QPushButton(
            "Add student"
        )


        self.remove_button = QPushButton(
            "Remove selected"
        )


        button_layout.addWidget(
            self.add_button
        )


        button_layout.addWidget(
            self.remove_button
        )


        main_layout.addLayout(
            button_layout
        )


        # ====================================================
        # 7. STATUSLEISTEN-LABEL
        # ====================================================

        self.average_label = QLabel()


        self.statusBar().addPermanentWidget(
            self.average_label
        )


        # ====================================================
        # 8. SIGNALS UND SLOTS
        # ====================================================

        self.add_button.clicked.connect(
            self.add_student
        )


        self.remove_button.clicked.connect(
            self.remove_selected
        )


        # Wenn ein Wert im Model geändert wird:
        #
        # Durchschnitt neu berechnen.
        self.model.dataChanged.connect(
            self.update_average
        )


        # Stretch-Goal:
        #
        # Model meldet ungültige Eingabe.
        self.model.validation_error.connect(
            self.show_validation_error
        )


        # Durchschnitt direkt beim Start berechnen.
        self.update_average()


    # ========================================================
    # 9. NÄCHSTE STUDENT-ID
    # ========================================================

    def next_student_id(self):
        """
        Erzeugt automatisch die nächste Studenten-ID.

        Beispiele:

            s001
            s002
            s003
        """

        return (
            f"s{self.model.rowCount() + 1:03d}"
        )


    # ========================================================
    # 10. STUDENT HINZUFÜGEN
    # ========================================================

    def add_student(self):
        """
        Fügt einen neuen Studenten hinzu.

        Ablauf:

        1. Name abfragen.
        2. Neue ID erzeugen.
        3. Student-Objekt erstellen.
        4. Über das Model hinzufügen.
        5. Durchschnitt aktualisieren.
        """

        name, ok = QInputDialog.getText(
            self,
            "Add student",
            "Name:",
        )


        # Cancel?
        if not ok:

            return


        name = name.strip()


        # Leeren Namen verhindern.
        if not name:

            self.statusBar().showMessage(
                "Name must not be empty.",
                3000,
            )

            return


        # Student erzeugen.
        student = Student(
            name=name,
            student_id=self.next_student_id(),
            grade=0.0,
            enrolled=True,
        )


        # Über das MODEL hinzufügen.
        self.model.add_student(
            student
        )


        # Spalten eventuell neu anpassen.
        self.table.resizeColumnsToContents()


        # Durchschnitt aktualisieren.
        self.update_average()


    # ========================================================
    # 11. AUSGEWÄHLTEN STUDENTEN ENTFERNEN
    # ========================================================

    def remove_selected(self):
        """
        Entfernt die aktuell ausgewählte Studenten-Zeile.

        Wichtig:

        currentIndex()
            ↓
        isValid()
            ↓
        index.row()
            ↓
        model.remove_student(row)
        """

        # Aktuelle Auswahl.
        index = self.table.currentIndex()


        # Keine gültige Auswahl?
        if not index.isValid():

            self.statusBar().showMessage(
                "Please select a student first.",
                3000,
            )

            return


        # Zeile über das Model entfernen.
        self.model.remove_student(
            index.row()
        )


        # Durchschnitt aktualisieren.
        self.update_average()


    # ========================================================
    # 12. DURCHSCHNITT BERECHNEN
    # ========================================================

    def update_average(self, *args):
        """
        Berechnet den Durchschnitt der Grades aller
        eingeschriebenen Studenten.

        Nur:

            enrolled == True

        wird berücksichtigt.

        *args bedeutet:
        Qt darf Argumente mitsenden, die wir hier nicht brauchen.
        """

        enrolled_students = [

            student

            for student in self.model.students()

            if student.enrolled

        ]


        # Niemand eingeschrieben?
        if not enrolled_students:

            self.average_label.setText(
                "Average grade (enrolled): —"
            )

            return


        # Summe aller relevanten Noten.
        total = sum(

            student.grade

            for student in enrolled_students

        )


        # Durchschnitt.
        average = (
            total
            / len(enrolled_students)
        )


        self.average_label.setText(
            f"Average grade (enrolled): {average:.2f}"
        )


    # ========================================================
    # 13. VALIDIERUNGSFEHLER
    # ========================================================

    def show_validation_error(self, message):
        """
        Zeigt eine Fehlermeldung für einige Sekunden
        in der Statusleiste.

        Beispiel:

            Grade must be between 0 and 100.
        """

        self.statusBar().showMessage(
            message,
            4000,
        )


# ============================================================
# 14. MAIN-FUNKTION
# ============================================================

def main():
    """
    Startet die komplette PySide6-Anwendung.
    """

    # Eine QApplication erzeugen.
    app = QApplication(
        sys.argv
    )


    # Unser Fenster erzeugen.
    window = StudentsWindow()


    # Fenster anzeigen.
    window.show()


    # Event-Loop starten.
    return app.exec()


# ============================================================
# 15. PROGRAMMSTART
# ============================================================

if __name__ == "__main__":

    sys.exit(
        main()
    )