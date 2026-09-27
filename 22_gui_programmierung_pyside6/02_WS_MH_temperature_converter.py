"""
PySide6 – Workshop 02
Signals und Slots: Celsius-Fahrenheit-Temperaturkonverter

Dieses Programm erstellt einen interaktiven Temperatur-Konverter
mit PySide6.

Die Anwendung enthält:
- ein Hauptfenster als eigene ConverterWindow-Klasse,
- einen horizontalen QSlider für Celsius,
- eine QSpinBox für Celsius,
- ein QLabel für die Fahrenheit-Ausgabe,
- eine bidirektionale Synchronisierung zwischen Slider und Spin Box,
- eine Live-Berechnung von Celsius nach Fahrenheit,
- Hinweise bei Temperaturen unter 0 °C bzw. über 100 °C,
- optional einen Reset-Button als Stretch-Goal.

Wichtige Lernziele:
- Signals und Slots verstehen
- connect() verwenden
- valueChanged als Signal verwenden
- Methoden anderer Widgets direkt als Slots verwenden
- eigene Methoden als Slots verwenden
- ein Fenster als eigene Klasse organisieren
- Vererbung von QWidget verstehen
- mit self auf Widgets und Methoden zugreifen
"""


# ============================================================
# 1. IMPORTE
# ============================================================

# Das Python-Modul "sys" benötigen wir wieder für:
#
# - sys.argv
# - sys.exit()
#
# sys.argv wird an QApplication übergeben.
# sys.exit() beendet das Programm später sauber.
import sys


# Qt benötigen wir unter anderem für:
#
# Qt.Horizontal
#
# Damit sagen wir dem QSlider, dass er horizontal
# dargestellt werden soll.
from PySide6.QtCore import Qt


# Hier importieren wir alle Widgets, die wir
# für unseren Temperatur-Konverter benötigen.
from PySide6.QtWidgets import (
    QApplication,   # Verwaltet die gesamte GUI-Anwendung
    QWidget,        # Basisklasse unseres Hauptfensters
    QLabel,         # Zeigt Text an
    QSlider,        # Schieberegler
    QSpinBox,       # Zahlen-Eingabefeld mit Pfeilen
    QPushButton,    # Anklickbarer Button
)


# ============================================================
# 2. EIGENE FENSTERKLASSE
# ============================================================

