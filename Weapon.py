import inventoryObject

class Weapon(inventoryObject.inventoryObject):
	
	def __init__(self, name, description, type, weight, value, damage, range):
		self.name=name
		self.description=description
		self.type=type
		self.weight=weight
		self.value=value
		self.damage=damage
		self.range=range
		
	def examine(self):
		return self.name+"<br> "+self.description+"<br> Damage: "+str(self.damage)+"<br> Weight: "+str(self.weight)+"<br> Value: "+str(self.value)+"<br> Range: "+str(self.range)