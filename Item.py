import inventoryObject

class Item(inventoryObject.inventoryObject):
	
	
	def __init__(self, name, shortDescription, longDescription, type, subType, weight, value):
		self.name=name
		self.shortDescription=shortDescription
		self.longDescription=longDescription
		self.type=type
		self.subType=subType
		self.weight=weight
		self.value=value
		
	