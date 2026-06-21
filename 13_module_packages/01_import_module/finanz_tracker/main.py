from finance.expenses import Expense
from finance.income import Income
from finance.analytics.budget import Budget
from finance.analytics.reporting import print_financial_report


def main():
    """Testet den persönlichen Finanz-Tracker."""

    expenses = [
        Expense(50.00, "Lebensmittel"),
        Expense(20.00, "Transport"),
        Expense(100.00, "Freizeit"),
        Expense(30.00, "Lebensmittel"),
    ]

    incomes = [
        Income(1200.00, "Gehalt"),
        Income(150.00, "Nebenjob"),
    ]

    budget = Budget(250.00)

    if budget.can_afford(expenses):
        print("Die Ausgaben liegen im Budget.")
    else:
        print("Die Ausgaben liegen über dem Budget.")

    print()

    print_financial_report(incomes, expenses)


main()