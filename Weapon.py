import Item

class Weapon(Item.Item):
	
	def __init__(self, name, description, type, weight, value, damage, range):
		self.name=name
		self.description=description
		self.type=type
		self.weight=weight
		self.value=value