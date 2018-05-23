from inventory import Inventory
from direction import Direction

class Room():

    def __init__(self):
        self.inventory = Inventory()
        self.name = ''
        self.long_description = ''
        self.short_description = ''
        self.exits = {}
        self.monster = None

    def listExits(self):
        return_value = ""
        if len(self.exits) > 0:
            for exit in self.exits:
                direction = Direction(exit)
                if exit < 0:
                    # direction =
                    pass 
                return_value += '%s ' % (direction)
        else:
            return 'No exits. You are stuck.'
        return 'The exits are %s' % (return_value)

    def hasMonster(self):
        if self.monster is not None:
            return True
        return False
