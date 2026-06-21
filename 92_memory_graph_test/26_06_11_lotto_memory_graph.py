import random
import memory_graph as mg


# ------------------------------------------------------------
# Einstellungen für unser Lottospiel
# ------------------------------------------------------------

LOTTO_MIN = 1
LOTTO_MAX = 49
ANZAHL_ZAHLEN = 6

# Damit die Zufallszahlen bei jedem Start gleich sind.
# Das ist gut für eine Schritt-für-Schritt-Doku.
random.seed(7)

# Wenn du zusätzlich viele PDF-Dateien speichern willst:
PDFS_ERSTELLEN = False

schritt_nummer = 1


def zeige_schritt(titel, zustand):
    """
    Diese Funktion zeigt den aktuellen Speicherzustand an.

    titel:
        Kurzer Text, damit wir wissen, an welcher Stelle wir sind.

    zustand:
        Ein Dictionary mit den Variablen, die Memory Graph anzeigen soll.
    """

    global schritt_nummer

    print("\n" + "=" * 60)
    print(f"Schritt {schritt_nummer}: {titel}")
    print("=" * 60)

    # Zeigt den Memory Graph am Bildschirm.
    mg.show(zustand)

    # Optional: zusätzlich als PDF speichern.
    if PDFS_ERSTELLEN:
        dateiname = f"lotto_schritt_{schritt_nummer:02d}.pdf"
        mg.render(zustand, dateiname)
        print(f"PDF gespeichert als: {dateiname}")

    schritt_nummer += 1


# ------------------------------------------------------------
# Schritt 1: Startzustand
# ------------------------------------------------------------

spieler_zahlen = []
computer_zahlen = []
treffer = []

zeige_schritt(
    "Start: Alle Listen sind noch leer",
    {
        "spieler_zahlen": spieler_zahlen,
        "computer_zahlen": computer_zahlen,
        "treffer": treffer,
    },
)


# ------------------------------------------------------------
# Schritt 2: Spielerzahlen werden vorbereitet
# ------------------------------------------------------------

vorgegebene_spieler_zahlen = [3, 8, 12, 21, 34, 49]

zeige_schritt(
    "Die vorgegebenen Spielerzahlen liegen bereit",
    {
        "vorgegebene_spieler_zahlen": vorgegebene_spieler_zahlen,
        "spieler_zahlen": spieler_zahlen,
        "computer_zahlen": computer_zahlen,
        "treffer": treffer,
    },
)


# ------------------------------------------------------------
# Schritt 3: Spielerzahlen werden einzeln übernommen
# ------------------------------------------------------------

for zahl in vorgegebene_spieler_zahlen:
    aktuelle_zahl = zahl

    zeige_schritt(
        f"Wir schauen uns die Spielerzahl {aktuelle_zahl} an",
        {
            "vorgegebene_spieler_zahlen": vorgegebene_spieler_zahlen,
            "aktuelle_zahl": aktuelle_zahl,
            "spieler_zahlen": spieler_zahlen,
            "computer_zahlen": computer_zahlen,
            "treffer": treffer,
        },
    )

    if LOTTO_MIN <= aktuelle_zahl <= LOTTO_MAX and aktuelle_zahl not in spieler_zahlen:
        spieler_zahlen.append(aktuelle_zahl)

        zeige_schritt(
            f"Die Zahl {aktuelle_zahl} wurde zu spieler_zahlen hinzugefügt",
            {
                "vorgegebene_spieler_zahlen": vorgegebene_spieler_zahlen,
                "aktuelle_zahl": aktuelle_zahl,
                "spieler_zahlen": spieler_zahlen,
                "computer_zahlen": computer_zahlen,
                "treffer": treffer,
            },
        )


# ------------------------------------------------------------
# Schritt 4: Computerzahlen werden erzeugt
# ------------------------------------------------------------

zeige_schritt(
    "Jetzt erzeugt der Computer seine Lottozahlen",
    {
        "spieler_zahlen": spieler_zahlen,
        "computer_zahlen": computer_zahlen,
        "treffer": treffer,
    },
)


