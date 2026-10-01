"""
PySide6 – Workshop 07
Rückgängig machen mit dem Command Pattern

Datei:
    student_model.py

Diese Datei enthält:
- Student-Dataclass
- QUndoCommand-Klassen für Undo/Redo
- StudentModel(QAbstractTableModel)

Pflichtteil:
- AddStudentCommand
- RemoveStudentCommand
- ChangeGradeCommand
- QUndoStack-Anbindung über StudentModel.set_undo_stack()

Stretch-Goal:
- ChangeNameCommand mit id() und mergeWith()

Wichtiges Muster:
    setData()      = öffentliche Tür, die Änderungen AUFZEICHNET
    set_grade()    = interne Tür, die Änderungen ANWENDET
    set_name()     = interne Tür, die Änderungen ANWENDET

Commands rufen niemals setData() auf.
"""

from dataclasses import dataclass

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
    Signal,
)
from PySide6.QtGui import QUndoCommand


# ============================================================
# 1. DATENKLASSE
# ============================================================

@dataclass
class Student:
    """
    Repräsentiert einen Studenten.

    Attributes:
        name (str):
            Name des Studenten.

        student_id (str):
            Studenten-ID.

        grade (float):
            Punktzahl zwischen 0 und 100.

        enrolled (bool):
            True = eingeschrieben.
    """

    name: str
    student_id: str
    grade: float = 0.0
    enrolled: bool = True


# ============================================================
# 2. COMMAND: NOTE ÄNDERN
# ============================================================

class ChangeGradeCommand(QUndoCommand):
    """
    Macht eine Notenänderung rückgängig bzw. wiederholbar.

    Der Command speichert sowohl den alten als auch den neuen Wert.
    """

    def __init__(self, model, row, new_grade, old_grade):
        """Speichert alles, was redo() und undo() benötigen."""
        super().__init__(f"Change grade of row {row + 1}")

        self.model = model
        self.row = row
        self.new_grade = new_grade
        self.old_grade = old_grade

    def redo(self):
        """Wendet die neue Note an."""
        self.model.set_grade(
            self.row,
            self.new_grade,
        )

    def undo(self):
        """Stellt die alte Note wieder her."""
        self.model.set_grade(
            self.row,
            self.old_grade,
        )


# ============================================================
# 3. COMMAND: STUDENT HINZUFÜGEN
# ============================================================

class AddStudentCommand(QUndoCommand):
    """
    Fügt einen Studenten als undoable Command hinzu.

    Der Einfüge-Index wird gespeichert, damit Undo/Redo immer
    dieselbe Tabellenposition verwendet.
    """

    def __init__(self, model, student, row=None):
        """Speichert Model, Student und Zielzeile."""
        super().__init__(f"Add {student.name}")

        self.model = model
        self.student = student

        if row is None:
            row = model.rowCount()

        self.row = row

    def redo(self):
        """Fügt den Studenten an der gespeicherten Zeile ein."""
        self.model.insert_student(
            self.row,
            self.student,
        )

    def undo(self):
        """Entfernt genau den zuvor eingefügten Studenten."""
        self.model.remove_student(
            self.row
        )


# ============================================================
# 4. COMMAND: STUDENT ENTFERNEN
# ============================================================

class RemoveStudentCommand(QUndoCommand):
    """
    Entfernt einen Studenten und kann ihn am gleichen Index
    wiederherstellen.

    Das Speichern des ursprünglichen Index ist wichtig.
    """

    def __init__(self, model, row):
        """Merkt sich Zeile und Student vor dem Entfernen."""
        student = model.student_at(row)

        super().__init__(f"Remove {student.name}")

        self.model = model
        self.row = row
        self.student = student

    def redo(self):
        """Entfernt die gespeicherte Zeile."""
        self.model.remove_student(
            self.row
        )

    def undo(self):
        """Fügt den Studenten am ursprünglichen Index wieder ein."""
        self.model.insert_student(
            self.row,
            self.student,
        )


# ============================================================
# 5. STRETCH-GOAL: NAME ÄNDERN + MERGING
# ============================================================

class ChangeNameCommand(QUndoCommand):
    """
    Undoable Namensänderung.

    Mehrere aufeinanderfolgende Namensänderungen derselben Zeile
    können mit mergeWith() zu einem Undo-Schritt verschmelzen.
    """

    COMMAND_ID = 1

    def __init__(self, model, row, new_name, old_name):
        """Speichert alten und neuen Namen."""
        super().__init__(f"Change name of row {row + 1}")

        self.model = model
        self.row = row
        self.new_name = new_name
        self.old_name = old_name

    def redo(self):
        """Wendet den neuen Namen an."""
        self.model.set_name(
            self.row,
            self.new_name,
        )

    def undo(self):
        """Stellt den ursprünglichen Namen wieder her."""
        self.model.set_name(
            self.row,
            self.old_name,
        )

    def id(self):
        """
        Liefert eine feste Command-ID.

        Nur Commands mit derselben ID kommen für Merging infrage.
        """
        return self.COMMAND_ID

    def mergeWith(self, other):
        """
        Verschmilzt aufeinanderfolgende Namensänderungen derselben
        Tabellenzeile.

        Der alte Name dieses Commands bleibt erhalten.
        Nur der neueste neue Name wird übernommen.
        """
        if not isinstance(other, ChangeNameCommand):
            return False

        if other.model is not self.model:
            return False

        if other.row != self.row:
            return False

        self.new_name = other.new_name

        return True


