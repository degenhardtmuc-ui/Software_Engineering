from abc import ABC, abstractmethod


class BankAccount:
    """
    Repräsentiert ein einfaches Bankkonto.

    Das BankAccount-Objekt ist im Command Pattern der Receiver.
    Es führt die eigentlichen Aktionen aus:
    Geld einzahlen und Geld auszahlen.
    """

    def __init__(self, balance: float = 0.0):
        """
        Erstellt ein Bankkonto mit einem Startguthaben.

        Args:
            balance (float): Startguthaben des Kontos.
        """
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Zahlt Geld auf das Konto ein.

        Args:
            amount (float): Betrag, der eingezahlt werden soll.
        """
        self.balance += amount
        print(f"{amount:.2f} € eingezahlt.")
        print(f"Neuer Kontostand: {self.balance:.2f} €")

    def withdraw(self, amount: float) -> None:
        """
        Hebt Geld vom Konto ab.

        Args:
            amount (float): Betrag, der ausgezahlt werden soll.

        Raises:
            ValueError: Wenn nicht genügend Guthaben vorhanden ist.
        """
        if amount > self.balance:
            raise ValueError("Nicht genügend Guthaben.")

        self.balance -= amount
        print(f"{amount:.2f} € ausgezahlt.")
        print(f"Neuer Kontostand: {self.balance:.2f} €")

    def show_balance(self) -> None:
        """Gibt den aktuellen Kontostand aus."""
        print(f"Aktueller Kontostand: {self.balance:.2f} €")


class Command(ABC):
    """
    Abstrakte Basisklasse für alle Commands.

    Jeder konkrete Command muss festlegen,
    wie er ausgeführt und rückgängig gemacht wird.
    """

    @abstractmethod
    def execute(self) -> None:
        """Führt den Command aus."""
        pass

    @abstractmethod
    def undo(self) -> None:
        """Macht den Command rückgängig."""
        pass


class DepositCommand(Command):
    """
    Command zum Einzahlen von Geld.

    Der Command kennt den Receiver (BankAccount)
    sowie den einzuzahlenden Betrag.
    """

    def __init__(self, account: BankAccount, amount: float):
        """
        Erstellt einen neuen Einzahlungs-Command.

        Args:
            account (BankAccount): Das betroffene Bankkonto.
            amount (float): Der einzuzahlende Betrag.
        """
        self.account = account
        self.amount = amount

    def execute(self) -> None:
        """Führt die Einzahlung aus."""
        self.account.deposit(self.amount)

    def undo(self) -> None:
        """
        Macht die Einzahlung rückgängig.

        Eine Einzahlung wird rückgängig gemacht,
        indem derselbe Betrag wieder ausgezahlt wird.
        """
        print("Einzahlung wird rückgängig gemacht.")
        self.account.withdraw(self.amount)


class WithdrawCommand(Command):
    """
    Command zum Auszahlen von Geld.

    Der Command kapselt eine Auszahlung
    und kennt das dazugehörige Bankkonto.
    """

    def __init__(self, account: BankAccount, amount: float):
        """
        Erstellt einen neuen Auszahlungs-Command.

        Args:
            account (BankAccount): Das betroffene Bankkonto.
            amount (float): Der auszuzahlende Betrag.
        """
        self.account = account
        self.amount = amount
        self.executed = False

    def execute(self) -> None:
        """
        Führt die Auszahlung aus.

        Wenn die Auszahlung erfolgreich war,
        wird gespeichert, dass der Command ausgeführt wurde.
        """
        self.account.withdraw(self.amount)
        self.executed = True

    def undo(self) -> None:
        """
        Macht die Auszahlung rückgängig.

        Der ausgezahlte Betrag wird wieder eingezahlt.
        """
        if self.executed:
            print("Auszahlung wird rückgängig gemacht.")
            self.account.deposit(self.amount)


class ATM:
    """
    Repräsentiert den Invoker des Command Patterns.

    Der ATM führt Commands aus und speichert sie
    in einer History, damit die letzte Transaktion
    rückgängig gemacht werden kann.
    """

    def __init__(self):
        """Initialisiert den ATM mit einer leeren Command-History."""
        self.history = []

    def execute_command(self, command: Command) -> None:
        """
        Führt einen Command aus und speichert ihn.

        Args:
            command (Command): Der auszuführende Command.
        """
        command.execute()
        self.history.append(command)

    def undo_last_transaction(self) -> None:
        """
        Macht die zuletzt ausgeführte Transaktion rückgängig.

        Falls noch keine Transaktion vorhanden ist,
        wird eine entsprechende Meldung ausgegeben.
        """
        if not self.history:
            print("Keine Transaktion zum Rückgängigmachen vorhanden.")
            return

        command = self.history.pop()
        command.undo()


# -------------------------------------------------
# Client / Testprogramm
# -------------------------------------------------

account = BankAccount(1000.0)
atm = ATM()

print("\n--- Start ---")
account.show_balance()

print("\n--- 200 € einzahlen ---")
deposit_command = DepositCommand(account, 200.0)
atm.execute_command(deposit_command)

print("\n--- 150 € auszahlen ---")
withdraw_command = WithdrawCommand(account, 150.0)
atm.execute_command(withdraw_command)

print("\n--- Letzte Transaktion rückgängig machen ---")
atm.undo_last_transaction()

print("\n--- Aktueller Kontostand ---")
account.show_balance()