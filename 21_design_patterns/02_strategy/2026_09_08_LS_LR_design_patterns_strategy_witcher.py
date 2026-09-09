from abc import ABC, abstractmethod


class FightStrategy(ABC):
    """Schnittstelle für verschiedene Kampfstrategien."""

    @abstractmethod
    def fight(self) -> None:
        """Führt die jeweilige Kampfstrategie aus."""
        pass


class FightWithSword(FightStrategy):
    """Kampfstrategie für den Kampf mit dem Schwert."""

    def fight(self) -> None:
        """Kämpft mit dem Schwert."""
        print("Der Witcher kämpft mit dem Schwert.")


class FightWithMagic(FightStrategy):
    """Kampfstrategie für den Kampf mit Magie."""

    def fight(self) -> None:
        """Kämpft mit Magie."""
        print("Der Witcher kämpft mit Magie.")


class FightWithCrossbow(FightStrategy):
    """Kampfstrategie für den Kampf mit der Armbrust."""

    def fight(self) -> None:
        """Kämpft mit der Armbrust."""
        print("Der Witcher kämpft mit der Armbrust.")


class Avatar:
    """Spielfigur, deren Kampfstrategie ausgetauscht werden kann."""

    def __init__(self, name: str):
        """Erstellt einen Avatar ohne Kampfstrategie."""
        self.name = name
        self.fight_strategy = None

    def set_fight_strategy(self, strategy: FightStrategy) -> None:
        """Setzt eine neue Kampfstrategie."""
        self.fight_strategy = strategy

    def fight(self) -> None:
        """Führt die aktuell ausgewählte Kampfstrategie aus."""
        if self.fight_strategy:
            self.fight_strategy.fight()


# Anwendung
geralt = Avatar("Geralt")

geralt.set_fight_strategy(FightWithSword())
geralt.fight()

geralt.set_fight_strategy(FightWithMagic())
geralt.fight()

#Der Witcher bleibt derselbe.

#Nur das Verhalten wird ausgetauscht:

#Geralt
#  │
# └── Armbrust