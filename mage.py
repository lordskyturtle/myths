from character import Character
from item import Item

class Mage(Character):

    def __init__(self):
        super(Mage, self).__init__()
        self.name = "mage"
        self.attack = 4
        self.max_health = 17
        self.health = 17
        self.defence = 1
        self.description = "You are an arcane wizard with limitless powers of fire and other elements.You destroy your table weekly."
        self.weapon = "staff and magic"
        self.inventory.add(Item('wand', True))
        
