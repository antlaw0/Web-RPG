import Item

itemList=[]
def createItem(name, description, type, weight, value):
	i=Item.Item(name, description, type, weight, value)
	itemList.append(i)

#create list of items
createItem("Healing Potion", "A red potion that heals 25 points of health.", 0, 1, 50)

def get(id):
	return itemList[id]