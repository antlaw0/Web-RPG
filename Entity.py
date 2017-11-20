class Entity(object):
	name=""
	description=""
	level=1
	exp=0
	maxhp=1
	hp=maxhp
	maxsp=1
	sp=maxsp
	maxmp=1
	mp=maxmp
	inventory=[]
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
	
	def __init__(self, name, description, h, s, m, strength, dexterity, agility, intelligence, willpower, charisma):
		self.name=name
		self.description=description
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
		
	def showStats(self):
		return "Name:  "+self.name+"<br> Description:  "+self.description+"<br> Level:  "+str(self.level)+"<br>HP:  "+str(self.hp)+" \ "+str(self.maxhp)
	
	def showEquipment(self):
		eq=""
		eq+=self.name+"'s Equipment:  <br>"
		for i in self.equipment:
			if i != None:
				eq+=i.name+"<br>"
		return eq
		
	def showInventory(self):
		inv=""
		inv+=self.name+"'s inventory: <br>"
		for i in self.inventory:
			
			inv+=i.name+" "+str(i.quantity)+"<br>"
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