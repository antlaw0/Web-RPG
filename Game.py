import Room
import Entity

#init variables
x=0 #x position of player
y=0 #y position of player
enteredRoom=False

	

#add rooms to map
Room.create_room("Big room", "A big room. This is where you start the game.", 0,0)
Room.create_room("A Small room", "A small room. There is not much in this room, just a wooden table and a lamp giving faint light throughout the room.", -1,0)
Room.create_room("Library", "Rows of dusty tomes line the walls of this old library. A desk and chair are at the far end where presumably people sit and read.", 0,1)
Room.create_room("Dining Room", "An ornate dining room complete with long table with twelve chairs. A vase of flowers are in the center of the table atop a white table cloth.", 1,0)
Room.create_room("Grand Staircase", "You are at the foot of a grand staircase that leads up to the second floor.", 0,-1)

#init first starting room
currentRoom = Room.rooms[0]
party=[]
char1=  Entity.Entity("Char1", "First character", 100, 100, 100, 20, 20, 20, 20, 20, 20)
party.append(char1)
	
#this method reads a string which if it is a vallid command, executes the input command
def processCommand(cmd):
	global currentRoom, x, y
	msg=[]
	cmd=cmd.split(" ")
	
	if len(cmd) ==1 and cmd[0] in ["N", "n", "North", "north", "E", "e", "East", "east", "S", "s", "South", "south", "W", "w", "West", "west"]:
		msg.append(move(cmd[0]))
		
	elif len(cmd) == 2 and cmd[1] == "stats":
		found=False
		for char in party:
			if char.name == cmd[0]:
				msg.append(char.showStats())
				found=True
				break
		if found == False:
			msg.append("Character not in party.")
		
	else:
		msg.append("Command not recognized.")
	#initial messages
	msg.insert(0, str(x)+", "+str(y))
	msg.insert(1, currentRoom.name)
	msg.insert(2, currentRoom.description)
	return msg
	
	
#this method loops through all rooms in the rooms array until it finds the room at the player's x and y position 
def get_room():
	global x, y, enteredRoom
	for i in range(len(Room.rooms)):
		global currentRoom
		r = Room.rooms[i]
		if r.x == x and r.y == y:
			return Room.rooms[i]
			enteredRoom=False
			break

#This method returns whether or not a room exists at given coordinates			
def room_exists(x, y):
	
	roomFound = False
	for i in range(len(Room.rooms)):
		if Room.rooms[i].x==x and Room.rooms[i].y == y:
			roomFound = True
			break
	return roomFound
		
def move(cmd):
	global x,y, currentRoom
	if cmd == "North" or cmd == "north" or cmd == "n":
		if room_exists(x,y-1):
			y-=1
			currentRoom =  get_room()
			return "Moving north."
		else:
			 return "You can't go that way."
	elif cmd == "West" or cmd == "west" or cmd == "w":
		if room_exists(x-1,y):
			x-=1
			currentRoom =  get_room()
			return "Moving west."
		
		else:
			return "You can't go that way."
	elif cmd == "East" or cmd == "east" or cmd == "e":
		if room_exists(x+1,y):
			x+=1
			currentRoom =  get_room()
			return "Moving east."
		
		else:
			return"You can't go that way."
	elif cmd == "South" or cmd == "south" or cmd == "s":
		if room_exists(x,y+1):
			y+=1
			currentRoom =  get_room()
			return "Moving south."
		else:
			return "You can't go that way."
		

	
	