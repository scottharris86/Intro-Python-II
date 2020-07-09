from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Sword", ""), Item("Bucket", ""), Item("Flashlight", ""), Item("Rope", "")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Gun", ""), Item("Water", ""), Item("Lamp", ""), Item("Spring", "")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Stick", ""), Item("Match", ""), Item("Rock", ""), Item("Rope", "")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Sword", ""), Item("Rock", ""), Item("Lamp", ""), Item("Blanket", "")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Gun", ""), Item("Fish", ""), Item("Ruby", ""), Item("Coin", "")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Scott", room['outside'])

user_input = None
verb = None
object_name = None

while not verb == 'q':
    print(f"your currently in room: {player.current_room.name}")
    print(f"{player.current_room.description}")
    print(f"available items are: {[item.name for item in player.current_room.items]}")
    user_input = input("Enter a Command: [n] move north, [s] move south, [e] move east, [w] move west [get] <item name> [drop] <item name> [i] inventory [q] quit\n")
    split_word = user_input.split(" ")
    verb = split_word[0]
    if len(split_word) > 1:
        object_name = split_word[1]
    # user chooses n
    if verb == 'n':
        if player.current_room.n_to != None:
            # we can move them north
            player.current_room = player.current_room.n_to
        else:
            print("Theres no room in that direction. Try again!")
    # user chooses s
    elif verb == 's':
        if player.current_room.s_to != None:
            # we can move them south
            player.current_room = player.current_room.s_to
        else:
            print("Theres no room in that direction. Try again!")
    # user chooses e
    elif verb == 'e':
        if player.current_room.e_to != None:
            # we can move them east
            player.current_room = player.current_room.e_to
        else:
            print("Theres no room in that direction. Try again!")
    # user chooses w
    elif verb == 'w':
        if player.current_room.w_to != None:
            # we can move them south
            player.current_room = player.current_room.w_to
        else:
            print("Theres no room in that direction. Try again!")
    elif verb == 'q':
        pass

    elif verb == 'get':
        for item in player.current_room.items:
            if item.name == object_name:
                player.current_room.items.remove(item)
                player.items.append(item)
                item.on_take()

    elif verb == 'drop':
        for item in player.items:
            if item.name == object_name:
                player.items.remove(item)
                player.current_room.items.append(item)
                item.on_drop()
    elif verb == "i":
        print(f"inventory: {[item.name for item in player.items]}")
    else:
       print("Unrecognized input. Try again!") 

# user_input = input("Enter a Command: [n] move north, [s] move south, [e] move east, [w] move west [q] quit")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
