# test.py

from room import Room

if __name__ == "__main__":
	r = Room()
	r.exits = {"e" : 1 , 'w' : 2 , 'n' : 3}
	r.listExits()