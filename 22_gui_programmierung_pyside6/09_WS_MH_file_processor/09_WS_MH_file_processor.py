"""
PySide6 – Workshop 09
Lang laufende Aufgaben

Datei:
    workshop09_file_processor.py

Workshop-Ziel:
- simuliertes Batch-Tool mit ca. 20 Dateien
- QProgressBar, Start, Cancel, aktuelle Datei
- Version A: QTimer-Chunking
- Version B: QThreadPool + QRunnable
- Fortschritt über Signals
- kooperativer Abbruch
- Stretch-Goal: failed(str) und Fehlerliste

Wichtige Regeln:
1. Langsame Arbeit niemals direkt in einem normalen GUI-Handler als
   große Schleife ausführen – sonst blockiert die Event-Loop.
2. Timer-Version:
       ein kleiner Arbeitsschritt pro timeout
       -> danach Kontrolle zurück an die Event-Loop
3. Thread-Version:
       Worker berührt niemals Widgets.
       Ergebnisse/Fortschritt kommen ausschließlich über Signals zurück.
4. Abbruch ist kooperativ:
       Der Worker prüft regelmäßig ein Flag und beendet sich selbst.
5. QApplication.processEvents() wird bewusst NICHT verwendet.
"""

import sys
import time

from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    QTimer,
    Signal,
)

from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


# ============================================================
# 1. WORKER-SIGNALS
# ============================================================

class WorkerSignals(QObject):
    """
    Signals des Thread-Workers.

    QRunnable ist selbst kein QObject.
    Deshalb liegen die Signals auf einer separaten QObject-Klasse.

    Signals:
        progress(int):
            Anzahl fertig bearbeiteter Dateien.

        current_file(str):
            Name der aktuell bearbeiteten Datei.

        finished(bool):
            True  -> Arbeit blieb unbearbeitet (Abbruch)
            False -> alles wurde abgearbeitet.

        failed(str):
            Stretch-Goal: Meldung zu simulierten Fehlern.
    """

    progress = Signal(int)

    current_file = Signal(str)

    finished = Signal(bool)

    failed = Signal(str)


# ============================================================
# 2. THREAD-WORKER
# ============================================================

class ProcessWorker(QRunnable):
    """
    Verarbeitet die Dateiliste in einem ThreadPool-Thread.

    Der Worker greift NIEMALS direkt auf Widgets zu.

    Kommunikation zur GUI:
        ausschließlich über self.signals.
    """

    def __init__(self, files):
        """Speichert eine eigene Kopie der Eingabedaten."""

        super().__init__()

        self.files = list(
            files
        )

        self.signals = WorkerSignals()

        # Kooperatives Abbruch-Flag.
        self._cancelled = False


    # ========================================================
    # ABBRUCH ANFORDERN
    # ========================================================

    def cancel(self):
        """
        Fordert einen Abbruch an.

        Das ist eine ANFORDERUNG, kein sofortiger Thread-Abbruch.

        run() prüft dieses Flag vor jeder neuen Datei.
        """

        self._cancelled = True


    # ========================================================
    # WORKER-THREAD
    # ========================================================

    def run(self):
        """
        Läuft im Worker-Thread.

        Pro Datei:

        1. Abbruch prüfen.
        2. aktuellen Dateinamen melden.
        3. langsame Arbeit simulieren.
        4. Stretch-Goal-Fehler ggf. melden.
        5. Fortschritt melden.
        """

        completed = 0


        # ----------------------------------------------------
        # DATEIEN NACHEINANDER VERARBEITEN
        # ----------------------------------------------------

        for number, file_name in enumerate(
            self.files,
            start=1,
        ):


            # =================================================
            # KOOPERATIVER ABBRUCH
            # =================================================

            if self._cancelled:

                break


            # =================================================
            # AKTUELLE DATEI MELDEN
            # =================================================

            # WICHTIG:
            #
            # Der Worker verändert NICHT direkt ein QLabel.
            #
            # Er sendet lediglich ein Signal.
            self.signals.current_file.emit(
                file_name
            )


            # =================================================
            # LANGSAME ARBEIT SIMULIEREN
            # =================================================

            # Im Worker-Thread darf diese langsame Operation
            # stattfinden.
            #
            # Die GUI-Event-Loop wird dadurch nicht blockiert.
            time.sleep(
                0.3
            )


            # =================================================
            # STRETCH-GOAL:
            # JEDE 7. DATEI "SCHLÄGT FEHL"
            # =================================================

            if number % 7 == 0:

                self.signals.failed.emit(
                    f"{file_name}: simulated failure"
                )


            # =================================================
            # FORTSCHRITT
            # =================================================

            # Die Datei wurde abgearbeitet.
            #
            # Auch bei einem simulierten Fehler gilt sie
            # als bearbeitet.
            completed += 1


            self.signals.progress.emit(
                completed
            )


        # ====================================================
        # FINISHED-SIGNAL
        # ====================================================

        # True bedeutet:
        #
        # Es blieb Arbeit unbearbeitet.
        cancelled = (
            completed
            < len(self.files)
        )


        self.signals.finished.emit(
            cancelled
        )


