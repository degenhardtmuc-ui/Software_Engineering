from typing import Callable, Optional


FightStrategy = Callable[[], None]


def fight_with_sword() -> None:
    """Führt einen Kampf mit dem Schwert aus."""
    print("Fight with Sword")


def fight_with_magic() -> None:
    """Führt einen Kampf mit Magie aus."""
    print("Fight with Magic")


class Avatar:
    """Avatar mit einer austauschbaren Kampffunktion."""

    def __init__(
        self,
        name: str,
        fight_strategy: Optional[FightStrategy] = None
    ):
        """Erstellt einen Avatar mit optionaler Kampfstrategie."""
        self.name = name
        self.fight_strategy = fight_strategy

    def fight(self) -> None:
        """Führt die aktuell gesetzte Kampfstrategie aus."""
        if self.fight_strategy:
            self.fight_strategy()


# Anwendung
avatar = Avatar("Witcher 3")

avatar.fight_strategy = fight_with_sword
avatar.fight()

avatar.fight_strategy = fight_with_magic
avatar.fight()


#Wichtig!
#avatar.fight_strategy = fight_with_sword

#bedeutet:

#Speichere die Funktion als Strategie.

#Dagegen:

#avatar.fight_strategy = fight_with_sword()

#bedeutet:

#Führe die Funktion jetzt aus und speichere ihr Ergebnis.

#Das wollen wir hier nicht.