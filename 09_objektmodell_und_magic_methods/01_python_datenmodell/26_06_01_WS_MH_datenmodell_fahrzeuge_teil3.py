class Kfz:
    def __init__(self, hersteller, kennzeichen):
        self.hersteller = hersteller
        self.kennzeichen = kennzeichen

    def __repr__(self):
        return f"Kfz('{self.hersteller}', '{self.kennzeichen}')"

    def __eq__(self, anderes_fahrzeug):
        return self.hersteller == anderes_fahrzeug.hersteller and self.kennzeichen == anderes_fahrzeug.kennzeichen

    def melde_um(self, neues_kennzeichen):
        self.kennzeichen = neues_kennzeichen


bmw = Kfz("BMW", "M-BN 123")
print(bmw)

bmw2 = Kfz("BMW", "M-BN 123")
print(bmw2)

assert bmw == bmw2

vw = Kfz("VW", "WOB-VW 246")
print(vw)

vw.melde_um("BGL-A 9")
print(vw)

assert vw.kennzeichen == "BGL-A 9" and vw.hersteller == "VW"

bmw.melde_um("F-B 21")
print(bmw)

assert bmw != bmw2