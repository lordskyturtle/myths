from character import Character
from item import Item

class Warrior(Character):

    def __init__(self):
        super(Warrior, self).__init__()
        self.name = "warrior"
        self.attack = 7
        self.max_health = 16
        self.health = 16
        self.defence = 4
        self.description = "You are a huge hulking slab of muscle and reflexes and have trouble with doors."
        self.weapon = "sword"
        self.inventory.add(Item('sword',True))
