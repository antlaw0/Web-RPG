import Item

class Apparel(Item.Item):
	
	def __init__(self, name, description, type, weight, value, physdef, magdef):
		self.name=name
		self.description=description
		self.type=type
		self.weight=weight
		self.value=value
		self.physdef=physdef
		self.magdef=magdef