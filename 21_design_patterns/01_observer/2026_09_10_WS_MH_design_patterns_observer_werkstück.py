# Item mit name und serial_number
# ItemObserver mit update(item)
# Producer als Publisher
# PrintingObserver
# CountingObserver

# Der Producer ist das Subject bzw. der Publisher. 
# PrintingObserver und CountingObserver registrieren sich über attach(). 
# Sobald ein neues Item produziert wird, pusht der Producer das Item über notify() an alle Observer. 
# Jeder Observer reagiert anschließend mit seiner eigenen update()-Methode.

# Der Producer muss nicht wissen, was die Observer mit dem Item machen. 
# Dadurch sind die Komponenten lose gekoppelt (Low Coupling)





from dataclasses import dataclass, field
from abc import ABC, abstractmethod


# ---------------------------------------------------------
# Werkstück
# ---------------------------------------------------------

@dataclass
class Item:
    """Repräsentiert ein produziertes Werkstück."""

    name: str
    serial_number: int


# ---------------------------------------------------------
# Observer Interface
# ---------------------------------------------------------

class ItemObserver(ABC):
    """Schnittstelle für alle Beobachter der Produktion."""

    @abstractmethod
    def update(self, item: Item) -> None:
        """Reagiert auf ein neu produziertes Werkstück."""
        pass


# ---------------------------------------------------------
# Observer 1: Ausgabe
# ---------------------------------------------------------

class PrintingObserver(ItemObserver):
    """Gibt jedes neu produzierte Werkstück aus."""

    def update(self, item: Item) -> None:
        """Zeigt Name und Seriennummer des Werkstücks."""

        print(
            f"Produziert: {item.name}, "
            f"Seriennummer: {item.serial_number}"
        )


# ---------------------------------------------------------
# Observer 2: Zähler
# ---------------------------------------------------------

class CountingObserver(ItemObserver):
    """Zählt, wie viele Werkstücke produziert wurden."""

    def __init__(self):
        """Startet den Produktionszähler bei null."""

        self.count = 0

    def update(self, item: Item) -> None:
        """Erhöht den Zähler bei jedem neuen Werkstück."""

        self.count += 1

        print(
            f"Anzahl produzierter Werkstücke: {self.count}"
        )


# ---------------------------------------------------------
# Subject / Publisher
# ---------------------------------------------------------

@dataclass
class Producer:
    """Produziert Werkstücke und informiert seine Observer."""

    observers: list[ItemObserver] = field(default_factory=list)

    def attach(self, observer: ItemObserver) -> None:
        """Meldet einen Observer beim Producer an."""

        self.observers.append(observer)

    def detach(self, observer: ItemObserver) -> None:
        """Meldet einen Observer wieder ab."""

        self.observers.remove(observer)

    def notify(self, item: Item) -> None:
        """Informiert alle Observer über das neue Werkstück."""

        for observer in self.observers:
            observer.update(item)

    def produce(
        self,
        name: str,
        serial_number: int
    ) -> Item:
        """Produziert ein Werkstück und informiert die Observer."""

        item = Item(
            name=name,
            serial_number=serial_number
        )

        self.notify(item)

        return item


# ---------------------------------------------------------
# Anwendung
# ---------------------------------------------------------

producer = Producer()

printer = PrintingObserver()
counter = CountingObserver()


# Observer anmelden
producer.attach(printer)
producer.attach(counter)


# Werkstücke produzieren
producer.produce("Zahnrad", 1001)
producer.produce("Schraube", 1002)
producer.produce("Motor", 1003)


============================================


# Producer
#   │
#   │ produce()
#   ↓
# neues Item
#   │
#   ↓
# notify(item)
#   │
#   ├───────────────┐
#   ↓               ↓
# PrintingObserver  CountingObserver
#   ↓               ↓
# ausgeben           zählen



