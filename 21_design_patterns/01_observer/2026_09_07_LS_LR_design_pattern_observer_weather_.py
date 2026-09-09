Observer Interface

==============

public interface Observer {

 

 public void update(Subject subject);

}

==============

Subject Interface

============

public interface Subject {

 

 public void attach(Observer observer);

 public void detach(Observer observer);

 public void notifyAttachedObservers();

 

}

Concrectes Subject = WeatherStation

public class WeatherStation implements Subject{

 

 private int temperature;

 private int pressure; 

 private int humidity;

 private Date time; 

 

 List<Observer> observers;

 

 public WeatherStation() {

  observers = new ArrayList<>();

 }

 

 

 

 public int getTemperature() {

  return temperature;

 }

 

 public void setTemperature(int temperature) {

  this.temperature = temperature;

  notifyAttachedObservers();

 }

 

 public int getPressure() {

  return pressure;

 }

 

 public void setPressure(int pressure) {

  this.pressure = pressure;

  notifyAttachedObservers();

 }

 

 public int getHumidity() {

  return humidity;

 }

 

 public void setHumidity(int humidity) {

  this.humidity = humidity;

  notifyAttachedObservers();

 }

 

 public Date getTime() {

  return time;

 }

 

 public void setTime(Date time) {

  this.time = time;

 }

 public class WeatherDisplay implements Observer {

 

 // Er soll sich bei einem Subject registrieren/deregistrieren. 

 WeatherStation weatherStation;  // Konkretes Subect!

 

 

 

 public WeatherDisplay(WeatherStation weatherStationSubject) {

  this.weatherStation = weatherStationSubject;

 }

 

 public void register() {

  weatherStation.attach(this);

 }

 

 public void deregister() {

  System.out.println("Rufe detach auf..");

  weatherStation.detach(this);

 }

 

 @Override

 public void update(Subject subject) {

  if(weatherStation == subject) {

   show();

  }

  

 }

public void show() {

  int temperature = weatherStation.getTemperature();

  int pressure = weatherStation.getPressure();

  int humidity = weatherStation.getHumidity();

  Date date = weatherStation.getTime();

  

  System.out.println("=========== In show() Methode in WeatherDisplay ===============");

  System.out.println("Display I has received new weather data...");

  System.out.println("Temperature: " + temperature);

  System.out.println("Pressure: " + pressure);

  System.out.println("Humidity: " + humidity);

 }

}

  

 }

// Ein neuer Observer will sich registrien:

 @Override

 public void attach(Observer observer) {

  observers.add(observer);

 }

 // Ein neuer Observer will sich registrien:

 @Override

 public void attach(Observer observer) {

  observers.add(observer);

 }

 

 @Override

 public void detach(Observer observer) {

  System.out.println("Observers vor dem Löschen: " + observers.size() + observers);

  if(observers.indexOf(observer) >= 0)

   observers.remove(observer);

  System.out.println("Observer WeatherDisplayI erfolgreich gelöscht");

  System.out.println("Observers nach dem Löschen: " + observers.size() + observers);

=======================

Concrete Observer = WeatherDisplay

============

 @Override

 public void detach(Observer observer) {

  System.out.println("Observers vor dem Löschen: " + observers.size() + observers);

  if(observers.indexOf(observer) >= 0)

   observers.remove(observer);

  System.out.println("Observer WeatherDisplayI erfolgreich gelöscht");

  System.out.println("Observers nach dem Löschen: " + observers.size() + observers);

=======================
Main Methode

public class Main {

 

 public static void main(String[] args) {

  

  WeatherStation weatherStation = new WeatherStation(); // Concrete-Subect

 WeatherDisplay weatherDisplayI = new WeatherDisplay(weatherStation); //Concrete Observer

  weatherDisplayI.register();

  

  TimeUnit.MILLISECONDS.sleep(2000);

   weatherStation.setTemperature(30);

   

   TimeUnit.MILLISECONDS.sleep(2000);

   weatherStation.setPressure(80);

   

   TimeUnit.MILLISECONDS.sleep(2000);

   weatherStation.setHumidity(40);









=================





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

=========================================================================

from abc import ABC, abstractmethod


class Observer(ABC):
    """Schnittstelle für alle Beobachter."""

    @abstractmethod
    def update(self, temperature: float) -> None:
        """Reagiert auf eine neue Temperatur."""
        pass


class WeatherData:
    """Speichert Wetterdaten und informiert angemeldete Beobachter."""

    def __init__(self):
        """Erstellt eine Wetterstation ohne Beobachter."""
        self.observers = []
        self.temperature = 0.0

    def attach(self, observer: Observer) -> None:
        """Meldet einen neuen Beobachter an."""
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Meldet einen Beobachter wieder ab."""
        self.observers.remove(observer)

    def notify(self) -> None:
        """Benachrichtigt alle angemeldeten Beobachter."""
        for observer in self.observers:
            observer.update(self.temperature)

    def set_temperature(self, temperature: float) -> None:
        """Ändert die Temperatur und informiert die Beobachter."""
        self.temperature = temperature
        self.notify()


class WeatherDisplay(Observer):
    """Zeigt neue Wetterdaten an."""

    def __init__(self, name: str):
        """Erstellt ein Display mit einem Namen."""
        self.name = name

    def update(self, temperature: float) -> None:
        """Zeigt die neue Temperatur an."""
        print(f"{self.name}: {temperature} °C")


# Anwendung
weather = WeatherData()

display1 = WeatherDisplay("Display 1")
display2 = WeatherDisplay("Display 2")

weather.attach(display1)
weather.attach(display2)

weather.set_temperature(25)


WeatherData  = Subject
Display      = Observer

attach()     = anmelden
detach()     = abmelden
notify()     = alle informieren
update()     = auf Änderung reagieren