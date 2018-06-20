class Direction:

    directions = {'e':'East', 'w':'West', 'n':'North', 's':'South'}


    def __init__(self, name):
        self.name = name
   
    def __repr__(self):
        return self.getFullName()

    def getFullName(self):
        if (self.name in self.directions):
            return self.directions[self.name]

    def getName(self):
        return self.name