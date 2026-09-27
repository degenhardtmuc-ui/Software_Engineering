from abc import ABC, abstractmethod


class TV:
    """
    Repräsentiert einen Fernseher.

    Der TV ist der Receiver im Command Pattern.
    Er führt die eigentlichen Aktionen aus:
    einschalten und ausschalten.
    """

    def __init__(self):
        """Initialisiert den Fernseher im ausgeschalteten Zustand."""
        self.is_on = False

    def on(self):
        """Schaltet den Fernseher ein."""
        self.is_on = True
        print("TV ist AN")

    def off(self):
        """Schaltet den Fernseher aus."""
        self.is_on = False
        print("TV ist AUS")


class Command(ABC):
    """
    Abstrakte Basisklasse für alle Commands.

    Jeder konkrete Command muss execute() und undo()
    implementieren.
    """

    @abstractmethod
    def execute(self):
        """Führt den Command aus."""
        pass

    @abstractmethod
    def undo(self):
        """Macht den Command rückgängig."""
        pass


class TVOnCommand(Command):
    """
    Konkreter Command zum Einschalten des Fernsehers.
    """

    def __init__(self, tv):
        """
        Erstellt einen TVOnCommand.

        Args:
            tv (TV): Der Fernseher, auf dem der Command arbeitet.
        """
        self.tv = tv
        self.previous = None

    def execute(self):
        """
        Speichert den vorherigen Zustand und schaltet den TV ein.
        """
        self.previous = self.tv.is_on
        self.tv.on()

    def undo(self):
        """
        Stellt den vorherigen Zustand des Fernsehers wieder her.
        """
        if self.previous:
            self.tv.on()
        else:
            self.tv.off()


class TVOffCommand(Command):
    """
    Konkreter Command zum Ausschalten des Fernsehers.
    """

    def __init__(self, tv):
        """
        Erstellt einen TVOffCommand.

        Args:
            tv (TV): Der Fernseher, auf dem der Command arbeitet.
        """
        self.tv = tv
        self.previous = None

    def execute(self):
        """
        Speichert den vorherigen Zustand und schaltet den TV aus.
        """
        self.previous = self.tv.is_on
        self.tv.off()

    def undo(self):
        """
        Stellt den vorherigen Zustand des Fernsehers wieder her.
        """
        if self.previous:
            self.tv.on()
        else:
            self.tv.off()


class RemoteControl:
    """
    Repräsentiert den Invoker im Command Pattern.

    Die Fernbedienung führt Commands aus und merkt sich
    den zuletzt ausgeführten Command für Undo.
    """

    def __init__(self):
        """Initialisiert die Fernbedienung."""
        self.command = None
        self.last_command = None

    def set_command(self, command):
        """
        Setzt den aktuell auszuführenden Command.

        Args:
            command (Command): Der gewünschte Command.
        """
        self.command = command

    def press_button(self):
        """
        Führt den aktuell gesetzten Command aus.
        """
        if self.command is None:
            print("Kein Command gesetzt.")
            return

        self.command.execute()
        self.last_command = self.command

    def undo(self):
        """
        Macht den zuletzt ausgeführten Command rückgängig.
        """
        if self.last_command is None:
            print("Nichts rückgängig zu machen.")
            return

        self.last_command.undo()


# -------------------------------------------------
# Test / Client
# -------------------------------------------------

tv = TV()

tv_on = TVOnCommand(tv)
tv_off = TVOffCommand(tv)

remote = RemoteControl()

remote.set_command(tv_on)
remote.press_button()

remote.set_command(tv_off)
remote.press_button()

remote.undo()


=============================================

# Was passiert beim undo()?

# Nach:

# remote.set_command(tv_off)
# remote.press_button()

# war der letzte Command:

# TVOffCommand

# Also macht:

# remote.undo()

# den TVOffCommand rückgängig und stellt den vorherigen Zustand wieder her:

# TV ist AN
# Die Rollen
# TV → Receiver
# Command → Interface / abstrakte Basisklasse
# TVOnCommand → Concrete Command
# TVOffCommand → Concrete Command
# RemoteControl → Invoker
# Testcode unten → Client

# Der passende Kurzsatz für den Kurs ist:

# „Die Fernbedienung kennt nicht direkt tv.on() oder tv.off(), sondern arbeitet nur mit Commands. 
# Dadurch wird die konkrete Aktion gekapselt.