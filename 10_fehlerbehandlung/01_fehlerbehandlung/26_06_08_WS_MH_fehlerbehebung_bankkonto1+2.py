# bank_account_app.py
# Workshop: Bank Account (Teil 1 + Teil 2)


class BankAccount:
    """Eine einfache Klasse für ein Bankkonto."""

    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Startguthaben darf nicht negativ sein.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Einzahlung darf nicht negativ sein.")
        self.balance = self.balance + amount
        print(f"{amount:.2f} Euro eingezahlt.")
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Auszahlung darf nicht negativ sein.")
        if self.balance - amount < 0:
            raise ValueError("Nicht genug Guthaben auf dem Konto.")
        self.balance = self.balance - amount
        print(f"{amount:.2f} Euro abgehoben.")
        return self.balance

    def show_balance(self):
        print(f"Konto von {self.owner}: {self.balance:.2f} Euro")


def test_successful_transactions():
    print("=== Erfolgreiche Transaktionen ===")
    account = BankAccount("Daniel", 100)
    account.show_balance()

    account.deposit(50)
    account.show_balance()

    account.withdraw(30)
    account.show_balance()


def test_error_transactions():
    print("\n=== Fehlerfälle mit Exceptions ===")

    try:
        account = BankAccount("Fehlerkonto", -10)
    except ValueError as error:
        print("Fehler beim Erstellen:", error)

    account = BankAccount("Testkonto", 100)

    try:
        account.deposit(-20)
    except ValueError as error:
        print("Fehler bei deposit:", error)

    try:
        account.withdraw(-30)
    except ValueError as error:
        print("Fehler bei withdraw:", error)

    try:
        account.withdraw(200)
    except ValueError as error:
        print("Fehler bei withdraw:", error)


def main():
    test_successful_transactions()
    test_error_transactions()


if __name__ == "__main__":
    main()