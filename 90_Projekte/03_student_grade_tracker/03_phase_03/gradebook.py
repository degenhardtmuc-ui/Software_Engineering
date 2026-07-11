"""Hauptmodul für die Verwaltung des Notenbuchs.

Dieses Modul enthält die Klasse GradeBook.

Die Klasse GradeBook ist die zentrale Verwaltungsklasse der Anwendung.
Sie sammelt und verwaltet alle wichtigen Daten des Projekts.

Sie verwaltet:
- Studenten
- Kurse
- Noten
- Notenstatistiken
- Suchfunktionen
- Speichern und Laden mit JSON
- Export und Import mit CSV

Merksatz:
Das GradeBook ist wie die Zentrale der Anwendung.
Hier laufen Studenten, Kurse und Noten zusammen.
"""

# ============================================================
# Imports: Benötigte Python-Module und eigene Klassen laden
# ============================================================

# json wird benutzt, um Daten als JSON-Datei zu speichern oder zu laden.
import json

# re wird benutzt, um mit regulären Ausdrücken zu suchen.
import re

# Path wird benutzt, um Dateipfade sauber zu behandeln.
from pathlib import Path

# Course ist die Klasse für einen Kurs oder ein Fach.
from notenverwaltung.course import Course

# Eigene Fehlerklassen werden importiert.
# Dadurch kann das Programm genauere Fehlermeldungen auslösen.
from notenverwaltung.exceptions import (
    CourseNotFoundError,
    DuplicateEntryError,
    PersistenceError,
    StudentNotFoundError,
)

# Grade ist die Klasse für eine einzelne Note.
from notenverwaltung.grade import Grade

# Student ist die Klasse für einen einzelnen Studenten.
from notenverwaltung.student import Student


# ============================================================
# Hauptklasse: GradeBook-Verwaltung
# ============================================================

