from inventory import Inventory
from item import Item


class Character(object):

    def __init__(self):

        self.name = 'Unnamed'
        self.attack = 0
        self.max_health = 0
        self.health = 0
        self.defence = 0
        self.magic = 0
        self.description = ""
        self.weapon = ""
        self.inventory = Inventory()
        self.inventory.add(Item('gold'), 10)

    def hasMagic(self):
        if self.magic > 0:
            return True
        return False

    def showInventory(self):
        return_value = ""
        inventory = self.inventory.inventory
        for thing in inventory.keys():
            item = inventory[thing]
            return_value += ("%s %s \n" % (item.name.capitalize(), item.quantity))
        return return_value

    def showStats(self):
        return_value = "%s You are armed with a %s.\n"
        return_value += "Your attack is %s, defence is %s and health is %s\n" 
        return return_value % ( 
            self.description, 
            self.weapon, 
            self.attack,
            self.defence,
            self.health
        ) + self.showInventory()

    def showHealth(self):
        return "Health: %s\n" % (self.health)


    def injure(self, amount=10):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
