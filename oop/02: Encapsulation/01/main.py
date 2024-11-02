fireball_damage = 500
potion_mana = 100
fireball_cost = 50


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence

        self.name = name
        self.health = stamina * 100
        self.mana = intelligence * 10

    def cast_fireball(self, target):
        if self.mana >= fireball_cost:
            target.get_fireballed()
            self.mana -= fireball_cost
        else:
            raise Exception(f"{self.name} cannot cast fireball")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_fireballed(self):
        self.health -= fireball_damage

    def drink_mana_potion(self):
        self.mana += potion_mana
