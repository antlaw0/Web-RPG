"""
Entity types:
0. Character
1. Friendly NPC
2. Hostile NPC
"""

class Entity(object):
	name=""
	description=""
	level=1
	
	maxhp=1
	hp=maxhp
	maxsp=1
	sp=maxsp
	maxmp=1
	mp=maxmp
	equipment=[]
	strength=1
	dexterity=1
	agility=1
	intelligence=1
	willpower=1
	charisma=1
	leftHand=None
	rightHand=None
	head=None
	equipment.append(head)
	body=None
	equipment.append(body)
	legs=None
	equipment.append(legs)
	arms=None
	feet=None
	equipment.append(feet)
	skill=[]
	for i in range(20):
		skill.append(0)
	
	def __init__(self, name, shortDescription, longDescription, type, subType, h, s, m, strength, dexterity, agility, intelligence, willpower, charisma):
		self.name=name
		self.shortDescription=shortDescription
		self.longDescription=longDescription
		self.type=type
		self.subType=subType
		self.ap=1
		self.maxhp=h
		self.hp=h
		self.maxsp=s
		self.sp=s
		self.maxmp=m
		self.mp=m
		self.strength=strength
		self.dexterity=dexterity
		self.agility=agility
		self.intelligence=intelligence
		self.willpower=willpower
		self.charisma=charisma
		self.inventory=[]
		self.xp=0
		
	def showStats(self):
		string=""
		string+="Name:  "+self.name+"<br>"
		string+=self.shortDescription+"<br>"
		string+="Level:  "+str(self.level)+"<br>"
		string+="HP:  "+str(self.hp)+" \ "+str(self.maxhp)+"<br>"
		string+="SP:  "+str(self.sp)+" \ "+str(self.maxsp)+"<br>"
		string+="MP:  "+str(self.mp)+" \ "+str(self.maxmp)+"<br>"
		string+="Strength:  "+str(self.strength)+"<br>"
		string+="Dexterity:  "+str(self.dexterity)+"<br>"
		string+="Agility:  "+str(self.agility)+"<br>"
		string+="Intelligence:  "+str(self.intelligence)+"<br>"
		string+="Charisma:  "+str(self.charisma)+"<br>"
		string+="Willpower:  "+str(self.willpower)+"<br>"
		return string
	
	def showEquipment(self):
		eq=""
		eq+=self.name+"'s Equipment:  <br>"
		if self.leftHand == None:
			eq+="Left hand:  none <br>"
		else:
			eq+="Left hand: "+self.leftHand.name+"<br>"
		if self.rightHand == None:
			eq+="Right hand:  none <br>"
		else:
			eq+="Right hand: "+self.rightHand.name+"<br>"
		if self.head == None:
			eq+="Head:  none <br>"
		else:
			eq+="Head: "+self.head.name+"<br>"
		if self.body == None:
			eq+="Body:  none <br>"
		else:
			eq+="Body: "+self.body.name+"<br>"
		if self.arms == None:
			eq+="Arms:  none <br>"
		else:
			eq+="Arms: "+self.arms.name+"<br>"
		if self.legs == None:
			eq+="Legs:  none <br>"
		else:
			eq+="Legs: "+self.legs.name+"<br>"
		if self.feet == None:
			eq+="Feet:  none <br>"
		else:
			eq+="Feet: "+self.feet.name+"<br>"
		return eq
		
	def showInventory(self):
		inv=""
		inv+=self.name+"'s inventory: <br>"
		n=1
		for i in self.inventory:
			if i.equipped == True:
				e="(equipped)"
			else:
				e=""
			inv+=str(n)+". "+i.name+" "+str(i.quantity)+" "+e+"<br>"
			n+=1
		return inv
		
	def equipFeet(self, obj):
		if self.feet != None:
			self.feet=obj
			obj.equipped=True
		else:
			self.feet.equipped=False
			self.feet=obj
			obj.equipped=True
	
	def equipLegs(self, obj):
		if self.legs != None:
			self.legs=obj
			obj.equipped=True
		else:
			self.legs.equipped=False
			self.legs=obj
			obj.equipped=True
		
	def equipBody(self, obj):
		if self.body != None:
			self.body.equipped=False
			self.body=obj
			self.body.equipped=True
		else:
			self.body=obj
			self.body.equipped=True
	
	def equipWeapon(self, obj):
		if obj.hands == 1:
			if self.rightHand == None:
				self.rightHand = obj
				obj.equipped=True
				return self.name+" equips "+obj.name+" in right hand."
			elif self.leftHand == None:
				self.leftHand = obj
				obj.equipped=True
				return self.name+" equips "+obj.name+" in left hand."
		else: #must be two-handed
			if self.leftHand == None and self.rightHand == None:
				self.rightHand = obj
				self.leftHand = obj
				obj.equipped = True
				return self.name+" equips "+obj.name
			else: #does not have both hands empty
				return self.name+" needs both hands empty to equip this weapon."
			
				
	
	def hasCurrency(self):
		found=False
		for i in self.inventory:
			if i.type == 0 and i.subType == 0:
				#this is gold
				found=True
				break
		return found
		
	def getCurrency(self):
		for i in self.inventory:
			if i.type == 0 and i.subType == 0:
				return i
	def getPhysDef(self):
		total=0
		if self.head != None:
			total+=self.head.physdef
		if self.body != None:
			total+=self.body.physdef
		if self.arms != None:
			total+=self.arms.physdef
		if self.legs != None:
			total+= self.legs.physdef
		if self.feet != None:
			total+= self.feet.physdef
		
		return total