import inventoryObject

class Item(inventoryObject.inventoryObject):
	
	
	def __init__(self, name, description, type, weight, value):
		self.name=name
		self.description=description
		self.type=0
		self.weight=weight
		self.value=value
		
	