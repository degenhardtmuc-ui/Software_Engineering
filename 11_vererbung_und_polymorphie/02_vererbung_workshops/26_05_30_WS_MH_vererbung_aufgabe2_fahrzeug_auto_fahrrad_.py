class Fahrzeug:
    """
    This class represents a general vehicle.
    It stores basic information like manufacturer, model, year and speed.
    """

    def __init__(self, hersteller, modell, baujahr, maximale_geschwindigkeit, aktuelle_geschwindigkeit=0.0):
        """
        The constructor creates a new vehicle object.
        It saves all given values as attributes of the object.
        """
        self.hersteller = hersteller
        self.modell = modell
        self.baujahr = baujahr
        self.maximale_geschwindigkeit = maximale_geschwindigkeit
        self.aktuelle_geschwindigkeit = aktuelle_geschwindigkeit

    def beschleunige(self, wert):
        """
        This method increases the current speed.
        The speed cannot be higher than the maximum speed.
        """
        self.aktuelle_geschwindigkeit += wert

        if self.aktuelle_geschwindigkeit > self.maximale_geschwindigkeit:
            self.aktuelle_geschwindigkeit = self.maximale_geschwindigkeit

    def bremse(self, wert):
        """
        This method decreases the current speed.
        The speed cannot be lower than 0.
        """
        self.aktuelle_geschwindigkeit -= wert

        if self.aktuelle_geschwindigkeit < 0:
            self.aktuelle_geschwindigkeit = 0

    def details(self):
        """
        This method returns general information about the vehicle.
        """
        return (
            f"Hersteller: {self.hersteller}, "
            f"Modell: {self.modell}, "
            f"Baujahr: {self.baujahr}, "
            f"Maximale Geschwindigkeit: {self.maximale_geschwindigkeit} km/h, "
            f"Aktuelle Geschwindigkeit: {self.aktuelle_geschwindigkeit} km/h"
        )


class Auto(Fahrzeug):
    """
    This class represents a car.
    It inherits from Fahrzeug and adds car-specific attributes.
    """

    def __init__(
        self,
        hersteller,
        modell,
        baujahr,
        maximale_geschwindigkeit,
        anzahl_tueren,
        kraftstoffart,
        aktuelle_geschwindigkeit=0.0
    ):
        """
        The constructor creates a new car object.
        First it uses the constructor of the parent class Fahrzeug.
        Then it saves the special car attributes.
        """
        super().__init__(
            hersteller,
            modell,
            baujahr,
            maximale_geschwindigkeit,
            aktuelle_geschwindigkeit
        )

        self.anzahl_tueren = anzahl_tueren
        self.kraftstoffart = kraftstoffart

    def details(self):
        """
        This method returns the basic vehicle information
        and adds car-specific information.
        """
        basisinformationen = super().details()

        return (
            f"{basisinformationen}, "
            f"Anzahl Türen: {self.anzahl_tueren}, "
            f"Kraftstoffart: {self.kraftstoffart}"
        )

    def __repr__(self):
        """
        This method returns a readable representation of the car object.
        It looks similar to the constructor call.
        """
        return (
            f"Auto('{self.hersteller}', '{self.modell}', {self.baujahr}, "
            f"{self.maximale_geschwindigkeit}, {self.anzahl_tueren}, "
            f"'{self.kraftstoffart}', {self.aktuelle_geschwindigkeit})"
        )


class Fahrrad(Fahrzeug):
    """
    This class represents a bicycle.
    It inherits from Fahrzeug and adds bicycle-specific attributes.
    """

    def __init__(
        self,
        hersteller,
        modell,
        baujahr,
        maximale_geschwindigkeit,
        anzahl_gaenge,
        rahmentyp,
        aktuelle_geschwindigkeit=0.0
    ):
        """
        The constructor creates a new bicycle object.
        First it uses the constructor of the parent class Fahrzeug.
        Then it saves the special bicycle attributes.
        """
        super().__init__(
            hersteller,
            modell,
            baujahr,
            maximale_geschwindigkeit,
            aktuelle_geschwindigkeit
        )

        self.anzahl_gaenge = anzahl_gaenge
        self.rahmentyp = rahmentyp

    def details(self):
        """
        This method returns the basic vehicle information
        and adds bicycle-specific information.
        """
        basisinformationen = super().details()

        return (
            f"{basisinformationen}, "
            f"Anzahl Gänge: {self.anzahl_gaenge}, "
            f"Rahmentyp: {self.rahmentyp}"
        )

    def klingel(self):
        """
        This method prints a bicycle bell sound.
        """
        print("Klingeling!")

    def __repr__(self):
        """
        This method returns a readable representation of the bicycle object.
        It looks similar to the constructor call.
        """
        return (
            f"Fahrrad('{self.hersteller}', '{self.modell}', {self.baujahr}, "
            f"{self.maximale_geschwindigkeit}, {self.anzahl_gaenge}, "
            f"'{self.rahmentyp}', {self.aktuelle_geschwindigkeit})"
        )


# ------------------------------------------------------------
# Testbereich für Auto
# ------------------------------------------------------------

mein_auto = Auto("Volkswagen", "Golf", 2020, 220.0, 5, "Benzin")

print("Auto am Anfang:")
print(mein_auto.details())

mein_auto.beschleunige(80)
print("\nAuto nach dem Beschleunigen:")
print(mein_auto.details())

mein_auto.beschleunige(200)
print("\nAuto nach zu starkem Beschleunigen:")
print(mein_auto.details())

mein_auto.bremse(50)
print("\nAuto nach dem Bremsen:")
print(mein_auto.details())

print("\nrepr vom Auto:")
print(repr(mein_auto))


# ------------------------------------------------------------
# Testbereich für Fahrrad
# ------------------------------------------------------------

mein_fahrrad = Fahrrad("Cube", "Aim", 2022, 40.0, 21, "Mountainbike")

print("\nFahrrad am Anfang:")
print(mein_fahrrad.details())

mein_fahrrad.beschleunige(15)
print("\nFahrrad nach dem Beschleunigen:")
print(mein_fahrrad.details())

mein_fahrrad.bremse(20)
print("\nFahrrad nach starkem Bremsen:")
print(mein_fahrrad.details())

print("\nFahrrad klingelt:")
mein_fahrrad.klingel()

print("\nrepr vom Fahrrad:")
print(repr(mein_fahrrad))