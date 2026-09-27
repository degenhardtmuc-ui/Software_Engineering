from abc import ABC, abstractmethod


class Account:
    """
    Repräsentiert ein einfaches Bankkonto.

    Das Account-Objekt ist der Receiver im Command Pattern.
    Es führt die eigentlichen Aktionen wie Einzahlen und
    Auszahlen aus.
    """

    def __init__(self, initial_balance=0):
        """
        Erstellt ein Konto mit einem Startguthaben.

        Args:
            initial_balance (float): Startguthaben des Kontos.
        """
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Zahlt einen Betrag auf das Konto ein.

        Args:
            amount (float): Einzuzahlender Betrag.
        """
        self.balance += amount
        print(f"Deposited: ${amount}. New Balance: ${self.balance}")

    def withdraw(self, amount):
        """
        Hebt einen Betrag vom Konto ab.

        Args:
            amount (float): Auszuzahlender Betrag.

        Returns:
            bool: True, wenn die Auszahlung erfolgreich war,
            sonst False.
        """
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New Balance: ${self.balance}")
            return True

        print(f"Insufficient funds. Current Balance: ${self.balance}")
        return False

    def get_balance(self):
        """
        Gibt den aktuellen Kontostand zurück.

        Returns:
            float: Aktueller Kontostand.
        """
        return self.balance


class Command(ABC):
    """
    Abstrakte Basisklasse für alle Commands.

    Jeder konkrete Command muss execute() und undo()
    implementieren.
    """

    def __init__(self, account: Account):
        """
        Speichert den Receiver, auf dem der Command arbeitet.

        Args:
            account (Account): Das betroffene Bankkonto.
        """
        self.account = account

    @abstractmethod
    def execute(self):
        """
        Führt den Command aus.
        """
        pass

    @abstractmethod
    def undo(self):
        """
        Macht den Command rückgängig.
        """
        pass


class DepositCommand(Command):
    """
    Konkreter Command für eine Einzahlung.
    """

    def __init__(self, account, amount):
        """
        Erstellt einen Einzahlungs-Command.

        Args:
            account (Account): Das betroffene Konto.
            amount (float): Der einzuzahlende Betrag.
        """
        super().__init__(account)
        self.amount = amount

    def execute(self):
        """
        Führt die Einzahlung aus.
        """
        self.account.deposit(self.amount)

    def undo(self):
        """
        Macht die Einzahlung rückgängig,
        indem derselbe Betrag wieder ausgezahlt wird.
        """
        self.account.withdraw(self.amount)


class WithdrawCommand(Command):
    """
    Konkreter Command für eine Auszahlung.
    """

    def __init__(self, account, amount):
        """
        Erstellt einen Auszahlungs-Command.

        Args:
            account (Account): Das betroffene Konto.
            amount (float): Der auszuzahlende Betrag.
        """
        super().__init__(account)
        self.amount = amount
        self.executed = False

    def execute(self):
        """
        Führt die Auszahlung aus.

        Der Rückgabewert wird gespeichert, damit nur
        erfolgreiche Auszahlungen rückgängig gemacht werden.
        """
        self.executed = self.account.withdraw(self.amount)

    def undo(self):
        """
        Macht eine erfolgreiche Auszahlung rückgängig,
        indem der Betrag wieder eingezahlt wird.
        """
        if self.executed:
            self.account.deposit(self.amount)


class ATM:
    """
    Repräsentiert den Invoker des Command Patterns.

    Der ATM erstellt und führt Commands aus und verwaltet
    eine Undo- sowie eine Redo-History.
    """

    def __init__(self, initial_balance):
        """
        Erstellt einen ATM mit einem Konto.

        Args:
            initial_balance (float): Startguthaben des Kontos.
        """
        self.account = Account(initial_balance)
        self.history = []
        self.redo_state = []

    def deposit(self, amount):
        """
        Führt eine Einzahlung aus und speichert den Command
        in der History.

        Args:
            amount (float): Einzuzahlender Betrag.
        """
        command = DepositCommand(self.account, amount)
        command.execute()

        self.history.append(command)

        # Neue Aktion macht alte Redo-Schritte ungültig.
        self.redo_state.clear()

    def withdraw(self, amount):
        """
        Führt eine Auszahlung aus.

        Nur erfolgreiche Auszahlungen werden in der History
        gespeichert.

        Args:
            amount (float): Auszuzahlender Betrag.
        """
        command = WithdrawCommand(self.account, amount)
        command.execute()

        if command.executed:
            self.history.append(command)
            self.redo_state.clear()

    def undo(self):
        """
        Macht die zuletzt ausgeführte Transaktion rückgängig.

        Der Command wird aus der History entfernt und auf
        den Redo-Stack gelegt.
        """
        if not self.history:
            print("Nothing to undo.")
            return

        command = self.history.pop()

        command.undo()

        self.redo_state.append(command)

    def redo(self):
        """
        Führt den zuletzt rückgängig gemachten Command
        erneut aus.

        Der Command wird vom Redo-Stack zurück in die
        normale History verschoben.
        """
        if not self.redo_state:
            print("Nothing to redo.")
            return

        command = self.redo_state.pop()

        command.execute()

        self.history.append(command)

    def get_balance(self):
        """
        Gibt den aktuellen Kontostand zurück.

        Returns:
            float: Aktueller Kontostand.
        """
        return self.account.get_balance()


# Test
atm = ATM(1000)

atm.deposit(200)
atm.withdraw(100)

print("Balance:", atm.get_balance())

atm.undo()
print("After undo:", atm.get_balance())

atm.redo()
print("After redo:", atm.get_balance())