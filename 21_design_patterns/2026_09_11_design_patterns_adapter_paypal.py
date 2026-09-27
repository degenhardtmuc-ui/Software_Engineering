# Die PayPal-API ist inkompatibel, weil sie sendPayment() statt pay() verwendet und außerdem Cent statt Euro erwartet. 
# Der Adapter übersetzt sowohl die Schnittstelle als auch die Daten


# Checkout
#   │
#   │ pay(10.00 €)
#   ↓
# PayPalAdapter
#    │
#   │ 10 € × 100
#   ↓
# PayPalApi
#   │
#   │ send_payment(1000)
#   ↓
# 1000 Cent

# Client: Checkout
# Target: PaymentService
# Adapter: PayPalAdapter
# Adaptee: PayPalApi





from abc import ABC, abstractmethod


class PaymentService(ABC):
    """Gemeinsame Schnittstelle für Zahlungen in unserer Anwendung."""

    @abstractmethod
    def pay(self, amount_in_euro: float) -> None:
        """Führt eine Zahlung in Euro aus."""
        pass


class PayPalApi:
    """Simuliert eine fremde PayPal-API.

    Die API erwartet den Betrag in Cent und verwendet
    die Methode send_payment().
    """

    def send_payment(self, amount_in_cents: int) -> None:
        """Sendet eine PayPal-Zahlung in Cent."""
        print(f"PayPal-Zahlung: {amount_in_cents} Cents")


class PayPalAdapter(PaymentService):
    """Passt die PayPalApi an unseren PaymentService an."""

    def __init__(self, paypal_api: PayPalApi):
        """Speichert die vorhandene PayPal-API."""
        self.paypal_api = paypal_api

    def pay(self, amount_in_euro: float) -> None:
        """Übersetzt Euro in Cent und pay() in send_payment()."""

        amount_in_cents = int(round(amount_in_euro * 100))

        self.paypal_api.send_payment(amount_in_cents)


class Checkout:
    """Verwendet einen PaymentService zum Bezahlen."""

    def __init__(self, payment_service: PaymentService):
        """Speichert den verwendeten Zahlungsdienst."""
        self.payment_service = payment_service

    def checkout(self, amount_in_euro: float) -> None:
        """Führt den Bezahlvorgang aus."""
        self.payment_service.pay(amount_in_euro)


# --------------------------------------------------
# Nutzung
# --------------------------------------------------

paypal_api = PayPalApi()

paypal_adapter = PayPalAdapter(paypal_api)

checkout = Checkout(paypal_adapter)

checkout.checkout(10.00)


========================================================

@Override
public void pay(double amountInEuro) {
    creditCard.payWithCreditCard(amountInEuro);
}

# In meiner Schnittstellen-Implementierung nutze ich den fremden Dienst
# Checkout
#   │
#   │ erwartet pay(1000)
#   ↓
# CreditCardAdapter
#   │
#   │ übersetzt
#   ↓
# payWithCreditCard(1000)
#    │
#   ↓
# CreditCard

# Der Adapter implementiert meine gewünschte PaymentService-Schnittstelle und delegiert pay() an die inkompatible Methode payWithCreditCard() des fremden Dienstes

from abc import ABC, abstractmethod


class PaymentService(ABC):
    """Definiert die gemeinsame Schnittstelle für Zahlungen."""

    @abstractmethod
    def pay(self, amount: float) -> None:
        """Führt eine Zahlung aus."""
        pass


class CreditCard:
    """Fremder Kreditkarten-Dienst mit eigener Schnittstelle."""

    def pay_with_credit_card(self, amount: float) -> None:
        """Führt eine Kreditkartenzahlung aus."""
        print(f"Kreditkartenzahlung: {amount} Euro")


class CreditCardAdapter(PaymentService):
    """Passt CreditCard an die PaymentService-Schnittstelle an."""

    def __init__(self, credit_card: CreditCard):
        """Speichert den fremden Kreditkarten-Dienst."""
        self.credit_card = credit_card

    def pay(self, amount: float) -> None:
        """Übersetzt pay() in pay_with_credit_card()."""
        self.credit_card.pay_with_credit_card(amount)


# Nutzung
credit_card = CreditCard()

adapter = CreditCardAdapter(credit_card)

adapter.pay(1000)