class ConverterWindow(QWidget):
    """
    Hauptfenster für den Celsius-Fahrenheit-Konverter.

    ConverterWindow erbt von QWidget.

    Dadurch ist ConverterWindow selbst ein QWidget und besitzt
    alle wichtigen Eigenschaften und Methoden eines QWidget.

    Beispiele:
    - setWindowTitle()
    - resize()
    - show()

    Gleichzeitig können wir unser Fenster um eigene Widgets,
    Methoden und Logik erweitern.
    """


    # ========================================================
    # 3. KONSTRUKTOR
    # ========================================================

    def __init__(self):
        """
        Initialisiert das Hauptfenster.

        Hier werden:
        - das QWidget initialisiert,
        - Fenstertitel und Größe gesetzt,
        - Slider erstellt,
        - Spin Box erstellt,
        - Labels erstellt,
        - Reset-Button erstellt,
        - Signals und Slots miteinander verbunden.

        __init__ wird automatisch ausgeführt, sobald wir später
        ein ConverterWindow-Objekt erzeugen.
        """

        # ----------------------------------------------------
        # QWidget-Konstruktor aufrufen
        # ----------------------------------------------------

        # ConverterWindow erbt von QWidget.
        #
        # Deshalb muss auch der Konstruktor von QWidget
        # ausgeführt werden.
        #
        # super() verweist hier auf die Elternklasse QWidget.
        super().__init__()


        # ====================================================
        # 4. HAUPTFENSTER KONFIGURIEREN
        # ====================================================

        # Text in der Titelleiste des Fensters.
        self.setWindowTitle("Temperatur-Konverter")


        # Startgröße:
        #
        # Breite = 430 Pixel
        # Höhe   = 230 Pixel
        self.resize(430, 230)


        # ====================================================
        # 5. CELSIUS-LABEL
        # ====================================================

        # Dieses QLabel zeigt lediglich die Beschriftung
        # "Celsius:" an.
        #
        # self bedeutet:
        # Das aktuelle ConverterWindow ist der Parent.
        self.celsius_label = QLabel(
            "Celsius:",
            self
        )


        # Position und Größe:
        #
        # x      = 20
        # y      = 30
        # Breite = 70
        # Höhe   = 25
        self.celsius_label.setGeometry(
            20,
            30,
            70,
            25
        )


        # ====================================================
        # 6. QSLIDER ERSTELLEN
        # ====================================================

        # QSlider erzeugt einen Schieberegler.
        #
        # Qt.Horizontal bedeutet:
        # Der Slider läuft von links nach rechts.
        #
        # self bedeutet wieder:
        # Das Hauptfenster ist der Parent.
        self.slider = QSlider(
            Qt.Horizontal,
            self
        )


        # Position des Sliders.
        self.slider.setGeometry(
            90,
            30,
            210,
            25
        )


        # Der Benutzer darf Werte zwischen
        #
        # -50 °C
        #
        # und
        #
        # +150 °C
        #
        # auswählen.
        self.slider.setRange(
            -50,
            150
        )


        # Startwert:
        #
        # 20 °C
        self.slider.setValue(20)


        # ====================================================
        # 7. QSPINBOX ERSTELLEN
        # ====================================================

        # QSpinBox ist ein Zahlenfeld.
        #
        # Der Benutzer kann:
        #
        # - eine Zahl eingeben
        # - den Pfeil nach oben benutzen
        # - den Pfeil nach unten benutzen
        self.spin_box = QSpinBox(self)


        # Position der Spin Box.
        self.spin_box.setGeometry(
            320,
            30,
            80,
            25
        )


        # Wichtig:
        #
        # Slider und Spin Box bekommen denselben Wertebereich.
        self.spin_box.setRange(
            -50,
            150
        )


        # Auch die Spin Box beginnt bei 20 °C.
        self.spin_box.setValue(20)


        # ====================================================
        # 8. FAHRENHEIT-AUSGABE
        # ====================================================

        # Dieses QLabel wird später unser Ergebnis anzeigen.
        #
        # Zum Beispiel:
        #
        # 20 °C = 68.0 °F
        self.fahrenheit_label = QLabel(
            "",
            self
        )


        self.fahrenheit_label.setGeometry(
            20,
            85,
            380,
            30
        )


        # ====================================================
        # 9. OPTIONALER RESET-BUTTON
        # ====================================================

        # Das ist das Stretch-Goal des Workshops.
        #
        # Der Button setzt später alles wieder auf
        #
        # 20 °C
        #
        # zurück.
        self.reset_button = QPushButton(
            "Reset",
            self
        )


        self.reset_button.setGeometry(
            155,
            145,
            120,
            32
        )


        # ====================================================
        # 10. SIGNAL:
        # SLIDER -> SPIN BOX
        # ====================================================

        # JETZT KOMMT DAS WICHTIGSTE THEMA DES WORKSHOPS:
        #
        # SIGNALS UND SLOTS
        #
        # valueChanged ist ein SIGNAL.
        #
        # Es wird ausgelöst, wenn sich der Wert
        # des Sliders verändert.
        #
        # setValue ist hier der SLOT.
        #
        # connect() verbindet beide miteinander.
        self.slider.valueChanged.connect(
            self.spin_box.setValue
        )


        # ====================================================
        # 11. SIGNAL:
        # SPIN BOX -> SLIDER
        # ====================================================

        # Jetzt bauen wir die Gegenrichtung.
        #
        # Wenn sich die Spin Box verändert,
        # soll sich der Slider ebenfalls verändern.
        self.spin_box.valueChanged.connect(
            self.slider.setValue
        )


        # ====================================================
        # 12. SIGNAL:
        # SLIDER -> FAHRENHEIT-BERECHNUNG
        # ====================================================

        # Ein Signal kann mit mehreren Slots verbunden sein.
        #
        # valueChanged aktualisiert bereits die Spin Box.
        #
        # Gleichzeitig verbinden wir dasselbe Signal
        # mit unserer eigenen Methode:
        #
        # update_fahrenheit
        self.slider.valueChanged.connect(
            self.update_fahrenheit
        )


        # ====================================================
        # 13. SIGNAL:
        # RESET-BUTTON -> RESET-METHODE
        # ====================================================

        # clicked ist das Signal des Buttons.
        #
        # Wenn der Benutzer auf den Button klickt,
        # wird unsere Methode reset_temperature aufgerufen.
        self.reset_button.clicked.connect(
            self.reset_temperature
        )


        # ====================================================
        # 14. STARTANZEIGE BERECHNEN
        # ====================================================

        # Wir haben weiter oben bereits:
        #
        # self.slider.setValue(20)
        #
        # ausgeführt.
        #
        # Zu diesem Zeitpunkt war valueChanged aber noch
        # NICHT mit update_fahrenheit verbunden.
        #
        # Deshalb berechnen wir die Startanzeige einmal
        # manuell.
        self.update_fahrenheit(
            self.slider.value()
        )


    # ========================================================
    # 15. FAHRENHEIT BERECHNEN
    # ========================================================

    def update_fahrenheit(self, celsius):
        """
        Berechnet Fahrenheit aus einem Celsius-Wert.

        Args:
            celsius (int):
                Der aktuelle Celsius-Wert.

                Dieser Wert wird automatisch vom
                valueChanged-Signal des Sliders an
                diese Methode übergeben.

        Formel:
            Fahrenheit = Celsius * 9 / 5 + 32

        Zusätzlich zeigt das Programm:

        - über 100 °C:
          "water boils!"

        - unter 0 °C:
          "water freezes!"
        """


        # ----------------------------------------------------
        # Celsius in Fahrenheit umrechnen
        # ----------------------------------------------------

        # Formel:
        #
        # F = C × 9 / 5 + 32
        fahrenheit = celsius * 9 / 5 + 32


        # ----------------------------------------------------
        # Ausgabetext erstellen
        # ----------------------------------------------------

        # :.1f bedeutet:
        #
        # Zeige die Zahl mit genau einer Nachkommastelle an.
        #
        # Beispiel:
        #
        # 68.0
        #
        # statt:
        #
        # 68.000000
        message = (
            f"{celsius} °C = "
            f"{fahrenheit:.1f} °F"
        )


        # ----------------------------------------------------
        # Prüfen: Wasser kocht?
        # ----------------------------------------------------

        # Laut Aufgabenstellung gilt:
        #
        # ÜBER 100 °C
        #
        # also:
        #
        # > 100
        #
        # und NICHT:
        #
        # >= 100
        if celsius > 100:

            message += " — water boils!"


        # ----------------------------------------------------
        # Prüfen: Wasser gefriert?
        # ----------------------------------------------------

        # Laut Aufgabenstellung:
        #
        # UNTER 0 °C
        #
        # also:
        #
        # < 0
        #
        # und NICHT:
        #
        # <= 0
        elif celsius < 0:

            message += " — water freezes!"


        # ----------------------------------------------------
        # QLabel aktualisieren
        # ----------------------------------------------------

        # Der fertige Text wird jetzt in unserem
        # Fahrenheit-Label angezeigt.
        self.fahrenheit_label.setText(message)


    # ========================================================
    # 16. RESET-METHODE
    # ========================================================

    def reset_temperature(self):
        """
        Setzt die Temperatur wieder auf 20 °C.

        Interessant:
        Wir müssen NICHT separat

        - die Spin Box,
        - die Fahrenheit-Anzeige

        zurücksetzen.

        Wir setzen lediglich den Slider.

        Seine bestehenden Signals sorgen automatisch dafür,
        dass alle anderen Widgets aktualisiert werden.
        """

        self.slider.setValue(20)


# ============================================================
# 17. QAPPLICATION ERSTELLEN
# ============================================================

# Wie bereits in Workshop 1 benötigt jede normale
# PySide6-Anwendung eine QApplication.
app = QApplication(sys.argv)


# ============================================================
# 18. UNSER EIGENES FENSTER ERZEUGEN
# ============================================================

# Jetzt erzeugen wir ein Objekt unserer eigenen Klasse.
#
# Dadurch wird automatisch:
#
# ConverterWindow.__init__()
#
# ausgeführt.
window = ConverterWindow()


# ============================================================
# 19. FENSTER SICHTBAR MACHEN
# ============================================================

window.show()


# ============================================================
# 20. EVENT-LOOP STARTEN
# ============================================================

# app.exec() startet wieder die Event-Loop.
#
# Jetzt wartet Qt beispielsweise auf:
#
# - Slider-Bewegungen
# - Änderungen der Spin Box
# - Button-Klicks
# - Tastatureingaben
# - Fensterereignisse
#
# Diese Events können anschließend Signals auslösen.
sys.exit(app.exec())