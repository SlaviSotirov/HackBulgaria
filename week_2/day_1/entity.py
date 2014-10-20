from weapon import Weapon


class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, dmg):
        if self.health < dmg:
            self.health = 0
        else:
            self.health -= dmg

    def take_healing(self, hp):
        if self.health > 0:
            if self.health + hp > self._MAX_HEALTH:
                self.health = self._MAX_HEALTH
            else:
                self.health += hp
            return True
        else:
            return False

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def has_weapon(self):
        if self.weapon is not None:
            return True
        else:
            return False
