@dataclass
class DependentInit:
    x: InitVar[float] = 0.0
    y: InitVar[float] = 0.0
    z: InitVar[float] = 0.0
    point: Point3D = field(init=False)

    def __post_init__(self, x, y, z):
        self.point = Point3D(x, y, z)

x = DependentInit(22.1, 3, -14.5) 

# Erklärung:
# __post_init__(self, x, y, z) ruft Python automatisch im Hintergrund auf
# darin passiert: self.point = Point3D(x, y, z)
# => x = 22.1, y = 3, z = -14.5

x: InitVar[float]
y: InitVar[float]
z: InitVar[float]
# Diese Werte sind nur für den Start da. Sie werden an __post_init__ übergeben, aber nicht als normale # Attribute gespeichert

# Falsch wäre:
self.x
self.y
self.z

# sondern nur:
self.point

# point: Point3D = field(init=False)
# heißt: point soll zum Objekt gehören, aber ich gebe point nicht direkt beim Erstellen ein
# nicht:
DependentInit(point)
# sondern: 
DependentInit(22.1, 3, -14.5)
# point wird danach automatisch in __post_init__ gebaut

# InitVar benutzt man, wenn Werte nur beim Erstellen gebraucht werden. Diese Werte werden an # #__post_init__ weitergegeben. Mit field(init=False) sagt man: Dieses Attribut wird nicht direkt im
# Konstruktor übergeben, sondern später im Code gesetzt
# oder:
# Ich gebe x, y, z rein, aber gespeichert wird daraus nur ein fertiger Point3D


x = DependentInit(22.1, 3, -14.5)
# x, y, z werden angenommen
__post_init__(22.1, 3, -14.5) wird aufgerufen
self.point = Point3D(22.1, 3, -14.5)

============================================================
# InitVar bedeutet: Der Wert wird nur für die Initialisierung benutzt. Er wird an __post_init__ weitergegeben, aber nicht dauerhaft als normales Attribut im Objekt gespeichert. Mit field(init=False) wird ein Attribut nicht direkt im Konstruktor abgefragt, sondern später im Code gesetzt.

def fakeNew(x, y, z):
    newObject = DependentInit()
    newObject.__init__()


def fakeNew(x, y, z):
    newObject = DependentInit(x, y, z)
    return newObject
    newObject.x = x
    newObject.__post_init__()

===================================================================

@dataclass
class DependentInit:
    x: InitVar[float] = 0.0
    y: InitVar[float] = 0.0
    z: InitVar[float] = 0.0
    point: Point3D = field(init=False)

    def __post_init__(self, x, y, z):
        self.point = Point3D(x, y, z)
