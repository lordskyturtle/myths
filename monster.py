from character import Character

class Monster(Character):
    
    def __init__(self, name, attack, damage, health):
        self.name = name
        self.attack = 0
        self.health = 0
        self.damage = 0
