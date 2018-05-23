# key
class Key:

    def __init__(self, name, unlocked):
        self.name = name
        # self.description = description
        self.unlocked = unlocked

    def unlock(self):
        return self.unlocked

