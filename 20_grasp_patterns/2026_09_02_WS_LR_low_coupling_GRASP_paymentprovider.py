# Low Coupling = geringe Abhängigkeit zwischen Klassen.
# Dependency Injection = Abhängigkeit wird von außen übergeben.
# Protocol = definiert den benötigten Vertrag.
# Polymorphie = unterschiedliche Objekte können über dieselbe Schnittstelle benutzt werden.
# DIP (SOLID) = die höhere Logik hängt von einer Abstraktion statt einer konkreten Implementierung ab.

# geringe Kopplung: OrderProcessor kennt nicht mehr CreditCardPayment direkt, sondern nur den Vertrag PaymentProvider. 
# Die konkrete Zahlungsart wird von außen über den Konstruktor injiziert.“



from typing import Protocol


# Schnittstelle / Vertrag
class PaymentProvider(Protocol):
    def pay(self, amount: float) -> None:
        ...


# Konkrete Implementierung: Kreditkarte
class CreditCardPayment:
    def pay(self, amount: float) -> None:
        print(f"Zahle {amount}€ per Kreditkarte.")


# Konkrete Implementierung: PayPal
class PaypalPayment:
    def pay(self, amount: float) -> None:
        print(f"Zahle {amount}€ per PayPal.")


# Verarbeitung der Bestellung
class OrderProcessor:
    def __init__(self, payment_provider: PaymentProvider):
        # Geringe Kopplung:
        # Die konkrete Zahlungsart wird von außen übergeben.
        self.payment_provider = payment_provider

    def checkout(self, amount: float) -> None:
        self.payment_provider.pay(amount)


# Flexibler Einsatz mit Kreditkarte
processor = OrderProcessor(CreditCardPayment())
processor.checkout(49.99)


# Flexibler Einsatz mit PayPal
processor = OrderProcessor(PaypalPayment())
processor.checkout(29.99)

# Ausgabe wäre: Zahle 49.99€ per Kreditkarte.
# Zahle 29.99€ per PayPal.

====================================================
# Der OrderProcessor baut sich seine Kreditkartenzahlung nicht mehr selbst. Er sagt nur:
# „Gib mir irgendeinen Zahlungsdienst, der pay() kann.“

# Deshalb funktioniert:
# processor = OrderProcessor(CreditCardPayment())
# genauso wie:
# processor = OrderProcessor(PaypalPayment())
# ohne eine einzige Zeile im OrderProcessor zu ändern.

# OrderProcessor ist jetzt nicht mehr fest an CreditCardPayment gekoppelt. 
# Er erwartet nur ein Objekt, das dem PaymentProvider-Protocol entspricht und eine pay()-Methode besitzt. 
# Dadurch kannst du unterschiedliche Zahlungsarten flexibel austauschen

=====================================================

# Frage?: Funktioniert es auch mit ABC?
# ABC arbeitet mit expliziter Vererbung und eignet sich für eine echte Klassenhierarchie. 
# Protocol arbeitet mit Structural Typing: Entscheidend ist nicht, von welcher Klasse ein Objekt erbt, sondern ob es die benötigten Methoden besitzt.
# ABC = Was bist du?
# Protocol = Was kannst du?

from abc import ABC, abstractmethod
from typing import Protocol


# ==========================================
# 1. ABC-Ansatz – explizite Vererbung
# ==========================================

class SpeakerABC(ABC):

    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(SpeakerABC):
    # MUSS explizit von SpeakerABC erben

    def speak(self) -> str:
        return "Woof"


# ==========================================
# 2. Protocol-Ansatz – Structural Typing
# ==========================================

class SpeakerProtocol(Protocol):

    def speak(self) -> str:
        ...


class Robot:
    # Erbt NICHT von SpeakerProtocol

    def speak(self) -> str:
        return "Beep Boop"


def make_it_speak(item: SpeakerProtocol) -> None:
    print(item.speak())


# Funktioniert ohne Vererbung:
make_it_speak(Robot())

========================================