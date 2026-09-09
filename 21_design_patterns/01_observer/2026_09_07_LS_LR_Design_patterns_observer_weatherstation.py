from abc import ABC, abstractmethod


# 1. Observer-Interface
class Observer(ABC):

    @abstractmethod
    def update(self, temperature):
        pass


# 2. Subject
class WeatherData:

    def __init__(self):
        self.observers = []
        self.temperature = 0

    def attach(self, observer):
        """Observer anmelden"""
        self.observers.append(observer)

    def detach(self, observer):
        """Observer abmelden"""
        self.observers.remove(observer)

    def notify(self):
        """Alle Observer benachrichtigen"""
        for observer in self.observers:
            observer.update(self.temperature)

    def set_temperature(self, temperature):
        """Wetterdaten ändern"""
        self.temperature = temperature

        # Änderung → alle Observer informieren
        self.notify()


# 3. Konkreter Observer
class WeatherDisplay(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, temperature):
        print(
            f"{self.name}: "
            f"Neue Temperatur = {temperature} °C"
        )


# 4. Anwendung
weather = WeatherData()

display1 = WeatherDisplay("Display 1")
display2 = WeatherDisplay("Display 2")

weather.attach(display1)
weather.attach(display2)

weather.set_temperature(25)