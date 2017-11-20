import inventoryObject

class Apparel(inventoryObject.inventoryObject):
	
	def __init__(self, name, description, subType, weight, value, physdef, magdef):
		self.name=name
		self.description=description
		self.type=1
		self.subType=subType
		self.weight=weight
		self.value=value
		self.physdef=physdef
		self.magdef=magdef
		self.equipped=False