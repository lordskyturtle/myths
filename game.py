import sys
from inventory import Inventory
from item import Item
from world import World
from room import Room
from character import Character
from ranger import Ranger
from mage import Mage
from warrior import Warrior



class Game:

    def __init__(self, player, world, location):
        self.world = world
        self.usewords = ['with', 'on', 'in']
        self.input = ""
        self.words = []
        self.player = player
        self.location = location
        self.room = self.world.room[location]
        self.commands = {
            'exits': self.world.listExits,
            'ex': self.world.listExits,
            'i': self.player.showInventory,
            'c': self.player.showStats,
            'l': self.world.look,
            'look': self.world.look,
            'desc' : self.world.showInventory,
            'description': self.world.showInventory,
            'e': self.world.moveEast,
            'w': self.world.moveWest,
            'n': self.world.moveNorth,
            's': self.world.moveSouth,
            'q': sys.exit,
            'quit': sys.exit,
            '[': self.player.inventory.dump,
            ']': self.world.dump,
            'h': self.player.showHealth,
            'hurt': self.player.injure,
            'p': self.needTwoWords,
            'pick': self.needTwoWords,
            'get': self.needTwoWords,
            'd': self.needTwoWords,
            'drop': self.needTwoWords,
            'throw': self.needTwoWords,
            'use' : self.needTwoWords,
            'unlock': self.needTwoWords,
        }
        self.multi = {
            'p': self.pickup,
            'pick': self.pickup,
            'get': self.pickup,
            'd': self.drop,
            'drop': self.drop,
            'throw': self.drop,
            'use': self.use,
            'u': self.use,
            'unlock': self.unlock
        }

    def command(self,console_prompt='>'):
        command = raw_input(console_prompt).lower()
        # inject dependency into self
        self.input = command
        # simple verbs
        if command in self.commands:
            return self.commands[command]()
        words = command.split(' ')
        self.words = words
        # if more than one word and its in commands
        if len(words) > 1 and words[0] in self.multi:
            return self.multi[words[0]](words)

    def mainLoop(self):
        print("This would be the intro to the game... enter something...")
        while 1:
            command = self.command('>')
            print(command)
                    
    def pickup(self, words):
        if words[1] == 'up':
            words.pop(1)
        words.pop(0)
        rest = ' '.join(words)
        retval = "Picking up " + rest + "."
        itemtopickup = Item(rest)
        if self.world.hasItem(itemtopickup):
            actualItem = self.world.getItem(itemtopickup)
            if actualItem.isMovable() == True:
                self.world.removeItem(itemtopickup)
                self.player.inventory.add(actualItem)
                return retval
            else:
                return self.world.getItem(itemtopickup).getMessage('nopickup', itemtopickup.name + ' cannot be moved.')                
        else:
            return "you cannot pick up that item."
            
    def drop(self, words):
        words = self.words
        words.pop(0)
        rest = ' '.join(words)
        description = "dropping %s.\n" % (rest)
        itemtodrop = self.player.inventory.remove(Item(rest)) 
        if itemtodrop:
            self.room.inventory.add(itemtodrop)
        else:
            return "%s - you cannot drop that item." % (description)

    def use(self, words):
        retval = ""
        words.pop(0)
        rest = ' '.join(words)
        itemtouse = self.player.inventory.get(Item(rest))
        if itemtouse == None:
            before = ""
            after = ""
            parse_mode = "before"
            discard = False
            for word in words:
                if word in self.usewords and parse_mode == "before":
                    parse_mode = "after"
                    discard = True
                if parse_mode == "before" and discard == False:
                    before += word + " "
                if parse_mode == "after" and discard == False:
                    after += word + " "
                discard = False
            if before != '' and after != '':
                retval += before + " used with " + after
                itemtouse = self.player.inventory.get(Item(before))
                if itemtouse == None:
                    retval += before + " does not exit"
                else:
                    return itemtouse.use(after)
            else:
                retval += "you do not have that item."
        elif 'description' in itemtouse.effects.keys():
            description = itemtouse.effects['description']
            retval += description
        elif 'healing' in itemtouse.effects.keys():
            if self.player.health == self.player.max_health:
                retval += "Your health is already full."
            else:
                healing = itemtouse.effects['healing']
                self.player.health = self.player.health + healing
                retval +=("you used " + itemtouse.name + ".")
                if self.player.health > self.player.max_health:
                   self.player.health = self.player.max_health
                self.player.inventory.remove(itemtouse)
        else:
            return "you cannot use that item"
        return retval

    def needTwoWords(self):
        return "Sorry you need to enter more than one word"

    def unlock(self):
        