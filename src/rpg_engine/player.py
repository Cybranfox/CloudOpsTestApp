class Player:
    def __init__(self):
        self.hp = 100
        self.xp = 0
        self.mana = 50

    def lose_hp(self, amount):
        self.hp = max(0, self.hp - amount)

    def gain_xp(self, amount):
        self.xp += amount

    def spend_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        return False

    def regenerate_mana(self, amount):
        self.mana = min(50, self.mana + amount)
