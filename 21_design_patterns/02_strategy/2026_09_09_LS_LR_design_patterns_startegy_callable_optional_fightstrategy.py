# Strategy Pattern mit Optional

# Jetzt darf der Avatar auch ohne Strategie erstellt werden.

from typing import Callable, Optional


# Typdefinition für eine Kampfstrategie
FightStrategy = Callable[[], None]


def fight_with_sword() -> None:
    """Führt einen Kampf mit dem Schwert aus."""
    print("Fight with Sword")


def fight_with_bow() -> None:
    """Führt einen Kampf mit dem Bogen aus."""
    print("Fight with Bow")


class Avatar:
    """Repräsentiert einen Avatar mit optionaler Kampfstrategie."""

    def __init__(
        self,
        name: str,
        fight_strategy: Optional[FightStrategy] = None
    ):
        """
        Erstellt einen Avatar.

        Eine Kampfstrategie kann angegeben werden,
        muss aber nicht vorhanden sein.
        """
        self.name = name
        self.fight_strategy = fight_strategy

    def fight(self) -> None:
        """
        Führt die aktuelle Kampfstrategie aus.

        Wenn keine Strategie vorhanden ist,
        kämpft der Avatar mit bloßen Händen.
        """
        if self.fight_strategy is not None:
            self.fight_strategy()
        else:
            print(f"{self.name} kämpft mit bloßen Händen!")


# Nutzung
hero = Avatar("Arthur")


# 1. Noch keine Strategie
hero.fight()


# 2. Schwert-Strategie zuweisen
hero.fight_strategy = fight_with_sword

hero.fight()


# 3. Strategie wechseln
hero.fight_strategy = fight_with_bow

hero.fight()


# 4. Lambda-Funktion als Strategie
hero.fight_strategy = lambda: print("Fight with Magic")

hero.fight()
===========================================================

# Was bedeutet Optional?

# Diese Zeile:

# fight_strategy: Optional[FightStrategy] = None

# bedeutet:

# „fight_strategy kann eine FightStrategy sein – oder None.“

# Also:

# Optional[FightStrategy]

#        ↓

# FightStrategy ODER None

# Die moderne Schreibweise dafür wäre:

# fight_strategy: FightStrategy | None = None

# Der Unterschied in einem Satz

# Callable beschreibt, was für eine Funktion die Strategie sein muss.

# Optional sagt, dass diese Strategie vorhanden sein kann, aber nicht vorhanden sein muss.

# Merke!:
# Callable = „Welche Funktion darf ich einsetzen?“
# Optional = „Darf auch keine Funktion gesetzt sein?“