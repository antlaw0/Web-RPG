import roomList
import Entity
import Item
import Apparel
import Weapon

#init variables
x=0 #x position of player
y=0 #y position of player
enteredRoom=False

	

#Apparel
#a=Apparel.apparel(name, description, type, weight, value, physdef, magdef):

a1= Apparel.Apparel("Clothes", "simple clothes.", 1, 1, 5, 0, 0)
a2=Apparel.Apparel("Shoes", "Simple pair of shoes", 2, 2, 2, 0, 0)
a3=Apparel.Apparel("Hat", "A simple hat", 3, 1, 1, 0, 0)
	
	#Weapons
w1=Weapon.Weapon( "Dagger", "A small dagger", 1, 1, 5, 5, 1)
	
	
#init first starting room
currentRoom = roomList.rooms[0]
party=[]
char1=  Entity.Entity("Char1", "First character", 100, 100, 100, 20, 20, 20, 20, 20, 20)
char1.inventory.append(a1)
char1.inventory.append(w1)
party.append(char1)
char2=  Entity.Entity("Char2", "Second character", 100, 100, 100, 20, 20, 20, 20, 20, 20)
party.append(char2)
	
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
		
	
	elif len(cmd) == 2 and cmd[1] == "inventory":
		found=False
		for char in party:
			if char.name == cmd[0]:
				msg.append(char.showInventory())
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
	for i in range(len(roomList.rooms)):
		global currentRoom
		r = roomList.rooms[i]
		if r.x == x and r.y == y:
			return roomList.rooms[i]
			enteredRoom=False
			break

#This method returns whether or not a room exists at given coordinates			
def room_exists(x, y):
	
	roomFound = False
	for i in range(len(roomList.rooms)):
		if roomList.rooms[i].x==x and roomList.rooms[i].y == y:
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
		

	
	