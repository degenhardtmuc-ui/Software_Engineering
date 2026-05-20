
# ============================================================
# 1) Funktion: print_all
# ============================================================

def print_all(items: list):
    """
    Gibt alle Elemente aus items aus.
    Pro Zeile wird genau ein Element ausgegeben.

    Wichtig:
    Eine for-Schleife geht Element für Element durch eine Sammlung.
    Bei einer Liste sind die Elemente z. B. "Tee", "Kaffee".
    Bei einem String sind die Elemente einzelne Buchstaben.
    """

    # enumerate(items) liefert zwei Dinge gleichzeitig:
    # index = Nummer/Position des Elements, beginnend bei 0
    # item  = das aktuelle Element
    for index, item in enumerate(items):
        print(f"Eintrag der Liste: {index} {item}")


# ============================================================
# 2) Einkaufsliste ausgeben
# ============================================================

def drucke_einkaufsliste(einkaufsliste: list):
    """
    Gibt die Einkaufsliste aus.
    Pro Zeile wird ein Produkt ausgegeben.
    """

    for item in einkaufsliste:
        print(f"Kaufe: {item}")


# ============================================================
# 3) Produkt kaufen / hinzufügen
# ============================================================

def kaufe(produkt: str, einkaufsliste: list):
    """
    Fügt ein Produkt zur Einkaufsliste hinzu.

    Wichtig:
    einkaufsliste + [produkt] erstellt eine NEUE Liste.
    Die alte Liste wird nicht direkt verändert.

    Deshalb muss man das Ergebnis wieder speichern:

    meine_einkaufsliste = kaufe("Butter", meine_einkaufsliste)
    """

    return einkaufsliste + [produkt]


# ============================================================
# 4) Hauptprogramm
# ============================================================

if __name__ == "__main__":

    print("========== Teil 1: print_all mit einem String ==========")

    # Aufgabe:
    # Was passiert, wenn man print_all mit einem String aufruft?
    #
    # Antwort:
    # Python behandelt den String "abc" wie eine Sammlung von Zeichen.
    # Die for-Schleife geht also Zeichen für Zeichen durch:
    # a, dann b, dann c.
    print_all("abc")

    print()
    print("========== Teil 2: Zwei Einkaufslisten erstellen ==========")

    # Beide Listen starten gleich.
    meine_einkaufsliste = ["Tee", "Kaffee"]
    eine_andere_einkaufsliste = ["Tee", "Kaffee"]

    print("Meine Einkaufsliste am Anfang:")
    drucke_einkaufsliste(meine_einkaufsliste)

    print()
    print("Eine andere Einkaufsliste am Anfang:")
    drucke_einkaufsliste(eine_andere_einkaufsliste)

    print()
    print("========== Teil 3: Butter und Brot hinzufügen ==========")

    # Wir fügen Butter und Brot nur zu MEINER Einkaufsliste hinzu.
    # Wichtig: Weil kaufe(...) eine neue Liste zurückgibt,
    # müssen wir das Ergebnis wieder in meine_einkaufsliste speichern.
    meine_einkaufsliste = kaufe("Butter", meine_einkaufsliste)
    meine_einkaufsliste = kaufe("Brot", meine_einkaufsliste)

    print("Meine Einkaufsliste nach Butter und Brot:")
    drucke_einkaufsliste(meine_einkaufsliste)

    print()
    print("Eine andere Einkaufsliste bleibt unverändert:")
    drucke_einkaufsliste(eine_andere_einkaufsliste)

    print()
    print("========== Teil 4: Nochmals Butter und Brot hinzufügen ==========")

    # Jetzt fügen wir Butter und Brot NOCHMALS hinzu.
    meine_einkaufsliste = kaufe("Butter", meine_einkaufsliste)
    meine_einkaufsliste = kaufe("Brot", meine_einkaufsliste)

    print("Meine Einkaufsliste nach dem zweiten Hinzufügen:")
    drucke_einkaufsliste(meine_einkaufsliste)

    print()
    print("Eine andere Einkaufsliste bleibt immer noch unverändert:")
    drucke_einkaufsliste(eine_andere_einkaufsliste)

    print()
    print("========== Erklärung ==========")

    print("1. print_all('abc') gibt a, b und c einzeln aus, weil ein String aus Zeichen besteht.")
    print("2. meine_einkaufsliste wurde erweitert.")
    print("3. eine_andere_einkaufsliste wurde nicht verändert.")
    print("4. Wenn man Butter und Brot nochmals hinzufügt, stehen sie doppelt in der Liste.")


    Der wichtigste Punkt aus deiner Aufgabe:
    print_all("abc")
    gibt aus:

Eintrag der Liste: 0 a
Eintrag der Liste: 1 b
Eintrag der Liste: 2 c
Und bei der Einkaufsliste passiert am Ende das:

Tee
Kaffee
Butter
Brot
Butter
Brot
