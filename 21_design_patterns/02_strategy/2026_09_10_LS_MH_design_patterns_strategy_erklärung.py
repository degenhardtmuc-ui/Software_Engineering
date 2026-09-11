from abc import ABC, abstractmethod


class Strategy(ABC):
    """Definiert die gemeinsame Schnittstelle aller Strategien."""

    @abstractmethod
    def algorithm(self, values: list[float]) -> float:
        """Führt den jeweiligen Algorithmus aus."""
        pass


class StrategyA(Strategy):
    """Erste konkrete Strategie."""

    def algorithm(self, values: list[float]) -> float:
        """Berechnet mit Algorithmus A ein Ergebnis."""
        return sum(values)


class StrategyB(Strategy):
    """Zweite konkrete Strategie."""

    def algorithm(self, values: list[float]) -> float:
        """Berechnet mit Algorithmus B ein Ergebnis."""
        return max(values)


class Context:
    """Verwendet eine austauschbare Strategie."""

    def __init__(self, strategy: Strategy):
        """Speichert die gewünschte Strategie."""
        self.strategy = strategy

    def execute(self, values: list[float]) -> float:
        """Delegiert die Berechnung an die Strategie."""
        return self.strategy.algorithm(values)


context = Context(StrategyA())

print(context.execute([10, 20, 30]))

# Strategie wechseln
context.strategy = StrategyB()

print(context.execute([10, 20, 30]))


===========================================================

#                    Strategy
#                       ABC
#                        │
#            ┌───────────┼───────────┐
#            ↓           ↓           ↓
#       Strategy A   Strategy B   Strategy C
#            \           |           /
#                        ↓
#                     Context

# Der Context weiß, dass er eine Strategie benutzen soll, aber die konkrete Berechnung steckt in der jeweiligen Strategy-Klasse