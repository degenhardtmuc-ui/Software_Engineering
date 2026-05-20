def drucke_einkaufsliste(einkaufsliste):
    for item in einkaufsliste:
        print(f"Kaufe: {item}")


def kaufe(produkt, einkaufsliste, geld):
    """
    Fügt Produkt nur hinzu, wenn genug Geld vorhanden ist.
    Butter kostet 60.
    Brot kostet 60.
    """

    if produkt == "Butter" and geld >= 60:
        geld = geld - 60
        einkaufsliste = einkaufsliste + [produkt]

    elif produkt == "Brot" and geld >= 60:
        geld = geld - 60
        einkaufsliste = einkaufsliste + [produkt]

    else:
        print(f"Nicht genug Geld für {produkt}.")

    return einkaufsliste, geld


if __name__ == "__main__":

    meine_einkaufsliste = ["Tee", "Kaffee"]
    eine_andere_einkaufsliste = ["Tee", "Kaffee"]
    geld = 130

    meine_einkaufsliste, geld = kaufe("Butter", meine_einkaufsliste, geld)
    meine_einkaufsliste, geld = kaufe("Brot", meine_einkaufsliste, geld)

    print("Meine Einkaufsliste:")
    drucke_einkaufsliste(meine_einkaufsliste)

    print("Restgeld:", geld)

    print("--------------------")

    print("Andere Einkaufsliste:")
    drucke_einkaufsliste(eine_andere_einkaufsliste)

    print("--------------------")

    meine_einkaufsliste, geld = kaufe("Butter", meine_einkaufsliste, geld)
    meine_einkaufsliste, geld = kaufe("Brot", meine_einkaufsliste, geld)

    print("Meine Einkaufsliste nach nochmal kaufen:")
    drucke_einkaufsliste(meine_einkaufsliste)

    print("Restgeld:", geld)

#Bei der Geld-Version passiert:
Du hast am Anfang 130. Butter kostet 60, Brot kostet 60. Danach bleiben 10 übrig. Beim zweiten Versuch reicht das Geld nicht mehr für Butter oder Brot.