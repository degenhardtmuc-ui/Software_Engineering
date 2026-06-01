from dataclasses import dataclass, field
from typing import List


@dataclass
class ShoppingListItem:
    product: str
    price: float
    amount: int = 1

    def total_price(self):
        return self.price * self.amount


@dataclass
class ShoppingList:
    items: List[ShoppingListItem] = field(default_factory=list)

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        gesamtpreis = 0.0
        for item in self.items:
            gesamtpreis = gesamtpreis + item.total_price()
        return gesamtpreis

    def __str__(self):
        text = "Einkaufsliste\n"
        for item in self.items:
            zeile = f"    {item.amount} x {item.product} à {item.price:.2f}"
            zeile = zeile + f" = {item.total_price():.2f}\n"
            text = text + zeile
        text = text + f"Gesamt: {self.total_price():.2f}"
        return text

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        if isinstance(index, str):
            gefundene_items = []
            for item in self.items:
                if item.product == index:
                    gefundene_items.append(item)
            return gefundene_items

        return self.items[index]


mein_kaffee = ShoppingListItem("Kaffee", 6.99, 2)

print("Gesamtpreis Kaffee:", mein_kaffee.total_price())

meine_einkaufsliste = ShoppingList()
meine_einkaufsliste.add_item(ShoppingListItem("Tee", 1.99, 2))
meine_einkaufsliste.add_item(ShoppingListItem("Kaffee", 6.99))

print("Gesamtpreis Einkaufsliste:", meine_einkaufsliste.total_price())
print()
print(meine_einkaufsliste)
print()
print("repr-Ausgabe:")
print(repr(meine_einkaufsliste))
print()
print("Laenge der Einkaufsliste:", len(meine_einkaufsliste))
print("Erstes Element:", meine_einkaufsliste[0])
print("Zweites Element:", meine_einkaufsliste[1])
print()
print("Ausgabe mit for-Schleife:")
for item in meine_einkaufsliste:
    print(item)
print()
print("Suche nach Tee:", meine_einkaufsliste["Tee"])
print("Suche nach Kaffee:", meine_einkaufsliste["Kaffee"])
print("Suche nach Milch:", meine_einkaufsliste["Milch"])

assert mein_kaffee.product == "Kaffee"
assert mein_kaffee.price == 6.99
assert mein_kaffee.amount == 2
assert round(mein_kaffee.total_price(), 2) == 13.98

assert len(meine_einkaufsliste) == 2
assert meine_einkaufsliste[0].product == "Tee"
assert meine_einkaufsliste[1].product == "Kaffee"
assert round(meine_einkaufsliste.total_price(), 2) == 10.97
assert meine_einkaufsliste["Tee"][0].amount == 2
assert meine_einkaufsliste["Milch"] == []

print()
print("Alle Tests wurden erfolgreich ausgefuehrt.")