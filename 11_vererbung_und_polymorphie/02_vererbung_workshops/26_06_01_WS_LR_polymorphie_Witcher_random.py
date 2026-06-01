from abc import ABC, abstractmethod
import random


class FightStrategy(ABC):
    @abstractmethod
    def fight(self):
        pass


class FightWithSword(FightStrategy):
    def fight(self):
        print("Strategy: Fight with Sword")


class FightWithMagic(FightStrategy):
    def fight(self):
        print("Strategy: Fight with Magic")


class FightWithGun(FightStrategy):
    def fight(self):
        print("Strategy: Fight with Gun")


class Avatar:
    def __init__(self, name):
        self.name = name
        self.fight_strategy = None

    def set_fight_strategy(self, fight_strategy):
        self.fight_strategy = fight_strategy

    def set_random_fight_strategy(self):
        strategy_list = [FightWithSword(), FightWithMagic(), FightWithGun()]
        self.fight_strategy = random.choice(strategy_list)

    def fight(self):
        if self.fight_strategy is not None:
            self.fight_strategy.fight()
        else:
            print("No fight strategy selected.")


def main():
    witcher = Avatar("The Witcher")

    # feste Strategie: Sword
    witcher.set_fight_strategy(FightWithSword())
    witcher.fight()

    # feste Strategie: Magic
    witcher.set_fight_strategy(FightWithMagic())
    witcher.fight()

    # feste Strategie: Gun
    witcher.set_fight_strategy(FightWithGun())
    witcher.fight()

    # zufällige Strategie
    witcher.set_random_fight_strategy()
    witcher.fight()


main()