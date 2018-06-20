import sys
from inventory import Inventory
from item import Item
from world import World
from room import Room
from character import Character
from ranger import Ranger
from mage import Mage
from game import Game
from warrior import Warrior


def startgame ():
    print("Welcome to Myths and Monsters!This is a text based game where you type to answer.Now lets begin by picking your class.")
    while 1:
        characterloop()
        print('looping')

def characterloop():
    character = None
    while character is None:
        character = getCharacter()
    print(character.showStats())
    print("Do you want this class.")
    answer = raw_input("yes or no:")
    if answer == 'yes' or answer == 'y':
        dogame(character)
    return 

def getCharacter():
    print("Warrior     Mage     Ranger")
    character = None
    answer = raw_input("Answer:")
    if answer.lower() in ['w','warrior']:
        character = Warrior()
    if answer.lower() in ['m','mage']:
        character = Mage() #Character("mage")
    if answer.lower() in ['r','ranger']:
        character = Ranger() #Character("ranger")
    if answer.lower() in ['quit','q']:
        sys.exit()
    return character

def dogame(character):
    world = World()
    location = 0
    game = Game(character, world, location)
    game.mainLoop()

if __name__ == '__main__':
    startgame()
