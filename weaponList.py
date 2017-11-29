"""
Weapon sub types:
1= dagger
2 = sword
3 = greatsword
4 = battleaxe
5 = warhammer
6= shortbow
7 = longbow
8 = crossbow


"""
import Weapon

weaponList=[]
	

#create list of all weapons
 #args:  (name, shortDescription, longDescription, subType, weight, value, damage, hands, range):
	
w=Weapon.Weapon( "Dagger", "A small dagger", "This is a small, metal dagger approximately 8 inches long with a leather grip.", 1, 1, 5, 5, 1, 1)
weaponList.append(w)
w=Weapon.Weapon( "Battleaxe", "A large battleaxe", "It is a large, two-handed battleaxe with a double-headed blade.", 4, 7, 25, 20, 2, 1)
weaponList.append(w)
	
	

def get(id):
	return weaponList[id]