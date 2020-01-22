from character import Character
from inventory import Inventory

class Spellbook:
	def __init__(self):
		self.inventory = Inventory()
		self.active = None


	def chooseSpell(self):
		keystopress = {}
		for item in self.inventory.inventory.keys():
			keystopress[item[0]] = item
		print ('Choose a spell to cast ')
		for key in keystopress:
			print "%s - %s" % (key.upper(), keystopress[key])


	def main(self):
		self.choice = False
        # input
        # what do you want to do 
        # Attack? Defend? Run Away? Spell?
        # 
        # while self.choice == False:
        #     options = self.getOptions()
        #     self.outputOptions(options)
        #     command = raw_input('>').strip().lower()
        #     if command in self.option_string.keys():
        #         #print(self.option_string[command])          
        #         self.commands[self.option_string[command]]()
        #         output = ""
        #         if self.combat == False:
        #             break
        #         self.monsterOptions()
        #         # player attacks monster defends
        #         combat_messages = self.doCombat()
        #         for line in combat_messages:
        #             output += line + "\n"
        #         if self.monster.health <= 0:
        #             output += "\n" + self.success()
        #             if self.character.health <= 0:
        #                 self.character.health += 2
        #         else:
        #             if self.character.health <= 0:
        #                 output += "\n" + self.death()
        #         print output
        # return self.result
