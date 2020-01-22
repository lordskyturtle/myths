from spellbook import Spellbook
from spell import Spell


if __name__ == "__main__":
	testSpellbook = Spellbook()
	spell = Spell()
	spell.name = "Fireball"
	spell.magic_cost = 10
	spell.effect = 'Healing'
	spell.description = "A firey ball of fire fly from you hands."
	spell2 = Spell()
	spell2.name = "Heading Hands"
	spell2.description = "Your hands tingle with healing energy and stuff"
	testSpellbook.inventory.add(spell)
	testSpellbook.inventory.add(spell2)
	choice = testSpellbook.chooseSpell()
