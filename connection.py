# connections
class Connection():
    def __init__(self, room_id, name=None, state=None, key=None, locked=None):
        self.room_id = room_id
        self.name = name
        self.state = state
        self.key = key
        self.locked = locked

