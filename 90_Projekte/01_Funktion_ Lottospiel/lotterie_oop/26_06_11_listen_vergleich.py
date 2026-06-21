import memory_graph as mg


liste_1 = [1, 2, 3]
liste_2 = liste_1

liste_2.append(4)

daten = {
    "liste_1": liste_1,
    "liste_2": liste_2
}


mg.render(daten, "listen_verbindung.pdf")