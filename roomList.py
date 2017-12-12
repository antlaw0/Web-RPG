import Room
import Entity
import Item

rooms=[]
	
#add rooms to map
room=Room.Room("Rogue Encampment", "A small encampment.", "This is where you start the game. It is a small encampment in a forest clearing where a few travellers have set up a permanent camp. A few tents and huts circle the perimiter while a large bonfire flanked by some weery travellers sitting on fallen logs.", 0,0)
item=Item.Item("Gold", "A small pile of gold coins are lying on the ground here.", "It is a small pile of gold coins. They look valuable.", 0, 0, 0, 1)
item.quantity=5
room.thingsInRoom.append(item)
entity=  Entity.Entity("Helper Dude", "A helpful looking test entity stands here.", "He is a human male. He seems friendly and willing to assist the developer in testing out certain functions.", 1, 0, 100, 100, 100, 20, 20, 20, 20, 20, 20)

room.thingsInRoom.append(entity)
entity=  Entity.Entity("Goblin", "A menacing looking goblin stands here.", "It appears to be a goblin brandishing a wicked looking dagger. It is bristling and snarling at you.", 2, 0, 25, 50, 15, 10, 25, 25, 10, 10, 10)
entity.xp+=10
room.thingsInRoom.append(entity)

rooms.append(room)
room=Room.Room("Western edge of Rogue Encampment", "A heavily wooded section of forest.", "Trees ranging from ten to fifty feet tall surround you. The smell of earth is strong in the air. You hear sounds of human activity nearby to the east.", -1,0)
rooms.append(room)
room=Room.Room("South of Rogue Encampment", "Heavily wooded section of forest.", "Trees ranging from ten to fifty feet tall surround you. The smell of earth is strong in the air. You hear sounds of human activity nearby to the north.", 0,1)
rooms.append(room)
room=Room.Room("Eastern edge of Rogue Encampment", "Heavily wooded section of forest.", "Trees ranging from ten to fifty feet tall surround you. The smell of earth is strong in the air. You hear sounds of human activity nearby to the west.", 1,0)
rooms.append(room)
room=Room.Room("North of Rogue Encampment","Heavily wooded section of forest.", "Trees ranging from ten to fifty feet tall surround you. The smell of earth is strong in the air. You hear sounds of human activity nearby to the south.",  0,-1)
rooms.append(room)
room=Room.Room("Path to the Castle","Heavily wooded section of forest.", "Trees ranging from ten to fifty feet tall surround you. The smell of earth is strong in the air. You hear sounds of human activity nearby to the south. There is a small trail barely visible leading northward.",  0,-2)
rooms.append(room)
room=Room.Room("Forest trail","Heavily wooded section of forest.", "Trees ranging from ten to fifty feet tall surround you. The smell of earth is strong in the air. You hear sounds of human activity far  to the south. There is a small trail   leading northward. ",  0,-3)
item=Item.Item("Mysterious note", "A piece of parchment is lying on the ground here.", "It is a hastily scrawled note that reads: Help, I am being held prisoner in the castle!", 1, 0, 0, 0)
item.quantity=1
room.thingsInRoom.append(item)
rooms.append(room)

room=Room.Room("Clearing in forest","Heavily wooded section of forest.", "Trees ranging from ten to fifty feet tall surround you. The smell of earth is strong in the air. You hear sounds of human activity far  to the south. You can see a trail in the forest to the west of this clearing. ",  1,-3)
entity=  Entity.Entity("Ogre", "A menacing looking ogre stands here.", "It is a large ogre. It is brandishing a club at you and hurling insults at you. \"I am going to eat you you pathetic worm!\" it shouts at you and your party.", 2, 0, 75, 80, 10, 30, 10, 10, 10, 10, 2)
entity.xp+=20
room.thingsInRoom.append(entity)
rooms.append(room)

room=Room.Room("Before the castle","A small road leading to the castle.", "All the trees have been cleared from this area as a small road leads to a large castle not far to the north. Lights from the castle are visible in the distance. ",  1,-4)
rooms.append(room)



