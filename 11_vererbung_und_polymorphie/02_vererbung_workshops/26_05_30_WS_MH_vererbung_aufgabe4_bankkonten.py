"""
Workshop: Bankkonten

This file shows inheritance in Python:
- BankKonto is the base class.
- SparKonto inherits from BankKonto.
- GiroKonto inherits from BankKonto.
"""


class BankKonto:
    """Simple base class for a normal bank account."""

    def __init__(self, konto_nummer, saldo, konto_inhaber):
        """Create a new bank account object."""
        self.konto_nummer = konto_nummer
        self.saldo = float(saldo)
        self.konto_inhaber = konto_inhaber

    def zahle_ein(self, betrag):
        """Deposit money into the account."""
        if betrag <= 0:
            return False

        self.saldo = self.saldo + betrag
        return True

    def hebe_ab(self, betrag):
        """Withdraw money if enough balance is available."""
        if betrag <= 0:
            return False

        if betrag <= self.saldo:
            self.saldo = self.saldo - betrag
            return True

        return False

    def get_saldo(self):
        """Return the current balance."""
        return self.saldo

    def konto_info(self):
        """Return account information as a string."""
        return (
            f"Kontonummer: {self.konto_nummer}, "
            f"Inhaber: {self.konto_inhaber}, "
            f"Saldo: {self.saldo:.2f} EUR"
        )


class SparKonto(BankKonto):
    """Savings account: it has interest and a withdrawal fee."""

    def __init__(self, konto_nummer, saldo, konto_inhaber, zinssatz):
        """Create a savings account object."""
        super().__init__(konto_nummer, saldo, konto_inhaber)
        self.zinssatz = zinssatz

    def addiere_zinsen(self):
        """Add interest to the current balance."""
        self.saldo = self.saldo * (1 + self.zinssatz)
        return self.saldo

    def hebe_ab(self, betrag):
        """Withdraw money and also subtract a 1.50 EUR fee."""
        if betrag <= 0:
            return False

        gebuehr = 1.50
        gesamtkosten = betrag + gebuehr

        if gesamtkosten <= self.saldo:
            self.saldo = self.saldo - gesamtkosten
            return True

        return False

    def konto_info(self):
        """Return savings account information as a string."""
        return (
            super().konto_info()
            + f", Zinssatz: {self.zinssatz * 100:.2f}%"
        )


class GiroKonto(BankKonto):
    """Checking account: it allows overdraft up to a limit."""

    def __init__(self, konto_nummer, saldo, konto_inhaber, ueberziehungs_limit):
        """Create a checking account object."""
        super().__init__(konto_nummer, saldo, konto_inhaber)
        self.ueberziehungs_limit = ueberziehungs_limit

    def hebe_ab(self, betrag):
        """Withdraw money if the overdraft limit is not exceeded."""
        if betrag <= 0:
            return False

        neuer_saldo = self.saldo - betrag

        if neuer_saldo >= -self.ueberziehungs_limit:
            self.saldo = neuer_saldo
            return True

        return False

    def ziehe_monatliche_gebuehr_ab(self, gebuehr):
        """Subtract the monthly account fee."""
        return self.hebe_ab(gebuehr)

    def konto_info(self):
        """Return checking account information as a string."""
        return (
            super().konto_info()
            + f", Ueberziehungslimit: {self.ueberziehungs_limit:.2f} EUR"
        )


# ------------------------------------------------------------
# Testbereich mit assert
# ------------------------------------------------------------
# assert bedeutet: Python prueft, ob eine Aussage wahr ist.
# Wenn die Aussage falsch ist, stoppt das Programm mit einem Fehler.
# Wenn kein Fehler kommt, ist der Test bestanden.


# 1. BankKonto testen
bankkonto = BankKonto("B-100", 100.0, "Daniel")
assert bankkonto.konto_nummer == "B-100"
assert bankkonto.get_saldo() == 100.0

assert bankkonto.zahle_ein(50.0) is True
assert bankkonto.get_saldo() == 150.0

assert bankkonto.hebe_ab(30.0) is True
assert bankkonto.get_saldo() == 120.0

assert bankkonto.hebe_ab(200.0) is False
assert bankkonto.get_saldo() == 120.0

assert bankkonto.zahle_ein(-10.0) is False
assert bankkonto.get_saldo() == 120.0

assert "Daniel" in bankkonto.konto_info()


# 2. SparKonto testen
sparkonto = SparKonto("S-200", 1000.0, "Irena", 0.02)
assert sparkonto.konto_nummer == "S-200"
assert sparkonto.zinssatz == 0.02

sparkonto.addiere_zinsen()
assert round(sparkonto.get_saldo(), 2) == 1020.00

assert sparkonto.hebe_ab(100.0) is True
assert round(sparkonto.get_saldo(), 2) == 918.50

assert sparkonto.hebe_ab(2000.0) is False
assert round(sparkonto.get_saldo(), 2) == 918.50

assert sparkonto.hebe_ab(-5.0) is False
assert round(sparkonto.get_saldo(), 2) == 918.50

assert "Zinssatz" in sparkonto.konto_info()


# 3. GiroKonto testen
girokonto = GiroKonto("G-300", 100.0, "Daniel", 500.0)
assert girokonto.konto_nummer == "G-300"
assert girokonto.ueberziehungs_limit == 500.0

assert girokonto.hebe_ab(550.0) is True
assert girokonto.get_saldo() == -450.0

assert girokonto.hebe_ab(60.0) is False
assert girokonto.get_saldo() == -450.0

assert girokonto.ziehe_monatliche_gebuehr_ab(10.0) is True
assert girokonto.get_saldo() == -460.0

assert girokonto.ziehe_monatliche_gebuehr_ab(50.0) is False
assert girokonto.get_saldo() == -460.0

assert girokonto.zahle_ein(60.0) is True
assert girokonto.get_saldo() == -400.0

assert "Ueberziehungslimit" in girokonto.konto_info()


# 4. Kleine sichtbare Ausgabe fuer VS Code
print("Alle assert-Tests wurden bestanden.")
print()
print("Bankkonto:")
print(bankkonto.konto_info())
print()
print("Sparkonto:")
print(sparkonto.konto_info())
print()
print("Girokonto:")
print(girokonto.konto_info())