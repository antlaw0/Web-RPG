import Item

itemList=[]
def createItem(name, shortDescription, longDescription, type, weight, value):
	i=Item.Item(name, shortDescription, longDescription, type, weight, value)
	itemList.append(i)

#create list of items
createItem("Healing Potion", "A red potion.", "It is a small vial of red liquid. Most people would recognize it is a healing potion of some sort.", 0, 1, 50)

def get(id):
	return itemList[id]