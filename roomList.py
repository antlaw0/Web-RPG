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