# ============================================================
# 6. EIGENES TABELLENMODEL
# ============================================================

class StudentModel(QAbstractTableModel):
    """
    Eigenes Tabellenmodell für Student-Objekte.

    Workshop-7-Erweiterung:
    Das Model kennt optional einen QUndoStack.

    setData() ist die öffentliche Aufzeichnungstür.
    set_grade()/set_name() sind interne Anwendungstüren.
    """

    HEADERS = [
        "Name",
        "Student ID",
        "Grade",
        "Enrolled",
    ]

    validation_error = Signal(str)

    def __init__(
        self,
        students=None,
        undo_stack=None,
        parent=None,
    ):
        """Initialisiert Daten und optionalen Undo-Stack."""
        super().__init__(parent)

        self._students = (
            list(students)
            if students
            else []
        )

        self.undo_stack = undo_stack

    def set_undo_stack(self, undo_stack):
        """Verbindet das Model nachträglich mit einem QUndoStack."""
        self.undo_stack = undo_stack


    # ========================================================
    # 7. MODEL-GRÖSSE
    # ========================================================

    def rowCount(self, parent=QModelIndex()):
        """Gibt die Anzahl der Tabellenzeilen zurück."""
        if parent.isValid():
            return 0

        return len(self._students)

    def columnCount(self, parent=QModelIndex()):
        """Gibt die Anzahl der Tabellenspalten zurück."""
        if parent.isValid():
            return 0

        return len(self.HEADERS)


    # ========================================================
    # 8. DATEN AUSLESEN
    # ========================================================

    def data(
        self,
        index,
        role=Qt.ItemDataRole.DisplayRole,
    ):
        """Liefert den Inhalt einer Tabellenzelle."""
        if not index.isValid():
            return None

        student = self._students[
            index.row()
        ]

        column = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if column == 0:
                return student.name

            if column == 1:
                return student.student_id

            if column == 2:
                return f"{student.grade:.1f}"

        if role == Qt.ItemDataRole.EditRole:
            if column == 0:
                return student.name

            if column == 1:
                return student.student_id

            if column == 2:
                return student.grade

        if (
            role == Qt.ItemDataRole.CheckStateRole
            and column == 3
        ):
            return (
                Qt.CheckState.Checked
                if student.enrolled
                else Qt.CheckState.Unchecked
            )

        if (
            role == Qt.ItemDataRole.ToolTipRole
            and column == 2
        ):
            return "Final grade, 0-100"

        return None

    def headerData(
        self,
        section,
        orientation,
        role=Qt.ItemDataRole.DisplayRole,
    ):
        """Liefert die horizontalen Spaltenüberschriften."""
        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation == Qt.Orientation.Horizontal
            and 0 <= section < len(self.HEADERS)
        ):
            return self.HEADERS[
                section
            ]

        return None


    # ========================================================
    # 9. FLAGS
    # ========================================================

    def flags(self, index):
        """Legt fest, was der Benutzer mit einer Zelle tun darf."""
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags

        base = (
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsSelectable
        )

        if index.column() == 3:
            return (
                base
                | Qt.ItemFlag.ItemIsUserCheckable
            )

        return (
            base
            | Qt.ItemFlag.ItemIsEditable
        )


    # ========================================================
    # 10. ÖFFENTLICHE TÜR: ÄNDERUNG AUFZEICHNEN
    # ========================================================

    def setData(
        self,
        index,
        value,
        role=Qt.ItemDataRole.EditRole,
    ):
        """
        Nimmt Bearbeitungen aus der QTableView entgegen.

        Grade:
            wird über ChangeGradeCommand auf den Undo-Stack gelegt.

        Name:
            Stretch-Goal - wird über ChangeNameCommand auf den
            Undo-Stack gelegt und kann gemerged werden.

        Student ID und Enrolled:
            bleiben wie in Session 6 direkte Änderungen.
        """
        if not index.isValid():
            return False

        student = self._students[
            index.row()
        ]

        row = index.row()
        column = index.column()


        # ----------------------------------------------------
        # NAME -> STRETCH-COMMAND
        # ----------------------------------------------------

        if (
            role == Qt.ItemDataRole.EditRole
            and column == 0
        ):
            new_name = str(value).strip()

            if not new_name:
                self.validation_error.emit(
                    "Name must not be empty."
                )
                return False

            old_name = student.name

            if new_name == old_name:
                return True

            if self.undo_stack is None:
                self.set_name(
                    row,
                    new_name,
                )
            else:
                self.undo_stack.push(
                    ChangeNameCommand(
                        self,
                        row,
                        new_name,
                        old_name,
                    )
                )

            return True


        # ----------------------------------------------------
        # STUDENT-ID -> DIREKT WIE SESSION 6
        # ----------------------------------------------------

        if (
            role == Qt.ItemDataRole.EditRole
            and column == 1
        ):
            new_id = str(value).strip()

            if not new_id:
                self.validation_error.emit(
                    "Student ID must not be empty."
                )
                return False

            student.student_id = new_id

            self.dataChanged.emit(
                index,
                index,
                [
                    Qt.ItemDataRole.DisplayRole,
                    Qt.ItemDataRole.EditRole,
                ],
            )

            return True


        # ----------------------------------------------------
        # GRADE -> COMMAND
        # ----------------------------------------------------

        if (
            role == Qt.ItemDataRole.EditRole
            and column == 2
        ):
            old_grade = student.grade

            try:
                new_grade = float(value)

            except (TypeError, ValueError):
                self.validation_error.emit(
                    "Grade must be a number between 0 and 100."
                )
                return False

            if not 0 <= new_grade <= 100:
                self.validation_error.emit(
                    "Grade must be between 0 and 100."
                )
                return False

            if new_grade == old_grade:
                return True

            if self.undo_stack is None:
                self.set_grade(
                    row,
                    new_grade,
                )
            else:
                self.undo_stack.push(
                    ChangeGradeCommand(
                        self,
                        row,
                        new_grade,
                        old_grade,
                    )
                )

            return True


        # ----------------------------------------------------
        # ENROLLED -> DIREKT WIE SESSION 6
        # ----------------------------------------------------

        if (
            role == Qt.ItemDataRole.CheckStateRole
            and column == 3
        ):
            student.enrolled = value in (
                Qt.CheckState.Checked,
                Qt.CheckState.Checked.value,
            )

            self.dataChanged.emit(
                index,
                index,
                [
                    Qt.ItemDataRole.CheckStateRole
                ],
            )

            return True

        return False


    # ========================================================
    # 11. INTERNE TÜR: ÄNDERUNGEN NUR ANWENDEN
    # ========================================================

    def set_grade(
        self,
        row,
        new_grade,
    ):
        """
        Wendet eine Note an und benachrichtigt die View.

        Diese Methode zeichnet NICHT auf.
        Commands dürfen sie deshalb gefahrlos aus redo()/undo()
        aufrufen.
        """
        if not 0 <= row < len(self._students):
            return False

        self._students[
            row
        ].grade = new_grade

        index = self.index(
            row,
            2,
        )

        self.dataChanged.emit(
            index,
            index,
            [
                Qt.ItemDataRole.DisplayRole,
                Qt.ItemDataRole.EditRole,
            ],
        )

        return True

    def set_name(
        self,
        row,
        new_name,
    ):
        """
        Wendet einen Namen an und benachrichtigt die View.

        Auch diese Methode zeichnet NICHT auf.
        """
        if not 0 <= row < len(self._students):
            return False

        self._students[
            row
        ].name = new_name

        index = self.index(
            row,
            0,
        )

        self.dataChanged.emit(
            index,
            index,
            [
                Qt.ItemDataRole.DisplayRole,
                Qt.ItemDataRole.EditRole,
            ],
        )

        return True


    # ========================================================
    # 12. STRUKTURELLE LOW-LEVEL-MUTATIONEN
    # ========================================================

    def insert_student(
        self,
        row,
        student,
    ):
        """
        Fügt einen Studenten an einer bestimmten Zeile ein.

        Diese Methode zeichnet selbst nichts auf.
        """
        if not 0 <= row <= len(self._students):
            return False

        self.beginInsertRows(
            QModelIndex(),
            row,
            row,
        )

        self._students.insert(
            row,
            student,
        )

        self.endInsertRows()

        return True

    def remove_student(
        self,
        row,
    ):
        """
        Entfernt einen Studenten an einer bestimmten Zeile.

        Diese Methode zeichnet selbst nichts auf.
        """
        if not 0 <= row < len(self._students):
            return None

        self.beginRemoveRows(
            QModelIndex(),
            row,
            row,
        )

        student = self._students.pop(
            row
        )

        self.endRemoveRows()

        return student


    # ========================================================
    # 13. ACCESSORS
    # ========================================================

    def student_at(
        self,
        row,
    ):
        """Gibt den Studenten einer bestimmten Zeile zurück."""
        return self._students[
            row
        ]

    def students(self):
        """Gibt eine Kopie der Studentenliste zurück."""
        return list(
            self._students
        )