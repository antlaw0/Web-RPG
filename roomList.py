import Room

rooms=[]
def createRoom(name, description, x,y):
	r = Room.Room(name, description, x,y)
	rooms.append(r)

#add rooms to map
createRoom("Big room", "A big room. This is where you start the game.", 0,0)
createRoom("A Small room", "A small room. There is not much in this room, just a wooden table and a lamp giving faint light throughout the room.", -1,0)
createRoom("Library", "Rows of dusty tomes line the walls of this old library. A desk and chair are at the far end where presumably people sit and read.", 0,1)
createRoom("Dining Room", "An ornate dining room complete with long table with twelve chairs. A vase of flowers are in the center of the table atop a white table cloth.", 1,0)
createRoom("Grand Staircase", "You are at the foot of a grand staircase that leads up to the second floor.", 0,-1)


