# key
class Key:

    def __init__(self, name, unlocked, target):
        self.name = name
        self.target = target
        # self.description = description
        self.unlocked = unlocked

    def unlock(self):
        return self.unlocked

