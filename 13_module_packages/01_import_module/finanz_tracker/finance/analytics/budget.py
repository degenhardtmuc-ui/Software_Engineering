from ..expenses import Expense, total_expenses


class Budget:
    """Speichert ein Budget-Limit und prüft, ob die Ausgaben darunter bleiben."""

    def __init__(self, limit: float):
        self.limit = limit

    def can_afford(self, expenses: list[Expense]) -> bool:
        """Prüft, ob die gesamten Ausgaben innerhalb des Budgets liegen."""

        total = total_expenses(expenses)

        return total <= self.limit