# ============================================================
# 3. HAUPTFENSTER
# ============================================================

class ProcessorWindow(QMainWindow):
    """
    Simuliertes Batch-Tool.

    Beide Workshop-Versionen sind in EINER Anwendung enthalten:

        Version A - Timer
        Version B - Thread

    Über die Mode-ComboBox können beide direkt verglichen werden.
    """

    def __init__(self):
        """
        Erstellt:

        - Dateiliste,
        - Timer,
        - Worker-State,
        - ProgressBar,
        - Start/Cancel,
        - Mode-Auswahl,
        - Statusanzeige,
        - Fehlerliste.
        """

        super().__init__()


        # ====================================================
        # 4. FENSTER
        # ====================================================

        self.setWindowTitle(
            "File Processor"
        )


        self.resize(
            620,
            470,
        )


        # ====================================================
        # 5. FIKTIVE DATEIEN
        # ====================================================

        self.files = [

            f"file_{number:02d}.dat"

            for number in range(
                1,
                21,
            )

        ]


        # ====================================================
        # 6. TIMER-STATE FÜR VERSION A
        # ====================================================

        self.timer = QTimer(
            self
        )


        self.timer.timeout.connect(
            self.process_one_timer_file
        )


        self.timer_files = []

        self.timer_index = 0


        # ====================================================
        # 7. THREAD-STATE FÜR VERSION B
        # ====================================================

        # WICHTIG:
        #
        # Worker-Referenz auf self halten.
        #
        # So bleibt das Python-Objekt während der Arbeit
        # erhalten.
        self.worker = None


        # ====================================================
        # 8. CENTRAL WIDGET
        # ====================================================

        central_widget = QWidget()


        self.setCentralWidget(
            central_widget
        )


        main_layout = QVBoxLayout(
            central_widget
        )


        # ====================================================
        # 9. MODUSWAHL
        # ====================================================

        mode_row = QHBoxLayout()


        mode_row.addWidget(
            QLabel(
                "Mode:"
            )
        )


        self.mode_combo = QComboBox()


        self.mode_combo.addItems(
            [
                "Version A - Timer",
                "Version B - Thread",
            ]
        )


        mode_row.addWidget(
            self.mode_combo
        )


        main_layout.addLayout(
            mode_row
        )


        # ====================================================
        # 10. AKTUELLE DATEI
        # ====================================================

        self.current_file_label = QLabel(
            "Current file: -"
        )


        main_layout.addWidget(
            self.current_file_label
        )


        # ====================================================
        # 11. PROGRESS BAR
        # ====================================================

        self.progress = QProgressBar()


        self.progress.setRange(
            0,
            len(self.files),
        )


        self.progress.setValue(
            0
        )


        main_layout.addWidget(
            self.progress
        )


        # ====================================================
        # 12. START / CANCEL
        # ====================================================

        button_row = QHBoxLayout()


        self.start_button = QPushButton(
            "Start"
        )


        self.cancel_button = QPushButton(
            "Cancel"
        )


        self.cancel_button.setEnabled(
            False
        )


        button_row.addWidget(
            self.start_button
        )


        button_row.addWidget(
            self.cancel_button
        )


        main_layout.addLayout(
            button_row
        )


        # ====================================================
        # 13. STRETCH-GOAL: FEHLERLISTE
        # ====================================================

        main_layout.addWidget(
            QLabel(
                "Failures "
                "(Thread version / Stretch Goal):"
            )
        )


        self.error_list = QListWidget()


        main_layout.addWidget(
            self.error_list
        )


        # ====================================================
        # 14. SIGNALS UND SLOTS
        # ====================================================

        self.start_button.clicked.connect(
            self.on_start
        )


        self.cancel_button.clicked.connect(
            self.on_cancel
        )


        # ====================================================
        # 15. STARTSTATUS
        # ====================================================

        self.statusBar().showMessage(
            "Ready"
        )


    # ========================================================
    # 16. UI FÜR NEUEN LAUF VORBEREITEN
    # ========================================================

    def prepare_run(self):
        """
        Bereitet die Oberfläche für einen neuen Lauf vor.
        """

        self.progress.setRange(
            0,
            len(self.files),
        )


        self.progress.setValue(
            0
        )


        self.current_file_label.setText(
            "Current file: -"
        )


        self.error_list.clear()


        self.start_button.setEnabled(
            False
        )


        self.cancel_button.setEnabled(
            True
        )


        # Während eines Laufs darf der Modus
        # nicht geändert werden.
        self.mode_combo.setEnabled(
            False
        )


    # ========================================================
    # 17. LAUF BEENDEN
    # ========================================================

    def finish_run(self, cancelled):
        """
        Stellt die Oberfläche nach Ende/Abbruch zurück.

        Args:
            cancelled (bool):

                True:
                    Arbeit blieb unbearbeitet.

                False:
                    alles wurde abgearbeitet.
        """

        self.start_button.setEnabled(
            True
        )


        self.cancel_button.setEnabled(
            False
        )


        self.mode_combo.setEnabled(
            True
        )


        self.current_file_label.setText(
            "Current file: -"
        )


        # Laut Workshop-Hinweis:
        #
        # nach Ende Progress wieder auf 0.
        self.progress.setValue(
            0
        )


        if cancelled:

            self.statusBar().showMessage(
                "Cancelled"
            )

        else:

            self.statusBar().showMessage(
                "Done"
            )


    # ========================================================
    # 18. START
    # ========================================================

    def on_start(self):
        """
        Startet je nach ComboBox:

            Version A
            oder
            Version B
        """

        # Doppelstart verhindern.
        if self.timer.isActive():

            return


        if self.worker is not None:

            return


        selected_mode = (
            self.mode_combo.currentText()
        )


        if selected_mode.startswith(
            "Version A"
        ):

            self.start_timer_version()

        else:

            self.start_thread_version()


    # ========================================================
    # 19. VERSION A - QTIMER
    # ========================================================

    def start_timer_version(self):
        """
        Startet Timer-Chunking.

        WARUM friert nicht die gesamte Batch-Verarbeitung ein?

        Weil immer nur EINE Datei bearbeitet wird.

        Danach endet der timeout-Handler und die Kontrolle geht
        zurück an die Qt-Event-Loop.

        Die Event-Loop kann zwischen zwei Ticks Maus-, Paint-
        und Cancel-Ereignisse bearbeiten.

        WICHTIG:
        time.sleep(0.3) ist absichtlich grob für den Workshop.

        Während DIESER EINEN Datei blockiert der GUI-Thread
        kurz.

        In echter Software müssen Timer-Slices deutlich
        kürzer sein.
        """

        self.prepare_run()


        self.statusBar().showMessage(
            "Running - Timer version"
        )


        self.timer_files = list(
            self.files
        )


        self.timer_index = 0


        # 0 ms:
        #
        # nächster Tick, sobald Event-Loop wieder Zeit hat.
        self.timer.start(
            0
        )


    # ========================================================
    # 20. EINE DATEI PRO TIMER-TICK
    # ========================================================

    def process_one_timer_file(self):
        """
        Verarbeitet genau EINE Datei pro Timer-Tick.

        Danach kehrt die Methode zur Event-Loop zurück.
        """

        # Alles fertig?
        if self.timer_index >= len(
            self.timer_files
        ):

            self.timer.stop()


            self.finish_run(
                cancelled=False
            )


            return


        file_name = self.timer_files[
            self.timer_index
        ]


        self.current_file_label.setText(
            f"Current file: {file_name}"
        )


        # ====================================================
        # SIMULIERTE ARBEIT
        # ====================================================

        # Version A läuft weiterhin im GUI-Thread.
        #
        # Dieser einzelne Slice blockiert deshalb 0.3 Sekunden.
        #
        # Der Unterschied zur großen Schleife:
        #
        # Nach jeder Datei kehren wir zur Event-Loop zurück.
        time.sleep(
            0.3
        )


        # ====================================================
        # FORTSCHRITT
        # ====================================================

        self.timer_index += 1


        self.progress.setValue(
            self.timer_index
        )


        # Letzte Datei erledigt?
        if self.timer_index >= len(
            self.timer_files
        ):

            self.timer.stop()


            self.finish_run(
                cancelled=False
            )


    # ========================================================
    # 21. VERSION B - THREADPOOL
    # ========================================================

    def start_thread_version(self):
        """
        Startet einen ProcessWorker im globalen QThreadPool.
        """

        self.prepare_run()


        self.statusBar().showMessage(
            "Running - Thread version"
        )


        self.worker = ProcessWorker(
            self.files
        )


        # ====================================================
        # WORKER -> GUI NUR ÜBER SIGNALS
        # ====================================================

        self.worker.signals.progress.connect(
            self.progress.setValue
        )


        self.worker.signals.current_file.connect(
            self.on_current_file
        )


        self.worker.signals.failed.connect(
            self.on_failed
        )


        self.worker.signals.finished.connect(
            self.on_thread_finished
        )


        # Worker in den globalen ThreadPool einreihen.
        QThreadPool.globalInstance().start(
            self.worker
        )


    # ========================================================
    # 22. CURRENT-FILE-SIGNAL
    # ========================================================

    def on_current_file(self, file_name):
        """
        Dieser Slot läuft im GUI-Thread.

        Deshalb darf er das QLabel ändern.
        """

        self.current_file_label.setText(
            f"Current file: {file_name}"
        )


    # ========================================================
    # 23. STRETCH-GOAL FEHLER
    # ========================================================

    def on_failed(self, message):
        """
        Sammelt simulierte Dateifehler.
        """

        self.error_list.addItem(
            message
        )


    # ========================================================
    # 24. THREAD FERTIG
    # ========================================================

    def on_thread_finished(self, cancelled):
        """
        Wird über finished(bool) aufgerufen.

        cancelled == True:
            Arbeit blieb unbearbeitet.

        cancelled == False:
            alle Dateien wurden abgearbeitet.
        """

        self.finish_run(
            cancelled=cancelled
        )


        # Worker-Referenz erst nach Ende freigeben.
        self.worker = None


    # ========================================================
    # 25. CANCEL
    # ========================================================

    def on_cancel(self):
        """
        Bricht die aktive Version ab.

        Timer:
            stoppt zwischen zwei Slices.

        Thread:
            setzt ein kooperatives Abbruch-Flag.

            Die aktuell laufende Datei wird zuerst
            fertiggestellt.
        """


        # ====================================================
        # TIMER-VERSION
        # ====================================================

        if self.timer.isActive():

            self.timer.stop()


            cancelled = (
                self.timer_index
                < len(self.timer_files)
            )


            self.finish_run(
                cancelled=cancelled
            )


            return


        # ====================================================
        # THREAD-VERSION
        # ====================================================

        if self.worker is not None:

            self.worker.cancel()


            # Zweites Cancel nicht notwendig.
            self.cancel_button.setEnabled(
                False
            )


            self.statusBar().showMessage(
                "Cancellation requested..."
            )


    # ========================================================
    # 26. FENSTER SCHLIESSEN
    # ========================================================

    def closeEvent(self, event):
        """
        Räumt laufende Arbeit beim Schließen bestmöglich auf.

        Timer:
            sofort stoppen.

        Thread:
            kooperativen Abbruch anfordern.
        """

        if self.timer.isActive():

            self.timer.stop()


        if self.worker is not None:

            self.worker.cancel()


        event.accept()


# ============================================================
# 27. PROGRAMMSTART
# ============================================================

def main():
    """
    Startet die PySide6-Anwendung.
    """

    app = QApplication(
        sys.argv
    )


    window = ProcessorWindow()


    window.show()


    return app.exec()


if __name__ == "__main__":

    sys.exit(
        main()
    )