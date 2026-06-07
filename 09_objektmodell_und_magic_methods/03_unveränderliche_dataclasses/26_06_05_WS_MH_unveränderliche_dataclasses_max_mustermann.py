# Eine normale Dataclass ist veränderbar und deshalb nicht als dict-Key erlaubt. 
# Mit frozen=True wird sie unveränderlich. 
# Dadurch kann Python sie sicher hashen und als Schlüssel im Dictionary verwenden.


from dataclasses import dataclass


@dataclass
class NameMutable:
    """A normal name object.

    This object can still be changed after it was created.
    Because of that, Python does not allow it as a dictionary key.
    """

    first_name: str
    last_name: str


mutable_name = NameMutable("Max", "Mustermann")

try:
    test_dict = {mutable_name: "first test"}
except TypeError as error:
    print("Normal dataclass cannot be used as dict key:")
    print(error)


@dataclass(frozen=True)
class Name:
    """A simple name object.

    frozen=True means: the object cannot be changed later.
    That makes it safe to use the object as a dictionary key.
    """

    first_name: str
    last_name: str


name = Name("Max", "Mustermann")

name_dict = {name: "This is Max Mustermann"}

print("\nFrozen Name object:")
print(name)

print("\nDictionary:")
print(name_dict)

print("\nValue for key name:")
print(name_dict[name])

try:
    name.first_name = "Moritz"
except Exception as error:
    print("\nFrozen dataclass cannot be changed:")
    print(error)


# Eine normale Dataclass ist veränderbar und deshalb nicht als dict-Key erlaubt. 
# Mit frozen=True wird sie unveränderlich. 
# Dadurch kann Python sie sicher hashen und als Schlüssel im Dictionary verwenden.