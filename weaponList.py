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
def createWeapon(name, description, subType, weight, value, damage, range):
	w=Weapon.Weapon( "Dagger", "A small dagger", 1, 1, 5, 5, 1)
	weaponList.append(w)


#create list of all weapons
createWeapon( "Dagger", "A small dagger", 1, 1, 5, 5, 1)
	
	

def get(id):
	return weaponList[id]