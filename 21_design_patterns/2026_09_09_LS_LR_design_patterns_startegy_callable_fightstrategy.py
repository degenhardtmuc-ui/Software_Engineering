# Strategy Pattern mit Callable
# Hier wird festgelegt: 
# Eine FightStrategy ist einfach eine Funktion, die keine Argumente benötigt und nichts zurückgibt.


from typing import Callable


# Typdefinition für eine Kampfstrategie
FightStrategy = Callable[[], None]


def fight_with_sword() -> None:
    """Führt einen Kampf mit dem Schwert aus."""
    print("Fight with Sword")


def fight_with_bow() -> None:
    """Führt einen Kampf mit dem Bogen aus."""
    print("Fight with Bow")


class Avatar:
    """Repräsentiert einen Avatar mit austauschbarer Kampfstrategie."""

    def __init__(
        self,
        name: str,
        fight_strategy: FightStrategy
    ):
        """Erstellt einen Avatar mit Name und Kampfstrategie."""
        self.name = name
        self.fight_strategy = fight_strategy

    def fight(self) -> None:
        """Führt die aktuell gesetzte Kampfstrategie aus."""
        self.fight_strategy()


# Nutzung
witcher = Avatar(
    "Witcher",
    fight_strategy=fight_with_sword
)

witcher.fight()


# Strategie dynamisch wechseln
witcher.fight_strategy = fight_with_bow

witcher.fight()
=======================================================

# Was bedeutet Callable?

# FightStrategy = Callable[[], None]

# Ganz simpel:

# FightStrategy muss eine aufrufbare Funktion sein, die keine Parameter erwartet und None zurückgibt.

# Und wichtig:

# fight_strategy=fight_with_sword

# ohne (), weil wir die Funktion übergeben, nicht sofort ausführen.