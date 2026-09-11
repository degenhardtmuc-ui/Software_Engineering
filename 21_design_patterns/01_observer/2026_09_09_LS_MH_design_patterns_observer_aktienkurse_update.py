from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from random import randint, sample, normalvariate


# ============================================================
# 1. Datenklasse Stock
# ============================================================

@dataclass
class Stock:
    """Repräsentiert eine Aktie mit Name und aktuellem Preis."""

    name: str
    price: float


# ============================================================
# 2. Observer-Interface
# ============================================================

class StockObserver(ABC):
    """Gemeinsame Schnittstelle für alle Aktien-Observer."""

    @abstractmethod
    def update(self, stocks: list[Stock]) -> None:
        """Reagiert auf eine Liste geänderter Aktien."""
        pass


# ============================================================
# 3. Observer: Gibt alle Änderungen aus
# ============================================================

class PrintingStockObserver(StockObserver):
    """Gibt alle Aktien aus, die sich geändert haben."""

    def __init__(self, name: str):
        """Erstellt einen Observer mit einem Namen."""
        self.name = name

    def update(self, stocks: list[Stock]) -> None:
        """Gibt alle erhaltenen Aktien aus."""

        print(
            f"PrintingStockObserver "
            f"{self.name} received update:"
        )

        for stock in stocks:
            print(f"  {stock.name}: {stock.price:.2f}")


# ============================================================
# 4. Observer: Meldet nur gestiegene Kurse
# ============================================================

class RisingStockObserver(StockObserver):
    """Gibt nur Aktien aus, deren Preis gestiegen ist."""

    def __init__(self, name: str):
        """Erstellt den Observer und einen Speicher alter Preise."""

        self.name = name
        self.old_prices: dict[str, float] = {}

    def update(self, stocks: list[Stock]) -> None:
        """Vergleicht neue Preise mit den vorherigen Preisen."""

        for stock in stocks:

            old_price = self.old_prices.get(
                stock.name,
                float("-inf")
            )

            if stock.price > old_price:
                print(
                    f"RisingStockObserver "
                    f"{self.name} received update:"
                )

                print(
                    f"  {stock.name}: "
                    f"{old_price:.2f} -> "
                    f"{stock.price:.2f}"
                )

            # Neuen Preis für später speichern
            self.old_prices[stock.name] = stock.price


# ============================================================
# 5. Subject / Publisher
# ============================================================

@dataclass
class StockMarket:
    """Verwaltet Aktien und benachrichtigt seine Observer."""

    stocks: list[Stock] = field(default_factory=list)

    observers: list[StockObserver] = field(
        default_factory=list
    )

    price_dist_mean: float = 1.0
    price_dist_stddev: float = 0.3

    def attach_observer(
        self,
        observer: StockObserver
    ) -> None:
        """Meldet einen Observer beim Aktienmarkt an."""

        self.observers.append(observer)

    def detach_observer(
        self,
        observer: StockObserver
    ) -> None:
        """Meldet einen Observer wieder ab."""

        self.observers.remove(observer)

    def notify_observers(
        self,
        stocks: list[Stock]
    ) -> None:
        """Sendet die geänderten Aktien an alle Observer."""

        for observer in self.observers:
            observer.update(stocks)

    def add_stock(self, stock: Stock) -> None:
        """Fügt eine Aktie hinzu und informiert die Observer."""

        self.stocks.append(stock)

        self.notify_observers([stock])

    def update_prices(self) -> None:
        """Ändert zufällig einige Aktienkurse."""

        stocks_to_update = (
            self._select_stocks_to_update()
        )

        self._update_prices_for(
            stocks_to_update
        )

        self.notify_observers(
            stocks_to_update
        )

    def _select_stocks_to_update(
        self
    ) -> list[Stock]:
        """Wählt zufällig Aktien aus, deren Preise geändert werden."""

        if not self.stocks:
            return []

        number = randint(
            1,
            len(self.stocks)
        )

        return sample(
            self.stocks,
            number
        )

    def _update_prices_for(
        self,
        stocks: list[Stock]
    ) -> None:
        """Verändert die Preise der ausgewählten Aktien."""

        for stock in stocks:

            change_percent = normalvariate(
                self.price_dist_mean,
                self.price_dist_stddev
            )

            stock.price *= change_percent


# ============================================================
# 6. Anwendung
# ============================================================

market = StockMarket()


# Observer erzeugen
printing_observer = PrintingStockObserver(
    "PrintingObserver"
)

rising_observer = RisingStockObserver(
    "RisingObserver"
)


# Observer anmelden
market.attach_observer(
    printing_observer
)

market.attach_observer(
    rising_observer
)


# Aktien hinzufügen
market.add_stock(
    Stock("Banana", 100.0)
)

market.add_stock(
    Stock("Billionz", 200.0)
)

market.add_stock(
    Stock("Microsoft", 300.0)
)

market.add_stock(
    Stock("BCD", 400.0)
)


# Preise zufällig verändern
market.update_prices()




==============================================


#                    StockMarket
#                      SUBJECT
#                         │
#                         │ enthält
#                         ↓
#                       Stock
#
#StockMarket
#    │
#    │ notify_observers(stocks)
#    ↓
#               StockObserver
#                INTERFACE
#                    │
#
#             ┌──────┴──────┐
#             ↓             ↓
# PrintingStockObserver   RisingStockObserver
#             │             │
#         zeigt alle     zeigt nur
#         Änderungen     Preissteigerungen

# def notify_observers(self, stocks):
#    for observer in self.observers:
#        observer.update(stocks)


# Gehe durch alle angemeldeten Observer und gib jedem die geänderten Aktien.

# Das ist Push, weil StockMarket die Daten stocks direkt an: update(stocks) übergibt.

# Warum zwei verschiedene Observer? - Der PrintingStockObserver sagt: „Ich möchte jede Änderung sehen.“

# Der RisingStockObserver sagt: „Mich interessieren nur gestiegene Aktien.“

# Jeder Observer entscheidet selbst, was er mit der Benachrichtigung macht.

# Der StockMarket kennt nur das StockObserver-Interface. 
# Dadurch kann ich beliebig neue Observer hinzufügen, ohne den StockMarket ändern zu müssen.

# Das ist gleichzeitig Low Coupling und einer der größten Vorteile des Observer Patterns