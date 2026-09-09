from typing import Callable, Optional

 

# Typ-Definition für eine Funktion ohne Parameter und Rückgabe (None)

FightStrategy = Callable[[], None]

 

 

# Konkrete Strategien als reine Funktionen

def fight_with_sword() -> None:

    print("Fight with Sword..")

 

 

def fight_with_bow() -> None:

    print("Fight with Bow..")

 

 

# Client-Klasse

class Avatar:

 

    def __init__(

        self, name: str, fight_strategy: Optional[FightStrategy] = None

    ):

        self.name = name

        self.fight_strategy: Optional[FightStrategy] = fight_strategy

 

    def fight(self) -> None:

        # Prüfung auf None, da das Attribut Optional ist

        if self.fight_strategy is not None:

            self.fight_strategy()

        else:

            print(f"{self.name} kämpft mit bloßen Händen!")

 

 

# Nutzung

hero = Avatar("Arthur")

# 1. Aufruf ohne gesetzte Strategie (None)

hero.fight()  # Output: Arthur kämpft mit bloßen Händen!

 

# 2. Dynamisches Zuweisen einer Strategie

hero.fight_strategy = fight_with_sword

hero.fight()  # Output: Fight with Sword..

 

# 3. Zuweisen einer Lambda-Funktion als "Quick Fix"

hero.fight_strategy = lambda: print("Fight with Magic..")

hero.fight()  # Output: Fight with Magic..