class GradeBook:
    """Verwaltet Studenten, Kurse, Noten, Statistiken und Dateien.

    Die Klasse GradeBook ist die zentrale Klasse der Anwendung.

    Sie speichert:
    - alle Studenten
    - alle Kurse
    - alle eingetragenen Noten

    Außerdem bietet sie Methoden, um:
    - Studenten hinzuzufügen
    - Kurse hinzuzufügen
    - Noten einzutragen
    - Durchschnittswerte zu berechnen
    - Bestehensquoten zu berechnen
    - beste Studenten zu finden
    - gefährdete Studenten zu finden
    - Studenten und Kurse zu suchen
    - Daten als JSON zu speichern und zu laden
    - Noten als CSV zu exportieren und zu importieren

    Merksatz:
    GradeBook verwaltet nicht nur Daten, sondern auch die wichtigsten
    Funktionen rund um diese Daten.
    """

    # ========================================================
    # Initialisierung: Ein leeres GradeBook erstellen
    # ========================================================

    def __init__(self) -> None:
        """Erstellt ein leeres GradeBook-Objekt.

        Beim Erstellen eines neuen GradeBooks werden drei leere
        Sammlungen angelegt.

        Es gibt:
        - students: ein Dictionary für alle Studenten
        - courses: ein Dictionary für alle Kurse
        - grades: eine Liste für alle Noten

        Merksatz:
        Beim Start ist das GradeBook leer.
        Danach können Studenten, Kurse und Noten hinzugefügt werden.
        """

        # Hier werden alle Studenten gespeichert.
        # Der Schlüssel ist die student_id.
        # Der Wert ist das Student-Objekt.
        self.students: dict[str, Student] = {}

        # Hier werden alle Kurse gespeichert.
        # Der Schlüssel ist die course_id.
        # Der Wert ist das Course-Objekt.
        self.courses: dict[str, Course] = {}

        # Hier werden alle Grade-Objekte gespeichert.
        # Eine Liste ist sinnvoll, weil jede Note ein eigener Eintrag ist.
        self.grades: list[Grade] = []

    # ========================================================
    # Studentenverwaltung: Studenten hinzufügen
    # ========================================================

    def add_student(self, student: Student) -> None:
        """Fügt einen Studenten zum GradeBook hinzu.

        Der Student wird über seine student_id gespeichert.

        Wenn bereits ein Student mit derselben ID existiert,
        wird ein DuplicateEntryError ausgelöst.

        Dadurch werden doppelte Studenten verhindert.

        Args:
            student: Das Student-Objekt, das hinzugefügt werden soll.

        Raises:
            DuplicateEntryError: Wenn die student_id bereits existiert.
        """

        # Prüfen, ob die student_id bereits im Dictionary vorhanden ist.
        if student.student_id in self.students:
            # Wenn ja, wird ein eigener Fehler ausgelöst.
            raise DuplicateEntryError(
                f"Student with ID {student.student_id} already exists."
            )

        # Wenn die ID noch nicht existiert, wird der Student gespeichert.
        self.students[student.student_id] = student

    # ========================================================
    # Kursverwaltung: Kurse hinzufügen
    # ========================================================

    def add_course(self, course: Course) -> None:
        """Fügt einen Kurs zum GradeBook hinzu.

        Der Kurs wird über seine course_id gespeichert.

        Wenn bereits ein Kurs mit derselben ID existiert,
        wird ein DuplicateEntryError ausgelöst.

        Dadurch werden doppelte Kurse verhindert.

        Args:
            course: Das Course-Objekt, das hinzugefügt werden soll.

        Raises:
            DuplicateEntryError: Wenn die course_id bereits existiert.
        """

        # Prüfen, ob die course_id bereits im Dictionary vorhanden ist.
        if course.course_id in self.courses:
            # Wenn ja, wird ein eigener Fehler ausgelöst.
            raise DuplicateEntryError(
                f"Course with ID {course.course_id} already exists."
            )

        # Wenn die ID noch nicht existiert, wird der Kurs gespeichert.
        self.courses[course.course_id] = course

    # ========================================================
    # Notenverwaltung: Eine neue Note eintragen
    # ========================================================

    def record_grade(
        self,
        student_id: str,
        course_id: str,
        score: float,
        date: str,
        notes: str = "",
    ) -> Grade:
        """Erstellt und speichert eine Note für einen vorhandenen Studenten und Kurs.

        Die Methode prüft zuerst:
        - Existiert der Student?
        - Existiert der Kurs?

        Nur wenn beide existieren, wird eine neue Grade erstellt.

        Args:
            student_id: Die ID des Studenten.
            course_id: Die ID des Kurses.
            score: Die erreichte Punktzahl.
            date: Das Datum der Note.
            notes: Optionale Notizen zur Note.

        Returns:
            Das neu erstellte Grade-Objekt.

        Raises:
            StudentNotFoundError: Wenn die student_id nicht existiert.
            CourseNotFoundError: Wenn die course_id nicht existiert.

        Merksatz:
        Eine Note darf nur eingetragen werden, wenn Student und Kurs
        vorher im GradeBook vorhanden sind.
        """

        # Prüfen, ob der Student existiert.
        if student_id not in self.students:
            raise StudentNotFoundError(
                f"Student with ID {student_id} does not exist."
            )

        # Prüfen, ob der Kurs existiert.
        if course_id not in self.courses:
            raise CourseNotFoundError(
                f"Course with ID {course_id} does not exist."
            )

        # Den passenden Studenten aus dem Dictionary holen.
        student = self.students[student_id]

        # Den passenden Kurs aus dem Dictionary holen.
        course = self.courses[course_id]

        # Ein neues Grade-Objekt erstellen.
        # Diese Note verbindet den Studenten mit dem Kurs.
        grade = Grade(
            student=student,
            course=course,
            score=score,
            date=date,
            notes=notes,
        )

        # Die neue Note wird in der internen Notenliste gespeichert.
        self.grades.append(grade)

        # Die neu erstellte Note wird zurückgegeben.
        return grade

    # ========================================================
    # Notensuche: Alle Noten eines Studenten holen
    # ========================================================

    def get_student_grades(self, student_id: str) -> list[Grade]:
        """Gibt alle Noten eines bestimmten Studenten zurück.

        Die Methode durchsucht die interne Notenliste.
        Es werden nur die Noten zurückgegeben, die zur student_id passen.

        Args:
            student_id: Die ID des Studenten.

        Returns:
            Eine Liste mit Grade-Objekten des Studenten.

        Raises:
            StudentNotFoundError: Wenn die student_id nicht existiert.
        """

        # Erst prüfen, ob der Student überhaupt existiert.
        if student_id not in self.students:
            raise StudentNotFoundError(
                f"Student with ID {student_id} does not exist."
            )

        # List Comprehension:
        # Es werden alle Noten gesammelt, deren student_id passt.
        return [
            grade
            for grade in self.grades
            if grade.student.student_id == student_id
        ]

    # ========================================================
    # Notensuche: Alle Noten eines Kurses holen
    # ========================================================

    def get_course_grades(self, course_id: str) -> list[Grade]:
        """Gibt alle Noten eines bestimmten Kurses zurück.

        Die Methode durchsucht die interne Notenliste.
        Es werden nur die Noten zurückgegeben, die zur course_id passen.

        Args:
            course_id: Die ID des Kurses.

        Returns:
            Eine Liste mit Grade-Objekten des Kurses.

        Raises:
            CourseNotFoundError: Wenn die course_id nicht existiert.
        """

        # Erst prüfen, ob der Kurs überhaupt existiert.
        if course_id not in self.courses:
            raise CourseNotFoundError(
                f"Course with ID {course_id} does not exist."
            )

        # List Comprehension:
        # Es werden alle Noten gesammelt, deren course_id passt.
        return [
            grade
            for grade in self.grades
            if grade.course.course_id == course_id
        ]

    # ========================================================
    # Statistik: Durchschnitt eines Studenten berechnen
    # ========================================================

    def student_average(self, student_id: str) -> float:
        """Berechnet den Durchschnitt eines Studenten in Prozent.

        Zuerst werden alle Noten des Studenten geholt.
        Danach wird der Durchschnitt der Prozentwerte berechnet.

        Args:
            student_id: Die ID des Studenten.

        Returns:
            Der Durchschnitt des Studenten in Prozent.

        Raises:
            StudentNotFoundError: Wenn die student_id nicht existiert.
            ValueError: Wenn der Student noch keine Noten hat.

        Merksatz:
        Ohne Noten kann kein Durchschnitt berechnet werden.
        """

        # Alle Noten des Studenten holen.
        grades = self.get_student_grades(student_id)

        # Wenn die Liste leer ist, kann man keinen Durchschnitt berechnen.
        if not grades:
            raise ValueError(f"No grades recorded for student {student_id}.")

        # Alle Prozentwerte der Noten zusammenzählen.
        total_percentage = sum(grade.percentage for grade in grades)

        # Summe durch Anzahl der Noten teilen.
        return total_percentage / len(grades)

    # ========================================================
    # Statistik: Durchschnitt eines Kurses berechnen
    # ========================================================

    def course_average(self, course_id: str) -> float:
        """Berechnet den Durchschnittswert eines Kurses.

        Zuerst werden alle Noten des Kurses geholt.
        Danach wird der Durchschnitt der Punkte berechnet.

        Args:
            course_id: Die ID des Kurses.

        Returns:
            Der durchschnittliche Score des Kurses.

        Raises:
            CourseNotFoundError: Wenn die course_id nicht existiert.
            ValueError: Wenn der Kurs noch keine Noten hat.
        """

        # Alle Noten des Kurses holen.
        grades = self.get_course_grades(course_id)

        # Wenn keine Noten vorhanden sind, ist kein Durchschnitt möglich.
        if not grades:
            raise ValueError(f"No grades recorded for course {course_id}.")

        # Alle Scores zusammenzählen.
        total_score = sum(grade.score for grade in grades)

        # Summe durch Anzahl der Noten teilen.
        return total_score / len(grades)

    # ========================================================
    # Statistik: Bestehensquote eines Kurses berechnen
    # ========================================================

    def course_pass_rate(self, course_id: str) -> float:
        """Berechnet die Bestehensquote eines Kurses in Prozent.

        Die Methode zählt, wie viele Noten bestanden sind.
        Danach wird berechnet, wie viel Prozent der Noten bestanden wurden.

        Args:
            course_id: Die ID des Kurses.

        Returns:
            Die Bestehensquote des Kurses in Prozent.

        Raises:
            CourseNotFoundError: Wenn die course_id nicht existiert.
            ValueError: Wenn der Kurs noch keine Noten hat.
        """

        # Alle Noten des Kurses holen.
        grades = self.get_course_grades(course_id)

        # Ohne Noten kann keine Bestehensquote berechnet werden.
        if not grades:
            raise ValueError(f"No grades recorded for course {course_id}.")

        # Zähler für bestandene Noten.
        passing_grades = 0

        # Jede Note im Kurs durchgehen.
        for grade in grades:
            # Die Property is_passing sagt True, wenn die Note bestanden ist.
            if grade.is_passing:
                passing_grades = passing_grades + 1

        # Bestandene Noten durch alle Noten teilen und mal 100 rechnen.
        return passing_grades / len(grades) * 100

    # ========================================================
    # Ranking: Beste Studenten finden
    # ========================================================

    def top_students(self, n: int = 5) -> list[tuple[Student, float]]:
        """Gibt die besten N Studenten nach Durchschnitt zurück.

        Für jeden Studenten mit mindestens einer Note wird der Durchschnitt
        berechnet. Danach wird die Liste absteigend sortiert.

        Args:
            n: Maximale Anzahl der zurückgegebenen Studenten.

        Returns:
            Eine Liste von Tupeln.
            Jedes Tupel enthält:
            - Student-Objekt
            - Durchschnittswert

        Merksatz:
        top_students sortiert nach Leistung von hoch nach niedrig.
        """

        # Leere Liste für Studenten mit Durchschnitt.
        averages = []

        # Alle Studenten im GradeBook durchgehen.
        for student_id, student in self.students.items():
            # Noten des aktuellen Studenten holen.
            student_grades = self.get_student_grades(student_id)

            # Nur Studenten mit mindestens einer Note berücksichtigen.
            if student_grades:
                # Durchschnitt berechnen.
                average = self.student_average(student_id)

                # Student und Durchschnitt als Tupel speichern.
                averages.append((student, average))

        # Liste nach Durchschnitt sortieren.
        # reverse=True bedeutet: höchster Wert zuerst.
        averages.sort(key=lambda item: item[1], reverse=True)

        # Nur die besten n Studenten zurückgeben.
        return averages[:n]

    # ========================================================
    # Risikoanalyse: Studenten unter einem Grenzwert finden
    # ========================================================

    def students_at_risk(self, threshold: float = 60.0) -> list[Student]:
        """Gibt Studenten zurück, deren Durchschnitt unter einem Grenzwert liegt.

        Diese Methode kann verwendet werden, um Studenten zu finden,
        die Unterstützung brauchen könnten.

        Nur Studenten mit mindestens einer Note werden geprüft.

        Args:
            threshold: Grenzwert in Prozent.

        Returns:
            Eine Liste mit Studenten unterhalb des Grenzwerts.
        """

        # Leere Liste für gefährdete Studenten.
        at_risk_students = []

        # Alle Studenten durchgehen.
        for student_id, student in self.students.items():
            # Noten des Studenten holen.
            student_grades = self.get_student_grades(student_id)

            # Nur prüfen, wenn der Student überhaupt Noten hat.
            if student_grades:
                # Durchschnitt berechnen.
                average = self.student_average(student_id)

                # Prüfen, ob der Durchschnitt unter dem Grenzwert liegt.
                if average < threshold:
                    at_risk_students.append(student)

        # Liste der gefährdeten Studenten zurückgeben.
        return at_risk_students

    # ========================================================
    # Suchfunktionen: Studenten suchen
    # ========================================================

    def search_students(self, query: str) -> list[Student]:
        """Sucht Studenten nach Vorname, Nachname, E-Mail oder vollem Namen.

        Die Suche verwendet reguläre Ausdrücke.
        Die Suche ist nicht abhängig von Groß- und Kleinschreibung.

        Args:
            query: Suchtext oder regulärer Ausdruck.

        Returns:
            Eine Liste mit passenden Student-Objekten.

        Beispiel:
            Suche nach "anna" findet auch "Anna".
        """

        # Suchmuster erstellen.
        # re.IGNORECASE bedeutet: Groß- und Kleinschreibung ignorieren.
        pattern = re.compile(query, re.IGNORECASE)

        # Alle Studenten durchsuchen.
        return [
            student
            for student in self.students.values()
            if pattern.search(student.first_name)
            or pattern.search(student.last_name)
            or pattern.search(student.email)
            or pattern.search(student.full_name)
        ]

    # ========================================================
    # Suchfunktionen: Kurse suchen
    # ========================================================

    def search_courses(self, query: str) -> list[Course]:
        """Sucht Kurse nach Kursnamen.

        Die Suche verwendet reguläre Ausdrücke.
        Die Suche ist nicht abhängig von Groß- und Kleinschreibung.

        Args:
            query: Suchtext oder regulärer Ausdruck.

        Returns:
            Eine Liste mit passenden Course-Objekten.
        """

        # Suchmuster erstellen.
        pattern = re.compile(query, re.IGNORECASE)

        # Alle Kurse durchsuchen und passende Kurse zurückgeben.
        return [
            course
            for course in self.courses.values()
            if pattern.search(course.name)
        ]

    # ========================================================
    # JSON-Persistenz: GradeBook in Dictionary umwandeln
    # ========================================================

    def to_dict(self) -> dict:
        """Wandelt das komplette GradeBook in einfache Dictionary-Daten um.

        Diese Methode bereitet das GradeBook für das Speichern als JSON vor.

        Komplexe Objekte wie Student, Course und Grade werden in einfache
        Dictionaries umgewandelt.

        Returns:
            Ein Dictionary mit Studenten, Kursen und Noten.

        Merksatz:
        JSON kann keine eigenen Python-Objekte direkt speichern.
        Deshalb müssen sie zuerst in einfache Daten umgewandelt werden.
        """

        # Leere Liste für Studentendaten.
        students_data = []

        # Jeden Studenten in ein Dictionary umwandeln.
        for student in self.students.values():
            students_data.append(
                {
                    "student_id": student.student_id,
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "email": student.email,
                }
            )

        # Leere Liste für Kursdaten.
        courses_data = []

        # Jeden Kurs in ein Dictionary umwandeln.
        for course in self.courses.values():
            courses_data.append(
                {
                    "course_id": course.course_id,
                    "name": course.name,
                    "max_grade": course.max_grade,
                    "passing_grade": course.passing_grade,
                }
            )

        # Leere Liste für Notendaten.
        grades_data = []

        # Jede Note in ein Dictionary umwandeln.
        for grade in self.grades:
            grades_data.append(
                {
                    "student_id": grade.student.student_id,
                    "course_id": grade.course.course_id,
                    "score": grade.score,
                    "date": grade.date,
                    "notes": grade.notes,
                }
            )

        # Alle Daten in einem großen Dictionary zurückgeben.
        return {
            "students": students_data,
            "courses": courses_data,
            "grades": grades_data,
        }

    # ========================================================
    # JSON-Persistenz: GradeBook aus Dictionary wiederherstellen
    # ========================================================

    @classmethod
    def from_dict(cls, data: dict) -> "GradeBook":
        """Erstellt ein GradeBook aus Dictionary-Daten.

        Diese Methode wird vor allem nach dem Laden einer JSON-Datei benutzt.

        Aus einfachen Dictionary-Daten werden wieder echte Objekte erstellt:
        - Student-Objekte
        - Course-Objekte
        - Grade-Objekte

        Args:
            data: Dictionary mit Studenten, Kursen und Noten.

        Returns:
            Ein neu aufgebautes GradeBook-Objekt.

        Raises:
            KeyError: Wenn wichtige Schlüssel fehlen.
            ValueError: Wenn geladene Werte ungültig sind.
        """

        # Neues leeres GradeBook erstellen.
        gradebook = cls()

        # Alle Studentendaten durchgehen.
        for student_data in data["students"]:
            # Aus den Dictionary-Daten ein Student-Objekt erstellen.
            student = Student(
                student_id=student_data["student_id"],
                first_name=student_data["first_name"],
                last_name=student_data["last_name"],
                email=student_data["email"],
            )

            # Student zum GradeBook hinzufügen.
            gradebook.add_student(student)

        # Alle Kursdaten durchgehen.
        for course_data in data["courses"]:
            # Aus den Dictionary-Daten ein Course-Objekt erstellen.
            course = Course(
                course_id=course_data["course_id"],
                name=course_data["name"],
                max_grade=course_data["max_grade"],
                passing_grade=course_data["passing_grade"],
            )

            # Kurs zum GradeBook hinzufügen.
            gradebook.add_course(course)

        # Alle Notendaten durchgehen.
        for grade_data in data["grades"]:
            # record_grade erstellt wieder ein echtes Grade-Objekt.
            gradebook.record_grade(
                student_id=grade_data["student_id"],
                course_id=grade_data["course_id"],
                score=grade_data["score"],
                date=grade_data["date"],
                notes=grade_data.get("notes", ""),
            )

        # Das neu aufgebaute GradeBook zurückgeben.
        return gradebook

    # ========================================================
    # JSON-Persistenz: GradeBook als JSON-Datei speichern
    # ========================================================

    def save_json(self, file_path: str) -> None:
        """Speichert das komplette GradeBook als JSON-Datei.

        Die Methode wandelt das GradeBook zuerst in Dictionary-Daten um.
        Danach werden diese Daten in JSON-Text umgewandelt.
        Zum Schluss wird der JSON-Text in eine Datei geschrieben.

        Args:
            file_path: Pfad, unter dem die JSON-Datei gespeichert wird.

        Raises:
            PersistenceError: Wenn die Datei nicht geschrieben werden kann.
        """

        try:
            # Dateipfad vorbereiten.
            path = Path(file_path)

            # GradeBook in einfache Dictionary-Daten umwandeln.
            data = self.to_dict()

            # Dictionary-Daten in schön formatierten JSON-Text umwandeln.
            json_text = json.dumps(data, indent=4)

            # JSON-Text in Datei schreiben.
            path.write_text(json_text, encoding="utf-8")

        except OSError as error:
            # OSError kann z. B. entstehen, wenn der Pfad ungültig ist.
            raise PersistenceError(
                f"Could not save JSON file: {file_path}"
            ) from error

    # ========================================================
    # JSON-Persistenz: GradeBook aus JSON-Datei laden
    # ========================================================

    @classmethod
    def load_json(cls, file_path: str) -> "GradeBook":
        """Lädt ein GradeBook aus einer JSON-Datei.

        Die Methode liest zuerst JSON-Text aus einer Datei.
        Danach wird der JSON-Text in Dictionary-Daten umgewandelt.
        Aus diesen Daten wird wieder ein GradeBook erstellt.

        Args:
            file_path: Pfad der JSON-Datei.

        Returns:
            Ein geladenes GradeBook-Objekt.

        Raises:
            PersistenceError: Wenn die Datei nicht gelesen, nicht dekodiert
                oder nicht korrekt umgewandelt werden kann.
        """

        try:
            # Dateipfad vorbereiten.
            path = Path(file_path)

            # JSON-Text aus Datei lesen.
            json_text = path.read_text(encoding="utf-8")

            # JSON-Text in Python-Daten umwandeln.
            data = json.loads(json_text)

            # Aus den Python-Daten wieder ein GradeBook erstellen.
            return cls.from_dict(data)

        except OSError as error:
            # Fehler beim Lesen der Datei.
            raise PersistenceError(
                f"Could not read JSON file: {file_path}"
            ) from error

        except json.JSONDecodeError as error:
            # Fehler, wenn der JSON-Inhalt kaputt oder ungültig ist.
            raise PersistenceError(
                f"Could not decode JSON file: {file_path}"
            ) from error

        except (KeyError, TypeError, ValueError) as error:
            # Fehler, wenn die JSON-Datei nicht zur erwarteten Struktur passt.
            raise PersistenceError(
                f"JSON file contains invalid grade book data: {file_path}"
            ) from error

    # ========================================================
    # CSV-Export: Noten in CSV-Datei speichern
    # ========================================================

    def export_grades_to_csv(self, file_path: str) -> None:
        """Exportiert alle gespeicherten Noten in eine einfache CSV-Datei.

        Die CSV-Datei enthält:
        - eine Kopfzeile
        - eine Zeile pro Note

        Jede Zeile enthält:
        - student_id
        - course_id
        - score
        - date

        Args:
            file_path: Pfad, unter dem die CSV-Datei gespeichert wird.

        Raises:
            PersistenceError: Wenn die CSV-Datei nicht geschrieben werden kann.
        """

        try:
            # Dateipfad vorbereiten.
            path = Path(file_path)

            # Erste Zeile der CSV-Datei ist die Kopfzeile.
            lines = ["student_id,course_id,score,date"]

            # Jede Note in eine CSV-Zeile umwandeln.
            for grade in self.grades:
                line = (
                    f"{grade.student.student_id},"
                    f"{grade.course.course_id},"
                    f"{grade.score},"
                    f"{grade.date}"
                )

                # CSV-Zeile zur Liste hinzufügen.
                lines.append(line)

            # Alle Zeilen mit Zeilenumbrüchen verbinden.
            csv_text = "\n".join(lines)

            # CSV-Text in Datei schreiben.
            path.write_text(csv_text, encoding="utf-8")

        except OSError as error:
            # Fehler beim Schreiben der Datei.
            raise PersistenceError(
                f"Could not write CSV file: {file_path}"
            ) from error

    # ========================================================
    # CSV-Import: Noten aus CSV-Datei laden
    # ========================================================

    def import_grades_from_csv(self, file_path: str) -> dict:
        """Importiert Noten aus einer CSV-Datei und gibt einen Bericht zurück.

        Die Methode liest eine CSV-Datei Zeile für Zeile.

        Gültige Zeilen werden als Noten importiert.
        Ungültige Zeilen werden übersprungen und im Fehlerbericht gespeichert.

        Der Bericht enthält:
        - imported: Anzahl erfolgreich importierter Noten
        - skipped: Anzahl übersprungener Zeilen
        - errors: Liste mit Fehlermeldungen

        Args:
            file_path: Pfad der CSV-Datei.

        Returns:
            Ein Dictionary mit Import-Statistik und Fehlermeldungen.

        Raises:
            PersistenceError: Wenn die CSV-Datei nicht gelesen werden kann.

        Merksatz:
        CSV-Import ist vorsichtig:
        Gute Zeilen werden übernommen, schlechte Zeilen werden gemeldet.
        """

        try:
            # Dateipfad vorbereiten.
            path = Path(file_path)

            # Datei lesen und in einzelne Zeilen aufteilen.
            lines = path.read_text(encoding="utf-8").splitlines()

        except OSError as error:
            # Fehler beim Lesen der Datei.
            raise PersistenceError(
                f"Could not read CSV file: {file_path}"
            ) from error

        # Bericht vorbereiten.
        # imported zählt erfolgreiche Importe.
        # skipped zählt übersprungene Zeilen.
        # errors sammelt Fehlermeldungen.
        report = {
            "imported": 0,
            "skipped": 0,
            "errors": [],
        }

        # Regulärer Ausdruck für gültige CSV-Zeilen.
        # Erwartetes Format:
        # student_id,course_id,score,date
        pattern = re.compile(
            r"^([^,]+),([^,]+),([0-9]+(?:\.[0-9]+)?),(\d{4}-\d{2}-\d{2})$"
        )

        # Jede Zeile der Datei durchgehen.
        # start=1 bedeutet: Zeilennummern beginnen bei 1.
        for line_number, line in enumerate(lines, start=1):
            # Kopfzeile überspringen.
            if line_number == 1 and line == "student_id,course_id,score,date":
                continue

            # Prüfen, ob die Zeile zum erwarteten Muster passt.
            match = pattern.match(line)

            # Wenn die Zeile nicht passt, wird sie übersprungen.
            if not match:
                report["skipped"] = report["skipped"] + 1
                report["errors"].append(f"Line {line_number}: invalid format")
                continue

            # Werte aus der CSV-Zeile herauslesen.
            student_id = match.group(1)
            course_id = match.group(2)
            score = float(match.group(3))
            date = match.group(4)

            try:
                # Note eintragen.
                # Dabei wird automatisch geprüft, ob Student und Kurs existieren.
                self.record_grade(
                    student_id=student_id,
                    course_id=course_id,
                    score=score,
                    date=date,
                )

                # Erfolgreichen Import zählen.
                report["imported"] = report["imported"] + 1

            except ValueError as error:
                # Wenn beim Eintragen ein Fehler passiert,
                # wird die Zeile übersprungen und im Bericht gespeichert.
                report["skipped"] = report["skipped"] + 1
                report["errors"].append(f"Line {line_number}: {error}")

        # Am Ende wird der Importbericht zurückgegeben.
        return report