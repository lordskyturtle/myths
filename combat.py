from monster import Monster
from character import Character

class Combat:

    def __init__(self, monster, character):
        self.monster = monster
        self.character = character
        self.combat = True
        self.option_string = {
            'A' : 'attack',
            'D' : 'defend',
            'R' : 'run away',
            'S' : 'spell'
        }
        self.main()

    def main(self):
        # input
        # what do you want to do 
        # Attack? Defend? Run Away? Spell?
        while combat:
            option = self.getOptions()
            print(option)
            combat = False


    def getOptions(self):
        options = ['attack', 'defend', 'run']
        options_command = ['A', 'D', 'R']
        if self.character.hasMagic():
            options.append('spell')
            options_command.append('S')
        for option in options:
            print(option)
        command = raw_input('>')
        if command in options_command:
            return self.option_string[command]
        if command.lower() in options:
            for option in self.option_string.keys():
                if self.option_string[option] == command.lower():
                    return self.option_string[option]
        return "Nothing found"

