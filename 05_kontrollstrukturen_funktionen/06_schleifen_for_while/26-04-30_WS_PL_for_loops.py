# Erster Teil: Ausgabe for-loop des Strings 'abc'
def print_all(eine_liste):
    """
    Gibt Einträge der Liste aus. Pro Zeile ein Eintrag.
    """
    for index, item in enumerate(eine_liste):
        print(f"Eintrag der Liste: {index} {item}")


# Einkaufsliste

def drucke_einkaufsliste(einkaufsliste):
    """
    Gibt Einträge der Einkaufsliste aus. Pro Zeile ein Eintrag.
    """
    for item in einkaufsliste:
        print(f"Kaufe: {item}")


def kaufe(produkt, einkaufsliste):
    """
    Fügt der Einkaufsliste das Produkt hinzu und gibt die neue Liste zurück.
    """
    neue_einkaufsliste = einkaufsliste + [produkt]
    return neue_einkaufsliste


if __name__ == "__main__":

    print_all("abc")

    print("--------------------")

    meine_einkaufsliste = ["Tee", "Kaffee"]
    eine_andere_einkaufsliste = ["Tee", "Kaffee"]

    print("Meine Einkaufsliste am Anfang:")
    drucke_einkaufsliste(meine_einkaufsliste)

    print("--------------------")

    meine_einkaufsliste = kaufe("Butter", meine_einkaufsliste)
    meine_einkaufsliste = kaufe("Brot", meine_einkaufsliste)

    print("Meine Einkaufsliste nach Butter und Brot:")
    drucke_einkaufsliste(meine_einkaufsliste)

    print("--------------------")

    print("Andere Einkaufsliste:")
    drucke_einkaufsliste(eine_andere_einkaufsliste)

    print("--------------------")

    meine_einkaufsliste = kaufe("Butter", meine_einkaufsliste)
    meine_einkaufsliste = kaufe("Brot", meine_einkaufsliste)

    print("Meine Einkaufsliste nach nochmal Butter und Brot:")
    drucke_einkaufsliste(meine_einkaufsliste)