from random import randint


class Fight:
    _HERO_TURN = "Hero's turn"
    _ORC_TURN = "Orc's turn"
    _HERO_WINNER = "Hero wins"
    _ORC_WINNER = "Orc wins"
    _FIGHT_STATUS = "{} dealt {} dmg to {} ({} hp remainining)"

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def _flip_coin(self):
        coin = randint(1, 100)
        if coin <= 50:
            return self._HERO_TURN
        else:
            return self._ORC_TURN

    def simulate_fight(self):
        turn = self._flip_coin()
        afk = ""
        dmg_taken = 0
        if turn == self._HERO_TURN:
            afk = self._ORC_TURN
        else:
            afk = self._HERO_TURN

        print("")
        while self.orc.is_alive() and self.hero.is_alive():
            if turn == self._HERO_TURN:
                dmg_taken = self.hero.attack()
                self.orc.take_damage(dmg_taken)
            else:
                dmg_taken = self.orc.attack()
                self.hero.take_damage(dmg_taken)
            if turn == self._HERO_TURN:
                print(self._FIGHT_STATUS.format(self.hero.name, dmg_taken, self.orc.name, self.orc.get_health()))
            else:
                print(self._FIGHT_STATUS.format(self.orc.name, dmg_taken, self.hero.name, self.hero.get_health()))
            turn, afk = afk, turn

        if self.hero.is_alive():
            print(self._HERO_WINNER + "\n")
            return self._HERO_WINNER
        else:
            print(self._ORC_WINNER + "\n")
            return self._ORC_WINNER
