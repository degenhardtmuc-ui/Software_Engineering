class Expense:
    """Speichert eine einzelne Ausgabe mit Betrag und Kategorie."""

    def __init__(self, amount: float, category: str):
        self.amount = amount
        self.category = category


def summarize_expenses(expenses: list[Expense]) -> dict[str, float]:
    """Fasst alle Ausgaben nach Kategorien zusammen."""

    summary = {}

    for expense in expenses:
        if expense.category not in summary:
            summary[expense.category] = 0

        summary[expense.category] += expense.amount

    return summary


def total_expenses(expenses: list[Expense]) -> float:
    """Berechnet die gesamten Ausgaben."""

    total = 0

    for expense in expenses:
        total += expense.amount

    return total