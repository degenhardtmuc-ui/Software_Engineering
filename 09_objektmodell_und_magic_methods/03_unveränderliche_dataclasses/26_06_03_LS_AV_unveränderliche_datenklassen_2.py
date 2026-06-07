from dataclasses import dataclass


@dataclass
class Name:
    first_name: str
    last_name: str


name = Name("John", "Doe")

print(name)
===========================================
# als key in einem dic

phone_book = {
    name: "This is John Doe"
}

print(phone_book)

==============================================
# frozen = True

from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    first_name: str
    last_name: str


name = Name("John", "Doe")

phone_book = {
    name: "This is John Doe"
}

print(phone_book)
print(phone_book[name])