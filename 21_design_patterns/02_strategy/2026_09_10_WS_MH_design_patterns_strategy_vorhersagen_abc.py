# Mittelwert aller Werte
# letzter Wert, beziehungsweise 0, wenn die Liste leer ist.

from abc import ABC, abstractmethod


# ============================================================
# Strategy Interface
# ============================================================

class PredictionStrategy(ABC):
    """Definiert die Schnittstelle für Vorhersage-Strategien."""

    @abstractmethod
    def predict(self, values: list[float]) -> float:
        """Berechnet aus vorhandenen Werten eine Vorhersage."""
        pass


# ============================================================
# Strategy 1: Mittelwert
# ============================================================

class AverageStrategy(PredictionStrategy):
    """Verwendet den Mittelwert als Vorhersage."""

    def predict(self, values: list[float]) -> float:
        """Berechnet den Mittelwert aller vorhandenen Werte."""

        if not values:
            return 0.0

        return sum(values) / len(values)


# ============================================================
# Strategy 2: Letzter Wert
# ============================================================

class LastValueStrategy(PredictionStrategy):
    """Verwendet den letzten Wert als Vorhersage."""

    def predict(self, values: list[float]) -> float:
        """Gibt den letzten Wert oder bei leerer Liste 0 zurück."""

        if not values:
            return 0.0

        return values[-1]

# =============================================================
# Context
# ============================================================

class Predictor:
    """Erstellt Vorhersagen mit einer austauschbaren Strategie."""

    def __init__(self, strategy: PredictionStrategy):
        """Erstellt einen Predictor mit einer Strategie."""

        self.strategy = strategy

    def predict(self, values: list[float]) -> float:
        """Delegiert die Vorhersage an die aktuelle Strategie."""

        return self.strategy.predict(values)


# ============================================================
# Nutzung
# ============================================================

values = [
    100.0,
    110.0,
    120.0,
    130.0
]


# Mittelwert-Strategie
predictor = Predictor(AverageStrategy())

result = predictor.predict(values)

print("Mittelwert-Vorhersage:", result)


# Strategie wechseln
predictor.strategy = LastValueStrategy()

result = predictor.predict(values)

print("Letzter-Wert-Vorhersage:", result)


=====================================================================

================================================


# Der Predictor wird nicht geändert: predictor.predict(values)

# Nur diese Zeile ändert sich: predictor.strategy = AverageStrategy()

# oder: predictor.strategy = LastValueStrategy()



#                    PredictionStrategy
#                           │
#                  ┌────────┴────────┐
#                  ↓                 ↓
#          AverageStrategy    LastValueStrategy
#                  \                 /
#                   \               /
#                        Predictor
# Der Predictor ist der Context. 
# PredictionStrategy definiert die gemeinsame Schnittstelle und AverageStrategy sowie LastValueStrategy implementieren unterschiedliche Algorithmen. 
# Die Strategie kann ausgetauscht werden, ohne den Predictor zu verändern.
# ============================================================