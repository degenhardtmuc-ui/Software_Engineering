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