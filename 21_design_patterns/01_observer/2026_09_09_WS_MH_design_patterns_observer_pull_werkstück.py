# Beim Pull Observer bekommt der Observer nicht das Item zugeschickt.

# Er bekommt stattdessen Zugriff auf den Producer und holt sich selbst den aktuellen Zustand.


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
    def update(self, producer) -> None:
        """Reagiert auf eine Änderung des Producers."""
        pass


class PrintingObserver(ItemObserver):
    """Liest das zuletzt produzierte Item vom Producer."""

    def update(self, producer) -> None:
        """Holt sich das aktuelle Item selbst."""

        item = producer.last_item

        if item is not None:
            print(
                f"Neues Werkstück: {item.name}, "
                f"Seriennummer: {item.serial_number}"
            )


class Producer:
    """Produziert Werkstücke und informiert Observer."""

    def __init__(self):
        """Erstellt einen Producer ohne aktuelles Item."""

        self.observers = []
        self.last_item = None

    def attach(self, observer: ItemObserver) -> None:
        """Meldet einen Observer an."""

        self.observers.append(observer)

    def detach(self, observer: ItemObserver) -> None:
        """Meldet einen Observer ab."""

        self.observers.remove(observer)

    def notify(self) -> None:
        """Informiert alle Observer über eine Änderung."""

        for observer in self.observers:
            observer.update(self)

    def produce(
        self,
        name: str,
        serial_number: int
    ) -> Item:
        """Produziert ein neues Werkstück."""

        self.last_item = Item(
            name,
            serial_number
        )

        self.notify()

        return self.last_item


# -----------------------------
# Nutzung
# -----------------------------

producer = Producer()

printer = PrintingObserver()

producer.attach(printer)

producer.produce("Zahnrad", 1001)
producer.produce("Schraube", 1002)

===============================================

# Producer ändert sich
#       ↓
#    notify()
#       ↓
# Observer erfährt:
# "Da hat sich etwas geändert"
#       ↓
# Observer holt selbst:
# producer.last_item

# Pull = Der Observer holt sich die benötigten Daten selbst.