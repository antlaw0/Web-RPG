import Apparel

apparelList=[]
def createApparel(name, description, type, weight, value, physdef, magdef):
	a=Apparel.Apparel(name, description, type, weight, value, physdef, magdef)
	apparelList.append(a)


#list of all apparels
createApparel("Clothes", "simple clothes.", 1, 1, 5, 0, 0)
createApparel("Shoes", "Simple pair of shoes", 2, 2, 2, 0, 0)
createApparel("Hat", "A simple hat", 3, 1, 1, 0, 0)
	

def get(id):
	return apparelList[id]
		