from item import Item

class Inventory():

    def __init__(self):
        self.inventory = {}


    def add(self, item, quantity = 1):
        # if item.name in self.inventory.keys():
        #     self.inventory[item.name].quantity += quantity
        # else:
        #     self.inventory[item.name] = item
        #     self.inventory[item.name].quantity = quantity
        if item.isStackable() == True:
            if item.name in self.inventory.keys():
                self.inventory[item.name].quantity += quantity
            else:
                self.inventory[item.name] = item
                self.inventory[item.name].quantity = quantity
            return
        self.inventory[item.name] = item
        self.inventory[item.name].quantity = quantity



    def remove(self, item):
        if item.name in self.inventory.keys():
            if self.inventory[item.name].undroppable:
                return False
            self.inventory[item.name].quantity -= 1
            if self.inventory[item.name].quantity < 1:
                self.inventory.pop(item.name)
            return True
        return False


    def list(self):
        return_value = ""
        for item_key in self.inventory.keys():
            item = self.inventory[item_key]
            if item.quantity > 1:
                return_value += "%s %s\n" % (item.quantity, item.name)
            else:
                return_value += item.name
        return return_value

    def dump(self):
        retval = ""
        for item_key in self.inventory.keys():
            retval += self.inventory[item_key].info()
        return retval

    def find(self, item):
        if item.name in self.inventory.keys():
            return True
        return False

    def get(self, item):
        if self.find(item) == True:
            return self.inventory[item.name]


        

