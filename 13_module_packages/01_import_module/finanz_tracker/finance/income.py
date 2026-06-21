class Income:
    """Speichert eine einzelne Einnahme mit Betrag und Quelle."""

    def __init__(self, amount: float, source: str):
        self.amount = amount
        self.source = source


def summarize_incomes(incomes: list[Income]) -> dict[str, float]:
    """Fasst alle Einnahmen nach Quellen zusammen."""

    summary = {}

    for income in incomes:
        if income.source not in summary:
            summary[income.source] = 0

        summary[income.source] += income.amount

    return summary


def total_income(incomes: list[Income]) -> float:
    """Berechnet die gesamten Einnahmen."""

    total = 0

    for income in incomes:
        total += income.amount

    return total