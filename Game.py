import models
from app import db
import roomList
import Entity
import itemList
import apparelList
import weaponList
import Weapon
import Apparel
import random

#init variables
x=0 #x position of player
y=0 #y position of player
enteredRoom=False

#init first starting room
currentRoom = roomList.rooms[0]
party=[]
char1=  Entity.Entity("Char1", "First character", "Here goes the long description", 0, 0, 100, 100, 100, 20, 20, 20, 20, 20, 20)
print(char1.stringifyStats())
char1.inventory.append(apparelList.get(0))
char1.inventory.append(weaponList.get(0))
char1.inventory.append(itemList.get(0))
char1.inventory.append(weaponList.get(1))

party.append(char1)
char2=  Entity.Entity("Char2", "Second character", "Here goes the long description.", 0, 0, 100, 100, 100, 20, 20, 20, 20, 20, 20)
party.append(char2)


def processCommandReturnJSON(cmd):
<<<<<<< HEAD
	return processCommand(cmd)
=======
	#placeholder, obviously replace with your own code
	msg = ['hello', 'turn left', 'you are on the moon']
	return msg
>>>>>>> 6e0dbe70ea54e2eb12557c0321c13bba86d2f66f

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
	elif len(cmd) == 3 and cmd[1] == "unequip":
		msg.append(unequip(cmd[0], cmd[2]))
	elif len(cmd) == 2 and cmd[1] == "equipment":
		msg.append(showEquipment(cmd[0]))
	elif len(cmd) == 1 and cmd[0] == "party":
		msg.append(showParty())
	elif len(cmd) == 3 and cmd[1] == "look":
		msg.append(look(cmd[0], cmd[2]))
	elif len(cmd) == 2 and cmd[1] == "look":
		msg.append(lookRoom())
	elif len(cmd) == 3 and cmd[1] == "attack":
		msg.append(attack(cmd[0], cmd[2]))
	elif len(cmd) == 1 and cmd[0] == "save":
		msg.append(save())
	elif len(cmd) == 3 and cmd[1] == "drop":
		msg.append(drop(cmd[0], cmd[2]))
	elif len(cmd) == 1 and cmd[0] == "wait":
		msg.append(wait())
	elif len(cmd) == 3 and cmd[1] == "examine":
		msg.append(examine(cmd[0], cmd[2]))
	elif len(cmd) == 3 and cmd[1] == "take":
		msg.append(take(cmd[0], cmd[2]))

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




def equipItem(charName, itemNum):
	foundChar=False
	foundItem=False
	itemNum = int(itemNum)
	for char in party:
		if charName == char.name:
			foundChar=True
			break
	if foundChar == False:
		return "Character not in party."

	#if entered index within range of length of char's inventory
	if itemNum <= len(char.inventory) and itemNum > 0:
		i = char.inventory[itemNum-1]
		print("Found "+i.name)
	else:
		return "List index out of range."
	#if item is already equipped
	if i.equipped == True:
		return char.name+" already has "+i.name+" equipped."

	#type 1: apparel, subtype 1: footwear
	elif i.type == 1 and i.subType == 1:
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
	elif i.type == 2:
		return char.equipWeapon(i)
		foundItem=True
		print(char.name+" equips "+i.name)


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


def take(charName, objNum):
	foundChar=False
	for char in party:
		if char.name == charName:
			foundChar = True
			break
	if foundChar == False:
		return "Character not in party."
	else:
		# if entered index is greater zero less than list of things in room
		if int(objNum) <= len(currentRoom.thingsInRoom) and int(objNum) >= 0:
			i=int(objNum)-1
			obj = currentRoom.thingsInRoom[i]
			#if gold
			if obj.type == 0 and obj.subType == 0:
				if char.hasCurrency() == True:
					currencyObject=char.getCurrency()
					currencyObject.quantity+=obj.quantity
				else:
					char.inventory.insert(0, obj)
				currentRoom.thingsInRoom.remove(obj)
			return char.name+" takes "+obj.name
		else:
			return  "List index out of range."


def lookRoom():
	return currentRoom.longDescription

def attack(attackerName, targetNum):
	resultMessage=""
	foundChar=False
	targetNum=int(targetNum)
	for char in party:
		if attackerName == char.name:
			attacker=char
			foundChar=True
	if foundChar == False:
		return "Character not in party."
	foundTarget=False
	#if target index within range
	if targetNum <= len(currentRoom.thingsInRoom) and targetNum > 0 :
		foundTarget = True
		target= currentRoom.thingsInRoom[targetNum-1]
	else:
		foundTarget=False
	if foundTarget == False:
		return "List index out of range."
	if isinstance(target, Entity.Entity) == False:
		return "You cannot attack that."
	#target is an instance of Entity...
	#if target is friendly
	elif target.type == 1:
		return target.name+" is not hostile."
	#target is hostile
	elif target.type == 2:
		return calcDamage(attacker, target)


def calcDamage(attacker, target):
	resultMessage=""
	#does attacker have any action points
	if attacker.ap == 0:
		return attacker.name+" does not have any actions left."
	else:
		#if target is in list of things in room or in party list
		if target in currentRoom.thingsInRoom or target in party:
			resultMessage+=calcLeftHandDamage(attacker, target)
			#if left  hand is not two-handed and attacker has not already attacked with left hand
			if attacker.rightHand != None:
				if attacker.leftHand.hands != 2:

					resultMessage+= calcRightHandDamage(attacker, target)
			#attacker used action point
			attacker.ap-=1
			return resultMessage


