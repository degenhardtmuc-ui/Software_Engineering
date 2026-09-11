# Beim Push Observer schickt der Producer das neue Item direkt an den Observer

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Item:
    """Repräsentiert ein produziertes Werkstück."""

    name: str
    serial_number: int


class ItemObserver(ABC):
    """Schnittstelle für alle Observer."""

    @abstractmethod
    def update(self, item: Item) -> None:
        """Reagiert auf ein neu produziertes Werkstück."""
        pass


class PrintingObserver(ItemObserver):
    """Gibt ein neu produziertes Werkstück aus."""

    def update(self, item: Item) -> None:
        """Zeigt Name und Seriennummer des Werkstücks."""

        print(
            f"Neues Werkstück: {item.name}, "
            f"Seriennummer: {item.serial_number}"
        )


class Producer:
    """Produziert Werkstücke und informiert seine Observer."""

    def __init__(self):
        """Erstellt einen Producer ohne Observer."""

        self.observers = []

    def attach(self, observer: ItemObserver) -> None:
        """Meldet einen Observer an."""

        self.observers.append(observer)

    def detach(self, observer: ItemObserver) -> None:
        """Meldet einen Observer ab."""

        self.observers.remove(observer)

    def notify(self, item: Item) -> None:
        """Sendet das neue Item an alle Observer."""

        for observer in self.observers:
            observer.update(item)

    def produce(
        self,
        name: str,
        serial_number: int
    ) -> Item:
        """Produziert ein Item und informiert die Observer."""

        item = Item(name, serial_number)

        self.notify(item)

        return item


# -----------------------------
# Nutzung
# -----------------------------

producer = Producer()

printer = PrintingObserver()

producer.attach(printer)

producer.produce("Zahnrad", 1001)
producer.produce("Schraube", 1002)
producer.produce("Motor", 1003)

=====================================

# Producer produziert Item
#          ↓
#      notify(item)
#          ↓
#     update(item)
#          ↓
#  PrintingObserver

# Push = Das Subject schickt die Daten direkt mit

# Das T aus dem UML-Diagramm ist hier also: Item
# Aus: update(T) wird: update(item)


