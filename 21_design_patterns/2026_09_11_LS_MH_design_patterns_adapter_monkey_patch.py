class LegacyEmployee:
    """Alte Klasse, die keine name()-Methode besitzt."""

    def __init__(self, first_name: str, last_name: str):
        """Erstellt einen Mitarbeiter."""
        self.first_name = first_name
        self.last_name = last_name


def name(self) -> str:
    """Gibt Vor- und Nachnamen gemeinsam zurück."""
    return f"{self.first_name} {self.last_name}"


# Methode nachträglich hinzufügen
LegacyEmployee.name = name


employee = LegacyEmployee(
    "Max",
    "Mustermann"
)

print(employee.name())


# Die Klasse hatte ursprünglich keine:

#name()

# Methode.

# Wir hängen sie zur Laufzeit nachträglich an:

# LegacyEmployee.name = name

# Das nennt man Monkey Patching.

# Monkey Patching = vorhandenes Verhalten zur Laufzeit verändern oder ergänzen, ohne den ursprünglichen Quellcode direkt zu ändern.