# myList = ['a', 'b', 'c', 'd']
# letters = 'abcdefghijkl'
# numbers = "123456789"
#
# # newString = ''
# # for c in myList:
# #     newString += c + ','  # every time through the loop, it is creating a new variable because strings are immutable
#
# newString = " mississippi, ".join(numbers)  # much more efficient
# print(newString)

locations = {0: 'You are sitting in front of a computer learning Python',
             1: 'You are standing at the end of a road before a small brick building',
             2: 'You are are at the top of a hill',
             3: 'You are inside a building, a well house for a small stream',
             4: 'You are in a valley beside a stream',
             5: 'You are in the forest'}

exits = [{'Q': 0},
         {'N': 5, 'E': 3, 'S': 4, 'W': 2, 'Q': 0},  # Each dictionary represents the paths from a room
         {'N': 5, 'Q': 0},
         {'W': 1, 'Q': 0},
         {'N': 1, 'W': 2, 'Q': 0},
         {'S': 1, 'W': 2, 'Q': 0}]

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()

    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")