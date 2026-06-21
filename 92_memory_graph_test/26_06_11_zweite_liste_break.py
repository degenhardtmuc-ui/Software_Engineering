import memory_graph as mg


zahlen = [1, 2, 3]
mg.show(mg.locals_jupyter())

zweite_liste = zahlen
mg.show(mg.locals_jupyter())

zweite_liste.append(4)
mg.show(mg.locals_jupyter())