# Web-RPG
Flask web app rpg game (Software development Projects class MCTC)
This is a role-playing game. You control a group of adventurers in a medieval fantasy world as they gain experience, level up, and obtain items. The game uses a command interface where you input different commands:
start
This command starts the messages showing on login
direction
Typing north, south, east, or west (or n, s, e, w for short) moves the party in that direction if they are able to move in that direction
<character name> look
This command tells the corresponding character to look at their environment. This is useful to get more information about your surroundings.
<character name> look <object>
This command tells the corresponding character to look at the given object. This is useful to get more information about that object.
<character name> stats
This commands gives statistics about the given character such as current HP (health points), SP (stamina points), MP (magic points), as well as other self-explanitory attributes.
<character name> inventory
Shows the inventory of the given character
<character name> examine <inventory slot number>
Tells the given character to examine an item in their inventory more closley.
wait
This command is used to advance game time. Currently, it allows the regaining of action points.
<character name> attack <target number index>
This tells the character to attack the target in the current room with their default attack, either unarmed or with currently equipped weaponary. This expends an action point that can only be regained through the wait command.
<character name> take <item index>
This command tells the current character to take an item from the environment
<character name> drop <item index>
This command tells the character to drop an item from their inventory.
<character name> sayto <target index> word
This command tells the given character to say 'word' to the given character in the environment. Only sentient objects or characters can be talked to and not all characters will respond back.