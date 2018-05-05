from character import Character
from item import Item

class Ranger(Character):

    def __init__(self):
        super(Ranger, self).__init__()
        self.name = "ranger"
        self.attack = 5
        self.max_health = 19
        self.health = 19
        self.defence = 12
        self.magic = 0
        self.description = "You are a well trained ranger with a couple arrows and a sharp eye to defeat all those who stand in his way.Has a phobia of squirrels."
        self.weapon = "bow and knife"
        self.inventory.add(Item('bow',True))
        self.inventory.add(Item('knife',True))
        self.inventory.add(Item('quiver',True))
