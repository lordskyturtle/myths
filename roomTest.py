# test.py

from room import Room

if __name__ == "__main__":
	r = Room()
	r.exits = {"e" : 1 , 'w' : 2 , 'n' : 3}
	print(r.listExits())
	if r.hasMonster():
		print "MONSTER"
	else:
		print "NO MONSTER"
	r.monster = {}
	print 'putting a monster in the room'
	if r.hasMonster():
		print "MONSTER"
	else:
		print "NO MONSTER"
	