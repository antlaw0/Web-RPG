import Weapon

weaponList=[]
def createWeapon(name, description, type, weight, value, damage, range):
	w=Weapon.Weapon( "Dagger", "A small dagger", 1, 1, 5, 5, 1)
	weaponList.append(w)


#create list of all weapons
createWeapon( "Dagger", "A small dagger", 1, 1, 5, 5, 1)
	
	

def get(id):
	return weaponList[id]