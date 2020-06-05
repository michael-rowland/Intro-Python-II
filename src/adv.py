from textwrap import wrap

from item import Item
from player import Player
from room import Room


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
     falling into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
     west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by earlier
     adventurers. The only exit is to the south."""),
}

items = {
    'key': Item("key", "this should unlock something"),
    'map': Item("map", "directions to something mysterious"),
}

# Link rooms together
room['outside'].connections["n"] = room['foyer']
room['foyer'].connections["s"] = room['outside']
room['foyer'].connections["n"] = room['overlook']
room['foyer'].connections["e"] = room['narrow']
room['overlook'].connections["s"] = room['foyer']
room['narrow'].connections["w"] = room['foyer']
room['narrow'].connections["n"] = room['treasure']
room['treasure'].connections["s"] = room['narrow']

# Populate items
room['overlook'].items = [items['key']]
room['foyer'].items = [items['map']]

name = input("Please input your name: ")
player = Player(name, room['outside'])
print(f"Welcome {name}!")

available_commands = {'quit', 'move', 'get', 'take', 'drop', 'i', 'inventory'}


def help_message():
    print('Available commands:')
    for i in available_commands:
        print(f"* {i} ...")


user_is_playing = True
while user_is_playing:
    print(player.current_room.name)

    # IF WE GET TO TREASURE CHAMBER, SUCCESS, QUIT
    if player.current_room.name == 'Treasure Chamber':
        print('Success!')
        user_is_playing = False
        break

    # PRINT ROOM DESCRIPTION
    for line in wrap(player.current_room.description, 40):
        print(line)

    # PRINT ITEMS IN ROOM
    if len(player.current_room.items) > 0:
        print("Items available:")
        for i in player.current_room.items:
            print(i)

    user_input = input('# ')
    instructions = user_input.split(" ")

    if instructions[0] == 'quit':
        print("Quitting")
        user_is_playing = False
    elif instructions[0] == 'move':
        player.move(instructions[1])
    elif instructions[0] in ['get', 'take']:
        player.get(instructions[1])
    elif instructions[0] == 'drop':
        player.drop(instructions[1])
    elif instructions[0] in ['i', 'inventory']:
        player.get_inventory()
    else:
        print("Invalid command")
        help_message()
