from monster import Monster
from character import Character
from warrior import Warrior
from random import randint 

class Combat:

    def __init__(self, character, monster):
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
            'spell' : 'S - cast a spell'
        }
        self.commands = {
            'attack' : self.attack,
            'defend' : self.defend,
            'quit' : self.quit,
            'run' : self.run,
            'spell' : self.spell
        }
        self.result = "error"



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
                self.commands[self.option_string[command]]()
                output = ""
                if self.combat == False:
                    break
                self.monsterOptions()
                # player attacks monster defends
                combat_messages = self.doCombat()
                for line in combat_messages:
                    output += line + "\n"
                if self.monster.health <= 0:
                    output += "\n" + self.success()
                    if self.character.health <= 0:
                        self.character.health += 2
                else:
                    if self.character.health <= 0:
                        output += "\n" + self.death()
                print output
        return self.result

    def doCombat(self):
        # init
        # 
        chanceofdefend = 0
        characterdefend = 0
        output = []
        output.append("\n %s is %s \n You are %s \n " % (self.monster.name, self.monsterOption, self.playerOption))
        # set monster defence
        if self.monsterOption == "defending":
            chanceofdefend = self.monster.defence * 5
        if self.monsterOption == "attacking":
            changeofdefend = self.monster.defence
        if self.monsterOption == "running":
            chanceofdefend = 0
        # set player defence
        if self.playerOption == "defending":
            characterdefend = self.character.defence * 10
        if self.playerOption == "attacking":
            characterdefend = self.character.defence
        if self.playerOption == "spelling" or self.playerOption == "running":
            characterdefend = 0

        if self.playerOption == "spelling":
            # if self.player.spellbook.active.effect == heal
            # == attack 
            # == fireball
            # == 

        if self.playerOption == "attacking":
            chance = randint(0,100)
            # if roll is less than the monsters defence then miss
            if chance <= chanceofdefend:
                output.append("You attack but miss")
            else:
                self.monster.health = self.monster.health - self.character.attack
                output.append("You attack and hit the %s for %s damage" % (self.monster.name, self.character.attack))
        
        if self.monsterOption == "attacking":
            chance = randint(0,100)
            # if roll is less than the players defence then miss
            if chance <= characterdefend:
                output.append("\n You defend yourself.\n")
            else:
                self.character.injure(self.monster.attack)
                output.append("\n You got hit for %s \n" % (self.monster.attack) )
        
        if self.playerOption == "defending" and self.monsterOption == "defending":
            output.append("\n A boring interlude occurs where you both cower in fear.\n")

        if self.playerOption == "running":
            chance = randint(0,100)
            if chance >= 50:
                self.combat = False
                self.result = "ran"
                output.append("\nYou ran away. You coward.\n")
            if chance <= 10 and chance >0:
                damage = randint(1,3)
                self.character.injure(damage)
                output.append("\nYou stumble and hurt yourself for %s damage\n" % (damage))
            if chance == 0:
                self.character.injure(100000)
                output.append("You turn, trip and the %s lands on you and crushes you" % (self.monster.name))
        
        if self.playerOption == "fumbling":
            output.append("You either forget you cannot cast any magic or somehow the universe has sapped your magical powers. Either way that doesn't work.")

        if self.monsterOption == "running":
            chance = randint(0,100)
            if chance >= 50:
                self.combat = False
                self.result = "monster ran"
                output.append("\nYou literally scare the poor %s away.\n" %(self.monster.name))


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
        self.playerOption = "running"

    def defend(self):
        self.playerOption = 'defending'

    def attack(self):
        self.playerOption = 'attacking'
        
    def spell(self):
        if self.character.hasMagic():
            self.playerOption = "spelling"
            # todo add a call to self.character.spellbook.choose()
            # this sets the spell in self.character.spellbook.active
        else:
            self.playerOption = "fumbling"
        return

    def monsterOptions(self):
        options = ['attacking', 'defending', 'running']
        which = randint(0,2)
        self.monsterOption = options[which]
        return

    def quit(self):
        self.combat = False
        self.result = "quit"
        return '\nYou quit the game'

    def success(self):
        self.combat = False
        self.result = "monster dead"
        return "\nYou vanquish the monster"

    def death(self):
        self.combat = False
        self.result = "death"
        return "\nYou feel very sleepy. You fall to the ground and the game ends."
