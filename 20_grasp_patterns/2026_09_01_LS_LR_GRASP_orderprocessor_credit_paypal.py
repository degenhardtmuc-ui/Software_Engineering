class CreditCardPayment:

    def pay(self, amount: float):

        print(f"Zahle {amount}€ per Kreditkarte.")

class PayPalPayment:

    def pay(self, amount: float):

        print(f"Zahle {amount}€ per PayPal.")

class OrderProcessor:

    def __init__(self):

        # Enge Kopplung: Instanziiert die konkrete Klasse selbst

        self.payment = CreditCardPayment()

 

    def checkout(self, amount: float):

        self.payment.pay(amount)

=====================

Lösung

from typing import Protocol

# Schnittstelle / Vertrag

class PaymentProvider(Protocol):

    def pay(self, amount: float) -> None:

        ...

============

class CreditCardPayment:

    def pay(self, amount: float) -> None:

        print(f"Zahle {amount}€ per Kreditkarte.")

=========

class PaypalPayment:

    def pay(self, amount: float) -> None:

        print(f"Zahle {amount}€ per PayPal.")

==============

class OrderProcessor:

    def __init__(self, payment_provider: PaymentProvider):

        # Geringe Kopplung: Die Abhängigkeit wird von außen übergeben

        self.payment_provider = payment_provider

 

    def checkout(self, amount: float):

        self.payment_provider.pay(amount)

# Flexibler Einsatz:

processor = OrderProcessor(CreditCardPayment())

processor.checkout(49.99)

Aufgabe
Wie würdest du die Klasse UserManager umbauen, um die Kopplung zu reduzieren, sodass flexibel auch ein SMSNotifier oder SlackNotifier übergeben werden

class EmailNotifier:

    def send(self, message: str):

        print(f"E-Mail gesendet: {message}")

 

class UserManager:

    def __init__(self):

        self.notifier = EmailNotifier()

 

    def register_user(self, username: str):

        print(f"Benutzer {username} angelegt.")

        self.notifier.send(f"Willkommen, {username}!")


==============================================================

from typing import Protocol


# 1. Vertrag / Schnittstelle
class Notifier(Protocol):

    def send(self, message: str) -> None:
        ...


# 2. Konkrete Implementierungen
class EmailNotifier:

    def send(self, message: str) -> None:
        print(f"E-Mail gesendet: {message}")


class SMSNotifier:

    def send(self, message: str) -> None:
        print(f"SMS gesendet: {message}")


class SlackNotifier:

    def send(self, message: str) -> None:
        print(f"Slack-Nachricht gesendet: {message}")


# 3. UserManager kennt nur noch den Vertrag
class UserManager:

    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def register_user(self, username: str) -> None:
        print(f"Benutzer {username} angelegt.")
        self.notifier.send(f"Willkommen, {username}!")

manager = UserManager(EmailNotifier())
manager.register_user("Daniel")

manager = UserManager(SMSNotifier())
manager.register_user("Daniel")

manager = UserManager(SlackNotifier())
manager.register_user("Daniel")

#Problem war: self.notifier = EmailNotifier()
# UserManager erzeugt selbst einen konkreten EmailNotifier

# „Ich reduziere die Kopplung, indem ich einen Notifier als Protocol definiere und die konkrete Implementierung per Dependency Injection 
# an den UserManager übergebe. 
#Dadurch hängt UserManager nicht mehr direkt von EmailNotifier ab und ich kann beispielsweise SMSNotifier oder SlackNotifier austauschen, 
# ohne UserManager zu verändern.“

