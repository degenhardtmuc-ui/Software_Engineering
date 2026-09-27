# Übungen: Command Pattern

**Ablauf:** Setup ausführen → Aufgabe lesen → TODOs ersetzen → Testzelle ausführen.

- Bearbeite nur die Methoden mit `# TODO`. Lass die Tests unverändert.

- `pass` ist ein Platzhalter. Er wird durch deinen Code ersetzt.

- `assert` prüft eine Erwartung. Bei einem Fehler: Meldung lesen, Code korrigieren,

  die geänderte Klassenzelle und danach die Testzelle erneut ausführen.

- Für jede neue Aktion ein neues Command-Objekt erstellen.

- Alle nötigen Klassen stehen hier. Du brauchst keine andere Datei.

Übung und Lösung haben dieselbe Reihenfolge und dieselben Tests.

-Receiever

class Light:

    def __init__(self):

        self.is_on= False

        

    def on(self):

        self.is_on = True

        print("Licht AN")

        

    def off(self):

        self.is_on = False

        print("Licht Aus")

-Command

from abc import ABC, abstractmethod 

class Command(ABC):

    @abstractmethod

    def execute(self):

        pass

    

    @abstractmethod

    def undo(self):

        pass

 

class LightOnCommand(Command):

    def __init__(self, light):

        self.light = light

        self.previous = None

        

    def execute(self):

        self.previous = self.light.is_on

        self.light.on()

        

    def undo(self):

        if self.previous:

            self.light.on()

        else:

            self.light.off()

 

-Invoker

class RemoteContole:

    def __init__(self):

        self.history = []

        

    def press(self, command):

        command.execute()

        self.history.append(command)

        

    def undo(self):

        if not self.history:

            print("Nichts rüchgängig zu machen.")

            return 

        command = self.history.pop()

        command.undo()

from abc import ABC, abstractmethod

 

class Command(ABC):

    @abstractmethod

    def execute(self):

        pass

    @abstractmethod

    def undo(self):

        pass

class Light:

    def __init__(self):

        self.is_on = False

    def on(self):

        self.is_on = True

        print("Licht AN")

    def off(self):

        self.is_on = False

        print("Licht AUS")

class LightOnCommand(Command):

    def __init__(self, light):

        self.light = light

        self.previous = None

    def execute(self):

        # Erst den alten Zustand merken, dann ändern.

        self.previous = self.light.is_on

        self.light.on()

    def undo(self):

        if self.previous:

            self.light.on()

        else:

            self.light.off()

class RemoteControl:

    def __init__(self):

        self.history = []

    def press(self, command):

        command.execute()

        self.history.append(command)

    def undo(self):

        if not self.history:

            print("Nichts rückgängig zu machen.")

            return

        command = self.history.pop()

        command.undo()

==================================================================


from abc import ABC, abstractmethod


# Receiver
class Light:

    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True
        print("Licht AN")

    def off(self):
        self.is_on = False
        print("Licht AUS")


# Command
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete Command
class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light
        self.previous = None

    def execute(self):
        self.previous = self.light.is_on
        self.light.on()

    def undo(self):
        if self.previous:
            self.light.on()
        else:
            self.light.off()


# Invoker
class RemoteControl:

    def __init__(self):
        self.history = []

    def press(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if not self.history:
            print("Nichts rückgängig zu machen.")
            return

        command = self.history.pop()
        command.undo()
====================================================

from abc import ABC, abstractmethod


# ============================================================
# RECEIVER
# ============================================================

class Light:
    """
    Repräsentiert eine Lampe.

    Die Klasse Light ist der Receiver im Command Pattern.
    Sie führt die eigentlichen Aktionen aus:
    Licht einschalten und Licht ausschalten.
    """

    def __init__(self):
        """Initialisiert die Lampe im ausgeschalteten Zustand."""
        self.is_on = False

    def on(self):
        """Schaltet das Licht ein."""
        self.is_on = True
        print("Licht AN")

    def off(self):
        """Schaltet das Licht aus."""
        self.is_on = False
        print("Licht AUS")


# ============================================================
# COMMAND
# ============================================================

class Command(ABC):
    """
    Abstrakte Basisklasse für alle Commands.

    Jeder konkrete Command muss eine execute()- und
    eine undo()-Methode bereitstellen.
    """

    @abstractmethod
    def execute(self):
        """Führt den Command aus."""
        pass

    @abstractmethod
    def undo(self):
        """Macht den Command rückgängig."""
        pass


# ============================================================
# CONCRETE COMMAND
# ============================================================

class LightOnCommand(Command):
    """
    Konkreter Command zum Einschalten einer Lampe.

    Der vorherige Zustand der Lampe wird gespeichert,
    damit der Command später rückgängig gemacht werden kann.
    """

    def __init__(self, light):
        """
        Erstellt einen neuen LightOnCommand.

        Args:
            light (Light): Die Lampe, auf der der Command arbeitet.
        """
        self.light = light
        self.previous = None

    def execute(self):
        """
        Führt den Command aus.

        Zuerst wird der aktuelle Zustand gespeichert.
        Anschließend wird das Licht eingeschaltet.
        """
        self.previous = self.light.is_on
        self.light.on()

    def undo(self):
        """
        Stellt den Zustand vor execute() wieder her.
        """
        if self.previous:
            self.light.on()
        else:
            self.light.off()


# ============================================================
# INVOKER
# ============================================================

class RemoteControl:
    """
    Repräsentiert die Fernbedienung.

    Die Fernbedienung ist der Invoker des Command Patterns.
    Sie führt Commands aus und speichert sie in einer History,
    damit die letzte Aktion rückgängig gemacht werden kann.
    """

    def __init__(self):
        """Initialisiert eine leere Command-History."""
        self.history = []

    def press(self, command):
        """
        Führt einen Command aus und speichert ihn.

        Args:
            command (Command): Der auszuführende Command.
        """
        command.execute()
        self.history.append(command)

    def undo(self):
        """
        Macht den zuletzt ausgeführten Command rückgängig.

        Wenn keine Aktion gespeichert ist, wird eine
        entsprechende Meldung ausgegeben.
        """
        if not self.history:
            print("Nichts rückgängig zu machen.")
            return

        command = self.history.pop()
        command.undo()


===========================================================

from abc import ABC, abstractmethod


# Receiver
class Light:

    def __init__(self):
        self.is_on = False

    def on(self):
        self.is_on = True
        print("Licht AN")

    def off(self):
        self.is_on = False
        print("Licht AUS")


# Command
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete Command: Licht AN
class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light
        self.previous = None

    def execute(self):
        self.previous = self.light.is_on
        self.light.on()

    def undo(self):
        if self.previous:
            self.light.on()
        else:
            self.light.off()


# Concrete Command: Licht AUS
class LightOffCommand(Command):

    def __init__(self, light):
        self.light = light
        self.previous = None

    def execute(self):
        self.previous = self.light.is_on
        self.light.off()

    def undo(self):
        if self.previous:
            self.light.on()
        else:
            self.light.off()


# Invoker
class RemoteControl:

    def __init__(self):
        self.history = []

    def press(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if not self.history:
            print("Nichts rückgängig zu machen.")
            return

        command = self.history.pop()
        command.undo()


# Test
light = Light()
remote = RemoteControl()

remote.press(LightOnCommand(light))
print("Zustand:", light.is_on)

remote.press(LightOffCommand(light))
print("Zustand:", light.is_on)

remote.undo()
print("Nach Undo:", light.is_on)

remote.undo()
print("Nach zweitem Undo:", light.is_on)