while len(computer_zahlen) < ANZAHL_ZAHLEN:
    zufallszahl = random.randint(LOTTO_MIN, LOTTO_MAX)

    zeige_schritt(
        f"Der Computer hat die Zufallszahl {zufallszahl} erzeugt",
        {
            "zufallszahl": zufallszahl,
            "spieler_zahlen": spieler_zahlen,
            "computer_zahlen": computer_zahlen,
            "treffer": treffer,
        },
    )

    if zufallszahl not in computer_zahlen:
        computer_zahlen.append(zufallszahl)

        zeige_schritt(
            f"Die Zufallszahl {zufallszahl} wurde zu computer_zahlen hinzugefügt",
            {
                "zufallszahl": zufallszahl,
                "spieler_zahlen": spieler_zahlen,
                "computer_zahlen": computer_zahlen,
                "treffer": treffer,
            },
        )

    else:
        zeige_schritt(
            f"Die Zufallszahl {zufallszahl} war schon vorhanden und wird ignoriert",
            {
                "zufallszahl": zufallszahl,
                "spieler_zahlen": spieler_zahlen,
                "computer_zahlen": computer_zahlen,
                "treffer": treffer,
            },
        )


# ------------------------------------------------------------
# Schritt 5: Zahlen sortieren
# ------------------------------------------------------------

spieler_zahlen.sort()
computer_zahlen.sort()

zeige_schritt(
    "Spielerzahlen und Computerzahlen wurden sortiert",
    {
        "spieler_zahlen": spieler_zahlen,
        "computer_zahlen": computer_zahlen,
        "treffer": treffer,
    },
)


# ------------------------------------------------------------
# Schritt 6: Treffer suchen
# ------------------------------------------------------------

for zahl in spieler_zahlen:
    aktuelle_zahl = zahl

    zeige_schritt(
        f"Wir prüfen, ob {aktuelle_zahl} in den Computerzahlen vorkommt",
        {
            "aktuelle_zahl": aktuelle_zahl,
            "spieler_zahlen": spieler_zahlen,
            "computer_zahlen": computer_zahlen,
            "treffer": treffer,
        },
    )

    if aktuelle_zahl in computer_zahlen:
        treffer.append(aktuelle_zahl)

        zeige_schritt(
            f"Treffer gefunden: {aktuelle_zahl}",
            {
                "aktuelle_zahl": aktuelle_zahl,
                "spieler_zahlen": spieler_zahlen,
                "computer_zahlen": computer_zahlen,
                "treffer": treffer,
            },
        )

    else:
        zeige_schritt(
            f"Kein Treffer bei der Zahl {aktuelle_zahl}",
            {
                "aktuelle_zahl": aktuelle_zahl,
                "spieler_zahlen": spieler_zahlen,
                "computer_zahlen": computer_zahlen,
                "treffer": treffer,
            },
        )


# ------------------------------------------------------------
# Schritt 7: Ergebnis auswerten
# ------------------------------------------------------------

anzahl_treffer = len(treffer)

zeige_schritt(
    "Die Anzahl der Treffer wurde berechnet",
    {
        "spieler_zahlen": spieler_zahlen,
        "computer_zahlen": computer_zahlen,
        "treffer": treffer,
        "anzahl_treffer": anzahl_treffer,
    },
)


if anzahl_treffer == 6:
    ergebnis_text = "Jackpot! 6 Richtige!"
elif anzahl_treffer >= 3:
    ergebnis_text = "Kleiner Gewinn!"
else:
    ergebnis_text = "Leider kein Gewinn."


zeige_schritt(
    "Das Endergebnis wurde festgelegt",
    {
        "spieler_zahlen": spieler_zahlen,
        "computer_zahlen": computer_zahlen,
        "treffer": treffer,
        "anzahl_treffer": anzahl_treffer,
        "ergebnis_text": ergebnis_text,
    },
)


# ------------------------------------------------------------
# Schritt 8: Ausgabe
# ------------------------------------------------------------

print("\nERGEBNIS")
print("Spielerzahlen:", spieler_zahlen)
print("Computerzahlen:", computer_zahlen)
print("Treffer:", treffer)
print("Anzahl Treffer:", anzahl_treffer)
print(ergebnis_text)