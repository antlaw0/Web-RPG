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


#list of all apparels
a=Apparel.Apparel("Tunic", "A simple cloth tunic.", "This is a simple cloth tunic that looks like it can fit most humanoid races.", 3, 1, 5, 0, 0)
apparelList.append(a)
a=Apparel.Apparel("Shoes", "A simple pair of shoes", "They are a simple pair of brown, leather shoes worn by most common folk.", 1, 2, 2, 0, 0)
apparelList.append(a)
a=Apparel.Apparel("Hat", "A simple hat", "It is a simple cloth cap worn by most common folk.", 6, 1, 1, 0, 0)
apparelList.append(a)

	

def get(id):
	return apparelList[id]
		