def calcRightHandDamage(attacker, target):
	hand = attacker.rightHand
	resultMessage=""
	noMessage=False
	if isinstance(hand, Apparel.Apparel):
		return resultMessage
	elif hand == None:
		handName="unarmed"
		handAttribute=attacker.strength
		handDamage=0
	elif isinstance(hand, Weapon.Weapon):
		#if melee
		handName=hand.name
		handDamage=hand.damage
		if hand.range == 1:
			handAttribute=attacker.strength
		else: #ranged attack
			handAttribute=attacker.dexterity
	dmg = (handDamage + random.randint(0, handAttribute)) - target.getPhysDef()
	#check if negative damage
	if dmg < 0:
		dmg=0
	target.hp-= dmg
	resultMessage+=attacker.name+" attacks "+target.name+" with "+handName+" for "+str(dmg)+" points of damage.<br>"
	if target.hp <= 0 and target in currentRoom.thingsInRoom:
		resultMessage+=target.name+" has been defeated."
		xpAmount=target.xp
		resultMessage+="Party gains "+str(xpAmount)+" experience."
		partyGainXp(xpAmount)
		currentRoom.thingsInRoom.remove(target)
	return resultMessage



def calcLeftHandDamage(attacker, target):
	hand = attacker.leftHand
	resultMessage=""
	noMessage=False
	if isinstance(hand, Apparel.Apparel):
		return resultMessage
	elif hand == None:
		handName="unarmed"
		handAttribute=attacker.strength
		handDamage=0
	elif isinstance(hand, Weapon.Weapon):
		#if melee
		handName=hand.name
		handDamage=hand.damage
		if hand.range == 1:
			handAttribute=attacker.strength
		else: #ranged attack
			handAttribute=attacker.dexterity
	dmg = (handDamage + random.randint(0, handAttribute)) - target.getPhysDef()
	#check if negative damage
	if dmg < 0:
		dmg=0
	target.hp-= dmg
	resultMessage+=attacker.name+" attacks "+target.name+" with "+handName+" for "+str(dmg)+" points of damage.<br>"
	if target.hp <= 0:
		resultMessage+=target.name+" has been defeated."
		xpAmount=target.xp
		resultMessage+="Party gains "+str(xpAmount)+" experience."
		partyGainXp(xpAmount)
		currentRoom.thingsInRoom.remove(target)
	return resultMessage

def partyGainXp(amount):
	chars = len(party)
	eachXP = round(amount/chars,0)
	for char in party:
		char.xp+=eachXP
		print(char.name+" gains "+str(eachXP)+" XP.")

def unequip(charName, slotName):
	foundChar=False
	for char in party:
		if charName == char.name:
			foundChar = True
			break
	if foundChar == False:
		return "Character not in party."
	if slotName == "right" or slotName == "rh" or slotName == "righthand":
		if char.rightHand != None:
			n=char.rightHand.name
			char.rightHand.equipped=False
			char.rightHand = None
			return char.name+" unequips "+n+" from right hand."

		else:
			return char.name+"'s right hand is already empty."
	elif slotName == "left" or slotName == "lh" or slotName == "lefthand":
		if char.leftHand != None:
			n=char.leftHand.name
			char.leftHand.equipped=False
			char.leftHand = None
			return char.name+" unequips "+n+" from left hand."

		else:
			return char.name+"'s left hand is already empty."
	elif slotName == "body":
		if char.body != None:
			char.body.equipped=False
			return char.name+" unequips "+char.body.name+"."
			char.body=None
		else:
			return char.name+"'s body equipment slot is already unequipped."
	elif slotName == "head":
		if char.head != None:
			char.head.equipped=False
			return char.name+" unequips "+char.head.name+"."
			char.head=None
		else:
			return char.name+"'s head equipment slot is already empty."
	elif slotName == "legs":
		if char.legs != None:
			char.legs.equipped=False
			return char.name+" unequips "+char.legs.name+"."
			char.legs=None
		else:
			return char.name+"'s legs equipment slot is already empty."
	elif slotName == "arms":
		if char.arms != None:
			char.arms.equipped=False
			return char.name+" unequips "+char.arms+"."
			char.arms=None
		else:
			return char.name+"'s arms equipment slot is already empty."
	elif slotName == "feet":
		if char.feet != None:
			char.feet.equipped=False
			return char.name+" unequips "+char.feet.name+"."
			char.feet=None
		else:
			return char.name+"'s feet equipment slot is already empty."
	else:
		return slotName+" is not an equipment slot."

def wait():
	for o in currentRoom.thingsInRoom:
		# if object is instance of Entity
		if isinstance(o, Entity.Entity):
			#if entity is hostile
			if o.type == 2:
				#get random target
				targetIndex = random.randint(0, len(party)-1)
				target = party[targetIndex]
				#refresh all party member's action points
				for char in party:
					char.ap=1
				#perform attack calculations
				return calcDamage(o, target)

def drop(charName, itemNo):
	itemNo =int(itemNo)
	foundChar=False
	for char in party:
		if charName == char.name:
			foundChar = True
			break
	if foundChar == False:
		return "Character not in party."
	return char.dropItem(itemNo)

def save():
	c=models.Character(1,char1.stringifyStats(), char2.stringifyStats())
	db.session.add(c)
	db.session.commit()
<<<<<<< HEAD
	return"Save successful"
=======
	return"Save successful"
>>>>>>> 6e0dbe70ea54e2eb12557c0321c13bba86d2f66f
