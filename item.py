import pprint
from key import Key

class Item():

    def __init__(self, name, undroppable = False):
        self.name = name
        self.undroppable = undroppable
        self.quantity = 1
        self.movable = True
        self.messages = {'test':'test'}
        self.effects = {}

    def __repr__(self):
        return self.name

    def info(self):
        return str(self.__dict__)


    def isMovable(self):
        return self.movable

    def getMessage(self, message, defaultMessage):
        if message in self.messages.keys():
            return(self.messages[message])
        else:
            return(defaultMessage)

    def isStackable(self):
        return True

    def isKey(self):
        if isinstance(self.key, Key):
            return True
        return False

    def unlock(self, target):
        if self.isKey():
            if target.name == self.key.target:
                return self.key.unlocked
        return "Nothing happens"

    def use(self, item):
        return "Interesting stuff happens"