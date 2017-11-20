import inventoryObject

class Weapon(inventoryObject.inventoryObject):
	
	def __init__(self, name, description, subType, weight, value, damage, range):
		self.name=name
		self.description=description
		self.type=2
		self.subType=subType
		self.weight=weight
		self.value=value
		self.damage=damage
		self.range=range
		self.equipped=False
		
	def examine(self):
		return self.name+"<br> "+self.description+"<br> Damage: "+str(self.damage)+"<br> Weight: "+str(self.weight)+"<br> Value: "+str(self.value)+"<br> Range: "+str(self.range)