from monster import Monster
from character import Character
from warrior import Warrior
from random import randint 

class Combat:

    def __init__(self, monster, character):
        self.monster = monster
        self.character = character
        self.combat = True
        self.playerOption = ""
        self.monsterOption = ""
        self.option_string = {
            'a' : 'attack',
            'd' : 'defend',
            'r' : 'run',
            's' : 'spell',
            'cast': 'spell',
            'q': 'quit'
        }
        self.option_descriptions = {
            'attack' : 'A - attack with a weapon',
            'defend' : 'D - defend yourself',
            'run' : 'R - try to run away',
            'spell' : 'S - cast a healing spell'
        }
        self.commands = {
            'attack' : self.attack,
            'defend' : self.defend,
            'quit' : self.quit,
            'run' : self.run,
            'spell' : self.spell
        }
        self.main()

    def main(self):

        # input
        # what do you want to do 
        # Attack? Defend? Run Away? Spell?
        while self.combat == True:
            options = self.getOptions()
            self.outputOptions(options)
            command = raw_input('>').strip().lower()
            if command in self.option_string.keys():
                #print(self.option_string[command])          
                output = self.commands[self.option_string[command]]()
                if self.combat == False:
                    break
                self.monsterOptions()
                # player attacks monster defends
                combat_messages = self.doCombat()
                for lines in combat_messages:
                    output += combat_messages + "\n"
                if self.monster.health <= 0:
                    output += "\n" + self.success()
                    if self.player.health <= 0:
                        self.player.health += 2
                else:
                    if self.player.health <= 0:
                        output += "\n" + self.death()
                print output
            

    def doCombat(self):
        # player defends monster defends
        # player attacks monster attacks
        # player spells monster defends
        # player spells monster attacks
        # player defends monster attacks
        # player runs monster attacks
        # player defends monster runs
        # player runs monster runs
        # player attacks monster runs
        # player runs monster defends
        chanceofdefend = 0
        characterdefend = 0
        output = []
        if self.monsterOption == "defending":
            chanceofdefend = self.monster.defence * 5
        if self.monsterOption == "attacking":
            changeofdefend = self.monster.defence
        if self.monsterOption == "running":
            chanceofdefend = 0

        if self.playerOption == "defending":
            characterdefend = self.character.defence * 5
        if self.playerOption == "attacking":
            characterdefend = self.character.defence
        if self.playerOption == "spelling" or self.playerOption == "running":
            characterdefend = 0

        if self.playerOption == "attacking":
            chance = randint(0,100)
            if chance <= chanceofdefend:
                output[] = "You attack but miss"
            else:
                self.monster.health = self.monster.health - self.character.attack
                output[] = "You attack and hit the %s for %s damage" % (self.monster.name, self.character.attack)
        
        if self.monsterOption == "attacking":
            chance = randint(0,100)
            if chance <= characterdefend:
                output[] = "you defend"
            else:
                self.character.injure(self.monster.attack)
                output[] = "you got hit for %s" %self.monster.attack
        if self.playerOption == "defending" and self.monsterOption == "defending":
            output[] = "A boring interlude where you both cower in fear."
        return output


    def getOptions(self):
        options = ['attack', 'defend', 'run']
        if self.character.hasMagic():
            options.append('spell')     
        return options

    def outputOptions(self,options):
        for o in options:
            print self.option_descriptions[o]    

    def run(self):
        chance = randint(0,100)
        if chance >= 50:
            self.combat = False
            return 'You ran away. You coward.'
        if chance <= 10 and chance >0:
            damage = randint(1,3)
            self.character.injure(damage)
            return "You stumble and hurt yourself for %s damage" % (damage)
        if chance == 0:
            self.character.injure(100000)
            return "You turn, trip and the %s lands on you and crushes you" % (self.monster.name)
        return "You just can't get away."

    def defend(self):
        self.playerOption = 'defending'
        return 'defending'

    def attack(self):
        self.playerOption = 'attacking'
        return 'attacking'
        

    def spell(self):
        self.playerOption = "spell"
        return 'spelling'

    def monsterOptions(self):
        options = ['attacking', 'defending', 'running']
        which = randint(0,2)
        self.monsterOption = options[which]
        return

    def quit(self):
        self.combat = False
        return 'You quit the game'

    def success(self):
        self.combat = False
        return "You vanquish the monster"

    def death(self):
        self.combat = False
        return "You feel very sleepy. You fall to the ground and the game ends."
