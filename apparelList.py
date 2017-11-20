"""
Apparel sub types:
1=footwear
2=legwear
3=body
5=hands
6=headwear
7=shields
8=necklace
9=ring
10 = 
"""


import Apparel

apparelList=[]
def createApparel(name, description, type, weight, value, physdef, magdef):
	a=Apparel.Apparel(name, description, type, weight, value, physdef, magdef)
	apparelList.append(a)


#list of all apparels
createApparel("Clothes", "simple clothes.", 3, 1, 5, 0, 0)
createApparel("Shoes", "Simple pair of shoes", 1, 2, 2, 0, 0)
createApparel("Hat", "A simple hat", 6, 1, 1, 0, 0)
	

def get(id):
	return apparelList[id]
		