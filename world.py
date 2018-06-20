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
            3 : self.kitchen(),
            4 : self.hall(),
            5 : self.corridor(),
            6 : self.armoury(),
            7 : self.banquet_hall(),
            8 : self.kings_hall(),
            9 : self.kings_office(),
            10 : self.kitchen2(),
        }
        self.location = 4
                 

    def shack(self):
        room = Room()
        lantern = Item('lantern')
        lantern.effects['description'] = 'You would light up the room but the lantern was too sick.'
        room.inventory.add(lantern)
        kitchenKey = Item("kitchen key")
        kitchenKey.shortname = 'key'
        kitchenKey.movable = True
        kitchenKey.key = Key("kitchen key", "The door is unlocked.")
        kitchenKey.effects['description'] = "It's a key to the kitchen."
        room.inventory.add(kitchenKey)
        room.long_description = """You are in a small shack. It has a creaky floor, leaky roof and you are scared.oh not of the room but the cage with a lion in it."""
        room.short_description = """A small wooden shack."""
        room.name = "Shack"
        #room.exits = {'e': 1, 'w': -3}
        room.exits = {
                'e': Connection(1), 
                'w': Connection( 3,
                    'kitchen door',
                    'locked',
                    kitchenKey, 
                    'The kitchen door is firmly locked. There should be a key somewhere around.') }
        #room.locked = {'w': }

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
        room.monster = Monster('orc', 5, 10, 1)

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


    def hall(self):
        room = Room()
        room.name = "Hall"
        boot = Item("old boot")
        boot.effects["description"] = "An old boot.We haven't added weapons yet so feel free to not use it as a weapon.Also it would break because it is old."
        room.inventory.add(boot)
        room.long_description = "This is the entrance.Please take some time to appreiciate our lack of graphics."
        room.short_description = "Its the entrance.We told you.Seriously what were you expecting."
        room.exits = {"e": Connection(5)}
        return room



    def corridor(self):
        room = Room()
        room.name = 'corridor'
        boot = Item("old boot")
        boot.effects["description"] = "An old boot.We haven't added weapons yet so feel free to not use it as a weapon.Also it would break because it is old."
        room.inventory.add(boot)
        mould = Item("mould")
        mould.movable = False
        mould.messages["nopickup"] = "Theres too much moss to pick up and you are scared of it because it might consume you."
        room.long_description = "This is a corridor full of armour. Your in a castle by the way."
        room.short_description = "Its a corridor. You expected us to make the same joke and ask what were you expecting.\nThese descriptions are supposed to be shorter but right now they're just as long or longer"
        room.exits = {
        "e": Connection(7),
        "n": Connection(6),
        "w": Connection(4)
        }
        room.monster = Monster("Testmonster", 4, 7, 6)
        return room

    def armoury(self):
        room = Room()
        room.name = 'Armoury'
        key = Item("kitchen key")
        key.effects["description"] = "Its a key to the kitchen."
        key.key = Key("kitchen key", "The kitchen door opens and the beautiful smell of mould fills your nostrils")
        room.inventory.add(key)
        sword = Item("sword")
        sword.movable = False
        sword.messages["nopickup"] = "WE SAID all the weapons have been cursed to never be picked up."
        room.long_description = "Its an armoury. Some how all the weapons have been cursed to never be picked up or equipped, and also to be able to speak."
        room.short_description = "Its an armoury."
        room.exits = {
        "s": Connection(5)
        }
        return room

    def banquet_hall(self):
        room = Room()
        room.name = 'Banquet Hall'
        breadcrumbs = Item("bread crumbs")
        breadcrumbs.effects['description'] = "What are you going to do with BREADCRUMBS!"
        room.inventory.add(breadcrumbs)
        plate = Item("Broken plate")
        plate.movable = False
        plate.messages["nopickup"] = "You are a safe person and know not to pick up broken pottery.\nOr you would be if you had not just asked your character to pick up a broke plate."
        room.inventory.add(plate)
        room.long_description = "A banquet hall complete with the nesessary broken plates and really long broken table just to show that its old."
        room.short_description = "A delicous smelling banquet hall."
        room.exits = {
        "w": Connection(5),
        "e": Connection(8),
        "s": Connection(10, "kitchen", "locked", "kitchen key", "The kitchen is locked. There's a note here saying that the chef has gone to the armoury.")
        }
        return room


    def kitchen2(self):
        room = Room()
        moldyCheese = Item('moldy cheese')
        moldyCheese.movable = True
        moldyCheese.effects['healing'] = 5
        room.inventory.add(moldyCheese)
        cat = Item('cat')
        cat.movable = False
        cat.messages['nopickup'] = 'It seems like a cat but its actually an alien.'
        room.inventory.add((cat))
        wierdThing = Item('???')
        wierdThing.movable = False
        wierdThing.messages['nopickup'] = "Its seems to be a slimy looking thing that is stuck to the floor and tried to eat your hand when you touched it."
        key2 = Item("cake key")
        key2.effects["description"] = "A key the looks like a cake but is actually the key for the kings office."
        key2.key = Key("cake key", "The king's office unlocks.")
        room.inventory.add((wierdThing))
        room.long_description = """It's the castle kitchen but its hard to tell because it also could be a pet room, for aliens, which the room is full of."""
        room.short_description = """An old kitchen, or pet room, for aliens"""
        room.name = "Kitchen"
        room.exits = {'n': Connection(7) }        
        #room.exits = {'e': 0}
        room.monster = Monster("Musclar spoon", 6, 10, 3)
        return room

    def kings_hall(self):
        room = Room()
        room.name = "Kings Throne Room"
        documents = Item("documents")
        documents.effects["description"] = "It says the King had to do a food inspection so he's probably been to the kitchen."
        room.inventory.add(documents)
        room.long_description = "This is the King's throne room. It has his throne and many seats for legal cases."
        room.short_description = "It's the throne room."
        room.exits = {
        "w": Connection(7),
        "n": Connection(9, "kings office", "locked", "cake key", "the door is locked. The king must not want people to go in his office.")
        }
        return room

    def kings_office(self):
        room = Room()
        room.name = "Kings Office"
        boot = Item("old boot")
        boot.effects["description"] = "An old boot.We haven't added weapons yet so feel free to not use it as a weapon.Also it would break because it is old."
        room.inventory.add(boot)
        mould = Item("mould")
        mould.movable = False
        mould.messages["nopickup"] = "Theres too much moss to pick up and you are scared of it because it might consume you."
        room.long_description = "This is the hall.Please take s"
        room.short_description = "Its the hall.We told you.Seriously what were you expecting."
        room.exits = {
        "s": Connection(8)
        }
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
