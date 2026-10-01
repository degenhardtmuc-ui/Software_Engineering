"""
PySide6 – Workshop 07
Rückgängig machen mit dem Command Pattern

Datei:
    students_window.py

Diese Datei erweitert Workshop 6 um:
- QUndoStack
- Undo/Redo-Aktionen im Edit-Menü
- AddStudentCommand
- RemoveStudentCommand
- ChangeGradeCommand
- Clean-State-Sternchen im Fenstertitel
- Stretch-Goal: ChangeNameCommand mit Merging

Start:
    python students_window.py
"""

import sys

from PySide6.QtGui import (
    QKeySequence,
    QUndoStack,
)
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

from student_model import (
    AddStudentCommand,
    RemoveStudentCommand,
    Student,
    StudentModel,
)


# ============================================================
# 1. HAUPTFENSTER
# ============================================================

class StudentsWindow(QMainWindow):
    """Studenten-Tabelle mit Undo/Redo-Historie."""

    def __init__(self):
        """Erstellt Fenster, Undo-Stack, Model, View und UI."""
        super().__init__()

        self.base_title = "Students"

        self.setWindowTitle(
            self.base_title
        )

        self.resize(
            760,
            470,
        )


        # ====================================================
        # 2. QUNDOSTACK
        # ====================================================

        # Der Stack gehört dem Fenster.
        self.undo_stack = QUndoStack(
            self
        )

        # Clean-State-Signal.
        self.undo_stack.cleanChanged.connect(
            self.on_clean_changed
        )


        # ====================================================
        # 3. UNDO/REDO-ACTIONS
        # ====================================================

        self.undo_action = (
            self.undo_stack.createUndoAction(
                self,
                "&Undo",
            )
        )

        self.undo_action.setShortcut(
            QKeySequence.StandardKey.Undo
        )

        self.redo_action = (
            self.undo_stack.createRedoAction(
                self,
                "&Redo",
            )
        )

        self.redo_action.setShortcut(
            QKeySequence.StandardKey.Redo
        )

        edit_menu = self.menuBar().addMenu(
            "&Edit"
        )

        edit_menu.addAction(
            self.undo_action
        )

        edit_menu.addAction(
            self.redo_action
        )


        # ====================================================
        # 4. ZENTRALES WIDGET
        # ====================================================

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        main_layout = QVBoxLayout(
            central_widget
        )


        # ====================================================
        # 5. STARTDATEN
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
        # 6. MODEL MIT UNDO-STACK
        # ====================================================

        self.model = StudentModel(
            students=students,
            undo_stack=self.undo_stack,
        )


        # ====================================================
        # 7. QTABLEVIEW
        # ====================================================

        self.table = QTableView()

        self.table.setModel(
            self.model
        )

        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.table.resizeColumnsToContents()

        main_layout.addWidget(
            self.table
        )


        # ====================================================
        # 8. BUTTONS
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
        # 9. STATUSLEISTE
        # ====================================================

        self.average_label = QLabel()

        self.statusBar().addPermanentWidget(
            self.average_label
        )


        # ====================================================
        # 10. SIGNALS UND SLOTS
        # ====================================================

        self.add_button.clicked.connect(
            self.add_student
        )

        self.remove_button.clicked.connect(
            self.remove_selected
        )

        # Durchschnitt nach Zelländerungen und
        # strukturellen Änderungen aktualisieren.
        self.model.dataChanged.connect(
            self.update_average
        )

        self.model.rowsInserted.connect(
            self.update_average
        )

        self.model.rowsRemoved.connect(
            self.update_average
        )

        self.model.validation_error.connect(
            self.show_validation_error
        )


        # ====================================================
        # 11. CLEAN-STATE
        # ====================================================

        # Für diesen Workshop behandeln wir den Startzustand
        # als "zuletzt gespeicherten" Zustand.
        self.undo_stack.setClean()

        self.on_clean_changed(
            self.undo_stack.isClean()
        )

        self.update_average()


    # ========================================================
    # 12. NÄCHSTE STUDENT-ID
    # ========================================================

    def next_student_id(self):
        """
        Erzeugt eine neue Studenten-ID, ohne gelöschte IDs
        versehentlich doppelt zu vergeben.
        """
        numbers = []

        for student in self.model.students():
            student_id = student.student_id

            if (
                student_id.startswith("s")
                and student_id[1:].isdigit()
            ):
                numbers.append(
                    int(student_id[1:])
                )

        next_number = (
            max(
                numbers,
                default=0,
            )
            + 1
        )

        return (
            f"s{next_number:03d}"
        )


    # ========================================================
    # 13. ADD STUDENT -> COMMAND PUSHEN
    # ========================================================

    def add_student(self):
        """Erstellt einen Studenten und pusht AddStudentCommand."""
        name, ok = QInputDialog.getText(
            self,
            "Add student",
            "Name:",
        )

        if not ok:
            return

        name = name.strip()

        if not name:
            self.statusBar().showMessage(
                "Name must not be empty.",
                3000,
            )
            return

        student = Student(
            name=name,
            student_id=self.next_student_id(),
            grade=0.0,
            enrolled=True,
        )

        command = AddStudentCommand(
            self.model,
            student,
        )

        # push() ruft automatisch command.redo() auf.
        self.undo_stack.push(
            command
        )

        self.table.resizeColumnsToContents()


    # ========================================================
    # 14. REMOVE SELECTED -> COMMAND PUSHEN
    # ========================================================

    def remove_selected(self):
        """Pusht einen RemoveStudentCommand für die gewählte Zeile."""
        index = self.table.currentIndex()

        if not index.isValid():
            self.statusBar().showMessage(
                "Please select a student first.",
                3000,
            )
            return

        command = RemoveStudentCommand(
            self.model,
            index.row(),
        )

        self.undo_stack.push(
            command
        )


    # ========================================================
    # 15. DURCHSCHNITT
    # ========================================================

    def update_average(self, *args):
        """Berechnet den Durchschnitt eingeschriebener Studenten."""
        enrolled_students = [
            student
            for student in self.model.students()
            if student.enrolled
        ]

        if not enrolled_students:
            self.average_label.setText(
                "Average grade (enrolled): -"
            )
            return

        average = (
            sum(
                student.grade
                for student in enrolled_students
            )
            / len(enrolled_students)
        )

        self.average_label.setText(
            f"Average grade (enrolled): {average:.2f}"
        )


    # ========================================================
    # 16. CLEAN / DIRTY IM FENSTERTITEL
    # ========================================================

    def on_clean_changed(self, clean):
        """
        Zeigt ein Sternchen, sobald der Undo-Stack vom Clean-State
        abweicht.
        """
        if clean:
            self.setWindowTitle(
                self.base_title
            )
        else:
            self.setWindowTitle(
                self.base_title + " *"
            )


    # ========================================================
    # 17. VALIDIERUNGSFEHLER
    # ========================================================

    def show_validation_error(self, message):
        """Zeigt Model-Validierungsfehler in der Statusleiste."""
        self.statusBar().showMessage(
            message,
            4000,
        )


# ============================================================
# 18. PROGRAMMSTART
# ============================================================

def main():
    """Startet die PySide6-Anwendung."""
    app = QApplication(
        sys.argv
    )

    window = StudentsWindow()

    window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(
        main()
    )