# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.

locations = {0: 'You are sitting in front of a computer learning Python',
             1: 'You are standing at the end of a road before a small brick building',
             2: 'You are are at the top of a hill',
             3: 'You are inside a building, a well house for a small stream',
             4: 'You are in a valley beside a stream',
             5: 'You are in the forest'}

exits = {0: {'Q': 0},
         1: {'N': 5, 'E': 3, 'S': 4, 'W': 2, 'Q': 0},  # Each dictionary represents the paths from a room
         2: {'N': 5, 'Q': 0},
         3: {'W': 1, 'Q': 0},
         4: {'N': 1, 'W': 2, 'Q': 0},
         5: {'S': 1, 'W': 2, 'Q': 0}}

namedExits = {1: {'5': 5, '3': 3, '4': 4, '2': 2},
              2: {'5': 5},
              3: {'1': 1},
              4: {'1': 1, '2': 2},
              5: {'1': 1, '2': 2}}

vocab = {'NORTH':      'N',
         'EAST':       'E',
         'SOUTH':      'S',
         'WEST':       'W',
         'QUIT':       'Q',
         'ROAD':       '1',
         'HILL':       '2',
         'BUILDING':   '3',
         'VALLEY':     '4',
         'FOREST':     '5'}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:
        break
    else:  # Update the exits to include namedExits
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()

    if len(direction) > 1:  # more than one letter, so check vocab
        words = direction.split()  # split the words apart
        for word in words:
            if word in vocab:  # if the typed word is in the vocab, then set the direction
                direction = vocab[word]
                break

    if direction in allExits:  # check the direction is available in the allExits combined dictionary
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")