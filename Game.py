import roomList
import Entity
import itemList
import apparelList
import weaponList

#init variables
x=0 #x position of player
y=0 #y position of player
enteredRoom=False

#init first starting room
currentRoom = roomList.rooms[0]
party=[]
char1=  Entity.Entity("Char1", "First character", "Here goes the long description", 0, 0, 100, 100, 100, 20, 20, 20, 20, 20, 20)
char1.inventory.append(apparelList.get(0))
char1.inventory.append(weaponList.get(0))
char1.inventory.append(itemList.get(0))
party.append(char1)
char2=  Entity.Entity("Char2", "Second character", "Here goes the long description.", 0, 0, 100, 100, 100, 20, 20, 20, 20, 20, 20)
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
		
	elif len(cmd) == 3 and cmd[1] == "equip":
		msg.append(equipItem(cmd[0], cmd[2]))
	elif len(cmd) == 2 and cmd[1] == "equipment":
		msg.append(showEquipment(cmd[0]))
	elif len(cmd) == 1 and cmd[0] == "party":
		msg.append(showParty())
	elif len(cmd) == 3 and cmd[1] == "look":
		msg.append(look(cmd[0], cmd[2]))
	elif len(cmd) == 3 and cmd[1] == "examine":
		msg.append(examine(cmd[0], cmd[2]))
	else:
		msg.append("Command not recognized.")
	
	
	#initial messages
	msg.insert(0, str(x)+", "+str(y))
	msg.insert(1, currentRoom.name)
	msg.insert(2, currentRoom.description)
	msg.insert(3, currentRoom.showThingsInRoom())
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
		

	
	
def equipItem(charName, itemName):
	foundChar=False
	foundItem=False
	for char in party:
		if charName == char.name:
			foundChar=True
			break
	if foundChar == False:
		return "Character not in party."
		
	#loop through char's inventory
	for i in char.inventory:
		if i.name == itemName:
			#type 1: apparel, subtype 1: footwear
			if i.type == 1 and i.subType == 1:
				char.equipFeet(i)
				return char.name+" equips  "+char.feet.name
				foundItem=True
			#apparel, legwear
			elif i.type ==1 and i.subType == 2:
				char.equipLegs(i)
				return char.name+" equips "+char.legs.name
				foundItem=True
			elif i.type ==1 and i.subType == 3:
				char.equipBody(i)
				return char.name+" equips "+char.body.name
				foundItem=True
		else:
			return "Item not in "+char.name+"'s inventory."
			
			
def showEquipment(charName):
	foundChar=False
	for char in party:
		if charName == char.name:
			foundChar=True
			break
	if foundChar == False:
		return "Character not in party."
	else:
		return char.showEquipment()
		

		
def showParty():
	p=""
	i=1
	p+="Characters in party: <br>"
	for char in party:
		p+=str(i)+":  "+char.name+"<br>"
		i+=1
	return p
	
def look(charName, objNum):
	foundChar=False
	for char in party:
		if char.name == charName:
			foundChar = True
			break
	if foundChar == False:
		return "Character not in party."
	else:
		foundObj=False
		# if entered index is greater zero less than list of things in room
		if int(objNum) <= len(currentRoom.thingsInRoom) and int(objNum) >= 0:
			i=int(objNum)-1
			description = currentRoom.thingsInRoom[i].longDescription
			return description
		else:
			return  "List index out of range."
		
			

			
def examine(charName, objNum):
	foundChar=False
	for char in party:
		if char.name == charName:
			foundChar = True
			break
	if foundChar == False:
		return "Character not in party."
	else:
		# if entered index is greater zero less than list of things in inventory
		if int(objNum) <= len(char.inventory) and int(objNum) >= 0:
			i=int(objNum)-1
			description = char.inventory[i].longDescription
			return description
		else:
			return  "List index out of range."
		
			
