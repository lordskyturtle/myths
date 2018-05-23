# World
from room import Room
from inventory import Inventory
from item import Item
from direction import Direction
from monster import Monster
from key import Key
from connection import Connection


class World():
    
    def __init__(self):
        self.room = {
            0 : self.shack(),
            1 : self.bedroom(),
            2 : self.bedroom2(),
            3 : self.kitchen()
        }
        self.location = 0

    def shack(self):
        room = Room()
        lantern = Item('lantern')
        lantern.effects['description'] = 'You would light up the room but the lantern was too sick.'
        room.inventory.add(lantern)
        kitchenKey = Item("kitchen key")
        kitchenKey.shortname = 'key'
        kitchenKey.key = Key("kitchen key", "The door is unlocked.")
        kitchenKey.effects['description'] = "It's a key to the kitchen."
        room.inventory.add(kitchenKey)
        room.long_description = """You are in a small shack. It has a creaky floor, leaky roof and you are scared.oh not of the room but the cage with a lion in it."""
        room.short_description = """A small wooden shack."""
        room.name = "Shack"
        #room.exits = {'e': 1, 'w': -3}
        room.exits = {'e': Connection(1), 'w': Connection(3,'kitchen door','locked',kitchenKey,'The kitchen door is firmly locked. There should be a key somewhere around.') }
        #room.locked = {'w': }
        room.monster = Monster('orc', 5, 10, 1)
        return room

    def bedroom(self):
        room = Room()
        hairBrush = Item('hair brush')
        hairBrush.effects['description'] = 'You brush your hair. That\'s it.'
        room.inventory.add(hairBrush)
        giantBear = Item('a giant stuffed bear')
        giantBear.movable = False
        giantBear.messages['nopickup'] = 'You would pick it up but its too big and would probably eat you. Wait you mean the stuffed bear? It\'s too big.'
        room.inventory.add(giantBear)
        room.long_description = """You stand in a bedroom. You at least assume it is a bedroom because of the bed. Although the giant bear might make sleeping a bit difficult.oh yeah the its a stuffed bear."""
        room.short_description = """A bedroom"""
        room.name = "Bedroom"
        room.exits = {'n': Connection(2), 'w': Connection(0) }

        #room.exits = {'w': 0,'n': 2}
        return room


    def bedroom2(self):
        room = Room()
        skittles = Item('a packet of skittles')
        skittles.effects['healing'] = 5
        room.inventory.add(skittles)
        room.long_description = """It's another bedroom. With another bed. The bed appears to be asleep."""
        room.short_description = """Another bedroom."""
        room.name = "Bedroom"
        room.exits = {'s': Connection(1) }
        #room.exits = {'s': 1}
        return room

    def kitchen(self):
        room = Room()
        moldyCheese = Item('moldy cheese')
        moldyCheese.movable = True
        moldyCheese.effects['healing'] = 5
        room.inventory.add(moldyCheese)
        badApple = Item('bad apple')
        badApple.effects['description'] = 'It sports a biker jacket and surprisingly no motorcycle until you remember that the cat might have eaten it.By the way the cat is an alien.'
        room.inventory.add((badApple))
        wierdThing = Item('???')
        wierdThing.movable = False
        wierdThing.messages['nopickup'] = "You do NOT want to pick that up. Really you don't."
        room.inventory.add((wierdThing))
        room.long_description = """You think it's a kitchen but its hard to tell because it also could be a pet room, for aliens, which the room is full of."""
        room.short_description = """An old kitchen."""
        room.name = "Kitchen"
        room.exits = {'e': Connection(0) }        
        #room.exits = {'e': 0}
        return room

    def showInventory(self):
        room = self.room[self.location]
        return_value = ""
        inventory = room.inventory.inventory
        for thing in inventory.keys():
            item = inventory[thing]
            return_value += ("%s %s \n" % (item.name.capitalize(), item.quantity))
        return return_value


    def getItem(self, item):
        return self.room[self.location].inventory.get(item)

    def hasItem(self, item):
        inventory = self.room[self.location].inventory
        return inventory.find(item)

    def removeItem(self,item):
        return self.room[self.location].inventory.remove(item)

    def look(self, long_description=False):
        if not long_description:
            output = (self.room[self.location].short_description)
            output = output + "\n" + self.showInventory()
            return output
        else:
            return (self.room[self.location].long_description)

    def listExits(self):
        return(self.room[self.location].listExits())
    
    def move(self, direction):
        room = self.room[self.location]
        if len(room.exits) > 0:
            if direction in room.exits:
                if room.exits[direction].state == 'locked':
                    return room.exits[direction].locked
                self.location = room.exits[direction].room_id
                # replace with a proper move()
                return self.look(True) + "\n" + self.showInventory()
            else:
                return "There is nothing there."
        else:
            return "There are no exits."

    def moveNorth(self):
        return self.move('n')

    def moveSouth(self):
        return self.move('s')

    def moveEast(self):
        return self.move('e')

    def moveWest(self):
        return self.move('w')

    def dump(self):
        here = self.room[self.location]
        dump = "%s\n%s\n" % ( here.__dict__, here.inventory.dump())
        return dump
