from abc import ABC, abstractmethod


# ============================================================
# Gemeinsame Schnittstelle / Target
# ============================================================

class MessageService(ABC):
    """Definiert die einheitliche Schnittstelle für Nachrichtendienste."""

    @abstractmethod
    def send(self, receiver: str, message: str) -> None:
        """Sendet eine Nachricht an einen Empfänger."""
        pass

    @abstractmethod
    def receive(self, receiver: str) -> None:
        """Empfängt eine Nachricht."""
        pass


# ============================================================
# Vorhandener Dienst 1: SMS
# ============================================================

class SMS:
    """Vorhandener SMS-Dienst mit eigener Schnittstelle."""

    def send_text(self, number: str, message: str) -> None:
        """Sendet eine SMS an eine Telefonnummer."""
        print(f"SMS an {number}: {message}")

    def receive_text(self, number: str) -> None:
        """Empfängt eine SMS von einer Telefonnummer."""
        print(f"SMS von {number} empfangen.")


# ============================================================
# Vorhandener Dienst 2: E-Mail
# ============================================================

class Email:
    """Vorhandener E-Mail-Dienst mit eigener Schnittstelle."""

    def send_email(self, address: str, text: str) -> None:
        """Sendet eine E-Mail."""
        print(f"E-Mail an {address}: {text}")

    def receive_email(self, address: str) -> None:
        """Empfängt eine E-Mail."""
        print(f"E-Mail von {address} empfangen.")


# ============================================================
# Vorhandener Dienst 3: In-App-Chat
# ============================================================

class InAppChat:
    """Vorhandener In-App-Chat mit eigener Schnittstelle."""

    def post_message(self, username: str, text: str) -> None:
        """Sendet eine Nachricht im In-App-Chat."""
        print(f"Chat an {username}: {text}")

    def read_message(self, username: str) -> None:
        """Liest eine Nachricht im In-App-Chat."""
        print(f"Chat-Nachricht von {username} empfangen.")


# ============================================================
# Adapter für SMS
# ============================================================

class SMSAdapter(MessageService):
    """Passt den SMS-Dienst an die gemeinsame Schnittstelle an."""

    def __init__(self, sms: SMS):
        """Speichert den vorhandenen SMS-Dienst."""
        self.sms = sms

    def send(self, receiver: str, message: str) -> None:
        """Übersetzt send() in send_text()."""
        self.sms.send_text(receiver, message)

    def receive(self, receiver: str) -> None:
        """Übersetzt receive() in receive_text()."""
        self.sms.receive_text(receiver)


# ============================================================
# Adapter für E-Mail
# ============================================================

class EmailAdapter(MessageService):
    """Passt den E-Mail-Dienst an die gemeinsame Schnittstelle an."""

    def __init__(self, email: Email):
        """Speichert den vorhandenen E-Mail-Dienst."""
        self.email = email

    def send(self, receiver: str, message: str) -> None:
        """Übersetzt send() in send_email()."""
        self.email.send_email(receiver, message)

    def receive(self, receiver: str) -> None:
        """Übersetzt receive() in receive_email()."""
        self.email.receive_email(receiver)


# ============================================================
# Adapter für In-App-Chat
# ============================================================

class ChatAdapter(MessageService):
    """Passt den In-App-Chat an die gemeinsame Schnittstelle an."""

    def __init__(self, chat: InAppChat):
        """Speichert den vorhandenen Chat-Dienst."""
        self.chat = chat

    def send(self, receiver: str, message: str) -> None:
        """Übersetzt send() in post_message()."""
        self.chat.post_message(receiver, message)

    def receive(self, receiver: str) -> None:
        """Übersetzt receive() in read_message()."""
        self.chat.read_message(receiver)


# ============================================================
# Chat-Client
# ============================================================

class ChatClient:
    """Verwendet Nachrichtendienste über eine gemeinsame Schnittstelle."""

    def send_message(
        self,
        service: MessageService,
        receiver: str,
        message: str
    ) -> None:
        """Sendet eine Nachricht über einen beliebigen Dienst."""
        service.send(receiver, message)

    def receive_message(
        self,
        service: MessageService,
        receiver: str
    ) -> None:
        """Empfängt eine Nachricht über einen beliebigen Dienst."""
        service.receive(receiver)


# ============================================================
# Anwendung
# ============================================================

client = ChatClient()

sms = SMSAdapter(SMS())
email = EmailAdapter(Email())
chat = ChatAdapter(InAppChat())


client.send_message(
    sms,
    "01701234567",
    "Hallo per SMS!"
)

client.send_message(
    email,
    "anna@example.com",
    "Hallo per E-Mail!"
)

client.send_message(
    chat,
    "Anna",
    "Hallo im Chat!"
)
========================================================================
# Was macht der Adapter?

# Ohne Adapter hätte dein ChatClient das Problem:

# sms.send_text(...)
# email.send_email(...)
# chat.post_message(...)

# Drei unterschiedliche Schnittstellen.

# Der Adapter macht daraus überall:

# service.send(...)

# Also:

#                   MessageService
#                    send()
#                       ↑
#          ┌────────────┼────────────┐
#          │            │            │
#     SMSAdapter   EmailAdapter   ChatAdapter
#          │            │            │
#          ↓            ↓            ↓
#     send_text()  send_email() post_message()
#          │            │            │
#         SMS          E-Mail       Chat
#
# Adapter = Übersetzer.

# 3. Das Entscheidende im Code

# Zum Beispiel:

# class SMSAdapter(MessageService):

#    def send(self, receiver, message):
#       self.sms.send_text(receiver, message)

# Der ChatClient sagt:

# send()

# Der Adapter übersetzt:

# send()
#  ↓
# SMSAdapter
#  ↓
# send_text()

# Bei E-Mail:

# send()
#  ↓
# EmailAdapter
#  ↓
# send_email()

# Der ChatClient muss davon nichts wissen.

# Der Adapter stellt dem Client eine einheitliche Schnittstelle zur Verfügung und übersetzt deren Aufrufe in die dienstspezifischen Methoden. 
# Dadurch muss der ChatClient nicht wissen, ob im Hintergrund SMS, E-Mail oder In-App-Chat verwendet wird.