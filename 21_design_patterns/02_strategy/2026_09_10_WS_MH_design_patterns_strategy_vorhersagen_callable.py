# Hier bedeutet: Callable[[list[float]], float]

# ganz einfach: Eine Funktion bekommt eine list[float] hinein und gibt einen float zurück.



from typing import Callable


PredictionStrategy = Callable[[list[float]], float]


def average_prediction(values: list[float]) -> float:
    """Verwendet den Mittelwert als Vorhersage."""

    if not values:
        return 0.0

    return sum(values) / len(values)


def last_value_prediction(values: list[float]) -> float:
    """Verwendet den letzten Wert als Vorhersage."""

    if not values:
        return 0.0

    return values[-1]


class Predictor:
    """Verwendet eine austauschbare Vorhersagefunktion."""

    def __init__(self, strategy: PredictionStrategy):
        """Speichert die gewünschte Vorhersage-Strategie."""

        self.strategy = strategy

    def predict(self, values: list[float]) -> float:
        """Führt die aktuelle Strategie aus."""

        return self.strategy(values)


values = [100, 110, 120, 130]

predictor = Predictor(average_prediction)

print(predictor.predict(values))


# Strategie wechseln
predictor.strategy = last_value_prediction

print(predictor.predict(values))