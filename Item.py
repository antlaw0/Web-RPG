import inventoryObject

class Item(inventoryObject.inventoryObject):
	
	
	def __init__(self, name, shortDescription, longDescription, type, weight, value):
		self.name=name
		self.shortDescription=shortDescription
		self.longDescription=longDescription
		self.type=0
		self.weight=weight
		self.value=value
		
	