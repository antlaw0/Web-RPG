class Room(object):
	name = ""
	description = ""
	x = 0
	y = 0
	
	def __init__(self, name, description, x, y):
		self.name = name
		self.description = description
		self.x = x
		self.y = y
	
rooms = []
def create_room(name, description, x, y):
	room = Room(name, description, x, y)
	rooms.append(room)
	return room
	
