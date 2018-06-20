from character import Character

class Monster(Character):
    
    def __init__(self, name, attack, defence, health):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
