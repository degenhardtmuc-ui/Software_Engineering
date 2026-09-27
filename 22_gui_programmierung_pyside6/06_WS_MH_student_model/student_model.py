"""
Workshop 06 – Model/View II: Eigene Models
Datei: student_model.py

Diese Datei enthält:
- die Student-Dataclass
- ein eigenes StudentModel auf Basis von QAbstractTableModel

Spalten:
0 -> Name
1 -> Student ID
2 -> Grade
3 -> Enrolled
"""

from dataclasses import dataclass

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    Qt,
    Signal,
)


# ============================================================
# 1. STUDENT-DATENKLASSE
# ============================================================

@dataclass
class Student:
    """
    Datenobjekt für einen einzelnen Studenten.

    Attributes:
        name (str):
            Name des Studenten.

        student_id (str):
            Studenten-ID.

        grade (float):
            Punktzahl zwischen 0 und 100.

        enrolled (bool):
            True = eingeschrieben
            False = nicht eingeschrieben
    """

    name: str
    student_id: str
    grade: float = 0.0
    enrolled: bool = True


# ============================================================
# 2. EIGENES TABELLENMODEL
# ============================================================

class StudentModel(QAbstractTableModel):
    """
    Eigenes Tabellenmodell für Student-Objekte.

    Das Model ist der Adapter zwischen:

        Python-Student-Objekten
                ↓
          StudentModel
                ↓
           QTableView

    Qt fragt dieses Model zum Beispiel:

    - Wie viele Zeilen gibt es?
    - Wie viele Spalten gibt es?
    - Was steht in einer Zelle?
    - Darf die Zelle bearbeitet werden?
    - Ist die Checkbox aktiviert?
    """

    # Überschriften unserer vier Spalten.
    HEADERS = [
        "Name",
        "Student ID",
        "Grade",
        "Enrolled",
    ]

    # Stretch-Goal:
    # Bei einer ungültigen Note kann das Model dem Fenster
    # eine Fehlermeldung senden.
    validation_error = Signal(str)


    # ========================================================
    # 3. KONSTRUKTOR
    # ========================================================

    def __init__(self, students=None, parent=None):
        """
        Initialisiert das Model.

        Args:
            students:
                Optionale Liste mit Student-Objekten.

            parent:
                Optionales Qt-Parent-Objekt.
        """

        super().__init__(parent)

        # Unsere eigentliche Datenliste.
        self._students = list(students) if students else []


    # ========================================================
    # 4. ANZAHL DER ZEILEN
    # ========================================================

    def rowCount(self, parent=QModelIndex()):
        """
        Gibt die Anzahl der Tabellenzeilen zurück.

        Ein Student = eine Zeile.
        """

        if parent.isValid():
            return 0

        return len(self._students)


    # ========================================================
    # 5. ANZAHL DER SPALTEN
    # ========================================================

    def columnCount(self, parent=QModelIndex()):
        """
        Gibt die Anzahl der Tabellenspalten zurück.
        """

        if parent.isValid():
            return 0

        return len(self.HEADERS)


    # ========================================================
    # 6. DATEN AN DIE VIEW LIEFERN
    # ========================================================

    def data(
        self,
        index,
        role=Qt.ItemDataRole.DisplayRole,
    ):
        """
        Liefert den Inhalt einer Tabellenzelle.

        Wichtige Roles:

        DisplayRole:
            Was wird normal angezeigt?

        EditRole:
            Welcher Wert erscheint beim Bearbeiten?

        CheckStateRole:
            Ist eine Checkbox angehakt?

        ToolTipRole:
            Welcher Tooltip wird angezeigt?
        """

        # Ungültige Zelle?
        if not index.isValid():
            return None


        # Student anhand der Zeile holen.
        student = self._students[index.row()]

        # Spalte bestimmen.
        column = index.column()


        # ----------------------------------------------------
        # NORMALER ANZEIGE- UND EDITIERWERT
        # ----------------------------------------------------

        if role in (
            Qt.ItemDataRole.DisplayRole,
            Qt.ItemDataRole.EditRole,
        ):

            # Spalte 0: Name
            if column == 0:
                return student.name

            # Spalte 1: Student ID
            if column == 1:
                return student.student_id

            # Spalte 2: Grade
            if column == 2:
                return f"{student.grade:.1f}"

            # Spalte 3 wird als Checkbox angezeigt.
            if column == 3:
                return None


        # ----------------------------------------------------
        # CHECKBOX
        # ----------------------------------------------------

        if (
            role == Qt.ItemDataRole.CheckStateRole
            and column == 3
        ):

            if student.enrolled:
                return Qt.CheckState.Checked

            return Qt.CheckState.Unchecked


        # ----------------------------------------------------
        # TOOLTIP FÜR GRADE
        # ----------------------------------------------------

        if (
            role == Qt.ItemDataRole.ToolTipRole
            and column == 2
        ):

            return "Final grade, 0–100"


        # Alle nicht unterstützten Roles:
        return None


    # ========================================================
    # 7. SPALTENÜBERSCHRIFTEN
    # ========================================================

    def headerData(
        self,
        section,
        orientation,
        role=Qt.ItemDataRole.DisplayRole,
    ):
        """
        Liefert die horizontalen Spaltenüberschriften.
        """

        if (
            role == Qt.ItemDataRole.DisplayRole
            and orientation == Qt.Orientation.Horizontal
            and 0 <= section < len(self.HEADERS)
        ):

            return self.HEADERS[section]


        return None


    # ========================================================
    # 8. FLAGS
    # ========================================================

    def flags(self, index):
        """
        Legt fest, was der Benutzer mit einer Zelle machen darf.

        Spalten 0–2:
            auswählbar
            aktiviert
            editierbar

        Spalte 3:
            auswählbar
            aktiviert
            Checkbox anklickbar
        """

        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags


        # Grundrechte einer normalen Zelle.
        base = (
            Qt.ItemFlag.ItemIsEnabled
            | Qt.ItemFlag.ItemIsSelectable
        )


        # Enrolled-Spalte:
        if index.column() == 3:

            return (
                base
                | Qt.ItemFlag.ItemIsUserCheckable
            )


        # Name, Student ID und Grade:
        return (
            base
            | Qt.ItemFlag.ItemIsEditable
        )


    # ========================================================
    # 9. DATEN ÄNDERN
    # ========================================================

    def setData(
        self,
        index,
        value,
        role=Qt.ItemDataRole.EditRole,
    ):
        """
        Übernimmt Änderungen aus der Tabelle in unsere Daten.

        Stretch-Goal:
        Grades außerhalb von 0–100 werden abgelehnt.

        Returns:
            True:
                Änderung akzeptiert.

            False:
                Änderung abgelehnt.
        """

        if not index.isValid():
            return False


        student = self._students[index.row()]

        column = index.column()


        # ----------------------------------------------------
        # NORMALE TEXT-/ZAHLENBEARBEITUNG
        # ----------------------------------------------------

        if role == Qt.ItemDataRole.EditRole:


            # Name
            if column == 0:

                new_name = str(value).strip()

                if not new_name:

                    self.validation_error.emit(
                        "Name must not be empty."
                    )

                    return False

                student.name = new_name


            # Student ID
            elif column == 1:

                new_id = str(value).strip()

                if not new_id:

                    self.validation_error.emit(
                        "Student ID must not be empty."
                    )

                    return False

                student.student_id = new_id


            # Grade
            elif column == 2:

                try:

                    new_grade = float(value)

                except (TypeError, ValueError):

                    self.validation_error.emit(
                        "Grade must be a number between 0 and 100."
                    )

                    return False


                # Stretch-Goal:
                if not 0 <= new_grade <= 100:

                    self.validation_error.emit(
                        "Grade must be between 0 and 100."
                    )

                    return False


                student.grade = new_grade


            else:

                return False


            # ------------------------------------------------
            # VIEW ÜBER DIE ÄNDERUNG INFORMIEREN
            # ------------------------------------------------

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
        # CHECKBOX ÄNDERN
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
    # 10. STUDENT HINZUFÜGEN
    # ========================================================

    def add_student(self, student):
        """
        Fügt einen Studenten korrekt zum Model hinzu.

        Wichtig:

        Nicht einfach nur:

            self._students.append(...)

        sondern:

            beginInsertRows()
            append()
            endInsertRows()

        Dadurch weiß die View von der neuen Zeile.
        """

        row = len(self._students)


        self.beginInsertRows(
            QModelIndex(),
            row,
            row,
        )


        self._students.append(
            student
        )


        self.endInsertRows()


    # ========================================================
    # 11. STUDENT ENTFERNEN
    # ========================================================

    def remove_student(self, row):
        """
        Entfernt einen Studenten korrekt aus dem Model.

        Returns:
            True bei Erfolg.
        """

        if not 0 <= row < len(self._students):

            return False


        self.beginRemoveRows(
            QModelIndex(),
            row,
            row,
        )


        del self._students[row]


        self.endRemoveRows()


        return True


    # ========================================================
    # 12. STUDENTENLISTE ZURÜCKGEBEN
    # ========================================================

    def students(self):
        """
        Gibt eine Kopie der Studentenliste zurück.

        So muss das Fenster nicht direkt auf:

            self._students

        zugreifen.
        """

        return list(self._students)