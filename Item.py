class Item(object):
	name=""
	description=""
	type=0
	weight=0
	value=0
	quantity=1
	
	
	def __init__(self, name, description, type, weight, value):
		self.name=name
		self.description=description
		self.type=type
		self.weight=weight
		self.value=value
		
	