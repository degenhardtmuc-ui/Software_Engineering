class FightStrategy:
    def fight(self):
        print("No fight strategy selected")


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
        self.fight_strategy = FightStrategy()

    def set_fight_strategy(self, fight_strategy):
        self.fight_strategy = fight_strategy

    def fight(self):
        self.fight_strategy.fight()


witcher = Avatar("The Witcher")

witcher.set_fight_strategy(FightWithSword())
witcher.fight()

witcher.set_fight_strategy(FightWithMagic())
witcher.fight()

witcher.set_fight_strategy(FightWithGun())
witcher.fight()