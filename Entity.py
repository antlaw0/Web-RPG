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
	strength=1
	dexterity=1
	agility=1
	intelligence=1
	willpower=1
	charisma=1
	leftHand=None
	rightHand=None
	head=None
	body=None
	legs=None
	arms=None
	feet=None
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