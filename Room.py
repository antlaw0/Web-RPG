import Entity

class Room(object):
	name = ""
	description = ""
	x = 0
	y = 0
	
	def __init__(self, name, shortDescription, longDescription, x, y):
		self.name = name
		self.shortDescription = shortDescription
		self.longDescription=longDescription
		self.x = x
		self.y = y
		self.thingsInRoom=[]
	
	def showThingsInRoom(self):
		things=""
		n=1
		for o in self.thingsInRoom:
			if isinstance(o,Entity.Entity):
				if o.type == 2: #if hostile
					healthString=" (HP:  "+str(o.hp)+" \ "+str(o.maxhp)+")"
				else:
					healthString=""
			else:
				healthString=""
			things+=str(n)+". <u>"+o.shortDescription+healthString+"</u> <br>"
			n+=1
		return things
	