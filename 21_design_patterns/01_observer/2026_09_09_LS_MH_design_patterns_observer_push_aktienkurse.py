# Beim Push Observer übergibt das Subject die relevanten geänderten Daten direkt an update(). 
# Der Observer muss die Daten also nicht selbst beim Subject abfragen.
# StockMarket
#    │
#    ├── attach()   → Observer anmelden
#    ├── detach()   → Observer abmelden
#    │
#    └── notify()
#          │
#          ├── PrintingStockObserver
#          │       → zeigt alles
#│
#          └── RisingStockObserver
#                  → reagiert auf steigende Kurse






from dataclasses import dataclass, field
from abc import ABC, abstractmethod


# ---------------------------------------------------------
# 1. Aktie
# ---------------------------------------------------------

@dataclass
class Stock:
    """Repräsentiert eine Aktie mit Name und aktuellem Preis."""

    name: str
    price: float


# ---------------------------------------------------------
# 2. Observer Interface
# ---------------------------------------------------------

class StockObserver(ABC):
    """Schnittstelle für alle Beobachter des Aktienmarktes."""

    @abstractmethod
    def update(self, stock: Stock) -> None:
        """Reagiert auf eine Änderung einer Aktie."""
        pass


# ---------------------------------------------------------
# 3. Observer 1: Gibt jede Änderung aus
# ---------------------------------------------------------

class PrintingStockObserver(StockObserver):
    """Gibt jede neue oder geänderte Aktie aus."""

    def update(self, stock: Stock) -> None:
        """Zeigt den aktuellen Aktienkurs an."""

        print(f"[Printer] {stock.name}: {stock.price:.2f}")


# ---------------------------------------------------------
# 4. Observer 2: Meldet nur steigende Kurse
# ---------------------------------------------------------

class RisingStockObserver(StockObserver):
    """Meldet eine Aktie nur dann, wenn ihr Kurs gestiegen ist."""

    def __init__(self):
        """Speichert die vorherigen Kurse der Aktien."""

        self.old_prices = {}

    def update(self, stock: Stock) -> None:
        """Prüft, ob der Aktienkurs gestiegen ist."""

        old_price = self.old_prices.get(stock.name)

        if old_price is None:
            print(
                f"[RisingAlert] {stock.name}: "
                f"-inf -> {stock.price:.2f}"
            )

        elif stock.price > old_price:
            print(
                f"[RisingAlert] {stock.name}: "
                f"{old_price:.2f} -> {stock.price:.2f}"
            )

        # Aktuellen Preis für die nächste Prüfung merken
        self.old_prices[stock.name] = stock.price


# ---------------------------------------------------------
# 5. Subject / Publisher
# ---------------------------------------------------------

@dataclass
class StockMarket:
    """Verwaltet Aktien und benachrichtigt seine Observer."""

    stocks: list[Stock] = field(default_factory=list)
    _observers: list[StockObserver] = field(default_factory=list)

    def attach(self, observer: StockObserver) -> None:
        """Meldet einen Observer beim Aktienmarkt an."""

        self._observers.append(observer)

    def detach(self, observer: StockObserver) -> None:
        """Meldet einen Observer wieder ab."""

        self._observers.remove(observer)

    def _notify_observers(self, stock: Stock) -> None:
        """Sendet die geänderte Aktie an alle Observer."""

        for observer in self._observers:
            observer.update(stock)

    def add_stock(self, stock: Stock) -> None:
        """Fügt eine Aktie hinzu und informiert die Observer."""

        self.stocks.append(stock)
        self._notify_observers(stock)

    def update_stock_price(
        self,
        name: str,
        new_price: float
    ) -> None:
        """Ändert einen Aktienkurs und informiert die Observer."""

        for stock in self.stocks:

            if stock.name == name:
                stock.price = new_price

                self._notify_observers(stock)
                return

        raise ValueError(f"Aktie {name!r} nicht gefunden")


# ---------------------------------------------------------
# 6. Anwendung
# ---------------------------------------------------------

market = StockMarket()

printer = PrintingStockObserver()
rising_alert = RisingStockObserver()


# Observer anmelden
market.attach(printer)
market.attach(rising_alert)


# Aktien hinzufügen
market.add_stock(Stock("Banana", 100.0))
market.add_stock(Stock("Billionz", 200.0))
market.add_stock(Stock("Microsoft", 300.0))


# Kurs steigt
market.update_stock_price("Banana", 105.0)


# Kurs fällt
market.update_stock_price("Billionz", 190.0)


# Kurs steigt
market.update_stock_price("Microsoft", 310.0)


===========================================

# Beim Aktien-Beispiel ist StockMarket das Subject/Publisher. 
# Es verwaltet seine Observer und ruft bei einer Änderung aktiv deren update(...) auf:

# def _notify_observers(self, stock):
#    for observer in self._observers:
#        observer.update(stock)

# Der entscheidende Punkt bei Push ist:

# Das Subject schickt die geänderten Daten direkt an die Observer.

# Also:

# Aktienkurs ändert sich
#        ↓
# StockMarket
        ↓
# _notify_observers(stock)
#        ↓
# observer.update(stock)
#        ↓
# ┌───────────────┬────────────────┐
# ↓               ↓
# PrintingObserver RisingStockObserver

# attach() meldet einen Observer an, detach() entfernt ihn und update(stock) ist die Reaktion des jeweiligen Observers.

# Besonders interessant ist der RisingStockObserver: 
# Er reagiert nicht einfach auf alles, sondern prüft zusätzlich eine Bedingung. 

# Das entspricht sehr gut unserem früheren 75-%-Skill-Beispiel: 
# Benachrichtigung kommt an, aber der konkrete Observer entscheidet, ob daraus eine Aktion entsteht.






