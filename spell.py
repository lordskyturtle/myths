from item import Item

class Spell(Item):

    def __init__(self):
        self.magic_cost = 0
        self.option_key = ''

    def isStackable(self):
        return False
