from ..income import Income, summarize_incomes, total_income
from ..expenses import Expense, summarize_expenses, total_expenses


def print_financial_report(incomes: list[Income], expenses: list[Expense]) -> None:
    """Druckt einen einfachen Finanzbericht aus."""

    income_summary = summarize_incomes(incomes)
    expense_summary = summarize_expenses(expenses)

    total_in = total_income(incomes)
    total_out = total_expenses(expenses)

    result = total_in - total_out

    print("Finanzbericht")
    print("-" * 30)

    print("Einnahmen pro Quelle:")
    for source, amount in income_summary.items():
        print(f"{source}: {amount:.2f} Euro")

    print()

    print("Ausgaben pro Kategorie:")
    for category, amount in expense_summary.items():
        print(f"{category}: {amount:.2f} Euro")

    print()

    print(f"Gesamteinnahmen: {total_in:.2f} Euro")
    print(f"Gesamtausgaben: {total_out:.2f} Euro")

    if result >= 0:
        print(f"Überschuss: {result:.2f} Euro")
    else:
        print(f"Defizit: {abs(result):.2f} Euro")