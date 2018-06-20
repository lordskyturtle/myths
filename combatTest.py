from combat import Combat
from warrior import Warrior
from mage import Mage
from ranger import Ranger

if __name__ == "__main__":
    testPlayer = Warrior()
    testMonster = Warrior()
    print "You attack a testMonster"
    Combat(Warrior(), testMonster)
    print "You attack a mage"
    Combat(Mage(), Mage())
    print "You attack a Ranger"
    Combat(Mage(), Ranger())
